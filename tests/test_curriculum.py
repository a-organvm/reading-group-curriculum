"""Tests for the curriculum module."""

from src.curriculum import ReadingCurriculum


class TestReadingCurriculum:
    def test_create_curriculum(self) -> None:
        curr = ReadingCurriculum("Ontology Reading Group", theme="philosophy")
        assert curr.title == "Ontology Reading Group"
        assert curr.session_count == 0

    def test_add_session(self) -> None:
        curr = ReadingCurriculum("Test")
        session = curr.add_session(
            "Week 1: Foundations",
            readings=["Being and Time, Ch. 1"],
            discussion_questions=["What is Dasein?"],
        )
        assert session.week == 1
        assert curr.session_count == 1

    def test_sessions_auto_increment_week(self) -> None:
        curr = ReadingCurriculum("Test")
        s1 = curr.add_session("Week 1", readings=["R1"])
        s2 = curr.add_session("Week 2", readings=["R2"])
        assert s1.week == 1
        assert s2.week == 2

    def test_complete_session(self) -> None:
        curr = ReadingCurriculum("Test")
        session = curr.add_session("W1", readings=["R1"])
        assert curr.completed_count == 0
        curr.complete_session(session.session_id)
        assert curr.completed_count == 1

    def test_progress_percentage(self) -> None:
        curr = ReadingCurriculum("Test")
        s1 = curr.add_session("W1", readings=["R1"])
        curr.add_session("W2", readings=["R2"])
        curr.complete_session(s1.session_id)
        assert curr.progress_pct == 50.0

    def test_get_next_session(self) -> None:
        curr = ReadingCurriculum("Test")
        s1 = curr.add_session("W1", readings=["R1"])
        s2 = curr.add_session("W2", readings=["R2"])
        curr.complete_session(s1.session_id)
        next_s = curr.get_next_session()
        assert next_s is not None
        assert next_s.session_id == s2.session_id

    def test_get_total_readings(self) -> None:
        curr = ReadingCurriculum("Test")
        curr.add_session("W1", readings=["R1", "R2"])
        curr.add_session("W2", readings=["R3"])
        assert curr.get_total_readings() == 3

    def test_export(self) -> None:
        curr = ReadingCurriculum("Export Test", theme="theory")
        curr.add_session("W1", readings=["R1"])
        data = curr.export()
        assert data["title"] == "Export Test"
        assert data["theme"] == "theory"
