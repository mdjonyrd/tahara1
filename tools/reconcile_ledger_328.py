#!/usr/bin/env python3
"""Phase 2 — Bind all 328 ledger rows to live DOCX paragraphs via text matching.

Input: audit/B1_P01-11_UNIDENTIFIED_REFERENCES_AUDIT_v1.0.csv (immutable anchors)
       manuscript-export/B1_P01-11_reader.paragraphs.jsonl
Output: audit/B1_P01-11_328_ROW_RECONCILIATION.csv
"""
from __future__ import annotations

import csv
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "audit" / "B1_P01-11_UNIDENTIFIED_REFERENCES_AUDIT_v1.0.csv"
LEDGER_V13 = ROOT / "audit" / "B1_P01-11_UNIDENTIFIED_REFERENCES_AUDIT_v1.3.csv"
PARAS = ROOT / "manuscript-export" / "B1_P01-11_reader.paragraphs.jsonl"
OUT = ROOT / "audit" / "B1_P01-11_328_ROW_RECONCILIATION.csv"


WIN_PATH_RE = re.compile(r"[A-Za-z]:\\[^\s,\"']*")


def redact_windows_paths(s: str) -> str:
    return WIN_PATH_RE.sub("[LOCAL-PATH-REDACTED]", s) if s else s


def norm(s: str) -> str:
    s = s or ""
    s = s.replace("\u200c", "").replace("\xa0", " ")
    s = re.sub(r"\s+", " ", s).strip()
    # strip common bullet / quote wrappers for matching
    s = s.lstrip("•").strip()
    s = s.strip("“”\"'‘’")
    return s


def load_paras() -> list[dict]:
    rows = []
    with PARAS.open(encoding="utf-8") as f:
        for line in f:
            rows.append(json.loads(line))
    return rows


def best_match(text: str, paras: list[dict], hint: int | None) -> tuple[int | None, str, float]:
    """Return (para_index, match_type, score)."""
    nt = norm(text)
    if not nt:
        return None, "EMPTY_LEDGER_TEXT", 0.0

    # 1) exact full-text match
    exact = [p for p in paras if norm(p["text"]) == nt]
    if exact:
        if hint is not None:
            near = [p for p in exact if abs(p["para_index"] - hint) <= 5]
            if near:
                return near[0]["para_index"], "EXACT", 1.0
        return exact[0]["para_index"], "EXACT", 1.0

    # 2) ledger text contained in paragraph or vice versa
    candidates: list[tuple[float, int, str]] = []
    # use a distinctive core (middle slice) for long texts
    core = nt if len(nt) <= 80 else nt[:60]
    core2 = nt[-60:] if len(nt) > 80 else nt

    search_range = paras
    if hint is not None:
        lo = max(0, hint - 40)
        hi = min(len(paras), hint + 40)
        search_range = paras[lo:hi]

    for p in search_range:
        pt = norm(p["text"])
        if not pt:
            continue
        if nt in pt or pt in nt:
            score = min(len(nt), len(pt)) / max(len(nt), len(pt))
            candidates.append((score, p["para_index"], "CONTAINS"))
        elif core and core in pt:
            candidates.append((0.85, p["para_index"], "PREFIX_CORE"))
        elif core2 and core2 in pt:
            candidates.append((0.8, p["para_index"], "SUFFIX_CORE"))

    if candidates:
        candidates.sort(key=lambda x: (-x[0], abs((hint or 0) - x[1])))
        sc, idx, mt = candidates[0]
        return idx, mt, sc

    # 3) global contains fallback
    for p in paras:
        pt = norm(p["text"])
        if nt and (nt in pt or (len(nt) > 40 and nt[:40] in pt)):
            return p["para_index"], "GLOBAL_CONTAINS", 0.7

    return None, "UNMATCHED", 0.0


def main() -> None:
    if not PARAS.exists():
        sys.exit("run export_docx_paragraphs.py first")
    paras = load_paras()

    # load v1.3 for enriched status if present
    v13: dict[str, dict] = {}
    if LEDGER_V13.exists():
        with LEDGER_V13.open(encoding="utf-8-sig") as f:
            for row in csv.DictReader(f):
                rid = row.get("Row_ID") or row.get("ID")
                if rid:
                    v13[rid] = row

    out_rows = []
    stats = {"EXACT": 0, "CONTAINS": 0, "PREFIX_CORE": 0, "SUFFIX_CORE": 0, "GLOBAL_CONTAINS": 0, "UNMATCHED": 0, "EMPTY_LEDGER_TEXT": 0}

    with LEDGER.open(encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rid = row.get("ID") or row.get("\ufeffID")
            try:
                hint = int(row["Paragraph_Index"])
            except (KeyError, ValueError):
                hint = None
            text = row.get("Text", "")
            idx, mtype, score = best_match(text, paras, hint)
            stats[mtype] = stats.get(mtype, 0) + 1
            live = paras[idx]["text"] if idx is not None else ""
            delta = "" if idx is None or hint is None else str(idx - hint)
            enriched = v13.get(rid or "", {})
            out_rows.append(
                {
                    "Row_ID": rid,
                    "Ledger_Paragraph_Index": row.get("Paragraph_Index", ""),
                    "Live_Para_Index": "" if idx is None else str(idx),
                    "Index_Delta": delta,
                    "Match_Type": mtype,
                    "Match_Score": f"{score:.3f}",
                    "Part": row.get("Part", ""),
                    "Chapter": row.get("Chapter", ""),
                    "Ledger_Status": row.get("Status", ""),
                    "Final_Status_v1_3": enriched.get("Final_Status", ""),
                    "Triage_v1_3": enriched.get("Triage", ""),
                    "Register_Key": enriched.get("Register_Key", ""),
                    "Ledger_Text": redact_windows_paths(text),
                    "Live_Text": redact_windows_paths(live),
                    "Text_Equal_Norm": "YES" if norm(text) == norm(live) and live else "NO",
                    "Bind_Status": "BOUND" if idx is not None else "UNBOUND",
                }
            )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    fields = list(out_rows[0].keys()) if out_rows else []
    with OUT.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(out_rows)

    bound = sum(1 for r in out_rows if r["Bind_Status"] == "BOUND")
    summary = {
        "total_rows": len(out_rows),
        "bound": bound,
        "unbound": len(out_rows) - bound,
        "match_types": stats,
        "out": str(OUT.relative_to(ROOT)),
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
