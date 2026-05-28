import re


def clean_text(text: str) -> str:
    """
    Clean extracted PDF text.

    Args:
        text: Raw text extracted from PDF.

    Returns:
        Cleaned text.
    """

    if not text:
        return ""

    text = text.replace("\x00", " ")

    text = re.sub(r"\s+", " ", text)

    text = re.sub(r"Page\s+\d+", "", text, flags=re.IGNORECASE)

    text = text.strip()

    return text