# textutils

`textutils` is a small Python library providing simple text-processing utilities.

The project is used to practice the foundations of open-source development:
project structure, documentation, Git workflows, testing, packaging, release
automation, and project maintenance.

## Features

The library provides:

- `word_count(text)` — counts words separated by whitespace.
- `character_count(text)` — counts every character in the input text.
- `reverse(text)` — returns the input text in reverse order.
- `capitalize_words(text)` — capitalizes the first ASCII letter of each word.
- `snake_case(text)` — converts whitespace-separated words to lowercase snake_case.

## Installation

Install the released package from PyPI:

```bash
python -m pip install textutils-subzero710
```

The distribution name on PyPI is `textutils-subzero710`, while the Python import remains
`textutils`.

For local development:

```bash
git clone https://github.com/Subzero710/textutils.git
cd textutils
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
```

## Usage

```python
from textutils import (
    capitalize_words,
    character_count,
    reverse,
    snake_case,
    word_count,
)

print(word_count("Hello Open Source"))       # 3
print(character_count("hello"))              # 5
print(reverse("hello"))                      # olleh
print(capitalize_words("hello open source")) # Hello Open Source
print(snake_case("Hello Open Source"))       # hello_open_source
```

## Development checks

Run the full local validation:

```bash
python -m black --check .
python -m ruff check .
python -m pytest
```

Build the wheel and source distribution:

```bash
python -m build
```

Generated release artifacts are written to `dist/`.

## Public API

The supported public API is exported by `textutils/__init__.py`.

Internal implementation helpers use a leading underscore and are not part of
the public API.

## Contributing

When making a change:

1. Keep the change focused.
2. Add or update tests when behavior changes.
3. Run Black, Ruff, and pytest before pushing.
4. Use a clear and descriptive commit message.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
