"""Export curricula as publishable markdown."""

from __future__ import annotations

from typing import Any


def export_curriculum_markdown(curriculum_data: dict[str, Any]) -> str:
    """Render a curriculum dict as a formatted markdown document.

    Args:
        curriculum_data: Dictionary with keys title, description, theme,
            duration_weeks, organ_focus, and optional sessions list.

    Returns:
        A markdown string ready for publishing.
    """
    md = f"# {curriculum_data['title']}\n\n"
    md += f"*{curriculum_data['description']}*\n\n"
    md += f"**Theme:** {curriculum_data['theme']}  \n"
    md += f"**Duration:** {curriculum_data['duration_weeks']} weeks  \n"
    if curriculum_data.get("organ_focus"):
        md += f"**Focus:** {curriculum_data['organ_focus']}  \n"
    md += "\n---\n\n"

    for session in curriculum_data.get("sessions", []):
        md += f"## Week {session['week']}: {session['title']}\n\n"

        if session.get("readings"):
            md += "### Readings\n\n"
            for r in session["readings"]:
                if isinstance(r, dict):
                    md += f"- **{r['title']}** by {r['author']}"
                    if r.get("pages"):
                        md += f" (pp. {r['pages']})"
                    md += "\n"
                else:
                    md += f"- {r}\n"
            md += "\n"

        if session.get("questions"):
            md += "### Discussion Questions\n\n"
            for q in session["questions"]:
                md += f"1. {q}\n"
            md += "\n"

        if session.get("activities"):
            md += "### Activities\n\n"
            for a in session["activities"]:
                md += f"- {a}\n"
            md += "\n"

        md += "---\n\n"

    return md
