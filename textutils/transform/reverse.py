"""Text-reversal utility."""

from .._validation import _ensure_text


def reverse(text):
    """Reverse the characters of a text.

    Parameters
    ----------
    text : str
        Text to reverse.

    Returns
    -------
    str
        New string containing the characters in reverse order.

    Raises
    ------
    TypeError
        If ``text`` is not a string.
    """
    _ensure_text(text)
    reversed_text = ""

    for char in text:
        reversed_text = char + reversed_text

    return reversed_text
