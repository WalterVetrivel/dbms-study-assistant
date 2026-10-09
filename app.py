"""Streamlit entry point. Run with:  streamlit run app.py

Starts as a minimal echo chat so you can learn st.chat_message / st.chat_input /
st.session_state first, then swap the echo for the agent (SPEC section 7.3).
"""

import streamlit as st

from dbms_bot.config import settings

st.set_page_config(page_title="DBMS Study Assistant", page_icon="🗄️")
st.title("🗄️ DBMS Study Assistant")

with st.sidebar:
    st.subheader(settings.course_name)
    st.caption(f"Model: {settings.ollama_model} · Embeddings: {settings.embedding_model}")
    st.caption("Answers are generated from course material and may contain errors. "
               "Verify with your notes.")

SUGGESTED = [
    "What is a candidate key?",
    "Explain BCNF to a first-year student",
    "Quiz me on transactions",
]

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

chip = st.pills("Try asking", SUGGESTED, selection_mode="single", key="chip")
prompt = st.chat_input("Ask about DBMS…") or chip

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    reply = f"(echo) {prompt}"  # TODO: replace with the agent call
    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.markdown(reply)
