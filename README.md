# 🗄️ DBMS Study Assistant

A local, CPU-only study assistant for **Database Management Systems**. It answers questions from course notes with page-level citations, explains hard concepts simply, generates 5-question MCQ quizzes, and says so when the material doesn't cover a question.

Built with Python, RAG (PyMuPDF, sentence-transformers, ChromaDB), a local LLM through Ollama, an MCP tool server, and Streamlit. Design: [SPEC.md](SPEC.md).

> Status: work in progress (FDP 14-day build).

## Requirements

- Python 3.11 or 3.12
- [Ollama](https://ollama.com) with `qwen3.5:4b` (or `qwen2.5:3b` on slower machines)
- About 8 GB RAM; no GPU needed

## Setup (Windows PowerShell)

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install torch --index-url https://download.pytorch.org/whl/cpu
pip install -r requirements.txt
copy .env.example .env
ollama pull qwen3.5:4b
```

## Usage

```powershell
# 1. Put PDFs in data/raw/{notes,syllabus,question_bank,textbooks}/
python scripts/inventory.py      # check page counts and text layers
python scripts/ingest.py         # build the vector store
streamlit run app.py             # open the chat UI
python scripts/evaluate.py       # run the 20-question test log
```

## Project layout

```
app.py              Streamlit UI
dbms_bot/           config, ingestion, RAG, LLM client, tools, MCP server, agent
scripts/            inventory, ingest, evaluate
data/raw/           source PDFs (textbooks are git-ignored)
data/sample/        small sample knowledge base you can publish
eval/               test questions and results
docs/               architecture diagram and project report
```

## Copyright note

Textbook PDFs and the vector store built from them are git-ignored and never published. Only the author's own notes in `data/sample/` are included.
