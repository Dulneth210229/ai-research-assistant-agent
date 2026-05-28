from vectorstore.faiss_store import FAISSVectorStore


def main() -> None:
    vector_store = FAISSVectorStore()

    vector_store.load(
        index_path="data/processed/faiss.index",
        metadata_path="data/processed/faiss_metadata.pkl",
    )

    print("Semantic search is ready. Type 'exit' to stop.")
    print()

    while True:
        query = input("Search query: ")

        if query.lower().strip() in ["exit", "quit"]:
            print("Goodbye!")
            break

        results = vector_store.search(query=query, top_k=3)

        print()
        print("Top Results:")
        print("=" * 60)

        for number, result in enumerate(results, start=1):
            print(f"\nResult {number}")
            print(f"Source: {result['source_file']}")
            print(f"Page: {result['page_number']}")
            print(f"Chunk ID: {result['chunk_id']}")
            print(f"Distance Score: {result['score']}")
            print("-" * 60)
            print(result["text"][:700])
            print("-" * 60)

        print()


if __name__ == "__main__":
    main()