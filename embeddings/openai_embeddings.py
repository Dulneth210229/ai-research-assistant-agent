from __future__ import annotations

from openai import OpenAI

from config.settings import settings
from embeddings.base import BaseEmbeddingProvider


class OpenAIEmbeddingProvider(BaseEmbeddingProvider):
    """
    OpenAI embedding provider.
    Converts text into vectors using OpenAI embedding models.
    """

    def __init__(self) -> None:
        if not settings.openai_api_key or settings.openai_api_key == "your_openai_api_key_here":
            raise ValueError(
                "OpenAI API key is missing. Please set OPENAI_API_KEY in your .env file."
            )

        self.client = OpenAI(api_key=settings.openai_api_key)
        self.model = settings.openai_embedding_model

    def embed_text(self, text: str) -> list[float]:
        response = self.client.embeddings.create(
            model=self.model,
            input=text,
        )

        return response.data[0].embedding

    def embed_documents(self, texts: list[str]) -> list[list[float]]:
        response = self.client.embeddings.create(
            model=self.model,
            input=texts,
        )

        return [item.embedding for item in response.data]