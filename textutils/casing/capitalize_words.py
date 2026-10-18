"""Word-capitalization utility."""

from .._validation import _ensure_text


def capitalize_words(text):
    """Capitalize the first ASCII letter of each word.

    Words are separated by spaces, tabs, or newline characters.

    Parameters
    ----------
    text : str
        Text whose words will be capitalized.

    Returns
    -------
    str
        Text with the first lowercase ASCII letter of each word converted
        to uppercase.

    Raises
    ------
    TypeError
        If ``text`` is not a string.
    """
    _ensure_text(text)
    result = ""
    capitalize_next = True

    for char in text:
        if char in " ":
            result += char
            capitalize_next = True
        elif capitalize_next:
            if "a" <= char <= "z":
                result += chr(ord(char) - 32)
            else:
                result += char

            capitalize_next = False
        else:
            result += char

    return result
