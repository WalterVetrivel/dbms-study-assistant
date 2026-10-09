"""Central settings, loaded from environment variables and .env (see .env.example)."""

from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

ROOT = Path(__file__).resolve().parent.parent


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=ROOT / ".env", extra="ignore")

    course_name: str = "Database Management Systems"

    # LLM
    llm_provider: str = "ollama"  # "ollama" | "openai_compat"
    ollama_host: str = "http://localhost:11434"
    ollama_model: str = "qwen3.5:4b"
    num_ctx: int = 4096
    temperature: float = 0.2
    openai_compat_base_url: str = ""
    openai_compat_api_key: str = ""
    openai_compat_model: str = ""

    # Embeddings and retrieval
    embedding_model: str = "BAAI/bge-small-en-v1.5"
    chroma_dir: Path = ROOT / "data" / "chroma"
    collection_name: str = "dbms"
    chunk_size: int = 800
    chunk_overlap: int = 120
    top_k: int = 4
    relevance_threshold: float = 0.45

    # Source material
    raw_dir: Path = ROOT / "data" / "raw"


settings = Settings()
