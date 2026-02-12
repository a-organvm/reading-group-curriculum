"""Tests for the reading_list module."""

from src.reading_list import ReadingList


class TestReadingList:
    def test_create_reading_list(self) -> None:
        rl = ReadingList("Philosophy Essentials")
        assert rl.name == "Philosophy Essentials"
        assert rl.entry_count == 0

    def test_add_entry(self) -> None:
        rl = ReadingList("Test")
        entry = rl.add_entry("Republic", "Plato", source="book", difficulty="advanced")
        assert entry.title == "Republic"
        assert entry.difficulty == "advanced"
        assert rl.entry_count == 1

    def test_annotate_entry(self) -> None:
        rl = ReadingList("Test")
        entry = rl.add_entry("Test Book", "Author")
        result = rl.annotate(entry.entry_id, "Key insight on page 42")
        assert result is True
        assert len(entry.annotations) == 1

    def test_annotate_unknown_returns_false(self) -> None:
        rl = ReadingList("Test")
        assert rl.annotate("fake_id", "note") is False

    def test_filter_by_difficulty(self) -> None:
        rl = ReadingList("Test")
        rl.add_entry("Easy Read", "A", difficulty="beginner")
        rl.add_entry("Hard Read", "B", difficulty="advanced")
        rl.add_entry("Medium Read", "C", difficulty="intermediate")
        beginners = rl.filter_by_difficulty("beginner")
        assert len(beginners) == 1
        assert beginners[0].title == "Easy Read"

    def test_filter_by_tag(self) -> None:
        rl = ReadingList("Test")
        rl.add_entry("Book A", "A", tags=["ontology", "theory"])
        rl.add_entry("Book B", "B", tags=["epistemology"])
        results = rl.filter_by_tag("ontology")
        assert len(results) == 1

    def test_search_by_title(self) -> None:
        rl = ReadingList("Test")
        rl.add_entry("Being and Time", "Heidegger")
        rl.add_entry("Critique of Pure Reason", "Kant")
        results = rl.search("being")
        assert len(results) == 1
        assert results[0].author == "Heidegger"
