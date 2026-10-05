#!/usr/bin/env python3
"""Phases 3–4 — Fresh claim inventory from live DOCX (NOT limited to 328).

High-precision first: citation bullets, named books + numbers, Qur'an refs,
attribution formulas. Does NOT invent sources for unmatched narrative prose.

Claim_IDs: B1-C00001…
Outputs:
  audit/B1_P01-11_CLAIM_INVENTORY.csv
  manuscript-export/B1_P01-11_flagged_contexts.jsonl
"""
from __future__ import annotations

import csv
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
PARAS = ROOT / "manuscript-export" / "B1_P01-11_reader.paragraphs.jsonl"
RECON = ROOT / "audit" / "B1_P01-11_328_ROW_RECONCILIATION.csv"
OUT_CLAIMS = ROOT / "audit" / "B1_P01-11_CLAIM_INVENTORY.csv"
OUT_FLAGS = ROOT / "manuscript-export" / "B1_P01-11_flagged_contexts.jsonl"

# Bengali digits → ASCII
BN_DIGITS = str.maketrans("০১২৩৪৫৬৭৮৯", "0123456789")
WIN_PATH_RE = re.compile(r"[A-Za-z]:\\[^\s,\"']*")


def redact_windows_paths(s: str) -> str:
    return WIN_PATH_RE.sub("[LOCAL-PATH-REDACTED]", s) if s else s

SUNNI_BOOKS = [
    (r"সহীহ\s*বুখারি|বুখারি", "Sahih_al-Bukhari", "SUNNI"),
    (r"সহীহ\s*মুসলিম|মুসলিম", "Sahih_Muslim", "SUNNI"),
    (r"জামে\s*তিরমিযি|তিরমিযি", "Jami_al-Tirmidhi", "SUNNI"),
    (r"সুনানে?\s*আবু\s*দাউদ|আবু\s*দাউদ", "Sunan_Abu_Dawud", "SUNNI"),
    (r"সুনানে?\s*ইবনে?\s*মাজাহ|ইবনে?\s*মাজাহ", "Sunan_Ibn_Majah", "SUNNI"),
    (r"নাসাঈ|নাসায়ী", "Sunan_al-Nasai", "SUNNI"),
    (r"মুসনাদে?\s*আহমদ|মুসনাদ\s*আহমদ", "Musnad_Ahmad", "SUNNI"),
    (r"মুস্তাদরক|হাকিম", "Mustadrak_al-Hakim", "SUNNI"),
    (r"ত্ববারানী|তাবারানী", "al-Tabarani", "SUNNI"),
    (r"বায়হাকী|বাইহাকী", "al-Bayhaqi", "SUNNI"),
    (r"কানজুল?\s*উম্মাল|কানয", "Kanz_al-Ummal", "SUNNI"),
    (r"দুররুল?\s*মানসুর", "al-Durr_al-Manthur", "SUNNI"),
    (r"ইবনে?\s*সা.?দ|তবাকাত", "Ibn_Saad_Tabaqat", "SUNNI"),
    (r"ইস্তি.?আব|আল-ইস্তিআব", "al-Istiab", "SUNNI"),
    (r"ইসাবা|আল-ইসাবা", "al-Isabah", "SUNNI"),
    (r"বালাযুরী|বালাধুরী", "al-Baladhuri", "SUNNI"),
]

SHIA_BOOKS = [
    (r"আল-?কাফি|কাফি", "al-Kafi", "SHIA"),
    (r"বিহারুল?\s*আনওয়ার|বিহার", "Bihar_al-Anwar", "SHIA"),
    (r"ইহতিজাজ|আল-?ইহতিজাজ", "al-Ihtijaj", "SHIA"),
    (r"তাফসীরুল?\s*কুম্মী|কুম্মী", "Tafsir_al-Qummi", "SHIA"),
    (r"আইয়াশী", "Tafsir_al-Ayyashi", "SHIA"),
    (r"কামালুদ?\s*দীন|কামাল\s*আদ-দীন", "Kamal_al-Din", "SHIA"),
    (r"ইলালুশ?\s*শারা.?ই|ইলাল", "Ilal_al-Sharai", "SHIA"),
    (r"কুরবুল?\s*ইসনাদ", "Qurb_al-Isnad", "SHIA"),
    (r"কিতাব\s*সুল্লাইম|সুল্লাইম", "Kitab_Sulaym", "SHIA"),
    (r"আমালী|আল-?আমালী", "al-Amali", "SHIA"),
    (r"তাবিলুল?\s*আয়াত|তা'বিল", "Tawil_al-Ayat", "SHIA"),
    (r"নাহজুল?\s*বালাগা", "Nahj_al-Balagha", "SHIA"),
]

