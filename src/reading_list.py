"""Reading list management with annotations and recommendations.

DEPRECATED: This in-memory implementation is retained as an offline fallback.
For database-backed operations, use repository.py with koinonia-db models.

Provides the ReadingList class for curating and annotating collections
of readings for group study.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any
from uuid import uuid4


@dataclass
class ReadingEntry:
    """A single entry in a reading list."""

    entry_id: str
    title: str
    author: str
    source: str  # book, article, essay, etc.
    url: str | None = None
    pages: str | None = None  # e.g., "1-45" or "Ch. 3"
    difficulty: str = "intermediate"  # beginner, intermediate, advanced
    annotations: list[str] = field(default_factory=list)
    tags: list[str] = field(default_factory=list)


class ReadingList:
    """Curated reading list with annotations and search.

    Manages a collection of reading entries with tagging,
    difficulty filtering, and annotation capabilities.
    """

    def __init__(self, name: str) -> None:
        self._name = name
        self._entries: dict[str, ReadingEntry] = {}

    @property
    def name(self) -> str:
        """Return the list name."""
        return self._name

    @property
    def entry_count(self) -> int:
        """Return the number of entries."""
        return len(self._entries)

    def add_entry(
        self,
        title: str,
        author: str,
        source: str = "book",
        url: str | None = None,
        pages: str | None = None,
        difficulty: str = "intermediate",
        tags: list[str] | None = None,
    ) -> ReadingEntry:
        """Add a reading to the list.

        Args:
            title: Title of the work.
            author: Author name(s).
            source: Type of source (book, article, essay).
            url: Optional URL for online resources.
            pages: Page range or chapter reference.
            difficulty: Difficulty level.
            tags: Categorization tags.

        Returns:
            The created ReadingEntry.
        """
        entry = ReadingEntry(
            entry_id=uuid4().hex[:8],
            title=title,
            author=author,
            source=source,
            url=url,
            pages=pages,
            difficulty=difficulty,
            tags=tags or [],
        )
        self._entries[entry.entry_id] = entry
        return entry

    def annotate(self, entry_id: str, annotation: str) -> bool:
        """Add an annotation to a reading entry.

        Args:
            entry_id: The entry to annotate.
            annotation: The annotation text.

        Returns:
            True if the entry was found and annotated.
        """
        entry = self._entries.get(entry_id)
        if entry is None:
            return False
        entry.annotations.append(annotation)
        return True

    def filter_by_difficulty(self, difficulty: str) -> list[ReadingEntry]:
        """Get all entries of a specific difficulty level."""
        return [e for e in self._entries.values() if e.difficulty == difficulty]

    def filter_by_tag(self, tag: str) -> list[ReadingEntry]:
        """Get all entries with a specific tag."""
        return [e for e in self._entries.values() if tag in e.tags]

    def search(self, query: str) -> list[ReadingEntry]:
        """Search entries by title or author.

        Args:
            query: Search term (case-insensitive).

        Returns:
            List of matching entries.
        """
        q = query.lower()
        return [
            e for e in self._entries.values()
            if q in e.title.lower() or q in e.author.lower()
        ]

    def export(self) -> dict[str, Any]:
        """Export the reading list as a dictionary."""
        return {
            "name": self._name,
            "entry_count": self.entry_count,
            "entries": [
                {
                    "entry_id": e.entry_id,
                    "title": e.title,
                    "author": e.author,
                    "source": e.source,
                    "difficulty": e.difficulty,
                    "tags": e.tags,
                    "annotation_count": len(e.annotations),
                }
                for e in self._entries.values()
            ],
        }
