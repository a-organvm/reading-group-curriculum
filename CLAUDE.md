# CLAUDE.md — reading-group-curriculum

**ORGAN VI** (Community) · `organvm-vi-koinonia/reading-group-curriculum`
**Status:** ACTIVE · **Branch:** `main`

## What This Repo Is

Structured reading group curricula spanning eight-organ domains: 8-12 week programs with curated reading lists, discussion guides, and exercises

## Stack

**Languages:** Python
**Build:** Python (pip/setuptools)
**Testing:** pytest (likely)

## Directory Structure

```
📁 .github/
📁 docs/
    adr
📁 src/
    __init__.py
    __main__.py
    config.py
    curriculum.py
    export.py
    guides.py
    reading_list.py
    repository.py
📁 tests/
    __init__.py
    test_curriculum.py
    test_export.py
    test_guides.py
    test_reading_list.py
  .gitignore
  CHANGELOG.md
  LICENSE
  README.md
  pyproject.toml
  seed.yaml
```

## Key Files

- `README.md` — Project documentation
- `pyproject.toml` — Python project config
- `seed.yaml` — ORGANVM orchestration metadata
- `src/` — Main source code
- `tests/` — Test suite

## Development

```bash
pip install -e .    # Install in development mode
pytest              # Run tests
```

## ORGANVM Context

This repository is part of the **ORGANVM** eight-organ creative-institutional system.
It belongs to **ORGAN VI (Community)** under the `organvm-vi-koinonia` GitHub organization.

**Registry:** [`registry-v2.json`](https://github.com/meta-organvm/organvm-corpvs-testamentvm/blob/main/registry-v2.json)
**Corpus:** [`organvm-corpvs-testamentvm`](https://github.com/meta-organvm/organvm-corpvs-testamentvm)
