import json
from pathlib import Path
from typing import Any

from documents.loader import load_pdf_text
from documents.cleaner import clean_text
from documents.chunker import chunk_text


def process_pdf(file_path: str, output_dir: str = "data/processed", chunk_size: int = 1000, chunk_overlap: int = 200,) -> str:
    """
    Process a PDF into cleaned text chunks with metadata.

    Args:
        file_path: PDF file path.
        output_dir: Directory where processed JSON will be saved.
        chunk_size: Maximum characters per chunk.
        chunk_overlap: Overlap between chunks.

    Returns:
        Path to the saved JSON file.
    """

    pdf_path = Path(file_path)
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    pages = load_pdf_text(file_path)
    all_chunks: list[dict[str, Any]] = []

    for page in pages:
        page_number = page["page_number"]
        raw_text = page["text"]

        cleaned_text = clean_text(raw_text)

        chunks = chunk_text(
            cleaned_text,
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
        )

        for chunk_index, chunk in enumerate(chunks, start=1):
            all_chunks.append(
                {
                    "chunk_id": f"{pdf_path.stem}_p{page_number}_c{chunk_index}",
                    "source_file": pdf_path.name,
                    "page_number": page_number,
                    "chunk_index": chunk_index,
                    "text": chunk,
                    "metadata": {
                        "source_path": str(pdf_path),
                        "document_type": "pdf",
                    },
                }
            )

    output_file = output_path / f"{pdf_path.stem}_chunks.json"

    with output_file.open("w", encoding="utf-8") as file:
        json.dump(all_chunks, file, indent=2, ensure_ascii=False)

    return str(output_file)