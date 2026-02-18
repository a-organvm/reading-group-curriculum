"""CLI for reading-group-curriculum."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import click


@click.group()
def cli():
    """Reading group curriculum management."""


@cli.command("list")
def list_curricula():
    """List all curricula."""
    from .config import Settings
    from .repository import CurriculumRepository

    repo = CurriculumRepository(Settings.require_db())
    curricula = repo.list_curricula()
    if not curricula:
        click.echo("No curricula found. Run 'curriculum seed' first.")
        return
    for c in curricula:
        click.echo(f"  [{c.id}] {c.title} ({c.duration_weeks} weeks, {c.theme})")


@cli.command()
@click.argument("curriculum_id", type=int)
def show(curriculum_id: int):
    """Show details of a curriculum."""
    from .config import Settings
    from .repository import CurriculumRepository

    repo = CurriculumRepository(Settings.require_db())
    c = repo.get_curriculum(curriculum_id)
    if not c:
        click.echo(f"Curriculum {curriculum_id} not found.", err=True)
        sys.exit(1)
    click.echo(f"# {c.title}")
    click.echo(f"Theme: {c.theme}")
    click.echo(f"Duration: {c.duration_weeks} weeks")
    click.echo(f"Description: {c.description}")
    sessions = repo.get_sessions(curriculum_id)
    for s in sessions:
        click.echo(f"  Week {s.week}: {s.title} ({s.duration_minutes}min)")


@cli.command()
@click.argument("curriculum_id", type=int)
@click.option("--format", "fmt", type=click.Choice(["md", "json"]), default="md")
def export(curriculum_id: int, fmt: str):
    """Export a curriculum as markdown or JSON."""
    from .config import Settings
    from .export import export_curriculum_markdown
    from .repository import CurriculumRepository

    repo = CurriculumRepository(Settings.require_db())
    c = repo.get_curriculum(curriculum_id)
    if not c:
        click.echo(f"Curriculum {curriculum_id} not found.", err=True)
        sys.exit(1)
    sessions = repo.get_sessions(curriculum_id)
    data = {
        "title": c.title,
        "theme": c.theme,
        "organ_focus": c.organ_focus,
        "duration_weeks": c.duration_weeks,
        "description": c.description,
        "sessions": [
            {
                "week": s.week,
                "title": s.title,
                "readings": [],
                "questions": [],
                "activities": [],
            }
            for s in sessions
        ],
    }
    if fmt == "md":
        click.echo(export_curriculum_markdown(data))
    else:
        click.echo(json.dumps(data, indent=2, default=str))


@cli.command()
def seed():
    """Seed curricula from koinonia-db seed files."""
    from .config import Settings
    from .repository import CurriculumRepository

    repo = CurriculumRepository(Settings.require_db())
    seed_dir = Path(__file__).resolve().parent.parent.parent / "koinonia-db" / "seed"
    curricula_file = seed_dir / "curricula.json"
    readings_file = seed_dir / "reading_lists.json"

    if not curricula_file.exists():
        click.echo(f"Seed file not found: {curricula_file}", err=True)
        sys.exit(1)

    curricula_data = json.loads(curricula_file.read_text())
    readings_data = (
        json.loads(readings_file.read_text()) if readings_file.exists() else {"entries": []}
    )

    # Create reading entries first
    entry_map: dict[str, int] = {}
    for entry in readings_data["entries"]:
        eid = repo.add_entry(
            title=entry["title"],
            author=entry["author"],
            source_type=entry.get("source_type", "book"),
            url=entry.get("url"),
            pages=entry.get("pages"),
            difficulty=entry.get("difficulty", "intermediate"),
            organ_tags=entry.get("organ_tags", []),
        )
        entry_map[entry["key"]] = eid

    for c in curricula_data["curricula"]:
        cid = repo.add_curriculum(
            title=c["title"],
            theme=c["theme"],
            organ_focus=c.get("organ_focus"),
            duration_weeks=c["duration_weeks"],
            description=c["description"],
        )
        for sess in c["sessions"]:
            sid = repo.add_session(cid, sess["week"], sess["title"])
            # Link readings
            for rkey in sess.get("readings", []):
                if rkey in entry_map:
                    repo.link_entry_to_session(sid, entry_map[rkey])
            # Add discussion questions
            for q in sess.get("questions", []):
                repo.add_discussion_question(sid, q)
            # Add guide with activities
            repo.add_guide(
                session_id=sid,
                opening_questions=sess.get("questions", [])[:2],
                deep_dive_questions=sess.get("questions", [])[2:],
                activities=sess.get("activities", []),
                closing_reflection=(
                    f"How has this session changed your understanding of {sess['title']}?"
                ),
            )
        click.echo(f"  Seeded: {c['title']} ({c['duration_weeks']} weeks)")

    click.echo(f"Done. {len(curricula_data['curricula'])} curricula seeded.")


if __name__ == "__main__":
    cli()
