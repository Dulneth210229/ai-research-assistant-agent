from __future__ import annotations

from ollama import Client

from config.settings import settings
from embeddings.base import BaseEmbeddingProvider


class OllamaEmbeddingProvider(BaseEmbeddingProvider):
    """
    Ollama local embedding provider.
    Converts text into vectors using a locally installed Ollama embedding model.
    """

    def __init__(self) -> None:
        self.client = Client(host=settings.ollama_base_url)
        self.model = settings.ollama_embedding_model

    def embed_text(self, text: str) -> list[float]:
        response = self.client.embeddings(
            model=self.model,
            prompt=text,
        )

        return response["embedding"]

    def embed_documents(self, texts: list[str]) -> list[list[float]]:
        embeddings = []

        for text in texts:
            embedding = self.embed_text(text)
            embeddings.append(embedding)

        return embeddings