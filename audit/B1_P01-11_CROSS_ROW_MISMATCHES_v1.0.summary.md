# B1_P01-11 — Cross-Row Consistency Audit v1.0 (summary)

**Date:** 2026-10-03
**Output:** `audit/B1_P01-11_CROSS_ROW_MISMATCHES_v1.0.csv` (91 rows, XRM-001 … XRM-091)
**Inputs read:** all 328 rows of ledger v1.2 (every column); audit v1.0 (BUG-01…10); audit v1.1 §2 (BUG-11…30, register table); `audit/verification/sunni_six_books_check_2026-10-03.md` + `.raw.txt`; `sources/S-181_…`; `manuscript-patches/B1_P03_C06_FADAK_S-181_PATCH.md`.
**Live evidence:** `tools/verify_sunni.py show/search` (six-book Arabic corpus). For Muslim, numbers were re-checked by Abd al-Baqi `arabicnumber` prefix (see finding 4 below).
**Gate:** `BOOK 1 · PARTS 1–11 — CITATION AUDIT: PRINT BLOCKED` (unchanged).

Method: started from the `Register_Key` groups, then compared every row pairwise within each topic (Fadak, Thaqalayn, Bidaa-minni, Tasbih, Kisa, Bab-Fatima, Madinat al-ilm, Imam/jahiliyya, Ruya, Fatima-nar, Salat-batra, Nur, Sirat, Mahr, Ghadir, Fatima's worship, etc.) and against the six-book corpus, S-181 and the v1.0/v1.1 audit claims.

---

## 1. Counts per Conflict_Type

A row may carry more than one letter (e.g. `C/D`). "All tags" counts every letter. "Primary" counts only the first letter.

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
| J | character/name/location/speaker conflicts | 14 | 13 |
| K | «সূত্র নেই» where a source exists | 8 | 6 |
| L | CONFIRMED/VERIFIED where only text existence is shown | 5 | 4 |
| M | citation supports only part of the sentence | 12 | 5 |
| N | citation reused outside its context / wrong register | 5 | 1 |
| | **Total rows** | — | **91** |

37 of the 91 rows rest in part on research-layer knowledge. Their Evidence says "research-layer knowledge; needs page lock", and their Correct_Status is CANDIDATE or PAGE-CHECK. 51 rows quote live six-book corpus output.

Five rows are tagged `[row-vs-corpus; Row_B = context row]`: XRM-082, 084, 085, 086 and 087. Each is a conflict between one row and the corpus or an audit claim. Their Row_B is only a context row, not a real second party to the conflict.

---

## 2. The 10 most consequential mismatches for print safety

1. **XRM-001: Basra, not Kufa** (REF-276 vs REF-279).
   - Bukhari 784 reads «صلى مع علي … بالبصرة». The prose has the Companions talking in the Kufa mosque.
   - The remark belongs to one Companion, Imran b. Husayn, not to «সাহাবারা».
   - This is a factual error in the reader text.
2. **XRM-002: Aus ibn al-Hadathan is listed as a witness for Umm Ayman and Ali** (REF-081).
   - S-181 places him with Aisha and Hafsa on the «لا نورث» counter-testimony.
   - The corpus agrees: Bukhari 4033/3094 have «مالك بن أوس بن الحدثان» on the «لا نورث» side.
3. **XRM-009: «কিতাবুল্লাহ ও আমার ইতরাত» is marked CONFIRMED under Sahih Muslim 2408** (REF-157).
   - The corpus text of Muslim 2408.01–.04 has «ثقلين … وأهل بيتي». «عترتي» is absent.
   - This attributes to Sahih Muslim a wording it does not contain. It contradicts REF-043 and BUG-04.
4. **XRM-025: the evidence file behind every "VERIFIED-LIVE" Muslim number is wrong.**
   - In the raw output, `verify_sunni.py show muslim N` fell back to the sequential number. Examples: 2408 returns a Zakat hadith, 2404 returns Zakat, 1851 returns Travellers' prayer.
   - Re-checking by `arabicnumber` prefix confirms the ledger's content claims, so the conclusions stand. The evidence trail does not.
   - About 28 rows are affected. The tool must be fixed and the batch re-run before any Muslim number is printed as verified.
   - The same defect left Muslim 2989 wrongly at PAGE-CHECK (XRM-026).
   - **Update, later on 2026-10-03:** while this audit was running, another process (not this audit) put an uncommitted fix to `find()` in the working tree and regenerated `raw.txt`. The fix matches the integer part of `arabicnumber` and has no fallback for Muslim. The raw file now shows, for example, «muslim 2408 (num 6225/ar 2408.01) [The Book of the Merits of the Companions]».
   - The `.md` table was built on the old run and still lists Muslim 2989 as «⚠ PAGE-CHECK», Bukhari 3110 as the «جويرية» hadith, and Abu Dawud 5023 as «فقد رآني».
5. **XRM-005: Abu Dawud 2972 is cited only for Umar b. Abd al-Aziz's restoration of Fadak** (REF-079 vs REF-078/121/136).
   - Its own text says «وإن فاطمة سألته أن يجعلها لها فأبى».
   - Three graders mark it Daif.
   - The patch prints it as "CONFIRMED" (XRM-006). The ledger Text still says «আবু দাউদের মতে».
6. **XRM-014: Abu Dawud 5023 does not read «فقد رآني».**
   - Its text is «فسيراني في اليقظة أو لكأنما رآني في اليقظة».
   - BUG-13, the HAD-RUYA register and the six-book table all state the wrong wording.
   - The manuscript's wording is Bukhari 110 / Muslim 2266.01.
7. **XRM-030, XRM-029, XRM-028: weak reports printed as flat «রাসূলুল্লাহ ﷺ বলেছেন».**
   - «জ্ঞানের নগরী» (REF-308): Tirmidhi 3723 itself says «غريب منكر».
   - Anger → wudu (REF-304): Abu Dawud 4784 is da'if but is merged with the sahih 4782.
   - Tirmidhi 2951 (REF-222): graded Daif by Shakir, Albani and Zubair.
   - All three break the BUG-22 rule.
8. **XRM-062: «আমরা নবীগণ উত্তরাধিকার রেখে যাই না» (= «معاشر الأنبياء») is printed on Bukhari/Muslim numbers** (REF-123).
   - That wording appears in none of the six books.
   - It is the al-Ihtijaj (Shia) wording quoted in S-181 §3-D, so this mixes a Shia recension into a Sunni citation.
9. **XRM-059: the honorific "proof" chain in Part 3, Ch. 05 (REF-075).**
   - «وهي جويرية فأقبلت تسعى» is **Bukhari 520**, not 3110. Bukhari 3110 is Miswar's report of Ali's proposal.
   - Bukhari 5361, 6318 and 6726 carry the dual «عليهما السلام».
   - All honorifics shown are as printed in this one digital edition.
10. **XRM-039: the chapter titled «নয় মাস ধরে…» cites Tirmidhi 3206** (REF-144/274 vs REF-187/267/269).
    - Tirmidhi 3206 is Anas, six months, fajr only, and da'if.
    - The nine-month, every-prayer report is a different narration (Ibn Abbas; Shawahid; CANDIDATE).

Close behind these:
- XRM-042/043: «লেজকাটা দরুদ».
  - The prose gives it as the Prophet's own words.
  - al-Kafi has it as an Imam's address to a man.
  - The Sunni wording, from al-Sawa'iq, has no isnad.
  - The extra parts of the dialogue come from the author's notebook.
- XRM-066: Tirmidhi 3874/3868 are munkar and 3819 is da'if, with no grade printed.
- XRM-038: Muslim 2424 is CONFIRMED for an Umm Salama version that is not in it.
- XRM-022: Bukhari 3705 is cited for a Tasbih whose order and timing differ from the prose (bedtime, takbir-tasbih-tahmid).
- XRM-064: Fadak as Khadija's mahr, which has no source.

---

## 3. What could not be verified here (stated plainly)

- **Shia sources:** al-Kafi, Bihar al-Anwar, 'Ilal al-Shara'i', Kamal al-Din, al-Ihtijaj, Tafsir al-Qummi/al-Ayyashi, Kitab Sulaym, Qurb al-Isnad, Fiqh al-Rida. No corpus is reachable from here.
  - Every volume, page, bab or hadith number for these works is still unverified, as are every Imam attribution and every wording.
  - Affected rows: XRM-021, 023, 045, 046, 047, 048, 052, 053, 065, 070, 072, 090.
- **Sunni works outside the six books:** al-Hakim, Tabarani, Ahmad, Bayhaqi, Kanz al-'Ummal, Ibn Sa'd, Isti'ab/Isaba, al-Durr al-Manthur, al-Tha'labi, Shawahid al-Tanzil, al-Sawa'iq, al-Adab al-Mufrad, Muwatta'.
  - Every number and page given for these is research-layer and still unverified.
  - Specific items I could not check:
    - who speaks in the Ghadir congratulation in Ahmad (XRM-036);
    - Ibn Umar as the speaker of «ولا بزفرة واحدة» (XRM-054);
    - the Jabir version of «مدينة العلم» in al-Hakim (XRM-032);
    - the «جواز» sirat report (XRM-071);
    - «تتورم قدماها» (XRM-073);
    - the speaker of «أعدى عدوك نفسك» (XRM-083);
    - the Muwatta' «نعمت» (XRM-086);
    - al-Hasakani's sectarian classification (XRM-067);
    - the 'Aqaba/14-men detail (XRM-056).
- **Edition pages:** none of the six-book page numbers were checked. The corpus has no print pagination.
- **Honorifics and minor wording:** results such as «عليها السلام» or «نعم/نعمت» reflect the fawazahmed0 Arabic edition only. Print editions may differ.
- **The manuscript DOCX:** it is not available here. All conflicts are drawn from the ledger `Text` column only. Context beyond that line, such as surrounding prose and page numbers, was not seen.
- **S-181's own URLs:** I took them as recorded in S-181 and did not re-fetch them, because sunnah.com and dorar.net are blocked.

## 4. Next actions (order)

1. Review and commit the working-tree fix to the Muslim lookup in `tools/verify_sunni.py`, together with the regenerated `raw.txt`. Then rebuild the `sunni_six_books_check_2026-10-03.md` table from the new run (XRM-025/026).
2. Correct the audit's own statements contradicted by the corpus:
   - BUG-13 / HAD-RUYA (Abu Dawud 5023);
   - BUG-30 (Bukhari 2035/3101 read «يبلغ…»; Muslim 2175 has both wordings);
   - v1.0 BUG-05 (Bukhari 3767 = «بضعة مني»);
   - REF-075 (520, not 3110);
   - REF-016 (Tirmidhi 3372, not 3370);
   - REF-224 (Tirmidhi 2950, not 2951);
   - REF-186 (the «مكانك» wording is in 3205/3787, not 3871).
3. Apply the J-type corrections: Basra (XRM-001), Aus (XRM-002) and the speaker rows.
4. Print grades wherever B applies.
5. Withdraw the status «CONFIRMED» everywhere until edition lock (XRM-078/079), and remove the AI paraphrase from REF-126.
6. Update the Status column for the 62 VL rows only after step 1 (XRM-081).
7. Split the register keys that mix different hadiths: HAD-IMAM-JAHILIYYA, HAD-WILAYA-KAFI, HAD-FADAK-1726, HAD-FADAK-TESTIMONY (REF-141), HAD-FATIMA-NAR and HAD-MANZILA/MUBAHALA.

PRINT BLOCKED stands.
