"""Tests for reading_group_curriculum data_export — curricula index and sample."""
import json
from pathlib import Path

from src.data_export import (
    load_seed_curricula,
    load_seed_readings,
    build_curricula_index,
    render_sample_curriculum,
    export_all,
)


SEED_DIR = Path(__file__).parent.parent.parent / "koinonia-db" / "seed"


def test_load_seed_curricula():
    """Loads curricula from the real seed file."""
    curricula = load_seed_curricula(SEED_DIR)
    assert len(curricula) >= 3
    assert curricula[0]["title"]


def test_load_seed_readings():
    """Loads reading entries from the real seed file."""
    readings = load_seed_readings(SEED_DIR)
    assert len(readings) > 10
    assert readings[0]["title"]


def test_load_seed_missing_dir(tmp_path):
    """Returns empty lists when seed dir doesn't have files."""
    assert load_seed_curricula(tmp_path) == []
    assert load_seed_readings(tmp_path) == []


def test_build_curricula_index():
    """Index has expected structure and counts."""
    curricula = load_seed_curricula(SEED_DIR)
    readings = load_seed_readings(SEED_DIR)
    index = build_curricula_index(curricula, readings)
    assert index["curriculum_count"] >= 3
    assert index["total_sessions"] > 0
    assert index["total_weeks"] > 0
    assert len(index["themes"]) > 0
    assert index["reading_entry_count"] > 0
    for c in index["curricula"]:
        assert "title" in c
        assert "session_count" in c
        assert "theme" in c


def test_render_sample_curriculum():
    """Renders a curriculum to markdown with expected headings."""
    curricula = load_seed_curricula(SEED_DIR)
    md = render_sample_curriculum(curricula[0])
    assert md.startswith("# ")
    assert "**Theme:**" in md
    assert "**Duration:**" in md
    assert "## Week" in md


def test_export_all_writes_files(tmp_path):
    """export_all writes both artifacts to the output directory."""
    paths = export_all(seed_dir=SEED_DIR, output_dir=tmp_path)
    assert len(paths) == 2

    index_path = tmp_path / "curricula-index.json"
    assert index_path.exists()
    data = json.loads(index_path.read_text())
    assert data["curriculum_count"] >= 3

    md_path = tmp_path / "sample-curriculum.md"
    assert md_path.exists()
    assert md_path.read_text().startswith("# ")
