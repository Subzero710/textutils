"""Word-counting utility."""

from .._validation import _ensure_text


def word_count(text):
    """Count the number of words in a text.

    Words are separated by spaces, tabs, or newline characters.

    Parameters
    ----------
    text : str
        Text to analyze.

    Returns
    -------
    int
        Number of words contained in ``text``.

    Raises
    ------
    TypeError
        If ``text`` is not a string.
    """
    _ensure_text(text)
    count = 0
    in_word = False

    for char in text:
        if not char.isspace():
            if not in_word:
                count += 1
                in_word = True
        else:
            in_word = False

    return count
