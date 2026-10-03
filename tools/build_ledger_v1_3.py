#!/usr/bin/env python3
"""Build ledger v1.3 (Phase 12) by joining ledger v1.2 with the control tables.

Inputs (missing control files are tolerated: their columns stay 'pending'):
  audit/B1_P01-11_UNIDENTIFIED_REFERENCES_AUDIT_v1.2.csv          (required)
  audit/B1_P01-11_CROSS_ROW_MISMATCHES_v1.0.csv                   -> Cross_Row_Mismatch
  audit/B1_P01-11_GRADING_CONTROL_v1.0.csv                        -> Grading
  audit/B1_P01-11_UNIDENTIFIED_ROWS_DECISIONS_v1.0.csv            -> UNID Final_Status / Verified_Source
  audit/B1_P01-11_SOURCE_REGISTER_v1.1.csv                        -> register normalisation rule
Output:
  audit/B1_P01-11_UNIDENTIFIED_REFERENCES_AUDIT_v1.3.csv  (all 328 rows, 23 columns)
No row is ever dropped. Nothing is upgraded to VERIFIED unless the v1.2 triage is VL
(live six-book check) or S181 (URL-backed S-181 report).
"""
import csv, re, sys
from pathlib import Path
from collections import defaultdict
sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parent.parent
A = ROOT / "audit"

def read(name):
    p = A / name
    if not p.exists():
        print(f"  (missing, columns stay pending) {name}"); return []
    with p.open(encoding="utf-8-sig", newline="") as fh:
        return list(csv.DictReader(fh))

rows = read("B1_P01-11_UNIDENTIFIED_REFERENCES_AUDIT_v1.2.csv")
assert len(rows) == 328, len(rows)
xrm = read("B1_P01-11_CROSS_ROW_MISMATCHES_v1.0.csv")
grd = read("B1_P01-11_GRADING_CONTROL_v1.0.csv")
und = read("B1_P01-11_UNIDENTIFIED_ROWS_DECISIONS_v1.0.csv")
reg = read("B1_P01-11_SOURCE_REGISTER_v1.1.csv")

REF = re.compile(r"REF-\d{3}")
xr_by_row = defaultdict(list)
for m in xrm:
    for r in set(REF.findall(m.get("Row_A","") + " " + m.get("Row_B",""))):
        xr_by_row[r].append(m.get("Mismatch_ID",""))
gr_by_row = defaultdict(list)
for g in grd:
    for r in set(REF.findall(g.get("Row_IDs",""))):
        gr_by_row[r].append(f'{g.get("Book","")} {g.get("Hadith_Number","")}: {g.get("Graders_and_Grades","")} → {g.get("Safety_Class","")}')
und_by_row = {u["Row_ID"]: u for u in und if u.get("Row_ID")}
reg_by_key = {r["Register_Key"]: r for r in reg if r.get("Register_Key")}

SIX = {"bukhari":"Sahih al-Bukhari","muslim":"Sahih Muslim","abu dawud":"Sunan Abi Dawud","abudawud":"Sunan Abi Dawud",
       "tirmidhi":"Jami' al-Tirmidhi","ibn majah":"Sunan Ibn Majah","nasa'i":"Sunan al-Nasa'i"}
SIX_RE = re.compile(r"\b(Bukhari|Muslim|Abu Dawud|Tirmidhi|Ibn Majah|Nasa'i)\s+(\d{1,4})", re.I)
SHIA_RE = re.compile(r"(al-Kafi|Bihar al-Anwar|Bihar|'Ilal al-Shara'i'|Kamal al-Din|Tafsir al-Qummi|Tafsir al-Ayyashi|al-Ihtijaj|Nahj al-Balagha|'Uyun Akhbar al-Rida|Ma'ani al-Akhbar|Tahdhib al-Ahkam|Shawahid al-Tanzil|al-Mustadrak|al-Hakim|Tabarani|Durr al-Manthur|Kashshaf)[^;,.]*?(\d{1,3}):(\d{1,4})")

def first_six(text):
    m = SIX_RE.search(text or "")
    return (SIX[m.group(1).lower()], m.group(2)) if m else ("", "")
def first_shia(text):
    m = SHIA_RE.search(text or "")
    return (m.group(1), m.group(2), m.group(3)) if m else ("", "", "")

FINAL = {
 "VL":   "VERIFIED (six-book number + text, 2026-10-03); grade/edition per control tables",
 "MM":   "CORRECTED — manuscript patch pending",
 "EDN":  "EDITION-NUMBER MAP PENDING (use standard numbering)",
 "CAND": "CANDIDATE — PAGE-CHECK (not live-verifiable here)",
 "SPC":  "PAGE-CHECK (Shia source; edition/page lock)",
 "UNID": "NOT VERIFIED / SOURCE-MISSING",
 "DUP":  "NORMALISE via register key",
 "PROSE":"PROSE — follows source-block row",
 "HIST": "NON-HADITH — PAGE-CHECK",
 "S181": "S-181: VERIFIED-S181-URL / EDITION-LOCK PENDING",
 "Q":    "QURAN TEXT CHECK",
}
HUMAN_YES = {"MM","UNID","S181","EDN","DUP","CAND","SPC","PROSE"}

