# textutils

`textutils` is a small Python library providing simple text-processing utilities.

The project is used to practice the foundations of open-source development: project structure, documentation, Git workflows, testing, packaging, and project maintenance.

## Features

The library currently provides four utilities:

- `word_count(text)` — counts words separated by spaces, tabs, or newlines.
- `character_count(text)` — counts every character in the input text.
- `reverse(text)` — returns the input text in reverse order.
- `capitalize_words(text)` — uppercases the first character of each word when that character is a lowercase ASCII letter; words are separated by spaces, tabs, or newlines.
- `snack_case(text)` - Replace space by underscore in the text and all the text is lowercase.

## Project structure

```text
textutils/
├── textutils/
│   ├── __init__.py
│   ├── casing/
│   │   ├── __init__.py
│   │   └── capitalize_words.py
│   └── transform/
│       ├── __init__.py
│       ├── word_count.py
│       ├── character_count.py
│       └── reverse.py
├── tests/
│   ├── test_casing.py
│   └── test_transform.py
├── .gitignore
├── CHANGELOG.md
├── LICENSE
├── README.md
└── pyproject.toml
```

## Installation

Clone the repository:

```bash
git clone https://github.com/Subzero710/textutils.git
cd textutils
```

Install the library in editable mode:

```bash
python -m pip install -e .
```

To install the test dependency as well:

```bash
python -m pip install -e ".[test]"
```

## Usage

### Text transformations

```python
from textutils.transform import word_count, character_count, reverse

text = "Hello Open Source"

print(word_count(text))       # 3
print(character_count(text))  # 17
print(reverse(text))          # ecruoS nepO olleH
```

### Casing

```python
from textutils.casing import capitalize_words

print(capitalize_words("hello open source"))
# Hello Open Source
```

## Testing

The project uses `pytest` for unit testing.

Run the complete test suite from the repository root:

```bash
python -m pytest
```

The tests cover normal inputs as well as cases such as empty strings, repeated spaces, tabs, and newlines.

## Contributing

Contributions are welcome.

When making a change:

1. Keep the change focused.
2. Add or update tests when behavior changes.
3. Run the test suite with `python -m pytest`.
4. Use a clear and descriptive commit message.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
