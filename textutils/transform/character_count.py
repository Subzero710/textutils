"""Character-counting utility."""

from .._validation import _ensure_text


def character_count(text):
    """Count the number of characters in a text.

    Parameters
    ----------
    text : str
        Text whose characters will be counted.

    Returns
    -------
    int
        Total number of characters in ``text``.

    Raises
    ------
    TypeError
        If ``text`` is not a string.
    """
    _ensure_text(text)
    count = 0

    for _ in text:
        count += 1

    return count
