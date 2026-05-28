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

    text = text.replace("\x00", " ") #Removes null characters that sometimes appear in PDFs.

    text = re.sub(r"\s+", " ", text) #Converts multiple spaces and newlines into one space.

    text = re.sub(r"Page\s+\d+", "", text, flags=re.IGNORECASE) #Removes common page number patterns like "Page 1", "Page 2", etc.

    text = text.strip() #Removes leading and trailing whitespace.

    return text