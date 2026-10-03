# B1_P01-11 — CITATION / REFERENCE AUDIT v1.1

**Builds on:** `B1_P01-11_CITATION_AUDIT_v1.0.md` (immutable) and ledger v1.0 (328 rows)
**Audit date:** 2026-10-03
**Inputs read in full:** all 328 ledger rows (source-note text + prose lines), audit v1.0, S-181 report
**New evidence:** live check of every numbered Sunni reference against the six canonical collections (`audit/verification/sunni_six_books_check_2026-10-03.md`)
**Outputs:** ledger v1.2 (`…_AUDIT_v1.2.csv`, per-row triage), this report, `tools/verify_sunni.py`
**Gate:** `BOOK 1 · PARTS 1–11 — CITATION AUDIT: PRINT BLOCKED` (unchanged)

---

## 1. Executive result

| Triage (ledger v1.2) | Rows | Meaning |
|---|---|---|
| VERIFIED-LIVE | 62 | hadith number + text confirmed today in the six books; many need a **grade** printed |
| SHIA-PAGE-CHECK | 68 | right Shia book named; volume/page/hadith to lock (no Shia corpus reachable from here) |
| CANDIDATE | 67 | source identified from research knowledge; page to lock before print |
| PROSE-LINE | 48 | «বর্ণিত আছে» sentences; each follows its source-block row |
| UNIDENTIFIED | 30 | no classical source known → attribution-only wording or removal |
| NON-HADITH | 17 | history / geography / poetry / institutional |
| DUPLICATE | 13 | same reference as another row → one canonical citation (register) |
| MISMATCH | 12 | wrong number / book / place / wording — corrections below |
| RESOLVED-S181 | 5 | Umm Ayman / Fadak testimony |
| EDITION-NUMBER | 4 | Bengali/local edition numbers → map to standard |
| QURAN-TEXT | 2 | Quran wording checks |

**Headline:** of 328 rows, **12 are factual citation errors** (not just missing pages), **4 are "no source" claims that do have a canonical source**, **5 register groups cite the same hadith 3–5 times with different statuses**, and **30 have no locatable classical source at all**. Nothing here is ready to flip `PRINT BLOCKED`.

---

## 2. New bugs (BUG-11 … BUG-30)

v1.0's BUG-01…10 stand. Added:

### BUG-11 — Basra, not Kufa (REF-276, REF-279) — **factual**
The prose has Companions in the **Kufa** mosque saying they regained the Prophet's prayer behind Ali. The cited hadith (Bukhari 784, 786; Imran b. Husayn / Mutarrif) reads «صلى مع علي **بالبصرة**». Fix the place name or re-source the Kufa claim.

### BUG-12 — Bengali-edition hadith numbers used as if standard (REF-049, 075, 107, 126)
«Bukhari 1815» = Bukhari **1954**; «Bukhari 2874, 3446, 6270, 496» are Bengali-edition numbers (standard: 3092, 3093, **3110**, 3705, 3711-12, 4240-41, 5361, 6318, 6726); «Muslim 6062 / p. 917» = Muslim **2404**. One numbering system for the whole book: standard (sunnah.com / Abd al-Baqi).

### BUG-13 — Abu Dawud 5021 is the wrong hadith (REF-013)
5021 = Abu Qatada «الرؤيا من الله والحلم من الشيطان». The two claims need **5019** («الرؤيا ثلاث») and **5023** («من رآني في المنام فقد رآني»); also Bukhari 110 / 6993, Muslim 2266.

### BUG-14 — «Musnad Ahmad 3786» for the Ark hadith (REF-011, 191, 208)
Wrong book and number. The Ark hadith is al-Hakim, al-Mustadrak 2:343 (h. 3312) and 3:151 (h. 4720); Tabarani al-Awsat 5870 / al-Kabir 2636-2638. Absent from all six books (verified).

