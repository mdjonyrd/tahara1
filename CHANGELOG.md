# Changelog

## 2026-10-03 — S-181 resolved to edition-lock stage
- Added `audit/` with the v1.0 citation audit MD and ledger CSV (328 rows) as immutable inputs.
- Added `sources/S-181_UMM_AYMAN_FADAK_VERIFICATION.md`: three claims separated (identity / «woman of Paradise» / Fadak testimony); Sunni and Shia recensions kept apart; Aus ibn al-Hadathan moved to counter-testimony; Hakim attribution NOT VERIFIED → blocked; Ibn Sa'd report marked mursal/weak; edition-lock checklist (11 items).
- Added `manuscript-patches/B1_P03_C06_FADAK_S-181_PATCH.md`: prose corrections A-1..A-3 (p. 213) and replacement source block (p. 217) with `⟦…⟧` placeholders.
- Added `tools/apply_resolutions.py` and generated ledger v1.1: REF-078, REF-079, REF-081, REF-082 updated (`Status_v1_1`, `Resolution_Ref`, `Resolution_Note`); 324 rows unchanged.
- Added `tools/ledger_stats.py`.
- Gate unchanged: `PRINT BLOCKED` (324 unresolved + 4 at edition-lock stage).
