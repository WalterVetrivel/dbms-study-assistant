"""Step 3b: ChromaDB wrapper (persistent client, cosine distance)."""


def upsert_chunks(chunks: list[dict], embeddings: list[list[float]]) -> None:
    """TODO: chromadb.PersistentClient(settings.chroma_dir); collection with hnsw:space=cosine."""
    raise NotImplementedError


def search(query_embedding: list[float], top_k: int = 4) -> list[dict]:
    """TODO: return [{text, metadata, score}] with score = 1 - cosine distance."""
    raise NotImplementedError
