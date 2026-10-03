#!/usr/bin/env python3
"""Apply source-verification resolutions to the unidentified-reference ledger.

Input : audit/B1_P01-11_UNIDENTIFIED_REFERENCES_AUDIT_v1.0.csv  (never modified)
Output: audit/B1_P01-11_UNIDENTIFIED_REFERENCES_AUDIT_v1.1.csv  (S-181 resolutions)
        audit/B1_P01-11_UNIDENTIFIED_REFERENCES_AUDIT_v1.2.csv  (v1.1 + per-row triage)

The original columns (ID, Paragraph_Index, Part, Chapter, Status, Text) are copied
verbatim. Three columns are appended:
  Status_v1_1      - current QA status after the listed resolution (or the original
                     Status, unchanged, for rows with no resolution yet)
  Resolution_Ref   - the source-verification file / section that justifies the change
  Resolution_Note  - one-line summary of what changed and what is still pending

Two-phase rule: the resolutions live in RESOLUTIONS below (data), the transform is
generic. Add a new entry per resolved REF-ID; never edit v1.0 by hand.
"""
import csv
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "audit" / "B1_P01-11_UNIDENTIFIED_REFERENCES_AUDIT_v1.0.csv"
DST = ROOT / "audit" / "B1_P01-11_UNIDENTIFIED_REFERENCES_AUDIT_v1.1.csv"
DST12 = ROOT / "audit" / "B1_P01-11_UNIDENTIFIED_REFERENCES_AUDIT_v1.2.csv"

S181 = "sources/S-181_UMM_AYMAN_FADAK_VERIFICATION.md"
PATCH = "manuscript-patches/B1_P03_C06_FADAK_S-181_PATCH.md"

RESOLUTIONS = {
    "REF-078": (
        "ATTRIBUTED; EDITION-LOCK PENDING",
        f"{S181} §3-D; {PATCH} A-3",
        "«লিখেও দিয়ে গেছেন» = al-Ihtijaj recension (Abu Bakr writes the deed, Umar tears it). "
        "Keep «বর্ণিত আছে» in dialogue; source block must attribute to al-Tabrisi, al-Ihtijaj vol. 1 "
        "(edition/page to lock). Do not merge with Baladhuri recension.",
    ),
    "REF-079": (
        "VERIFIED (numbers); GRADING CORRECTED",
        f"{S181} §4 (last row); {PATCH} B; audit BUG-01",
        "Abu Dawud 2968 and 2972 numbers confirmed (sunnah.com). Grading of 2972 is al-Albani's Da'if, "
        "not Abu Dawud's own — rewrite «আবু দাউদের মতে» → «আল-আলবানীর মতে». Bukhari 4240–4241 already CONFIRMED.",
    ),
    "REF-081": (
        "VERIFIED (split 081a/081b); EDITION-LOCK PENDING",
        f"{S181} §3-A..3-E; {PATCH} A-3, B",
        "081a Ali + Umm Ayman testimony: VERIFIED in Sunni primary (Baladhuri, Futuh al-Buldan, two recensions) "
        "and Shia (al-Ihtijaj 1; Kitab Sulaym; Ibn Abi al-Hadid, Sharh 16/213-214, 216, 225, 273-275). "
        "081b Aus ibn al-Hadathan: NOT Umm Ayman's witness — counter-testimony with Aisha and Hafsa on «لا نورث» "
        "(Qurb al-Isnad; Bihar 22/101 h.59). Separate in prose and source block. Edition pages to lock.",
    ),
    "REF-082": (
        "FOUND — MURSAL (Ibn Sa'd); Bihar 29 VERIFIED; Hakim NOT VERIFIED",
        f"{S181} §2; {PATCH} A-2, B; audit BUG-03",
        "Wording «من سره أن يتزوج امرأة من أهل الجنة فليتزوج أم أيمن» exists in Ibn Sa'd, Tabaqat (Sufyan ibn Uqbah; "
        "mursal; al-Suyuti mursal, al-Albani da'if). Must be written as «ইবনে সা'দের একটি মুরসাল বর্ণনায়», never as sahih. "
        "Shia wording «إن أم أيمن امرأة من أهل الجنة» VERIFIED in Bihar vol. 29 (p.128/176 — pick one edition). "
        "Hakim/Mustadrak: no reference found — PRINT BLOCKED for any Hakim attribution.",
    ),
}


def main() -> int:
    with SRC.open(encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh)
        rows = list(reader)
        base_cols = list(reader.fieldnames)

    out_cols = base_cols + ["Status_v1_1", "Resolution_Ref", "Resolution_Note"]
    applied = []
    for row in rows:
        res = RESOLUTIONS.get(row["ID"])
        if res:
            row["Status_v1_1"], row["Resolution_Ref"], row["Resolution_Note"] = res
            applied.append(row["ID"])
        else:
            row["Status_v1_1"] = row["Status"]
            row["Resolution_Ref"] = ""
            row["Resolution_Note"] = ""

    missing = sorted(set(RESOLUTIONS) - set(applied))
    if missing:
        print(f"ERROR: resolutions reference unknown IDs: {missing}", file=sys.stderr)
        return 1

    with DST.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=out_cols)
        writer.writeheader()
        writer.writerows(rows)

    # ---- v1.2: per-row triage (tools/triage_v1_2.py) ----
    sys.path.insert(0, str(ROOT / "tools"))
    from triage_v1_2 import T, CODES
    cols12 = out_cols + ["Triage", "Triage_Label", "Candidate_Source", "Register_Key", "Audit_Note"]
    for row in rows:
        code, cand, reg, note = T[row["ID"]]
        row["Triage"], row["Triage_Label"] = code, CODES[code]
        row["Candidate_Source"], row["Register_Key"], row["Audit_Note"] = cand, reg, note
    with DST12.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=cols12)
        writer.writeheader()
        writer.writerows(rows)
    print(f"wrote   : {DST12.relative_to(ROOT)}  (triage rows: {sum(1 for r in rows if r['Triage'])})")
    print(f"rows in : {len(rows)}")
    print(f"rows out: {len(rows)}")
    print(f"applied : {', '.join(applied)}")
    print(f"wrote   : {DST.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
