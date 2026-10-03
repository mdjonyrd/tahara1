# tools/ — how to reproduce the B1_P01-11 citation-audit artefacts

All commands run from the repository root, Python 3.11, standard library only. Every command below was run on 2026-10-03 and the output described is what it produced. Bengali/Arabic text is UTF-8 (each script calls `sys.stdout.reconfigure(encoding="utf-8")`).

## 1. Pipeline at a glance

```
audit/..._AUDIT_v1.0.csv  (immutable input, 328 rows)
        │  tools/apply_resolutions.py      (RESOLUTIONS dict: S-181 rows)
        ▼
audit/..._AUDIT_v1.1.csv  (v1.0 + Status_v1_1, Resolution_Ref, Resolution_Note)
        │  tools/apply_resolutions.py      (+ tools/triage_v1_2.py  T[REF] = (code, candidate, register_key, note))
        ▼
audit/..._AUDIT_v1.2.csv  (v1.1 + Triage, Triage_Label, Candidate_Source, Register_Key, Audit_Note)
        │  tools/build_ledger_v1_3.py      (joins control tables, see §6)
        ▼
audit/..._AUDIT_v1.3.csv  (328 rows, 23 columns)

tools/verify_sunni.py ──► audit/verification/sunni_six_books_check_2026-10-03.{md,raw.txt}
```

## 2. `apply_resolutions.py` — v1.0 → v1.1 → v1.2

```
python3 tools/apply_resolutions.py
```
* Reads `audit/B1_P01-11_UNIDENTIFIED_REFERENCES_AUDIT_v1.0.csv` (never modified).
* Writes **v1.1** (original 6 columns copied verbatim + `Status_v1_1`, `Resolution_Ref`, `Resolution_Note`; only REF-078, 079, 081, 082 carry a resolution — the S-181 Umm Ayman / Fadak work; the other 324 rows get `Status_v1_1 = Status`).
* Imports `tools/triage_v1_2.py` and writes **v1.2** (adds `Triage`, `Triage_Label`, `Candidate_Source`, `Register_Key`, `Audit_Note`).
* Printed output: `wrote … v1.2 (triage rows: 328)`, `rows in : 328`, `rows out: 328`, `applied : REF-078, REF-079, REF-081, REF-082`, `wrote … v1.1`.
* Reproducibility check done: run in a scratch copy of the repo, both output files were byte-identical (`cmp`) to the committed v1.1 and v1.2.
* To add a resolution: add a REF-ID entry to `RESOLUTIONS` in the script and re-run. Never edit v1.0 or v1.1 by hand. The script exits with an error if a resolution names an unknown REF-ID.
* The script **overwrites** v1.1 and v1.2 in `audit/` — run it in a copy if other work is reading them.

## 3. `triage_v1_2.py` — the per-row triage table

```
python3 tools/triage_v1_2.py
```
Asserts that `T` has exactly 328 entries (REF-001 … REF-328) and prints the triage histogram:
`68 SPC · 67 CAND · 62 VL · 48 PROSE · 30 UNID · 17 HIST · 13 DUP · 12 MM · 5 S181 · 4 EDN · 2 Q`.
It is data, not a transform: `T[REF] = (code, candidate_or_correction, register_key, note)`. Codes (full list in the module docstring and `CODES`): VL VERIFIED-LIVE, MM MISMATCH, EDN EDITION-NUMBER, CAND CANDIDATE, SPC SHIA-PAGE-CHECK, UNID UNIDENTIFIED, DUP DUPLICATE, PROSE PROSE-LINE, HIST NON-HADITH, S181 RESOLVED-S181, Q QURAN-TEXT. `Register_Key` groups rows that cite the same hadith (several keys may be joined by `;`). Change a triage by editing this file and re-running `apply_resolutions.py`.

## 4. `ledger_stats.py` — status counts

```
python3 tools/ledger_stats.py audit/B1_P01-11_UNIDENTIFIED_REFERENCES_AUDIT_v1.0.csv
python3 tools/ledger_stats.py audit/B1_P01-11_UNIDENTIFIED_REFERENCES_AUDIT_v1.1.csv   # also the default with no argument
python3 tools/ledger_stats.py audit/B1_P01-11_UNIDENTIFIED_REFERENCES_AUDIT_v1.2.csv
```
Prints file, row count (328), the column used (`Status` for v1.0; `Status_v1_1` when present), number of resolved rows, marker-class counts and the top raw statuses. Observed: v1.0 → PAGE-CHECK 245, «বর্ণিত আছে» 146, «সূত্র নেই» 5, «মেলানো বাকি» 17, PRINT BLOCKED 2 (resolved 0); v1.1/v1.2 → PAGE-CHECK 242, «বর্ণিত আছে» 144, NOT VERIFIED 1, resolved 4. (Piping into `head` raises a harmless `BrokenPipeError`.)

