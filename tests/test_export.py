"""Tests for the export module."""

from src.export import export_curriculum_markdown


class TestExportCurriculumMarkdown:
    def test_basic_header(self) -> None:
        data = {
            "title": "Test Curriculum",
            "description": "A test description",
            "theme": "philosophy",
            "duration_weeks": 4,
            "organ_focus": None,
        }
        md = export_curriculum_markdown(data)
        assert "# Test Curriculum" in md
        assert "*A test description*" in md
        assert "**Theme:** philosophy" in md
        assert "**Duration:** 4 weeks" in md

    def test_organ_focus_included_when_set(self) -> None:
        data = {
            "title": "Focus Test",
            "description": "desc",
            "theme": "theory",
            "duration_weeks": 2,
            "organ_focus": "ORGAN-I",
        }
        md = export_curriculum_markdown(data)
        assert "**Focus:** ORGAN-I" in md

    def test_organ_focus_omitted_when_none(self) -> None:
        data = {
            "title": "No Focus",
            "description": "desc",
            "theme": "general",
            "duration_weeks": 1,
            "organ_focus": None,
        }
        md = export_curriculum_markdown(data)
        assert "**Focus:**" not in md

    def test_session_rendering(self) -> None:
        data = {
            "title": "Session Test",
            "description": "desc",
            "theme": "t",
            "duration_weeks": 1,
            "organ_focus": None,
            "sessions": [
                {
                    "week": 1,
                    "title": "Foundations",
                    "readings": ["Being and Time"],
                    "questions": ["What is Dasein?"],
                    "activities": ["Draw a diagram"],
                },
            ],
        }
        md = export_curriculum_markdown(data)
        assert "## Week 1: Foundations" in md
        assert "### Readings" in md
        assert "- Being and Time" in md
        assert "### Discussion Questions" in md
        assert "1. What is Dasein?" in md
        assert "### Activities" in md
        assert "- Draw a diagram" in md

    def test_dict_readings_with_pages(self) -> None:
        data = {
            "title": "Dict Readings",
            "description": "desc",
            "theme": "t",
            "duration_weeks": 1,
            "organ_focus": None,
            "sessions": [
                {
                    "week": 1,
                    "title": "W1",
                    "readings": [
                        {"title": "GEB", "author": "Hofstadter", "pages": "1-36"},
                    ],
                    "questions": [],
                    "activities": [],
                },
            ],
        }
        md = export_curriculum_markdown(data)
        assert "**GEB** by Hofstadter (pp. 1-36)" in md

    def test_dict_readings_without_pages(self) -> None:
        data = {
            "title": "No Pages",
            "description": "desc",
            "theme": "t",
            "duration_weeks": 1,
            "organ_focus": None,
            "sessions": [
                {
                    "week": 1,
                    "title": "W1",
                    "readings": [
                        {"title": "Republic", "author": "Plato"},
                    ],
                    "questions": [],
                    "activities": [],
                },
            ],
        }
        md = export_curriculum_markdown(data)
        assert "**Republic** by Plato" in md
        assert "(pp." not in md

    def test_empty_sessions(self) -> None:
        data = {
            "title": "Empty",
            "description": "desc",
            "theme": "t",
            "duration_weeks": 0,
            "organ_focus": None,
            "sessions": [],
        }
        md = export_curriculum_markdown(data)
        assert "# Empty" in md
        assert "---" in md

    def test_multiple_sessions(self) -> None:
        data = {
            "title": "Multi",
            "description": "desc",
            "theme": "t",
            "duration_weeks": 2,
            "organ_focus": None,
            "sessions": [
                {"week": 1, "title": "First", "readings": [], "questions": [], "activities": []},
                {"week": 2, "title": "Second", "readings": [], "questions": [], "activities": []},
            ],
        }
        md = export_curriculum_markdown(data)
        assert "## Week 1: First" in md
        assert "## Week 2: Second" in md

    def test_session_without_optional_sections(self) -> None:
        data = {
            "title": "Minimal",
            "description": "desc",
            "theme": "t",
            "duration_weeks": 1,
            "organ_focus": None,
            "sessions": [
                {"week": 1, "title": "Bare", "readings": [], "questions": [], "activities": []},
            ],
        }
        md = export_curriculum_markdown(data)
        assert "## Week 1: Bare" in md
        # No sub-headers when lists are empty
        assert "### Readings" not in md
        assert "### Discussion Questions" not in md
        assert "### Activities" not in md
