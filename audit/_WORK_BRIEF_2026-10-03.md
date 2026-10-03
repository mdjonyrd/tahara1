# SHARED BRIEF — B1_P01-11 Citation Audit v1.2 work package (2026-10-03)

Repository (git, already cloned): /home/user/tahara1   — do NOT run git commit/push; just write your output file(s).
Work in Python 3 / bash. Always `sys.stdout.reconfigure(encoding='utf-8')`. Bengali + Arabic text is UTF-8.

## Inputs (read what your task needs; all paths relative to repo root)
- audit/B1_P01-11_UNIDENTIFIED_REFERENCES_AUDIT_v1.2.csv   — 328 rows. Columns: ID, Paragraph_Index, Part, Chapter, Status, Text (the manuscript's own source-note or prose line), Status_v1_1, Resolution_Ref, Resolution_Note, Triage, Triage_Label, Candidate_Source, Register_Key, Audit_Note
- tools/triage_v1_2.py        — the same triage as a Python dict T[REF] = (code, candidate, register_key, note); codes explained in its docstring
- audit/B1_P01-11_CITATION_AUDIT_v1.0.md  — original audit (BUG-01..10)
- audit/B1_P01-11_CITATION_AUDIT_v1.1.md  — audit v1.1 (BUG-11..30, 12 mismatch corrections, register table)
- audit/verification/sunni_six_books_check_2026-10-03.md (+ .raw.txt) — live check of six-book numbers
- sources/S-181_UMM_AYMAN_FADAK_VERIFICATION.md — Umm Ayman / Fadak source-verification report
- manuscript-patches/B1_P03_C06_FADAK_S-181_PATCH.md — existing patch for Part 3 Ch 06
- tools/verify_sunni.py — `python3 tools/verify_sunni.py show <bukhari|muslim|abudawud|tirmidhi|ibnmajah|nasai> <number>` prints Arabic text + grades; `search "<arabic substring>"` searches all six books. Corpus already present in tools/_hadith-api/editions (do not re-fetch). Muslim numbers = Abd al-Baqi numbering.

## HARD FACTS ABOUT THIS ENVIRONMENT
- The manuscript DOCX (B1_P01-11_reader.docx) is NOT available here. The only manuscript text we have is the ledger `Text` column (source-note bullets and some prose lines). Where a task asks for manuscript page/paragraph, use Paragraph_Index from the ledger and write Page = "PAGE-CHECK (docx not available)".
- Network: sunnah.com, dorar.net, thaqalayn.net, cdn.jsdelivr.net are BLOCKED. GitHub works. Only the six Sunni books are verifiable here (via tools/verify_sunni.py). Shia works and Sunni works outside the six books CANNOT be live-verified here.

## GLOBAL LAW (from the author — binding)
- Do NOT rewrite the manuscript freely; do NOT improve theology; do NOT add arguments; do NOT remove historical claims merely because disputed; do NOT silently reconcile conflicting narrations.
- Do NOT treat AI output (including your own memory) as evidence. PRIMARY SOURCE > recognized digital primary source > scholarly secondary > AI.
- Every correction must be traceable to a specific source. Edition/page differences MUST remain explicit.
- "NOT FOUND" ≠ "DOES NOT EXIST". If a source cannot be page-locked, mark PAGE-CHECK; never invent a page/number.
- Never mark anything VERIFIED unless evidence in this repo (verify_sunni.py output, S-181 report with its URLs) supports it. Knowledge-based identifications are CANDIDATE, never VERIFIED.
- Keep Sunni and Shia recensions separate. Never merge Umm Ayman's testimony with Aus ibn al-Hadathan's (he belongs to the counter-testimony with Aisha/Hafsa on «لا نورث»).
- Weak/munkar reports may never be rendered as flat «রাসূল ﷺ বলেছেন».
- Preserve all 328 rows in any ledger output. CSV: UTF-8, header row, quote fields properly (use csv module).
- Print gate stays PRINT BLOCKED. Never write PRINT ALLOWED.

## Status vocabulary
PAGE-CHECK · বর্ণিত আছে (unattributed) · সূত্র নেই/SOURCE-MISSING · NOT VERIFIED · PRINT BLOCKED · VERIFIED (live evidence) · CANDIDATE · EDITION-LOCK PENDING · CORRECTED · CONFIRMED (edition-locked, print-ready)

## Register keys
See `Register_Key` column in the v1.2 CSV and the table in audit v1.1 §2 BUG-26 (HAD-THAQALAYN, HAD-MADINAT-ILM, HAD-BIDAA-MINNI, …).

When you finish: write your file(s) to the exact paths given in your task, then reply with: files written, row counts, and any fact you could NOT verify (say so plainly).
