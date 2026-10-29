# Changelog

All notable changes to this project are documented in this file.

## [0.1.0] - 2026-10-29

### Added

- `word_count(text)` utility.
- `character_count(text)` utility.
- `reverse(text)` utility.
- `capitalize_words(text)` utility.
- `snake_case(text)` utility.
- Public API through `textutils/__init__.py`.
- Unit tests for normal inputs and edge cases.
- Expected-exception tests for invalid input types.
- Test coverage reporting with `pytest-cov`.
- Package configuration with `pyproject.toml`.
- Black and Ruff development tooling.
- Automated CI workflow.
- Automated PyPI release workflow using Trusted Publishing.

### Changed

- Organized utilities into dedicated packages and modules.
- Added NumPy-style public API docstrings.
- Added a private input-validation helper.

### Fixed

- Correct handling of tabs and other whitespace in `word_count`.
- Correct handling of whitespace in `capitalize_words`.
