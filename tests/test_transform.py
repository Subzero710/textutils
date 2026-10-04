from textutils.transform import word_count, character_count, reverse, snake_case


def test_word_count_basic():
    assert word_count("hello world") == 2


def test_word_count_empty():
    assert word_count("") == 0


def test_word_count_multiple_spaces():
    assert word_count("hello   world") == 2


def test_character_count():
    assert character_count("hello") == 5


def test_reverse():
    assert reverse("hello") == "olleh"

def test_word_count_tabs_and_newlines():
    assert word_count("hello\tworld\npython") == 3


def test_reverse_empty():
    assert reverse("") == ""


def test_snack_case():
    assert snake_case("doc ia") == "doc_ia"
    
def test_snack_case_double_space():
    assert snake_case("salut  toi") == "salut_toi"