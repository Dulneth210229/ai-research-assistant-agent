from __future__ import annotations

from config.settings import settings
from embeddings.base import BaseEmbeddingProvider
from embeddings.openai_embeddings import OpenAIEmbeddingProvider
from embeddings.ollama_embeddings import OllamaEmbeddingProvider


def get_embedding_provider() -> BaseEmbeddingProvider:
    """
    Return selected embedding provider based on EMBEDDING_PROVIDER in .env.
    """

    if settings.embedding_provider == "openai":
        return OpenAIEmbeddingProvider()

    if settings.embedding_provider == "ollama":
        return OllamaEmbeddingProvider()

    raise ValueError(
        f"Unsupported EMBEDDING_PROVIDER '{settings.embedding_provider}'. "
        "Use 'openai' or 'ollama'."
    )