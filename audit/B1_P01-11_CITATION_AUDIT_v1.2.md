# B1_P01-11 — CITATION / REFERENCE AUDIT v1.2 (consolidated report)

**Book:** Book 1 · Parts 1–11 (manuscript `B1_P01-11_reader.docx`, **not available in this environment**)
**Date:** 2026-10-03 · **Phase:** 13 of the v1.2 work package (consolidation)
**Builds on:** audit v1.0 (BUG-01…10, immutable), audit v1.1 (BUG-11…30, §3 corrections), and every control file listed in "Files in this release".
**Method:** this report is compiled **only** from the files listed under §2 (read in full, or header + §1 for the patch plan). Counts were recomputed with Python 3 from the CSVs where the task asked for it (v1.3 ledger, cross-row CSV, grading control, Shia control, Fadak map, decisions CSV, source register, patch-plan block/NO_CHANGE lines). No new identification, number, page or grade is introduced here; no memory-based statement is used as evidence.
**Gate:** `BOOK 1 · PARTS 1–11 — CITATION AUDIT: PRINT BLOCKED` (unchanged)

---

## 1 Executive Summary

1. **All 328 ledger rows are accounted for** (§3): each row is triaged in ledger v1.3, and each row has exactly one patch block (105 rows) or one NO_CHANGE line (223 rows) in the manuscript patch plan. 196 rows are tied to at least one of the 95 register keys. **No row is CONFIRMED (edition-locked, print-ready).**
2. **Live evidence exists only for the six Sunni books.** 62 rows are VERIFIED-LIVE (six-book number + text). The Sunni verification pass produced **214** (book × number × row) classifications: 146 EXACT_MATCH, 35 PARTIAL_MATCH, 14 GRADING_MISMATCH, 7 EDITION_DEPENDENT, 6 WRONG_TEXT, 3 WRONG_SUBJECT, 2 WRONG_NUMBER, 1 NOT_FOUND (§6).
3. **Nothing Shia is live-verified.** The Shia control lists 169 citation lines for 109 ledger rows: 98 PAGE-CHECK, 64 CANDIDATE, 7 VERIFIED-S181-URL (URLs recorded in S-181, not re-opened here) (§7).
4. **Audit v1.1 itself contained errors**, found in the corpus and recorded as C-01…C-28. Among them: Abu Dawud 5023 does not read «فقد رآني»; the «جويرية» passage is Bukhari 520, not 3110; Muslim 91 does not carry the verbatim «مثقال حبة من خردل من كبر»; «عترتي» is absent from Sahih Muslim; Tirmidhi 3206 says six months, not nine; Abu Dawud 2972 is a contrary report (§13–§15).
5. **92 cross-row conflicts** were found (XRM-001…092). The most consequential for print safety: Basra, not Kufa; Aus ibn al-Hadathan placed among Umm Ayman's witnesses; «ইতরাত» marked CONFIRMED under Muslim 2408; weak reports printed as flat «রাসূলুল্লাহ ﷺ বলেছেন» (§5).
6. **38 graded six-book numbers** are under grading control. 23 of them are not "sahih per graders": 2 MUNKAR, 2 VERY WEAK, 6 WEAK REPORT, 5 DISPUTED, 6 GRADERS DISAGREE, 1 "source exists but not acceptable as unqualified proof", and 1 HASAN. None of them may be printed as flat «রাসূল ﷺ বলেছেন» (§10).
7. **Fadak and Umm Ayman.** The Fadak evidence map has 73 lines over eleven claim units. 45 lines are Sunni and 28 Shia, kept recension by recension. The Umm Ayman control leaves ten residual flags (F-1…F-10). The key ones: the deed's writer (Prophet vs Abu Bakr), «হাদী», and Malik b. Aws ≠ Aus ibn al-Hadathan (§8–§9).
8. **The 40 unidentified / «সূত্র নেই» rows have been decided** (§11, §16). There are 6 CANONICAL_SOURCE_FOUND (2 partial), 16 PLAUSIBLE_SOURCE_ONLY, 3 SECONDARY_SOURCE_ONLY and 15 NO_SOURCE_LOCATED. 8 rows are flagged for the author's decision.
9. **The patch queue holds 105 blocks.** Confidence: HIGH 53, MEDIUM 20, LOW 32. 79 blocks require human review (§17). The DOCX has not been modified.
10. **Verdict: PRINT BLOCKED** (§18). The execution order to lift it is in §19.

---

## 2 Scope

### 2.1 Input files (all read for this report)

| File | Role | Size used here |
|---|---|---|
| `audit/B1_P01-11_CITATION_AUDIT_v1.1.md` | BUG-11…30, register table, §3 mismatch table | 20 bugs, 12 MM rows |
| `audit/_CORRECTIONS_TO_V1_1_2026-10-03.md` | corrections confirmed in the six-book corpus | C-01…C-28 |
| `audit/B1_P01-11_UNIDENTIFIED_REFERENCES_AUDIT_v1.3.csv` | ledger v1.3 (23 columns, all control tables joined) | 328 rows |
| `audit/B1_P01-11_CROSS_ROW_MISMATCHES_v1.0.csv` + `.summary.md` | cross-row conflicts | 92 rows |
| `audit/B1_P01-11_SUNNI_VERIFICATION_EVIDENCE_v1.1.md` | six-book numbered-hadith verification | 214 classifications |
| `audit/verification/sunni_six_books_check_2026-10-03.md` | live six-book check (table A/B) | — |
| `audit/B1_P01-11_GRADING_CONTROL_v1.0.csv` | grades as printed in the corpus | 38 rows |
| `audit/B1_P01-11_SHIA_SOURCE_CONTROL_v1.0.csv` | Shia citation lines | 169 rows |
| `audit/B1_P01-11_FADAK_EVIDENCE_MAP_v1.0.csv` | Fadak claim units × sources | 73 rows |
| `audit/B1_P01-11_UMM_AYMAN_CONTROL_v1.0.md` | Umm Ayman units, formulations, flags | F-1…F-10 |
| `audit/B1_P01-11_UNIDENTIFIED_ROWS_DECISIONS_v1.0.csv` + `.summary.md` | decisions on unidentified / «সূত্র নেই» rows | 40 rows |
| `audit/B1_P01-11_INTERNAL_SOURCE_ID_AUDIT_v1.0.md` | internal IDs, local paths, secondary stand-ins | — |
| `audit/B1_P01-11_SOURCE_REGISTER_v1.1.csv` | normalisation register | 95 keys |
| `manuscript-patches/B1_P01-11_MANUSCRIPT_PATCH_PLAN_v1.0.md` | proposed edits (header + §1 counts; block/NO_CHANGE lines counted) | 105 blocks / 223 NO_CHANGE |
| `sources/S-181_UMM_AYMAN_FADAK_VERIFICATION.md` | Umm Ayman / Fadak research report | — |

### 2.2 Hard limits

- **The manuscript DOCX is not available.** The only manuscript text is the ledger `Text` column (v1.3: `Exact_Text`), which holds source-note bullets and some prose lines. Every `Page` field reads `PAGE-CHECK (docx not available); ¶<Paragraph_Index>`.
- **Network:** sunnah.com, dorar.net, thaqalayn.net and cdn.jsdelivr.net are blocked; GitHub works. Only the six Sunni books are verifiable here, through `tools/verify_sunni.py` and the fawazahmed0/hadith-api Arabic corpus. Grades are those printed by the corpus grade field (later scholars and editors), not re-checked against sunnah.com or dorar.net.
- **Status vocabulary:** PAGE-CHECK · বর্ণিত আছে · সূত্র নেই/SOURCE-MISSING · NOT VERIFIED · PRINT BLOCKED · VERIFIED (live evidence) · VERIFIED-S181-URL · CANDIDATE · EDITION-LOCK PENDING · CORRECTED · CONFIRMED (edition-locked, print-ready).

### 2.3 Where the input files disagree (the later / corrected file is followed)

| # | Earlier statement (file) | Later / corrected statement (file) | Followed here |
|---|---|---|---|
| D-1 | Six-book check, table A: Muslim 91 ✅ «لا يدخل الجنة من في قلبه مثقال حبة من خردل من كبر» | C-18; Sunni evidence v1.1 §4: Muslim 91 has «ذرة من كبر» / «حبة خردل من كبرياء»; the verbatim wording is Abu Dawud 4091, Tirmidhi 1998, Ibn Majah 59 / 4173 | C-18 |
| D-2 | Six-book check, table A: Bukhari 7083 / Muslim 2888 «إذا التقى المسلمان بسيفيهما» | C-19: 7083 and 2888.01 read «إذا تواجه»; «التقى» is in Bukhari 31, 6875 and Muslim 2888.02 | C-19 |
| D-3 | Six-book check, table A: Tirmidhi 2951 for rows 223 **and 224** | C-04; Sunni evidence: REF-224 = Tirmidhi **2950** («بغير علم»); 2951 = «اتقوا الحديث عني» | C-04 |
| D-4 | Six-book check, table A: Bukhari 114 / 4431 ✅ for rows 134, 158 | C-25: «حسبنا كتاب الله» is in Bukhari 114, 4432, 5669, 7366 and Muslim 1637.03, not in 4431 / 3053 / Muslim 1637.01 | C-25 |
| D-5 | Six-book check, table A: Abu Dawud 2972 = «Umar b. Abd al-Aziz restores Fadak», ⚠ grade only | C-11; XRM-005: the text says «وإن فاطمة سألته أن يجعلها لها فأبى». It is a contrary report, Daif per three graders | C-11 |
| D-6 | Six-book check §D: "C-01…C-16" | The corrections file now runs to C-28 | C-01…C-28 |
| D-7 | Source register v1.1, HAD-RUYA: «Sunan Abu Dawud 5023 ("من رآني في المنام فقد رآني")» | C-01: 5023 reads «فسيراني في اليقظة»; «فقد رآني» is Bukhari 110 / Muslim 2266.01 | C-01. **The register row still needs updating** |
| D-8 | Audit v1.1 BUG-26: HAD-MADINAT-ILM = 5 rows | C-22; register v1.1: 6 rows (adds prose REF-308) | C-22 |
| D-9 | Audit v1.1 BUG-26: HAD-KISA = «Muslim 2424; Tirmidhi 3871» | C-05 / C-20; register v1.1: «أنت على مكانك» = Tirmidhi 3205 / 3787; 3871 = «إنك على خير» | C-05 |
| D-10 | Audit v1.1 BUG-25 list of 30 contains REF-007 | Ledger v1.2/v1.3 triage: REF-041 = UNID, REF-007 = CAND. The decisions file covers both rows | v1.3 (30 UNID = list with 041, without 007) |
| D-11 | Ledger v1.3 REF-158 Required_Action: «সহীহ বুখারি ১১৪, ৪৪৩১» | C-25: cite 4431 only for the Thursday scene, not for «حسبنا كتاب الله» | C-25. **The ledger cell still needs updating** |
| D-12 | Ledger v1.3 REF-293 Required_Action: "Numbers correct" | XRM-087: Muslim 2818 says «لن يدخل الجنة», not «لن ينجي»; C-21: the first two Muslim 2816 sub-reports are unnumbered in the corpus | XRM-087 / C-21 (open) |
| D-13 | Decisions summary: "REF-087 → Muslim 91" (canonical) | C-18: cite the book whose wording is quoted | C-18 (§11) |
| D-14 | Ledger v1.3 REF-075 Verified_Source: "Sahih al-Bukhari 3092 (… corrected target)" | C-02; Sunni evidence §4: the proof-04 passage «وهي جويرية فأقبلت تسعى» is Bukhari **520** | C-02 for the proof-04 passage |
| D-15 | Audit v1.1 BUG-22: Tirmidhi 3819, Abu Dawud 4784 and Tirmidhi 2952 = "da'if" | Grading control: all three DISPUTED. Zubair Ali Zai: Isnaad Hasan (3819, 4784); Shakir: Sahih Isnaad Maqtu (2952) | Grading control |
| D-16 | XRM summary: the Muslim-lookup fix was "uncommitted" in the working tree | Sunni evidence v1.1 §3: "fixed during this pass", all Muslim numbers re-run. The repository log checked while compiling this report shows commit `c231415` "Fix Muslim number matching …" | Fixed + re-run |
| D-17 | S-181 §5: once its 11-item checklist is complete, S-181 leaves "CONDITIONAL" | Work brief: the book gate stays PRINT BLOCKED | Book gate (§18) |
| D-18 | Task brief for this report: "residual flags F-1..F-9" | Umm Ayman control §4 lists **F-1…F-10** (F-10 = «أم أيمن أمي بعد أمي» without grade) | All ten are reported (§9) |

---

## 3 328-row coverage statement

**Manuscript source.** The DOCX (`B1_P01-11_reader.docx`) was **not available**. The ledger `Text` column is the only representation of the manuscript (v1.3 column `Exact_Text`). Every `Page` in v1.3 reads `PAGE-CHECK (docx not available); ¶<Paragraph_Index>`. Wherever this report says "manuscript", it means that column. Surrounding prose, real page numbers, and whether earlier patches (e.g. the S-181 patch) have been applied could not be seen.

Each of the 328 rows is covered three ways:

1. **Triaged in ledger v1.3.** Every row has a `Triage` code, a `Final_Status`, `Required_Action` and `Human_Review` value (§4).
2. **Patch block or NO_CHANGE line.** The patch plan has exactly one entry per row: **105** patch blocks (PB1-001…PB1-105, each naming one ledger REF) and **223** NO_CHANGE lines (§3 table of the plan). The check run for this report gave 105 + 223 = 328, with no missing row, no duplicate, and no row in both lists.
3. **Register key where applicable.** **162** rows carry a key in the v1.3 `Register_Key` column, which uses 60 distinct keys. The register v1.1 `Rows` column names **196** distinct rows across its 95 keys. The 34 extra rows belong to the 35 keys added in register v1.1 that were not back-filled into the ledger column (e.g. REF-087 → HAD-MITHQAL-KIBR, REF-105 → HAD-KAWTHAR-KHAYR). **132** rows have no register key: these are single-occurrence citations. REF-251 is one of them, and the S-ID audit asks for a key of its own (see BUG-44).

| Triage (v1.3) | Rows | Patch block | NO_CHANGE | v1.3 Register_Key | Named in register v1.1 | Human_Review = YES |
|---|---|---|---|---|---|---|
| SPC SHIA-PAGE-CHECK | 68 | 0 | 68 | 33 | 33 | 68 |
| CAND CANDIDATE | 67 | 5 | 62 | 33 | 34 | 67 |
| VL VERIFIED-LIVE | 62 | 32 | 30 | 35 | 62 | 24 |
| PROSE PROSE-LINE | 48 | 3 | 45 | 29 | 29 | 48 |
| UNID UNIDENTIFIED | 30 | 30 | 0 | 4 | 4 | 30 |
| HIST NON-HADITH | 17 | 1 | 16 | 3 | 3 | 0 |
| DUP DUPLICATE | 13 | 13 | 0 | 11 | 12 | 13 |
| MM MISMATCH | 12 | 12 | 0 | 6 | 10 | 12 |
| S181 RESOLVED-S181 | 5 | 5 | 0 | 5 | 5 | 5 |
| EDN EDITION-NUMBER | 4 | 4 | 0 | 3 | 4 | 4 |
| Q QURAN-TEXT | 2 | 0 | 2 | 0 | 0 | 0 |
| **Total** | **328** | **105** | **223** | **162** | **196** | **271** |

