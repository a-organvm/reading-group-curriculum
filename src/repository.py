"""Repository for reading group curriculum database operations."""

from __future__ import annotations

from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from koinonia_db.models.reading import (
    Curriculum,
    ReadingSessionRow,
    Entry,
    SessionEntry,
    DiscussionQuestion,
    Guide,
)


class CurriculumRepository:
    """Sync repository wrapping SQLAlchemy queries for CLI use."""

    def __init__(self, database_url: str) -> None:
        self._engine = create_engine(database_url)

    # ── Curricula ──────────────────────────────────────────────

    def add_curriculum(
        self,
        title: str,
        theme: str,
        organ_focus: str | None,
        duration_weeks: int,
        description: str,
    ) -> int:
        """Insert a curriculum row and return its id."""
        with Session(self._engine) as s:
            row = Curriculum(
                title=title,
                theme=theme,
                organ_focus=organ_focus,
                duration_weeks=duration_weeks,
                description=description,
            )
            s.add(row)
            s.commit()
            return row.id

    def get_curriculum(self, curriculum_id: int) -> Curriculum | None:
        """Fetch a single curriculum by id."""
        with Session(self._engine) as s:
            return s.get(Curriculum, curriculum_id)

    def list_curricula(self) -> list[Curriculum]:
        """Return all curricula ordered by id."""
        with Session(self._engine) as s:
            stmt = select(Curriculum).order_by(Curriculum.id)
            return list(s.scalars(stmt))

    def count_curricula(self) -> int:
        """Return the total number of curricula."""
        with Session(self._engine) as s:
            return s.query(Curriculum).count()

    # ── Sessions ───────────────────────────────────────────────

    def add_session(
        self,
        curriculum_id: int,
        week: int,
        title: str,
        duration_minutes: int = 90,
    ) -> int:
        """Insert a session row and return its id."""
        with Session(self._engine) as s:
            row = ReadingSessionRow(
                curriculum_id=curriculum_id,
                week=week,
                title=title,
                duration_minutes=duration_minutes,
            )
            s.add(row)
            s.commit()
            return row.id

    def get_sessions(self, curriculum_id: int) -> list[ReadingSessionRow]:
        """Return all sessions for a curriculum, ordered by week."""
        with Session(self._engine) as s:
            stmt = (
                select(ReadingSessionRow)
                .where(ReadingSessionRow.curriculum_id == curriculum_id)
                .order_by(ReadingSessionRow.week)
            )
            return list(s.scalars(stmt))

    # ── Entries ────────────────────────────────────────────────

    def add_entry(
        self,
        title: str,
        author: str,
        source_type: str = "book",
        url: str | None = None,
        pages: str | None = None,
        difficulty: str = "intermediate",
        organ_tags: list[str] | None = None,
    ) -> int:
        """Insert a reading entry and return its id."""
        with Session(self._engine) as s:
            row = Entry(
                title=title,
                author=author,
                source_type=source_type,
                url=url,
                pages=pages,
                difficulty=difficulty,
                organ_tags=organ_tags or [],
            )
            s.add(row)
            s.commit()
            return row.id

    def get_entry_by_title(self, title: str) -> Entry | None:
        """Find an entry by exact title match."""
        with Session(self._engine) as s:
            stmt = select(Entry).where(Entry.title == title)
            return s.scalar(stmt)

    def count_entries(self) -> int:
        """Return the total number of reading entries."""
        with Session(self._engine) as s:
            return s.query(Entry).count()

    # ── Linking & Questions ────────────────────────────────────

    def link_entry_to_session(self, session_id: int, entry_id: int) -> None:
        """Create a session-entry association."""
        with Session(self._engine) as s:
            s.add(SessionEntry(session_id=session_id, entry_id=entry_id))
            s.commit()

    def add_discussion_question(
        self,
        session_id: int,
        question_text: str,
        category: str = "deep_dive",
    ) -> int:
        """Insert a discussion question and return its id."""
        with Session(self._engine) as s:
            row = DiscussionQuestion(
                session_id=session_id,
                question_text=question_text,
                category=category,
            )
            s.add(row)
            s.commit()
            return row.id

    # ── Guides ─────────────────────────────────────────────────

    def add_guide(
        self,
        session_id: int,
        opening_questions: list[str],
        deep_dive_questions: list[str],
        activities: list[str],
        closing_reflection: str,
    ) -> int:
        """Insert a discussion guide and return its id."""
        with Session(self._engine) as s:
            row = Guide(
                session_id=session_id,
                opening_questions=opening_questions,
                deep_dive_questions=deep_dive_questions,
                activities=activities,
                closing_reflection=closing_reflection,
            )
            s.add(row)
            s.commit()
            return row.id
