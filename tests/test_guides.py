"""Tests for the guides module."""

from src.guides import GuideGenerator


class TestGuideGenerator:
    def test_generate_guide(self) -> None:
        gen = GuideGenerator()
        guide = gen.generate("Recursion and Identity")
        assert guide.session_title == "Recursion and Identity"
        assert len(guide.opening_questions) > 0
        assert len(guide.deep_dive_questions) > 0
        assert len(guide.activities) > 0
        assert guide.estimated_minutes == 90

    def test_custom_questions(self) -> None:
        gen = GuideGenerator()
        guide = gen.generate("Test", custom_questions=["What is X?"])
        assert "What is X?" in guide.deep_dive_questions

    def test_custom_activities(self) -> None:
        gen = GuideGenerator()
        guide = gen.generate("Test", custom_activities=["Draw a diagram"])
        assert "Draw a diagram" in guide.activities

    def test_closing_reflection(self) -> None:
        gen = GuideGenerator()
        guide = gen.generate("Philosophy of Mind")
        assert "Philosophy of Mind" in guide.closing_reflection

    def test_guide_count(self) -> None:
        gen = GuideGenerator()
        assert gen.guide_count == 0
        gen.generate("Guide 1")
        gen.generate("Guide 2")
        assert gen.guide_count == 2

    def test_add_template_question(self) -> None:
        gen = GuideGenerator()
        assert gen.add_template_question("opening", "New opener?") is True
        guide = gen.generate("Test")
        assert "New opener?" in guide.opening_questions

    def test_add_template_invalid_category(self) -> None:
        gen = GuideGenerator()
        assert gen.add_template_question("nonexistent", "Q?") is False

    def test_export_guide(self) -> None:
        gen = GuideGenerator()
        guide = gen.generate("Export Test")
        data = gen.export_guide(guide)
        assert data["session_title"] == "Export Test"
        assert "guide_id" in data
        assert "opening_questions" in data

    def test_estimated_minutes_custom(self) -> None:
        gen = GuideGenerator()
        guide = gen.generate("Short Session", estimated_minutes=45)
        assert guide.estimated_minutes == 45