QURAN_RE = re.compile(
    r"(?:কুরআন|সূরা|আয়াত)?\s*(?:সূরা\s*)?([০-৯0-9]{1,3})\s*[:：]\s*([০-৯0-9]{1,3})"
)
HADITH_NUM_RE = re.compile(
    r"(?:হাদীস|হাদিস)?\s*(?:নং|নম্বর|number)?\s*([০-৯0-9]{1,5})"
)
BN_NUM_RE = re.compile(r"[০-৯]{1,5}")


def bn_to_int(s: str) -> str:
    return (s or "").translate(BN_DIGITS)


def load_paras() -> list[dict]:
    with PARAS.open(encoding="utf-8") as f:
        return [json.loads(line) for line in f]


def load_recon_by_para() -> dict[int, list[str]]:
    m: dict[int, list[str]] = {}
    if not RECON.exists():
        return m
    with RECON.open(encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row.get("Live_Para_Index", "").isdigit():
                idx = int(row["Live_Para_Index"])
                m.setdefault(idx, []).append(row["Row_ID"])
    return m


def detect_books(text: str) -> list[tuple[str, str]]:
    found = []
    for pat, name, trad in SUNNI_BOOKS + SHIA_BOOKS:
        if re.search(pat, text):
            found.append((name, trad))
    return found


def extract_quran_refs(text: str) -> list[str]:
    refs = []
    for m in QURAN_RE.finditer(text):
        refs.append(f"{bn_to_int(m.group(1))}:{bn_to_int(m.group(2))}")
    return refs


def extract_hadith_numbers_near_books(text: str) -> list[str]:
    """Pull numbers that appear near book names (high precision)."""
    nums = []
    for pat, name, _trad in SUNNI_BOOKS + SHIA_BOOKS:
        for m in re.finditer(pat, text):
            window = text[m.end() : m.end() + 40]
            for nm in BN_NUM_RE.findall(window) + re.findall(r"\b(\d{1,5})\b", window):
                nums.append(f"{name}:{bn_to_int(nm)}")
    # also «জামে তিরমিযি ৩৭৭৫» style already covered; add explicit হাদীস N
    for m in re.finditer(r"হাদীস\s*([০-৯0-9]{1,5})", text):
        nums.append(f"HADITH:{bn_to_int(m.group(1))}")
    return nums


def classify_claim(text: str, books: list[tuple[str, str]], qrefs: list[str], flags: list[str]) -> dict:
    traditions = sorted({t for _, t in books})
    if qrefs and not traditions:
        traditions = ["QURAN"]
    if "UMM_AYMAN" in flags:
        claim_family = "UMM_AYMAN"
    elif "FADAK" in flags:
        claim_family = "FADAK"
    elif qrefs:
        claim_family = "QURAN"
    elif any(t == "SHIA" for t in traditions) and any(t == "SUNNI" for t in traditions):
        claim_family = "MIXED_CITATION"
    elif "SHIA" in traditions:
        claim_family = "SHIA_NARRATION"
    elif "SUNNI" in traditions:
        claim_family = "SUNNI_NARRATION"
    elif "BARNITA_MARKER" in flags or "বর্ণিত আছে" in text:
        claim_family = "ATTRIBUTION_ONLY"
    elif "CITATION_BULLET" in flags and ("সূত্র নেই" in text or "খাতায় সূত্র নেই" in text):
        claim_family = "SOURCE_MISSING_NOTE"
    elif "CITATION_BULLET" in flags:
        claim_family = "SOURCE_BLOCK_NOTE"
    else:
        claim_family = "PROSE_ATTRIBUTION"

    # support class (SOURCE_EXISTENCE ≠ CLAIM_SUPPORT)
    if qrefs:
        support = "QURAN_REF"
    elif books:
        support = "NAMED_SOURCE"
    elif "সূত্র নেই" in text or "খাতায় সূত্র নেই" in text:
        support = "NO_SOURCE_STATED"
    elif "বর্ণিত আছে" in text:
        support = "ATTRIBUTION_FORMULA"
    else:
        support = "NARRATIVE_ONLY"

    precision = "HIGH"
    if claim_family in ("PROSE_ATTRIBUTION",) and support == "NARRATIVE_ONLY":
        precision = "LOW"
    elif claim_family == "ATTRIBUTION_ONLY":
        precision = "MEDIUM"

    return {
        "Claim_Family": claim_family,
        "Tradition": "|".join(traditions) if traditions else "UNSPECIFIED",
        "Support_Class": support,
        "Extraction_Precision": precision,
        "Books": "|".join(sorted({b for b, _ in books})),
        "Quran_Refs": "|".join(qrefs),
    }


def should_extract(text: str, flags: list[str]) -> bool:
    if not text.strip():
        return False
    # high-precision gates
    if text.strip().startswith("•"):
        # skip pure structural notes with no claim?
        if "কোনো আয়াত বা হাদীস উদ্ধৃত হয়নি" in text:
            return True  # still a control claim
        return True
    if "PAGE-CHECK" in text:
        return True
    if extract_quran_refs(text):
        return True
    if detect_books(text):
        return True
    if "বর্ণিত আছে" in text or "রাসূল" in text and "বলেছেন" in text:
        return True
    if "উম্মে আইমান" in text or "ফাদাক" in text:
        return True
    # flagged citation contexts
    if any(f in flags for f in ("CITATION_BULLET", "SUNNI_BOOK", "SHIA_BOOK", "SUTRA_MARKER")):
        return True
    return False


def infer_part_chapter(paras: list[dict], idx: int) -> tuple[str, str]:
    """Walk backward for part/chapter headings (heuristic)."""
    part, chapter = "", ""
    for j in range(idx, max(-1, idx - 80), -1):
        t = (paras[j]["text"] or "").strip()
        if not t:
            continue
        # Part headings often short with «ভাগ» or digit+title
        if re.match(r"^(ভাগ|PART)\s*[০-৯0-9]+", t) or re.match(r"^[০-৯0-9]{1,2}\s*$", t):
            if not part:
                part = t[:80]
        # Chapter: starts with Bengali digits like ০৬
        if re.match(r"^[০-৯]{2}\s+", t) and len(t) < 120:
            if not chapter:
                chapter = t[:120]
        if part and chapter:
            break
    return part, chapter


def main() -> None:
    paras = load_paras()
    recon = load_recon_by_para()
    claims = []
    flagged = []
    cid = 0

    for p in paras:
        text = p["text"] or ""
        flags = p.get("flags") or []
        if flags:
            flagged.append(p)
        if not should_extract(text, flags):
            continue
        books = detect_books(text)
        qrefs = extract_quran_refs(text)
        hnums = extract_hadith_numbers_near_books(text)
        meta = classify_claim(text, books, qrefs, flags)
        # skip pure narrative LOW unless bound to ledger or special
        if meta["Extraction_Precision"] == "LOW" and p["para_index"] not in recon:
            if not any(f in flags for f in ("UMM_AYMAN", "FADAK", "RASUL_SAID")):
                continue
        cid += 1
        part, chapter = infer_part_chapter(paras, p["para_index"])
        ledger_ids = "|".join(recon.get(p["para_index"], []))
        claims.append(
            {
                "Claim_ID": f"B1-C{cid:05d}",
                "Para_Index": p["para_index"],
                "Part_Guess": part,
                "Chapter_Guess": chapter,
                "Claim_Family": meta["Claim_Family"],
                "Tradition": meta["Tradition"],
                "Support_Class": meta["Support_Class"],
                "Extraction_Precision": meta["Extraction_Precision"],
                "Books_Named": meta["Books"],
                "Hadith_Numbers_Guess": "|".join(hnums),
                "Quran_Refs": meta["Quran_Refs"],
                "Flags": "|".join(flags),
                "Ledger_Row_IDs": ledger_ids,
                "Is_Source_Bullet": "YES" if text.strip().startswith("•") else "NO",
                "Text": redact_windows_paths(text),
                "Verification_Status": "PENDING",
                "Human_Decision": "",
            }
        )

    OUT_CLAIMS.parent.mkdir(parents=True, exist_ok=True)
    fields = list(claims[0].keys()) if claims else []
    with OUT_CLAIMS.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(claims)

    with OUT_FLAGS.open("w", encoding="utf-8") as f:
        for row in flagged:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")

    print(
        json.dumps(
            {
                "claims": len(claims),
                "flagged_contexts": len(flagged),
                "high": sum(1 for c in claims if c["Extraction_Precision"] == "HIGH"),
                "medium": sum(1 for c in claims if c["Extraction_Precision"] == "MEDIUM"),
                "low": sum(1 for c in claims if c["Extraction_Precision"] == "LOW"),
                "out": str(OUT_CLAIMS.relative_to(ROOT)),
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
