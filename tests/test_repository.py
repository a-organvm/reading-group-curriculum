"""Tests for CurriculumRepository — structure and method availability."""

from __future__ import annotations

import os

import pytest

from src.repository import CurriculumRepository


# ── Structure Tests (no DB required) ───────────────────────────


def test_repository_has_add_curriculum():
    assert hasattr(CurriculumRepository, "add_curriculum")
    assert callable(getattr(CurriculumRepository, "add_curriculum"))


def test_repository_has_get_curriculum():
    assert hasattr(CurriculumRepository, "get_curriculum")
    assert callable(getattr(CurriculumRepository, "get_curriculum"))


def test_repository_has_list_curricula():
    assert hasattr(CurriculumRepository, "list_curricula")
    assert callable(getattr(CurriculumRepository, "list_curricula"))


def test_repository_has_count_curricula():
    assert hasattr(CurriculumRepository, "count_curricula")
    assert callable(getattr(CurriculumRepository, "count_curricula"))


def test_repository_has_add_session():
    assert hasattr(CurriculumRepository, "add_session")


def test_repository_has_get_sessions():
    assert hasattr(CurriculumRepository, "get_sessions")


def test_repository_has_add_entry():
    assert hasattr(CurriculumRepository, "add_entry")


def test_repository_has_get_entry_by_title():
    assert hasattr(CurriculumRepository, "get_entry_by_title")


def test_repository_has_count_entries():
    assert hasattr(CurriculumRepository, "count_entries")


def test_repository_has_link_entry_to_session():
    assert hasattr(CurriculumRepository, "link_entry_to_session")


def test_repository_has_add_discussion_question():
    assert hasattr(CurriculumRepository, "add_discussion_question")


def test_repository_has_add_guide():
    assert hasattr(CurriculumRepository, "add_guide")


# ── Live DB Tests (gated behind DATABASE_URL) ──────────────────

_skip_no_db = pytest.mark.skipif(
    not os.environ.get("DATABASE_URL"),
    reason="DATABASE_URL not set — skipping live DB tests",
)


@_skip_no_db
def test_live_instantiation():
    repo = CurriculumRepository(os.environ["DATABASE_URL"])
    assert repo is not None


@_skip_no_db
def test_live_count_curricula():
    repo = CurriculumRepository(os.environ["DATABASE_URL"])
    count = repo.count_curricula()
    assert isinstance(count, int)
    assert count >= 0


@_skip_no_db
def test_live_list_curricula():
    repo = CurriculumRepository(os.environ["DATABASE_URL"])
    curricula = repo.list_curricula()
    assert isinstance(curricula, list)


@_skip_no_db
def test_live_count_entries():
    repo = CurriculumRepository(os.environ["DATABASE_URL"])
    count = repo.count_entries()
    assert isinstance(count, int)
    assert count >= 0
