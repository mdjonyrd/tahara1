# B1_P01-11 — Unidentified rows & «সূত্র নেই» recheck — decisions v1.0 (summary)

**Date:** 2026-10-03 · **Companion CSV:** `audit/B1_P01-11_UNIDENTIFIED_ROWS_DECISIONS_v1.0.csv` (40 rows)
**Input:** `audit/B1_P01-11_UNIDENTIFIED_REFERENCES_AUDIT_v1.2.csv` (328 rows; this file does not modify it)
**Tool:** `tools/verify_sunni.py search` / `show`, run against the six-book corpus (fawazahmed0/hadith-api Arabic editions). The tool searches for an exact substring once the diacritics are removed. 153 Arabic search terms were run in total, 2–6 per row. Each row's terms and hit counts are in `Arabic_Search_Terms_Tried`.
**Print gate:** PRINT BLOCKED (unchanged).

## Scope (40 rows)

| Group | Rows | n |
|---|---|---|
| CSV `Triage = UNID` | 002, 006, 014, 020, 041, 084, 090, 091, 097, 100, 115, 125, 140, 159, 175, 196, 199, 209, 215, 219, 228, 239, 244, 248, 265, 266, 272, 292, 295, 321 | 30 |
| In the task list but CSV triage = CAND | 007 | 1 |
| Status/Text contains «সূত্র নেই» / «সূত্রহীন» / «উৎস পাওয়া যায়নি» / «সূত্র খাতায় নেই» (not UNID) | 087, 103, 104, 105, 273 | 5 |
| Known cases to confirm (not covered above) | 004, 096 | 2 |
| Extended sweep: an unsourced sub-claim inside a VL row | 134, 202 | 2 |

**Discrepancy:** the task's list of 30 contains REF-007 but not REF-041. In the v1.2 CSV, REF-041 has Triage = UNID and REF-007 has Triage = CAND. Both rows are included here.

## Counts per classification

| Classification | n | Rows |
|---|---|---|
| CANONICAL_SOURCE_FOUND | 6 | 004, 014*, 087, 096†, 105, 159* |
| PLAUSIBLE_SOURCE_ONLY | 16 | 041, 090, 091, 097, 103, 104, 115, 175, 196, 202, 209, 215, 219, 228, 244, 272 |
| SECONDARY_SOURCE_ONLY | 3 | 265, 266, 321 |
| NO_SOURCE_LOCATED | 15 | 002, 006, 007, 020, 084, 100, 125, 134, 140, 199, 239, 248, 273, 292, 295 |
| **Total** | **40** | |

\* Partial match. The six-book text exists, but we cannot confirm it is the same text as the manuscript wording, because the docx is unavailable. These rows are handled as FLAG-FOR-AUTHOR-DECISION.
† Only the short kisa report is confirmed. The long Jabir text is not in the six books.

