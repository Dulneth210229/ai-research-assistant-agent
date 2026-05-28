from __future__ import annotations

import json
import pickle
from pathlib import Path
from typing import Any

import faiss
import numpy as np

from embeddings.factory import get_embedding_provider


class FAISSVectorStore:
    """
    FAISS-based vector store for semantic search.
    """

    def __init__(self) -> None:
        self.embedding_provider = get_embedding_provider()
        self.index = None
        self.documents: list[dict[str, Any]] = []

    def build_from_chunks(self, chunks_file: str, index_output_path: str = "data/processed/faiss.index", metadata_output_path: str = "data/processed/faiss_metadata.pkl") -> None:
        chunks_path = Path(chunks_file)

        if not chunks_path.exists():
            raise FileNotFoundError(f"Chunks file not found: {chunks_file}")

        with chunks_path.open("r", encoding="utf-8") as file:
            chunks = json.load(file)

        if not chunks:
            raise ValueError("Chunks file is empty. Cannot build FAISS index.")

        texts = [chunk["text"] for chunk in chunks]

        print(f"Creating embeddings for {len(texts)} chunks...")
        embeddings = self.embedding_provider.embed_documents(texts)

        embedding_array = np.array(embeddings).astype("float32")

        dimension = embedding_array.shape[1]

        self.index = faiss.IndexFlatL2(dimension)
        self.index.add(embedding_array)

        self.documents = chunks

        faiss.write_index(self.index, index_output_path)

        with open(metadata_output_path, "wb") as file:
            pickle.dump(self.documents, file)

        print("FAISS index created successfully.")
        print(f"Index saved to: {index_output_path}")
        print(f"Metadata saved to: {metadata_output_path}")

    def load(self, index_path: str = "data/processed/faiss.index", metadata_path: str = "data/processed/faiss_metadata.pkl") -> None:
        if not Path(index_path).exists():
            raise FileNotFoundError(f"FAISS index not found: {index_path}")

        if not Path(metadata_path).exists():
            raise FileNotFoundError(f"Metadata file not found: {metadata_path}")

        self.index = faiss.read_index(index_path)

        with open(metadata_path, "rb") as file:
            self.documents = pickle.load(file)

    def search(self, query: str, top_k: int = 3) -> list[dict[str, Any]]:
        if self.index is None:
            raise ValueError("FAISS index is not loaded. Call load() first.")

        query_embedding = self.embedding_provider.embed_text(query)
        query_vector = np.array([query_embedding]).astype("float32")

        distances, indices = self.index.search(query_vector, top_k)

        results = []

        for distance, index in zip(distances[0], indices[0]):
            if index == -1:
                continue

            document = self.documents[index]

            results.append(
                {
                    "score": float(distance),
                    "chunk_id": document["chunk_id"],
                    "source_file": document["source_file"],
                    "page_number": document["page_number"],
                    "chunk_index": document["chunk_index"],
                    "text": document["text"],
                    "metadata": document["metadata"],
                }
            )

        return results