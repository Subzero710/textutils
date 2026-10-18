import pytest

from textutils import character_count, reverse, snake_case, word_count


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("hello world", 2),
        ("", 0),
        ("hello   world", 2),
        ("hello	world  python", 3),
        ("   ", 0),
    ],
)
def test_word_count(text, expected):
    assert word_count(text) == expected


@pytest.mark.parametrize(
    ("text", "expected"),
    [("hello", 5), ("", 0), ("hello world", 11), ("é", 1)],
)
def test_character_count(text, expected):
    assert character_count(text) == expected


@pytest.mark.parametrize(
    ("text", "expected"),
    [("hello", "olleh"), ("", ""), ("a", "a"), ("été", "été")],
)
def test_reverse(text, expected):
    assert reverse(text) == expected


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("doc ia", "doc_ia"),
        ("salut  toi", "salut_toi"),
        ("Hello World", "hello_world"),
        (" hello	world   python ", "hello_world_python"),
        ("", ""),
    ],
)
def test_snake_case(text, expected):
    assert snake_case(text) == expected


@pytest.mark.parametrize(
    "function",
    [word_count, character_count, reverse, snake_case],
)
def test_transform_functions_reject_non_string(function):
    with pytest.raises(TypeError, match="text must be a str"):
        function(123)
