"""Step 2b: split page records into ~800-character chunks with overlap, keeping metadata.

Chunk id format: "{doc_id}:{page}:{n}" so re-ingesting is idempotent.
"""


def chunk_pages(pages: list[dict], size: int = 800, overlap: int = 120) -> list[dict]:
    """TODO: recursive split on paragraph -> line -> sentence; keep SQL blocks intact."""
    raise NotImplementedError
