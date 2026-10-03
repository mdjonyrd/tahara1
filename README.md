# tahara1 — বই ১ Citation Audit Workspace

«জান্নাতে যেতে হলে জানতে হবে» — **বই ১, ভাগ ১–১১** (`B1_P01-11_reader.docx`, 768 pp.)-এর citation/reference integrity workspace।
এখানে manuscript-এর prose নেই; আছে audit ledger, source-verification report, এবং manuscript-এ বসানোর patch।

**বর্তমান gate:** `BOOK 1 · PARTS 1–11 — CITATION AUDIT: PRINT BLOCKED` (328 unresolved marker; 4 resolved to edition-lock stage)

## Layout

| Path | কী |
|------|-----|
| `audit/B1_P01-11_CITATION_AUDIT_v1.0.md` | পূর্ণ audit (BUG-01…10, verified web corrections, 328-row ledger, final gate)। **Immutable.** |
| `audit/B1_P01-11_UNIDENTIFIED_REFERENCES_AUDIT_v1.0.csv` | Machine-readable ledger v1.0: `ID, Paragraph_Index, Part, Chapter, Status, Text`। **Immutable.** |
| `audit/B1_P01-11_UNIDENTIFIED_REFERENCES_AUDIT_v1.1.csv` | v1.0 + `Status_v1_1, Resolution_Ref, Resolution_Note`। `tools/apply_resolutions.py` দিয়ে generated; হাতে edit নয়। |
| `sources/S-<id>_*.md` | এক source-lock = এক file। দাবি আলাদা, status আলাদা, edition-lock checklist সহ। |
| `manuscript-patches/` | Prose + source-block replacement text, `⟦…⟧` placeholder = edition lock বাকি। |
| `tools/apply_resolutions.py` | v1.0 → v1.1 transform। নতুন resolution = `RESOLUTIONS` dict-এ একটি entry। |
| `tools/ledger_stats.py` | কোনো ledger CSV-র status count। |

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

## Resolved so far

| Source | Ledger rows | Status |
|--------|-------------|--------|
| `S-181` উম্মে আইমান ও ফাদাকের সাক্ষ্য | REF-078, 079, 081, 082 | RESEARCH COMPLETE / EDITION LOCK PENDING / PRINT: CONDITIONAL |

## Rules (never violate)
- Manuscript prose চুপিচুপি বদলানো যাবে না — patch file দিয়ে, দেখিয়ে।
- কোনো volume/page/hadith number অনুমান করে বসানো যাবে না।
- Sunni ও Shia recension আলাদা attribution-এ; composite narration নয়।
- Weak/mursal report-কে «সহিহ হাদিস» বলা যাবে না; «X-এর বর্ণনায়» লিখতে হবে।
- v1.0 audit files immutable; নতুন version = নতুন file।
- Local Windows path citation হিসেবে নয় (BUG-07)।
