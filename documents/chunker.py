from typing import List

def chunk_text(text: str, chunk_size: int = 1000, chunk_overlap: int = 200) -> List[str]:
    """
    Split text into overlapping chunks.

    Args:
        text: Cleaned page text.
        chunk_size: Maximum number of characters in each chunk.
        chunk_overlap: Number of characters repeated between chunks.

    Returns:
        List of text chunks.
    """

    if not text:
        return []
    
    if chunk_overlap >= chunk_size:
        raise ValueError("chunk_overlap must be smaller than chunk_size to avoid infinite loops.")
    
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        start = end - chunk_overlap

    return chunks