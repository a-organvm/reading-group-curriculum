"""Generate static data artifacts from seed curriculum data.

Produces:
  data/curricula-index.json  — index of curricula with session counts
  data/sample-curriculum.md  — first curriculum rendered as markdown

Reads seed JSON directly (no database required).
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .export import export_curriculum_markdown

SEED_DIR = Path(__file__).parent.parent.parent / "koinonia-db" / "seed"


def load_seed_curricula(seed_dir: Path | None = None) -> list[dict[str, Any]]:
    """Load curriculum data from koinonia-db seed file."""
    seed_dir = seed_dir or SEED_DIR
    path = seed_dir / "curricula.json"
    if not path.exists():
        return []
    data = json.loads(path.read_text())
    return data.get("curricula", [])


def load_seed_readings(seed_dir: Path | None = None) -> list[dict[str, Any]]:
    """Load reading list entries from koinonia-db seed file."""
    seed_dir = seed_dir or SEED_DIR
    path = seed_dir / "reading_lists.json"
    if not path.exists():
        return []
    data = json.loads(path.read_text())
    return data.get("entries", [])


def build_curricula_index(
    curricula: list[dict[str, Any]],
    readings: list[dict[str, Any]],
) -> dict[str, Any]:
    """Build a summary index from curriculum and reading data."""
    themes = sorted({c.get("theme", "general") for c in curricula})
    total_sessions = sum(len(c.get("sessions", [])) for c in curricula)
    total_weeks = sum(c.get("duration_weeks", 0) for c in curricula)

    # Count unique reading keys referenced across all curricula sessions
    referenced_keys: set[str] = set()
    for c in curricula:
        for s in c.get("sessions", []):
            referenced_keys.update(s.get("readings", []))

    return {
        "curriculum_count": len(curricula),
        "total_sessions": total_sessions,
        "total_weeks": total_weeks,
        "themes": themes,
        "reading_entry_count": len(readings),
        "referenced_reading_keys": len(referenced_keys),
        "curricula": [
            {
                "title": c["title"],
                "theme": c.get("theme"),
                "organ_focus": c.get("organ_focus"),
                "duration_weeks": c.get("duration_weeks"),
                "session_count": len(c.get("sessions", [])),
                "description": c.get("description", ""),
            }
            for c in curricula
        ],
    }


def render_sample_curriculum(curriculum: dict[str, Any]) -> str:
    """Render a curriculum dict as markdown using the existing export function."""
    return export_curriculum_markdown(curriculum)


def export_all(
    seed_dir: Path | None = None,
    output_dir: Path | None = None,
) -> list[Path]:
    """Generate all data artifacts and return output paths."""
    curricula = load_seed_curricula(seed_dir)
    readings = load_seed_readings(seed_dir)
    output_dir = output_dir or Path(__file__).parent.parent / "data"
    output_dir.mkdir(parents=True, exist_ok=True)
    outputs: list[Path] = []

    # curricula-index.json
    index = build_curricula_index(curricula, readings)
    index_path = output_dir / "curricula-index.json"
    index_path.write_text(json.dumps(index, indent=2) + "\n")
    outputs.append(index_path)

    # sample-curriculum.md
    if curricula:
        md = render_sample_curriculum(curricula[0])
        md_path = output_dir / "sample-curriculum.md"
        md_path.write_text(md)
        outputs.append(md_path)

    return outputs


def main() -> None:
    """CLI entry point for data export."""
    paths = export_all()
    for p in paths:
        print(f"Written: {p}")


if __name__ == "__main__":
    main()
