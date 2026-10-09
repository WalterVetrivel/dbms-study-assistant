"""Build or refresh the vector store: extract -> chunk -> embed -> upsert into ChromaDB.

Run:  python scripts/ingest.py
TODO: walk settings.raw_dir subfolders (notes, syllabus, question_bank, textbooks),
      call dbms_bot.ingest.extract / chunk, dbms_bot.rag.embed / store, print chunk counts.
"""