## 5. `verify_sunni.py` — live check of the six Sunni books

```
python3 tools/verify_sunni.py fetch                  # one-time: sparse-clone the Arabic JSON editions
python3 tools/verify_sunni.py show bukhari 4240      # one hadith (+ grades); all sub-reports for Muslim
python3 tools/verify_sunni.py show muslim 2408
python3 tools/verify_sunni.py search "دار الحكمة"    # substring search across all six books (Arabic, diacritics ignored)
python3 tools/verify_sunni.py batch > out.txt        # run the built-in check list (BATCH numbers + TERMS)
```
* Books: `bukhari muslim abudawud tirmidhi ibnmajah nasai`.
* **Network:** only GitHub is reachable from the cloud environment. sunnah.com, dorar.net, thaqalayn.net, cdn.jsdelivr.net and hubbeali.com are blocked, so anything outside the six Sunni books (Shia works, al-Hakim, al-Tabarani, Ahmad, Bayhaqi, tafsir works) **cannot be live-verified here**. `fetch` clones `https://github.com/fawazahmed0/hadith-api` (depth 1, sparse) and checks out the six `editions/ara-*.json` files; tested in a scratch copy (≈9 s, six files). Do not run `fetch` inside a populated `tools/_hadith-api/` that holds extra editions (e.g. `eng-abudawud.json`): it resets the sparse-checkout list to the six Arabic files.
* **`tools/_hadith-api/` is git-ignored** (`.gitignore`: `tools/_hadith-api/`, `__pycache__/`). A fresh clone has no corpus: run `fetch` first, otherwise every command exits with `editions missing - run: python3 tools/verify_sunni.py fetch`.
* **Numbering:** Bukhari, Abu Dawud, Tirmidhi, Ibn Majah, Nasa'i use the standard (sunnah.com) number.
* **Muslim numbering caveat:** the corpus stores **Abd al-Baqi** numbers in `arabicnumber` with a sub-report suffix (`2408.01 … 2408.04`), while its `hadithnumber` is a different, sequential numbering (e.g. 6225-6228 for the same hadith). `show muslim N` matches the integer part of `arabicnumber` and lists every sub-report; it deliberately has **no fallback** to `hadithnumber`. An earlier version of the tool (commit 5270d3c and before) fell back silently and printed the wrong hadith for most Muslim numbers (e.g. 8, 91, 1907, 2404, 2408 — the first `raw.txt` showed this); `audit/verification/sunni_six_books_check_2026-10-03.md` carries the correction note and the raw file was regenerated. If you see an unrelated hadith for a Muslim number you are on an old copy of the script.
* **Corpus quirk:** 344 Muslim entries have `arabicnumber = null` (148 of them with text). They are sub-reports with no printed number; e.g. the first two sub-reports of Muslim 2816 («لن ينجي أحدا منكم عمله») sit unnumbered directly before 2816.03, so `show muslim 2816` lists only 2816.03-.06 — use `search` to find them (verified: `search "لن ينجي أحدا منكم عمله"` returns Bukhari 6463 plus two `arNone` Muslim entries).
* `show` prints the first 230 characters of each entry (often just the isnad) and the dataset's grades (Albani, Zubair Ali Zai, Shakir, Arnaut, Bashar, Muhyi al-Din, F. A. Baqi). Grades are the dataset's, not this repo's; where graders disagree, the book must say so.
* `batch` regenerates the raw check list. Reproducibility check done: the `batch` output of the current script is byte-identical to `audit/verification/sunni_six_books_check_2026-10-03.raw.txt` (382 lines). The human table `…check_2026-10-03.md` is written by hand from that raw output.
* `NOT FOUND` ≠ does not exist: a miss means "not in these six books of this corpus".

## 6. `build_ledger_v1_3.py` — ledger v1.3 (control-table join)

```
python3 tools/build_ledger_v1_3.py
```
Joins ledger v1.2 with `audit/B1_P01-11_CROSS_ROW_MISMATCHES_v1.0.csv`, `…_GRADING_CONTROL_v1.0.csv`, `…_UNIDENTIFIED_ROWS_DECISIONS_v1.0.csv` and `…_SOURCE_REGISTER_v1.1.csv`; missing control files are tolerated (their columns stay "pending"). Writes `…_AUDIT_v1.3.csv` (328 rows, 23 columns) and prints Final_Status and Human_Review counts. Tested in a scratch copy: `wrote … rows=328 cols=23`. Nothing is upgraded to VERIFIED unless the v1.2 triage is VL or S181.

