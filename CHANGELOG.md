# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.4.0] - 2026-02-17

### Added
- **AQUA COMMUNIS sprint** — repository tests + CI normalization
- `tests/test_repository.py` — 12 structure tests + 4 live DB tests (gated behind `DATABASE_URL`)
- Test count: 33 → 49 (+16, 4 skipped)

### Changed
- CI Python version normalized from 3.12 to 3.11 (consistent with all other ORGAN-VI repos)

## [0.3.0] - 2026-02-17

### Added
- Full-text search via tsvector on reading entries (title + author)

## [0.2.0] - 2026-02-17

### Added

- Database-backed repository (CurriculumRepository) using koinonia-db models
- Click CLI with `list`, `show`, `export`, and `seed` commands
- Seed command imports curricula, reading entries, and discussion guides from JSON

### Changed

- URL conversion (postgresql→psycopg) moved from repository to config.py

### Deprecated

- In-memory `ReadingCurriculum`, `GuideGenerator`, and `ReadingList` classes (retained as offline fallback)

## [0.1.1] - 2026-02-11

### Added

- Platinum Sprint: standardized badge row, CHANGELOG
- Initial CHANGELOG following Keep a Changelog format

## [0.1.0] - 2026-02-11

### Added

- Initial public release as part of the organvm eight-organ system
- Core project structure and documentation

[Unreleased]: https://github.com/organvm-vi-koinonia/reading-group-curriculum/compare/v0.2.0...HEAD
[0.2.0]: https://github.com/organvm-vi-koinonia/reading-group-curriculum/compare/v0.1.1...v0.2.0
[0.1.1]: https://github.com/organvm-vi-koinonia/reading-group-curriculum/compare/v0.1.0...v0.1.1
[0.1.0]: https://github.com/organvm-vi-koinonia/reading-group-curriculum/releases/tag/v0.1.0
