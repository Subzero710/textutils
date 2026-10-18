import pytest

from textutils import capitalize_words


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("hello world", "Hello World"),
        ("", ""),
        ("hello   world", "Hello   World"),
        ("hello	world    python", "Hello	World    Python"),
        ("1hello world", "1hello World"),
        ("Already Capitalized", "Already Capitalized"),
    ],
)
def test_capitalize_words(text, expected):
    assert capitalize_words(text) == expected


def test_capitalize_words_rejects_non_string():
    with pytest.raises(TypeError, match="text must be a str"):
        capitalize_words(None)