out_cols = ["Row_ID","Part","Chapter","Page","Exact_Text","Current_Reference","Current_Status","Triage","Candidate_Source",
            "Verified_Source","Book","Volume","Page_or_Hadith","Edition","Hadith_Number","Grading","Claim_Support",
            "Cross_Row_Mismatch","Register_Key","Required_Action","Audit_Note","Human_Review","Final_Status"]
out = []
for r in rows:
    code = r["Triage"]; cand = r["Candidate_Source"]; rid = r["ID"]
    book, num = first_six(cand)
    sbook, svol, spage = first_shia(cand)
    verified = ""
    if code == "VL" and book: verified = f"{book} {num} (live six-book check 2026-10-03)"
    elif code == "S181": verified = "sources/S-181_UMM_AYMAN_FADAK_VERIFICATION.md (URL-backed; edition lock pending)"
    elif code in ("MM","EDN") and book and ("VL" in cand or "verified" in cand.lower()): verified = f"{book} {num} (live six-book check — corrected target)"
    u = und_by_row.get(rid)
    if u and u.get("Classification") == "CANONICAL_SOURCE_FOUND":
        verified = f'{u.get("Book","")} {u.get("Hadith_Number","")} (live six-book check via UNID decisions)'
    if code == "UNID" and u:
        final = f'{u.get("Classification","")} — {u.get("Recommended_Manuscript_Handling","")}'.strip(" —")
    else:
        final = FINAL[code]
    reg_rule = ""
    for k in [x.strip() for x in r["Register_Key"].split(";") if x.strip()]:
        if k in reg_by_key: reg_rule += f'[{k}] {reg_by_key[k].get("Normalisation_Rule","")} '
    claim = {"VL":"number+text confirmed; claim-support class in SUNNI_VERIFICATION_EVIDENCE_v1.1",
             "MM":"NO — citation does not support the sentence as written","EDN":"supported; number is edition-specific",
             "CAND":"not verifiable here","SPC":"not verifiable here","UNID":"NONE located","DUP":"see register key",
             "PROSE":"follows source-block row","HIST":"non-hadith","S181":"per S-181 §4 table","Q":"Quran text"}[code]
    out.append({
        "Row_ID": rid, "Part": r["Part"], "Chapter": r["Chapter"].strip(),
        "Page": f'PAGE-CHECK (docx not available); ¶{r["Paragraph_Index"]}',
        "Exact_Text": r["Text"].strip(), "Current_Reference": r["Text"].strip().lstrip("•").strip(),
        "Current_Status": r["Status_v1_1"], "Triage": f'{code} {r["Triage_Label"]}', "Candidate_Source": cand,
        "Verified_Source": verified,
        "Book": book or sbook or (u.get("Book","") if u else ""),
        "Volume": svol or (u.get("Volume","") if u else ""),
        "Page_or_Hadith": (num or spage) or (u.get("Page_or_Report","") if u else "") or ("PAGE-CHECK" if code in ("CAND","SPC","HIST") else ""),
        "Edition": "standard numbering (sunnah.com / Abd al-Baqi)" if code == "VL" and book else ("EDITION NOT LOCKED" if code in ("CAND","SPC","EDN","S181","HIST") else ""),
        "Hadith_Number": num, "Grading": " | ".join(gr_by_row.get(rid, [])) or ("pending GRADING_CONTROL" if not grd and code=="VL" else ""),
        "Claim_Support": claim, "Cross_Row_Mismatch": ", ".join(xr_by_row.get(rid, [])) or ("pending CROSS_ROW" if not xrm else ""),
        "Register_Key": r["Register_Key"], "Required_Action": (reg_rule + r["Audit_Note"]).strip(),
        "Audit_Note": r["Audit_Note"], "Human_Review": "YES" if code in HUMAN_YES or gr_by_row.get(rid) else "NO",
        "Final_Status": final,
    })
dst = A / "B1_P01-11_UNIDENTIFIED_REFERENCES_AUDIT_v1.3.csv"
with dst.open("w", encoding="utf-8", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=out_cols); w.writeheader(); w.writerows(out)
from collections import Counter
print(f"wrote {dst.relative_to(ROOT)} rows={len(out)} cols={len(out_cols)}")
print("Final_Status:", Counter(o["Final_Status"].split(" —")[0].split(" (")[0] for o in out).most_common())
print("Human_Review YES:", sum(o["Human_Review"]=="YES" for o in out), "| joined: xrm", bool(xrm), "grading", bool(grd), "unid", bool(und), "register", bool(reg))
