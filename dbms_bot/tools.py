"""Plain-Python tool implementations. mcp_server.py wraps these; tests call them directly."""


def search_notes(query: str, top_k: int = 4) -> list[dict]:
    """Return the most relevant course passages with source metadata."""
    raise NotImplementedError


def answer_question(question: str) -> dict:
    """Answer from course material. Returns {answer, sources, refused}. (C1, C4, C5)"""
    raise NotImplementedError


def explain_topic(topic: str, level: str = "first-year student") -> dict:
    """Explain a concept simply, still grounded in the notes. (C2)"""
    raise NotImplementedError


def generate_quiz(topic: str, num_questions: int = 5) -> dict:
    """Five MCQs with 4 options, the answer and a one-line explanation each. (C3)"""
    raise NotImplementedError


def summarize_topic(topic: str) -> dict:
    """Lesson summary for a unit or topic."""
    raise NotImplementedError
