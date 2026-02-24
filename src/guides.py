"""Discussion guide generation for reading groups.

DEPRECATED: This in-memory implementation is retained as an offline fallback.
For database-backed operations, use repository.py with koinonia-db models.

Provides the GuideGenerator for creating structured discussion
guides from reading materials with questions, prompts, and activities.
"""

from __future__ import annotations

import warnings

warnings.warn(
    "reading_group_curriculum.guides is deprecated — use repository.CurriculumRepository",
    DeprecationWarning,
    stacklevel=2,
)

from dataclasses import dataclass  # noqa: E402
from typing import Any  # noqa: E402
from uuid import uuid4  # noqa: E402


@dataclass
class DiscussionGuide:
    """A discussion guide for a reading group session."""

    guide_id: str
    session_title: str
    opening_questions: list[str]
    deep_dive_questions: list[str]
    activities: list[str]
    closing_reflection: str
    estimated_minutes: int


class GuideGenerator:
    """Generates discussion guides for reading group sessions.

    Creates structured guides with opening questions, deep-dive topics,
    interactive activities, and closing reflections.
    """

    def __init__(self) -> None:
        self._templates: dict[str, list[str]] = {
            "opening": [
                "What was your first reaction to this reading?",
                "Which passage stood out to you most, and why?",
                "How does this connect to your own experience?",
            ],
            "deep_dive": [
                "What assumptions does the author make?",
                "How would you challenge the central argument?",
                "What are the practical implications of this work?",
            ],
            "activities": [
                "Small group discussion: Share one key takeaway",
                "Pair and compare: Find someone who disagreed with you",
                "Written reflection: 3-minute freewrite on the theme",
            ],
        }
        self._generated: list[DiscussionGuide] = []

    @property
    def guide_count(self) -> int:
        """Return the number of generated guides."""
        return len(self._generated)

    def generate(
        self,
        session_title: str,
        custom_questions: list[str] | None = None,
        custom_activities: list[str] | None = None,
        estimated_minutes: int = 90,
    ) -> DiscussionGuide:
        """Generate a discussion guide for a session.

        Args:
            session_title: Title of the reading group session.
            custom_questions: Additional questions to include.
            custom_activities: Additional activities to include.
            estimated_minutes: Expected discussion duration.

        Returns:
            The generated DiscussionGuide.
        """
        opening = list(self._templates["opening"])
        deep_dive = list(self._templates["deep_dive"])
        activities = list(self._templates["activities"])

        if custom_questions:
            deep_dive.extend(custom_questions)
        if custom_activities:
            activities.extend(custom_activities)

        guide = DiscussionGuide(
            guide_id=uuid4().hex[:8],
            session_title=session_title,
            opening_questions=opening,
            deep_dive_questions=deep_dive,
            activities=activities,
            closing_reflection=f"How has this session changed your understanding of {session_title}?",
            estimated_minutes=estimated_minutes,
        )
        self._generated.append(guide)
        return guide

    def add_template_question(self, category: str, question: str) -> bool:
        """Add a question to the template library.

        Args:
            category: Template category (opening, deep_dive, activities).
            question: The question or activity text.

        Returns:
            True if the category exists and the question was added.
        """
        if category not in self._templates:
            return False
        self._templates[category].append(question)
        return True

    def export_guide(self, guide: DiscussionGuide) -> dict[str, Any]:
        """Export a guide as a dictionary."""
        return {
            "guide_id": guide.guide_id,
            "session_title": guide.session_title,
            "opening_questions": guide.opening_questions,
            "deep_dive_questions": guide.deep_dive_questions,
            "activities": guide.activities,
            "closing_reflection": guide.closing_reflection,
            "estimated_minutes": guide.estimated_minutes,
        }