The per-triage block counts match the patch-plan header: MM 12, EDN 4, S181 5, DUP 13, UNID 30, VL 32, PROSE 3, CAND 5, HIST 1.

The other control files key into the same rows. The Shia control covers 109 rows, the cross-row CSV is referenced by 190 rows in v1.3 `Cross_Row_Mismatch`, the grading control by 39 rows in v1.3 `Grading`, the Fadak map by its `Ledger_Rows` column, and the decisions CSV by 40 rows.

---

## 4 Triage distribution (ledger v1.3)

| Triage | Rows | Meaning (audit v1.1 §1) |
|---|---|---|
| SPC SHIA-PAGE-CHECK | 68 | right Shia book named; volume/page/hadith to lock |
| CAND CANDIDATE | 67 | source identified from research knowledge; page to lock |
| VL VERIFIED-LIVE | 62 | six-book number + text confirmed 2026-10-03 |
| PROSE PROSE-LINE | 48 | «বর্ণিত আছে» prose; follows its source-block row |
| UNID UNIDENTIFIED | 30 | no classical source located (decided in §16) |
| HIST NON-HADITH | 17 | history / geography / poetry / institutional |
| DUP DUPLICATE | 13 | same reference as another row → one canonical citation |
| MM MISMATCH | 12 | wrong number / book / place / wording (§13) |
| S181 RESOLVED-S181 | 5 | Umm Ayman / Fadak testimony (S-181) |
| EDN EDITION-NUMBER | 4 | Bengali / local edition numbers |
| Q QURAN-TEXT | 2 | Quran wording checks |
| **Total** | **328** | |

**`Final_Status` distribution (v1.3, computed):**

| Final_Status | Rows |
|---|---|
| PAGE-CHECK (Shia source; edition/page lock) | 68 |
| CANDIDATE — PAGE-CHECK (not live-verifiable here) | 67 |
| VERIFIED (six-book number + text, 2026-10-03); grade/edition per control tables | 62 |
| PROSE — follows source-block row | 48 |
| NON-HADITH — PAGE-CHECK | 17 |
| NORMALISE via register key | 13 |
| CORRECTED — manuscript patch pending | 12 |
| PLAUSIBLE_SOURCE_ONLY — KEEP-ATTRIBUTION-ONLY «বর্ণিত আছে» | 11 |
| NO_SOURCE_LOCATED — KEEP-ATTRIBUTION-ONLY «বর্ণিত আছে» | 8 |
| S-181: VERIFIED-S181-URL / EDITION-LOCK PENDING | 5 |
| EDITION-NUMBER MAP PENDING (use standard numbering) | 4 |
| NO_SOURCE_LOCATED — FLAG-FOR-AUTHOR-DECISION | 4 |
| SECONDARY_SOURCE_ONLY — KEEP-«বলা হয়» | 3 |
| CANONICAL_SOURCE_FOUND — FLAG-FOR-AUTHOR-DECISION | 2 |
| PLAUSIBLE_SOURCE_ONLY — FLAG-FOR-AUTHOR-DECISION | 2 |
| QURAN TEXT CHECK | 2 |
| **Total** | **328** |

Other v1.3 columns:
- `Human_Review`: YES 271, NO 57.
- `Edition`: EDITION NOT LOCKED 161; standard numbering (sunnah.com / Abd al-Baqi) 61; blank 106.
- `Claim_Support`: "not verifiable here" 135; "NO — citation does not support the sentence as written" 12.
- No row has Final_Status CONFIRMED.

---

## 5 Cross-row mismatches (92 rows, XRM-001…XRM-092)

Counts per conflict type. A row may carry several letters: "All tags" counts every letter, "Primary" counts only the first. These counts were recomputed from the CSV and match the summary.

| Code | Conflict type | All tags | Primary |
|---|---|---|---|
| A | same hadith under different numbers | 4 | 2 |
| B | different grading / grade missing | 11 | 7 |
| C | VERIFIED/CONFIRMED vs PAGE-CHECK for the same source | 20 | 18 |
| D | same narration, different wording/source combination | 24 | 9 |
| E | source used for a stronger claim | 5 | 3 |
| F | Sunni/Shia blending or misclassification | 9 | 2 |
| G | primary wording merged with commentary | 8 | 4 |
| H | book/volume/page/edition conflicts | 10 | 9 |
| I | hadith-number conflicts | 11 | 8 |
| J | character/name/location/speaker conflicts | 15 | 14 |
| K | «সূত্র নেই» where a source exists | 8 | 6 |
| L | CONFIRMED/VERIFIED where only text existence is shown | 5 | 4 |
| M | citation supports only part of the sentence | 12 | 5 |
| N | citation reused outside its context / wrong register | 5 | 1 |
| | **Total rows** | — | **92** |

Evidence base: 37 rows rest in part on research-layer knowledge (Correct_Status CANDIDATE / PAGE-CHECK). 51 rows quote live six-book corpus output. Five rows (XRM-082, 084–087) are row-vs-corpus conflicts with a context row as Row_B.

**Top 10 for print safety** (summary §2):

| # | XRM | Rows | Conflict |
|---|---|---|---|
| 1 | XRM-001 | REF-276 vs 279 | **Basra, not Kufa.** Bukhari 784 «صلى مع علي … بالبصرة»; the remark is Imran b. Husayn's, not «সাহাবারা» |
| 2 | XRM-002 (+092) | REF-081 | **Aus ibn al-Hadathan listed as a witness with Umm Ayman / Ali.** S-181 places him with Aisha and Hafsa on «لا نورث». He is not Malik b. Aws b. al-Hadathan (Bukhari 3094/4033, Muslim 1757) |
| 3 | XRM-009 | REF-157 | «কিতাবুল্লাহ ও আমার ইতরাত» CONFIRMED under Muslim 2408. Muslim 2408.01–.04 has «ثقلين … وأهل بيتي»; «عترتي» is absent |
| 4 | XRM-025 (+026) | 28 rows | The Muslim "VERIFIED-LIVE" evidence trail came from a lookup that returned the wrong hadith. The conclusions were re-confirmed after the fix (§6) |
| 5 | XRM-005 (+006) | REF-079 | Abu Dawud 2972 is cited only for the restoration. Its text says «فأبى»; three graders Daif; the patch labels it CONFIRMED |
| 6 | XRM-014 | REF-013 | Abu Dawud 5023 reads «فسيراني في اليقظة», not «فقد رآني» |
| 7 | XRM-028/029/030 | REF-222, 304, 308 | Weak reports as flat «রাসূলুল্লাহ ﷺ বলেছেন»: Tirmidhi 2951; Abu Dawud 4784 (merged with sahih 4782); Tirmidhi 3723 (self-declared «غريب منكر») |
| 8 | XRM-062 | REF-123 | «আমরা নবীগণ উত্তরাধিকার রেখে যাই না» (= «معاشر الأنبياء», the al-Ihtijaj wording) printed on Bukhari/Muslim numbers |
| 9 | XRM-059 | REF-075 | «وهي جويرية فأقبلت تسعى» = Bukhari **520**, not 3110 |
| 10 | XRM-039 | REF-144/274 vs 187/267/269 | Chapter «নয় মাস ধরে…» cites Tirmidhi 3206: Anas, **six** months, fajr only, da'if |

Close behind (summary): XRM-042/043 «লেজকাটা দরুদ» (speaker, expanded dialogue); XRM-066 (3874/3868 munkar, 3819 da'if, no grade printed); XRM-038 (Muslim 2424 CONFIRMED for an Umm Salama version not in it); XRM-022 (Bukhari 3705 for a different Tasbih order/timing); XRM-064 (Fadak as Khadija's mahr, no source).

The XRM summary recommends splitting the register keys that mix different hadiths: HAD-IMAM-JAHILIYYA, HAD-WILAYA-KAFI, HAD-FADAK-1726, HAD-FADAK-TESTIMONY (REF-141), HAD-FATIMA-NAR and HAD-MANZILA/MUBAHALA.

---

## 6 Numbered Sunni hadith verification

**Scope.** Every number the ledger attaches to Bukhari / Muslim / Abu Dawud / Tirmidhi / Ibn Majah / Nasa'i was checked, both in `Text` and in `Candidate_Source`, including audit-proposed numbers (tag `AU`) and numbers found by the search itself (`NEW`: Bukhari 520, Muslim 1794.01). The ledger cites **no** numbered Nasa'i hadith.

**Classification counts (per book × number × row triple):**

| Classification | Triples |
|---|---|
| EXACT_MATCH | 146 |
| PARTIAL_MATCH | 35 |
| GRADING_MISMATCH | 14 |
| EDITION_DEPENDENT | 7 |
| WRONG_TEXT | 6 |
| WRONG_SUBJECT | 3 |
| WRONG_NUMBER | 2 |
| NOT_FOUND | 1 |
| SOURCE_EXISTS_BUT_CLAIM_TOO_STRONG | 0 |
| **Total** | **214** |

Table lines: 176 (book × number) + 11 wording-only rows; 152 distinct (book, number) pairs.

- **WRONG_NUMBER (2):** REF-013 Abu Dawud 5021 (Abu Qatada, «الرؤيا من الله والحلم من الشيطان»); REF-075 Bukhari 3110 (audit pointer; the passage is 520).
- **WRONG_TEXT (6):** REF-016 Tirmidhi 3370; REF-022 Muslim 1015 and Tirmidhi 3462; REF-164 Tirmidhi 3723; REF-276 Bukhari 784 (location: Basra); REF-280 Tirmidhi 3714.
- **WRONG_SUBJECT (3):** REF-011 Tirmidhi 3786 (Thaqalayn, not the Ark); REF-099 Muslim 2369 («يا خير البرية — ذاك إبراهيم»); REF-160 Bukhari 5989 («الرحم شجنة»).
- **NOT_FOUND (1):** REF-237 Ibn Majah 116 (Ghadir report without the «بخ بخ» congratulation).
- **GRADING_MISMATCH (14):** Ibn Majah 2198 (005), 224 (009); Abu Dawud 4213 (071), 2972 (079), 3652 (225), 4784 (305); Tirmidhi 3874, 3868, 3819 (073), 3206 (144, 274), 3723 (309), 2951 (223), 2952 (225).
- **Wording-only searches**, absent from all six books: the Ark of Noah; «الجنة طيبة لا يدخلها إلا الطيب»; «أنا مدينة العلم»; «علي مع الحق»; Ghadir «بخ بخ»; Mi'raj «مقاريض» (as a lips-scissors report); «الشرك الأصغر»; «بزفرة»; «أحصنت فرجها» / «فطم»; «الصلاة البتراء»; «أم أبيها». NOT FOUND here does not mean the report does not exist.

**The tool-fix incident and re-verification.**
- **Defect.** In the first run, `verify_sunni.find()` matched Muslim Abd al-Baqi numbers only when they had no sub-suffix. For ids such as `2408.01` it silently fell back to the corpus-internal sequential number and printed a **different hadith**. Examples: `show muslim 2408` → a Zakat hadith; 2404 → Zakat; 1851 → Travellers' prayer; 8 and 91 → empty Introduction entries. About 28 VL rows were affected (XRM-025), and Muslim 2989 was wrongly left at PAGE-CHECK (XRM-026; C-13, C-14).
- **Why conclusions held.** The six-book table's Muslim verdicts had come from `search`, which was unaffected. The Sunni-evidence and XRM passes verified Muslim lines directly by `arabicnumber` prefix.
- **Fix and re-run.** The fix matches the integer part of `arabicnumber` and never falls back. Every Muslim number was re-run with the fixed tool: 8, 91, 395, 667, 705, 761, 863, 1015, 1637, 1759, 1821, 1822, 1851, 1905, 1907, 2175, 2266, 2369, 2404, 2408, 2424, 2449, 2450, 2581, 2800–2802, 2816–2818, 2888, 2989, 6062. **No classification or grading note changed.** Muslim 2989.02 is now confirmed, and `show muslim 6062` = NOT FOUND (there is no Abd al-Baqi 6062).
- **Residual caveats.**
  - `show` prints at most 4 sub-reports (AB 2404.05 was read via `find()`).
  - The first two Muslim 2816 sub-reports are unnumbered in the corpus; use `search` for them (C-21).
  - The `.md` table of the six-book check was partly built on the old run and keeps stale lines (§2.3 D-1…D-6). It must be rebuilt (§19 step 7).
  - Corpus `section` labels are not fully reliable.

**Edition-dependent numbers (7 triples).**

| Row | Number as printed | Finding |
|---|---|---|
| REF-049 | Bukhari «1815» (Adhunik Prokashoni) | standard 1815 = Ka'b b. Ujra (lice); the hadith is standard **1954** |
| REF-075 | Bukhari «2874, 3446, 6270, 496» (Bengali ed.) | the same numbers in standard numbering are unrelated hadith; mapping needs the author's edition → PAGE-CHECK (do not guess) |
| REF-107 | Muslim «6062 / p. 917» (Bengali ed.) | no Abd al-Baqi 6062; standard = Muslim **2404** (verified at AB 2404.04) (C-28) |
| REF-223 | Tirmidhi «২৯৫০/২৯৫১ সংস্করণভেদে» | corpus: 2950 = «من قال في القرآن بغير علم»; 2951 = «اتقوا الحديث عني … برأيه» |

Related numbering items:
- REF-126: Bukhari 4240 is flagged as a "Bengali-edition number to map".
- REF-013: an edition reading of Abu Dawud «5021» cannot be excluded.
- REF-043: Muslim «2408a». The corpus sub-ids are 2408.01–.04, and which one «a» means cannot be determined here.
- Honorifics and minor wording, e.g. «نعم / نعمت» (Bukhari 2010, C-06) and «عليها السلام», reflect this one digital edition only.

**What changes in the ledger.**
- The 62 VL rows have their six-book **number** confirmed. Their v1.2 Status column still reads PAGE-CHECK / «বর্ণিত আছে» (XRM-081), and they are **not** CONFIRMED.
- Still open for these rows: grade printing (§10), a single numbering system (BUG-12), the edition / page lock, and the wording caveats C-01, C-08, C-18 and C-19.

---

## 7 Shia-source verification

**What is covered.** The Shia control has 169 citation lines (some ledger rows are split into sub-lines such as REF-081/a…f) for **109 distinct ledger rows**. It covers every row triaged SPC (68) plus the Shia lines inside 35 CAND, 4 S181 and 2 MM rows.