### BUG-15 — «الجنة طيبة لا يدخلها إلا الطيب» is not in Sahih Muslim (REF-022)
Confirmed absent. Nearest canonical texts say something else (Muslim 1015 «إن الله طيب لا يقبل إلا طيبا»; Tirmidhi 3462 «الجنة طيبة التربة»). Drop the Muslim attribution; drop or re-source the sentence.

### BUG-16 — "No source" claims that have a source
- REF-087 «مثقال حبة من خردل من كبر» → **Muslim 91** (also Abu Dawud 4091, Tirmidhi 1998, Ibn Majah 59).
- REF-105 Ibn Abbas on al-Kawthar → **Bukhari 4966**.
- REF-004 «الصدقة تطفئ الخطيئة» → **Tirmidhi 614, 2616; Ibn Majah 3973**.
- REF-096 short kisa → **Muslim 2424**.

### BUG-17 — v1.0 over-corrected Bukhari 4240 (REF-131)
4240 **does** contain «فلما توفيت دفنها زوجها علي ليلا ولم يؤذن بها أبا بكر وصلى عليها». Night burial and not informing Abu Bakr are CONFIRMED from 4240. Only the *wasiyya to conceal the grave* is not there (Shia: Bihar 43:183 ff).

### BUG-18 — «مدينة العلم» attributed to Tirmidhi (REF-164, 207, 240, 245, 309)
Tirmidhi has only **3723 «أنا دار الحكمة وعلي بابها»** (da'if). «أنا مدينة العلم وعلي بابها» is al-Hakim 3:126-127 (h. 4637-4639), Tabarani al-Kabir 11061, al-Khatib 11:48-50. Two wordings, two sources — never merged. Five rows → one register entry `HAD-MADINAT-ILM`.

### BUG-19 — «علي مع الحق والحق مع علي» ≠ what al-Hakim carries (REF-280)
al-Hakim / Tirmidhi 3714 carry «رحم الله عليا، اللهم أدر الحق معه حيث دار» (Tirmidhi: very da'if). The «علي مع الحق» wording is al-Khatib, Tarikh Baghdad 14:321 and later works. Quote one wording with its own source.

### BUG-20 — "China" clause of the knowledge hadith (REF-009)
«اطلبوا العلم ولو بالصين» is **not** in Ibn Majah 224 and is judged fabricated by Ibn Hibban and Ibn al-Jawzi. Ibn Majah 224 itself (first clause) is graded *very da'if* by al-Albani. Print accordingly.

### BUG-21 — Every al-Hakim citation needs a hadith number
After S-181 exposed a false Hakim attribution, all Hakim rows (031, 071, 156, 160, 161, 164, 191, 251, 259, 280, 309) are **number-lock mandatory** (al-Risala / Mustafa Ata numbering), with al-Dhahabi's remark where it exists.

### BUG-22 — Weak / munkar reports printed without grade (**print-safety**)
Confirmed grades now known and must appear in the source block: Abu Dawud 2972 (da'if), 3652 (da'if), **4213 (da'if)**, **4784 (da'if)**; Tirmidhi 2951-2952 (da'if), **3206 (da'if)**, 3723 (da'if), 3714 (very da'if), **3819 (da'if)**, **3868 (munkar)**, **3874 (munkar)**; Ibn Majah 224 (very da'if), 2198 (da'if/Albani); Tirmidhi 4 and 3786/3788 (graders disagree — say so). Rule: a *munkar*/*da'if* report may be narrated only with its grade, never as «রাসূল ﷺ বলেছেন» flat.

### BUG-23 — Fadak as Khadija's mahr (REF-125)
No classical source. Recommend removal, or «কেউ কেউ বলেন» with no citation.

### BUG-24 — Iqbal line misspelt (REF-074)
«مادی» → **«مادر»**. Source identified: Iqbal, *Rumuz-e Bekhudi*, section on Sayyida Fatima («مریم از یک نسبت عیسی عزیز…»). Needs edition page.

### BUG-25 — 30 rows have no locatable classical source
REF-002, 006, 007\*, 014, 020, 084, 090, 091, 097, 100, 115, 125, 140, 159, 175, 196, 199, 209, 215, 219, 228, 239, 244, 248, 265, 266, 272, 292, 295, 321. (\*007 needs the Arabic text to search.) Decision per row: attribution-only wording («বর্ণিত আছে» / «বলা হয়») **or** removal. None may carry a kitab name.

### BUG-26 — One hadith, many statuses (normalisation register)
Same reference cited in several rows with different statuses. Register keys now in ledger v1.2 (`Register_Key`); the book must carry **one** canonical citation per key:

| Key | Rows | Canonical lock |
|---|---|---|
| HAD-THAQALAYN | 043, 157, 206, 242, 258 | Muslim 2408; Tirmidhi 3786; Tirmidhi 3788 — all verified; grades differ |
| HAD-MADINAT-ILM | 164, 207, 240, 245, 309 | Hakim 4637-4639 (+ Tirmidhi 3723 only for «دار الحكمة») |
| HAD-BIDAA-MINNI | 072, 076, 142, 153, 250 | Bukhari 3714 (+ Muslim 2449 / Bukhari 5230 for «يؤذيني ما آذاها») |
| HAD-BAB-FATIMA-SALAT | 144, 187, 189, 269, 274 | Tirmidhi 3206 (da'if) + Shawahid al-Tanzil 2:11 ff |
| HAD-TASBIH | 003, 064, 066, 067 | Bukhari 3705 + one Kafi placement |
| HAD-ZAHRA-NAME | 246, 249, 289, 291 | 'Ilal al-Shara'i' 1:180-181 |
| HAD-FADAK-1726 | 121, 136, 137, 138 | Durr al-Manthur 4:177 + Kafi 1:543 h. 5 |
| HAD-FADAK-TESTIMONY | 078, 081, 122, 141 | S-181 |
| HAD-SAFINA | 011, 191, 208 | Hakim 3312 / 4720 |
| HAD-UMM-ABIHA | 069, 155, 255 | Isti'ab 4:1899 / Isaba 8:262 / Bihar 43:19 |
| HAD-RIDA-3SUNAN | 089, 216, 220 | Kafi 2:241 h. 39 |
| HAD-QIYAM-FATIMA | 068, 252, 262 | Abu Dawud 5217 / Tirmidhi 3872 |
| HAD-12-KHALIFA | 143, 152, 240 | Bukhari 7222 / Muslim 1821 |
| HAD-IMAM-JAHILIYYA | 037, 059, 083 | Kafi 1:376-377 (Shia wording) ≠ Muslim 1851 (bay'a wording) |
| HAD-MUBAHALA | 080, 106, 107, 236 | Muslim 2404 + Kashshaf 1:368-370 |
| HAD-BIDAA-KAFI | 217, 226, 231 | Kafi 1:54-58 |
| HAD-KISA | 096, 186, 188, 190 | Muslim 2424; Tirmidhi 3871 |
| HAD-MAHR-KHUMS | 050, 057, 168 | Fiqh al-Rida / Bihar 43 |
| HAD-FATIMA-NAR | 086, 256, 259 | Hakim 4726 / Tabarani 11685 / Kanz 12:109 |
| HAD-SALAT-BATRA | 025, 034, 302, 303 | Kafi 2:495 (Shia) / al-Sawa'iq (Sunni) |
| HAD-NUQTA | 024, 033, 321 | Kafi 1:114 for «بهاء الله»; nuqta saying NOT VERIFIED |
| HAD-RUYA | 013, 201 | Bukhari 110 / Muslim 2266 / Abu Dawud 5023 |
| others | see `Register_Key` column | |

### BUG-27 — Local path as citation (REF-101) — instance of BUG-07
Replace `F:\…hubbe_ali_ch108…md` with the Tafsir Hubb-e Ali hadith numbers (h. 10-11; hubbeali.com h. 9499).

### BUG-28 — Audit language inside a source block (REF-145) — instance of BUG-09

### BUG-29 — Secondary sources standing in for primaries
REF-294 (English anthology) → Bihar 43:76 / Manaqib 3:341; REF-296 (al-islam.org) → Misbah al-Mutahajjid; REF-297/299 (Mizan al-Hikma) → each primary; REF-279 (Mishkat / Tajrid) → Bukhari 784.

### BUG-30 — Muslim 2175 wording
Bukhari (2035 etc.): «يجري من الإنسان مجرى الدم»; Muslim 2175: «يبلغ من الإنسان مبلغ الدم». Quote the wording of the book you cite.

---

## 3. Mismatch corrections (the 12 MM rows)

| REF | Manuscript / ledger says | Correct |
|---|---|---|
| 009 | Ibn Majah (incl. China clause) | Ibn Majah 224 first clause only (very da'if); China clause unsupported |
| 011 | Musnad Ahmad 3786 | Hakim 3312 / 4720; Tabarani |
| 013 | Abu Dawud 5021 | Abu Dawud 5019 + 5023 |
| 022 | Sahih Muslim | not in Muslim — drop |
| 087 | no source | Muslim 91 |
| 101 | F:\ local path | Hubb-e Ali h. 10-11 |
| 105 | no source | Bukhari 4966 |
| 131 | 4240 lacks night-burial | 4240 has night burial + not informing Abu Bakr; only concealment wasiyya absent |
| 145 | audit note in source block | move to ledger |
| 279 | Kufa | **Basra** (Bukhari 784, 786) |
| 280 | Hakim: «علي مع الحق» | Hakim/Tirmidhi 3714: «أدر الحق معه»; «علي مع الحق» → Khatib 14:321 |
| 309 | Tirmidhi: «مدينة العلم» | Tirmidhi 3723 «دار الحكمة»; «مدينة العلم» → Hakim |

---

## 4. Verified today (62 rows) — what changes in the ledger
`PAGE-CHECK` on a six-book **number** is cleared for these rows (number and text confirmed); what remains is (a) printing the **grade** where BUG-22 applies, (b) choosing one numbering system (BUG-12), (c) edition page only if the book prints page numbers. Full table: `audit/verification/sunni_six_books_check_2026-10-03.md`.

---

## 5. What could not be verified from this environment
- **Shia sources** (al-Kafi, Bihar, 'Ilal, Kamal al-Din, Qummi, Ayyashi, Ihtijaj, Sulaym): 68 rows named correctly as far as the research layer can tell; vol/page/hadith lock needs the print editions or thaqalayn.net (blocked here).
- **Sunni works outside the six** (al-Hakim, Tabarani, Ahmad, Bayhaqi, Kanz, tafsir works): 67 CANDIDATE rows carry the specific book + approximate location; number/page lock pending.
- **Network:** sunnah.com, dorar.net, cdn.jsdelivr.net denied by the environment's network policy; GitHub allowed (used for the six-book corpus).

---

## 6. Next execution order (revised)
1. **Apply the 12 MM corrections** to the manuscript (prose + source blocks). Basra/Kufa and the four "no source → source" items first.
2. **Print grades** for every BUG-22 row; never print munkar/da'if as flat «রাসূল ﷺ বলেছেন».
3. **Normalise** the register groups (BUG-26): one canonical citation per key across all 11 parts.
4. **Decide the 30 UNID rows**: attribution-only or delete; no kitab names.
5. **Edition lock**: Shia 68 + Sunni-outside-six 67 rows, one chosen edition per work (reuse S-181 §5 checklist pattern).
6. Separate reader-facing attribution from QA vocabulary (BUG-10); remove local paths (BUG-07/27) and audit notes (BUG-09/28).
7. Re-run `tools/verify_sunni.py batch` and the ledger stats; only then `PRINT BLOCKED → PRINT ALLOWED`.
