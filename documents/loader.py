from pathlib import Path
from pypdf import PdfReader


def load_pdf_text(file_path: str) -> list[dict]:
    """
    Extract text from a PDF file page by page.

    Args:
        file_path: Path to the PDF file.

    Returns:
        A list of dictionaries. Each dictionary contains page number and text.
    """

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"PDF file not found: {file_path}")

    if path.suffix.lower() != ".pdf":
        raise ValueError("Only PDF files are supported in this loader.")

    reader = PdfReader(str(path))
    pages = []

    for page_index, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""

        pages.append(
            {
                "page_number": page_index,
                "text": text,
            }
        )

    return pages