# tahara1 — বই ১ Citation Audit Workspace

«জান্নাতে যেতে হলে জানতে হবে» — **বই ১, ভাগ ১–১১** (`B1_P01-11_reader.docx`, 768 pp.)-এর citation/reference integrity workspace।
এখানে manuscript-এর prose নেই; আছে audit ledger, source-verification report, এবং manuscript-এ বসানোর patch।

**বর্তমান gate:** `BOOK 1 · PARTS 1–11 — CITATION AUDIT: PRINT BLOCKED` — 328 row triaged (v1.2): 62 verified-live, 12 mismatch, 30 unidentified, বাকি page/edition lock

## Layout

| Path | কী |
|------|-----|
| `audit/B1_P01-11_CITATION_AUDIT_v1.0.md` | পূর্ণ audit (BUG-01…10, verified web corrections, 328-row ledger, final gate)। **Immutable.** |
| `audit/B1_P01-11_UNIDENTIFIED_REFERENCES_AUDIT_v1.0.csv` | Machine-readable ledger v1.0: `ID, Paragraph_Index, Part, Chapter, Status, Text`। **Immutable.** |
| `audit/B1_P01-11_UNIDENTIFIED_REFERENCES_AUDIT_v1.1.csv` | v1.0 + `Status_v1_1, Resolution_Ref, Resolution_Note`। `tools/apply_resolutions.py` দিয়ে generated; হাতে edit নয়। |
| `audit/B1_P01-11_UNIDENTIFIED_REFERENCES_AUDIT_v1.2.csv` | v1.1 + per-row triage: `Triage, Triage_Label, Candidate_Source, Register_Key, Audit_Note` (data: `tools/triage_v1_2.py`)। |
| `audit/B1_P01-11_CITATION_AUDIT_v1.1.md` | Audit v1.1: BUG-11…30, 12 mismatch corrections, normalisation register, revised execution order। |
| `audit/verification/` | Live-check evidence (six Sunni books vs. ledger numbers, 2026-10-03)। |
| `audit/B1_P01-11_CITATION_AUDIT_v1.2.md` | Consolidated audit v1.2 (19 sections): triage, cross-row mismatches, Sunni verification, Shia control, Fadak map, Umm Ayman, grading, S-ID audit, patch queue, next order। |
| `audit/B1_P01-11_UNIDENTIFIED_REFERENCES_AUDIT_v1.3.csv` | Final triage ledger: 328 rows × 23 columns (joins v1.2 + cross-row + grading + UNID decisions + register)। `tools/build_ledger_v1_3.py`। |
| `audit/B1_P01-11_CROSS_ROW_MISMATCHES_v1.0.csv` | 92 cross-row conflicts (types A–N) + summary। |
| `audit/B1_P01-11_SUNNI_VERIFICATION_EVIDENCE_v1.1.md` | 214 (book×number×row) classifications: EXACT/PARTIAL/WRONG_NUMBER/…। |
| `audit/B1_P01-11_GRADING_CONTROL_v1.0.csv` | 38 weak/disputed/munkar numbers with graders as printed + allowed Bengali formulation। |
| `audit/B1_P01-11_SHIA_SOURCE_CONTROL_v1.0.csv` | 169 Shia-source rows (all CANDIDATE/PAGE-CHECK; nothing Shia is live-verifiable here)। |
| `audit/B1_P01-11_FADAK_EVIDENCE_MAP_v1.0.csv` | 73 rows, 11 Fadak claims as separate evidentiary units। |
| `audit/B1_P01-11_UMM_AYMAN_CONTROL_v1.0.md` | Identity / relationship / Paradise report / testimony / family kept apart; flags F-1…F-9। |
| `audit/B1_P01-11_UNIDENTIFIED_ROWS_DECISIONS_v1.0.csv` | 40 rows (30 UNID + «সূত্র নেই» rechecks): 6 canonical found, 16 plausible, 3 secondary, 15 none। |
| `audit/B1_P01-11_SOURCE_REGISTER_v1.1.csv` | 95 register keys → one canonical citation each; 41 keys had status conflicts। |
| `audit/B1_P01-11_INTERNAL_SOURCE_ID_AUDIT_v1.0.md` | S-80…S-183, CL-HAD-*, local paths, secondary stand-ins। |
| `audit/_CORRECTIONS_TO_V1_1_2026-10-03.md` | C-01…C-28: v1.1 claims corrected against the corpus। |
| `manuscript-patches/B1_P01-11_MANUSCRIPT_PATCH_PLAN_v1.0.md` | 105 patch blocks + 223 NO_CHANGE; DOCX untouched। |
| `sources/S-<id>_*.md` | এক source-lock = এক file। দাবি আলাদা, status আলাদা, edition-lock checklist সহ। |
| `manuscript-patches/` | Prose + source-block replacement text, `⟦…⟧` placeholder = edition lock বাকি। |
| `tools/apply_resolutions.py` | v1.0 → v1.1 transform। নতুন resolution = `RESOLUTIONS` dict-এ একটি entry। |
| `tools/ledger_stats.py` | কোনো ledger CSV-র status count। |
| `tools/triage_v1_2.py` | 328 row-এর triage data (code, candidate source, register key, note)। |
| `tools/verify_sunni.py` | ছয় Sunni কিতাবে নম্বর/wording live check (GitHub corpus; `fetch` → `batch`)। |

