from __future__ import annotations

from typing import Any


def build_context_from_chunks(chunks: list[dict[str, Any]]) -> str:
    """
    Convert retrieved chunks into a readable context block for the LLM.

    Args:
        chunks: Retrieved chunks from FAISS search.

    Returns:
        A formatted context string.
    """

    context_parts = []

    for index, chunk in enumerate(chunks, start=1):
        source_file = chunk["source_file"]
        page_number = chunk["page_number"]
        text = chunk["text"]

        context_parts.append(
            f"[Source {index}]\n"
            f"File: {source_file}\n"
            f"Page: {page_number}\n"
            f"Content:\n{text}"
        )

    return "\n\n".join(context_parts)


def build_rag_prompt(question: str, chunks: list[dict[str, Any]]) -> str:
    """
    Build the final RAG prompt using the user question and retrieved document chunks.

    Args:
        question: User's question.
        chunks: Retrieved chunks from vector search.

    Returns:
        A complete prompt for the LLM.
    """

    context = build_context_from_chunks(chunks)

    prompt = f"""
You are an AI Research Assistant Agent.

Your task is to answer the user's question using ONLY the provided document context.

Rules:
1. Use only the provided context.
2. If the answer is not available in the context, say:
   "I could not find enough information in the provided document context."
3. Do not invent facts.
4. Write the answer clearly and simply.
5. When using information from a source, mention the source number like [Source 1].
6. At the end, provide a short "Sources Used" section.

Document Context:
{context}

User Question:
{question}

Answer:
"""

    return prompt.strip()