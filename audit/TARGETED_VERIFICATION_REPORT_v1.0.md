# TARGETED_VERIFICATION_REPORT_v1.0 — Book 1 Parts 01–11

**Date:** 2026-10-05
**Repo:** https://github.com/mdjonyrd/tahara1
**Branch:** `ccr-e641566e-pl28m8`
**Tip baseline:** `cce7fcc597131856b5d8606fdcbe50de809fe066`
**DOCX:** `book1/source/B1_P01-11_reader.docx`
**SHA256:** `337c70ea468a587ab248f5eb49ffacc0c167cfd421a76d145c02dbc8c0595ecc`
**MANUSCRIPT_WRITE:** FALSE
**Print gate:** **PRINT BLOCKED**

## 0. Scope

Targeted verification + human-decision pack against landed harvest CSVs + live DOCX wording. **No re-harvest. No DOCX modify. No patches. No auto author decisions. No fake VERIFIED.**

## 1. Input integrity

| Check | Result |
|---|---|
| Tip | `cce7fcc597131856b5d8606fdcbe50de809fe066` |
| DOCX SHA256 | `337c70ea468a587ab248f5eb49ffacc0c167cfd421a76d145c02dbc8c0595ecc` |
| Size | 825302 |
| Claims | 883 |
| Evidence | 956 |
| Recon BOUND | 328 / 328 |

## 2. Harvest status retained

| Status | Count |
|---|---|
| PAGE-CHECK | 438 |
| CONFLICT | 190 |
| VERIFIED | 154 |
| EDITION-LOCK | 97 |
| NOT_FOUND | 4 |

## 3. Phases A–N

| Phase | Deliverable | Count / result |
|---|---|---|
| A | `REF078_FADAK_DEED_DECISION_PACK_v1.0.md` | CONFLICT OPEN — AUTHOR DECISION REQUIRED |
| B | `CONFLICT_TRIAGE_v1.0.csv` | 190 |
| C | `EDITION_LOCK_REGISTER_v1.0.csv` | 97 |
| D | `NOT_FOUND_REVIEW.md` | 4 |
| E | `UNIDENTIFIED_DECISION_REGISTER_v1.0.csv` | 138 |
| F | `AUTHOR_DECISION_REGISTER_v1.0.csv` | 291 (AUTHOR_DECISION blank) |
| G | `GRADING_LANGUAGE_CONTROL_v1.0.md` | 38 grading rows; 82 RASUL_SAID flags |
| H | `SUNNI_OUTSIDE_SIX_REGISTER_v1.0.csv` | 47 |
| I | `SHIA_TARGETED_VERIFICATION_v1.0.csv` | 284 control rows; no live VERIFIED upgrade |
| J | `UMM_AYMAN_DECISION_PACK_v1.0.md` | 3 control rows; Aus separate |
| K | `MUKHE_CHURE_DECISION_NOTE.md` + `audit/research/SOURCE_HUNT_…` | NOT FOUND exact triad; dream framing |
| L | `PRIORITY_QUEUE_v1.0.csv` | 12 ranked items |
| M | `PATCH_READINESS_v1.0.md` | **NOT READY** — not patching |
| N | this report | complete |

## 4. Conflict triage buckets

| Conflict_Type | Count |
|---|---|
| ATTRIBUTION_VS_SOURCE_LOCK | 78 |
| SUNNI_SIX_NUMBER_OR_WORDING | 47 |
| SHIA_RECENSION_OR_PAGE | 19 |
| SOURCE_BLOCK_INTERNAL | 15 |
| FADAK_RECENSION | 9 |
| MIXED_SUNNI_SHIA_OR_CORPUS | 7 |
| QURAN_CITATION_CONFLICT | 6 |
| GENERAL_HARVEST_CONFLICT | 5 |
| UMM_AYMAN_CONTROL | 2 |
| MIXED_TRADITION_CITATION | 1 |
| FADAK_DEED_AUTHORSHIP | 1 |

## 5. Quality gates 1–12

| Gate | Name | Result |
|---|---|---|
| 1 | DOCX_SHA256_LOCK | **PASS** |
| 2 | TIP_BASELINE_cce7fcc | **PASS** |
| 3 | MANUSCRIPT_WRITE_FALSE_DOCX_UNCHANGED | **PASS** |
| 4 | NO_REHARVEST_USED_HARVEST_CSVS | **PASS** |
| 5 | NO_PATCHES_APPLIED | **PASS** |
| 6 | NO_AUTO_AUTHOR_DECISIONS | **PASS** |
| 7 | NO_FAKE_VERIFIED_UPGRADES | **PASS** |
| 8 | REF078_CONFLICT_OPEN | **PASS** |
| 9 | SUNNI_SHIA_KEPT_SEPARATE | **PASS** |
| 10 | UMM_AYMAN_AUS_SEPARATE | **PASS** |
| 11 | NOT_FOUND_NE_DOES_NOT_EXIST | **PASS** |
| 12 | PRINT_BLOCKED_REMAINS | **PASS** |

**Gates:** 12/12 PASS

## 6. Non-claims / stop rules honored

- DOCX not modified; SHA256 unchanged
- No PRINT ALLOWED
- No re-harvest
- No patches applied
- AUTHOR_DECISION columns left blank
- No fake VERIFIED upgrades
- SOURCE_EXISTENCE ≠ CLAIM_SUPPORT stated on conflict / mukhe / shia packs
- Sunni/Shia separate; Umm Ayman ≠ Aus; NOT_FOUND ≠ DOES_NOT_EXIST

## 7. Next (human)

1. Fill AUTHOR_DECISION on priority P1 (REF-078, Umm Ayman) then edition locks
2. O-7 reconcile before any patch apply
3. Only then manuscript patch → final citation audit → human PRINT ALLOWED

---
*Generated for targeted verification pass. STOP — no manuscript rewrite.*