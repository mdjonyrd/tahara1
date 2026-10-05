# SOURCE HARVEST README — Book 1 (Parts 01–11)

## Purpose

End-to-end **source harvest** against the live canonical DOCX. This package inventories source-bearing claims, reconciles the inherited 328-row ledger, and records verification status. It does **not** rewrite the manuscript and does **not** clear PRINT BLOCKED.

## Locks

- `MANUSCRIPT_WRITE=FALSE` — never modify `book1/source/B1_P01-11_reader.docx`
- SHA256 must be `337c70ea468a587ab248f5eb49ffacc0c167cfd421a76d145c02dbc8c0595ecc`
- Ledger rows are anchors only; live DOCX wins for paragraph binding
- Sunni / Shia kept separate; Umm Ayman ≠ Aus counter-testimony
- No invented page numbers; NOT FOUND ≠ DOES NOT EXIST
- No Windows paths in publication-facing source records

## Reproduce

```bash
# from repo root, on branch with the DOCX
python3 tools/export_docx_paragraphs.py
python3 tools/reconcile_ledger_328.py
python3 tools/extract_claims.py
python3 tools/verify_sunni.py fetch
python3 tools/verify_sunni.py batch > audit/verification/sunni_six_books_check_$(date +%F).raw.txt
python3 tools/build_source_harvest.py
# or: python3 tools/run_source_harvest.py
```

## Key outputs

| File | Phase |
|---|---|
| `manuscript-export/B1_P01-11_reader.paragraphs.jsonl` | 1 |
| `audit/B1_P01-11_328_ROW_RECONCILIATION.csv` | 2 |
| `audit/B1_P01-11_CLAIM_INVENTORY.csv` | 3–4 |
| `audit/B1_P01-11_SOURCE_REGISTER_v1.2.csv` | 5 |
| `audit/B1_P01-11_EVIDENCE_REGISTER_v1.0.csv` | 6 |
| `audit/B1_P01-11_CLAIM_SOURCE_MATRIX.csv` | 7 |
| `audit/B1_P01-11_QURAN_CONTROL.csv` | 8 |
| `audit/verification/sunni_six_books_check_2026-10-05.raw.txt` | 9 |
| `audit/B1_P01-11_SHIA_SOURCE_CONTROL_HARVEST.csv` | 10 |
| `audit/B1_P01-11_FADAK_SPECIAL_CONTROL.csv` | 11 |
| `audit/B1_P01-11_UMM_AYMAN_CONTROL_HARVEST.csv` | 12 |
| `audit/B1_P01-11_CROSS_CHAPTER_CONFLICTS.csv` | 13 |
| `audit/B1_P01-11_CHAPTER_SOURCE_MAP.csv` | 14 |
| `audit/B1_P01-11_LINE_BY_LINE_COVERAGE.csv` | 15 |
| `audit/ALL_UNIDENTIFIED_REFERENCES.csv` | 16 |
| `audit/B1_P01-11_BN_AR_TRANSLATION_CONTROL.csv` | 17 |
| `audit/B1_P01-11_OLD_VS_NEW_RECONCILIATION_SUMMARY.csv` | 18 |
| `audit/COMPLETE_SOURCE_HARVEST_REPORT.md` | 19 |
| `audit/SOURCE_HARVEST_README.md` | 20 |
| `audit/B1_P01-11_QUALITY_GATES_A-L.csv` | 21 |

## Status vocabulary

`VERIFIED` · `PAGE-CHECK` · `EDITION-LOCK` · `CONFLICT` · `NOT_FOUND` · `CANDIDATE` · `PRINT BLOCKED`

`VERIFIED` is used only with live six-book corpus evidence (or structural Qur'an ayah control). Everything else stays PAGE-CHECK / CANDIDATE / NOT_FOUND.

## Next (NOT this harvest)

SOURCE-MISSING → NOT VERIFIED → PAGE-CHECK → EDITION LOCK → GLOBAL REFERENCE NORMALIZATION → MANUSCRIPT PATCH → FINAL CITATION AUDIT → HUMAN REVIEW → PRINT ALLOWED (never automatic).
