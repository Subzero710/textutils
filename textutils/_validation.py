"""Internal validation helpers for textutils."""


def _ensure_text(text):
    """Validate that a public API input is text."""
    if not isinstance(text, str):
        raise TypeError("text must be a str")
