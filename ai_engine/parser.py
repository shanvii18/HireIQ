import fitz  # PyMuPDF


def extract_text(file_bytes: bytes) -> str:
    """
    Extract text from PDF bytes.
    Framework-independent, safe, and reusable.
    """
    if not file_bytes:
        raise ValueError("Empty file provided")

    try:
        doc = fitz.open(stream=file_bytes, filetype="pdf")

        text_chunks = []
        for page in doc:
            text_chunks.append(page.get_text())

        return " ".join(text_chunks).strip()

    except Exception as e:
        raise ValueError(f"Failed to extract text from PDF: {str(e)}")