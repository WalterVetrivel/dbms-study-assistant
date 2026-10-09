"""Agent loop: MCP client -> list tools -> let the model pick one -> call it.

Reliability layers for a small CPU model (SPEC section 4.3):
  1. native tool calling, 2. validate + retry once, 3. keyword fallback router.
"""

import re

FALLBACK_ROUTES = [
    (re.compile(r"\b(quiz|mcq|test me)\b", re.I), "generate_quiz"),
    (re.compile(r"\b(summar\w*|overview|recap)\b", re.I), "summarize_topic"),
    (re.compile(r"\b(explain|simple|simply|eli5|beginner)\b", re.I), "explain_topic"),
]


def route_by_keyword(message: str) -> str:
    """Layer 3: pick a tool name from keywords; default to answer_question."""
    for pattern, tool in FALLBACK_ROUTES:
        if pattern.search(message):
            return tool
    return "answer_question"


async def run_agent(message: str) -> dict:
    """TODO: open an MCP ClientSession (stdio_client or streamablehttp_client), list_tools,
    convert schemas to Ollama tools=[...], chat, call_tool, fall back to route_by_keyword."""
    raise NotImplementedError
