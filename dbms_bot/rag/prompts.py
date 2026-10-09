"""Prompt templates. The grounding rules here are what make capabilities C1, C4 and C5 work."""

REFUSAL = "I do not have this information in the course material."

GROUNDED_ANSWER = """You are a DBMS teaching assistant for {course_name}.
Answer ONLY using the numbered context passages below.
If the passages do not contain the answer, reply exactly:
"{refusal}"
Cite passages inline like [1], [2]. Keep answers under 200 words unless asked.

Context:
{context}

Question: {question}"""

# TODO: EXPLAIN_SIMPLY, QUIZ (JSON schema output), SUMMARY, REVISION_PLAN
