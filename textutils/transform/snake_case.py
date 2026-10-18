"""Snake-case conversion utility."""

from .._validation import _ensure_text


def snake_case(text):
    """Convert text to snake_case.

    Runs of whitespace are treated as a single word separator.

    Parameters
    ----------
    text : str
        Text to convert.

    Returns
    -------
    str
        Lowercase text with words joined by underscores.

    Raises
    ------
    TypeError
        If ``text`` is not a string.
    """
    _ensure_text(text)
    words = text.split()
    return "_".join(words).lower()
