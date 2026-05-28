from vectorstore.faiss_store import FAISSVectorStore


def main() -> None:
    chunks_file = "data/processed/sample_paper_chunks.json"

    vector_store = FAISSVectorStore()

    vector_store.build_from_chunks(
        chunks_file=chunks_file,
        index_output_path="data/processed/faiss.index",
        metadata_output_path="data/processed/faiss_metadata.pkl",
    )


if __name__ == "__main__":
    main()