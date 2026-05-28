from documents.processor import process_pdf


def main() -> None:
    pdf_path = "data/raw/sample_paper.pdf"

    output_file = process_pdf(
        file_path=pdf_path,
        output_dir="data/processed",
        chunk_size=1000,
        chunk_overlap=200,
    )

    print("PDF processed successfully.")
    print(f"Output saved to: {output_file}")


if __name__ == "__main__":
    main()