Works, by number of lines:

| Work | Lines |
|---|---|
| al-Kafi | 38 |
| Bihar al-Anwar | 38 |
| Nahj al-Balagha | 9 |
| Tafsir al-Qummi | 8 |
| al-Ihtijaj | 6 |
| Manaqib Al Abi Talib | 6 |
| Tafsir al-Ayyashi | 5 |
| 'Ilal al-Shara'i' | 4 |
| Sharh Nahj al-Balagha | 4 |
| Ma'ani al-Akhbar | 4 |
| Kamal al-Din, 'Uyun Akhbar al-Rida, Majma' al-Bayan, Ghurar al-Hikam | 3 each |
| Kitab Sulaym, Qurb al-Isnad, Fiqh al-Rida, Tahdhib al-Ahkam, Man la yahduruhu al-faqih, al-Khisal, Misbah al-Mutahajjid, Jamal al-Usbu', Misbah al-Shari'a (attributed) and others | 1–2 each |

**Status of the 169 lines:**

| Verification_Status | Lines |
|---|---|
| PAGE-CHECK | 98 |
| CANDIDATE | 64 |
| VERIFIED-S181-URL | 7 |
| **Total** | **169** |

Edition: **159 lines EDITION NOT LOCKED**. The other 10 name or assume an edition (Subhi Salih numbering, Mu'assasat al-Wafa, al-Khurasan ed., Dar Ihya al-Kutub al-Arabiyya, the Ansari ed. suggested by S-181, two editions reported by S-181), and none of those is locked.

**Nothing Shia is live-verified.** No Shia corpus is reachable from this environment: thaqalayn.net is blocked and no local Shia corpus exists. So every volume, page, bab and hadith number for al-Kafi, Bihar, 'Ilal, Kamal al-Din, al-Ihtijaj, the tafsirs of al-Qummi and al-Ayyashi, Sulaym, Qurb al-Isnad and Fiqh al-Rida is unverified. The same holds for every Imam attribution and every wording (XRM summary §3).

The 7 VERIFIED-S181-URL lines are REF-078, 081/a, 081/b, 081/c, 081/d, 081/f and 082. In each case **S-181 recorded a URL; the URL was not re-opened here.** "VERIFIED-S181-URL" is a research-layer status and is not live evidence from this environment.

Notable Shia-control findings:
- **The Ayyashi 67:22 doubt (REF-174/c).** The ledger cites *Tafsir al-Ayyashi* "on Q 67:22 (page not given)", status CANDIDATE. The control note reads: «CAUTION (knowledge-based, unverified here): the extant Tafsir al-Ayyashi is generally reported to stop at Surat al-Kahf — a 67:22 report there is doubtful.» Required action: **confirm existence before citing; otherwise drop Ayyashi for 67:22.** The caution is itself knowledge-based and is recorded as a doubt, not as a finding.
- **Speaker / Imam conflicts** inside Shia lines:
  - XRM-042: «লেজকাটা দরুদ», an Imam's address in al-Kafi, voiced as the Prophet's words in the prose.
  - XRM-070: Abu Abdullah vs Abu Ja'far.
  - XRM-072: al-Rida vs al-Kazim/al-Sadiq.
  - XRM-052: the book title «ফিকহুর রেজা» turned into Imam al-Rida's direct speech.
- **Placement / numbering conflicts:**
  - XRM-021: Tasbih in al-Kafi 2 vs 3 vs Man la yahduruh.
  - XRM-045: Bihar 85:20 vs 82:20.
  - XRM-046: one al-Kafi hadith under two bab names.
  - XRM-047: 'Ilal bab numbering.
  - XRM-065: al-Ihtijaj 1 paginations.
- **Classification:** al-Hasakani, *Shawahid al-Tanzil*, is triaged as Shia (SPC) in some rows and as a Sunni CANDIDATE in others (XRM-067). The Fadak map notes that al-Haskani is usually classed as a Hanafi (Sunni) author; that classification is knowledge-based, and the author is to confirm it.

---

## 8 Fadak evidence map (73 lines, eleven claim units)

Sunni lines: 45. Shia lines: 28. Statuses overall: VERIFIED-S181-URL 28 · VERIFIED-LIVE 24 · NOT VERIFIED 9 · PAGE-CHECK 7 · CANDIDATE 5.

| # | Claim unit | Lines | Sunni lines (status) | Shia lines (status) |
|---|---|---|---|---|
| 1 | Fatima's claim to Fadak (inheritance / grant) | 15 | VL 6 · S181-URL 1 · CAND 2 · PAGE-CHECK 1 | S181-URL 3 · PAGE-CHECK 2 |
| 2 | Abu Bakr's «لا نورث» response | 8 | VL 5 · CAND 1 | S181-URL 2 |
| 3 | Ali's testimony | 7 | S181-URL 2 · NOT VERIFIED 1 | S181-URL 3 · PAGE-CHECK 1 |
| 4 | Umm Ayman's testimony | 8 | S181-URL 2 · NOT VERIFIED 1 · CAND 1 | S181-URL 4 |
| 5 | Aus b. al-Hadathan counter-testimony («لا نورث» side) | 5 | VL 1 (Malik b. Aws blocking row) · NOT VERIFIED 1 | S181-URL 2 · PAGE-CHECK 1 |
| 6 | Aisha / Hafsa testimony | 6 | VL 2 · NOT VERIFIED 1 | S181-URL 2 · PAGE-CHECK 1 |
| 7 | Witness-count argument («رجلين أو رجل وامرأتين») | 5 | S181-URL 2 · NOT VERIFIED 1 | S181-URL 2 |
| 8 | Written-document (deed) episode | 5 | S181-URL 1 (absence row) · NOT VERIFIED 2 | S181-URL 1 · NOT VERIFIED 1 |
| 9 | Umar's intervention | 6 | VL 3 · NOT VERIFIED 1 | S181-URL 1 · CAND 1 |
| 10 | Burial at night (what Bukhari 4240 says) + **10-W** Fatima's will (separate unit, Shia only) | 2 + 1 | VL 2 | 10-W: PAGE-CHECK 1 (Bihar 43:183 ff) |
| 11 | Fatima's anger / separation («فهجرته فلم تكلمه حتى توفيت») | 5 | VL 5 | — |
| | **Total** | **73** | **45** | **28** |

**What each status rests on.**
- **VERIFIED-LIVE** lines are six-book texts read in the corpus: Bukhari 4240–4241, 3092/3093, 6725/6726, 3094; Muslim 1757.03, 1758, 1759; Abu Dawud 2963, 2968, 2972.
- **NOT VERIFIED** lines are mostly six-book string searches with 0 hits, e.g. «فدك»+«أم أيمن», recorded as "NOT FOUND ≠ DOES NOT EXIST". Two are *Tarikh al-Khulafa* (Suyuti) items that the ledger could not locate. One is the Prophet-wrote-the-deed version (C08-X01, see F-1).

**Baladhuri vs al-Ihtijaj: never merged** (S-181 §3-F; map C03, C04, C07, C08).
- **al-Baladhuri, *Futuh al-Buldan* (Sunni).** Recension 1: «وشهد لها علي بن أبي طالب فسألها شاهدا آخر فشهدت لها أم أيمن», and Abu Bakr answers «لا تجوز إلا شهادة رجلين أو رجل وامرأتين». Recension 2: «فجاءت بأم أيمن ورباح مولى النبي … فشهدا لها بذلك» (Ali not named), with «لا تجوز فيه إلا شهادة رجل وامرأتين». **No deed** in either recension: the deed belongs only to the al-Ihtijaj recension. Never build an R1 + R2 composite such as "Ali + Umm Ayman + Rabah". Edition: PAGE-CHECK (p. 30/35 vs 44–45; «527» is reference numbering).
- **al-Ihtijaj 1 (Shia).** Umm Ayman testifies, then Ali. Abu Bakr writes a deed («فكتب لها كتابا ودفعه إليها»), and Umar takes or tears it. Abu Bakr's stated position: «إن هذا فيء للمسلمين…». Umar's counter-argument: «أوس بن الحدثان وعائشة وحفصة يشهدون … إنا معاشر الأنبياء لا نورث» and «وأم أيمن فهي امرأة صالحة، لو كان معها غيرها لنظرنا فيه». Edition: pp. 90–92 vs 119–127, EDITION-LOCK PENDING.
- **The «state property» wording is not quoted from Baladhuri** in S-181 (C02-S06, CANDIDATE). The closest attested wording is al-Ihtijaj's «فيء للمسلمين», and it must not be transferred to Baladhuri.

**Aus ibn al-Hadathan vs Malik b. Aws b. al-Hadathan** (C-16; XRM-002, XRM-092; map C05).
- **Aus ibn al-Hadathan** (Banu Nadr) appears only in Shia chains, as a **counter**-witness with Aisha and Hafsa:
  - *Qurb al-Isnad* h. 99 / 335: «شهدت عليها عائشة وحفصة، ورجل من العرب يقال له أوس بن الحدثان … لا أورث». Bihar 22/101 h. 59 is PAGE-CHECK.
  - al-Ihtijaj: «إنا معاشر الأنبياء لا نورث».
  - He is never Umm Ayman's or Ali's co-witness.
- **Malik b. Aws b. al-Hadathan** is the Sunni **narrator** of Umar's later «لا نورث» session in his caliphate (Bukhari 3094, Muslim 1757.03, Abu Dawud 2963; C05-S01, VERIFIED-LIVE). He is a different person, in a different role, at a different time, and is no evidence for or against Aus. Searching «ابن الحدثان» in the six books returns only Malik, which invites the conflation.

**Unit 10.** Bukhari 4240 says exactly this: night burial **by Ali**, Abu Bakr not informed, Ali prayed over her. It has no will, no instruction to conceal the grave, and no night ghusl or kafan. The will (10-W) is cited only to its Shia source, with «শিয়া সূত্রে বর্ণিত», never under 4240 (BUG-17).

**Unit 9.** Abu Dawud 2972 is a **contrary** report («فأبى», C-11). It is cited with that content and its grade, not as support for the restoration claim.

---

## 9 Umm Ayman audit

**Units:** ID (identity) · REL (relationship to the Prophet ﷺ) · PAR (Paradise report: (a) Ibn Sa'd, (b) Bihar 29, (c) al-Hakim) · FAD (Fadak testimony) · FAM (later marriage / family).

**Passage inventory:**
- Ledger REF-081 (¶2816): Aus merged with Umm Ayman / Ali, pre-patch.
- REF-082 (¶2817): «জান্নাতি», Ibn Sa'd, no grade.
- REF-078 (¶2762): «লিখেও দিয়ে গেছেন».
- REF-122 (¶5291): Baladhuri next to the deed-tearing.
- REF-141 (¶5760): Umm **Hani**.
- Patch A-1, A-2, A-3 (p. 213) and patch B bullets 1–4 (p. 217) of `manuscript-patches/B1_P03_C06_FADAK_S-181_PATCH.md`.
- No blending was found in REF-085, REF-027/148 or REF-106. «কোলে-পিঠে মানুষ» does not occur in the ledger or the patch.

| Unit | Allowed formulation | Forbidden formulation | Source + status |
|---|---|---|---|
| **IDENTITY** | «উম্মে আইমান (বারাকা বিনতে সা'লাবা)», with source attributed | «উম্মে আইমান ছিলেন রাসূলের স্ত্রী» / «নবীজির স্ত্রী» (S-181 §1: FALSE); a specific owner claim such as «আমিনার দাসী» (S-181 §1-D: not safe) | al-Isti'ab «بركة بنت ثعلبة … وهي أم أيمن»: VERIFIED-S181-URL (pagination vol. 12 pp. 221–223 vs 876–877: PAGE-CHECK); al-Isaba 4/415–416: VERIFIED-S181-URL, edition PAGE-CHECK |
| **RELATIONSHIP** | «রাসূল ﷺ-এর মাওলা (মুক্ত দাসী) ও লালনকারিণী (হাদিনা, حاضنة)»; «যাঁর কোলে-পিঠে নবীজি বড় হয়েছেন» only as narration of «حاضنة», not as a quotation | «স্ত্রী» in any form; «মা» as fact («أم أيمن أمي بعد أمي» only as «আল-ইসতি'আবে বর্ণিত»); «হাদী» alone (F-5) | **VERIFIED-LIVE:** Bukhari 2630 / Muslim 1771.01 «أم أيمن مولاته أم أسامة بن زيد»; Bukhari 3737 «وكانت حاضنة النبي ﷺ» (appended remark); Muslim 2453; Muslim 2454 = Ibn Majah 1635. VERIFIED-S181-URL: al-Isaba «مولاة النبي ﷺ وحاضنته» |
| **PARADISE (a) Ibn Sa'd, Sunni** | «ইবনে সা'দের *আত-তাবাকাতুল কুবরা*-তে একটি **মুরসাল** বর্ণনায় এসেছে — "যে জান্নাতের একজন নারীকে বিবাহ করতে চায়, সে উম্মে আইমানকে বিবাহ করুক।"», with the grade in the source block | unqualified «উম্মে আইমান জান্নাতি» as a sahih fact; «সহিহ হাদিসে রাসূল ﷺ বলেছেন…»; flat «রাসূল ﷺ বলেছেন»; «তিনি জান্নাতি» without the conditional frame | «من سره أن يتزوج امرأة من أهل الجنة فليتزوج أم أيمن»: VERIFIED-S181-URL. Mursal (Sufyan b. Uqbah); al-Suyuti مرسل; al-Albani ضعيف, *Silsilat al-Da'ifa* 2260 (PAGE-CHECK). Vol. 8 p. 224 vs vol. 10: EDITION-LOCK PENDING |
| **PARADISE (b) Bihar 29, Shia** | «শিয়া সূত্রে, ফাদাকের বর্ণনার ভিতরে এসেছে: "إن أم أيمن امرأة من أهل الجنة"», with Shia attribution every time | merging (a) and (b) into one statement; presenting (b) as a direct saying of the Prophet ﷺ (speaker not identified, F-3); citing (b) for the marriage wording | Bihar 29, bab 11: VERIFIED-S181-URL; p. 176 vs p. 128: EDITION-LOCK PENDING |
| **PARADISE (c) al-Hakim** | nothing | any «হাকিম / আল-মুস্তাদরাক» citation for the Paradise wording | **NOT VERIFIED / PRINT BLOCKED** (S-181 §2-C) |
| **FADAK TESTIMONY** | each recension under its own attribution (Baladhuri R1 / R2; al-Ihtijaj; Sulaym «ولم يصدقها، ولا صدق أم أيمن»; Ibn Abi al-Hadid 16 «إن أم أيمن تشهد لي بأن رسول الله أعطاني فدك»); Aus only in a separate sentence as counter-witness with «শিয়া সূত্রে» | Aus as Umm Ayman's / Ali's co-witness; a Baladhuri + al-Ihtijaj or R1 + R2 composite; «Baladhuri: deed torn»; any six-book hadith for her testimony (0 hits); Malik b. Aws = Aus | Baladhuri, al-Ihtijaj, Sulaym, Ibn Abi al-Hadid 16, Bihar 29, Qurb al-Isnad: VERIFIED-S181-URL, edition PAGE-CHECK / EDITION-LOCK PENDING |
| **LATER MARRIAGE / FAMILY** | «পরে তিনি যায়েদ ইবনে হারিসা (রা.)-কে বিবাহ করেন এবং উসামা ইবনে যায়েদ (রা.)-এর মা হন» | using the mursal Paradise report as the source or motive for the marriage; any wording making her the Prophet's wife | VERIFIED-LIVE: Bukhari 2630 / Muslim 1771.01 «أم أسامة بن زيد»; Bukhari 3736 «أيمن ابن أم أيمن أخا أسامة لأمه»; VERIFIED-S181-URL: Ibn Sa'd, al-Isti'ab |

The six books contain **no** Umm Ayman Fadak testimony and **no** Paradise report about her (string searches). Bukhari 4120 / Muslim 1771.02 (the date palms) is **not Fadak**.

**Residual flags.** The control file has ten flags; F-10 is included although the task named F-1..F-9.

| # | Where | Problem | Required action |
|---|---|---|---|
| F-1 | REF-078 | Prose: the **Prophet** «লিখেও দিয়ে গেছেন»; al-Ihtijaj's writer is **Abu Bakr** («فكتب لها كتابا ودفعه إليها») | Keep «বর্ণিত আছে» with no al-Ihtijaj citation for the Prophet-wrote version, or switch to the Ihtijaj recension with «শিয়া সূত্রে». Author's decision |
| F-2 | Patch B•2 | Ibn Sa'd (Sunni, mursal) and Bihar 29 (Shia) in one bullet | Keep the line break and the «শিয়া সূত্রে:» marker |
| F-3 | Patch A-2(খ) | «إن أم أيمن امرأة من أهل الجنة» has no identified speaker (elided «فقال …») | Not «রাসূল ﷺ বলেছেন» until the page is read; PAGE-CHECK the speaker |
| F-4 | Patch A-3 Aus sentence | No tradition attribution; «আমরা নবীরা…» = al-Ihtijaj «إنا معاشر الأنبياء»; Qurb al-Isnad has «لا أورث» | Prefix «শিয়া সূত্রে (কুরবুল ইসনাদ; আল-ইহতিজাজ)…»; quote the cited source's wording |
| F-5 | Patch A-1, B•1, S-181 §1 | «হাদী» (meant: حاضنة) reads as هادي «guide», the word used for Ali in REF-179 | Prefer «লালনকারিণী (হাদিনা)». Author's choice |
| F-6 | REF-122 | Baladhuri / Tabari («state property») sits next to the deed-tearing; Baladhuri has no deed; Suyuti not located | Split the bullet; tearing only to al-Ihtijaj (or IAH 16 once a page is found); drop Suyuti unless a page is found |
| F-7 | Register HAD-FADAK-TESTIMONY | One lock covers deed (078), testimony (081), state property / tearing (122) and **Umm Hani** (141) | Split into sub-keys (e.g. -BALADHURI / -IHTIJAJ / FADAK-DEED / FADAK-COUNTER-AUS / FADAK-UMM-HANI) |
| F-8 | Patch B•1 vs HAD-UMM-ABIHA | Edition mixing: al-Isaba 4/415–416 vs 8:262; al-Isti'ab vol. 12 / 876–877 vs 4:1899; Ibn Sa'd vol. 8 p. 224 vs vol. 10 vs 8:24 | One edition per work for the whole book |
| F-9 | Patch B•3 | Sulaym is cited for Ali's testimony, but the quoted Sulaym text covers only the bayyina demand / Umm Ayman not believed | PAGE-CHECK Sulaym for Ali first |
| F-10 | Patch B•1 | «أم أيمن أمي بعد أمي» printed with no grade | Give the grade or attribute it as «আল-ইসতি'আবে বর্ণিত»; never a flat saying |

---

## 10 Hadith grading control (38 rows)

**Grade owner.** Every grade below is a **later scholar's or editor's**, as printed by the hadith-api corpus grade field (not re-verified on sunnah.com or dorar.net, which are blocked). The compilers' own hukm is not in the structured field. For Tirmidhi, the corpus **text** often embeds Tirmidhi's own remark, which is quoted in a separate column; this deviates from the brief's blanket "compiler grade: not in corpus" and is flagged because it changes the picture (e.g. 3868/3874: Tirmidhi «حسن غريب» vs Albani/Shakir «Munkar»). Bukhari and Muslim entries carry no grade field and are not in this table.

**Safety classes (38):**

| Safety class | Rows |
|---|---|
| SAHIH-PER-GRADERS | 15 |
| WEAK REPORT | 6 |
| GRADERS DISAGREE | 6 |
| DISPUTED | 5 |
| MUNKAR | 2 |
| VERY WEAK | 2 |
| SOURCE EXISTS BUT NOT ACCEPTABLE AS UNQUALIFIED PROOF | 1 |
| HASAN-PER-GRADERS | 1 |

By book: Tirmidhi 26, Abu Dawud 8, Ibn Majah 4.

**The rule against flat «রাসূল ﷺ বলেছেন» (BUG-22; Global Law).** A *munkar*, *da'if*, very weak or disputed report may be narrated **only with its grade and named graders**, never as a flat «রাসূল ﷺ বলেছেন». The allowed formulations in the control file are of the form:

- WEAK / VERY WEAK / MUNKAR: «তিরমিযিতে একটি দুর্বল (দাঈফ) বর্ণনা আছে (আহমাদ শাকির: দাঈফ; আলবানী: দাঈফ; যুবাইর আলী যাঈ: দাঈফ) যাতে বলা হয়েছে …» — «রাসূল ﷺ বলেছেন» নয়
- DISPUTED: «… এর মান নিয়ে মতভেদ আছে — অধিকাংশ গ্রেডার দাঈফ বলেছেন (…) — …» — «রাসূল ﷺ বলেছেন» নয়
- GRADERS DISAGREE: «… এর মান নিয়ে মতভেদ আছে (…) — …» — মতভেদ-বাক্য ছাড়া «রাসূল ﷺ বলেছেন» নয়
- Tirmidhi 3723: «তিরমিযিতে «أنا دار الحكمة وعلي بابها» শব্দে একটি বর্ণনা আছে (…); এটি «জ্ঞানের নগরী» (مدينة العلم) প্রমাণ হিসেবে উপস্থাপনযোগ্য নয়»
- Tirmidhi 3775 (HASAN): সব গ্রেডার «হাসান» বলেছেন («সহীহ» নয়); «সহীহ» লেখা যাবে না
- SAHIH-PER-GRADERS: «… বর্ণিত (graders) — …»; «রাসূল ﷺ বলেছেন» লিখতে হলে সংস্করণ-পৃষ্ঠা লক (PAGE-CHECK মুক্ত) হওয়ার পর

Abu Dawud 2972: the manuscript's attribution «আবু দাউদের মতে ضعيف» must become the printed graders (Al-Albani, Muhammad Muhyi al-Din Abdul Hamid, Zubair Ali Zai). The «قال أبو داود» in the text is a comment, not a grade.

**Mandatory numbers with grades as printed.** Rows 1–22 (munkar / very weak / weak / disputed / graders disagree / not acceptable as unqualified proof) must carry the grade qualifier and named graders in print. Row 23 (Tirmidhi 3775) must print «হাসান», never «সহীহ». Rows 24–38 (sahih per graders) still print the graders and stay PAGE-CHECK until edition lock.

| # | Book · No. | Rows | Key wording | Grades as printed (later graders) | Compiler remark in corpus text | Safety class |
|---|---|---|---|---|---|---|
| 1 | Tirmidhi 3868 | 073 | «أحب النساء إلى رسول الله» | Ahmad Muhammad Shakir → Munkar; Al-Albani → Munkar; Zubair Ali Zai → Daif | «قال أبو عيسى هذا حديث حسن غريب لا نعرفه إلا من هذا الوجه» | MUNKAR |
| 2 | Tirmidhi 3874 | 073 | «زوجها» | Ahmad Muhammad Shakir → Munkar; Al-Albani → Munkar; Zubair Ali Zai → Daif | «هذا حديث حسن غريب» | MUNKAR |
| 3 | Ibn Majah 224 | 009 | «طلب العلم فريضة على كل مسلم» | Al-Albani → Very Daif; Muhammad Fouad Abd al-Baqi → Very Daif; Shuaib Al Arnaut → Very Daif; Zubair Ali Zai → Daif | n/a (no compiler grade in corpus) | VERY WEAK |
| 4 | Tirmidhi 3714 | 280 | «رحم الله عليا اللهم أدر الحق معه حيث دار» | Ahmad Muhammad Shakir → Very Daif; Al-Albani → Very Daif; Zubair Ali Zai → Daif | «قال أبو عيسى هذا حديث غريب لا نعرفه إلا من هذا الوجه» | VERY WEAK |
| 5 | Tirmidhi 3723 | 164; 309 | «أنا دار الحكمة وعلي بابها» | Ahmad Muhammad Shakir → Daif; Al-Albani → Daif; Zubair Ali Zai → Daif | «هذا حديث غريب منكر» | SOURCE EXISTS BUT NOT ACCEPTABLE AS UNQUALIFIED PROOF |
| 6 | Abu Dawud 2972 | 079 | «رددتها على ما كانت» | Al-Albani → Daif; Muhammad Muhyi Al-Din Abdul Hamid → Daif; Zubair Ali Zai → Daif | «قال أبو داود» comment (not a grade) | WEAK REPORT |
| 7 | Abu Dawud 3652 | 225 | «من قال في كتاب الله عز وجل برأيه» | Al-Albani → Daif; Muhammad Muhyi Al-Din Abdul Hamid → Daif; Shuaib Al Arnaut → Daif; Zubair Ali Zai → Daif | n/a (no compiler grade in corpus) | WEAK REPORT |
| 8 | Abu Dawud 4213 | 071 | «آخر عهده بإنسان من أهله فاطمة» | Al-Albani → Daif Isnaad; Muhammad Muhyi Al-Din Abdul Hamid → Daif Isnaad; Shuaib Al Arnaut → Daif; Zubair Ali Zai → Daif | n/a (no compiler grade in corpus) | WEAK REPORT |
| 9 | Tirmidhi 2950 | 223; 224 | «من قال في القرآن بغير علم» | Ahmad Muhammad Shakir → Daif; Al-Albani → Daif; Zubair Ali Zai → Daif | «قال أبو عيسى هذا حديث حسن صحيح» | WEAK REPORT |
| 10 | Tirmidhi 2951 | 223; 224 | «اتقوا الحديث عني إلا ما علمتم» | Ahmad Muhammad Shakir → Daif; Al-Albani → Daif; Zubair Ali Zai → Daif | «قال أبو عيسى هذا حديث حسن» | WEAK REPORT |
| 11 | Tirmidhi 3206 | 144; 274; 187; 189 | «الصلاة يا أهل البيت» | Ahmad Muhammad Shakir → Daif; Al-Albani → Daif; Zubair Ali Zai → Daif | «هذا حديث حسن غريب من هذا الوجه إنما نعرفه من حديث حماد بن سلمة» | WEAK REPORT |
| 12 | Abu Dawud 1641 | 005 | «واشتر بالآخر قدوما» | Al-Albani → Daif; Muhammad Muhyi Al-Din Abdul Hamid → Daif; Shuaib Al Arnaut → Daif; Zubair Ali Zai → Isnaad Hasan | n/a (no compiler grade in corpus) | DISPUTED |
| 13 | Abu Dawud 4784 | 305 | «الغضب من الشيطان» | Al-Albani → Daif; Muhammad Muhyi Al-Din Abdul Hamid → Daif; Shuaib Al Arnaut → Daif; Zubair Ali Zai → Isnaad Hasan | n/a (no compiler grade in corpus) | DISPUTED |
| 14 | Ibn Majah 2198 | 005 | «واشتر بالآخر قدوما» | Al-Albani → Daif; Muhammad Fouad Abd al-Baqi → Daif; Zubair Ali Zai → Isnaad Hasan | n/a (no compiler grade in corpus) | DISPUTED |
| 15 | Tirmidhi 2952 | 225 | «من قال في القرآن برأيه فأصاب فقد أخطأ» | Ahmad Muhammad Shakir → Sahih Isnaad Maqtu; Al-Albani → Daif; Zubair Ali Zai → Daif | «قال أبو عيسى هذا حديث غريب» | DISPUTED |
| 16 | Tirmidhi 3819 | 073 | «أحب أهلي» | Ahmad Muhammad Shakir → Daif; Al-Albani → Daif; Bashar Awad Maarouf → Daif; Zubair Ali Zai → Isnaad Hasan | «هذا حديث حسن صحيح» | DISPUTED |
| 17 | Ibn Majah 116 | 237 | «فهذا ولي من أنا مولاه» | Al-Albani → Sahih; Muhammad Fouad Abd al-Baqi → Sahih; Shuaib Al Arnaut → Sahih Lighairihi; Zubair Ali Zai → Daif | n/a (no compiler grade in corpus) | GRADERS DISAGREE |
| 18 | Tirmidhi 4 | 271 | «مفتاح الجنة الصلاة» | Ahmad Muhammad Shakir → Sahih Lighairihi; Al-Albani → Sahih; Zubair Ali Zai → Daif | none | GRADERS DISAGREE |
| 19 | Tirmidhi 3370 | 016 | «ليس شيء أكرم على الله» | Ahmad Muhammad Shakir → Hasan; Al-Albani → Hasan; Bashar Awad Maarouf → Hasan; Zubair Ali Zai → Daif | «قال أبو عيسى هذا حديث حسن غريب لا نعرفه مرفوعا إلا من حديث عمران القطان وعمران القطان هو ابن داور ويكنى أبا ال» | GRADERS DISAGREE |
| 20 | Tirmidhi 3462 | 022 | «الجنة طيبة التربة» | Ahmad Muhammad Shakir → Hasan; Al-Albani → Hasan; Bashar Awad Maarouf → Hasan; Zubair Ali Zai → Daif | «هذا حديث حسن غريب من هذا الوجه من حديث ابن مسعود» | GRADERS DISAGREE |
| 21 | Tirmidhi 3786 | 011; 043; 157; 206; 242; 258 | «ما إن أخذتم به لن تضلوا» | Ahmad Muhammad Shakir → Sahih; Al-Albani → Sahih; Bashar Awad Maarouf → Hasan; Zubair Ali Zai → Daif | «هذا حديث حسن غريب من هذا الوجه» | GRADERS DISAGREE |
| 22 | Tirmidhi 3788 | 157; 206; 242; 258 | «ولن يتفرقا حتى يردا على الحوض» | Ahmad Muhammad Shakir → Sahih; Al-Albani → Sahih; Zubair Ali Zai → Daif | «هذا حديث حسن غريب» | GRADERS DISAGREE |
| 23 | Tirmidhi 3775 | 010 | «حسين مني وأنا من حسين» | Ahmad Muhammad Shakir → Hasan; Al-Albani → Hasan; Bashar Awad Maarouf → Hasan; Zubair Ali Zai → Hasan | «قال أبو عيسى هذا حديث حسن وإنما نعرفه من حديث عبد الله بن عثمان ابن خثيم وقد رواه غير واحد عن عبد الله بن عثما» | HASAN-PER-GRADERS |
| 24 | Abu Dawud 2356 | 049 | «يفطر على رطبات» | Al-Albani → Hasan Sahih; Muhammad Muhyi Al-Din Abdul Hamid → Hasan Sahih; Shuaib Al Arnaut → Sahih; Zubair Ali Zai → Isnaad Hasan | n/a (no compiler grade in corpus) | SAHIH-PER-GRADERS |
| 25 | Abu Dawud 4646 | 240 | «خلافة النبوة ثلاثون سنة» | Al-Albani → Hasan Sahih; Muhammad Muhyi Al-Din Abdul Hamid → Hasan Sahih; Zubair Ali Zai → Isnaad Hasan | n/a (no compiler grade in corpus) | SAHIH-PER-GRADERS |
| 26 | Abu Dawud 5217 | 068; 252; 262 | «أشبه سمتا وهديا ودلا» | Al-Albani → Sahih; Muhammad Muhyi Al-Din Abdul Hamid → Sahih; Shuaib Al Arnaut → Hasan Sahih; Zubair Ali Zai → Isnaad Hasan | n/a (no compiler grade in corpus) | SAHIH-PER-GRADERS |
| 27 | Ibn Majah 3973 | 004 | «والصدقة تطفئ الخطيئة» | Al-Albani → Sahih; Muhammad Fouad Abd al-Baqi → Sahih; Zubair Ali Zai → Hasan | n/a (no compiler grade in corpus) | SAHIH-PER-GRADERS |
| 28 | Tirmidhi 614 | 004 | «والصدقة تطفئ الخطيئة» | Ahmad Muhammad Shakir → Sahih; Al-Albani → Sahih; Zubair Ali Zai → Isnaad Hasan | «قال أبو عيسى هذا حديث حسن غريب من هذا الوجه لا نعرفه إلا من حديث عبيد الله بن موسى» | SAHIH-PER-GRADERS |
| 29 | Tirmidhi 696 | 049 | «يفطر قبل أن يصلي على رطبات» | Ahmad Muhammad Shakir → Sahih; Al-Albani → Sahih; Bashar Awad Maarouf → Hasan; Zubair Ali Zai → Isnaad Hasan | «قال أبو عيسى هذا حديث حسن غريب» | SAHIH-PER-GRADERS |
| 30 | Tirmidhi 1621 | 094 | «المجاهد من جاهد نفسه» | Ahmad Muhammad Shakir → Sahih; Al-Albani → Sahih; Bashar Awad Maarouf → Hasan Sahih; Zubair Ali Zai → Isnaad Hasan | «قال أبو عيسى وفي الباب عن عقبة بن عامر وجابر» | SAHIH-PER-GRADERS |
| 31 | Tirmidhi 1998 | 087 | «مثقال حبة من خردل من كبر» | Ahmad Muhammad Shakir → Sahih; Al-Albani → Sahih; Bashar Awad Maarouf → Hasan Sahih; Zubair Ali Zai → Sahih - Bukhari And Muslim | «قال أبو عيسى هذا حديث حسن صحيح» | SAHIH-PER-GRADERS |
| 32 | Tirmidhi 2226 | 240 | «الخلافة في أمتي ثلاثون سنة» | Ahmad Muhammad Shakir → Sahih; Al-Albani → Sahih; Bashar Awad Maarouf → Hasan; Zubair Ali Zai → Isnaad Hasan | «قال أبو عيسى وفي الباب عن عمر وعلي قالا لم يعهد النبي صلى الله عليه وسلم في الخلافة شيئا» | SAHIH-PER-GRADERS |
| 33 | Tirmidhi 2616 | 004 | «والصدقة تطفئ الخطيئة» | Ahmad Muhammad Shakir → Sahih; Al-Albani → Sahih; Bashar Awad Maarouf → Hasan Sahih; Zubair Ali Zai → Hasan | «قال أبو عيسى هذا حديث حسن صحيح» | SAHIH-PER-GRADERS |
| 34 | Tirmidhi 3540 | 261 | «عنان السماء» | Ahmad Muhammad Shakir → Sahih; Al-Albani → Sahih; Bashar Awad Maarouf → Hasan; Zubair Ali Zai → Isnaad Hasan | «قال أبو عيسى هذا حديث غريب لا نعرفه إلا من هذا الوجه» | SAHIH-PER-GRADERS |
| 35 | Tirmidhi 3713 | 012; 237 | «من كنت مولاه فعلي مولاه» | Ahmad Muhammad Shakir → Sahih; Al-Albani → Sahih; Zubair Ali Zai → Isnaad Sahih | «قال أبو عيسى هذا حديث حسن غريب» | SAHIH-PER-GRADERS |
| 36 | Tirmidhi 3768 | 012; 085 | «سيدا شباب أهل الجنة» | Ahmad Muhammad Shakir → Sahih; Al-Albani → Sahih; Bashar Awad Maarouf → Hasan Sahih; Zubair Ali Zai → Sahih | «قال أبو عيسى هذا حديث حسن صحيح» | SAHIH-PER-GRADERS |
| 37 | Tirmidhi 3871 | 186 | «فقالت أم سلمة وأنا معهم يا رسول الله» | Ahmad Muhammad Shakir → Sahih; Al-Albani → Sahih; Bashar Awad Maarouf → Hasan Sahih; Zubair Ali Zai → Hasan | «هذا حديث حسن صحيح وهو أحسن شيء روي في هذا الباب» | SAHIH-PER-GRADERS |
| 38 | Tirmidhi 3872 | 068; 252; 262 | «أشبه سمتا ودلا وهديا» | Ahmad Muhammad Shakir → Sahih; Al-Albani → Sahih; Bashar Awad Maarouf → Hasan Sahih; Zubair Ali Zai → Sahih | «قال أبو عيسى هذا حديث حسن صحيح غريب من هذا الوجه وقد روي هذا الحديث من غير وجه عن عائشة» | SAHIH-PER-GRADERS |

The compiler-remark column is quoted from the corpus text field as the control file gives it; some remarks are cut off in the source CSV.

---

## 11 «সূত্র নেই» corrections

Four rows say «সূত্র নেই» / «সূত্রহীন» / «নম্বর ছাড়া» although a six-book source exists (BUG-16; XRM-074/075/076; decisions CSV). All four are confirmed live. Each must quote **the wording of the book it cites**.

| Row | Manuscript (ledger Text) | Source found (live) | Wording caveat |
|---|---|---|---|
| **REF-087** | «অন্তরে সরিষা দানা পরিমাণ অহংকার» — এই শব্দে সূত্র খাতায় নেই | Abu Dawud **4091** «لا يدخل الجنة من كان في قلبه مثقال حبة من خردل من كبر»; Tirmidhi **1998** (graders: Shakir Sahih, Albani Sahih, Bashar Hasan Sahih, Zubair "Sahih - Bukhari And Muslim"); Ibn Majah **59 / 4173**; Muslim **91** (91.01–.03) | **C-18:** Muslim 91 does **not** carry the verbatim phrase. 91.01 / 91.03 read «مثقال ذرة من كبر»; 91.02 reads «مثقال حبة خردل من كبرياء». If «মুসলিম ৯১» is printed, quote its own wording; for the verbatim «مثقال حبة من خردل من كبر», cite Abu Dawud 4091 / Tirmidhi 1998 / Ibn Majah 59. The six-book table's ✅ for Muslim 91 is superseded (D-1) |
| **REF-105** | ইবনে আব্বাস: «আল কাওসার কী?» — খাতায় সূত্রহীন | Bukhari **4966** (also 6578): «عن ابن عباس … أنه قال في الكوثر هو الخير الذي أعطاه الله إياه» | This is Ibn Abbas's own statement, not a saying of the Prophet |
| **REF-004** | «সাদাকাহ গুনাহ নিভিয়ে দেয়, যেমন পানি আগুন» — তিরমিযিতে বর্ণিত বলে প্রচলিত; নম্বর ছাড়া | Tirmidhi **614** (Ka'b b. Ujra) and **2616** (Mu'adh); Ibn Majah **3973** | 614: Shakir Sahih, Albani Sahih, Zubair Isnaad Hasan; 2616: Shakir/Albani Sahih, Bashar Hasan Sahih, Zubair Hasan; 3973: Albani Sahih, Abd al-Baqi Sahih, Zubair Hasan. Print a number only after page lock |
| **REF-096** | চাদরের হাদীস (জাবির…) — দীর্ঘ পাঠের শব্দে মেলানো হয়নি; সংক্ষিপ্ত চাদর-রেওয়ায়েত সহীহ মুসলিমে | Muslim **2424** (Aisha, «مرط مرحل»; short version) | **Short version only.** The long Jabir text is not in the six books and stays on its Shia source line, never under Muslim. Umm Salama's report is Tirmidhi 3871 («إنك على خير»); «أنت على مكانك» is Tirmidhi 3205 / 3787 (C-05) |

**Partial finds in UNID rows (author must confirm identity; FLAG-FOR-AUTHOR-DECISION).**

| Row | Manuscript | Six-book text found | Why only partial |
|---|---|---|---|
| **REF-014** | চিট লিস্টের বাণীগুলো (চিন্তাহীন ইবাদত, জ্ঞানার্জন-শিক্ষাদান, চার ব্যক্তির পুরস্কার) — শ্রোতা ০৪-এ সূত্র ছাড়া | Tirmidhi **2325**: «إنما الدنيا لأربعة نفر عبد رزقه الله مالا وعلما فهو يتقي فيه ربه…» (Shakir / Albani Sahih; Zubair Ali Zai Daif) | Covers only the «চার ব্যক্তির পুরস্কার» item; identity with the manuscript wording is unconfirmed because the DOCX is unavailable; the other two sayings are NOT VERIFIED |
| **REF-159** | হুজরাত ১–১০ ও প্রথম দুই খলিফা — শ্রোতা ০৪ (আব্বুর মুখে) | Bukhari **4845** (also 7302; Tirmidhi 3266): «كاد الخيران أن يهلكا أبا بكر وعمر … فأنزل الله {يا أيها الذين آمنوا لا ترفعوا أصواتكم}» | The narration exists; its identity with the oral exegesis is unconfirmed |

**The second wording caveat: Abu Dawud 5023 (C-01).** This applies to REF-013 and REF-201 (HAD-RUYA), which are not «সূত্র নেই» rows but carry an audit-proposed source.
- 5023 reads «من رآني في المنام **فسيراني في اليقظة** … ولا يتمثل الشيطان بي».
- The manuscript's «সত্যিই আমাকে দেখল» = «فقد رآني» is Bukhari **110** / Muslim **2266.01** (also Tirmidhi 2276 and Ibn Majah 3900–3905, per the Sunni evidence).
- Cite 5023 only for «فسيراني في اليقظة», and 5019 for «الرؤيا ثلاث». 5021 is the wrong hadith.

---

## 12 Internal S-ID audit

**S-173 split.** S-173 is overloaded: a Ramadan date, Thaqalayn and Mawla. The only ledger row that prints it is REF-157, «মুসলিম ২৪০৮ … তিরমিযি ৩৭৮৬ … ৩৭৮৮ — CONFIRMED (S-173)».
- Split into:
  - `DATE-2014-RAMADAN`: a factual date, not a hadith. **No ledger row identified**; manuscript location PAGE-CHECK.
  - `HAD-THAQALAYN`: REF-043, 157, 206, 242, 258 (Muslim 2408; Tirmidhi 3786; Tirmidhi 3788). Grades differ.
  - `HAD-MAWLA`: REF-012, 233 (prose), 237 (Tirmidhi 3713).
- Retire S-173. After the split no row may print «S-173».

**S-174 lock.** The claim that Satan cannot take the Prophet's ﷺ form (v1.0 BUG-08). **The verification lock stays OPEN.** The wording «الشيطان لا يتمثل بي / في صورتي» is in Bukhari 110, Bukhari 6993, Muslim 2266 (.01, .02) and Abu Dawud 5023 in the local corpus. The author must choose one source and edition.

**Non-proof IDs.** S-80 (narrative: dream evidence), S-111 (authorial: 36:58 interpretation), S-114 (authorial: «light upon light» imagery; not to be merged with REF-042's al-Kafi line), S-122 (authorial: salawat reflection), S-148 and S-149 (teacher: spiritual experience), and S-183 (notebook prose) are classified **NON-EXTERNAL-PROOF**. None may sit in a hadith source block. All have 0 hits in the ledger `Text`, so their manuscript locations are PAGE-CHECK.

**S-181** stays a library-file ID. Strip the «— S-181 §…» pointers from the reader-facing patch block and replace them with the per-recension source lines once editions are locked.

**Local path, REF-101 (BUG-07 / BUG-27).**
- Currently cited: `F:\HZ Fatima Zahra SA Nobuwat & Imamat Bondhon\__REWRITTEN\Tafseer e Hubbe Ali en to Bn\hubbe_ali_ch108_আল-কাউসার_bangla.md ল. ২৪৬–২৪৯`.
- Proposed stable ID: `SRC-TAFSIR-HUBBE-ALI-108` (Surat al-Kawthar h. 10 = Ibn Babawayh; h. 11 = al-Ihtijaj).
- Library file ID: basename only. URL: hubbeali.com h. 9499 (full URL ⟦…⟧). Edition ⟦publisher, year⟧.
- A Bengali rewrite of a tafsir is a secondary stand-in.

**Secondary stand-ins → primaries** (replacement form = stable source ID + library file ID + URL + edition record):

| Row(s) | Currently | Primary / proposed ID |
|---|---|---|
| REF-294 | «Fatima Zahra in the Words of the Infallibles» | Bihar 43:76 (from Manaqib 3:341) and 43:172 (from Amali al-Saduq), `HAD-FATIMA-IBADA` |
| REF-296 | «খাতায় al-islam.org» | `SRC-MISBAH-AL-MUTAHAJJID` (al-Tusi, ~p. 300; Ibn Tawus, Jamal al-Usbu'), PAGE-CHECK |
| REF-297 | Mizan al-Hikma ch. 261 p. 676 (whole chapter) | one primary per underlying hadith; Mizan only as a finding aid |
| REF-299 | «দাসত্ব পাঁচটি জিনিস» via Mizan al-Hikma | Misbah al-Shari'a (attributed) → attribution-only «বর্ণিত আছে» |
| REF-279 | Mishkat / Tajrid al-Bukhari | `HAD-BASRA-SALAT` → Bukhari 784 (Basra) |
| REF-039 | hadithprophet.com URL | Bukhari 7171 / Muslim 2175 |
| REF-037, 040 / 038 / 029, 031 | forum, wiki and article URLs | al-Kafi 1:183-184 h. 8; Nahj khutba 1; Ghurar no. 4641; Tahdhib 2:289 h. 1157; Mustadrak |
| REF-019, 070, 127, 144, 210 | api.alquran.cloud | verse reference + stated Quran edition |
| REF-030, 034, 035, 042, 056 | thaqalayn.net / quran.ksu URLs | the book citations (al-Kafi, al-Tabari); URLs not re-checkable here |
| REF-137 / 033, 177 / 077 | Persian secondary; Yanabi' al-Mawadda; list including modern Bengali / Urdu authors | al-Durr al-Manthur 4:177; per-report primaries; one ID per work |

**CL-HAD-008 split (C-23).** CL-HAD-008 names two different hadiths:
- REF-250, Bukhari 3714 «ফাতিমা আমার অংশ» (six-book, verified) → map to `HAD-BIDAA-MINNI`.
- REF-251, al-Hakim 4730 «আল্লাহ তোমার ক্রোধে ক্রোধান্বিত হন» (Hakim only, number unlocked) → needs its own key; it has none in v1.3.
- Retire CL-HAD-008. CL-HAD-001/002 → HAD-THAQALAYN; CL-HAD-003 → HAD-MAWLA; CL-HAD-005/006 → HAD-EID-KHUTBA-BAD-SALAT. Delete «দেখুন SOURCE_REGISTER.md (CL-HAD-…)» from reader text, because that file is not in the repo.

**Other internal tokens to strip from reader text:**
- D-017 (REF-188)
- CITATION_RISK / SECOND_NOTEBOOK (REF-126, 131, 188)
- JONY-VERBATIM (REF-055 → al-Kafi 8, al-Rawda, h. 21)
- «খাতা…» in 93 source-note rows. The narrative notebook in REF-211, 306, 311, 314, 325 stays.
- «শ্রোতা ০৪» (REF-013, 014, 015, 016, 020, 077, 096, 158, 159)
- «লগ B3/B5» (REF-217, 219, 226, 231)
- «বাইবেল §৪» (REF-072, 079)
- STYLE §৪ (REF-142, 156)
- REV1 (REF-210, 224, 228, 260)
- outline lists (REF-240, 065, 204, 053)
- tool names (REF-043, 044, 053, 075)
- «Claude-এর অর্থানুবাদ» (REF-126). AI output is not evidence.
- the audit note in REF-145.

---

## 13 The 12 citation corrections (audit v1.1 §3, updated by C-01…C-28)

| REF | Manuscript / ledger says | Correct (v1.1) | Update in v1.2 |
|---|---|---|---|
| 009 | Ibn Majah (incl. China clause) | Ibn Majah 224 first clause only (very da'if); China clause unsupported | Confirmed. «الصين» is absent from 224. All four printed graders weaken 224 itself (Albani, Abd al-Baqi, Arnaut: Very Daif; Zubair: Daif), so a ledger wording that calls only the China clause weak understates the grade |
| 011 | Musnad Ahmad 3786 | Hakim 3312 / 4720; Tabarani | Confirmed: the Ark hadith is absent from the six books. Hakim / Tabarani are CANDIDATE (not verifiable here). Tirmidhi 3786 = Thaqalayn (number collision, XRM-012) |
| 013 | Abu Dawud 5021 | Abu Dawud 5019 + 5023 | **Corrected (C-01):** 5019 for «الرؤيا ثلاث»; «فقد رآني» = Bukhari 110 / Muslim 2266.01; 5023 only for «فسيراني في اليقظة» |
| 022 | Sahih Muslim | not in Muslim — drop | Confirmed. Muslim 1015 «إن الله طيب لا يقبل إلا طيبا» and Tirmidhi 3462 «الجنة طيبة التربة» are different texts |
| 087 | no source | Muslim 91 | **Refined (C-18):** verbatim wording = Abu Dawud 4091, Tirmidhi 1998, Ibn Majah 59 / 4173; Muslim 91 has «ذرة من كبر» / «حبة خردل من كبرياء» |
| 101 | F:\ local path | Hubb-e Ali h. 10-11 | Confirmed. Proposed `SRC-TAFSIR-HUBBE-ALI-108`; strip the folder path (§12) |
| 105 | no source | Bukhari 4966 | Confirmed (also 6578); it is Ibn Abbas's own statement |
| 131 | 4240 lacks night burial | 4240 has night burial + not informing Abu Bakr; only the concealment wasiyya is absent | Confirmed, re-checked after the tool fix. 4240 also has no washing / shrouding |
| 145 | audit note in source block | move to ledger | Confirmed |
| 279 | Kufa | **Basra** (Bukhari 784, 786) | **Refined (C-17):** only **784** contains «بالبصرة»; 786 (Mutarrif) names no place and is cited only for the takbir detail. The Kufa prose is REF-276; the speaker is Imran b. Husayn, not «সাহাবারা» (XRM-001) |
| 280 | Hakim: «علي مع الحق» | Hakim / Tirmidhi 3714: «أدر الحق معه»; «علي مع الحق» → Khatib 14:321 | Confirmed. Tirmidhi 3714 graded Very Daif (Shakir, Albani), Daif (Zubair); «علي مع الحق» has 0 hits in the six books |
| 309 | Tirmidhi: «مدينة العلم» | Tirmidhi 3723 «دار الحكمة»; «مدينة العلم» → Hakim | **Refined (C-10, C-22):** print Tirmidhi's own remark «هذا حديث غريب منكر» with the graders' Daif; HAD-MADINAT-ILM covers 6 rows including prose REF-308 |

Corrections C-01…C-28 that touch rows outside the 12 MM rows are listed in §15.

---

## 14 BUG-11 … BUG-30 (status after v1.2)

| BUG | One line | Status |
|---|---|---|
| BUG-11 | Basra, not Kufa (REF-276, 279) | **refined.** Only Bukhari 784 names Basra; 786 names no place (C-17) |
| BUG-12 | Bengali-edition numbers used as standard (REF-049, 075, 107, 126) | **corrected.** «جويرية» passage = Bukhari 520, not 3110 (C-02); Muslim 6062 does not exist in Abd al-Baqi numbering, standard = 2404 (C-28); the REF-075 Bengali numbers cannot be mapped without the author's edition (PAGE-CHECK) |
| BUG-13 | Abu Dawud 5021 is the wrong hadith (REF-013) | **corrected.** 5021 is wrong (confirmed), but 5023 reads «فسيراني في اليقظة»; «فقد رآني» = Bukhari 110 / Muslim 2266.01 (C-01) |
| BUG-14 | «Musnad Ahmad 3786» for the Ark hadith | **confirmed.** Absent from the six books; Hakim / Tabarani CANDIDATE |
| BUG-15 | «الجنة طيبة لا يدخلها إلا الطيب» not in Muslim | **confirmed** |
| BUG-16 | "No source" claims that have a source (087, 105, 004, 096) | **refined.** All four confirmed live; 087 wording per C-18; 096 short version only; 105 is Ibn Abbas's own statement |
| BUG-17 | v1.0 over-corrected Bukhari 4240 | **confirmed.** Re-checked after the tool fix; no will and no «قبر» in 4240 |
| BUG-18 | «مدينة العلم» attributed to Tirmidhi | **refined.** Tirmidhi's own remark «غريب منكر» (C-10); 6 rows, not 5 (C-22) |
| BUG-19 | «علي مع الحق» ≠ al-Hakim / Tirmidhi 3714 wording | **confirmed** (3714 Very Daif / Daif) |
| BUG-20 | "China" clause of the knowledge hadith | **confirmed.** 224 itself is weak per all four printed graders |
| BUG-21 | Every al-Hakim citation needs a hadith number | **confirmed.** Still not verifiable here (Hakim is outside the six books) |
| BUG-22 | Weak / munkar reports printed without grade | **refined.** Grades now as printed in the grading control (§10); 2950 vs 2951 split (C-04); Tirmidhi 3819, Abu Dawud 4784 and Tirmidhi 2952 are DISPUTED, not plain da'if; 3868/3874 Tirmidhi «حسن غريب» vs Munkar; 2972's grade belongs to the graders, not to Abu Dawud |
| BUG-23 | Fadak as Khadija's mahr (REF-125) | **refined.** NO_SOURCE_LOCATED («مهر خديجة», «صداق خديجة»: 0 hits). Per the Global Law it is not removed merely for lacking a source → FLAG-FOR-AUTHOR-DECISION |
| BUG-24 | Iqbal line «مادی» → «مادر» (REF-074) | **confirmed.** Patch block exists; edition page still needed |
| BUG-25 | 30 rows with no locatable classical source | **refined.** v1.3 UNID set has REF-041 instead of 007; 40 rows decided (§16); 2 UNID rows have partial six-book finds (014, 159) |
| BUG-26 | One hadith, many statuses (register) | **refined.** Register v1.1 = 95 keys over 196 rows, 41 keys with a status conflict. C-09 («عترتي» not in Muslim) and C-05 (Kisa numbers) change the HAD-THAQALAYN / HAD-KISA locks; HAD-RUYA still shows the old 5023 wording (D-7); splits recommended for HAD-FADAK-TESTIMONY and others |
| BUG-27 | Local path as citation (REF-101) | **confirmed.** Replacement form proposed (§12) |
| BUG-28 | Audit language inside a source block (REF-145) | **confirmed** |
| BUG-29 | Secondary sources standing in for primaries | **confirmed.** The S-ID audit adds more stand-ins (URL-only pointers, Yanabi', Persian secondary, modern authors) (§12) |
| BUG-30 | Muslim 2175 wording | **corrected.** Muslim 2175.01 has «يجري … مجرى الدم» and 2175.02 has «يبلغ … مبلغ الدم» («ولم يقل يجري»); Bukhari 2035 has «يبلغ» (C-08) |

---

## 15 New bugs discovered (BUG-31 onward)

### 15.1 New defects

| BUG | Rows | Defect | Source | Required action |
|---|---|---|---|---|
| **BUG-31** | ~28 VL rows; REF-317 | `verify_sunni.py show muslim N` fell back to sequential numbering and printed the wrong hadith; Muslim 2989 was left at PAGE-CHECK | C-14, C-13; XRM-025/026 | Fixed and all Muslim numbers re-run (no verdict changed). Rebuild the six-book `.md` table from the fixed run |
| **BUG-32** | REF-293 | The first two Muslim 2816 sub-reports are unnumbered in the corpus, so `show muslim 2816` is incomplete; also Muslim 2818 reads «لن يدخل الجنة», not the «নাজাত» wording (XRM-087), yet v1.3 says "Numbers correct" | C-21; XRM-087 | Use `search`; re-decide which Muslim number carries «لن ينجي» |
| **BUG-33** | REF-016 | «الدعاء هو العبادة» pointer = Tirmidhi 3370, which is Abu Hurayra «ليس شيء أكرم على الله» | C-03, C-26; XRM-085 | Cite Tirmidhi 2969 / 3247 / **3372**, Abu Dawud 1479, Ibn Majah 3828 |
| **BUG-34** | REF-224 (vs 223) | REF-224 marked DUPLICATE of Tirmidhi 2951, but «بغير علم» = **2950**; 2951 = «اتقوا الحديث عني» | C-04; XRM-027 | Two numbers, two wordings; both Daif per Shakir, Albani, Zubair |
| **BUG-35** | REF-186 | «أنت على مكانك وأنت على خير» cited to Tirmidhi 3871; 3871 reads «إنك على خير» | C-05, C-20 | 3205 / 3787 for the phrase; 3871 for the cloak (Umm Salama) |
| **BUG-36** | REF-054 | Manuscript «نعمت البدعة هذه»; corpus Bukhari 2010 «نعم البدعة هذه» | C-06; XRM-086 | Spelling per the cited edition (EDITION-DEPENDENT) |
| **BUG-37** | REF-157 (+043, 206, 242, 258) | «কিতাবুল্লাহ ও আমার ইতরাত» marked CONFIRMED under Muslim 2408; «عترتي» does not occur anywhere in Muslim | C-09; XRM-009 | «عترتي» rests on Tirmidhi 3786/3788 only (graders disagree); Muslim 2408 only for «أهل بيتي» |
| **BUG-38** | REF-079 (+078, 121, 136) | Abu Dawud 2972 printed as support / CONFIRMED (S-181 patch) for Umar b. Abd al-Aziz's restoration; its text says the Prophet declined Fatima's request («فأبى»); Daif ×3 | C-11; XRM-005/006 | Cite as a contrary report with its content and grade |
| **BUG-39** | REF-123 | «আমরা নবীগণ উত্তরাধিকার রেখে যাই না» (= «معاشر الأنبياء») on Bukhari / Muslim numbers; the six books have «لا نورث ما تركنا صدقة» | C-12; XRM-062 | Separate the Sunni wording from the al-Ihtijaj (Shia) wording |
| **BUG-40** | REF-144, 187, 189, 267, 269, 274 | **6-month vs 9-month.** Tirmidhi 3206 (Anas: **six** months, fajr only, da'if) cited for the chapter «নয় মাস ধরে…» | C-15; XRM-039/040 | The nine-month claim needs Shawahid al-Tanzil / Tabarani (CANDIDATE), cited separately and never merged |
| **BUG-41** | REF-081, 123, 078 | Malik b. Aws b. al-Hadathan (Sunni narrator, Bukhari 3094, Muslim 1757) risks being conflated with Aus ibn al-Hadathan (Shia counter-witness) | C-16; XRM-092 | Never conflate (§8) |
| **BUG-42** | REF-313 | «إذا التقى المسلمان بسيفيهما» cited to Bukhari 7083 / Muslim 2888; 7083 and 2888.01 read «تواجه» | C-19 | Quote the sub-report cited («التقى» = Bukhari 31, 6875, Muslim 2888.02) |
| **BUG-43** | REF-134, 158 | «حسبنا كتاب الله» cited at Bukhari 4431; the phrase is in 114, 4432, 5669, 7366 and Muslim 1637.03, not 4431 / 3053 / 1637.01; ledger v1.3 REF-158 still prints «১১৪, ৪৪৩১» | C-25 | 114 or 4432 for the phrase; 4431 only for the Thursday scene |
| **BUG-44** | REF-250, 251 | **CL-HAD-008 overload:** one register ID for Bukhari 3714 and Hakim 4730 | C-23; S-ID audit | Split; 251 gets its own key |
| **BUG-45** | REF-158 (vs candidate) | **Ahmad 3/364 vs 3/346** page conflict inside the ledger (also Bihar 22/469 vs 22:468-469) | C-24; XRM-068 | Lock from the Musnad edition |
| **BUG-46** | REF-078 | **Prophet-vs-Abu-Bakr deed:** the prose has the Prophet write the Fadak deed; al-Ihtijaj has Abu Bakr write it (Umar tears it); the ledger resolution equates them | F-1; Fadak map C08-X01; patch plan §2 | Author decides: «বর্ণিত আছে» with no al-Ihtijaj citation, or the Ihtijaj recension with «শিয়া সূত্রে» |
| **BUG-47** | S-181 patch A-1, B•1 | **«হাদী» ambiguity:** meant for حاضنة (nurse); reads as هادي (guide), the word used for Ali in REF-179 | F-5; patch plan §2 amendment | «লালনকারিণী / ধাত্রী (حاضنة)». Author's choice |
| **BUG-48** | REF-078, 081, 122, 141 | Register HAD-FADAK-TESTIMONY covers four units, including **Umm Hani** (REF-141, a different woman) | F-7; XRM-004 | Split into sub-keys |
| **BUG-49** | REF-188 | Muslim 2424 CONFIRMED for a kisa «through Umm Salama and Aisha»; 2424 is Aisha only, and Umm Salama is Tirmidhi 3871 | XRM-038; patch plan §2 | Cite each narrator's book |
| **BUG-50** | REF-142, 153 | «يسرني ما يسرها / يبسطني» (the «যে তাকে খুশি করে» clause) absent from the six books but mapped to Muslim 2449 («يؤذيني ما آذاها») / Bukhari 5230 | XRM-018; Sunni evidence §6; patch plan §2 | Do not map the positive clause to the six books |
| **BUG-51** | REF-076, 142, 250 | «যে তাকে কষ্ট দেয়» (hurt) attached to Bukhari 3714, whose verb is anger («أغضبها») | XRM-017 | Quote 3714's wording; «يؤذيني ما آذاها» = Muslim 2449 |
| **BUG-52** | REF-122 | Baladhuri bullet next to the deed-tearing; Suyuti, Tarikh al-Khulafa, for the tearing not located | F-6; XRM-003 | Split; drop Suyuti unless a page is found |
| **BUG-53** | Patch B•1, HAD-UMM-ABIHA, REF-150 | Edition mixing: al-Isaba 4/415–416 vs 8:262; al-Isti'ab 12 / 876–877 vs 4:1899; Ibn Sa'd 8 / 224 vs 10 vs 8:24 | F-8 | One edition per work |
| **BUG-54** | Patch B•3 | Kitab Sulaym cited for Ali's testimony; no Sulaym text for it is quoted in the repo | F-9; Fadak map C03-H04 | PAGE-CHECK first |
| **BUG-55** | Patch A-2(খ), B•1 | Speaker of «إن أم أيمن امرأة من أهل الجنة» unidentified; «أم أيمن أمي بعد أمي» printed with no grade | F-3, F-10 | No flat «রাসূল ﷺ বলেছেন» |
| **BUG-56** | REF-174/c | Tafsir al-Ayyashi cited for Q 67:22; the control notes (knowledge-based) that the extant Ayyashi is reported to stop at Surat al-Kahf | Shia control | Confirm existence or drop Ayyashi for 67:22 |
| **BUG-57** | REF-083 (+037, 059) | VERIFIED-LIVE triage on Muslim 1851 («من مات وليس في عنقه بيعة»), which does not carry the manuscript's «ইমাম» claim («إمام» absent) | XRM-024; XRM summary | Keep the Shia wording (Kafi) and the Muslim bay'a wording apart |
| **BUG-58** | REF-237, 233 | Ibn Majah 116 is the Ghadir report **without** «بخ بخ»; the congratulation is in no six-book hadith; the prose voices it as «সাহাবিরা» | Sunni evidence (NOT_FOUND); XRM-036 | Ahmad number stays PAGE-CHECK; single-speaker wording |
| **BUG-59** | REF-099 | Muslim 2369 «يا خير البرية — ذاك إبراهيم» is a different hadith from «خير البرية = Ali» (98:7) | Sunni evidence (WRONG_SUBJECT); six-book check B | Do not cite Muslim 2369 for this claim |
| **BUG-60** | REF-126 (+072, 076, 142, 157, 188, 206, 237, 242, 258) | «CONFIRMED» printed on rows whose basis is internal documents or an AI paraphrase («Claude-এর অর্থানুবাদ»); «বাইবেল §৪», STYLE, REV1 and tool names in source notes | XRM-078; S-ID audit §4 | Withdraw «CONFIRMED» until edition lock; strip the tokens; AI output is not evidence |
| **BUG-61** | REF-240 (+143, 152) | «আমার পর বারো জন খলিফা» quoted from texts that say neither «after me» nor (Bukhari) «khalifa» | XRM-033; register HAD-12-KHALIFA | Bukhari 7222 «اثنا عشر أميرا» and Muslim 1821 «اثنا عشر خليفة», each under its own number |

The remaining XRM rows (e.g. XRM-022 Tasbih order, XRM-042/043 «লেজকাটা দরুদ», XRM-060 six months vs «40 days to 8 months», XRM-066 munkar grades, XRM-073 «تتورم قدماها») are recorded in the cross-row CSV and handled through §5 and the patch plan. They are not renumbered here.

### 15.2 Corrections that refine earlier bugs (not new defects)

| C-xx | Refines | Note |
|---|---|---|
| C-01 | BUG-13, HAD-RUYA | 5023 wording |
| C-02, C-28 | BUG-12 | 520 not 3110; no AB 6062 |
| C-07 | v1.0 **BUG-05** | Bukhari 3767 = «فاطمة بضعة مني» (Miswar); «سيدة نساء» is 3624 (XRM-019) |
| C-08 | BUG-30 | Muslim 2175 has both wordings |
| C-10 | BUG-18, BUG-22 | Tirmidhi 3723 compiler remark «غريب منكر» |
| C-13 | XRM-026 | Muslim 2989.02 = mill-donkey report ✅ |
| C-17 | BUG-11 | 786 names no place |
| C-18 | BUG-16 | Muslim 91 wording |
| C-22 | BUG-18, BUG-26 | HAD-MADINAT-ILM = 6 rows |
| C-27 | six-book table §B | «مقاريض» occurs (Muslim 273.02, Tirmidhi 2402, Ibn Majah 346, Nasa'i 30) but never as the Mi'raj lips-scissors report; REF-318 still → Ahmad |

The other C-items (C-03/26, 04, 05/20, 06, 09, 11, 12, 14, 15, 16, 19, 21, 23, 24, 25) are new defects: BUG-31…45 above.

---

## 16 30 unidentified-reference decisions

The decisions CSV covers **40 rows**: the 30 UNID rows plus REF-007 (listed in BUG-25 but triaged CAND), five «সূত্র নেই» rows (087, 103, 104, 105, 273), two known cases (004, 096) and two extended-sweep rows (134, 202). 153 Arabic search terms were run (2–6 per row).

**Classification × recommended handling (40 rows):**

| Classification | n (40) | of which UNID (30) | Recommended handling (counts across 40) | Rows |
|---|---|---|---|---|
| CANONICAL_SOURCE_FOUND | 6 | 2 | ADD-SOURCE 4 (004, 087, 096, 105); FLAG-FOR-AUTHOR-DECISION 2 (014\*, 159\*) | 004, 014\*, 087, 096†, 105, 159\* |
| PLAUSIBLE_SOURCE_ONLY | 16 | 13 | KEEP-ATTRIBUTION-ONLY «বর্ণিত আছে» 14; FLAG-FOR-AUTHOR-DECISION 2 (090, 209) | 041, 090, 091, 097, 103, 104, 115, 175, 196, 202, 209, 215, 219, 228, 244, 272 |
| SECONDARY_SOURCE_ONLY | 3 | 3 | KEEP-«বলা হয়» 3 | 265, 266, 321 |
| NO_SOURCE_LOCATED | 15 | 12 | KEEP-ATTRIBUTION-ONLY «বর্ণিত আছে» 10; FLAG-FOR-AUTHOR-DECISION 4 (100, 125, 140, 199); KEEP-«বলা হয়» 1 (134) | 002, 006, 007, 020, 084, 100, 125, 134, 140, 199, 239, 248, 273, 292, 295 |
| **Total** | **40** | **30** | KEEP-ATTRIBUTION-ONLY 24 · FLAG 8 · KEEP-«বলা হয়» 4 · ADD-SOURCE 4 · REMOVE-KITAB-NAME 0 | |

\* partial match (§11). † short kisa report only.

For the 30 UNID rows, v1.3 `Final_Status` shows:

| Final_Status | Rows |
|---|---|
| PLAUSIBLE_SOURCE_ONLY — KEEP-ATTRIBUTION-ONLY «বর্ণিত আছে» | 11 |
| NO_SOURCE_LOCATED — KEEP-ATTRIBUTION-ONLY «বর্ণিত আছে» | 8 |
| NO_SOURCE_LOCATED — FLAG-FOR-AUTHOR-DECISION | 4 |
| SECONDARY_SOURCE_ONLY — KEEP-«বলা হয়» | 3 |
| CANONICAL_SOURCE_FOUND — FLAG-FOR-AUTHOR-DECISION | 2 |
| PLAUSIBLE_SOURCE_ONLY — FLAG-FOR-AUTHOR-DECISION | 2 |

**Handling per class:**
- **CANONICAL_SOURCE_FOUND:** print the six-book citation in the cited book's wording, after edition lock (ADD-SOURCE). For partial matches the author confirms identity first.
- **PLAUSIBLE_SOURCE_ONLY:** the candidate work is named from research knowledge only and is NOT VERIFIED. Print attribution-only «বর্ণিত আছে» with **no kitab name** until a page is locked. The candidate Arabic for REF-091, 104, 175, 196, 202, 215 and 219 is "from memory — not verified". REF-215 and REF-219 may be one narration; the author is to confirm.
- **SECONDARY_SOURCE_ONLY:** only later compilations or popular usage are known. Print «বলা হয়».
- **NO_SOURCE_LOCATED:** NOT FOUND in the six books, which does not mean it does not exist; SOURCE-MISSING. Print attribution-only «বর্ণিত আছে» / «বলা হয়». Per the Global Law, no historical claim is recommended for removal.
- **Near matches that must NOT be substituted:**

| Row | Near match | Why not |
|---|---|---|
| 002 | Bukhari 6472 | different subject |
| 041 | Abu Dawud 4700 / Tirmidhi 2155, 3319 | about the pen, not the light |
| 090 | Abu Dawud 4681 | four acts, not three |
| 091 | Tirmidhi 2398 | different saying |
| 097 | Tirmidhi 2449 / Abu Dawud 1682 | Daif; no mention of Tasnim |
| 209 | Tirmidhi 3789 | Daif; says «أهل بيتي», not «ولي» |
| 228 | Tirmidhi 3723 | «غريب منكر»; Ali, not Jabir |
| 248 | Muslim 2813 | different report |
| 265 | Bukhari 405 | different statement |
| 295 | Abu Dawud 1522 | said to Mu'adh, not Fatima |

**The 8 rows flagged for the author:**

| Row | Part | Claim (short) | Why flagged |
|---|---|---|---|
| REF-014 | 1 | চিট-লিস্টের বাণী: চিন্তাহীন ইবাদত; জ্ঞানার্জন-শিক্ষাদান; চার ব্যক্তির পুরস্কার | Tirmidhi 2325 matches only the «চার ব্যক্তি» item (graders split: Shakir/Albani Sahih, Zubair Daif); identity unconfirmed |
| REF-090 | 4 | চারটি বাণী («তিনটি গুণ… ঈমান পূর্ণ» …) | no exact six-book hit; related Abu Dawud 4681 (four acts) and Bukhari 16 / Muslim 43 (sweetness) are different |
| REF-100 | 5 | «সর্বপ্রথম জান্নাতে… আশেকরা পশ্চাতে» (খাতায় আরবি আছে) | «العاشق», «عشق»: 0 hits; the author must supply the notebook Arabic |
| REF-125 | 6 | ফাদাক সাইয়্যেদা খাদিজা (আ.)-এর মোহরানা | «مهر خديجة», «صداق خديجة»: 0 hits; «فدك» hits are the inheritance reports; not removed merely for lacking a source |
| REF-140 | 6 | আবান ইবনে তাগলিবের দুটি বর্ণনা (খাতায় কিতাবের নাম নেই) | Aban appears only as a transmitter in six-book isnads; the author must supply the text |
| REF-159 | 7 | সূরা হুজরাত ১–১০ ও প্রথম দুই খলিফা | Bukhari 4845 / 7302, Tirmidhi 3266 exist; identity with the oral exegesis unconfirmed |
| REF-199 | 8 | কুরাইশদের ভুলের কারণ «একই নূর» — খাতায় বিহারুল আনওয়ার ৫ম খণ্ড | 0 hits for «نور واحد» etc.; do not print «Bihar vol. 5» until checked; the author decides on the kitab name |
| REF-209 | 9 | «আমাকে ভালোবাসো, তার আগে আমার রাসূলকে… ওলিকে» | nearest Tirmidhi 3789 («أحبوا الله … وأحبوا أهل بيتي لحبي») differs in speaker and terms; must not be silently substituted |

---

## 17 Manuscript patch queue

From `manuscript-patches/B1_P01-11_MANUSCRIPT_PATCH_PLAN_v1.0.md` (header and §1). The DOCX was **not** modified; every CURRENT_TEXT is quoted from the ledger. Blocks are ordered by Part → Chapter → Paragraph_Index.

- Ledger rows: **328**. Patch blocks: **105**. NO_CHANGE rows: **223** (105 + 223 = 328, re-verified for this report: no gaps, no duplicates).
- Blocks by ledger triage: MM 12 · EDN 4 · S181 5 · DUP 13 · UNID 30 · VL 32 · PROSE 3 · CAND 5 · HIST 1.

| PATCH_TYPE | Primary (blocks) | Component occurrences |
|---|---|---|
| PRESERVE_WITH_PAGE_CHECK | 33 | 33 |
| CORRECT_HADITH_NUMBER | 23 | 23 |
| CORRECT_CITATION | 21 | 21 |
| ADD_SOURCE | 8 | 10 |
| SPLIT_CLAIM | 8 | 8 |
| WEAKEN_ATTRIBUTION | 5 | 6 |
| CORRECT_SOURCE | 3 | 3 |
| CORRECT_LOCATION | 2 | 2 |
| REMOVE_FALSE_SOURCE | 2 | 2 |
| **Total** | **105** | **108** |
| NO_CHANGE | 223 lines | — |

| CONFIDENCE | Blocks |
|---|---|
| HIGH (live evidence: corpus output or S-181 with URLs) | 53 |
| MEDIUM (knowledge-based candidate) | 20 |
| LOW | 32 |

| REQUIRES_HUMAN_REVIEW | Blocks |
|---|---|
| YES (every theological / historical wording change, every REMOVE_*, every disputed or munkar narration, every non-live item) | 79 |
| NO (pure number or grade fixes backed by live evidence on which graders agree) | 26 |

The CONFIDENCE and REQUIRES_HUMAN_REVIEW counts were re-counted from the block fields and match the header.

An unnumbered amendment to the existing S-181 patch, replacing «হাদী» with «লালনকারিণী / ধাত্রী (حاضنة)» (CORRECT_CITATION · HIGH · review YES), sits in plan §2.

**Not yet reflected in the plan:** the plan was built from ledger v1.2 and the v1.1 corrections. Before applying, check its REF-013, 087, 158, 186, 224, 313 and 123 blocks against C-01, C-18, C-25, C-05, C-04, C-19 and C-12. The plan's §2 already records C-01, C-02, C-04, C-08 and C-12-type findings for REF-075, 013, 224, 039 and 123. Whether each later C-item made it into the block text was not checked line by line for this report.

---

## 18 PRINT BLOCKED rationale

`BOOK 1 · PARTS 1–11 — CITATION AUDIT: PRINT BLOCKED` stands, for these reasons, each traceable to the files above:

1. **No row is CONFIRMED.** 0 of 328 rows are edition-locked. 161 rows read EDITION NOT LOCKED; the 61 "standard numbering" rows are locked to a digital numbering, not to a print edition and page.
2. **The manuscript itself has not been seen.** The DOCX is unavailable, every page is `PAGE-CHECK (docx not available)`, and whether earlier patches were applied is unknown.
3. **Factual citation errors are still in the text.** 12 MM rows are CORRECTED only in the ledger, with the manuscript patch pending, plus the new defects BUG-31…61 (e.g. Basra/Kufa, «ইতরাত» under Muslim, six vs nine months, the deed's writer).
4. **Weak reports lack grades.** 23 graded numbers are not sahih per graders, 2 of them MUNKAR. Prose still renders weak reports as flat «রাসূলুল্লাহ ﷺ বলেছেন» (XRM-028/029/030/050/051).
5. **Nothing Shia is live-verified.** 169 Shia lines: 98 PAGE-CHECK, 64 CANDIDATE, 7 resting on unopened S-181 URLs. 67 Sunni-outside-six rows are CANDIDATE (al-Hakim, Tabarani, Ahmad, Bayhaqi, Kanz …).
6. **The S-181 edition-lock checklist** (11 items) is open, so S-181 itself is "PRINT: CONDITIONAL".
7. **Normalisation is not done.** 41 of 95 register keys carry a status conflict, several keys mix different hadiths, and internal IDs and paths are still in reader text.
8. **Author decisions are pending.** 8 flagged unidentified rows, F-1 (deed writer), F-5 («হাদী»), S-174 source choice, REF-215/219 identity.
9. **Human review is pending.** 271 ledger rows have Human_Review = YES; 79 of 105 patch blocks require review.
10. **The evidence trail must be regenerated.** The six-book `.md` table still carries pre-correction lines (D-1…D-6), and the ledger Status column of the 62 VL rows has not been updated (XRM-081).

---

## 19 Exact next execution order

The order is fixed. Each step acts on the files and rows listed; a step is complete only when its exit condition is met.

**1. SOURCE-MISSING**
- **First, obtain the DOCX (`B1_P01-11_reader.docx`) or its paragraph export.** Map every ledger `Paragraph_Index` to its DOCX paragraph and page, and replace `PAGE-CHECK (docx not available); ¶n` in ledger v1.3 `Page` (328 rows).
- Decisions CSV, 15 NO_SOURCE_LOCATED rows: 002, 006, 007, 020, 084, 100, 125, 134, 140, 199, 239, 248, 273, 292, 295. For 006, 020, 084, 100, 140, 199, 239, 248, 292 and 295, get the actual manuscript / notebook wording from the DOCX or the author and re-run `verify_sunni.py search`.
- Author decisions on the 8 flagged rows (014, 090, 100, 125, 140, 159, 199, 209).
- Rows whose source is shown false: REF-022 (drop the Muslim attribution); REF-009 «ولو بالصين» clause; REF-011 «Musnad Ahmad 3786»; REF-251 «Hakim 4730» lock; REF-078 Prophet-wrote-deed version (F-1); «Suyuti, Tarikh al-Khulafa» for the tearing (REF-122).
- *Exit:* each of the 40 decision rows has the author's chosen handling; no kitab name sits on a row without a located source.

**2. NOT VERIFIED**
- **Unblock thaqalayn.net / sunnah.com / dorar.net, or run the Shia checks on a machine that can reach them.**
- Shia control: 98 PAGE-CHECK + 64 CANDIDATE lines (109 rows; 68 SPC rows), including REF-174/c (Ayyashi 67:22: confirm existence or drop) and the speaker / Imam conflicts (XRM-042, 052, 070, 072).
- Re-open the S-181 URLs behind the 7 VERIFIED-S181-URL Shia lines and the 28 Fadak-map VERIFIED-S181-URL lines.
- Ledger: 67 CAND rows. Every al-Hakim row needs a number (BUG-21): 031, 071, 156, 160, 161, 164, 191, 251, 259, 280, 309. Also 14 NOT VERIFIED decision rows, 9 NOT VERIFIED Fadak lines, and the 4 NOT VERIFIED register keys.
- Cross-check the 38 grading-control rows against sunnah.com / dorar.net, which was not possible here.
- *Exit:* each line is VERIFIED (live evidence, URL + extract saved under `audit/verification/`) or stays CANDIDATE / attribution-only.

**3. PAGE-CHECK**
- All rows with PAGE-CHECK in v1.3 `Final_Status`: 68 Shia, 67 CAND, 17 NON-HADITH (e.g. REF-074 Iqbal, *Rumuz-e Bekhudi*).
- The 33 PRESERVE_WITH_PAGE_CHECK patch blocks.
- Umm Ayman / Fadak page items (S-181 §5; control §5): Baladhuri p. 30/35 vs 44–45; Bihar 29 p. 128 vs 176; Bihar 22/101 h. 59; Qurb al-Isnad h. 99 vs 335; al-Ihtijaj 1 pp. 90–92 vs 119–127; Sulaym printed page (and whether it has Ali's testimony, F-9); IAH 16; al-Albani *Silsila* 2260; the speaker in Bihar 29 / al-Ihtijaj (F-3).
- REF-158 Ahmad 3/364 vs 3/346 (BUG-45); REF-023 / 032 Bihar 85:20 vs 82:20 (XRM-045).
- *Exit:* every cited work has volume / page / hadith from a physically or digitally consulted copy.

**4. EDITION LOCK**
- One edition per work for the whole book (F-8; BUG-53): Ibn Sa'd (vol. 8 vs 10), al-Isti'ab (4-vol. vs vol. 12), al-Isaba (4/415 vs 8:262), al-Ihtijaj, Bihar, al-Kafi (159 Shia lines EDITION NOT LOCKED), Futuh al-Buldan (al-Munajjid or de Goeje), Kanz al-'Ummal (XRM-049).
- Six books: choose the print edition behind the standard numbering for the 62 VL rows (161 v1.3 rows EDITION NOT LOCKED).
- Map the EDN rows 049, 075, 107, 126 to standard numbers (049 → 1954; 107 → 2404; 075 → author's edition needed; 126 → 4240 map).
- Resolve edition-dependent spellings: Bukhari 2010 «نعم / نعمت» (C-06) and honorifics (Bukhari 520, 5361, 6318, 6726); Muslim «2408a» sub-id.
- *Exit:* EDITION column filled for every cited row; one numbering system for the book.

**5. GLOBAL REFERENCE NORMALIZATION**
- `audit/B1_P01-11_SOURCE_REGISTER_v1.1.csv` (95 keys, 196 rows): resolve the 41 status conflicts.
- Update HAD-RUYA (C-01), HAD-KISA (C-05), HAD-THAQALAYN (C-09), HAD-QALAM (C-25), HAD-MADINAT-ILM (6 rows).
- Split HAD-FADAK-TESTIMONY (F-7), HAD-IMAM-JAHILIYYA, HAD-WILAYA-KAFI, HAD-FADAK-1726, HAD-FATIMA-NAR, HAD-MANZILA/MUBAHALA; split S-173 → DATE-2014-RAMADAN / HAD-THAQALAYN / HAD-MAWLA; retire CL-HAD-008 and give REF-251 its own key.
- Back-fill the 34 ledger rows that the register names but whose v1.3 `Register_Key` is blank.
- Strip internal IDs, paths and tokens from reader text (§12), and fix the stale v1.3 cells (REF-158 «৪৪৩১», REF-293 "Numbers correct", REF-075 520).
- *Exit:* one canonical citation per key across all 11 parts; no internal token in reader text.

**6. MANUSCRIPT PATCH**
- Apply `manuscript-patches/B1_P01-11_MANUSCRIPT_PATCH_PLAN_v1.0.md` (105 blocks) to the DOCX, with the 12 MM rows (§13) and Basra/Kufa first. Before applying, reconcile the blocks for REF-013, 087, 123, 158, 186, 224 and 313 with C-01, C-18, C-12, C-25, C-05, C-04 and C-19 (§17).
- Apply `manuscript-patches/B1_P03_C06_FADAK_S-181_PATCH.md` with the «হাদী» amendment, an attribution for the A-3 Aus sentence (F-4), separate lines for Ibn Sa'd and Bihar 29 (F-2), and «— S-181 §…» pointers removed.
- Insert the grade qualifiers from the grading control (rows 1–23 of §10) wherever the report is quoted. Use attribution-only wording for the UNID decisions.
- *Exit:* every one of the 105 blocks is applied or explicitly rejected by the author; the 223 NO_CHANGE rows are untouched.

**7. FINAL CITATION AUDIT**
- Re-run `tools/verify_sunni.py batch` with the fixed tool and rebuild `audit/verification/sunni_six_books_check_2026-10-03.md` (removing stale lines D-1…D-6).
- Re-run the ledger stats on a v1.4 ledger built from the patched DOCX. Update the Status column of the 62 VL rows (XRM-081).
- Confirm: zero flat «রাসূল ﷺ বলেছেন» on weak / munkar / disputed rows; zero merged Sunni / Shia recensions; zero «CONFIRMED» without an edition lock; zero internal IDs; all 328 rows still present.
- *Exit:* a clean v1.4 audit report with zero open MM / XRM items, or each remaining item signed off.

**8. HUMAN REVIEW**
- The 271 ledger rows with Human_Review = YES; the 79 review-required patch blocks; the 8 flagged UNID rows; F-1, F-5, F-10; the S-174 source choice; the REF-215/219 identity; the al-Hasakani classification (XRM-067).
- A qualified reviewer signs off the Sunni and Shia recension separation in the Fadak / Umm Ayman chapters.
- *Exit:* a written sign-off per Part.

**9. «PRINT ALLOWED» gate step (named here only as the last step of the sequence; NOT granted by this report)**
- The author decides, only after steps 1–8 are complete and recorded. This audit does not and cannot change the gate.

**Current gate: PRINT BLOCKED.**

---

## Files in this release

| Path | Content | Rows / units |
|---|---|---|
| `audit/B1_P01-11_CITATION_AUDIT_v1.2.md` | this consolidated report | 19 sections |
| `audit/B1_P01-11_CITATION_AUDIT_v1.1.md` | audit v1.1 (BUG-11…30, register table, §3) | 20 bugs; 12 MM corrections |
| `audit/B1_P01-11_CITATION_AUDIT_v1.0.md` | audit v1.0 (immutable; BUG-01…10) | — |
| `audit/_CORRECTIONS_TO_V1_1_2026-10-03.md` | corrections to v1.1 / S-181 patch | 28 (C-01…C-28) |
| `audit/B1_P01-11_UNIDENTIFIED_REFERENCES_AUDIT_v1.3.csv` | ledger v1.3 (23 columns) | 328 rows |
| `audit/B1_P01-11_UNIDENTIFIED_REFERENCES_AUDIT_v1.2.csv` / `_v1.1.csv` / `_v1.0.csv` | earlier ledgers (input history) | 328 rows each |
| `audit/B1_P01-11_CROSS_ROW_MISMATCHES_v1.0.csv` | cross-row conflicts | 92 rows |
| `audit/B1_P01-11_CROSS_ROW_MISMATCHES_v1.0.summary.md` | summary, counts, top 10 | — |
| `audit/B1_P01-11_SUNNI_VERIFICATION_EVIDENCE_v1.1.md` | six-book verification evidence | 214 classifications (176 + 11 table lines; 152 distinct pairs) |
| `audit/verification/sunni_six_books_check_2026-10-03.md` | live six-book check (tables A, B) | stale lines D-1…D-6 |
| `audit/verification/sunni_six_books_check_2026-10-03.raw.txt` | raw tool output (regenerated after fix) | 382 lines |
| `audit/B1_P01-11_GRADING_CONTROL_v1.0.csv` | grades as printed | 38 rows |
| `audit/B1_P01-11_SHIA_SOURCE_CONTROL_v1.0.csv` | Shia citation lines | 169 rows (109 ledger rows) |
| `audit/B1_P01-11_FADAK_EVIDENCE_MAP_v1.0.csv` | Fadak claim units × sources | 73 rows (11 units + 10-W) |
| `audit/B1_P01-11_UMM_AYMAN_CONTROL_v1.0.md` | Umm Ayman units / formulations / flags | 5 units (Paradise report split a/b/c); F-1…F-10 |
| `audit/B1_P01-11_UNIDENTIFIED_ROWS_DECISIONS_v1.0.csv` | decisions on unidentified / «সূত্র নেই» rows | 40 rows |
| `audit/B1_P01-11_UNIDENTIFIED_ROWS_DECISIONS_v1.0.summary.md` | summary | — |
| `audit/B1_P01-11_INTERNAL_SOURCE_ID_AUDIT_v1.0.md` | internal S-ID / path / stand-in audit | — |
| `audit/B1_P01-11_SOURCE_REGISTER_v1.1.csv` | normalisation register | 95 keys (196 rows) |
| `manuscript-patches/B1_P01-11_MANUSCRIPT_PATCH_PLAN_v1.0.md` | proposed manuscript edits | 105 blocks + 223 NO_CHANGE = 328 |
| `manuscript-patches/B1_P03_C06_FADAK_S-181_PATCH.md` | existing Part 3 Ch 06 Fadak patch (amendment pending) | — |
| `sources/S-181_UMM_AYMAN_FADAK_VERIFICATION.md` | Umm Ayman / Fadak research report | 11-item edition-lock checklist |
| `audit/_WORK_BRIEF_2026-10-03.md` | binding brief for the v1.2 package | — |
| `tools/verify_sunni.py` | six-book lookup / search tool (Muslim lookup fixed) | — |

**Gate: `BOOK 1 · PARTS 1–11 — CITATION AUDIT: PRINT BLOCKED`**
