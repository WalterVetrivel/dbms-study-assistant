"""Step 2a: extract text from PDFs, one record per page, with metadata.

Each record: {doc_id, file_name, doc_type, page, chapter, text}
doc_type comes from the subfolder name: notes | syllabus | question_bank | textbook.
"""

from pathlib import Path


def extract_pdf(path: Path, doc_type: str) -> list[dict]:
    """Return one record per page. TODO: PyMuPDF, strip headers/footers, detect chapter headings."""
    raise NotImplementedError
