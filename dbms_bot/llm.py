"""Provider abstraction so the same agent runs on local Ollama or a hosted OpenAI-compatible API."""


def chat(messages: list[dict], tools: list[dict] | None = None, stream: bool = False,
         format: dict | None = None):
    """TODO: if settings.llm_provider == "ollama": ollama.Client(host).chat(
    model, messages, tools=tools, stream=stream, format=format, think=False,
    options={"num_ctx": ..., "temperature": ...}). Else: OpenAI-compatible HTTP call."""
    raise NotImplementedError
