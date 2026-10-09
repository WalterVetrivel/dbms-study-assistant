"""List every PDF under data/raw with page count and whether it has a text layer.

Use the output to choose the ingest subset (SPEC section 6).
Run:  python scripts/inventory.py [folder]
"""

import sys
from pathlib import Path

import pymupdf

DEFAULT_ROOT = Path(__file__).resolve().parent.parent / "data" / "raw"
root = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_ROOT

print(f"{'folder':<16}{'pages':>6}  {'text?':<6} file")
for pdf in sorted(root.rglob("*.pdf")):
    try:
        with pymupdf.open(pdf) as doc:
            sample = [doc[i] for i in range(0, doc.page_count, max(1, doc.page_count // 5))][:5]
            has_text = any(len(p.get_text().strip()) > 50 for p in sample)
            flag = "yes" if has_text else "NO"
            print(f"{pdf.parent.name:<16}{doc.page_count:>6}  {flag:<6} {pdf.name}")
    except Exception as exc:  # noqa: BLE001
        print(f"{pdf.parent.name:<16}{'?':>6}  {'err':<6} {pdf.name} ({exc})")