## 7. File layout

### `audit/`
| File | What it is | How produced |
|---|---|---|
| `B1_P01-11_CITATION_AUDIT_v1.0.md` | original audit (BUG-01…10, full ledger text, «Internal source-ID audit») — immutable | written (not generated) |
| `B1_P01-11_CITATION_AUDIT_v1.1.md` | v1.1 report: triage table, BUG-11…30, 12 mismatch corrections (§3), BUG-26 register table (§2), next steps | written |
| `…_UNIDENTIFIED_REFERENCES_AUDIT_v1.0.csv` | ledger, 328 rows: ID, Paragraph_Index, Part, Chapter, Status, Text — immutable | input |
| `…_AUDIT_v1.1.csv` / `…_v1.2.csv` | ledger + resolutions / + triage | `apply_resolutions.py` |
| `…_AUDIT_v1.3.csv` | ledger + control tables (Page = «PAGE-CHECK (docx not available)») | `build_ledger_v1_3.py` |
| `B1_P01-11_SOURCE_REGISTER_v1.1.csv` | one row per Register_Key (60 from the ledger) + 35 `HAD-*` keys for six-book hadith numbers that had no key = 95 rows; columns Register_Key … Normalisation_Rule | written from the ledger, the audit v1.1 §2 BUG-26 seed and `show`/corpus checks (no generator script) |
| `B1_P01-11_INTERNAL_SOURCE_ID_AUDIT_v1.0.md` | Phase 10: internal S-IDs, local paths, secondary stand-ins | written |
| `B1_P01-11_CROSS_ROW_MISMATCHES_v1.0.csv` (+ `.summary.md`) | 92 cross-row inconsistencies (XRM-001…092) | written (separate work package) |
| `B1_P01-11_GRADING_CONTROL_v1.0.csv` | 38 grading-safety rows (grader, class, allowed formulation) | written (separate work package) |
| `B1_P01-11_SHIA_SOURCE_CONTROL_v1.0.csv` | 169 Shia-source rows (work, volume, page, edition, status) | written (separate work package) |
| `B1_P01-11_FADAK_EVIDENCE_MAP_v1.0.csv`, `B1_P01-11_UMM_AYMAN_CONTROL_v1.0.md` | Fadak / Umm Ayman evidence map and control (from `sources/S-181…`) | written (separate work package) |
| `B1_P01-11_UNIDENTIFIED_ROWS_DECISIONS_v1.0.csv` | 40 UNID-row decisions | written (separate work package) |
| `verification/sunni_six_books_check_2026-10-03.md` | human table of every six-book number and wording checked (✅ ⚠ ❌ ∅) | written from `.raw.txt` |
| `verification/sunni_six_books_check_2026-10-03.raw.txt` | raw `verify_sunni.py batch` output | `python3 tools/verify_sunni.py batch` |
| `_WORK_BRIEF_2026-10-03.md` | shared brief for this work package (binding rules: no free rewriting, AI output is not evidence, PRINT BLOCKED stays) | written |

The files marked «separate work package» have no generator in `tools/`; only the join in `build_ledger_v1_3.py` reads them. Files in `audit/` other than the ledgers' inputs were last listed on 2026-10-03 and may grow.

### `sources/`
`S-181_UMM_AYMAN_FADAK_VERIFICATION.md` — source-verification report for Umm Ayman and Fadak (identity, the Ibn Sa'd mursal «جنة» report, Baladhuri / al-Ihtijaj / Sulaym / Ibn Abi al-Hadid testimony, Aus ibn al-Hadathan separation, §5 edition-lock checklist). It is the evidence behind the four RESOLUTIONS in `apply_resolutions.py`. Status: research complete, edition lock pending, print CONDITIONAL.

### `manuscript-patches/`
`B1_P03_C06_FADAK_S-181_PATCH.md` — replacement prose (A-1…A-3) and source block (B) for Part 3 chapter 06, with `⟦…⟧` placeholders to be filled after the edition lock (§C checklist). Its source block still prints internal «— S-181 §…» pointers that must be removed before print. Patches are proposals; nothing here edits the manuscript.

## 8. Not reproducible here
The manuscript DOCX (`B1_P01-11_reader.docx`) is absent, so page numbers are `PAGE-CHECK (docx not available)`; Shia sources and Sunni works outside the six books cannot be fetched; sunnah.com / dorar.net / thaqalayn.net / hubbeali.com are blocked; the earlier notebook, `SOURCE_REGISTER.md` and log files named in the ledger are not in the repo.