## Status vocabulary

Reader-facing attribution (বইয়ে ছাপা হয়) আর internal QA status (এখানে) **আলাদা** (audit BUG-10)।

Internal QA statuses:
- `PAGE-CHECK` — উৎস জানা, খণ্ড-পৃষ্ঠা/নম্বর মেলানো বাকি
- `বর্ণিত আছে` — খাতায় সূত্র নেই বা মূল কিতাবে মেলানো হয়নি; prose-এ attribution-ছাড়া
- `সূত্র নেই` / `SOURCE-MISSING` — কোনো উৎস নেই
- `NOT VERIFIED` — খোঁজা হয়েছে, পাওয়া যায়নি → Hakim-type: attribution বাদ
- `PRINT BLOCKED` — এই reference নিয়ে ছাপা যাবে না
- `VERIFIED` — primary text পাওয়া গেছে (edition lock আলাদা)
- `EDITION-LOCK PENDING` — text verified, কিন্তু বইয়ের edition অনুযায়ী খণ্ড-পৃষ্ঠা এখনও lock হয়নি
- `CORRECTED` — manuscript-এর claim/attribution বদলাতে হবে (patch file-এ কী বদলাবে)
- `CONFIRMED` — edition lock সহ সম্পূর্ণ; print-ready

## Workflow

```
SOURCE-MISSING → NOT VERIFIED → PAGE-CHECK → EDITION LOCK → GLOBAL REFERENCE NORMALIZATION → FINAL CITATION AUDIT → PRINT ALLOWED
```

একটি source-lock resolve করতে:
1. `sources/S-<id>_<slug>.md` লিখুন — দাবি আলাদা করুন, প্রতিটির status, আরবি মূল, URL, edition-lock checklist।
2. `manuscript-patches/` -এ prose + source-block replacement লিখুন।
3. `tools/apply_resolutions.py`-র `RESOLUTIONS`-এ REF-ID entry যোগ করুন; script চালান; `tools/ledger_stats.py` দিয়ে count যাচাই করুন।
4. এক commit = এক source-lock।

## Triage codes (ledger v1.2)

`VL` verified-live · `MM` mismatch (correction given) · `EDN` edition-number · `CAND` candidate source · `SPC` Shia page-check · `UNID` unidentified · `DUP` duplicate → register key · `PROSE` prose line · `HIST` non-hadith · `S181` resolved · `Q` Quran text

## Resolved so far

| Source | Ledger rows | Status |
|--------|-------------|--------|
| `S-181` উম্মে আইমান ও ফাদাকের সাক্ষ্য | REF-078, 079, 081, 082 | RESEARCH COMPLETE / EDITION LOCK PENDING / PRINT: CONDITIONAL |
| Six-book live check | 62 rows VL; 12 MM | numbers confirmed; grades to print; see audit v1.1 §2–4 |
| Audit v1.2 work package (6 subagents) | all 328 rows | ledger v1.3, patch plan v1.0, 9 control tables — gate still PRINT BLOCKED |

## Rules (never violate)
- Manuscript prose চুপিচুপি বদলানো যাবে না — patch file দিয়ে, দেখিয়ে।
- কোনো volume/page/hadith number অনুমান করে বসানো যাবে না।
- Sunni ও Shia recension আলাদা attribution-এ; composite narration নয়।
- Weak/mursal report-কে «সহিহ হাদিস» বলা যাবে না; «X-এর বর্ণনায়» লিখতে হবে।
- v1.0 audit files immutable; নতুন version = নতুন file।
- Local Windows path citation হিসেবে নয় (BUG-07)।
