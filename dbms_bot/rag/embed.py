"""Step 3a: sentence-transformers embedding wrapper (bge-small-en-v1.5 by default)."""

# bge models expect this prefix on queries (not on documents).
QUERY_PREFIX = "Represent this sentence for searching relevant passages: "


def embed_documents(texts: list[str]) -> list[list[float]]:
    """TODO: load SentenceTransformer(settings.embedding_model) once; normalize_embeddings=True."""
    raise NotImplementedError


def embed_query(text: str) -> list[float]:
    """TODO: embed QUERY_PREFIX + text."""
    raise NotImplementedError
