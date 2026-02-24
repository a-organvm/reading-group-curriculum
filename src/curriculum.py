"""Reading group curriculum design.

DEPRECATED: This in-memory implementation is retained as an offline fallback.
For database-backed operations, use repository.py with koinonia-db models.

Provides the ReadingCurriculum class for organizing multi-session
reading programs with thematic arcs and progression tracking.
"""

from __future__ import annotations

import warnings

warnings.warn(
    "reading_group_curriculum.curriculum is deprecated — use repository.CurriculumRepository",
    DeprecationWarning,
    stacklevel=2,
)

from dataclasses import dataclass  # noqa: E402
from typing import Any  # noqa: E402
from uuid import uuid4  # noqa: E402


@dataclass
class Session:
    """A single reading group session."""

    session_id: str
    week: int
    title: str
    readings: list[str]
    discussion_questions: list[str]
    duration_minutes: int = 90
    completed: bool = False


class ReadingCurriculum:
    """A structured reading group curriculum.

    Organizes reading material into weekly sessions with discussion
    questions, tracks completion, and supports thematic grouping.
    """

    def __init__(self, title: str, theme: str = "general") -> None:
        self._title = title
        self._theme = theme
        self._sessions: list[Session] = []

    @property
    def title(self) -> str:
        """Return the curriculum title."""
        return self._title

    @property
    def session_count(self) -> int:
        """Return the total number of sessions."""
        return len(self._sessions)

    @property
    def completed_count(self) -> int:
        """Return the number of completed sessions."""
        return sum(1 for s in self._sessions if s.completed)

    @property
    def progress_pct(self) -> float:
        """Return completion percentage."""
        if not self._sessions:
            return 0.0
        return round(self.completed_count / self.session_count * 100, 1)

    def add_session(
        self,
        title: str,
        readings: list[str],
        discussion_questions: list[str] | None = None,
        duration_minutes: int = 90,
    ) -> Session:
        """Add a new session to the curriculum.

        Args:
            title: Session title.
            readings: List of reading assignments (titles or URLs).
            discussion_questions: Questions for group discussion.
            duration_minutes: Expected session duration.

        Returns:
            The created Session.
        """
        week = len(self._sessions) + 1
        session = Session(
            session_id=uuid4().hex[:8],
            week=week,
            title=title,
            readings=readings,
            discussion_questions=discussion_questions or [],
            duration_minutes=duration_minutes,
        )
        self._sessions.append(session)
        return session

    def complete_session(self, session_id: str) -> bool:
        """Mark a session as completed.

        Args:
            session_id: The session to mark complete.

        Returns:
            True if found and marked, False otherwise.
        """
        for session in self._sessions:
            if session.session_id == session_id:
                session.completed = True
                return True
        return False

    def get_next_session(self) -> Session | None:
        """Return the next incomplete session."""
        for session in self._sessions:
            if not session.completed:
                return session
        return None

    def get_total_readings(self) -> int:
        """Return the total number of reading assignments."""
        return sum(len(s.readings) for s in self._sessions)

    def export(self) -> dict[str, Any]:
        """Export the curriculum as a dictionary."""
        return {
            "title": self._title,
            "theme": self._theme,
            "sessions": self.session_count,
            "completed": self.completed_count,
            "progress_pct": self.progress_pct,
            "total_readings": self.get_total_readings(),
        }