Recommended handling:
- KEEP-ATTRIBUTION-ONLY «বর্ণিত আছে»: 24
- FLAG-FOR-AUTHOR-DECISION: 8 (014, 090, 100, 125, 140, 159, 199, 209)
- KEEP-«বলা হয়»: 4 (134, 265, 266, 321)
- ADD-SOURCE: 4 (004, 087, 096, 105)
- REMOVE-KITAB-NAME: 0. For REF-199 (the notebook's «Bihar vol. 5»), the author decides.

Per the global law, no historical claim is recommended for removal.

## Rows where a canonical six-book source was found (tool output quoted)

| Row | Source | Tool evidence (quoted) |
|---|---|---|
| REF-004 | **Tirmidhi 614, 2616**; also Ibn Majah 3973 | tirmidhi 614: «…والصدقة تطفئ الخطيئة كما يطفئ الماء النار…» (Shakir/Albani: Sahih); tirmidhi 2616: «…الصوم جنة والصدقة تطفئ الخطيئة كما يطفئ الماء النار وصلاة الرجل من جوف الليل» |
| REF-087 | **Muslim 91** (91.01–91.03); Abu Dawud 4091; Tirmidhi 1998/1999; Ibn Majah 59, 4173 | muslim 91.02: «لا يدخل النار أحد في قلبه مثقال حبة خردل من إيمان ولا يدخل الجنة أحد في قلبه مثقال حبة خردل من كبرياء»; muslim 91.01/91.03: «…مثقال ذرة من كبر»; abudawud 4091: «لا يدخل الجنة من كان في قلبه مثقال حبة من خردل من كبر» |
| REF-096 | **Muslim 2424** (short kisa report, Aisha) | «خرج النبي صلى الله عليه وسلم غداة وعليه مرط مرحل من شعر أسود فجاء الحسن بن علي فأدخله ثم جاء الحسين … ثم جاءت فاطمة … ثم جاء علي فأدخله ثم قال {إنما يريد الله ليذهب عنكم الرجس أهل البيت ويطهركم تطهيرا}» |
| REF-105 | **Bukhari 4966** (also 6578) | «عن ابن عباس … أنه قال في الكوثر هو الخير الذي أعطاه الله إياه» (Ibn Abbas's own statement, not a saying of the Prophet) |
| REF-014* | **Tirmidhi 2325** (the «চার ব্যক্তির পুরস্কার» item only) | «إنما الدنيا لأربعة نفر عبد رزقه الله مالا وعلما فهو يتقي فيه ربه…» (grades: Shakir/Albani Sahih; Zubair Ali Zai Daif) |
| REF-159* | **Bukhari 4845** (also 7302; Tirmidhi 3266) | «كاد الخيران أن يهلكا أبا بكر وعمر رضى الله عنهما رفعا أصواتهما عند النبي … فأنزل الله {يا أيها الذين آمنوا لا ترفعوا أصواتكم}» |

All four known cases are confirmed: REF-087 → Muslim 91, REF-105 → Bukhari 4966, REF-004 → Tirmidhi 614/2616, REF-096 → Muslim 2424.

**Other «সূত্র নেই»/UNID rows that turn out to have a six-book source:** REF-014 and REF-159, both partial and both need author confirmation. No other row in scope has a six-book text that matches its wording.

### A note on the tool and Muslim 91
Before the coordinator's fix, `show muslim 91` printed an empty Introduction entry. The ✅ for Muslim 91 in `verification/sunni_six_books_check_2026-10-03.md` therefore had no displayed text behind it. After the fix, `show muslim 91` lists sub-reports 91.01, 91.02 and 91.03 (Kitab al-Iman), and these match the `search` hits. `show muslim 2424` gives the same result before and after the fix.

## Related six-book texts that must NOT be substituted
These are near matches only. Using any of them in place of the manuscript wording would silently reconcile different reports.

| Row | Near match | Why it is not the claim |
|---|---|---|
| 002 | Bukhari 6472 etc. «سبعون ألفا بغير حساب» | Different subject |
| 041 | Abu Dawud 4700 / Tirmidhi 2155, 3319 «أول ما خلق الله القلم» | About the pen, not the light |
| 090 | Abu Dawud 4681 «فقد استكمل الإيمان» | Four acts, not three |
| 091 | Tirmidhi 2398 «أشد الناس بلاء» | Different saying |
| 097 | Tirmidhi 2449 / Abu Dawud 1682 «الرحيق المختوم» | Graded Daif; no mention of Tasnim |
| 209 | Tirmidhi 3789 «أحبوا الله لما يغذوكم…وأحبوا أهل بيتي لحبي» | Graded Daif by Shakir/Albani; says أهل بيتي, not «ولي» |
| 228 | Tirmidhi 3723 «أنا دار الحكمة وعلي بابها» | al-Tirmidhi calls it غريب منكر; narrated by Ali, not Jabir |
| 248 | Muslim 2813 «عرش إبليس على البحر» | Different report |
| 265 | Bukhari 405 «يناجي ربه» | Different statement |
| 295 | Abu Dawud 1522 «أعني على ذكرك…» | Said to Mu'adh, not Fatima |

## What could NOT be verified
- **No PLAUSIBLE or SECONDARY row is verified.** Every source named in those rows comes from research knowledge only. That covers al-Kafi, Thawab/'Iqab al-A'mal, al-Mahasin, al-Tawhid, Ma'ani al-Akhbar, Basa'ir al-Darajat, Tafsir al-Qummi, Bihar al-Anwar, al-Tabarani, al-Hakim, Ahmad's Fada'il, Kanz al-'Ummal, al-Kashshaf/al-Baghawi, Yanabi' al-Mawadda and Mashariq al-Anwar. Shia works and Sunni works outside the six books cannot be checked in this environment.
- **Volumes, pages and numbers are not confirmed.** Where the CSV gives any, they are either marked "location not known" / PAGE-CHECK or repeated from the ledger and labelled unconfirmed. Examples are al-Kabir 3:43 h. 2630 and Thawab p. 126.
- **The Arabic for knowledge-based candidates is marked "candidate wording, from memory — not verified".** This applies to REF-091, 104, 175, 196, 202, 215 and 219.
- **REF-215 and REF-219 may be one narration.** The halal/haram seeker who ends up chained by the neck looks like a single report attributed to Imam al-Sadiq. This is a hypothesis, and the author must confirm it.
- **Manuscript wording was unavailable for many rows.** For 006, 020, 084, 100, 140, 199, 239, 248, 292 and 295, the ledger gives only a summary, so the actual wording could not be searched. 100 and 140 especially need the author to supply the notebook Arabic or text.
- **Manuscript pages are not known.** The docx is unavailable, so every row's manuscript page is PAGE-CHECK. The ledger ¶ index is recorded in each row's Note.
- **No print edition is locked.** Even the canonical rows are EDITION-LOCK PENDING, because the corpus is a digital edition.
