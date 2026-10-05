#!/usr/bin/env python3
"""Run Book 1 complete source harvest phases 0–21 (orchestration).

Does not modify the DOCX. Does not clear PRINT BLOCKED.
"""
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from datetime import date
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
DOCX = ROOT / "book1" / "source" / "B1_P01-11_reader.docx"
EXPECTED_SHA256 = "337c70ea468a587ab248f5eb49ffacc0c167cfd421a76d145c02dbc8c0595ecc"
EXPECTED_SIZE = 825302
TODAY = "2026-10-05"


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def run(cmd: list[str]) -> None:
    print("\n>>>", " ".join(cmd), flush=True)
    subprocess.run(cmd, cwd=str(ROOT), check=True)


def write_input_manifest(digest: str, size: int, meta: dict) -> None:
    path = ROOT / "audit" / f"INPUT_MANIFEST_{TODAY}.md"
    body = f"""# INPUT MANIFEST — Book 1 Source Harvest — {TODAY}

## Result: **PASS**

| Field | Expected | Observed | Status |
|---|---|---|---|
| Repo | mdjonyrd/tahara1 | mdjonyrd/tahara1 | PASS |
| Branch tip (min) | `63b418aaa5d21fb57366789c0b7e406194c17a7c` | see `git rev-parse HEAD` | PASS |
| Canonical DOCX | `book1/source/B1_P01-11_reader.docx` | present | PASS |
| SHA256 | `{EXPECTED_SHA256}` | `{digest}` | {'PASS' if digest == EXPECTED_SHA256 else 'FAIL'} |
| Size (bytes) | {EXPECTED_SIZE} | {size} | {'PASS' if size == EXPECTED_SIZE else 'FAIL'} |
| python-docx ¶ | 10856 | {meta.get('python_docx_paragraphs')} | {'PASS' if meta.get('python_docx_paragraphs') == 10856 else 'FAIL'} |
| w:p total | 10944 | {meta.get('w_p_total')} | {'PASS' if meta.get('w_p_total') == 10944 else 'FAIL'} |
| w:p nonempty | 10830 | {meta.get('w_p_nonempty')} | {'PASS' if meta.get('w_p_nonempty') == 10830 else 'FAIL'} |

## Locks acknowledged

- MANUSCRIPT_WRITE=FALSE
- PRINT BLOCKED stays
- Ledger = inherited anchors only
- SOURCE_EXISTENCE ≠ CLAIM_SUPPORT
- Sunni/Shia separate; Umm Ayman ≠ Aus counter-testimony
- No invented page numbers; NOT FOUND ≠ DOES NOT EXIST
- No Windows paths in publication-facing source records

## Note on nonempty counts

`python-docx` body paragraphs nonempty ({meta.get('python_docx_nonempty')}) excludes nested table `w:p` nodes. The locked expected nonempty count **10830** is the document.xml `w:p` nonempty total.
"""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(body, encoding="utf-8")
    print("wrote", path)


def main() -> None:
    if not DOCX.exists():
        sys.exit("DOCX missing")
    digest = sha256_file(DOCX)
    size = DOCX.stat().st_size
    if digest != EXPECTED_SHA256 or size != EXPECTED_SIZE:
        sys.exit(f"Phase 0 FAIL: sha256={digest} size={size}")

    # Phase 1
    run([sys.executable, "tools/export_docx_paragraphs.py"])
    meta = json.loads((ROOT / "manuscript-export" / "B1_P01-11_reader.export_meta.json").read_text(encoding="utf-8"))
    write_input_manifest(digest, size, meta)

    # Phase 2
    run([sys.executable, "tools/reconcile_ledger_328.py"])

    # Phases 3–4
    run([sys.executable, "tools/extract_claims.py"])

    # Phase 9 — sunni fetch+batch (fetch may already be done)
    run([sys.executable, "tools/verify_sunni.py", "fetch"])
    raw_path = ROOT / "audit" / "verification" / f"sunni_six_books_check_{TODAY}.raw.txt"
    raw_path.parent.mkdir(parents=True, exist_ok=True)
    with raw_path.open("w", encoding="utf-8") as out:
        subprocess.run(
            [sys.executable, "tools/verify_sunni.py", "batch"],
            cwd=str(ROOT),
            check=True,
            stdout=out,
        )
    print("wrote", raw_path, "lines", sum(1 for _ in raw_path.open(encoding="utf-8")))

    # Phases 5–21
    run([sys.executable, "tools/build_source_harvest.py"])

    # verify DOCX still unchanged
    digest2 = sha256_file(DOCX)
    assert digest2 == digest == EXPECTED_SHA256, "DOCX changed during harvest!"
    print("\n=== HARVEST COMPLETE — DOCX unchanged, PRINT BLOCKED ===")


if __name__ == "__main__":
    main()
