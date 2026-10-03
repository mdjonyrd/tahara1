# B1 · Parts 1–11 — Manuscript Patch Plan v1.0

**File:** `manuscript-patches/B1_P01-11_MANUSCRIPT_PATCH_PLAN_v1.0.md`  
**Date:** 2026-10-03  
**Gate:** `BOOK 1 · PARTS 1–11 — CITATION AUDIT: PRINT BLOCKED` (unchanged by this plan)

> **The manuscript DOCX (`B1_P01-11_reader.docx`) was NOT modified, and is not available in this environment.** This plan is a list of proposed edits only. Every CURRENT_TEXT is quoted from the ledger `Text` column. No page numbers exist here: every PAGE field reads `PAGE-CHECK (docx not available); ¶<Paragraph_Index>`, and the editor must locate each item in the DOCX by its paragraph index and text.

## 0. Scope, inputs, method

**Scope.** All 328 ledger rows of Book 1, Parts 1–11. This file has one patch block for every row that needs a manuscript change, and one NO_CHANGE line for every other row (§3). Order: Part → Chapter (in manuscript sequence) → Paragraph_Index.

**Inputs read:**
- `audit/_WORK_BRIEF_2026-10-03.md` (binding rules)
- `audit/B1_P01-11_UNIDENTIFIED_REFERENCES_AUDIT_v1.2.csv` (328 rows, all read)
- `audit/B1_P01-11_CITATION_AUDIT_v1.1.md` (BUG-11…30, §2 register, §3 corrections table)
- `audit/verification/sunni_six_books_check_2026-10-03.md` (+ `.raw.txt`)
- `sources/S-181_UMM_AYMAN_FADAK_VERIFICATION.md`
- `manuscript-patches/B1_P03_C06_FADAK_S-181_PATCH.md`
- `tools/verify_sunni.py` corpus (`tools/_hadith-api/editions`, six books, Arabic) — every EVIDENCE line quoted below was produced on 2026-10-03 from this corpus
- Coordinator message (2026-10-03): Muslim-lookup fix in `verify_sunni.py`; Fadak/Umm Ayman agent findings (REF-078, «হাদী», Bukhari 4240 scope, Malik b. Aws ≠ Aus)

**Selection rule.** A row gets a patch block if it is MM, EDN, S181, DUP or UNID (all such rows); VL where a grade must be printed, a number must be added or mapped, or a wording/attribution is inexact; PROSE where the prose certainty or attribution exceeds or contradicts the source; or CAND/HIST where audit v1.1 names a concrete text defect (BUG-16 REF-004; BUG-18 REF-164; BUG-24 REF-074; BUG-29 REF-294, 296, 299). Every other row is NO_CHANGE.

**Evidence format.** Lines beginning `-- <book> <no.>` are `verify_sunni.py` corpus output: the header shows the number, Abd al-Baqi number and corpus grades, followed by a text window around the key phrase. Muslim is looked up by Abd al-Baqi number (sub-reports `.01`, `.02` …), which is the behaviour of the tool after the coordinator's fix (re-checked: `show muslim 2175` now returns 2175.01 / 2175.02). Lines beginning `search «…»` are substring searches over all six books. Anything outside the six books is labelled **KNOWLEDGE-ONLY** and is never marked VERIFIED.

**Confidence / review rules.** HIGH requires live evidence (corpus output or the S-181 report with its URLs). MEDIUM is a knowledge-based candidate; LOW is everything else. REQUIRES_HUMAN_REVIEW = NO only for pure number or grade fixes backed by live evidence on which graders agree. Every theological or historical wording change, every REMOVE_*, every disputed or munkar narration, and every non-live item is YES.

**Replacement wording.** Bengali in «…» is the proposed print text. ⟦…⟧ marks a slot to fill after edition lock; candidate numbers are never printed before lock. Dialogue and authorial voice are untouched: in prose rows only the attribution clause changes. Sunni and Shia recensions are never merged.

## 1. Counts

- Ledger rows: **328**. Patch blocks: **105**. NO_CHANGE rows (§3): **223**.
- Patch blocks by ledger triage: MM 12, EDN 4, S181 5, DUP 13, UNID 30, VL 32, PROSE 3, CAND 5, HIST 1.

**Per PATCH_TYPE** (some blocks are compound, e.g. `REMOVE_FALSE_SOURCE + ADD_SOURCE`; the "component" column counts each component, the "primary" column counts the first-named type, and the primary column sums to the block count):

| PATCH_TYPE | primary (blocks) | component occurrences |
|---|---|---|
| CORRECT_CITATION | 21 | 21 |
| CORRECT_LOCATION | 2 | 2 |
| CORRECT_HADITH_NUMBER | 23 | 23 |
| CORRECT_SOURCE | 3 | 3 |
| WEAKEN_ATTRIBUTION | 5 | 6 |
| ADD_SOURCE | 8 | 10 |
| REMOVE_FALSE_SOURCE | 2 | 2 |
| SPLIT_CLAIM | 8 | 8 |
| PRESERVE_WITH_PAGE_CHECK | 33 | 33 |
| NO_CHANGE | 223 (table §3) | — |
| **Total** | **105 blocks + 223 NO_CHANGE = 328** | 108 |

**Per CONFIDENCE** (patch blocks): HIGH 53 · MEDIUM 20 · LOW 32  
**REQUIRES_HUMAN_REVIEW = YES:** 79 of 105 (NO: 26).

## 2. Findings that go beyond audit v1.1 (from today's live checks)

- **REF-075:** «وهي جويرية فأقبلت تسعى» is **Bukhari 520**. Triage v1.2 maps it to 3110, which is wrong. Corpus scan: the phrase occurs only in 520.
- **REF-013:** Abu Dawud **5023** reads «فسيراني في اليقظة», not «فقد رآني». The manuscript's wording («সত্যিই আমাকে দেখল») is Bukhari 110 / Muslim 2266. The six-book report's gloss of 5023 is inexact.
- **REF-224:** the wording «বিনা ইলমে» = «بغير علم» is Tirmidhi **2950**, a separate hadith from 2951 (REF-223). The ledger's "same as 223" is wrong.
- **REF-039 / BUG-30:** Muslim 2175 carries **both** wordings: 2175a «يجري من الإنسان مجرى الدم» and 2175b «يبلغ من الإنسان مبلغ الدم». BUG-30 gives only the second.
- **REF-188:** Muslim 2424 is **Aisha only**. Umm Salama's short kisa report is Tirmidhi 3871 («إنك على خير»).
- **REF-123:** the gloss «আমরা নবীগণ…» (معاشر الأنبياء) is not in Bukhari 3093 / 6726 / Muslim 1759, which read «لا نورث ما تركنا صدقة».
- **REF-078:** the dialogue makes the **Prophet** the writer of the Fadak deed, but al-Ihtijaj has **Abu Bakr** writing it (and Umar tearing it). The ledger resolution's mapping is therefore unsafe. This agrees with the Fadak/Umm Ayman agent.
- **REF-142 / REF-153:** no «يسرني ما يسرها / يبسطني» wording exists in the six books (live search). «যে তাকে খুশি করে» must not be mapped to Muslim 2449 (whose wording is «يؤذيني ما آذاها»).
- **REF-081:** Malik b. Aws b. al-Hadathan (Sunni narrator of the Fadak / «لا نورث» dispute, Bukhari 3094, Muslim 1757, live) is a different person from the Shia-chain witness Aus ibn al-Hadathan. Keep them apart.
- **Tool:** before the coordinator's fix, `show muslim N` resolved most Muslim numbers to a different hadith (raw.txt shows e.g. «muslim 2175 … [Funerals]»). Muslim verdicts in the 2026-10-03 six-book report should be re-run with the fixed tool. All Muslim evidence in this plan was taken by Abd al-Baqi number.

**Amendment to the existing S-181 patch (not a ledger row; no block number).** `manuscript-patches/B1_P03_C06_FADAK_S-181_PATCH.md` A-1 and §B bullet 1 call Umm Ayman «হাদী». In Bengali this is ambiguous: it can be read as Arabic هادي «guide». The sources say **حاضنة**, i.e. nurse / foster-carer. Proposed: replace «হাদী» with «লালনকারিণী / ধাত্রী (حاضنة)» in both places. Live Sunni evidence for her identity:
  - `-- bukhari 3737 (num 3737/ar 3737) [Companions of the Prophet]  :: …وما ولدته أم أيمن. قال وحدثني بعض أصحابي عن سليمان وكانت حاضنة النبي صلى الله عليه وسلم.…`
  - `-- bukhari 2630 (num 2630/ar 2630) [Gifts]  :: …ه صلى الله عليه وسلم عذاقا فأعطاهن النبي صلى الله عليه وسلم أم أيمن مولاته أم أسامة بن زيد. قال ابن شهاب فأخبرني أنس بن مالك…`
  - `-- muslim 1771 (num 4603/ar 1771.01) [The Book of Jihad and Expedition]  :: …له عليه وسلم عذاقا لها فأعطاها رسول الله صلى الله عليه وسلم أم أيمن مولاته أم أسامة بن زيد . قال ابن شهاب فأخبرني أنس بن مالك…`
  - `-- bukhari 3736 (num 3736/ar 3736) [Companions of the Prophet]  :: …الزهري، أخبرني مولى، لأسامة بن زيد. أن الحجاج بن أيمن ابن أم أيمن،، وكان، أيمن ابن أم أيمن أخا أسامة لأمه، وهو رجل من الأنصار…`
  - `-- muslim 2453 (num 6317/ar 2453) [The Book of the Merits of the Co]  :: …عن ثابت، عن أنس، قال انطلق رسول الله صلى الله عليه وسلم إلى أم أيمن فانطلقت معه فناولته إناء فيه شراب - قال - فلا أدري أصادفته…`
  - `-- muslim 2454 (num 6318/ar 2454) [The Book of the Merits of the Co]  :: …نه بعد وفاة رسول الله صلى الله عليه وسلم لعمر انطلق بنا إلى أم أيمن نزورها كما كان رسول الله صلى الله عليه وسلم يزورها . فلما…`
  PATCH_TYPE CORRECT_CITATION · CONFIDENCE HIGH · REQUIRES_HUMAN_REVIEW YES (identity wording).

## 3. Patch blocks

---

## Part 1

### PB1-001

- **PATCH_ID:** PB1-001
- **PART:** 1
- **CHAPTER:** ০৩  আমার ভেতরেও একটি বন্ধ কুঠুরি
- **PAGE:** PAGE-CHECK (docx not available); ¶233
- **PARAGRAPH/LOCATION:** Ledger REF-002 · Paragraph_Index 233 · source-note bullet (chapter source block) · register HAD-SHIA-BIGHAYR-HISAB
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  ইমাম সাদিক (আলাইহিস্ সালাম) থেকে «বিনা হিসাবে প্রথম জান্নাতে» — খাতায় সূত্র নেই; «বর্ণিত আছে», PAGE-CHECK (উৎস খোঁজা বাকি; ছাপার আগে বই-খণ্ড-পৃষ্ঠা লাগবে)।
- **PROBLEM:** UNIDENTIFIED (BUG-25): no classical source located. The note is already attribution-only («বর্ণিত আছে») and carries no kitab name; prose that depends on it must not rise above «বর্ণিত আছে». Prose REF-001 (¶197) keeps «ইমাম সাদিক থেকে বর্ণিত আছে» — matches this status.
- **EVIDENCE:**
  - No source evidence exists in this repo for this row (audit v1.1 BUG-25 list). KNOWLEDGE-ONLY (research layer / audit v1.1 candidate; not verifiable from this environment).
- **SOURCE:** None located (ledger Candidate_Source: see CSV).
- **SOURCE_STATUS:** SOURCE-MISSING · বর্ণিত আছে · PRINT BLOCKED (book gate)
- **PROPOSED_ACTION:**
  Retain the current wording verbatim (no kitab name may be added). Author decides: keep as attribution-only, or delete the item (BUG-25). If a sanad is later found, re-open as ADD_SOURCE with PAGE-CHECK.
- **PATCH_TYPE:** PRESERVE_WITH_PAGE_CHECK
- **CONFIDENCE:** LOW
- **REQUIRES_HUMAN_REVIEW:** YES

### PB1-002

- **PATCH_ID:** PB1-002
- **PART:** 1
- **CHAPTER:** ০৫  ধন-সম্পদ, অভাব আর দানের পরীক্ষা
- **PAGE:** PAGE-CHECK (docx not available); ¶397
- **PARAGRAPH/LOCATION:** Ledger REF-004 · Paragraph_Index 397 · source-note bullet (chapter source block) · register HAD-SADAQA-NAR
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  «সাদাকাহ গুনাহ নিভিয়ে দেয়, যেমন পানি আগুন» — তিরমিযিতে বর্ণিত বলে প্রচলিত; PAGE-CHECK (নম্বর মেলানো বাকি, ছাপায় নম্বর ছাড়া)।
- **PROBLEM:** Note says the number is unmatched and the item should print without a number; the wording is in Tirmidhi 614, 2616 and Ibn Majah 3973 (audit BUG-16).
- **EVIDENCE:**
  - `-- tirmidhi 614 (num 614/ar 614) [The Book on Traveling] Ahmad Muhammad Shakir:Sahih;Al-Albani:Sahih;Zubair Ali Zai:Isnaad Hasan :: …مهم فهو مني وأنا منه وسيرد على الحوض يا كعب بن عجرة الصلاة برهان والصوم جنة حصينة والصدقة تطفئ الخطيئة كما يطفئ الماء النار . يا كعب بن عجرة إنه لا يربو لحم نبت من سحت إلا كانت النار…`
  - `-- tirmidhi 2616 (num 2616/ar 2616) [The Book on Faith] Ahmad Muhammad Shakir:Sahih;Al-Albani:Sahih;Bashar Awad Maarouf:Hasan Sahih;Zubair Ali Zai:Hasan :: …زكاة وتصوم رمضان وتحج البيت " . ثم قال " ألا أدلك على أبواب الخير الصوم جنة والصدقة تطفئ الخطيئة كما يطفئ الماء النار وصلاة الرجل من جوف الليل " . قال ثم تلا: ( تتجافى جن…`
  - `-- ibnmajah 3973 (num 3973/ar 3973) [Tribulations] Al-Albani:Sahih;Muhammad Fouad Abd al-Baqi:Sahih;Zubair Ali Zai:Hasan :: …زكاة وتصوم رمضان وتحج البيت " . ثم قال " ألا أدلك على أبواب الجنة الصوم جنة والصدقة تطفئ الخطيئة كما يطفئ النار الماء وصلاة الرجل في جوف الليل " . ثم قرأ {تتجافى جنوبهم عن ا…`
- **SOURCE:** Jami' al-Tirmidhi 614 (Ka'b b. Ujra), 2616 (Mu'adh b. Jabal); Sunan Ibn Majah 3973 (Mu'adh).
- **SOURCE_STATUS:** VERIFIED (live, number + text); grades in corpus: sahih (Albani, Shakir), hasan / isnad hasan (Zubair Ali Zai).
- **PROPOSED_ACTION:**
  Replace the bullet with:
  «•  «সাদাকাহ গুনাহ নিভিয়ে দেয়, যেমন পানি আগুন» — জামে তিরমিযি ৬১৪ (কা'ব ইবনে উজরা) ও ২৬১৬ (মুআয ইবনে জাবাল); সুনানে ইবনে মাজাহ ৩৯৭৩ (মুআয) — আলবানী: সহিহ।»
- **PATCH_TYPE:** ADD_SOURCE
- **CONFIDENCE:** HIGH
- **REQUIRES_HUMAN_REVIEW:** NO

### PB1-003

- **PATCH_ID:** PB1-003
- **PART:** 1
- **CHAPTER:** ০৬  “জানি না” বলার সাহস
- **PAGE:** PAGE-CHECK (docx not available); ¶497
- **PARAGRAPH/LOCATION:** Ledger REF-005 · Paragraph_Index 497 · source-note bullet (chapter source block)
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  কুঠার কিনে দেওয়ার ঘটনা: সুনানে ইবনে মাজাহ, কিতাবুত তিজারাত, হাদীস ২১৯৮ — খাতার সূত্র; PAGE-CHECK।
- **PROBLEM:** Number correct, but the report is graded weak by al-Albani and Abd al-Baqi while Zubair Ali Zai calls its isnad hasan; no grade is printed (BUG-22).
- **EVIDENCE:**
  - `-- ibnmajah 2198 (num 2198/ar 2198) [The Chapters on Business Transac] Al-Albani:Daif;Muhammad Fouad Abd al-Baqi:Daif;Zubair Ali Zai:Isnaad Hasan :: …وأخذ الدرهمين فأعطاهما الأنصاري وقال " اشتر بأحدهما طعاما فانبذه إلى أهلك واشتر بالآخر قدوما فأتني به " . ففعل فأخذه رسول الله صلى الله عليه وسلم فشد فيه عودا بيده وقال " اذه…`
- **SOURCE:** Sunan Ibn Majah 2198 (Anas b. Malik), Kitab al-Tijarat.
- **SOURCE_STATUS:** VERIFIED (live, number + text); graders disagree.
- **PROPOSED_ACTION:**
  Replace the bullet with:
  «•  কুঠার কিনে দেওয়ার ঘটনা: সুনানে ইবনে মাজাহ, কিতাবুত তিজারাত, হাদীস ২১৯৮ (আনাস) — সনদের মান নিয়ে মতভেদ: আলবানী ও মুহাম্মাদ ফুয়াদ আবদুল বাকি: যয়ীফ; যুবাইর আলী যাঈ: সনদ হাসান।»
  Check the prose that tells this story: it must not present it as a flat «রাসূলুল্লাহ ﷺ বলেছেন» without the grade.
- **PATCH_TYPE:** CORRECT_CITATION
- **CONFIDENCE:** HIGH
- **REQUIRES_HUMAN_REVIEW:** YES

### PB1-004

- **PATCH_ID:** PB1-004
- **PART:** 1
- **CHAPTER:** ০৬  “জানি না” বলার সাহস
- **PAGE:** PAGE-CHECK (docx not available); ¶498
- **PARAGRAPH/LOCATION:** Ledger REF-006 · Paragraph_Index 498 · source-note bullet (chapter source block)
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  চারবার বিয়ের ঘটনা — «বর্ণিত আছে»; উৎস খোঁজা বাকি, ছাপায় বইয়ের নাম ছাড়া।
- **PROBLEM:** UNIDENTIFIED (BUG-25): no classical source located. The note is already attribution-only («বর্ণিত আছে») and carries no kitab name; prose that depends on it must not rise above «বর্ণিত আছে».
- **EVIDENCE:**
  - No source evidence exists in this repo for this row (audit v1.1 BUG-25 list). KNOWLEDGE-ONLY (research layer / audit v1.1 candidate; not verifiable from this environment).
- **SOURCE:** None located (ledger Candidate_Source: see CSV).
- **SOURCE_STATUS:** SOURCE-MISSING · বর্ণিত আছে · PRINT BLOCKED (book gate)
- **PROPOSED_ACTION:**
  Retain the current wording verbatim (no kitab name may be added). Author decides: keep as attribution-only, or delete the item (BUG-25). If a sanad is later found, re-open as ADD_SOURCE with PAGE-CHECK.
- **PATCH_TYPE:** PRESERVE_WITH_PAGE_CHECK
- **CONFIDENCE:** LOW
- **REQUIRES_HUMAN_REVIEW:** YES

### PB1-005

- **PATCH_ID:** PB1-005
- **PART:** 1
- **CHAPTER:** ০৬  “জানি না” বলার সাহস
- **PAGE:** PAGE-CHECK (docx not available); ¶501
- **PARAGRAPH/LOCATION:** Ledger REF-009 · Paragraph_Index 501 · source-note bullet (chapter source block)
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  «জ্ঞান অর্জন ফরজ… শুকরের গলায় মণিমুক্তা» — সুনানে ইবনে মাজাহ (মুকাদ্দিমা) বলে প্রচলিত; «চীন» অংশ দুর্বল সনদের বলে আলেমদের মত। PAGE-CHECK।
- **PROBLEM:** The note runs together two separate things: (a) the Ibn Majah 224 text, which al-Albani, Shu'ayb al-Arna'ut and Abd al-Baqi grade «very weak», and (b) the «China» clause. The China clause does not appear anywhere in the six books, so it is not in Ibn Majah. The current note calls it only «দুর্বল» (weak), as part of an Ibn Majah attribution.
- **EVIDENCE:**
  - `-- ibnmajah 224 (num 224/ar 224) [The Book of the Sunnah] Al-Albani:Very Daif;Muhammad Fouad Abd al-Baqi:Very Daif;Shuaib Al Arnaut:Very Daif;Zubair Ali Zai:Daif :: …ر بن شنظير، عن محمد بن سيرين، عن أنس بن مالك، قال قال رسول الله صلى الله عليه وسلم  " طلب العلم فريضة على كل مسلم وواضع العلم عند غير أهله كمقلد الخنازير الجوهر واللؤلؤ والذهب " .…`
  - `search «بالصين» (all six books) → (none)`
  - Fabrication verdict on the China clause (Ibn Hibban; Ibn al-Jawzi, al-Mawdu'at): KNOWLEDGE-ONLY (research layer / audit v1.1 candidate; not verifiable from this environment).
- **SOURCE:** Sunan Ibn Majah 224 (Anas), Muqaddima — first clause only. China clause: no six-book source.
- **SOURCE_STATUS:** Clause (a): VERIFIED (live), grade «very da'if». Clause (b): ABSENT from the six books (live search); fabrication verdict is a CANDIDATE (not verifiable here).
- **PROPOSED_ACTION:**
  Replace the bullet with:
  «•  «জ্ঞান অর্জন ফরজ… শুকরের গলায় মণিমুক্তা» — সুনানে ইবনে মাজাহ, মুকাদ্দিমা, হাদীস ২২৪ (আনাস); সনদ অত্যন্ত দুর্বল (আলবানী, শুআইব আরনাউত ও মুহাম্মাদ ফুয়াদ আবদুল বাকি: «ضعيف جدا»)। «চীন» অংশটি ইবনে মাজাহতে নেই; সিহাহ সিত্তার কোথাও পাওয়া যায়নি — PAGE-CHECK (ইবনে হিব্বান ও ইবনুল জাওযির মূল্যায়নের পৃষ্ঠা)।»
  The prose that uses this saying (not in the ledger) must not attribute the China clause to Ibn Majah or to «সহিহ হাদিস», and must not present it as a flat «রাসূলুল্লাহ ﷺ বলেছেন». Rewrite only the attribution clause there, e.g. «বর্ণিত আছে (সনদ অত্যন্ত দুর্বল)».
- **PATCH_TYPE:** SPLIT_CLAIM
- **CONFIDENCE:** MEDIUM
- **REQUIRES_HUMAN_REVIEW:** YES

### PB1-006

- **PATCH_ID:** PB1-006
- **PART:** 1
- **CHAPTER:** ০৭  জুমার খুতবায় যা বলা হলো না
- **PAGE:** PAGE-CHECK (docx not available); ¶581
- **PARAGRAPH/LOCATION:** Ledger REF-011 · Paragraph_Index 581 · source-note bullet (chapter source block) · register HAD-SAFINA
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  «আমার আহলুল বাইত হচ্ছে নূহ (আলাইহিস্ সালাম)-এর নৌকার মতো। যারা এতে চড়ে, তারা নাজাত পায়; যারা বিমুখ হয়, তারা ডুবে যায়।» — খাতায় «মুসনাদে আহমদ ৩৭৮৬»; এই নম্বর সন্দেহজনক (তিরমিযি ৩৭৮৬ সাকালাইনের হাদীস)। PRINT BLOCKED নম্বরটি; ছাপায় «বর্ণিত আছে» যতক্ষণ সঠিক উৎস (হাকিম/তাবারানি) মেলানো না হয়।
- **PROBLEM:** The note cites «মুসনাদে আহমদ ৩৭৮৬», a wrong book and number for the Ark hadith (BUG-14). The number 3786 is Tirmidhi's Thaqalayn hadith, and the Ark wording appears nowhere in the six books. The real carriers are al-Hakim and al-Tabarani, which still need page lock (BUG-21).
- **EVIDENCE:**
  - `search «سفينة نوح» (all six books) → (none)`
  - `-- tirmidhi 3786 (num 3786/ar 3786) [Chapters on Virtues] Ahmad Muhammad Shakir:Sahih;Al-Albani:Sahih;Bashar Awad Maarouf:Hasan;Zubair Ali Zai:Daif :: …ء يخطب فسمعته يقول  " يا أيها الناس إني قد تركت فيكم ما إن أخذتم به لن تضلوا كتاب الله وعترتي أهل بيتي " .وفي الباب عن أبي ذر وأبي سعيد وزيد بن أرقم وحذيفة بن أسيد . وهذا حديث ح…`
  - Contents of Musnad Ahmad 3786 and the Hakim/Tabarani locations: KNOWLEDGE-ONLY (research layer / audit v1.1 candidate; not verifiable from this environment) (Ahmad, Hakim and Tabarani are not in the corpus).
- **SOURCE:** al-Hakim, al-Mustadrak (CANDIDATE: 2:343 h. 3312; 3:151 h. 4720); al-Tabarani, al-Mu'jam al-Awsat (CANDIDATE 5870) and al-Kabir (CANDIDATE 2636–2638).
- **SOURCE_STATUS:** Ahmad 3786 attribution: FALSE / PRINT BLOCKED. Hakim/Tabarani: CANDIDATE, EDITION-LOCK PENDING.
- **PROPOSED_ACTION:**
  Replace the bullet with (⟦…⟧ = fill after edition lock; do not print candidate numbers before lock):
  «•  «আমার আহলুল বাইত হচ্ছে নূহ (আলাইহিস্ সালাম)-এর নৌকার মতো। যারা এতে চড়ে, তারা নাজাত পায়; যারা বিমুখ হয়, তারা ডুবে যায়।» — আল-হাকিম, আল-মুস্তাদরাক আলাস সহিহাইন, ⟦edition⟧, খণ্ড ⟦ ⟧, হাদীস ⟦ ⟧ (যাহাবীর মন্তব্যসহ ⟦ ⟧); আত-তাবারানি, আল-মু'জামুল আওসাত, হাদীস ⟦ ⟧ ও আল-মু'জামুল কাবির, হাদীস ⟦ ⟧ — PAGE-CHECK। সিহাহ সিত্তায় এই শব্দে নেই।»
  In the related prose, keep «বর্ণিত আছে» until lock. Register HAD-SAFINA (REF-191, REF-208) must use this same citation.
- **PATCH_TYPE:** REMOVE_FALSE_SOURCE + ADD_SOURCE
- **CONFIDENCE:** MEDIUM
- **REQUIRES_HUMAN_REVIEW:** YES

### PB1-007

- **PATCH_ID:** PB1-007
- **PART:** 1
- **CHAPTER:** ১১  শুনেছি মানেই কি জেনেছি?
- **PAGE:** PAGE-CHECK (docx not available); ¶815
- **PARAGRAPH/LOCATION:** Ledger REF-013 · Paragraph_Index 815 · source-note bullet (chapter source block) · register HAD-RUYA
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  «যে স্বপ্নে আমাকে দেখল সে সত্যিই আমাকে দেখল» ও স্বপ্নের তিন প্রকার — শ্রোতা ০৪-এ «আবু দাউদ, হাদিস : ৫০২১»; PAGE-CHECK।
- **PROBLEM:** Abu Dawud 5021 is Abu Qatada's «الرؤيا من الله والحلم من الشيطان» and supports neither claim (BUG-13). Live check also shows Abu Dawud 5023 reads «فسيراني في اليقظة», not «فقد رآني». The exact wording «সত্যিই আমাকে দেখল» is therefore Bukhari 110 / Muslim 2266. (The six-book report's gloss of 5023 as «فقد رآني» is inexact.)
- **EVIDENCE:**
  - `-- abudawud 5021 (num 5021/ar 5021) [General Behavior (Kitab Al-Adab)] Al-Albani:Sahih;Muhammad Muhyi Al-Din Abdul Hamid:Sahih;Zubair Ali Zai:Sahih Bukhari (6984) Sahih Muslim (2261) :: …يقول سمعت أبا سلمة، يقول سمعت أبا قتادة، يقول سمعت رسول الله صلى الله عليه وسلم يقول  " الرؤيا من الله والحلم من الشيطان فإذا رأى أحدكم شيئا يكرهه فلينفث عن يساره ثلاث مرات ثم ليتعوذ من شرها ف…`
  - `-- abudawud 5019 (num 5019/ar 5019) [General Behavior (Kitab Al-Adab)] Al-Albani:Sahih;Muhammad Muhyi Al-Din Abdul Hamid:Sahih;Zubair Ali Zai:Sahih Bukhari (7017) Sahih Muslim (2263) :: …ه عليه وسلم قال " إذا اقترب الزمان لم تكد رؤيا المؤمن أن تكذب وأصدقهم رؤيا أصدقهم حديثا والرؤيا ثلاث فالرؤيا الصالحة بشرى من الله والرؤيا تحزين من الشيطان ورؤيا مما يحدث به المرء نفسه فإذا ر…`
  - `-- abudawud 5023 (num 5023/ar 5023) [General Behavior (Kitab Al-Adab)] Al-Albani:Sahih;Muhammad Muhyi Al-Din Abdul Hamid:Sahih;Shuaib Al Arnaut:Sahih;Zubair Ali Zai:Sahih Bukhari (6993) Sahih Muslim (2266) :: …برني أبو سلمة بن عبد الرحمن، أن أبا هريرة، قال سمعت رسول الله صلى الله عليه وسلم يقول " من رآني في المنام فسيراني في اليقظة " . أو " لكأنما رآني في اليقظة ولا يتمثل الشيطان بي "…`
  - `-- bukhari 110 (num 110/ar 110) [Knowledge]  :: …صالح، عن أبي هريرة، عن النبي صلى الله عليه وسلم قال  " تسموا باسمي ولا تكتنوا بكنيتي، ومن رآني في المنام فقد رآني، فإن الشيطان لا يتمثل في صورتي، ومن كذب على متعمدا فليتبوأ مقعده من ال…`
  - `-- muslim 2266 (num 5919/ar 2266.01) [The Book of Dreams]  :: …زيد - حدثنا أيوب، وهشام، عن محمد، عن أبي هريرة، قال قال رسول الله صلى الله عليه وسلم  " من رآني في المنام فقد رآني فإن الشيطان لا يتمثل بي " .…`
  - `-- bukhari 6993 (num 6993/ar 6993) [Interpretation of Dreams]  :: …ونس، عن الزهري، حدثني أبو سلمة، أن أبا هريرة، قال سمعت النبي صلى الله عليه وسلم يقول  " من رآني في المنام فسيراني في اليقظة، ولا يتمثل الشيطان بي ". قال أبو عبد الله قال ابن سيرين إ…`
- **SOURCE:** Sahih al-Bukhari 110, 6993; Sahih Muslim 2266; Sunan Abi Dawud 5019, 5023 (all Abu Hurayra).
- **SOURCE_STATUS:** VERIFIED (live). 5021 = wrong hadith → CORRECTED.
- **PROPOSED_ACTION:**
  Replace the bullet with:
  «•  «যে স্বপ্নে আমাকে দেখল সে সত্যিই আমাকে দেখল» — সহীহ বুখারী ১১০; সহীহ মুসলিম ২২৬৬ (আবু হুরাইরা); শব্দভেদে («সে জাগ্রত অবস্থায়ও আমাকে দেখবে») সহীহ বুখারী ৬৯৯৩ ও সুনানে আবু দাউদ ৫০২৩। স্বপ্নের তিন প্রকার — সুনানে আবু দাউদ ৫০১৯ (আবু হুরাইরা)।»
  Register HAD-RUYA (REF-201) uses the same numbers.
- **PATCH_TYPE:** CORRECT_HADITH_NUMBER
- **CONFIDENCE:** HIGH
- **REQUIRES_HUMAN_REVIEW:** NO

### PB1-008

- **PATCH_ID:** PB1-008
- **PART:** 1
- **CHAPTER:** ১১  শুনেছি মানেই কি জেনেছি?
- **PAGE:** PAGE-CHECK (docx not available); ¶817
- **PARAGRAPH/LOCATION:** Ledger REF-014 · Paragraph_Index 817 · source-note bullet (chapter source block)
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  চিট লিস্টের বাণীগুলো (চিন্তাহীন ইবাদত, জ্ঞানার্জন-শিক্ষাদান, চার ব্যক্তির পুরস্কার) — শ্রোতা ০৪-এ সূত্র ছাড়া; «বর্ণিত আছে», PAGE-CHECK।
- **PROBLEM:** UNIDENTIFIED (BUG-25): no classical source located. The note is already attribution-only («বর্ণিত আছে») and carries no kitab name; prose that depends on it must not rise above «বর্ণিত আছে».
- **EVIDENCE:**
  - No source evidence exists in this repo for this row (audit v1.1 BUG-25 list). KNOWLEDGE-ONLY (research layer / audit v1.1 candidate; not verifiable from this environment).
- **SOURCE:** None located (ledger Candidate_Source: see CSV).
- **SOURCE_STATUS:** SOURCE-MISSING · বর্ণিত আছে · PRINT BLOCKED (book gate)
- **PROPOSED_ACTION:**
  Retain the current wording verbatim (no kitab name may be added). Author decides: keep as attribution-only, or delete the item (BUG-25). If a sanad is later found, re-open as ADD_SOURCE with PAGE-CHECK.
- **PATCH_TYPE:** PRESERVE_WITH_PAGE_CHECK
- **CONFIDENCE:** LOW
- **REQUIRES_HUMAN_REVIEW:** YES

---

## Part 2

### PB1-009

- **PATCH_ID:** PB1-009
- **PART:** 2
- **CHAPTER:** ০৩  ইবলিস চিনেও কেন সিজদা করল না
- **PAGE:** PAGE-CHECK (docx not available); ¶1159
- **PARAGRAPH/LOCATION:** Ledger REF-020 · Paragraph_Index 1159 · source-note bullet (chapter source block)
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  শো'বার কাহিনী — শ্রোতা ০৪-এ জনির নোট; মূল উৎস মেলানো হয়নি — «বর্ণিত আছে»।
- **PROBLEM:** UNIDENTIFIED (BUG-25): no classical source located. The note is already attribution-only («বর্ণিত আছে») and carries no kitab name; prose that depends on it must not rise above «বর্ণিত আছে».
- **EVIDENCE:**
  - No source evidence exists in this repo for this row (audit v1.1 BUG-25 list). KNOWLEDGE-ONLY (research layer / audit v1.1 candidate; not verifiable from this environment).
- **SOURCE:** None located (ledger Candidate_Source: see CSV).
- **SOURCE_STATUS:** SOURCE-MISSING · বর্ণিত আছে · PRINT BLOCKED (book gate)
- **PROPOSED_ACTION:**
  Retain the current wording verbatim (no kitab name may be added). Author decides: keep as attribution-only, or delete the item (BUG-25). If a sanad is later found, re-open as ADD_SOURCE with PAGE-CHECK.
- **PATCH_TYPE:** PRESERVE_WITH_PAGE_CHECK
- **CONFIDENCE:** LOW
- **REQUIRES_HUMAN_REVIEW:** YES

### PB1-010

- **PATCH_ID:** PB1-010
- **PART:** 2
- **CHAPTER:** ০৫  জান্নাত কি আমল দিয়ে কেনা যায়?
- **PAGE:** PAGE-CHECK (docx not available); ¶1319
- **PARAGRAPH/LOCATION:** Ledger REF-022 · Paragraph_Index 1319 · source-note bullet (chapter source block)
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  «الجنة طيبة لا يدخلها إلا الطيب» — উৎস মেলেনি; «সহিহ মুসলিম» নাম PRINT BLOCKED।
- **PROBLEM:** «الجنة طيبة لا يدخلها إلا الطيب» is not in Sahih Muslim and appears nowhere in the six books (BUG-15). The nearest canonical texts say something else and must not be swapped in: Muslim 1015 is about Allah accepting only the pure, and Tirmidhi 3462 is about the soil of Paradise.
- **EVIDENCE:**
  - `search «الجنة طيبة» (all six books) → tirmidhi ar3462`
  - `-- tirmidhi 3462 (num 3462/ar 3462) [Chapters on Supplication] Ahmad Muhammad Shakir:Hasan;Al-Albani:Hasan;Bashar Awad Maarouf:Hasan;Zubair Ali Zai:Daif :: …يه وسلم  " لقيت إبراهيم ليلة أسري بي فقال يا محمد أقرئ أمتك مني السلام وأخبرهم أن الجنة طيبة التربة عذبة الماء وأنها قيعان وأن غراسها سبحان الله والحمد لله ولا إله إلا الله والله أكبر "…`
  - `-- muslim 1015 (num 2346/ar 1015) [The Book of Zakat]  :: …ي بن ثابت، عن أبي حازم، عن أبي هريرة، قال قال رسول الله صلى الله عليه وسلم " أيها الناس إن الله طيب لا يقبل إلا طيبا وإن الله أمر المؤمنين بما أمر به المرسلين فقال { يا أيها الرسل كلوا من…`
- **SOURCE:** None in the six books for this wording.
- **SOURCE_STATUS:** «সহিহ মুসলিম» attribution: FALSE — PRINT BLOCKED. Wording: SOURCE-MISSING.
- **PROPOSED_ACTION:**
  Replace the bullet with:
  «•  «الجنة طيبة لا يدخلها إلا الطيب» — এই শব্দে সহীহ মুসলিমসহ সিহাহ সিত্তায় পাওয়া যায়নি; বর্ণিত আছে।»
  In the chapter prose (¶ near 1319; not in the ledger), delete only the book name («সহিহ মুসলিমে…») wherever it attaches to this sentence. Keep the sentence as «বর্ণিত আছে», or (author's decision) drop the sentence. Do NOT substitute Muslim 1015 or Tirmidhi 3462, because their meaning is different.
- **PATCH_TYPE:** REMOVE_FALSE_SOURCE
- **CONFIDENCE:** HIGH
- **REQUIRES_HUMAN_REVIEW:** YES

### PB1-011

- **PATCH_ID:** PB1-011
- **PART:** 2
- **CHAPTER:** ০৬  আল্লাহর কাছে না পৌঁছানো নামাজ
- **PAGE:** PAGE-CHECK (docx not available); ¶1636
- **PARAGRAPH/LOCATION:** Ledger REF-039 · Paragraph_Index 1636 · source-note bullet (chapter source block)
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  শয়তান রক্তের পথে চলে (অংশ ১১৮): «إن الشيطان يجري من ابن آدم مجرى الدم», সহিহ বুখারী (সাফিয়্যার ঘটনা; যেমন হাদিস ৭১৭১) ও সহিহ মুসলিম, হাদিস ২১৭৫ (নম্বর PAGE-CHECK)। https://hadithprophet.com/hadith-37589.html
- **PROBLEM:** The quoted wording «يجري من ابن آدم مجرى الدم» is Bukhari 7171's. Muslim 2175 has two wordings: 2175a «يجري من الإنسان مجرى الدم» and 2175b «يبلغ من الإنسان مبلغ الدم». Audit BUG-30 gives only the second, so it is imprecise. The book should quote the wording of the hadith it cites.
- **EVIDENCE:**
  - `-- bukhari 7171 (num 7171/ar 7171) [Judgments (Ahkaam)]  :: …دعاهما فقال " إنما هي صفية ". قالا سبحان الله. قال " إن الشيطان يجري من ابن آدم مجرى الدم ". رواه شعيب وابن مسافر وابن أبي عتيق وإسحاق بن يحيى عن الزهري عن علي يعني ابن حسين…`
  - `-- muslim 2175 (num 5679/ar 2175.01) [The Book of Greetings]  :: …على رسلكما إنها صفية بنت حيى " . فقالا سبحان الله يا رسول الله . قال " إن الشيطان يجري من الإنسان مجرى الدم وإني خشيت أن يقذف في قلوبكما شرا " . أو قال " شيئا " .…`
  - `-- muslim 2175 (num 5680/ar 2175.02) [The Book of Greetings]  :: …قلبها . ثم ذكر بمعنى حديث معمر غير أنه قال فقال النبي صلى الله عليه وسلم " إن الشيطان يبلغ من الإنسان مبلغ الدم " . ولم يقل " يجري " .…`
- **SOURCE:** Sahih al-Bukhari 7171 (also 2035, 2038, 3101, 3281, 6219); Sahih Muslim 2175.
- **SOURCE_STATUS:** VERIFIED (live).
- **PROPOSED_ACTION:**
  Replace the bullet with:
  «•  শয়তান রক্তের পথে চলে (অংশ ১১৮): «إن الشيطان يجري من ابن آدم مجرى الدم» — সহিহ বুখারী ৭১৭১ (সাফিয়্যার ঘটনা; এই শব্দে); সহিহ মুসলিম ২১৭৫ (প্রথম বর্ণনায় «يجري من الإنسان مجرى الدم», দ্বিতীয় বর্ণনায় «يبلغ من الإنسان مبلغ الدم»)। https://hadithprophet.com/hadith-37589.html»
- **PATCH_TYPE:** CORRECT_CITATION
- **CONFIDENCE:** HIGH
- **REQUIRES_HUMAN_REVIEW:** NO

### PB1-012

- **PATCH_ID:** PB1-012
- **PART:** 2
- **CHAPTER:** ০৬  আল্লাহর কাছে না পৌঁছানো নামাজ
- **PAGE:** PAGE-CHECK (docx not available); ¶1638
- **PARAGRAPH/LOCATION:** Ledger REF-041 · Paragraph_Index 1638 · source-note bullet (chapter source block) · register HAD-NUR-AWWAL
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  নূরের প্রথম সৃষ্টি (অংশ ১২৬): «বর্ণিত আছে»; সনদসহ উৎস এই অধ্যায়ে দেওয়া হয়নি।
- **PROBLEM:** UNIDENTIFIED (BUG-25): no classical source located. The note is already attribution-only («বর্ণিত আছে») and carries no kitab name; prose that depends on it must not rise above «বর্ণিত আছে». Register HAD-NUR-AWWAL: normalise with REF-154 / REF-244 (all attribution-only).
- **EVIDENCE:**
  - No source evidence exists in this repo for this row (audit v1.1 BUG-25 list). KNOWLEDGE-ONLY (research layer / audit v1.1 candidate; not verifiable from this environment).
- **SOURCE:** None located (ledger Candidate_Source: see CSV).
- **SOURCE_STATUS:** SOURCE-MISSING · বর্ণিত আছে · PRINT BLOCKED (book gate)
- **PROPOSED_ACTION:**
  Retain the current wording verbatim (no kitab name may be added). Author decides: keep as attribution-only, or delete the item (BUG-25). If a sanad is later found, re-open as ADD_SOURCE with PAGE-CHECK.
- **PATCH_TYPE:** PRESERVE_WITH_PAGE_CHECK
- **CONFIDENCE:** LOW
- **REQUIRES_HUMAN_REVIEW:** YES

### PB1-013

- **PATCH_ID:** PB1-013
- **PART:** 2
- **CHAPTER:** ০৭  রাত পর্যন্ত: কুরআনের আলোকে ইফতার
- **PAGE:** PAGE-CHECK (docx not available); ¶1885
- **PARAGRAPH/LOCATION:** Ledger REF-049 · Paragraph_Index 1885 · source-note bullet (chapter source block) · register HAD-IFTAR-TAMR
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  উমর ও উসমানের ইফতার: মুয়াত্তা ইমাম মালিক, কিতাবুস সিয়াম (লেখকের ব্যবহৃত বাংলা সংস্করণে ১ম খণ্ড, পৃ. ২৩৯, হাদীস ৬৯৪)। «যখন পূর্ব দিক থেকে অন্ধকার আসে…»: সহীহ বুখারী, কিতাবুস সাওম, উমর ইবনুল খাত্তাবের সূত্রে (লেখকের ব্যবহৃত আধুনিক প্রকাশনী সংস্করণে হাদীস ১৮১৫)। আনাসের দুধের ঘটনা: মূল আরবি, মাকারিমুল আখলাক (তাবরিসি), রাসূলুল্লাহ ﷺ-এর পানীয় অধ্যায়, আনাসের নিজের ভাষায়; অধ্যায়ে ঘটনাটি শুধু এই আরবি পাঠ অনুযায়ী বলা হয়েছে (আনাস রাতভর আশঙ্কা করেছিলেন রাসূলুল্লাহ ﷺ হয়তো না খেয়ে রাত কাটাবেন; তিনি কখনো এ বিষয়ে জিজ্ঞেস বা উল্লেখ করেননি)। এছাড়া: সত্য কাহিনী সম্ভার (শহীদ মুতাহহারির দাস্তানে রাস্তান-এর বাংলা অনুবাদ), ‘ইফতারি’; মূল: মাকারিমুল আখলাক (তাবরিসি), রাসূলুল্লাহ ﷺ-এর পানীয় অধ্যায়; কুহলুল বাসার পৃ. ৬৭। পানি বা খেজুর দিয়ে রোযা খোলার কথা (অংশ ১১৭গ) «বর্ণিত আছে» বলে রাখা হয়েছে; মূল কিতাবের সূত্র এখনো মেলানো হয়নি।
  Relevant clause: «সহীহ বুখারী, কিতাবুস সাওম, উমর ইবনুল খাত্তাবের সূত্রে (লেখকের ব্যবহৃত আধুনিক প্রকাশনী সংস্করণে হাদীস ১৮১৫)»
  Relevant clause: «পানি বা খেজুর দিয়ে রোযা খোলার কথা (অংশ ১১৭গ) «বর্ণিত আছে» বলে রাখা হয়েছে; মূল কিতাবের সূত্র এখনো মেলানো হয়নি।»
- **PROBLEM:** «১৮১৫» is a Bengali (Adhunik Prokashoni) edition number used as if it were standard (BUG-12). The standard number is 1954, identified by its text. Separately, the dates/water clause is left as «বর্ণিত আছে» although the six books carry it. The command form the prose uses («খুলতে বলেছেন») is Abu Dawud 2355, and its graders disagree.
- **EVIDENCE:**
  - `-- bukhari 1954 (num 1954/ar 1954) [Fasting]  :: …لى الله عليه وسلم  " إذا أقبل الليل من ها هنا، وأدبر النهار من ها هنا، وغربت الشمس، فقد أفطر الصائم ".…`
  - `-- abudawud 2355 (num 2355/ar 2355) [Fasting (Kitab Al-Siyam)] Al-Albani:Daif;Muhammad Muhyi Al-Din Abdul Hamid:Daif;Shuaib Al Arnaut:Hasan Sahih;Zubair Ali Zai:Isnaad Sahih :: …باب، عن سلمان بن عامر، عمها قال قال رسول الله صلى الله عليه وسلم  " إذا كان أحدكم صائما فليفطر على التمر فإن لم يجد التمر فعلى الماء فإن الماء طهور " .…`
  - `-- abudawud 2356 (num 2356/ar 2356) [Fasting (Kitab Al-Siyam)] Al-Albani:Hasan Sahih;Muhammad Muhyi Al-Din Abdul Hamid:Hasan Sahih;Shuaib Al Arnaut:Sahih;Zubair Ali Zai:Isnaad Hasan :: …، حدثنا ثابت البناني، أنه سمع أنس بن مالك، يقول كان رسول الله صلى الله عليه وسلم يفطر على رطبات قبل أن يصلي فإن لم تكن رطبات فعلى تمرات فإن لم تكن حسا حسوات من ماء .…`
- **SOURCE:** Sahih al-Bukhari 1954 (Umar); Sunan Abi Dawud 2355 (Salman b. Amir, command), 2356 (Anas, practice). Muwatta' Bengali-edition reference stays as written (edition explicit).
- **SOURCE_STATUS:** VERIFIED (live). 2355: Albani da'if / Arna'ut hasan sahih / Zubair isnad sahih (disputed). 2356: hasan sahih.
- **PROPOSED_ACTION:**
  In the bullet, replace the clause «সহীহ বুখারী, কিতাবুস সাওম, উমর ইবনুল খাত্তাবের সূত্রে (লেখকের ব্যবহৃত আধুনিক প্রকাশনী সংস্করণে হাদীস ১৮১৫)» with:
  «সহীহ বুখারী, কিতাবুস সাওম, হাদীস ১৯৫৪ (আন্তর্জাতিক ক্রম; লেখকের ব্যবহৃত আধুনিক প্রকাশনী সংস্করণে ১৮১৫), উমর ইবনুল খাত্তাবের সূত্রে»
  and replace the closing clause «পানি বা খেজুর দিয়ে রোযা খোলার কথা (অংশ ১১৭গ) «বর্ণিত আছে» বলে রাখা হয়েছে; মূল কিতাবের সূত্র এখনো মেলানো হয়নি।» with:
  «পানি বা খেজুর দিয়ে রোযা খোলার কথা (অংশ ১১৭গ) — সুনানে আবু দাউদ ২৩৫৫ (সালমান ইবনে আমির; নির্দেশ হিসেবে; মান নিয়ে মতভেদ: আলবানী: যয়ীফ, শুআইব আরনাউত: হাসান সহিহ) ও ২৩৫৬ (আনাস; রাসূলুল্লাহ ﷺ-এর আমল হিসেবে; আলবানী: হাসান সহিহ)।»
  Prose REF-048 can keep «বর্ণিত আছে».
- **PATCH_TYPE:** CORRECT_HADITH_NUMBER + ADD_SOURCE
- **CONFIDENCE:** HIGH
- **REQUIRES_HUMAN_REVIEW:** YES

---

## Part 3

### PB1-014

- **PATCH_ID:** PB1-014
- **PART:** 3
- **CHAPTER:** ০৪  ঘরের ভেতরে ইসার আর ভালোবাসা
- **PAGE:** PAGE-CHECK (docx not available); ¶2648
- **PARAGRAPH/LOCATION:** Ledger REF-071 · Paragraph_Index 2648 · source-note bullet (chapter source block)
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  «فداك أبي وأمي» ও সফরের শুরু-শেষ ফাতিমার কাছে (ইবনে উমর; সাওবান) — সাওবানের বর্ণনা: সুনানে আবু দাউদ, কিতাবুত তারাজ্জুল, হাদীস ৪২১৩ — PAGE-CHECK; ইবনে উমরের বর্ণনা ও «ফাদাকি আবি ওয়া উম্মি» — হাকিম, আল-মুস্তাদরাক — PAGE-CHECK। ইবনে আব্বাসের চুমুর বর্ণনা — বর্ণিত আছে।
  Relevant clause: «সাওবানের বর্ণনা: সুনানে আবু দাউদ, কিতাবুত তারাজ্জুল, হাদীস ৪২১৩ — PAGE-CHECK»
- **PROBLEM:** Abu Dawud 4213 is the right number, but every grader in the corpus calls it weak, and no grade is printed (BUG-22).
- **EVIDENCE:**
  - `-- abudawud 4213 (num 4213/ar 4213) [Combing the Hair (Kitab Al-Taraj] Al-Albani:Daif Isnaad;Muhammad Muhyi Al-Din Abdul Hamid:Daif Isnaad;Shuaib Al Arnaut:Daif;Zubair Ali Zai:Daif :: …الله عليه وسلم قال كان رسول الله صلى الله عليه وسلم إذا سافر كان آخر عهده بإنسان من أهله فاطمة وأول من يدخل عليها إذا قدم فاطمة فقدم من غزاة له وقد علقت مسحا أو سترا على بابها وحلت الح…`
- **SOURCE:** Sunan Abi Dawud 4213 (Thawban), Kitab al-Tarajjul.
- **SOURCE_STATUS:** VERIFIED (live); da'if (Albani «Daif Isnaad», Abd al-Hamid «Daif Isnaad», Arna'ut, Zubair Ali Zai). Hakim part: CANDIDATE, number lock (BUG-21).
- **PROPOSED_ACTION:**
  In the bullet, replace «সাওবানের বর্ণনা: সুনানে আবু দাউদ, কিতাবুত তারাজ্জুল, হাদীস ৪২১৩ — PAGE-CHECK» with:
  «সাওবানের বর্ণনা: সুনানে আবু দাউদ, কিতাবুত তারাজ্জুল, হাদীস ৪২১৩ (সনদ দুর্বল — আলবানী: «ضعيف الإسناد»; শুআইব আরনাউত ও যুবাইর আলী যাঈ: যয়ীফ)»
  The rest of the bullet is unchanged. Wherever the prose near ¶2648 uses Thawban's report, it must not stand as a flat «রাসূলুল্লাহ ﷺ…» without «বর্ণিত আছে».
- **PATCH_TYPE:** CORRECT_CITATION
- **CONFIDENCE:** HIGH
- **REQUIRES_HUMAN_REVIEW:** NO

### PB1-015

- **PATCH_ID:** PB1-015
- **PART:** 3
- **CHAPTER:** ০৪  ঘরের ভেতরে ইসার আর ভালোবাসা
- **PAGE:** PAGE-CHECK (docx not available); ¶2650
- **PARAGRAPH/LOCATION:** Ledger REF-073 · Paragraph_Index 2650 · source-note bullet (chapter source block) · register HAD-AHABB-FATIMA
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  জুমাই ইবনে উমায়রের বর্ণনা (আয়েশা: ফাতিমা, পুরুষে তাঁর স্বামী) — সুনানে তিরমিযি, কিতাবুল মানাকিব, হাদীস ৩৮৭৪ — PAGE-CHECK। বুরাইদার বর্ণনা — তিরমিযি ৩৮৬৮ — PAGE-CHECK। উসামার বর্ণনা («ফাতিমা বিনতে মুহাম্মদ») — তিরমিযি ৩৮১৯ — PAGE-CHECK। আবু হুরাইরা ও কুফার মিম্বরের বর্ণনা («সে তোমার চেয়ে প্রিয়, তুমি তার চেয়ে স্নেহশীল») — বর্ণিত আছে (তাবারানি, আল-মু'জামুল আওসাত — PAGE-CHECK)।
- **PROBLEM:** The numbers are right, but two of the reports are MUNKAR (Tirmidhi 3874 and 3868, per al-Albani and Shakir), and 3819 is weak with graders disagreeing. No grade is printed (BUG-22, print-safety).
- **EVIDENCE:**
  - `-- tirmidhi 3874 (num 3874/ar 3874) [Chapters on Virtues] Ahmad Muhammad Shakir:Munkar;Al-Albani:Munkar;Zubair Ali Zai:Daif :: …حرب، عن أبي الجحاف، عن جميع بن عمير التيمي، قال دخلت مع عمتي على عائشة فسئلت أى الناس كان أحب إلى رسول الله صلى الله عليه وسلم قالت فاطمة . فقيل من الرجال قالت زوجها إن كان ما علمت…`
  - `-- tirmidhi 3868 (num 3868/ar 3868) [Chapters on Virtues] Ahmad Muhammad Shakir:Munkar;Al-Albani:Munkar;Zubair Ali Zai:Daif :: …حدثنا الأسود بن عامر، عن جعفر الأحمر، عن عبد الله بن عطاء، عن ابن بريدة، عن أبيه، قال كان أحب النساء إلى رسول الله صلى الله عليه وسلم فاطمة ومن الرجال علي . قال إبراهيم بن سعيد يعني من أهل…`
  - `-- tirmidhi 3819 (num 3819/ar 3819) [Chapters on Virtues] Ahmad Muhammad Shakir:Daif;Al-Albani:Daif;Bashar Awad Maarouf:Daif;Zubair Ali Zai:Isnaad Hasan :: …لكني أدري " . فأذن لهما فدخلا فقالا يا رسول الله جئناك نسألك أى أهلك أحب إليك قال " فاطمة بنت محمد " . فقالا ما جئناك نسألك عن أهلك . قال " أحب أهلي إلى من قد أنعم الله عليه وأنعمت…`
- **SOURCE:** Jami' al-Tirmidhi 3874 (Jumay' b. Umayr), 3868 (Buraydah), 3819 (Usama b. Zayd).
- **SOURCE_STATUS:** VERIFIED (live). 3874, 3868: munkar (Albani, Shakir) / da'if (Zubair). 3819: da'if (Albani, Shakir, Bashar) / isnad hasan (Zubair). Tabarani part: CANDIDATE.
- **PROPOSED_ACTION:**
  Replace the bullet with:
  «•  জুমাই ইবনে উমায়রের বর্ণনা (আয়েশা: ফাতিমা, পুরুষে তাঁর স্বামী) — সুনানে তিরমিযি, কিতাবুল মানাকিব, হাদীস ৩৮৭৪ (আলবানী ও আহমাদ শাকির: মুনকার; যুবাইর আলী যাঈ: যয়ীফ)। বুরাইদার বর্ণনা — তিরমিযি ৩৮৬৮ (আলবানী ও আহমাদ শাকির: মুনকার; যুবাইর আলী যাঈ: যয়ীফ)। উসামার বর্ণনা («ফাতিমা বিনতে মুহাম্মদ») — তিরমিযি ৩৮১৯ (মান নিয়ে মতভেদ: আলবানী, শাকির ও বাশশার আওয়াদ: যয়ীফ; যুবাইর আলী যাঈ: সনদ হাসান)। আবু হুরাইরা ও কুফার মিম্বরের বর্ণনা («সে তোমার চেয়ে প্রিয়, তুমি তার চেয়ে স্নেহশীল») — বর্ণিত আছে (তাবারানি, আল-মু'জামুল আওসাত — PAGE-CHECK)।»
  If the prose of Part 3 Ch 04 (near ¶2650) renders the Buraydah or Jumay' report as a flat «রাসূলুল্লাহ ﷺ…» or «সহিহ হাদিসে», change only the attribution clause, e.g. «তিরমিযির একটি বর্ণনায় (সনদ মুনকার)».
- **PATCH_TYPE:** CORRECT_CITATION
- **CONFIDENCE:** HIGH
- **REQUIRES_HUMAN_REVIEW:** YES

### PB1-016

- **PATCH_ID:** PB1-016
- **PART:** 3
- **CHAPTER:** ০৪  ঘরের ভেতরে ইসার আর ভালোবাসা
- **PAGE:** PAGE-CHECK (docx not available); ¶2651
- **PARAGRAPH/LOCATION:** Ledger REF-074 · Paragraph_Index 2651 · source-note bullet (chapter source block) · register LIT-IQBAL
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  ফারসি কবিতা (খাতা ¶5003–5004): «مادی آن مرکز پرکار عشق / مادری آن کاروان سالار عشق» — খাতার বানান হুবহু; প্রথম শব্দ সম্ভবত «مادر» (ইকবাল, রুমুযে বেখুদি — PAGE-CHECK)।
- **PROBLEM:** The note reproduces the notebook's misspelling «مادی». The poem is Iqbal's, and line 1 (and, per the research layer, line 2) begins «مادر» (BUG-24). There is no edition page.
- **EVIDENCE:**
  - Identification (Iqbal, Rumuz-e Bekhudi, section on Sayyida Fatima) and the reading «مادر»: KNOWLEDGE-ONLY (research layer / audit v1.1 candidate; not verifiable from this environment). No Persian corpus in this repo.
- **SOURCE:** Muhammad Iqbal, Rumuz-e Bekhudi, section on Sayyida Fatima (edition to choose).
- **SOURCE_STATUS:** CANDIDATE — EDITION-LOCK PENDING.
- **PROPOSED_ACTION:**
  Replace the bullet with:
  «•  ফারসি কবিতা: «مادر آن مرکز پرکار عشق / مادر آن کاروان سالار عشق» — মুহাম্মাদ ইকবাল, রুমুযে বেখুদি (মা সাইয়্যিদা ফাতিমা অংশ), ⟦edition⟧, পৃ. ⟦ ⟧ — PAGE-CHECK।»
  Apply the same spelling fix to the poem wherever it appears in the prose, after checking it against the chosen printed edition. If the edition reads line 2 differently, follow the edition.
- **PATCH_TYPE:** CORRECT_CITATION
- **CONFIDENCE:** MEDIUM
- **REQUIRES_HUMAN_REVIEW:** YES

### PB1-017

- **PATCH_ID:** PB1-017
- **PART:** 3
- **CHAPTER:** ০৫  “রাদিয়াল্লাহু আনহা”, নাকি “আলাইহাস্ সালাম”?
- **PAGE:** PAGE-CHECK (docx not available); ¶2730
- **PARAGRAPH/LOCATION:** Ledger REF-075 · Paragraph_Index 2730 · source-note bullet (chapter source block)
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  প্রমাণ ০১–০৪: সহীহ বুখারির আরবিতে «فَاطِمَةَ عَلَيْهَا السَّلاَمُ» — খাতার বাংলা-সংস্করণ নম্বর ২৮৭৪, ৩৪৪৬, ৬২৭০, ৪৯৬ — PAGE-CHECK (ছাপা ও ক্রমিক অনুযায়ী নম্বর বদলায়; sunnah.com নম্বর মেলাতে হবে)। প্রমাণ-০৪-এর আরবি অংশ: «…عَلَيْهَا السَّلاَمُ ـ وَهْىَ جُوَيْرِيَةٌ، فَأَقْبَلَتْ تَسْعَى…»।
- **PROBLEM:** Four Bengali-edition numbers are presented as if they were Bukhari numbers (BUG-12). Live text search finds that proof-04's Arabic («وهي جويرية فأقبلت تسعى») occurs in exactly one Bukhari hadith, 520. Triage v1.2 maps it to 3110, which is WRONG. Proofs 01–03 cannot be mapped without their texts.
- **EVIDENCE:**
  - `-- bukhari 520 (num 520/ar 520) [Prayers (Salat)]  :: …فضحكوا حتى مال بعضهم إلى بعض من الضحك، فانطلق منطلق إلى فاطمة عليها السلام وهى جويرية، فأقبلت تسعى وثبت النبي صلى الله عليه وسلم ساجدا حتى ألقته عنه، وأقبلت عليهم تسبهم، فلما قضى رسول الله…`
  - corpus scan (verify_sunni.py data, regex «فاطمة\s+عليها\s+السلام» over Bukhari) → 29 hadiths: 520, 2089, 2699, 2911, 3092, 3093, 3110, 3113, 3185, 3711, 3712, 3854, 4003, 4035, 4036, 4075, 4240, 4241, 4251, 4433, 4434, 4462, 5248, 5362, 5722, 6280, 6285, 6286, 7347; «فأقبلت تسعى» occurs only in 520.
- **SOURCE:** Sahih al-Bukhari 520 (Ibn Mas'ud; Kitab al-Salat) for proof-04; proofs 01–03: standard numbers to be chosen from the 29-hadith list.
- **SOURCE_STATUS:** Proof-04: VERIFIED (live text match). Mapping of ৪৯৬→520 follows the order of the notebook list (assumed). Proofs 01–03: PAGE-CHECK.
- **PROPOSED_ACTION:**
  Replace the bullet with:
  «•  প্রমাণ ০১–০৪: সহীহ বুখারির আরবিতে «فَاطِمَةَ عَلَيْهَا السَّلاَمُ» — প্রমাণ-০৪: সহীহ বুখারি ৫২০ (আন্তর্জাতিক ক্রম; খাতার বাংলা-সংস্করণে ৪৯৬), আরবি অংশ: «…عَلَيْهَا السَّلاَمُ ـ وَهْىَ جُوَيْرِيَةٌ، فَأَقْبَلَتْ تَسْعَى…»। প্রমাণ ০১–০৩: খাতার বাংলা-সংস্করণ নম্বর ২৮৭৪, ৩৪৪৬, ৬২৭০ — আন্তর্জাতিক নম্বর ⟦ ⟧, ⟦ ⟧, ⟦ ⟧ — PAGE-CHECK।»
  Editor: take each proof's Arabic from the notebook and match it against the 29-hadith list in EVIDENCE. Correct triage v1.2 / ledger Candidate_Source (3110 → 520).
- **PATCH_TYPE:** CORRECT_HADITH_NUMBER
- **CONFIDENCE:** HIGH
- **REQUIRES_HUMAN_REVIEW:** YES

### PB1-018

- **PATCH_ID:** PB1-018
- **PART:** 3
- **CHAPTER:** ০৬  ফাদাক, আর চুপ না থাকার সাহস
- **PAGE:** PAGE-CHECK (docx not available); ¶2762
- **PARAGRAPH/LOCATION:** Ledger REF-078 · Paragraph_Index 2762 · prose / dialogue line · register HAD-FADAK-TESTIMONY
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > ভাঙা কাপটা তিনি নিজের হাতে রাখলেন। এক চুমুক দিলেন। তারপর বললেন, "এক নম্বর কথা। রাসূলুল্লাহ ﷺ নিজে মেয়েকে ফাদাক দিয়ে গেছেন। বর্ণিত আছে, লিখেও দিয়ে গেছেন। যাঁর কথা কুরআনের পরেই চূড়ান্ত, তাঁর দেওয়া জিনিসের জন্য আবার সাক্ষী লাগবে? এটা মেয়ের জন্য অপমান না?"
  Relevant clause: «বর্ণিত আছে, লিখেও দিয়ে গেছেন।»
- **PROBLEM:** The dialogue joins two claims. (1) The Prophet gave Fadak to his daughter: the 17:26 reports, register HAD-FADAK-1726 (REF-121/136/137/138; CANDIDATE). (2) «বর্ণিত আছে, লিখেও দিয়ে গেছেন», which makes the PROPHET the writer of a deed. The ledger resolution maps clause 2 to the al-Ihtijaj recension. There, however, ABU BAKR writes the deed and Umar later takes and tears it. S-181 documents no report of the Prophet himself writing a Fadak deed. The source block therefore cannot borrow the Ihtijaj deed for this clause (confirmed by the Fadak/Umm Ayman verification agent).
- **EVIDENCE:**
  - sources/S-181_UMM_AYMAN_FADAK_VERIFICATION.md §3-D: al-Ihtijaj 1 — «فكتب لها كتابا ودفعه إليها» (writer = Abu Bakr), then Umar takes/tears it; URLs https://www.almerja.com/reading.php?idm=124286 · https://ablibrary.net/book_content/b/11726/191
  - manuscript-patches/B1_P03_C06_FADAK_S-181_PATCH.md A-3 / B («আবু বকর দলিল লেখেন; উমর ছিঁড়ে ফেলেন»).
  - Prophet-wrote-a-deed report: not found in S-181 — NOT FOUND ≠ DOES NOT EXIST.
- **SOURCE:** Clause 1: al-Durr al-Manthur 4:177 on 17:26 / al-Kafi 1:543 h. 5 (CANDIDATE, register HAD-FADAK-1726). Clause 2: no located source for a Prophet-written deed; al-Tabrisi, al-Ihtijaj 1 covers only an Abu-Bakr-written deed (Shia).
- **SOURCE_STATUS:** Clause 1: CANDIDATE — PAGE-CHECK. Clause 2: SOURCE-MISSING — PAGE-CHECK. Ihtijaj deed: VERIFIED as that work's narration (S-181), EDITION-LOCK PENDING.
- **PROPOSED_ACTION:**
  Dialogue voice is kept. Change only the attribution clause, choosing one option (author):
  (a) WEAKEN, keeping the subject: «বর্ণিত আছে, লিখেও দিয়ে গেছেন।» stays, and the chapter source block (¶ near 2814–2817) gets a separate bullet:
  «•  রাসূলুল্লাহ ﷺ নিজে ফাদাকের দলিল লিখে দিয়েছিলেন — বর্ণিত আছে; সূত্র পাওয়া যায়নি — PAGE-CHECK। (আল-ইহতিজাজে যে দলিলের কথা আছে, সেটি আবু বকরের লেখা; দেখুন পরের টীকা।)»
  (b) SPLIT, aligning the clause with the located Shia recension: «শিয়া বর্ণনায় আছে, পরে দলিলও লেখা হয়েছিল।» with the source block citing al-Tabrisi, al-Ihtijaj, খণ্ড ১ ⟦edition, পৃ.⟧ (আবু বকর দলিল লেখেন; উমর ছিঁড়ে ফেলেন) — PAGE-CHECK.
  Under either option, never cite al-Ihtijaj for a deed written by the Prophet, and never merge the Ihtijaj recension with Baladhuri's (S-181 §3-F).
- **PATCH_TYPE:** SPLIT_CLAIM + WEAKEN_ATTRIBUTION
- **CONFIDENCE:** MEDIUM
- **REQUIRES_HUMAN_REVIEW:** YES

### PB1-019

- **PATCH_ID:** PB1-019
- **PART:** 3
- **CHAPTER:** ০৬  ফাদাক, আর চুপ না থাকার সাহস
- **PAGE:** PAGE-CHECK (docx not available); ¶2814
- **PARAGRAPH/LOCATION:** Ledger REF-079 · Paragraph_Index 2814 · source-note bullet (chapter source block) · register HAD-BUKHARI-4240
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  প্রমাণ ০৫–০৭ (খাতা ¶1870–1886): সহীহ বুখারি ৪২৪০–৪২৪১ (ফাতিমা আলাইহাস সালাম মদিনা, ফাদাক ও খাইবারের খুমুসের অবশিষ্ট থেকে মিরাস চাইলেন; «فَأَبَى أَبُو بَكْرٍ أَنْ يَدْفَعَ إِلَى فَاطِمَةَ…») — বাইবেল §৪-এ ৪২৪০ উল্লিখিত, CONFIRMED (একবচন «فهجرته»)। সুনানে আবু দাউদ ২৯৬৮ (একই ঘটনা, «فَاطِمَةَ عَلَيْهَا السَّلَام») ও ২৯৭২ (উমর ইবনে আব্দুল আযীযের ফাদাক ফেরত; আবু দাউদের মতে «ضعيف») — PAGE-CHECK।
  Relevant clause: «ও ২৯৭২ (উমর ইবনে আব্দুল আযীযের ফাদাক ফেরত; আবু দাউদের মতে «ضعيف») — PAGE-CHECK।»
- **PROBLEM:** The note says «আবু দাউদের মতে «ضعيف»» for 2972. The grade belongs to al-Albani (also Abd al-Hamid and Zubair), not to Abu Dawud himself (BUG-01). Both numbers are verified, so the PAGE-CHECK on them is cleared.
- **EVIDENCE:**
  - `-- abudawud 2972 (num 2972/ar 2972) [Tribute, Spoils, and Rulership (] Al-Albani:Daif;Muhammad Muhyi Al-Din Abdul Hamid:Daif;Zubair Ali Zai:Daif :: …ل جمع عمر بن عبد العزيز بني مروان حين استخلف فقال إن رسول الله صلى الله عليه وسلم كانت له فدك فكان ينفق منها ويعود منها على صغير بني هاشم ويزوج منها أيمهم وإن فاطمة سألته أن يجعلها له…`
  - `-- abudawud 2968 (num 2968/ar 2968) [Tribute, Spoils, and Rulership (] Al-Albani:Sahih;Muhammad Muhyi Al-Din Abdul Hamid:Sahih;Shuaib Al Arnaut:Sahih;Zubair Ali Zai:Sahih Bukhari (4240، 4241) Sahih Muslim (1759) :: …ق رضى الله عنه تسأله ميراثها من رسول الله صلى الله عليه وسلم مما أفاء الله عليه بالمدينة وفدك وما بقي من خمس خيبر . فقال أبو بكر إن رسول الله صلى الله عليه وسلم قال  " لا نورث ما…`
  - `-- bukhari 4240 (num 4240/ar 4240) []  :: …لى الله عليه وسلم فأبى أبو بكر أن يدفع إلى فاطمة منها شيئا فوجدت فاطمة على أبي بكر في ذلك فهجرته، فلم تكلمه حتى توفيت، وعاشت بعد النبي صلى الله عليه وسلم ستة أشهر، فلما توفيت، دفنها زوجه…`
  - sources/S-181_UMM_AYMAN_FADAK_VERIFICATION.md §4 last row; manuscript-patches/B1_P03_C06_FADAK_S-181_PATCH.md B bullet 5.
- **SOURCE:** Sunan Abi Dawud 2968, 2972; Sahih al-Bukhari 4240–4241.
- **SOURCE_STATUS:** VERIFIED (numbers + text, live); GRADING CORRECTED.
- **PROPOSED_ACTION:**
  In the bullet, replace «ও ২৯৭২ (উমর ইবনে আব্দুল আযীযের ফাদাক ফেরত; আবু দাউদের মতে «ضعيف») — PAGE-CHECK।» with:
  «ও ২৯৭২ (উমর ইবনে আব্দুল আযীযের ফাদাক ফেরত; আল-আলবানীর মতে «ضعيف» — আবু দাউদের নিজের মত হিসেবে নয়) — নম্বর ও পাঠ CONFIRMED।»
  The rest of the bullet is unchanged.
- **PATCH_TYPE:** CORRECT_CITATION
- **CONFIDENCE:** HIGH
- **REQUIRES_HUMAN_REVIEW:** NO

### PB1-020

- **PATCH_ID:** PB1-020
- **PART:** 3
- **CHAPTER:** ০৬  ফাদাক, আর চুপ না থাকার সাহস
- **PAGE:** PAGE-CHECK (docx not available); ¶2816
- **PARAGRAPH/LOCATION:** Ledger REF-081 · Paragraph_Index 2816 · source-note bullet (chapter source block) · register HAD-FADAK-TESTIMONY
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  উম্মে আইমানের সাক্ষ্য, আলী (আলাইহিস্ সালাম)-এর সাক্ষ্য, মসজিদে আবু বকরের সাথে বিতর্ক, আউস ইবনুল হাদাসান — কিতাবু সুলাইম ইবনে কায়স; আত-তাবারসি, আল-ইহতিজাজ, খণ্ড ১ — PAGE-CHECK; খাতার নিজের নোট অনুযায়ী আউসের বিবরণ আলাদাভাবে মেলানো যায়নি, তাই ছাপার আগে পর্যন্ত «বর্ণিত আছে»।
- **PROBLEM:** One bullet merges three things: Umm Ayman's and Ali's testimony, the Sunni and Shia recensions, and Aus ibn al-Hadathan. Aus is NOT Umm Ayman's witness; he belongs to the counter-testimony on «لا نورث», with Aisha and Hafsa. Baladhuri (Sunni) and al-Ihtijaj (Shia) tell the event differently and must stay separate. Also do not confuse the Shia-chain witness Aus ibn al-Hadathan with Malik b. Aws b. al-Hadathan, the Sunni narrator of the Fadak/«لا نورث» dispute in Bukhari 3094 / Muslim 1757 (live). They are different people in different chains.
- **EVIDENCE:**
  - `-- bukhari 3094 (num 3094/ar 3094) [One-fifth of Booty to the Cause ]  :: …حدثنا إسحاق بن محمد الفروي، حدثنا مالك بن أنس، عن ابن شهاب، عن مالك بن أوس بن الحدثان،، وكان، محمد بن جبير ذكر لي ذكرا من حديثه ذلك، فانطلقت حتى أدخل على مالك بن أو…`
  - `-- muslim 1757 (num 4575/ar 1757.01) [The Book of Jihad and Expedition]  :: …واللفظ لابن أبي شيبة - قال إسحاق أخبرنا وقال الآخرون، حدثنا سفيان، عن عمرو، عن الزهري، عن مالك بن أوس، عن عمر، قال كانت أموال بني النضير مما أفاء الله على رسوله مما لم يوجف عليه المسلمون بخيل…`
  - sources/S-181_UMM_AYMAN_FADAK_VERIFICATION.md §3-A Baladhuri: https://ablibrary.net/book_content/b/2660/75 · https://najafdesertlibrary.com/book/فتوح-البلدان/v/1/p/75
  - sources/S-181_UMM_AYMAN_FADAK_VERIFICATION.md §3-B Aus: https://ablibrary.net/book_content/b/8597/96
  - sources/S-181_UMM_AYMAN_FADAK_VERIFICATION.md §3-C Sulaym: https://usul.ai/ar/t/kitab-sulaym-ibn-qays-al-hilali/106
  - sources/S-181_UMM_AYMAN_FADAK_VERIFICATION.md §3-E Ibn Abi al-Hadid 16: https://arabic.balaghah.net/sites/default/files/file/16.pdf
- **SOURCE:** Sunni: al-Baladhuri, Futuh al-Buldan (two recensions). Shia: al-Tabrisi, al-Ihtijaj 1; Kitab Sulaym; Ibn Abi al-Hadid, Sharh 16. Aus: Qurb al-Isnad → Bihar 22/101 h. 59.
- **SOURCE_STATUS:** VERIFIED (S-181, with URLs) — EDITION-LOCK PENDING (pages ⟦…⟧).
- **PROPOSED_ACTION:**
  Replace the bullet with the two bullets from manuscript-patches/B1_P03_C06_FADAK_S-181_PATCH.md §B (bullets 3 and 4), verbatim:
  «•  ফাদাকে আলী (আলাইহিস্ সালাম) ও উম্মে আইমানের সাক্ষ্য — সুন্নি: বালাযুরি, ফুতুহুল বুলদান, ⟦edition⟧, পৃ. ⟦ ⟧ («وشهد لها علي بن أبي طالب … فشهدت لها أم أيمن»; আবু বকর: «لا تجوز إلا شهادة رجلين أو رجل وامرأتين»); দ্বিতীয় বর্ণনায় সাক্ষী উম্মে আইমান ও রাবাহ। শিয়া: তাবারসি, আল-ইহতিজাজ, ⟦edition⟧, খণ্ড ১, পৃ. ⟦ ⟧ (আবু বকর দলিল লেখেন; উমর ছিঁড়ে ফেলেন); কিতাবু সুলাইম ইবনে কায়স, ⟦edition⟧, পৃ. ⟦ ⟧ («ولم يصدقها ولا صدق أم أيمن»); ইবনে আবিল হাদিদ, শারহু নাহজিল বালাগা, ⟦edition⟧, খণ্ড ১৬, পৃ. ২১৩–২১৪, ২১৬, ২২৫, ২৭৩–২৭৫। [সুন্নি ও শিয়া বর্ণনা আলাদা recension; এক করা হয়নি।]»
  «•  আউস ইবনুল হাদাসান — উম্মে আইমানের সাক্ষী নন; আয়েশা ও হাফসার সঙ্গে «لا نورث»-এর বিপক্ষ-সাক্ষ্যে — হিমইয়ারি, কুরবুল ইসনাদ, ⟦edition⟧, হা. ⟦৯৯/৩৩৫⟧; উদ্ধৃত: বিহারুল আনওয়ার, খণ্ড ২২, পৃ. ১০১, হা. ৫৯ ⟦edition⟧; আল-ইহতিজাজ, খণ্ড ১ (উমরের বক্তব্যে)।»
  Apply prose A-3 of the same patch. Do not add Malik b. Aws b. al-Hadathan (Bukhari 3094 / Muslim 1757) to either bullet: he is a Sunni narrator, not a witness.
- **PATCH_TYPE:** SPLIT_CLAIM
- **CONFIDENCE:** HIGH
- **REQUIRES_HUMAN_REVIEW:** YES

### PB1-021

- **PATCH_ID:** PB1-021
- **PART:** 3
- **CHAPTER:** ০৬  ফাদাক, আর চুপ না থাকার সাহস
- **PAGE:** PAGE-CHECK (docx not available); ¶2817
- **PARAGRAPH/LOCATION:** Ledger REF-082 · Paragraph_Index 2817 · source-note bullet (chapter source block) · register HAD-UMM-AYMAN-JANNA
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  «উম্মে আইমান জান্নাতি» — ইবনে সা'দ, আত-তাবাকাত — PAGE-CHECK।
- **PROBLEM:** «উম্মে আইমান জান্নাতি» is cited to Ibn Sa'd without its status. The Ibn Sa'd report is MURSAL (al-Suyuti: mursal; al-Albani: da'if). The Shia wording is a separate report inside the Fadak narrative (Bihar 29). The Hakim attribution is NOT VERIFIED. Prose must not say «সহিহ হাদিসে» or use a flat «রাসূলুল্লাহ ﷺ বলেছেন».
- **EVIDENCE:**
  - sources/S-181_UMM_AYMAN_FADAK_VERIFICATION.md §2-A/2-B: https://dorar.net/h/ipCT1d90 (text) · https://dorar.net/h/R71ZmTA4 (grading)
  - sources/S-181_UMM_AYMAN_FADAK_VERIFICATION.md §2-D Bihar 29: https://najafdesertlibrary.com/book/بحار-الأنوار/v/29/p/176
  - sources/S-181_UMM_AYMAN_FADAK_VERIFICATION.md §2-C: Hakim — no reference found.
- **SOURCE:** Ibn Sa'd, al-Tabaqat al-Kubra (Sufyan b. Uqba; mursal); al-Majlisi, Bihar al-Anwar 29 (Shia).
- **SOURCE_STATUS:** Ibn Sa'd: EXISTS — MURSAL/WEAK; Bihar 29: VERIFIED (edition lock p. 128/176); Hakim: NOT VERIFIED — PRINT BLOCKED.
- **PROPOSED_ACTION:**
  Replace the bullet with manuscript-patches/B1_P03_C06_FADAK_S-181_PATCH.md §B bullet 2, verbatim:
  «•  «যে জান্নাতের নারীকে বিবাহ করতে চায়, সে উম্মে আইমানকে বিবাহ করুক» — ইবনে সা'দ, আত-তাবাকাতুল কুবরা, ⟦edition⟧, খণ্ড ⟦ ⟧, পৃ. ⟦ ⟧ (সুফইয়ান ইবনে উকবা থেকে; মুরসাল — সুয়ূতী: মুরসাল; আলবানী: যয়ীফ)। শিয়া সূত্রে: মাজলিসি, বিহারুল আনওয়ার, ⟦edition⟧, খণ্ড ২৯, পৃ. ⟦১২৮/১৭৬⟧ («إن أم أيمن امرأة من أهل الجنة», ফাদাক-অধ্যায়)। [Hakim/Mustadrak — এই wording-এর reference পাওয়া যায়নি; উদ্ধৃত নয়।]»
  Prose: apply manuscript-patches/B1_P03_C06_FADAK_S-181_PATCH.md A-2. The attribution clause becomes «ইবনে সা'দের আত-তাবাকাতুল কুবরা-তে একটি মুরসাল বর্ণনায় এসেছে…» or «শিয়া সূত্রে ফাদাকের বর্ণনার ভিতরেই আছে…»; the two must never be merged.
- **PATCH_TYPE:** WEAKEN_ATTRIBUTION
- **CONFIDENCE:** HIGH
- **REQUIRES_HUMAN_REVIEW:** YES

### PB1-022

- **PATCH_ID:** PB1-022
- **PART:** 3
- **CHAPTER:** ০৭  আমার যুগের ইমাম কে?
- **PAGE:** PAGE-CHECK (docx not available); ¶2880
- **PARAGRAPH/LOCATION:** Ledger REF-084 · Paragraph_Index 2880 · source-note bullet (chapter source block)
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  সালমানের প্রশ্ন ও «মুশরিক/জাহিল» ভাগ — বর্ণিত আছে (মূল কিতাব মেলানো বাকি)।
- **PROBLEM:** UNIDENTIFIED (BUG-25): no classical source located. The note is already attribution-only («বর্ণিত আছে») and carries no kitab name; prose that depends on it must not rise above «বর্ণিত আছে».
- **EVIDENCE:**
  - No source evidence exists in this repo for this row (audit v1.1 BUG-25 list). KNOWLEDGE-ONLY (research layer / audit v1.1 candidate; not verifiable from this environment).
- **SOURCE:** None located (ledger Candidate_Source: see CSV).
- **SOURCE_STATUS:** SOURCE-MISSING · বর্ণিত আছে · PRINT BLOCKED (book gate)
- **PROPOSED_ACTION:**
  Retain the current wording verbatim (no kitab name may be added). Author decides: keep as attribution-only, or delete the item (BUG-25). If a sanad is later found, re-open as ADD_SOURCE with PAGE-CHECK.
- **PATCH_TYPE:** PRESERVE_WITH_PAGE_CHECK
- **CONFIDENCE:** LOW
- **REQUIRES_HUMAN_REVIEW:** YES

---

## Part 4

### PB1-023

- **PATCH_ID:** PB1-023
- **PART:** 4
- **CHAPTER:** ০৫  ইবাদত কীভাবে ভেতরটা বদলায়
- **PAGE:** PAGE-CHECK (docx not available); ¶3494
- **PARAGRAPH/LOCATION:** Ledger REF-086 · Paragraph_Index 3494 · source-note bullet (chapter source block) · register HAD-FATIMA-NAR
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  «إن الله فطم ابنتي فاطمة…» — খাতায় কানযুল উম্মাল, খণ্ড ৬, পৃ. ২১৯; খণ্ড/পৃষ্ঠা মেলানো হয়নি — PAGE-CHECK।
- **PROBLEM:** «কানযুল উম্মাল, খণ্ড ৬, পৃ. ২১৯» is an edition-specific location (the Hyderabad printing), given without naming the edition. Other editions (al-Risala) number it differently. The edition difference must be stated explicitly.
- **EVIDENCE:**
  - Wording absent from the six books: search «فطم ابنتي» (all six books) → (none)
  - Kanz al-'Ummal edition mapping (Hyderabad 6/219 ↔ al-Risala 12:109 h. 34227): KNOWLEDGE-ONLY (research layer / audit v1.1 candidate; not verifiable from this environment).
- **SOURCE:** al-Muttaqi al-Hindi, Kanz al-'Ummal (CANDIDATE: al-Risala ed. 12:109, h. 34227); also al-Tabarani; Ibn Asakir (CANDIDATE).
- **SOURCE_STATUS:** CANDIDATE — EDITION-LOCK PENDING. Register HAD-FATIMA-NAR (REF-256, REF-259).
- **PROPOSED_ACTION:**
  Replace the bullet with:
  «•  «إن الله فطم ابنتي فاطمة…» — আলী আল-মুত্তাকী আল-হিন্দি, কানযুল উম্মাল, ⟦edition: খাতার উল্লেখ অনুযায়ী খণ্ড ৬, পৃ. ২১৯ — কোন মুদ্রণ?⟧; অন্য মুদ্রণে খণ্ড ⟦ ⟧, পৃ. ⟦ ⟧, হাদীস ⟦ ⟧ — PAGE-CHECK। সিহাহ সিত্তায় নেই।»
- **PATCH_TYPE:** CORRECT_CITATION
- **CONFIDENCE:** MEDIUM
- **REQUIRES_HUMAN_REVIEW:** YES

### PB1-024

- **PATCH_ID:** PB1-024
- **PART:** 4
- **CHAPTER:** ০৫  ইবাদত কীভাবে ভেতরটা বদলায়
- **PAGE:** PAGE-CHECK (docx not available); ¶3495
- **PARAGRAPH/LOCATION:** Ledger REF-087 · Paragraph_Index 3495 · source-note bullet (chapter source block)
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  «অন্তরে সরিষা দানা পরিমাণ অহংকার» — এই শব্দে সূত্র খাতায় নেই — «বর্ণিত আছে»।
- **PROBLEM:** The note says there is no source, but the wording is in Sahih Muslim 91 and three other six-book collections (BUG-16).
- **EVIDENCE:**
  - `-- muslim 91 (num 266/ar 91.02) [The Book of Faith]  :: …ن عبد الله، قال قال رسول الله صلى الله عليه وسلم  " لا يدخل النار أحد في قلبه مثقال حبة خردل من إيمان ولا يدخل الجنة أحد في قلبه مثقال حبة خردل من كبرياء " .…`
  - `-- abudawud 4091 (num 4091/ar 4091) [Clothing (Kitab Al-Libas)] Al-Albani:Sahih;Muhammad Muhyi Al-Din Abdul Hamid:Sahih;Zubair Ali Zai:Sahih Muslim (91) :: …الله، قال قال رسول الله صلى الله عليه وسلم  " لا يدخل الجنة من كان في قلبه مثقال حبة من خردل من كبر ولا يدخل النار من كان في قلبه مثقال خردلة من إيمان " . قال أبو داود رواه القسم…`
  - `-- tirmidhi 1998 (num 1998/ar 1998) [Chapters on Righteousness And Ma] Ahmad Muhammad Shakir:Sahih;Al-Albani:Sahih;Bashar Awad Maarouf:Hasan Sahih;Zubair Ali Zai:Sahih - Bukhari And Muslim :: …الله، قال قال رسول الله صلى الله عليه وسلم  " لا يدخل الجنة من كان في قلبه مثقال حبة من خردل من كبر ولا يدخل النار من كان في قلبه مثقال حبة من إيمان " . وفي الباب عن أبي هريرة وا…`
  - `search «خردل من كبر» (all six books) → muslim ar91.02, abudawud ar4091, tirmidhi ar1998, ibnmajah ar59 … (+1)`
- **SOURCE:** Sahih Muslim 91 (Ibn Mas'ud); Sunan Abi Dawud 4091; Jami' al-Tirmidhi 1998; Sunan Ibn Majah 59.
- **SOURCE_STATUS:** VERIFIED (live); sahih.
- **PROPOSED_ACTION:**
  Replace the bullet with:
  «•  «অন্তরে সরিষা দানা পরিমাণ অহংকার» — সহীহ মুসলিম ৯১ (আবদুল্লাহ ইবনে মাসউদ); আরও: সুনানে আবু দাউদ ৪০৯১, জামে তিরমিযি ১৯৯৮, সুনানে ইবনে মাজাহ ৫৯।»
- **PATCH_TYPE:** ADD_SOURCE
- **CONFIDENCE:** HIGH
- **REQUIRES_HUMAN_REVIEW:** NO

### PB1-025

- **PATCH_ID:** PB1-025
- **PART:** 4
- **CHAPTER:** ০৬  প্রকৃত মুমিনকে চেনা যায় কীভাবে?
- **PAGE:** PAGE-CHECK (docx not available); ¶3599
- **PARAGRAPH/LOCATION:** Ledger REF-090 · Paragraph_Index 3599 · source-note bullet (chapter source block)
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  «তিনটি গুণ… ঈমান পূর্ণ হবে», «আমানতদার… প্রাচুর্যকে বিপদ», «সবকিছুই তাকে ভয় করে», «ফেরেশতারা মুমিনদের নূর দেখে» — খাতায় সূত্রহীন — «বর্ণিত আছে»।
- **PROBLEM:** UNIDENTIFIED (BUG-25): no classical source located. The note is already attribution-only («বর্ণিত আছে») and carries no kitab name; prose that depends on it must not rise above «বর্ণিত আছে».
- **EVIDENCE:**
  - No source evidence exists in this repo for this row (audit v1.1 BUG-25 list). KNOWLEDGE-ONLY (research layer / audit v1.1 candidate; not verifiable from this environment).
- **SOURCE:** None located (ledger Candidate_Source: see CSV).
- **SOURCE_STATUS:** SOURCE-MISSING · বর্ণিত আছে · PRINT BLOCKED (book gate)
- **PROPOSED_ACTION:**
  Retain the current wording verbatim (no kitab name may be added). Author decides: keep as attribution-only, or delete the item (BUG-25). If a sanad is later found, re-open as ADD_SOURCE with PAGE-CHECK.
- **PATCH_TYPE:** PRESERVE_WITH_PAGE_CHECK
- **CONFIDENCE:** LOW
- **REQUIRES_HUMAN_REVIEW:** YES

### PB1-026

- **PATCH_ID:** PB1-026
- **PART:** 4
- **CHAPTER:** ০৬  প্রকৃত মুমিনকে চেনা যায় কীভাবে?
- **PAGE:** PAGE-CHECK (docx not available); ¶3600
- **PARAGRAPH/LOCATION:** Ledger REF-091 · Paragraph_Index 3600 · source-note bullet (chapter source block)
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  «আল্লাহ মুমিনকে দুনিয়ার বিপদ থেকে মুক্ত রাখেননি…» — খাতায় সূত্রহীন — «বর্ণিত আছে»।
- **PROBLEM:** UNIDENTIFIED (BUG-25): no classical source located. The note is already attribution-only («বর্ণিত আছে») and carries no kitab name; prose that depends on it must not rise above «বর্ণিত আছে».
- **EVIDENCE:**
  - No source evidence exists in this repo for this row (audit v1.1 BUG-25 list). KNOWLEDGE-ONLY (research layer / audit v1.1 candidate; not verifiable from this environment).
- **SOURCE:** None located (ledger Candidate_Source: see CSV).
- **SOURCE_STATUS:** SOURCE-MISSING · বর্ণিত আছে · PRINT BLOCKED (book gate)
- **PROPOSED_ACTION:**
  Retain the current wording verbatim (no kitab name may be added). Author decides: keep as attribution-only, or delete the item (BUG-25). If a sanad is later found, re-open as ADD_SOURCE with PAGE-CHECK.
- **PATCH_TYPE:** PRESERVE_WITH_PAGE_CHECK
- **CONFIDENCE:** LOW
- **REQUIRES_HUMAN_REVIEW:** YES

---

## Part 5

### PB1-027

- **PATCH_ID:** PB1-027
- **PART:** 5
- **CHAPTER:** ০২  চাদরের নিচে কারা ছিলেন?
- **PAGE:** PAGE-CHECK (docx not available); ¶4017
- **PARAGRAPH/LOCATION:** Ledger REF-096 · Paragraph_Index 4017 · source-note bullet (chapter source block) · register HAD-KISA
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  চাদরের হাদীস (হাদীসে কিসা, জাবির ইবনে আব্দুল্লাহ আনসারীর বর্ণনা) — শ্রোতা ০৪ L478; জনির নোটে আহলে সুন্নাহর একাধিক উৎসের তালিকা (সহীহ মুসলিম, তিরমিযি…) — এই দীর্ঘ পাঠের শব্দে মেলানো হয়নি — «বর্ণিত আছে»; সংক্ষিপ্ত চাদর-রেওয়ায়েত সহীহ মুসলিমে (ফাযায়েলুস সাহাবা) — PAGE-CHECK।
  Relevant clause: «সংক্ষিপ্ত চাদর-রেওয়ায়েত সহীহ মুসলিমে (ফাযায়েলুস সাহাবা) — PAGE-CHECK।»
- **PROBLEM:** The short kisa report is cited to «সহীহ মুসলিম (ফাযায়েলুস সাহাবা) — PAGE-CHECK» with no number. Its number is Muslim 2424 (BUG-16). The long Jabir version must stay separate (Shia compilations, REF-190).
- **EVIDENCE:**
  - `-- muslim 2424 (num 6261/ar 2424) [The Book of the Merits of the Co]  :: …ن مصعب بن شيبة، عن صفية بنت شيبة، قالت قالت عائشة خرج النبي صلى الله عليه وسلم غداة وعليه مرط مرحل من شعر أسود فجاء الحسن بن علي فأدخله ثم جاء الحسين فدخل معه ثم جاءت فاطمة فأدخلها ثم جاء…`
- **SOURCE:** Sahih Muslim 2424 (Aisha).
- **SOURCE_STATUS:** VERIFIED (live). Long Jabir version: «বর্ণিত আছে» / SPC (REF-190).
- **PROPOSED_ACTION:**
  Replace only that closing clause with:
  «সংক্ষিপ্ত চাদর-রেওয়ায়েত (আয়িশা থেকে) — সহীহ মুসলিম, ফাযায়েলুস সাহাবা, হাদীস ২৪২৪।»
  The long-version clause («…এই দীর্ঘ পাঠের শব্দে মেলানো হয়নি — «বর্ণিত আছে»») is unchanged. Do not merge the two.
- **PATCH_TYPE:** ADD_SOURCE
- **CONFIDENCE:** HIGH
- **REQUIRES_HUMAN_REVIEW:** NO

### PB1-028

- **PATCH_ID:** PB1-028
- **PART:** 5
- **CHAPTER:** ০২  চাদরের নিচে কারা ছিলেন?
- **PAGE:** PAGE-CHECK (docx not available); ¶4018
- **PARAGRAPH/LOCATION:** Ledger REF-097 · Paragraph_Index 4018 · source-note bullet (chapter source block)
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  তাসনিম-সংক্রান্ত হাদীসগুলো (ক্ষুধার্তকে খাওয়ানো, মাদক পরিত্যাগ, «আমি প্রথম ব্যক্তি হব», আবু জাফর ও ইমাম সাদিক (আলাইহিমাস্ সালাম)-এর ব্যাখ্যা) — খাতায় সূত্রহীন — «বর্ণিত আছে»।
- **PROBLEM:** UNIDENTIFIED (BUG-25): no classical source located. The note is already attribution-only («বর্ণিত আছে») and carries no kitab name; prose that depends on it must not rise above «বর্ণিত আছে».
- **EVIDENCE:**
  - No source evidence exists in this repo for this row (audit v1.1 BUG-25 list). KNOWLEDGE-ONLY (research layer / audit v1.1 candidate; not verifiable from this environment).
- **SOURCE:** None located (ledger Candidate_Source: see CSV).
- **SOURCE_STATUS:** SOURCE-MISSING · বর্ণিত আছে · PRINT BLOCKED (book gate)
- **PROPOSED_ACTION:**
  Retain the current wording verbatim (no kitab name may be added). Author decides: keep as attribution-only, or delete the item (BUG-25). If a sanad is later found, re-open as ADD_SOURCE with PAGE-CHECK.
- **PATCH_TYPE:** PRESERVE_WITH_PAGE_CHECK
- **CONFIDENCE:** LOW
- **REQUIRES_HUMAN_REVIEW:** YES

### PB1-029

- **PATCH_ID:** PB1-029
- **PART:** 5
- **CHAPTER:** ০৩  ভালোবাসা কি শুধু অনুভূতি?
- **PAGE:** PAGE-CHECK (docx not available); ¶4093
- **PARAGRAPH/LOCATION:** Ledger REF-100 · Paragraph_Index 4093 · source-note bullet (chapter source block)
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  «সর্বপ্রথম জান্নাতে… আশেকরা পশ্চাতে», «আশেকরা একই স্থানে… পানাহার একত্রে» — খাতায় আরবি পাঠ আছে, সূত্র নেই — «বর্ণিত আছে»।
- **PROBLEM:** UNIDENTIFIED (BUG-25): no classical source located. The note is already attribution-only («বর্ণিত আছে») and carries no kitab name; prose that depends on it must not rise above «বর্ণিত আছে».
- **EVIDENCE:**
  - No source evidence exists in this repo for this row (audit v1.1 BUG-25 list). KNOWLEDGE-ONLY (research layer / audit v1.1 candidate; not verifiable from this environment).
- **SOURCE:** None located (ledger Candidate_Source: see CSV).
- **SOURCE_STATUS:** SOURCE-MISSING · বর্ণিত আছে · PRINT BLOCKED (book gate)
- **PROPOSED_ACTION:**
  Retain the current wording verbatim (no kitab name may be added). Author decides: keep as attribution-only, or delete the item (BUG-25). If a sanad is later found, re-open as ADD_SOURCE with PAGE-CHECK.
- **PATCH_TYPE:** PRESERVE_WITH_PAGE_CHECK
- **CONFIDENCE:** LOW
- **REQUIRES_HUMAN_REVIEW:** YES

### PB1-030

- **PATCH_ID:** PB1-030
- **PART:** 5
- **CHAPTER:** ০৪  সূরা কাওসার নতুন করে পড়া
- **PAGE:** PAGE-CHECK (docx not available); ¶4178
- **PARAGRAPH/LOCATION:** Ledger REF-101 · Paragraph_Index 4178 · source-note bullet (chapter source block)
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  বিদ্রূপকারী আমর ইবনুল আস («হে আবুল আবতার»), মসজিদে, হাকাম ইবনুল আসের সাথে — তাফসীরে হুব্বে আলী, সূরা আল-কাউসার, হা. ১০ (ইবনে বাবুওয়াইহ; হুবেআলী.কম হা. ৯৪৯৯) — VERIFIED (স্থানীয় কপি: F:\HZ Fatima Zahra SA Nobuwat & Imamat Bondhon\__REWRITTEN\Tafseer e Hubbe Ali en to Bn\hubbe_ali_ch108_আল-কাউসার_bangla.md ল. ২৪৬–২৪৯); পিতা আস ইবনে ওয়াইল — একই তাফসীর হা. ১১ (আল-ইহতিজাজ)। «পুত্র ইব্রাহিম» প্রসঙ্গ — খাতা; «বর্ণিত আছে»।
- **PROBLEM:** The source block cites a local Windows file path (F:\…hubbe_ali_ch108…md, lines 246–249) and the word «VERIFIED» (BUG-07/27). A reader cannot use a path. The citation must be the Tafsir Hubb-e Ali hadith numbers.
- **EVIDENCE:**
  - Tafsir Hubb-e Ali h. 10–11 / hubbeali.com h. 9499: KNOWLEDGE-ONLY (research layer / audit v1.1 candidate; not verifiable from this environment) (the local copy is not in this repo).
- **SOURCE:** Tafsir Hubb-e Ali, Surat al-Kawthar, h. 10 (from Ibn Babawayh) and h. 11 (from al-Ihtijaj); hubbeali.com h. 9499.
- **SOURCE_STATUS:** CANDIDATE — PAGE-CHECK (cannot be re-verified here).
- **PROPOSED_ACTION:**
  Replace the bullet with:
  «•  বিদ্রূপকারী আমর ইবনুল আস («হে আবুল আবতার»), মসজিদে, হাকাম ইবনুল আসের সাথে — তাফসীরে হুব্বে আলী, সূরা আল-কাউসার, হা. ১০ (ইবনে বাবুওয়াইহ থেকে; হুবেআলী.কম হা. ৯৪৯৯) — PAGE-CHECK; পিতা আস ইবনে ওয়াইল — একই তাফসীর হা. ১১ (আল-ইহতিজাজ থেকে) — PAGE-CHECK। «পুত্র ইব্রাহিম» প্রসঙ্গ — খাতা; «বর্ণিত আছে»।»
  Move the F:\ path into the ledger Resolution_Note only.
- **PATCH_TYPE:** CORRECT_CITATION
- **CONFIDENCE:** MEDIUM
- **REQUIRES_HUMAN_REVIEW:** YES

### PB1-031

- **PATCH_ID:** PB1-031
- **PART:** 5
- **CHAPTER:** ০৪  সূরা কাওসার নতুন করে পড়া
- **PAGE:** PAGE-CHECK (docx not available); ¶4182
- **PARAGRAPH/LOCATION:** Ledger REF-105 · Paragraph_Index 4182 · source-note bullet (chapter source block)
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  ইবনে আব্বাস: «আল কাওসার কী?» — খাতায় সূত্রহীন — «বর্ণিত আছে»।
- **PROBLEM:** The note says there is no source, but Ibn Abbas's explanation of al-Kawthar is Bukhari 4966 (BUG-16). Since the prose is not in the ledger, confirm that the scene uses this report (al-Kawthar = «the good Allah gave him»).
- **EVIDENCE:**
  - `-- bukhari 4966 (num 4966/ar 4966) [Prophetic Commentary on the Qur']  :: …اهيم، حدثنا هشيم، حدثنا أبو بشر، عن سعيد بن جبير، عن ابن عباس رضى الله عنهما أنه قال في الكوثر هو الخير الذي أعطاه الله إياه. قال أبو بشر قلت لسعيد بن جبير فإن الناس يزعمون أنه نهر ف…`
- **SOURCE:** Sahih al-Bukhari 4966 (Ibn Abbas via Sa'id b. Jubayr).
- **SOURCE_STATUS:** VERIFIED (live).
- **PROPOSED_ACTION:**
  Replace the bullet with:
  «•  ইবনে আব্বাস: «আল কাওসার কী?» — সহীহ বুখারী ৪৯৬৬ (সাঈদ ইবনে জুবাইরের সূত্রে): «الكوثر الخير الذي أعطاه الله إياه»।»
  If the prose quotes something else in Ibn Abbas's name, keep «বর্ণিত আছে» for that part.
- **PATCH_TYPE:** ADD_SOURCE
- **CONFIDENCE:** HIGH
- **REQUIRES_HUMAN_REVIEW:** YES

### PB1-032

- **PATCH_ID:** PB1-032
- **PART:** 5
- **CHAPTER:** ০৫  মুবাহালার দিন রাসূলুল্লাহ ﷺ কাদের ডাকলেন
- **PAGE:** PAGE-CHECK (docx not available); ¶4272
- **PARAGRAPH/LOCATION:** Ledger REF-107 · Paragraph_Index 4272 · source-note bullet (chapter source block) · register HAD-MUBAHALA
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  সা’দ ইবনে আবি ওয়াক্কাসের হাদীস (তিন কথা; মুবাহালার আয়াতে আলী, ফাতিমা, হাসান, হুসাইনকে ডাকা — «এরাই আমার পরিবার») — সহীহ মুসলিম, ফাযায়েলুস সাহাবা (আন্তর্জাতিক নম্বর ২৪০৪); জনির নোটে বাংলা সংস্করণ পৃ. ৯১৭, হাদীস ৬০৬২ — PAGE-CHECK।
- **PROBLEM:** The standard number 2404 is given, but the bullet keeps PAGE-CHECK and a second, Bengali-edition numbering (৬০৬২ / পৃ. ৯১৭). The book uses one numbering system, Abd al-Baqi (BUG-12). The edition number may stay only as an explicitly labelled secondary reference.
- **EVIDENCE:**
  - `-- muslim 2404 (num 6220/ar 2404.04) [The Book of the Merits of the Co]  :: …اءنا وأبناءكم} دعا رسول الله صلى الله عليه وسلم عليا وفاطمة وحسنا وحسينا فقال " اللهم هؤلاء أهلي " .…`
- **SOURCE:** Sahih Muslim 2404 (Sa'd b. Abi Waqqas).
- **SOURCE_STATUS:** VERIFIED (live).
- **PROPOSED_ACTION:**
  Replace the bullet with:
  «•  সা’দ ইবনে আবি ওয়াক্কাসের হাদীস (তিন কথা; মুবাহালার আয়াতে আলী, ফাতিমা, হাসান, হুসাইনকে ডাকা — «এরাই আমার পরিবার») — সহীহ মুসলিম, ফাযায়েলুস সাহাবা, হাদীস ২৪০৪ (আবদুল বাকি ক্রম; জনির নোটে বাংলা সংস্করণ পৃ. ৯১৭, হাদীস ৬০৬২)।»
- **PATCH_TYPE:** CORRECT_HADITH_NUMBER
- **CONFIDENCE:** HIGH
- **REQUIRES_HUMAN_REVIEW:** NO

### PB1-033

- **PATCH_ID:** PB1-033
- **PART:** 5
- **CHAPTER:** ০৬  নিজে ক্ষুধার্ত থেকেও অন্যকে খাওয়ানো
- **PAGE:** PAGE-CHECK (docx not available); ¶4353
- **PARAGRAPH/LOCATION:** Ledger REF-110 · Paragraph_Index 4353 · source-note bullet (chapter source block)
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  «ক্ষুধার্তকে আহার করানো → জান্নাতের ফল» ও «আশেকদের পানাহার একত্রে» — অধ্যায় ২ ও ৩-এর সূত্র দেখো («বর্ণিত আছে»)।
- **PROBLEM:** DUPLICATE: this is a cross-reference to REF-097 and REF-100 (Part 5 Ch 02, 03), both UNIDENTIFIED. The status («বর্ণিত আছে») already matches them, so normalisation needs no wording change.
- **EVIDENCE:**
  - Ledger REF-097 / REF-100: UNID, SOURCE-MISSING. No source evidence in repo.
- **SOURCE:** None located.
- **SOURCE_STATUS:** SOURCE-MISSING · বর্ণিত আছে.
- **PROPOSED_ACTION:**
  Retain the current wording verbatim. If REF-097/100 are deleted under BUG-25, delete this cross-reference with them.
- **PATCH_TYPE:** PRESERVE_WITH_PAGE_CHECK
- **CONFIDENCE:** LOW
- **REQUIRES_HUMAN_REVIEW:** YES

---

## Part 6

### PB1-034

- **PATCH_ID:** PB1-034
- **PART:** 6
- **CHAPTER:** ০২  যেদিন মদিনা দুই ভাগ হলো
- **PAGE:** PAGE-CHECK (docx not available); ¶4751
- **PARAGRAPH/LOCATION:** Ledger REF-115 · Paragraph_Index 4751 · source-note bullet (chapter source block)
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  আমিরুল মুমিনীন (আলাইহিস্ সালাম) আবু বকরের হাত ধরে দেখান — বর্ণিত আছে; PAGE-CHECK (খাতায় সূত্র নেই)।
- **PROBLEM:** UNIDENTIFIED (BUG-25): no classical source located. The note is already attribution-only («বর্ণিত আছে») and carries no kitab name; prose that depends on it must not rise above «বর্ণিত আছে». Prose REF-112 (¶4711) keeps «এমন বর্ণিত আছে» — matches.
- **EVIDENCE:**
  - No source evidence exists in this repo for this row (audit v1.1 BUG-25 list). KNOWLEDGE-ONLY (research layer / audit v1.1 candidate; not verifiable from this environment).
- **SOURCE:** None located (ledger Candidate_Source: see CSV).
- **SOURCE_STATUS:** SOURCE-MISSING · বর্ণিত আছে · PRINT BLOCKED (book gate)
- **PROPOSED_ACTION:**
  Retain the current wording verbatim (no kitab name may be added). Author decides: keep as attribution-only, or delete the item (BUG-25). If a sanad is later found, re-open as ADD_SOURCE with PAGE-CHECK.
- **PATCH_TYPE:** PRESERVE_WITH_PAGE_CHECK
- **CONFIDENCE:** LOW
- **REQUIRES_HUMAN_REVIEW:** YES

### PB1-035

- **PATCH_ID:** PB1-035
- **PART:** 6
- **CHAPTER:** ০৫  উত্তরাধিকার, উপহার, নাকি ব্যবস্থাপনা?
- **PAGE:** PAGE-CHECK (docx not available); ¶5291
- **PARAGRAPH/LOCATION:** Ledger REF-122 · Paragraph_Index 5291 · source-note bullet (chapter source block) · register HAD-FADAK-TESTIMONY
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  আবু বকরের রাষ্ট্রীয় সম্পত্তি ঘোষণা — খাতায়: বালাযুরী, ফুতুহুল বুলদান; তাবারী — PAGE-CHECK। দলিল ছিঁড়ে ফেলা — খাতায়: সুয়ূতী, তারিখুল খুলাফা; ইবনে আবিল হাদীদ, শারহু নাহজিল বালাগা খণ্ড ১৬ — PAGE-CHECK।
- **PROBLEM:** The deed-tearing is credited to al-Suyuti, Tarikh al-Khulafa' (not located) and Ibn Abi al-Hadid 16, while S-181 places the written deed and Umar's tearing it in al-Ihtijaj (Shia recension). The note also mixes Sunni and Shia attributions without labelling which is which. NOT FOUND ≠ DOES NOT EXIST: Suyuti is held back from print, not deleted from the ledger.
- **EVIDENCE:**
  - sources/S-181_UMM_AYMAN_FADAK_VERIFICATION.md §3-D: al-Ihtijaj — «إن هذا فيء للمسلمين…»; deed written, then taken/torn by Umar (https://www.almerja.com/reading.php?idm=124286)
  - sources/S-181_UMM_AYMAN_FADAK_VERIFICATION.md §3-E Ibn Abi al-Hadid vol. 16 (https://arabic.balaghah.net/sites/default/files/file/16.pdf)
  - Suyuti, Tarikh al-Khulafa' for the tearing: not located (ledger Candidate_Source) — KNOWLEDGE-ONLY (research layer / audit v1.1 candidate; not verifiable from this environment).
- **SOURCE:** al-Baladhuri, Futuh al-Buldan; al-Tabari; al-Tabrisi, al-Ihtijaj 1 (Shia); Ibn Abi al-Hadid, Sharh 16.
- **SOURCE_STATUS:** Ihtijaj/IAH: VERIFIED (S-181) — EDITION-LOCK PENDING. Suyuti: NOT VERIFIED. Baladhuri/Tabari for the «state property» statement: PAGE-CHECK.
- **PROPOSED_ACTION:**
  Replace the bullet with:
  «•  আবু বকরের রাষ্ট্রীয় সম্পত্তি ঘোষণা — খাতায়: বালাযুরী, ফুতুহুল বুলদান; তাবারী — PAGE-CHECK; শিয়া বর্ণনায়: আত-তাবারসি, আল-ইহতিজাজ, খণ্ড ১ («إن هذا فيء للمسلمين») — PAGE-CHECK। দলিল ছিঁড়ে ফেলা — শিয়া বর্ণনা: আল-ইহতিজাজ, খণ্ড ১ (আবু বকর দলিল লেখেন, উমর তা ছিঁড়ে ফেলেন); ইবনে আবিল হাদীদ, শারহু নাহজিল বালাগা, খণ্ড ১৬ — PAGE-CHECK।»
  Keep «সুয়ূতী, তারিখুল খুলাফা» in the ledger as NOT VERIFIED. It returns to print only with an edition page.
- **PATCH_TYPE:** CORRECT_SOURCE
- **CONFIDENCE:** MEDIUM
- **REQUIRES_HUMAN_REVIEW:** YES

### PB1-036

- **PATCH_ID:** PB1-036
- **PART:** 6
- **CHAPTER:** ০৫  উত্তরাধিকার, উপহার, নাকি ব্যবস্থাপনা?
- **PAGE:** PAGE-CHECK (docx not available); ¶5292
- **PARAGRAPH/LOCATION:** Ledger REF-123 · Paragraph_Index 5292 · source-note bullet (chapter source block) · register HAD-LA-NURITH
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  «আমরা নবীগণ উত্তরাধিকার রেখে যাই না» — খাতায়: বুখারি (খুমুস/ফারায়িদ), মুসলিম ১৭৫৯ — PAGE-CHECK।
- **PROBLEM:** The Bukhari numbers are missing («বুখারি (খুমুস/ফারায়িদ)»); they are 3093 and 6726. Also, the Bengali gloss «আমরা নবীগণ…» renders «معاشر الأنبياء», which none of the three cited texts contain. They read «لا نورث ما تركنا صدقة» (BUG-30 principle: quote the wording of the book cited).
- **EVIDENCE:**
  - `-- bukhari 3093 (num 3093/ar 3093) [One-fifth of Booty to the Cause ]  :: …عليه وسلم مما أفاء الله عليه. فقال لها أبو بكر إن رسول الله صلى الله عليه وسلم قال  " لا نورث ما تركنا صدقة ". فغضبت فاطمة بنت رسول الله صلى الله عليه وسلم فهجرت أبا بكر، فلم تزل…`
  - `-- bukhari 6726 (num 6726/ar 6726) [Laws of Inheritance (Al-Faraa'id]  :: …من فدك، وسهمهما من خيبر. فقال لهما أبو بكر سمعت رسول الله صلى الله عليه وسلم يقول  " لا نورث، ما تركنا صدقة، إنما يأكل آل محمد من هذا المال ". قال أبو بكر والله لا أدع أمرا رأيت…`
  - `-- muslim 1759 (num 4580/ar 1759.01) [The Book of Jihad and Expedition]  :: …ه بالمدينة وفدك وما بقي من خمس خيبر فقال أبو بكر إن رسول الله صلى الله عليه وسلم قال  " لا نورث ما تركنا صدقة إنما يأكل آل محمد - صلى الله عليه وسلم - في هذا المال " . وإني والله لا…`
- **SOURCE:** Sahih al-Bukhari 3093 (Fard al-Khumus), 6726 (al-Fara'id); Sahih Muslim 1759 — all Aisha, Abu Bakr reporting.
- **SOURCE_STATUS:** VERIFIED (live).
- **PROPOSED_ACTION:**
  Replace the bullet with:
  «•  «আমরা উত্তরাধিকার রেখে যাই না; যা রেখে যাই তা সাদাকা» (لا نورث ما تركنا صدقة) — সহীহ বুখারি ৩০৯৩ (কিতাবু ফারদিল খুমুস) ও ৬৭২৬ (কিতাবুল ফারায়িদ); সহীহ মুসলিম ১৭৫৯ (আয়িশা থেকে; আবু বকরের বর্ণনায়)। «নবীগণ» (معاشر الأنبياء) শব্দটি এই তিন বর্ণনায় নেই — সেই শব্দের সূত্র PAGE-CHECK।»
- **PATCH_TYPE:** CORRECT_HADITH_NUMBER
- **CONFIDENCE:** HIGH
- **REQUIRES_HUMAN_REVIEW:** YES

### PB1-037

- **PATCH_ID:** PB1-037
- **PART:** 6
- **CHAPTER:** ০৫  উত্তরাধিকার, উপহার, নাকি ব্যবস্থাপনা?
- **PAGE:** PAGE-CHECK (docx not available); ¶5294
- **PARAGRAPH/LOCATION:** Ledger REF-125 · Paragraph_Index 5294 · source-note bullet (chapter source block)
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  ফাদাক সাইয়্যেদা খাদিজা (আলাইহাস্ সালাম)-এর মোহরানা — বর্ণিত আছে; সূত্র খোলা।
- **PROBLEM:** The claim that Fadak was Khadija's mahr has no known classical source (BUG-23). «বর্ণিত আছে» implies a transmitted report. The audit recommends removal, or «কেউ কেউ বলেন» with no citation; under the global law, prefer weakening to deletion.
- **EVIDENCE:**
  - No source evidence in repo; audit v1.1 BUG-23. KNOWLEDGE-ONLY (research layer / audit v1.1 candidate; not verifiable from this environment).
- **SOURCE:** None located.
- **SOURCE_STATUS:** SOURCE-MISSING.
- **PROPOSED_ACTION:**
  Replace the bullet with:
  «•  ফাদাক সাইয়্যেদা খাদিজা (আলাইহাস্ সালাম)-এর মোহরানা — কেউ কেউ বলেন; কোনো ধ্রুপদি সূত্র পাওয়া যায়নি।»
  In the chapter prose (Part 6 Ch 05; not in the ledger), change only the attribution clause on this claim to «কেউ কেউ বলেন,». The author may instead delete the claim.
- **PATCH_TYPE:** WEAKEN_ATTRIBUTION
- **CONFIDENCE:** LOW
- **REQUIRES_HUMAN_REVIEW:** YES

### PB1-038

- **PATCH_ID:** PB1-038
- **PART:** 6
- **CHAPTER:** ০৬  বারবার ফাদাকে ফেরা কেন?
- **PAGE:** PAGE-CHECK (docx not available); ¶5369
- **PARAGRAPH/LOCATION:** Ledger REF-126 · Paragraph_Index 5369 · source-note bullet (chapter source block) · register HAD-BUKHARI-4240
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  সহীহ বুখারি ৪২৪০ (কিতাবুল মাগাযি, খায়বার অধ্যায়, আয়িশা থেকে): «فَوَجَدَتْ فَاطِمَةُ عَلَى أَبِي بَكْرٍ فِي ذَلِكَ فَهَجَرَتْهُ فَلَمْ تُكَلِّمْهُ حَتَّى تُوُفِّيَتْ، وَعَاشَتْ بَعْدَ النَّبِيِّ صلى الله عليه وسلم سِتَّةَ أَشْهُرٍ» — CONFIRMED (SECOND_NOTEBOOK/CITATION_RISK #১৩; একবচন «فهجرته»); বাংলা অর্থ এখানে Claude-এর অর্থানুবাদ; বাংলা সংস্করণের নম্বর PAGE-CHECK।
  Relevant clause: «— CONFIRMED (SECOND_NOTEBOOK/CITATION_RISK #১৩; একবচন «فهجرته»); বাংলা অর্থ এখানে Claude-এর অর্থানুবাদ; বাংলা সংস্করণের নম্বর PAGE-CHECK।»
- **PROBLEM:** 4240 is already the standard number and the text is verified. The trailing «বাংলা সংস্করণের নম্বর PAGE-CHECK» conflicts with the one-numbering rule (BUG-12). The bullet also carries internal QA references («SECOND_NOTEBOOK/CITATION_RISK #১৩») and an AI-translation remark («Claude-এর অর্থানুবাদ»). These belong in the ledger; how the translation is credited is the author's call.
- **EVIDENCE:**
  - `-- bukhari 4240 (num 4240/ar 4240) []  :: …لى الله عليه وسلم فأبى أبو بكر أن يدفع إلى فاطمة منها شيئا فوجدت فاطمة على أبي بكر في ذلك فهجرته، فلم تكلمه حتى توفيت، وعاشت بعد النبي صلى الله عليه وسلم ستة أشهر، فلما توفيت، دفنها زوجه…`
- **SOURCE:** Sahih al-Bukhari 4240 (Aisha), Kitab al-Maghazi.
- **SOURCE_STATUS:** VERIFIED (live) — CONFIRMED.
- **PROPOSED_ACTION:**
  Replace that clause with:
  «— CONFIRMED (একবচন «فهجرته»); নম্বর আন্তর্জাতিক (sunnah.com) ক্রমে; বাংলা অর্থ: ⟦অনুবাদের দায় — লেখক নির্ধারণ করবেন⟧।»
  The translation credit must stay truthful; do not silently remove the disclosure. The author chooses the wording.
- **PATCH_TYPE:** CORRECT_HADITH_NUMBER
- **CONFIDENCE:** HIGH
- **REQUIRES_HUMAN_REVIEW:** YES

### PB1-039

- **PATCH_ID:** PB1-039
- **PART:** 6
- **CHAPTER:** ০৭  তাঁর শেষ ইচ্ছা
- **PAGE:** PAGE-CHECK (docx not available); ¶5451
- **PARAGRAPH/LOCATION:** Ledger REF-131 · Paragraph_Index 5451 · source-note bullet (chapter source block) · register HAD-BUKHARI-4240
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  ফুপুর না-পড়া লাইন — সহীহ বুখারি ৪২৪০-এর পরের অংশ (CITATION_RISK #১৩-এর একই হাদীস), CONFIRMED; রাতে গোসল-কাফন-দাফন ও কবর গোপন রাখার ওসিয়ত — বর্ণিত আছে, PAGE-CHECK (খাতায় বুখারি ৪২৪০ লেখা, কিন্তু সেখানে গোপনের ওসিয়তের শব্দ নেই)।
- **PROBLEM:** The note implies that Bukhari 4240 does not support the night burial. It does: 4240 contains «فلما توفيت دفنها زوجها علي ليلا ولم يؤذن بها أبا بكر وصلى عليها» (BUG-17). Only the wasiyya to conceal the grave (and night ghusl/kafan) is absent from 4240.
- **EVIDENCE:**
  - `-- bukhari 4240 (num 4240/ar 4240) []  :: …ذلك فهجرته، فلم تكلمه حتى توفيت، وعاشت بعد النبي صلى الله عليه وسلم ستة أشهر، فلما توفيت، دفنها زوجها علي ليلا، ولم يؤذن بها أبا بكر وصلى عليها، وكان لعلي من الناس وجه حياة فاطمة، فلما توفيت…`
- **SOURCE:** Sahih al-Bukhari 4240 (Aisha).
- **SOURCE_STATUS:** Night burial / Abu Bakr not informed / Ali prayed: VERIFIED (live) — CONFIRMED. Concealment wasiyya: «বর্ণিত আছে» — Shia (Bihar 43:183 ff, CANDIDATE) — PAGE-CHECK; not in 4240.
- **PROPOSED_ACTION:**
  Replace the bullet with:
  «•  ফুপুর না-পড়া লাইন — সহীহ বুখারি ৪২৪০-এর পরের অংশ, CONFIRMED: «فلما توفيت دفنها زوجها علي ليلا ولم يؤذن بها أبا بكر وصلى عليها» (রাতে দাফন, আবু বকরকে খবর না দেওয়া, আলী (আলাইহিস্ সালাম)-এর জানাজা পড়ানো)। রাতে গোসল-কাফন ও কবর গোপন রাখার ওসিয়ত — বর্ণিত আছে (শিয়া সূত্রে; বিহারুল আনওয়ার, খণ্ড ৪৩ — PAGE-CHECK); বুখারি ৪২৪০-এ এই শব্দ নেই।»
  Keep the two statements in separate sentences. Do NOT attach the concealment wasiyya to 4240, and do NOT add any new or stronger claim about an explicit will of Fatima to conceal. The existing «বর্ণিত আছে» claim is only labelled with its Shia provenance (Bihar 43:183 ff — CANDIDATE, PAGE-CHECK; not verifiable here).
- **PATCH_TYPE:** CORRECT_CITATION
- **CONFIDENCE:** HIGH
- **REQUIRES_HUMAN_REVIEW:** YES

### PB1-040

- **PATCH_ID:** PB1-040
- **PART:** 6
- **CHAPTER:** ০৯  ওলায়াত মানে আমানত
- **PAGE:** PAGE-CHECK (docx not available); ¶5621
- **PARAGRAPH/LOCATION:** Ledger REF-134 · Paragraph_Index 5621 · source-note bullet (chapter source block) · register HAD-QALAM
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  কাগজ-কলম ও «কোরআনই আমাদের জন্য যথেষ্ট» (বৃহস্পতিবারের ঘটনা) — সহীহ বুখারি (কিতাবুল ইলম ও মাগাযি) — PAGE-CHECK; «কাবা মানুষের কাছে যায় না» — বর্ণিত আছে।
  Relevant clause: «কাগজ-কলম ও «কোরআনই আমাদের জন্য যথেষ্ট» (বৃহস্পতিবারের ঘটনা) — সহীহ বুখারি (কিতাবুল ইলম ও মাগাযি) — PAGE-CHECK;»
- **PROBLEM:** Bukhari is cited by book title only («কিতাবুল ইলম ও মাগাযি»). The numbers are verified: 114 (with «عندنا كتاب الله حسبنا») and 4431, plus Muslim 1637.
- **EVIDENCE:**
  - `-- bukhari 114 (num 114/ar 114) [Knowledge]  :: …تابا لا تضلوا بعده ". قال عمر إن النبي صلى الله عليه وسلم غلبه الوجع وعندنا كتاب الله حسبنا فاختلفوا وكثر اللغط. قال " قوموا عني، ولا ينبغي عندي التنازع ". فخرج ابن عباس يقو…`
  - `-- bukhari 4431 (num 4431/ar 4431) [Military Expeditions led by the ]  :: …حدثنا قتيبة، حدثنا سفيان، عن سليمان الأحول، عن سعيد بن جبير، قال قال ابن عباس يوم الخميس وما يوم الخميس اشتد برسول الله صلى الله عليه وسلم وجعه فقال " ائتوني أكتب لكم كتابا لن…`
  - `-- muslim 1637 (num 4232/ar 1637.01) [The Book of Wills]  :: …واللفظ لسعيد - قالوا حدثنا سفيان، عن سليمان الأحول، عن سعيد بن جبير، قال قال ابن عباس يوم الخميس وما يوم الخميس ثم بكى حتى بل دمعه الحصى . فقلت يا ابن عباس وما يوم الخميس قال اشتد برسو…`
- **SOURCE:** Sahih al-Bukhari 114, 4431; Sahih Muslim 1637 (Ibn Abbas).
- **SOURCE_STATUS:** VERIFIED (live). «কাবা মানুষের কাছে যায় না» — unchanged (no source).
- **PROPOSED_ACTION:**
  Replace that clause with:
  «কাগজ-কলম ও «কোরআনই আমাদের জন্য যথেষ্ট» (বৃহস্পতিবারের ঘটনা) — সহীহ বুখারি ১১৪ (কিতাবুল ইলম) ও ৪৪৩১ (কিতাবুল মাগাযি); সহীহ মুসলিম ১৬৩৭;»
- **PATCH_TYPE:** CORRECT_HADITH_NUMBER
- **CONFIDENCE:** HIGH
- **REQUIRES_HUMAN_REVIEW:** NO

### PB1-041

- **PATCH_ID:** PB1-041
- **PART:** 6
- **CHAPTER:** ০৯  ওলায়াত মানে আমানত
- **PAGE:** PAGE-CHECK (docx not available); ¶5622
- **PARAGRAPH/LOCATION:** Ledger REF-135 · Paragraph_Index 5622 · source-note bullet (chapter source block) · register HAD-BIHAR43-AGE
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  বয়স ও সময়কালের ভিন্নতা — খাতায়: বিহারুল আনওয়ার খণ্ড ৪৩ — PAGE-CHECK।
- **PROBLEM:** DUPLICATE of REF-130 (register HAD-BIHAR43-AGE). Both rows cite Bihar 43 for the age/duration variants, and the canonical citation is not yet page-locked.
- **EVIDENCE:**
  - Bihar al-Anwar 43 (CANDIDATE 43:6–9 age; 43:212–215 duration): KNOWLEDGE-ONLY (research layer / audit v1.1 candidate; not verifiable from this environment).
- **SOURCE:** al-Majlisi, Bihar al-Anwar vol. 43.
- **SOURCE_STATUS:** SHIA-PAGE-CHECK — EDITION-LOCK PENDING.
- **PROPOSED_ACTION:**
  Replace the bullet with:
  «•  বয়স ও সময়কালের ভিন্নতা — খাতায়: বিহারুল আনওয়ার খণ্ড ৪৩ — PAGE-CHECK (অধ্যায় ০৭-এর টীকার একই সূত্র)।»
  Once locked, print the same vol/page in REF-130 and REF-135.
- **PATCH_TYPE:** PRESERVE_WITH_PAGE_CHECK
- **CONFIDENCE:** MEDIUM
- **REQUIRES_HUMAN_REVIEW:** YES

### PB1-042

- **PATCH_ID:** PB1-042
- **PART:** 6
- **CHAPTER:** ১০  এবার নিজের ঘরে
- **PAGE:** PAGE-CHECK (docx not available); ¶5759
- **PARAGRAPH/LOCATION:** Ledger REF-140 · Paragraph_Index 5759 · source-note bullet (chapter source block)
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  আবান ইবনে তাগলিবের দুটি বর্ণনা — PAGE-CHECK (খাতায় কিতাবের নাম নেই)।
- **PROBLEM:** UNIDENTIFIED (BUG-25): no classical source located. The note is already attribution-only («বর্ণিত আছে») and carries no kitab name; prose that depends on it must not rise above «বর্ণিত আছে».
- **EVIDENCE:**
  - No source evidence exists in this repo for this row (audit v1.1 BUG-25 list). KNOWLEDGE-ONLY (research layer / audit v1.1 candidate; not verifiable from this environment).
- **SOURCE:** None located (ledger Candidate_Source: see CSV).
- **SOURCE_STATUS:** SOURCE-MISSING · বর্ণিত আছে · PRINT BLOCKED (book gate)
- **PROPOSED_ACTION:**
  Retain the current wording verbatim (no kitab name may be added). Author decides: keep as attribution-only, or delete the item (BUG-25). If a sanad is later found, re-open as ADD_SOURCE with PAGE-CHECK.
- **PATCH_TYPE:** PRESERVE_WITH_PAGE_CHECK
- **CONFIDENCE:** LOW
- **REQUIRES_HUMAN_REVIEW:** YES

---

## Part 7

### PB1-043

- **PATCH_ID:** PB1-043
- **PART:** 7
- **CHAPTER:** ০৩  কুরআনই কি যথেষ্ট নয়?
- **PAGE:** PAGE-CHECK (docx not available); ¶6047
- **PARAGRAPH/LOCATION:** Ledger REF-143 · Paragraph_Index 6047 · source-note bullet (chapter source block) · register HAD-12-KHALIFA
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  বারো খলিফা — সহীহ মুসলিম (কিতাবুল ইমারাহ), বুখারি ৭২২২ — PAGE-CHECK (খাতার শব্দ ও নম্বর মেলানো বাকি)।
- **PROBLEM:** Muslim is cited by book title only. The numbers are verified: Muslim 1821 («اثنا عشر خليفة… كلهم من قريش») and Bukhari 7222 («اثنا عشر أميرا…»). The two wordings must be kept distinct.
- **EVIDENCE:**
  - `-- muslim 1821 (num 4705/ar 1821.01) [The Book on Government]  :: …ت مع أبي على النبي صلى الله عليه وسلم فسمعته يقول " إن هذا الأمر لا ينقضي حتى يمضي فيهم اثنا عشر خليفة " . قال ثم تكلم بكلام خفي على - قال - فقلت لأبي ما قال قال " كلهم من قريش " .…`
  - `-- muslim 1822 (num 4711/ar 1822.01) [The Book on Government]  :: …وسلم يوم جمعة عشية رجم الأسلمي يقول " لا يزال الدين قائما حتى تقوم الساعة أو يكون عليكم اثنا عشر خليفة كلهم من قريش " . وسمعته يقول " عصيبة من المسلمين يفتتحون البيت الأبيض بيت كسرى أو آ…`
  - `-- bukhari 7222 (num 7222/ar 7222) []  :: …ا شعبة، عن عبد الملك، سمعت جابر بن سمرة، قال سمعت النبي صلى الله عليه وسلم يقول  " يكون اثنا عشر أميرا فقال كلمة لم أسمعها فقال أبي إنه قال كلهم من قريش ".…`
- **SOURCE:** Sahih Muslim 1821 (also 1822); Sahih al-Bukhari 7222 (Jabir b. Samura).
- **SOURCE_STATUS:** VERIFIED (live).
- **PROPOSED_ACTION:**
  Replace the bullet with:
  «•  বারো খলিফা — সহীহ মুসলিম, কিতাবুল ইমারাহ, হাদীস ১৮২১ («اثنا عشر خليفة… كلهم من قريش»); সহীহ বুখারি ৭২২২ («اثنا عشر أميرا… كلهم من قريش») — খাতার শব্দ মেলানো বাকি, PAGE-CHECK।»
  Register HAD-12-KHALIFA (REF-152, REF-240) uses the same citation.
- **PATCH_TYPE:** CORRECT_HADITH_NUMBER
- **CONFIDENCE:** HIGH
- **REQUIRES_HUMAN_REVIEW:** NO

### PB1-044

- **PATCH_ID:** PB1-044
- **PART:** 7
- **CHAPTER:** ০৩  কুরআনই কি যথেষ্ট নয়?
- **PAGE:** PAGE-CHECK (docx not available); ¶6048
- **PARAGRAPH/LOCATION:** Ledger REF-144 · Paragraph_Index 6048 · source-note bullet (chapter source block) · register HAD-BAB-FATIMA-SALAT
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  ছয় মাস ফজরে দরজায় ৩৩:৩৩ পাঠ (আনাস) — জামে তিরমিযি — PAGE-CHECK; কুরআন ৩৩:৩৩ — api.alquran.cloud, CONFIRMED।
- **PROBLEM:** Tirmidhi is cited without a number. The report is Tirmidhi 3206 and all three graders call it weak; no grade is printed (BUG-22).
- **EVIDENCE:**
  - `-- tirmidhi 3206 (num 3206/ar 3206) [Chapters on Tafsir] Ahmad Muhammad Shakir:Daif;Al-Albani:Daif;Zubair Ali Zai:Daif :: …مة، أخبرنا علي بن زيد، عن أنس بن مالك، أن رسول الله صلى الله عليه وسلم كان يمر بباب فاطمة ستة أشهر إذا خرج إلى صلاة الفجر يقول " الصلاة يا أهل البيت : ( إنما يريد الله ليذهب عنكم الر…`
- **SOURCE:** Jami' al-Tirmidhi 3206 (Anas).
- **SOURCE_STATUS:** VERIFIED (live); da'if (Shakir, Albani, Zubair).
- **PROPOSED_ACTION:**
  Replace the bullet with:
  «•  ছয় মাস ফজরে দরজায় ৩৩:৩৩ পাঠ (আনাস) — জামে তিরমিযি, হাদীস ৩২০৬ (সনদ দুর্বল — আলবানী, আহমাদ শাকির ও যুবাইর আলী যাঈ: যয়ীফ); কুরআন ৩৩:৩৩ — api.alquran.cloud, CONFIRMED।»
  Register HAD-BAB-FATIMA-SALAT (REF-187, 189, 269, 274).
- **PATCH_TYPE:** CORRECT_CITATION
- **CONFIDENCE:** HIGH
- **REQUIRES_HUMAN_REVIEW:** NO

### PB1-045

- **PATCH_ID:** PB1-045
- **PART:** 7
- **CHAPTER:** ০৪  এক বিয়ের ছয়টি বর্ণনা
- **PAGE:** PAGE-CHECK (docx not available); ¶6117
- **PARAGRAPH/LOCATION:** Ledger REF-145 · Paragraph_Index 6117 · source-note bullet (chapter source block)
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  নিচের আরবি পাঠ খাতা থেকে (¶3852–3877; খাতার কয়েকটি মুদ্রণ-ত্রুটি এখানে ঠিক করে লেখা — ছাপার আগে মূল কিতাবে মেলাতে হবে), বইয়ের নাম খাতায় নেই — PAGE-CHECK:
- **PROBLEM:** Audit and cleanup language sits inside a reader-facing source block: «খাতার কয়েকটি মুদ্রণ-ত্রুটি এখানে ঠিক করে লেখা — ছাপার আগে মূল কিতাবে মেলাতে হবে» (BUG-09/28).
- **EVIDENCE:**
  - Editorial; no source evidence required. Audit v1.1 BUG-28.
- **SOURCE:** Notebook ¶3852–3877 (book unnamed).
- **SOURCE_STATUS:** SOURCE-MISSING (book name) — PAGE-CHECK.
- **PROPOSED_ACTION:**
  Replace the bullet with:
  «•  নিচের আরবি পাঠ লেখকের খাতা থেকে; কিতাবের নাম ও খণ্ড-পৃষ্ঠা — PAGE-CHECK:»
  Move the remark about corrected misprints to the ledger Resolution_Note, listing each corrected word. The author decides whether the printed book should disclose the corrections.
- **PATCH_TYPE:** CORRECT_CITATION
- **CONFIDENCE:** MEDIUM
- **REQUIRES_HUMAN_REVIEW:** YES

### PB1-046

- **PATCH_ID:** PB1-046
- **PART:** 7
- **CHAPTER:** ০৫  বারোজন কারা, নূরের তাক কে?
- **PAGE:** PAGE-CHECK (docx not available); ¶6243
- **PARAGRAPH/LOCATION:** Ledger REF-152 · Paragraph_Index 6243 · source-note bullet (chapter source block) · register HAD-12-KHALIFA
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  বারো খলিফা — সহীহ মুসলিম (কিতাবুল ইমারাহ), বুখারি ৭২২২ — PAGE-CHECK।
- **PROBLEM:** DUPLICATE of REF-143 (HAD-12-KHALIFA). The Muslim number is missing and PAGE-CHECK stays on numbers that are now verified.
- **EVIDENCE:**
  - `-- muslim 1821 (num 4705/ar 1821.01) [The Book on Government]  :: …ت مع أبي على النبي صلى الله عليه وسلم فسمعته يقول " إن هذا الأمر لا ينقضي حتى يمضي فيهم اثنا عشر خليفة " . قال ثم تكلم بكلام خفي على - قال - فقلت لأبي ما قال قال " كلهم من قريش " .…`
  - `-- bukhari 7222 (num 7222/ar 7222) []  :: …ا شعبة، عن عبد الملك، سمعت جابر بن سمرة، قال سمعت النبي صلى الله عليه وسلم يقول  " يكون اثنا عشر أميرا فقال كلمة لم أسمعها فقال أبي إنه قال كلهم من قريش ".…`
- **SOURCE:** Sahih Muslim 1821; Sahih al-Bukhari 7222.
- **SOURCE_STATUS:** VERIFIED (live).
- **PROPOSED_ACTION:**
  Replace the bullet with the register-canonical form:
  «•  বারো খলিফা — সহীহ মুসলিম, কিতাবুল ইমারাহ, হাদীস ১৮২১ («اثنا عشر خليفة»); সহীহ বুখারি ৭২২২ («اثنا عشر أميرا»)।»
- **PATCH_TYPE:** CORRECT_HADITH_NUMBER
- **CONFIDENCE:** HIGH
- **REQUIRES_HUMAN_REVIEW:** NO

### PB1-047

- **PATCH_ID:** PB1-047
- **PART:** 7
- **CHAPTER:** ০৫  বারোজন কারা, নূরের তাক কে?
- **PAGE:** PAGE-CHECK (docx not available); ¶6244
- **PARAGRAPH/LOCATION:** Ledger REF-153 · Paragraph_Index 6244 · source-note bullet (chapter source block) · register HAD-BIDAA-MINNI
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  «ফাতিমা আমার অংশ…» — বুখারি ৩৭১৪ (শুধু «فمن أغضبها أغضبني»), বাকি অংশ — PAGE-CHECK।
- **PROBLEM:** DUPLICATE (HAD-BIDAA-MINNI). Bukhari 3714 carries only «فاطمة بضعة مني فمن أغضبها أغضبني». The «বাকি অংশ» is unidentified because the prose wording is not in the ledger. Only if that remainder is «يريبني ما رابها / يؤذيني ما آذاها» does it map to Muslim 2449 / Bukhari 5230. No «যে তাকে খুশি করে / يسرني ما يسرها» wording exists in the six books.
- **EVIDENCE:**
  - `-- bukhari 3714 (num 3714/ar 3714) [Companions of the Prophet]  :: …نار، عن ابن أبي مليكة، عن المسور بن مخرمة، أن رسول الله صلى الله عليه وسلم قال  " فاطمة بضعة مني، فمن أغضبها أغضبني ".…`
  - `-- muslim 2449 (num 6307/ar 2449.01) [The Book of the Merits of the Co]  :: …إلا أن يحب ابن أبي طالب أن يطلق ابنتي وينكح ابنتهم فإنما ابنتي بضعة مني يريبني ما رابها ويؤذيني ما آذاها " .…`
  - `-- bukhari 5230 (num 5230/ar 5230) [Wedlock, Marriage (Nikaah)]  :: …إلا أن يريد ابن أبي طالب أن يطلق ابنتي وينكح ابنتهم، فإنما هي بضعة مني، يريبني ما أرابها ويؤذيني ما آذاها ". هكذا قال.…`
  - `search «ما يسرها» (all six books) → (none)`
  - `search «يبسطني» (all six books) → (none)`
- **SOURCE:** Sahih al-Bukhari 3714 (canonical); Sahih Muslim 2449, Sahih al-Bukhari 5230 (only for the «يؤذيني ما آذاها» clause).
- **SOURCE_STATUS:** 3714: VERIFIED (live). Remaining clause: PAGE-CHECK.
- **PROPOSED_ACTION:**
  Replace the bullet with the register-canonical form:
  «•  «ফাতিমা আমার অংশ; যে তাকে রাগান্বিত করে, সে আমাকে রাগান্বিত করে» — সহীহ বুখারি ৩৭১৪ (শব্দ: «فاطمة بضعة مني فمن أغضبها أغضبني»); বাকি অংশ — বর্ণিত আছে, PAGE-CHECK।»
  If the remaining clause in the prose is «যা তাকে কষ্ট দেয়, তা আমাকে কষ্ট দেয়», add: «— সহীহ মুসলিম ২৪৪৯; সহীহ বুখারি ৫২৩০ («يؤذيني ما آذاها»)». Otherwise keep it PAGE-CHECK.
- **PATCH_TYPE:** CORRECT_CITATION
- **CONFIDENCE:** HIGH
- **REQUIRES_HUMAN_REVIEW:** YES

### PB1-048

- **PATCH_ID:** PB1-048
- **PART:** 7
- **CHAPTER:** ০৫  বারোজন কারা, নূরের তাক কে?
- **PAGE:** PAGE-CHECK (docx not available); ¶6246
- **PARAGRAPH/LOCATION:** Ledger REF-155 · Paragraph_Index 6246 · source-note bullet (chapter source block) · register HAD-UMM-ABIHA
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  উম্মে আবিহা — বর্ণিত আছে; PAGE-CHECK।
- **PROBLEM:** DUPLICATE (HAD-UMM-ABIHA, with REF-069 and REF-255). The three rows carry different levels of citation: «বর্ণিত আছে», «বর্ণিত আছে; PAGE-CHECK» and «বিহারুল আনওয়ার ৪৩». One canonical citation is needed.
- **EVIDENCE:**
  - `search «أم أبيها» (all six books) → (none)`
  - Isti'ab 4:1899 / Isaba 8:262 / Bihar 43:19 locations: KNOWLEDGE-ONLY (research layer / audit v1.1 candidate; not verifiable from this environment).
- **SOURCE:** Shia: al-Majlisi, Bihar al-Anwar 43 (from Maqatil al-Talibiyyin; Imam Ja'far al-Sadiq). Sunni candidates (Isti'ab, Isaba): CANDIDATE — not printed until locked.
- **SOURCE_STATUS:** CANDIDATE / SHIA-PAGE-CHECK — EDITION-LOCK PENDING. Not in the six books (live).
- **PROPOSED_ACTION:**
  Replace the bullet with the register-canonical form, which is the wording REF-255 already uses:
  «•  «উম্মু আবিহা» উপাধি — বর্ণিত আছে; বিহারুল আনওয়ার খণ্ড ৪৩, অধ্যায় ২ (মাকাতিলুত তালিবিয়্যিন থেকে, ইমাম জাফর আস-সাদিক (আলাইহিস্ সালাম)-এর সূত্রে) — PAGE-CHECK।»
- **PATCH_TYPE:** PRESERVE_WITH_PAGE_CHECK
- **CONFIDENCE:** MEDIUM
- **REQUIRES_HUMAN_REVIEW:** YES

### PB1-049

- **PATCH_ID:** PB1-049
- **PART:** 7
- **CHAPTER:** ০৬  মসজিদে বুরুল্লাহর আব্বুর সেই সকাল
- **PAGE:** PAGE-CHECK (docx not available); ¶6393
- **PARAGRAPH/LOCATION:** Ledger REF-157 · Paragraph_Index 6393 · source-note bullet (chapter source block) · register HAD-THAQALAYN
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  সাকালাইন («কিতাবুল্লাহ ও আমার ইতরাত, আহলুল বাইত») — মুসলিম ২৪০৮ (যায়েদ ইবনে আরকাম), তিরমিযি ৩৭৮৬ (জাবির), ৩৭৮৮ — CONFIRMED (S-173); আবু সাঈদ ও যায়েদ ইবনে সাবিতের বর্ণনা — PAGE-CHECK।
- **PROBLEM:** The bullet heading puts «ইতরাত» first and then lists Muslim 2408, but Muslim 2408's wording is «وأهل بيتي», not «عترتي». The graders of Tirmidhi 3786/3788 disagree, and the bullet does not say so (HAD-THAQALAYN normalisation; BUG-22/26).
- **EVIDENCE:**
  - `-- muslim 2408 (num 6225/ar 2408.01) [The Book of the Merits of the Co]  :: …الهدى والنور فخذوا بكتاب الله واستمسكوا به " . فحث على كتاب الله ورغب فيه ثم قال " وأهل بيتي أذكركم الله في أهل بيتي أذكركم الله في أهل بيتي أذكركم الله في أهل بيتي " . فقال له ح…`
  - `-- tirmidhi 3786 (num 3786/ar 3786) [Chapters on Virtues] Ahmad Muhammad Shakir:Sahih;Al-Albani:Sahih;Bashar Awad Maarouf:Hasan;Zubair Ali Zai:Daif :: …ء يخطب فسمعته يقول  " يا أيها الناس إني قد تركت فيكم ما إن أخذتم به لن تضلوا كتاب الله وعترتي أهل بيتي " .وفي الباب عن أبي ذر وأبي سعيد وزيد بن أرقم وحذيفة بن أسيد . وهذا حديث ح…`
  - `-- tirmidhi 3788 (num 3788/ar 3788) [Chapters on Virtues] Ahmad Muhammad Shakir:Sahih;Al-Albani:Sahih;Zubair Ali Zai:Daif :: …من الآخر كتاب الله حبل ممدود من السماء إلى الأرض وعترتي أهل بيتي ولن يتفرقا حتى يردا على الحوض فانظروا كيف تخلفوني فيهما " . هذا حديث حسن غريب .…`
- **SOURCE:** Sahih Muslim 2408 (Zayd b. Arqam); Jami' al-Tirmidhi 3786 (Jabir), 3788.
- **SOURCE_STATUS:** VERIFIED (live); 3786/3788 graders disagree.
- **PROPOSED_ACTION:**
  Replace the bullet with:
  «•  সাকালাইন («কিতাবুল্লাহ ও আমার ইতরাত, আহলুল বাইত») — সহীহ মুসলিম ২৪০৮ (যায়েদ ইবনে আরকাম; শব্দ «وأهل بيتي», «عترتي» নয়); জামে তিরমিযি ৩৭৮৬ (জাবির; «كتاب الله وعترتي أهل بيتي») ও ৩৭৮৮ («لن يتفرقا حتى يردا علي الحوض») — CONFIRMED (S-173); তিরমিযির দুই বর্ণনার মান নিয়ে মতভেদ (আলবানী ও আহমাদ শাকির: সহিহ; যুবাইর আলী যাঈ: যয়ীফ; ৩৭৮৬-এ বাশশার আওয়াদ: হাসান)। আবু সাঈদ ও যায়েদ ইবনে সাবিতের বর্ণনা — PAGE-CHECK।»
- **PATCH_TYPE:** CORRECT_CITATION
- **CONFIDENCE:** HIGH
- **REQUIRES_HUMAN_REVIEW:** YES

### PB1-050

- **PATCH_ID:** PB1-050
- **PART:** 7
- **CHAPTER:** ০৬  মসজিদে বুরুল্লাহর আব্বুর সেই সকাল
- **PAGE:** PAGE-CHECK (docx not available); ¶6395
- **PARAGRAPH/LOCATION:** Ledger REF-158 · Paragraph_Index 6395 · source-note bullet (chapter source block) · register HAD-QALAM
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  কাগজ-কলমের ঘটনা — সহীহ বুখারি (কিতাবুল ইলম, মাগাযি, মারাদুন নবী), মুসলিম; মুসনাদে আহমাদ ৩/৩৬৪; বিহারুল আনওয়ার ২২/৪৬৯; শেখ মুফিদ, আল-ইরশাদ — শ্রোতা ০৪-এর তালিকা, PAGE-CHECK।
- **PROBLEM:** The six-book references are given by chapter title only. The numbers are verified: Bukhari 114, 4431; Muslim 1637. The research layer gives Ahmad as 3/346 against the manuscript's 3/364; this is not resolvable here, so leave it PAGE-CHECK and do not change it.
- **EVIDENCE:**
  - `-- bukhari 114 (num 114/ar 114) [Knowledge]  :: …ن عبيد الله بن عبد الله، عن ابن عباس، قال لما اشتد بالنبي صلى الله عليه وسلم وجعه قال " ائتوني بكتاب أكتب لكم كتابا لا تضلوا بعده ". قال عمر إن النبي صلى الله عليه وسلم غلبه الوجع…`
  - `-- bukhari 4431 (num 4431/ar 4431) [Military Expeditions led by the ]  :: …ل قال ابن عباس يوم الخميس وما يوم الخميس اشتد برسول الله صلى الله عليه وسلم وجعه فقال " ائتوني أكتب لكم كتابا لن تضلوا بعده أبدا ". فتنازعوا، ولا ينبغي عند نبي تنازع، فقالوا ما شأن…`
  - `-- muslim 1637 (num 4232/ar 1637.01) [The Book of Wills]  :: …واللفظ لسعيد - قالوا حدثنا سفيان، عن سليمان الأحول، عن سعيد بن جبير، قال قال ابن عباس يوم الخميس وما يوم الخميس ثم بكى حتى بل دمعه الحصى . فقلت يا ابن عباس وما يوم الخميس قال اشتد برسو…`
- **SOURCE:** Sahih al-Bukhari 114, 4431; Sahih Muslim 1637; Musnad Ahmad 3/364 (PAGE-CHECK); Bihar 22/469; al-Irshad.
- **SOURCE_STATUS:** Six-book numbers VERIFIED (live); others PAGE-CHECK.
- **PROPOSED_ACTION:**
  Replace the bullet with:
  «•  কাগজ-কলমের ঘটনা — সহীহ বুখারি ১১৪ (কিতাবুল ইলম), ৪৪৩১ (মাগাযি) ও মারাদুন নবী অধ্যায়; সহীহ মুসলিম ১৬৩৭; মুসনাদে আহমাদ ৩/৩৬৪; বিহারুল আনওয়ার ২২/৪৬৯; শেখ মুফিদ, আল-ইরশাদ — শ্রোতা ০৪-এর তালিকা; আহমাদ, বিহার ও ইরশাদের খণ্ড-পৃষ্ঠা PAGE-CHECK।»
- **PATCH_TYPE:** CORRECT_HADITH_NUMBER
- **CONFIDENCE:** HIGH
- **REQUIRES_HUMAN_REVIEW:** NO

### PB1-051

- **PATCH_ID:** PB1-051
- **PART:** 7
- **CHAPTER:** ০৬  মসজিদে বুরুল্লাহর আব্বুর সেই সকাল
- **PAGE:** PAGE-CHECK (docx not available); ¶6396
- **PARAGRAPH/LOCATION:** Ledger REF-159 · Paragraph_Index 6396 · source-note bullet (chapter source block)
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  হুজরাত ১–১০ ও প্রথম দুই খলিফা — শ্রোতা ০৪ (আব্বুর মুখে), বর্ণিত আছে; PAGE-CHECK।
- **PROBLEM:** UNIDENTIFIED (BUG-25): no classical source located. The note is already attribution-only («বর্ণিত আছে») and carries no kitab name; prose that depends on it must not rise above «বর্ণিত আছে».
- **EVIDENCE:**
  - No source evidence exists in this repo for this row (audit v1.1 BUG-25 list). KNOWLEDGE-ONLY (research layer / audit v1.1 candidate; not verifiable from this environment).
- **SOURCE:** None located (ledger Candidate_Source: see CSV).
- **SOURCE_STATUS:** SOURCE-MISSING · বর্ণিত আছে · PRINT BLOCKED (book gate)
- **PROPOSED_ACTION:**
  Retain the current wording verbatim (no kitab name may be added). Author decides: keep as attribution-only, or delete the item (BUG-25). If a sanad is later found, re-open as ADD_SOURCE with PAGE-CHECK.
- **PATCH_TYPE:** PRESERVE_WITH_PAGE_CHECK
- **CONFIDENCE:** LOW
- **REQUIRES_HUMAN_REVIEW:** YES

### PB1-052

- **PATCH_ID:** PB1-052
- **PART:** 7
- **CHAPTER:** ০৮  কিতাবের জ্ঞান আছে কার কাছে?
- **PAGE:** PAGE-CHECK (docx not available); ¶6582
- **PARAGRAPH/LOCATION:** Ledger REF-164 · Paragraph_Index 6582 · source-note bullet (chapter source block) · register HAD-MADINAT-ILM
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  «আমি জ্ঞানের শহর, আলী তার দরজা» — PAGE-CHECK (তিরমিযি/হাকিম; নম্বর মেলানো বাকি)।
- **PROBLEM:** «তিরমিযি/হাকিম» are cited together for «আমি জ্ঞানের শহর». Tirmidhi does NOT carry «مدينة العلم», which appears nowhere in the six books. Tirmidhi 3723 is a different wording, «أنا دار الحكمة وعلي بابها», which Tirmidhi himself calls «غريب منكر» (BUG-18). The two wordings and their two sources must never be merged.
- **EVIDENCE:**
  - `search «مدينة العلم» (all six books) → (none)`
  - `-- tirmidhi 3723 (num 3723/ar 3723) [Chapters on Tafsir] Ahmad Muhammad Shakir:Daif;Al-Albani:Daif;Zubair Ali Zai:Daif :: …بن غفلة، عن الصنابحي، عن علي، رضى الله عنه قال قال رسول الله صلى الله عليه وسلم  " أنا دار الحكمة وعلي بابها " . هذا حديث غريب منكر . وروى بعضهم هذا الحديث عن شريك ولم يذكروا فيه عن…`
  - Hakim 3:126–127 (h. 4637–4639), Tabarani al-Kabir 11061, al-Khatib 11:48–50: KNOWLEDGE-ONLY (research layer / audit v1.1 candidate; not verifiable from this environment).
- **SOURCE:** al-Hakim, al-Mustadrak (CANDIDATE); al-Tabarani, al-Kabir (CANDIDATE) — for «مدينة العلم». Jami' al-Tirmidhi 3723 — for «دار الحكمة» only.
- **SOURCE_STATUS:** Tirmidhi 3723: VERIFIED (live), da'if (Shakir, Albani, Zubair) — Tirmidhi: «غريب منكر». Hakim/Tabarani: CANDIDATE — EDITION-LOCK PENDING. Register HAD-MADINAT-ILM.
- **PROPOSED_ACTION:**
  Replace the bullet with:
  «•  «আমি জ্ঞানের শহর, আলী তার দরজা» (أنا مدينة العلم وعلي بابها) — আল-হাকিম, আল-মুস্তাদরাক, ⟦edition⟧, খণ্ড ⟦ ⟧, হাদীস ⟦ ⟧; আত-তাবারানি, আল-মু'জামুল কাবির, হাদীস ⟦ ⟧ — PAGE-CHECK; এই শব্দে সিহাহ সিত্তায় নেই। জামে তিরমিযিতে ভিন্ন শব্দ: «আমি হিকমতের ঘর, আলী তার দরজা» (أنا دار الحكمة وعلي بابها) — হাদীস ৩৭২৩ (তিরমিযি: «غريب منكر»; আলবানী, আহমাদ শাকির ও যুবাইর আলী যাঈ: যয়ীফ)।»
- **PATCH_TYPE:** SPLIT_CLAIM
- **CONFIDENCE:** HIGH
- **REQUIRES_HUMAN_REVIEW:** YES

### PB1-053

- **PATCH_ID:** PB1-053
- **PART:** 7
- **CHAPTER:** ০৯  “ঈমানেরও কি দাম দিতে হয়?”
- **PAGE:** PAGE-CHECK (docx not available); ¶6673
- **PARAGRAPH/LOCATION:** Ledger REF-168 · Paragraph_Index 6673 · source-note bullet (chapter source block) · register HAD-MAHR-KHUMS
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  মা সাইয়্যিদার মোহর পৃথিবীর এক-পঞ্চমাংশ; জিবরাঈলের পায়ের আঘাতে পাঁচ নদী — ফিকহুর রেজা (খাতার উল্লেখ) — PAGE-CHECK।
- **PROBLEM:** DUPLICATE (HAD-MAHR-KHUMS). Here the item is attributed to Fiqh al-Rida («খাতার উল্লেখ»), while REF-057 states the same item as «মূল পাতা মেলানো হয়নি, তাই «বর্ণিত আছে»». Normalise to the weaker, documented status.
- **EVIDENCE:**
  - Fiqh al-Rida / Bihar 43:105 ff: KNOWLEDGE-ONLY (research layer / audit v1.1 candidate; not verifiable from this environment).
- **SOURCE:** Fiqh al-Rida (attribution as in the notebook); Bihar al-Anwar 43 (CANDIDATE).
- **SOURCE_STATUS:** SHIA-PAGE-CHECK — not opened; «বর্ণিত আছে».
- **PROPOSED_ACTION:**
  Replace the bullet with:
  «•  মা সাইয়্যিদার মোহর পৃথিবীর এক-পঞ্চমাংশ; জিবরাঈলের পায়ের আঘাতে পাঁচ নদী — লেখকের খাতায় ফিকহুর রেজা গ্রন্থের নামে আছে; মূল পাতা মেলানো হয়নি, তাই «বর্ণিত আছে» — PAGE-CHECK।»
- **PATCH_TYPE:** WEAKEN_ATTRIBUTION
- **CONFIDENCE:** MEDIUM
- **REQUIRES_HUMAN_REVIEW:** YES

### PB1-054

- **PATCH_ID:** PB1-054
- **PART:** 7
- **CHAPTER:** ১০  রোজ নামাজে কেন সরল পথ চাই
- **PAGE:** PAGE-CHECK (docx not available); ¶6739
- **PARAGRAPH/LOCATION:** Ledger REF-175 · Paragraph_Index 6739 · source-note bullet (chapter source block)
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  «সূর্য, চাঁদ, শুক্রতারা, দুই তারকা» — বর্ণিত আছে, PAGE-CHECK।
- **PROBLEM:** UNIDENTIFIED (BUG-25): no classical source located. The note is already attribution-only («বর্ণিত আছে») and carries no kitab name; prose that depends on it must not rise above «বর্ণিত আছে».
- **EVIDENCE:**
  - No source evidence exists in this repo for this row (audit v1.1 BUG-25 list). KNOWLEDGE-ONLY (research layer / audit v1.1 candidate; not verifiable from this environment).
- **SOURCE:** None located (ledger Candidate_Source: see CSV).
- **SOURCE_STATUS:** SOURCE-MISSING · বর্ণিত আছে · PRINT BLOCKED (book gate)
- **PROPOSED_ACTION:**
  Retain the current wording verbatim (no kitab name may be added). Author decides: keep as attribution-only, or delete the item (BUG-25). If a sanad is later found, re-open as ADD_SOURCE with PAGE-CHECK.
- **PATCH_TYPE:** PRESERVE_WITH_PAGE_CHECK
- **CONFIDENCE:** LOW
- **REQUIRES_HUMAN_REVIEW:** YES

---

## Part 8

### PB1-055

- **PATCH_ID:** PB1-055
- **PART:** 8
- **CHAPTER:** ০৩  আহলুল বাইত কারা, রাসূলুল্লাহ ﷺ নিজেই দেখালেন
- **PAGE:** PAGE-CHECK (docx not available); ¶7045
- **PARAGRAPH/LOCATION:** Ledger REF-186 · Paragraph_Index 7045 · source-note bullet (chapter source block) · register HAD-KISA
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  উম্মে সালামার ঘরে চাদর; «তুমি স্বস্থানে, কল্যাণের মধ্যে» — উমর ইবনে আবি সালামার সূত্রে জামে তিরমিযি — PAGE-CHECK (নম্বর মেলানো বাকি)।
- **PROBLEM:** Tirmidhi is cited without a number. The wording «أنت على مكانك وأنت على خير» is Tirmidhi 3205 (Umar b. Abi Salama). 3787 is the same report with «وأنت إلي خير».
- **EVIDENCE:**
  - `-- tirmidhi 3205 (num 3205/ar 3205) [Chapters on Tafsir] Ahmad Muhammad Shakir:Sahih;Al-Albani:Sahih;Zubair Ali Zai:Sahih :: …يتي فأذهب عنهم الرجس وطهرهم تطهيرا " . قالت أم سلمة وأنا معهم يا نبي الله قال " أنت على مكانك وأنت على خير " . قال هذا حديث غريب من هذا الوجه من حديث عطاء عن عمر بن أبي سلمة .…`
  - `-- tirmidhi 3787 (num 3787/ar 3787) [Chapters on Virtues] Ahmad Muhammad Shakir:Sahih;Al-Albani:Sahih;Zubair Ali Zai:Sahih :: …يتي فأذهب عنهم الرجس وطهرهم تطهيرا " . قالت أم سلمة وأنا معهم يا نبي الله قال " أنت على مكانك وأنت إلي خير " . وفي الباب عن أم سلمة ومعقل بن يسار وأبي الحمراء وأنس بن مالك . وهذا…`
- **SOURCE:** Jami' al-Tirmidhi 3205, 3787 (Umar b. Abi Salama).
- **SOURCE_STATUS:** VERIFIED (live); sahih (Shakir, Albani, Zubair).
- **PROPOSED_ACTION:**
  Replace the bullet with:
  «•  উম্মে সালামার ঘরে চাদর; «তুমি স্বস্থানে, কল্যাণের মধ্যে» — উমর ইবনে আবি সালামার সূত্রে জামে তিরমিযি ৩২০৫ (একই বর্ণনা ৩৭৮৭-এ «وأنت إلي خير» শব্দে)।»
- **PATCH_TYPE:** CORRECT_HADITH_NUMBER
- **CONFIDENCE:** HIGH
- **REQUIRES_HUMAN_REVIEW:** NO

### PB1-056

- **PATCH_ID:** PB1-056
- **PART:** 8
- **CHAPTER:** ০৪  মা সাইয়্যিদা ফাতিমাতুয্ যাহরা (আলাইহাস্ সালাম)-এর মুখে চাদরের ঘটনা
- **PAGE:** PAGE-CHECK (docx not available); ¶7109
- **PARAGRAPH/LOCATION:** Ledger REF-188 · Paragraph_Index 7109 · source-note bullet (chapter source block) · register HAD-KISA
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  কিসার সংক্ষিপ্ত রূপ (উম্মে সালামা ও আয়িশার সূত্রে) — সহীহ মুসলিম ২৪২৪ — CONFIRMED (SECOND_NOTEBOOK/CITATION_RISK; D-017); তিরমিযি, মুস্তাদরাক, বায়হাকী, দুররে মানসুর, শাওয়াহিদুত তানযীল, মুসনাদে আহমাদ (খাতার তালিকা) — PAGE-CHECK।
  Relevant clause: «কিসার সংক্ষিপ্ত রূপ (উম্মে সালামা ও আয়িশার সূত্রে) — সহীহ মুসলিম ২৪২৪ — CONFIRMED (SECOND_NOTEBOOK/CITATION_RISK; D-017);»
- **PROBLEM:** Muslim 2424 is attributed to «উম্মে সালামা ও আয়িশার সূত্রে», but Muslim 2424 is Aisha's report only. Umm Salama's short kisa report is Tirmidhi 3871 («إنك على خير»; Tirmidhi: hasan sahih).
- **EVIDENCE:**
  - `-- muslim 2424 (num 6261/ar 2424) [The Book of the Merits of the Co]  :: …ن مصعب بن شيبة، عن صفية بنت شيبة، قالت قالت عائشة خرج النبي صلى الله عليه وسلم غداة وعليه مرط مرحل من شعر أسود فجاء الحسن بن علي فأدخله ثم جاء الحسين فدخل معه ثم جاءت فاطمة فأدخلها ثم جاء…`
  - `-- tirmidhi 3871 (num 3871/ar 3871) [Chapters on Virtues] Ahmad Muhammad Shakir:Sahih;Al-Albani:Sahih;Bashar Awad Maarouf:Hasan Sahih;Zubair Ali Zai:Hasan :: …وخاصتي أذهب عنهم الرجس وطهرهم تطهيرا " . فقالت أم سلمة وأنا معهم يا رسول الله قال " إنك على خير " . هذا حديث حسن صحيح وهو أحسن شيء روي في هذا الباب . وفي الباب عن عمر بن أبي سلمة و…`
- **SOURCE:** Sahih Muslim 2424 (Aisha); Jami' al-Tirmidhi 3871 (Umm Salama).
- **SOURCE_STATUS:** VERIFIED (live).
- **PROPOSED_ACTION:**
  Replace that clause with:
  «কিসার সংক্ষিপ্ত রূপ — আয়িশার সূত্রে সহীহ মুসলিম ২৪২৪ — CONFIRMED; উম্মে সালামার সূত্রে জামে তিরমিযি ৩৮৭১ — CONFIRMED;»
  The rest of the bullet (other works — PAGE-CHECK) is unchanged.
- **PATCH_TYPE:** CORRECT_CITATION
- **CONFIDENCE:** HIGH
- **REQUIRES_HUMAN_REVIEW:** NO

### PB1-057

- **PATCH_ID:** PB1-057
- **PART:** 8
- **CHAPTER:** ০৯  “আমি কি এমন কারও ইবাদত করব, যাঁকে দেখিনি?”
- **PAGE:** PAGE-CHECK (docx not available); ¶7421
- **PARAGRAPH/LOCATION:** Ledger REF-196 · Paragraph_Index 7421 · source-note bullet (chapter source block)
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  «সাত আসমানের আড়ালে লুক্কায়িত» শপথকারীকে তিরস্কার — বর্ণিত আছে, PAGE-CHECK।
- **PROBLEM:** UNIDENTIFIED (BUG-25): no classical source located. The note is already attribution-only («বর্ণিত আছে») and carries no kitab name; prose that depends on it must not rise above «বর্ণিত আছে».
- **EVIDENCE:**
  - No source evidence exists in this repo for this row (audit v1.1 BUG-25 list). KNOWLEDGE-ONLY (research layer / audit v1.1 candidate; not verifiable from this environment).
- **SOURCE:** None located (ledger Candidate_Source: see CSV).
- **SOURCE_STATUS:** SOURCE-MISSING · বর্ণিত আছে · PRINT BLOCKED (book gate)
- **PROPOSED_ACTION:**
  Retain the current wording verbatim (no kitab name may be added). Author decides: keep as attribution-only, or delete the item (BUG-25). If a sanad is later found, re-open as ADD_SOURCE with PAGE-CHECK.
- **PATCH_TYPE:** PRESERVE_WITH_PAGE_CHECK
- **CONFIDENCE:** LOW
- **REQUIRES_HUMAN_REVIEW:** YES

### PB1-058

- **PATCH_ID:** PB1-058
- **PART:** 8
- **CHAPTER:** ১০  রাসূলুল্লাহ ﷺ-এর বিছানায় ইমাম আলী (আলাইহিস্ সালাম)
- **PAGE:** PAGE-CHECK (docx not available); ¶7478
- **PARAGRAPH/LOCATION:** Ledger REF-199 · Paragraph_Index 7478 · source-note bullet (chapter source block)
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  কুরাইশদের ভুলের কারণ «একই নূর» — বিহারুল আনওয়ার, ৫ম খণ্ড (খাতার উল্লেখ) — PAGE-CHECK।
- **PROBLEM:** The UNIDENTIFIED row carries a kitab name («বিহারুল আনওয়ার, ৫ম খণ্ড (খাতার উল্লেখ)»), but the text has not been located in Bihar 5. Under BUG-25, no UNID item may carry a kitab name.
- **EVIDENCE:**
  - No evidence in repo; ledger Candidate_Source: «Bihar vol. 5 citation unclear». KNOWLEDGE-ONLY (research layer / audit v1.1 candidate; not verifiable from this environment).
- **SOURCE:** Notebook mention: Bihar al-Anwar vol. 5 (not located).
- **SOURCE_STATUS:** SOURCE-MISSING.
- **PROPOSED_ACTION:**
  Replace the bullet with:
  «•  কুরাইশদের ভুলের কারণ «একই নূর» — বর্ণিত আছে।»
  Keep «বিহারুল আনওয়ার খণ্ড ৫ (খাতার উল্লেখ, মেলানো যায়নি)» in the ledger only. Restore it to print only with a located vol/page/hadith.
- **PATCH_TYPE:** WEAKEN_ATTRIBUTION
- **CONFIDENCE:** LOW
- **REQUIRES_HUMAN_REVIEW:** YES

### PB1-059

- **PATCH_ID:** PB1-059
- **PART:** 8
- **CHAPTER:** ১১  স্বপ্নে রাসূলুল্লাহ ﷺ-কে দেখলে কী হয়?
- **PAGE:** PAGE-CHECK (docx not available); ¶7522
- **PARAGRAPH/LOCATION:** Ledger REF-201 · Paragraph_Index 7522 · source-note bullet (chapter source block) · register HAD-RUYA
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  «যে স্বপ্নে আমাকে দেখল, সে সত্যিই আমাকে দেখল» — বর্ণিত আছে, PAGE-CHECK (বুখারি/মুসলিম; নম্বর মেলানো বাকি)।
- **PROBLEM:** The note is left as «বর্ণিত আছে, PAGE-CHECK (বুখারি/মুসলিম; নম্বর মেলানো বাকি)», but the exact wording is Bukhari 110 and Muslim 2266 (register HAD-RUYA with REF-013).
- **EVIDENCE:**
  - `-- bukhari 110 (num 110/ar 110) [Knowledge]  :: …صالح، عن أبي هريرة، عن النبي صلى الله عليه وسلم قال  " تسموا باسمي ولا تكتنوا بكنيتي، ومن رآني في المنام فقد رآني، فإن الشيطان لا يتمثل في صورتي، ومن كذب على متعمدا فليتبوأ مقعده من ال…`
  - `-- muslim 2266 (num 5919/ar 2266.01) [The Book of Dreams]  :: …زيد - حدثنا أيوب، وهشام، عن محمد، عن أبي هريرة، قال قال رسول الله صلى الله عليه وسلم  " من رآني في المنام فقد رآني فإن الشيطان لا يتمثل بي " .…`
- **SOURCE:** Sahih al-Bukhari 110; Sahih Muslim 2266 (Abu Hurayra).
- **SOURCE_STATUS:** VERIFIED (live).
- **PROPOSED_ACTION:**
  Replace the bullet with:
  «•  «যে স্বপ্নে আমাকে দেখল, সে সত্যিই আমাকে দেখল» — সহীহ বুখারী ১১০; সহীহ মুসলিম ২২৬৬ (আবু হুরাইরা)।»
- **PATCH_TYPE:** CORRECT_HADITH_NUMBER
- **CONFIDENCE:** HIGH
- **REQUIRES_HUMAN_REVIEW:** NO

---

## Part 9

### PB1-060

- **PATCH_ID:** PB1-060
- **PART:** 9
- **CHAPTER:** ০১  হেদায়াত দেখতে কেমন?
- **PAGE:** PAGE-CHECK (docx not available); ¶7731
- **PARAGRAPH/LOCATION:** Ledger REF-206 · Paragraph_Index 7731 · source-note bullet (chapter source block) · register HAD-THAQALAYN
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  সাকালাইনের হাদীস: «কিতাবুল্লাহ ও আহলুল বাইত» সহীহ মুসলিম ২৪০৮ (শব্দ «أهل بيتي»; CONFIRMED, সংস্করণ-পাঠ); «যদি আঁকড়ে ধরো, কখনো বিভ্রান্ত হবে না» অংশটি জামে তিরমিযি ৩৭৮৬ («كتاب الله وعترتي أهل بيتي», হাসান গরিব; CONFIRMED, সংস্করণ-পাঠ; মান নিয়ে মতভেদ আছে)। খাতার «তিরমিযি ৩৭৮৮» PAGE-CHECK।
  Relevant clause: «খাতার «তিরমিযি ৩৭৮৮» PAGE-CHECK।»
- **PROBLEM:** The note leaves «খাতার «তিরমিযি ৩৭৮৮» PAGE-CHECK», but 3788 is now verified («لن يتفرقا حتى يردا علي الحوض»). Its graders disagree, and the book must say so (HAD-THAQALAYN).
- **EVIDENCE:**
  - `-- tirmidhi 3788 (num 3788/ar 3788) [Chapters on Virtues] Ahmad Muhammad Shakir:Sahih;Al-Albani:Sahih;Zubair Ali Zai:Daif :: …من الآخر كتاب الله حبل ممدود من السماء إلى الأرض وعترتي أهل بيتي ولن يتفرقا حتى يردا على الحوض فانظروا كيف تخلفوني فيهما " . هذا حديث حسن غريب .…`
- **SOURCE:** Jami' al-Tirmidhi 3788.
- **SOURCE_STATUS:** VERIFIED (live); Shakir/Albani sahih, Zubair da'if.
- **PROPOSED_ACTION:**
  Replace that closing clause with:
  «খাতার «তিরমিযি ৩৭৮৮» — CONFIRMED («عترتي أهل بيتي… لن يتفرقا حتى يردا علي الحوض»; মান নিয়ে মতভেদ: আলবানী ও আহমাদ শাকির: সহিহ; যুবাইর আলী যাঈ: যয়ীফ)।»
- **PATCH_TYPE:** CORRECT_CITATION
- **CONFIDENCE:** HIGH
- **REQUIRES_HUMAN_REVIEW:** YES

### PB1-061

- **PATCH_ID:** PB1-061
- **PART:** 9
- **CHAPTER:** ০১  হেদায়াত দেখতে কেমন?
- **PAGE:** PAGE-CHECK (docx not available); ¶7732
- **PARAGRAPH/LOCATION:** Ledger REF-207 · Paragraph_Index 7732 · source-note bullet (chapter source block) · register HAD-MADINAT-ILM
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  «আমি জ্ঞানের শহর, আলী তার দরজা» — বর্ণিত আছে; PAGE-CHECK (কিতাব-খণ্ড-পৃষ্ঠা লাগবে)।
- **PROBLEM:** DUPLICATE (HAD-MADINAT-ILM). This row gives no book, while REF-309 names Hakim and Tirmidhi. The register canonical is al-Hakim (PAGE-CHECK). Tirmidhi must not be named for this wording.
- **EVIDENCE:**
  - `search «مدينة العلم» (all six books) → (none)`
  - Hakim locations: KNOWLEDGE-ONLY (research layer / audit v1.1 candidate; not verifiable from this environment).
- **SOURCE:** al-Hakim, al-Mustadrak (CANDIDATE).
- **SOURCE_STATUS:** CANDIDATE — EDITION-LOCK PENDING.
- **PROPOSED_ACTION:**
  Replace the bullet with:
  «•  «আমি জ্ঞানের শহর, আলী তার দরজা» — বর্ণিত আছে; আল-হাকিম, আল-মুস্তাদরাক, ⟦edition⟧, খণ্ড ⟦ ⟧, হাদীস ⟦ ⟧ — PAGE-CHECK; এই শব্দে সিহাহ সিত্তায় নেই (তিরমিযি ৩৭২৩-এর শব্দ ভিন্ন: «দারুল হিকমা»)।»
- **PATCH_TYPE:** ADD_SOURCE
- **CONFIDENCE:** MEDIUM
- **REQUIRES_HUMAN_REVIEW:** YES

### PB1-062

- **PATCH_ID:** PB1-062
- **PART:** 9
- **CHAPTER:** ০১  হেদায়াত দেখতে কেমন?
- **PAGE:** PAGE-CHECK (docx not available); ¶7733
- **PARAGRAPH/LOCATION:** Ledger REF-208 · Paragraph_Index 7733 · source-note bullet (chapter source block) · register HAD-SAFINA
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  কিশতীর হাদীস («যে চড়বে, সে নাজাত পাবে») — বর্ণিত আছে; PAGE-CHECK।
- **PROBLEM:** DUPLICATE (HAD-SAFINA). This row gives no book. The register canonical is al-Hakim / al-Tabarani (PAGE-CHECK), never «মুসনাদে আহমদ ৩৭৮৬» (see REF-011).
- **EVIDENCE:**
  - `search «سفينة نوح» (all six books) → (none)`
  - Hakim/Tabarani locations: KNOWLEDGE-ONLY (research layer / audit v1.1 candidate; not verifiable from this environment).
- **SOURCE:** al-Hakim, al-Mustadrak; al-Tabarani (CANDIDATE).
- **SOURCE_STATUS:** CANDIDATE — EDITION-LOCK PENDING.
- **PROPOSED_ACTION:**
  Replace the bullet with:
  «•  কিশতীর হাদীস («যে চড়বে, সে নাজাত পাবে») — বর্ণিত আছে; আল-হাকিম, আল-মুস্তাদরাক, খণ্ড ⟦ ⟧, হাদীস ⟦ ⟧; আত-তাবারানি, ⟦গ্রন্থ⟧, হাদীস ⟦ ⟧ — PAGE-CHECK; সিহাহ সিত্তায় নেই।»
- **PATCH_TYPE:** ADD_SOURCE
- **CONFIDENCE:** MEDIUM
- **REQUIRES_HUMAN_REVIEW:** YES

### PB1-063

- **PATCH_ID:** PB1-063
- **PART:** 9
- **CHAPTER:** ০১  হেদায়াত দেখতে কেমন?
- **PAGE:** PAGE-CHECK (docx not available); ¶7735
- **PARAGRAPH/LOCATION:** Ledger REF-209 · Paragraph_Index 7735 · source-note bullet (chapter source block)
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  «আমাকে ভালোবাসো, তার আগে আমার রাসূলকে… ওলিকে» — বর্ণিত আছে; উৎস পাওয়া যায়নি, PAGE-CHECK।
- **PROBLEM:** UNIDENTIFIED (BUG-25): no classical source located. The note is already attribution-only («বর্ণিত আছে») and carries no kitab name; prose that depends on it must not rise above «বর্ণিত আছে». Prose REF-205 (¶7687) keeps «বর্ণিত আছে, আল্লাহ বলেছেন…» — matches.
- **EVIDENCE:**
  - No source evidence exists in this repo for this row (audit v1.1 BUG-25 list). KNOWLEDGE-ONLY (research layer / audit v1.1 candidate; not verifiable from this environment).
- **SOURCE:** None located (ledger Candidate_Source: see CSV).
- **SOURCE_STATUS:** SOURCE-MISSING · বর্ণিত আছে · PRINT BLOCKED (book gate)
- **PROPOSED_ACTION:**
  Retain the current wording verbatim (no kitab name may be added). Author decides: keep as attribution-only, or delete the item (BUG-25). If a sanad is later found, re-open as ADD_SOURCE with PAGE-CHECK.
- **PATCH_TYPE:** PRESERVE_WITH_PAGE_CHECK
- **CONFIDENCE:** LOW
- **REQUIRES_HUMAN_REVIEW:** YES

### PB1-064

- **PATCH_ID:** PB1-064
- **PART:** 9
- **CHAPTER:** ০৩  জন্মদিনের কেক কি বিদআত?
- **PAGE:** PAGE-CHECK (docx not available); ¶7917
- **PARAGRAPH/LOCATION:** Ledger REF-215 · Paragraph_Index 7917 · prose / dialogue line
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > “বর্ণিত আছে, একবার অতীতের যুগে এক ব্যক্তি হালাল উপায়ে দুনিয়া অর্জনের চেষ্টা করল, কিন্তু তাতে সফল হতে পারল না। সে হারাম উপায়েও চেষ্টা করল, কিন্তু তাতেও সফল হলো না।
- **PROBLEM:** UNIDENTIFIED (BUG-25): no classical source located. The note is already attribution-only («বর্ণিত আছে») and carries no kitab name; prose that depends on it must not rise above «বর্ণিত আছে». This row is itself a prose line, already in «বর্ণিত আছে» form.
- **EVIDENCE:**
  - No source evidence exists in this repo for this row (audit v1.1 BUG-25 list). KNOWLEDGE-ONLY (research layer / audit v1.1 candidate; not verifiable from this environment).
- **SOURCE:** None located (ledger Candidate_Source: see CSV).
- **SOURCE_STATUS:** SOURCE-MISSING · বর্ণিত আছে · PRINT BLOCKED (book gate)
- **PROPOSED_ACTION:**
  Retain the current wording verbatim (no kitab name may be added). Author decides: keep as attribution-only, or delete the item (BUG-25). If a sanad is later found, re-open as ADD_SOURCE with PAGE-CHECK.
- **PATCH_TYPE:** PRESERVE_WITH_PAGE_CHECK
- **CONFIDENCE:** LOW
- **REQUIRES_HUMAN_REVIEW:** YES

### PB1-065

- **PATCH_ID:** PB1-065
- **PART:** 9
- **CHAPTER:** ০৩  জন্মদিনের কেক কি বিদআত?
- **PAGE:** PAGE-CHECK (docx not available); ¶8010
- **PARAGRAPH/LOCATION:** Ledger REF-219 · Paragraph_Index 8010 · source-note bullet (chapter source block)
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  শিকল-পরা লোকের ঘটনা — বর্ণিত আছে; আল-কাফিতে পাওয়া যায়নি (লগ B3), উৎস PAGE-CHECK।
- **PROBLEM:** UNIDENTIFIED (BUG-25): no classical source located. The note is already attribution-only («বর্ণিত আছে») and carries no kitab name; prose that depends on it must not rise above «বর্ণিত আছে». Strip the internal «(লগ B3)» marker in the BUG-10 pass.
- **EVIDENCE:**
  - No source evidence exists in this repo for this row (audit v1.1 BUG-25 list). KNOWLEDGE-ONLY (research layer / audit v1.1 candidate; not verifiable from this environment).
- **SOURCE:** None located (ledger Candidate_Source: see CSV).
- **SOURCE_STATUS:** SOURCE-MISSING · বর্ণিত আছে · PRINT BLOCKED (book gate)
- **PROPOSED_ACTION:**
  Retain the current wording verbatim (no kitab name may be added). Author decides: keep as attribution-only, or delete the item (BUG-25). If a sanad is later found, re-open as ADD_SOURCE with PAGE-CHECK.
- **PATCH_TYPE:** PRESERVE_WITH_PAGE_CHECK
- **CONFIDENCE:** LOW
- **REQUIRES_HUMAN_REVIEW:** YES

### PB1-066

- **PATCH_ID:** PB1-066
- **PART:** 9
- **CHAPTER:** ০৩  জন্মদিনের কেক কি বিদআত?
- **PAGE:** PAGE-CHECK (docx not available); ¶8011
- **PARAGRAPH/LOCATION:** Ledger REF-220 · Paragraph_Index 8011 · source-note bullet (chapter source block) · register HAD-RIDA-3SUNAN
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  ইমাম আল-রেযা (আলাইহিস্ সালাম)-এর «তিন সুন্নাহ» — বর্ণিত আছে; PAGE-CHECK।
- **PROBLEM:** DUPLICATE (HAD-RIDA-3SUNAN, with REF-089 and REF-216). REF-089 cites al-Kafi 2 and 'Uyun Akhbar al-Rida; this row gives no book. Normalise to one citation.
- **EVIDENCE:**
  - al-Kafi 2:241 h. 39; 'Uyun 1:256: KNOWLEDGE-ONLY (research layer / audit v1.1 candidate; not verifiable from this environment).
- **SOURCE:** al-Kulayni, al-Kafi vol. 2; al-Saduq, 'Uyun Akhbar al-Rida (CANDIDATE).
- **SOURCE_STATUS:** SHIA-PAGE-CHECK — EDITION-LOCK PENDING.
- **PROPOSED_ACTION:**
  Replace the bullet with:
  «•  ইমাম আল-রেযা (আলাইহিস্ সালাম)-এর «তিন সুন্নাহ» — বর্ণিত আছে; আল-কাফি, খণ্ড ২ ও উয়ূনু আখবারির রিদা — PAGE-CHECK (ভাগ ৪, অধ্যায় ০৬-এর টীকার একই সূত্র)।»
- **PATCH_TYPE:** ADD_SOURCE
- **CONFIDENCE:** MEDIUM
- **REQUIRES_HUMAN_REVIEW:** YES

### PB1-067

- **PATCH_ID:** PB1-067
- **PART:** 9
- **CHAPTER:** ০৪  যা বলি, তা কি নিজে করি?
- **PAGE:** PAGE-CHECK (docx not available); ¶8050
- **PARAGRAPH/LOCATION:** Ledger REF-222 · Paragraph_Index 8050 · prose / dialogue line
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > ইবনু আব্বাস হতে বর্ণিত আছে, রাসূলুল্লাহ ﷺ বলেন: নিশ্চিতভাবে যা তোমাদের জানা আছে তা ব্যতীত আমার নিকট হতে হাদীস বর্ণনা করা থেকে তোমরা নিবৃত্ত থাকবে। কারণ যে ব্যক্তি ইচ্ছাকৃতভাবে আমার প্রতি মিথ্যা আরোপ করে সে যেন জাহান্নামকে নিজের আবাস বানিয়ে নিল। আর যে ব্যক্তি নিজের খেয়াল মর্জিমত কুরআন প্রসঙ্গে কথা বলে সেও যেন জাহান্নামকে নিজের গৃহ বানিয়ে নিল।
  Relevant clause: «ইবনু আব্বাস হতে বর্ণিত আছে, রাসূলুল্লাহ ﷺ বলেন:»
- **PROBLEM:** The prose quotes the report in the standard hadith formula («ইবনু আব্বাস হতে বর্ণিত আছে, রাসূলুল্লাহ ﷺ বলেন:»), which presents it as an ordinary sound hadith. Its source, Tirmidhi 2951 (REF-223), is graded da'if by Shakir, Albani and Zubair. A weak report may not stand as a flat «রাসূল ﷺ বলেছেন» (BUG-22).
- **EVIDENCE:**
  - `-- tirmidhi 2951 (num 2951/ar 2951) [Chapters on Tafsir] Ahmad Muhammad Shakir:Daif;Al-Albani:Daif;Zubair Ali Zai:Daif :: …عوانة، عن عبد الأعلى، عن سعيد بن جبير، عن ابن عباس، عن النبي صلى الله عليه وسلم قال  " اتقوا الحديث عني إلا ما علمتم فمن كذب على متعمدا فليتبوأ مقعده من النار ومن قال في القرآن برأيه فليتبو…`
- **SOURCE:** Jami' al-Tirmidhi 2951 (Ibn Abbas).
- **SOURCE_STATUS:** VERIFIED (live); da'if.
- **PROPOSED_ACTION:**
  Change only the attribution clause to:
  «তিরমিযির একটি বর্ণনায় (সনদ দুর্বল) ইবনু আব্বাস থেকে এসেছে, রাসূলুল্লাহ ﷺ বলেন:»
  The quoted words that follow are unchanged.
- **PATCH_TYPE:** WEAKEN_ATTRIBUTION
- **CONFIDENCE:** HIGH
- **REQUIRES_HUMAN_REVIEW:** YES

### PB1-068

- **PATCH_ID:** PB1-068
- **PART:** 9
- **CHAPTER:** ০৪  যা বলি, তা কি নিজে করি?
- **PAGE:** PAGE-CHECK (docx not available); ¶8109
- **PARAGRAPH/LOCATION:** Ledger REF-223 · Paragraph_Index 8109 · source-note bullet (chapter source block)
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  ইবনে আব্বাসের হাদীস («যা জানা আছে তা ছাড়া হাদীস বর্ণনা থেকে বিরত থাকো… খেয়াল মর্জিমত কুরআন প্রসঙ্গে কথা বলে») — জামে তিরমিযি, তাফসির অধ্যায় (২৯৫০/২৯৫১, সংস্করণভেদে); PAGE-CHECK।
- **PROBLEM:** The note gives «২৯৫০/২৯৫১, সংস্করণভেদে». The wording quoted («যা জানা আছে তা ছাড়া… খেয়াল মর্জিমত») is 2951, not 2950, which is a different hadith («بغير علم»; see REF-224). No grade is printed.
- **EVIDENCE:**
  - `-- tirmidhi 2951 (num 2951/ar 2951) [Chapters on Tafsir] Ahmad Muhammad Shakir:Daif;Al-Albani:Daif;Zubair Ali Zai:Daif :: …عوانة، عن عبد الأعلى، عن سعيد بن جبير، عن ابن عباس، عن النبي صلى الله عليه وسلم قال  " اتقوا الحديث عني إلا ما علمتم فمن كذب على متعمدا فليتبوأ مقعده من النار ومن قال في القرآن برأيه فليتبو…`
  - `-- tirmidhi 2950 (num 2950/ar 2950) [Chapters on Tafsir] Ahmad Muhammad Shakir:Daif;Al-Albani:Daif;Zubair Ali Zai:Daif :: …ر، عن ابن عباس، رضى الله عنهما قال قال رسول الله صلى الله عليه وسلم  " من قال في القرآن بغير علم فليتبوأ مقعده من النار " . قال أبو عيسى هذا حديث حسن صحيح .…`
- **SOURCE:** Jami' al-Tirmidhi 2951 (Ibn Abbas).
- **SOURCE_STATUS:** VERIFIED (live); da'if (Shakir, Albani, Zubair).
- **PROPOSED_ACTION:**
  Replace the bullet with:
  «•  ইবনে আব্বাসের হাদীস («যা জানা আছে তা ছাড়া হাদীস বর্ণনা থেকে বিরত থাকো… খেয়াল মর্জিমত কুরআন প্রসঙ্গে কথা বলে») — জামে তিরমিযি, তাফসির অধ্যায়, হাদীস ২৯৫১ (সনদ দুর্বল — আলবানী, আহমাদ শাকির ও যুবাইর আলী যাঈ: যয়ীফ)।»
- **PATCH_TYPE:** CORRECT_HADITH_NUMBER
- **CONFIDENCE:** HIGH
- **REQUIRES_HUMAN_REVIEW:** NO

### PB1-069

- **PATCH_ID:** PB1-069
- **PART:** 9
- **CHAPTER:** ০৪  যা বলি, তা কি নিজে করি?
- **PAGE:** PAGE-CHECK (docx not available); ¶8110
- **PARAGRAPH/LOCATION:** Ledger REF-224 · Paragraph_Index 8110 · source-note bullet (chapter source block)
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  «যে ব্যক্তি সঠিক ইলম ব্যতীত কুরআন প্রসঙ্গে কোন কথা বলে…» (REV1-এ ফেরানো, ¶12200) — বর্ণিত আছে; PAGE-CHECK (তিরমিযি তাফসির অধ্যায় হতে পারে)।
- **PROBLEM:** The ledger treats this as a duplicate of REF-223 (2951). Live text shows that the quoted wording «সঠিক ইলম ব্যতীত» = «بغير علم» is Tirmidhi 2950, a separate hadith. The internal marker «(REV1-এ ফেরানো, ¶12200)» belongs in the ledger. Grades disagree: Tirmidhi says «حسن صحيح», while modern graders say da'if.
- **EVIDENCE:**
  - `-- tirmidhi 2950 (num 2950/ar 2950) [Chapters on Tafsir] Ahmad Muhammad Shakir:Daif;Al-Albani:Daif;Zubair Ali Zai:Daif :: …ر، عن ابن عباس، رضى الله عنهما قال قال رسول الله صلى الله عليه وسلم  " من قال في القرآن بغير علم فليتبوأ مقعده من النار " . قال أبو عيسى هذا حديث حسن صحيح .…`
- **SOURCE:** Jami' al-Tirmidhi 2950 (Ibn Abbas).
- **SOURCE_STATUS:** VERIFIED (live). Ledger register note («same as 223») CORRECTED → separate number.
- **PROPOSED_ACTION:**
  Replace the bullet with:
  «•  «যে ব্যক্তি সঠিক ইলম ব্যতীত কুরআন প্রসঙ্গে কোন কথা বলে…» — জামে তিরমিযি, তাফসির অধ্যায়, হাদীস ২৯৫০ (ইবনে আব্বাস; তিরমিযি: «حسن صحيح»; আলবানী, আহমাদ শাকির ও যুবাইর আলী যাঈ: যয়ীফ)।»
- **PATCH_TYPE:** CORRECT_HADITH_NUMBER
- **CONFIDENCE:** HIGH
- **REQUIRES_HUMAN_REVIEW:** YES

### PB1-070

- **PATCH_ID:** PB1-070
- **PART:** 9
- **CHAPTER:** ০৪  যা বলি, তা কি নিজে করি?
- **PAGE:** PAGE-CHECK (docx not available); ¶8111
- **PARAGRAPH/LOCATION:** Ledger REF-225 · Paragraph_Index 8111 · source-note bullet (chapter source block)
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  যুনদুবের হাদীস («মনগড়া ব্যাখ্যা সঠিক হলেও ভুল») — সুনান আবু দাউদ ৩৬৫২ (খাতামতো) ও তিরমিযি; PAGE-CHECK।
- **PROBLEM:** The Abu Dawud number is right but no grade is printed, and Tirmidhi is cited without a number (2952). Both are da'if. The corpus records Shakir's grade for 2952 as «Sahih Isnaad Maqtu»; a human must check what that label means before it is printed.
- **EVIDENCE:**
  - `-- abudawud 3652 (num 3652/ar 3652) [Knowledge (Kitab Al-Ilm)] Al-Albani:Daif;Muhammad Muhyi Al-Din Abdul Hamid:Daif;Shuaib Al Arnaut:Daif;Zubair Ali Zai:Daif :: …أبو عمران، عن جندب، قال قال رسول الله صلى الله عليه وسلم  " من قال في كتاب الله عز وجل برأيه فأصاب فقد أخطأ " .…`
  - `-- tirmidhi 2952 (num 2952/ar 2952) [Chapters on Tafsir] Ahmad Muhammad Shakir:Sahih Isnaad Maqtu;Al-Albani:Daif;Zubair Ali Zai:Daif :: …ن الجوني، عن جندب بن عبد الله، قال قال رسول الله صلى الله عليه وسلم  " من قال في القرآن برأيه فأصاب فقد أخطأ " . قال أبو عيسى هذا حديث غريب . وقد تكلم بعض أهل العلم في سهيل بن أ…`
- **SOURCE:** Sunan Abi Dawud 3652; Jami' al-Tirmidhi 2952 (Jundub).
- **SOURCE_STATUS:** VERIFIED (live); da'if (Albani, Arna'ut, Abd al-Hamid, Zubair).
- **PROPOSED_ACTION:**
  Replace the bullet with:
  «•  যুনদুবের হাদীস («মনগড়া ব্যাখ্যা সঠিক হলেও ভুল») — সুনান আবু দাউদ ৩৬৫২ (আলবানী, শুআইব আরনাউত, মুহিউদ্দীন আবদুল হামিদ ও যুবাইর আলী যাঈ: যয়ীফ) ও জামে তিরমিযি ২৯৫২ (তিরমিযি: «غريب»; আলবানী ও যুবাইর আলী যাঈ: যয়ীফ)।»
- **PATCH_TYPE:** CORRECT_CITATION
- **CONFIDENCE:** HIGH
- **REQUIRES_HUMAN_REVIEW:** YES

### PB1-071

- **PATCH_ID:** PB1-071
- **PART:** 9
- **CHAPTER:** ০৫  এক গ্রামের দুই আলেম
- **PAGE:** PAGE-CHECK (docx not available); ¶8207
- **PARAGRAPH/LOCATION:** Ledger REF-228 · Paragraph_Index 8207 · source-note bullet (chapter source block)
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  «রাসূলুল্লাহ ﷺ জাবিরকে বলেছিলেন… জ্ঞান-দ্বার» (REV1-এ ফেরানো, ¶12313–12315) — বর্ণিত আছে; PAGE-CHECK।
- **PROBLEM:** UNIDENTIFIED (BUG-25): no classical source located. The note is already attribution-only («বর্ণিত আছে») and carries no kitab name; prose that depends on it must not rise above «বর্ণিত আছে». Strip the internal «(REV1-এ ফেরানো, ¶12313–12315)» marker in the BUG-10 pass.
- **EVIDENCE:**
  - No source evidence exists in this repo for this row (audit v1.1 BUG-25 list). KNOWLEDGE-ONLY (research layer / audit v1.1 candidate; not verifiable from this environment).
- **SOURCE:** None located (ledger Candidate_Source: see CSV).
- **SOURCE_STATUS:** SOURCE-MISSING · বর্ণিত আছে · PRINT BLOCKED (book gate)
- **PROPOSED_ACTION:**
  Retain the current wording verbatim (no kitab name may be added). Author decides: keep as attribution-only, or delete the item (BUG-25). If a sanad is later found, re-open as ADD_SOURCE with PAGE-CHECK.
- **PATCH_TYPE:** PRESERVE_WITH_PAGE_CHECK
- **CONFIDENCE:** LOW
- **REQUIRES_HUMAN_REVIEW:** YES

### PB1-072

- **PATCH_ID:** PB1-072
- **PART:** 9
- **CHAPTER:** ০৫  এক গ্রামের দুই আলেম
- **PAGE:** PAGE-CHECK (docx not available); ¶8210
- **PARAGRAPH/LOCATION:** Ledger REF-231 · Paragraph_Index 8210 · source-note bullet (chapter source block) · register HAD-BIDAA-KAFI
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  «আল্লাহর কাছে সবচেয়ে ঘৃণিত দুই মানুষ» — আল-কাফি খণ্ড ১, বাব: বিদআত…, হাদীস ৬ = নাহজুল বালাগা খুতবা ১৭ (আগের পাসের যাচাই, PART_09 লগ B5); PAGE-CHECK।
- **PROBLEM:** DUPLICATE (HAD-BIDAA-KAFI, with REF-217 and REF-226). The bullet carries internal markers («আগের পাসের যাচাই, PART_09 লগ B5»), and its bab title differs from the canonical form used in REF-217.
- **EVIDENCE:**
  - al-Kafi 1:54 h. 6 = Nahj khutba 17: KNOWLEDGE-ONLY (research layer / audit v1.1 candidate; not verifiable from this environment).
- **SOURCE:** al-Kafi vol. 1, Kitab Fadl al-'Ilm, bab al-bida' wal-ra'y wal-maqayis, h. 6; Nahj al-Balagha khutba 17.
- **SOURCE_STATUS:** SHIA-PAGE-CHECK — EDITION-LOCK PENDING.
- **PROPOSED_ACTION:**
  Replace the bullet with:
  «•  «আল্লাহর কাছে সবচেয়ে ঘৃণিত দুই মানুষ» — আল-কাফি, খণ্ড ১, কিতাবু ফাদলিল ইলম, বাব: বিদআত, নিজস্ব মত ও কিয়াস, হাদীস ৬ = নাহজুল বালাগা, খুতবা ১৭ — PAGE-CHECK।»
- **PATCH_TYPE:** CORRECT_CITATION
- **CONFIDENCE:** MEDIUM
- **REQUIRES_HUMAN_REVIEW:** YES

### PB1-073

- **PATCH_ID:** PB1-073
- **PART:** 9
- **CHAPTER:** ০৬  কুরআনে খলিফা কাকে বলা হয়েছে?
- **PAGE:** PAGE-CHECK (docx not available); ¶8352
- **PARAGRAPH/LOCATION:** Ledger REF-239 · Paragraph_Index 8352 · source-note bullet (chapter source block)
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  «চতুর্থ খলিফা» উক্তি — বর্ণিত আছে; উৎস পাওয়া যায়নি।
- **PROBLEM:** UNIDENTIFIED (BUG-25): no classical source located. The note is already attribution-only («বর্ণিত আছে») and carries no kitab name; prose that depends on it must not rise above «বর্ণিত আছে». Prose REF-234 (¶8268) keeps «বর্ণিত আছে, কেউ কেউ বলত…» — matches.
- **EVIDENCE:**
  - No source evidence exists in this repo for this row (audit v1.1 BUG-25 list). KNOWLEDGE-ONLY (research layer / audit v1.1 candidate; not verifiable from this environment).
- **SOURCE:** None located (ledger Candidate_Source: see CSV).
- **SOURCE_STATUS:** SOURCE-MISSING · বর্ণিত আছে · PRINT BLOCKED (book gate)
- **PROPOSED_ACTION:**
  Retain the current wording verbatim (no kitab name may be added). Author decides: keep as attribution-only, or delete the item (BUG-25). If a sanad is later found, re-open as ADD_SOURCE with PAGE-CHECK.
- **PATCH_TYPE:** PRESERVE_WITH_PAGE_CHECK
- **CONFIDENCE:** LOW
- **REQUIRES_HUMAN_REVIEW:** YES

### PB1-074

- **PATCH_ID:** PB1-074
- **PART:** 9
- **CHAPTER:** ০৬  কুরআনে খলিফা কাকে বলা হয়েছে?
- **PAGE:** PAGE-CHECK (docx not available); ¶8353
- **PARAGRAPH/LOCATION:** Ledger REF-240 · Paragraph_Index 8353 · source-note bullet (chapter source block) · register HAD-12-KHALIFA; HAD-MADINAT-ILM
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  «আমার পর বারো জন খলিফা, সবাই কুরাইশ» — সহীহ বুখারি ও মুসলিমে প্রসিদ্ধ; «খিলাফত ৩০ বছর» — সুনান আবু দাউদ/তিরমিযি; «তুমি আমার ওসী ও খলিফা», «প্রত্যেক নবীর ওসী আছে, আমার ওসী আলী», «আমি জ্ঞানের নগরী, আলী তার দরজা» — সবগুলো বর্ণিত আছে; নম্বর-পৃষ্ঠা PAGE-CHECK (তাকাভির তালিকা)।
- **PROBLEM:** One bullet groups five items. Two are verified six-book hadiths, but they are printed without numbers (twelve khalifas: Bukhari 7222 / Muslim 1821; thirty years: Abu Dawud 4646 / Tirmidhi 2226). The «মদিনাতুল ইলম» item belongs to register HAD-MADINAT-ILM (Hakim, not Tirmidhi). The «ওসী» items have no located source. Each needs its own status.
- **EVIDENCE:**
  - `-- bukhari 7222 (num 7222/ar 7222) []  :: …ا شعبة، عن عبد الملك، سمعت جابر بن سمرة، قال سمعت النبي صلى الله عليه وسلم يقول  " يكون اثنا عشر أميرا فقال كلمة لم أسمعها فقال أبي إنه قال كلهم من قريش ".…`
  - `-- muslim 1821 (num 4705/ar 1821.01) [The Book on Government]  :: …ت مع أبي على النبي صلى الله عليه وسلم فسمعته يقول " إن هذا الأمر لا ينقضي حتى يمضي فيهم اثنا عشر خليفة " . قال ثم تكلم بكلام خفي على - قال - فقلت لأبي ما قال قال " كلهم من قريش " .…`
  - `-- abudawud 4646 (num 4646/ar 4646) [Model Behavior of the Prophet (K] Al-Albani:Hasan Sahih;Muhammad Muhyi Al-Din Abdul Hamid:Hasan Sahih;Zubair Ali Zai:Isnaad Hasan :: …سعيد، عن سعيد بن جمهان، عن سفينة، قال قال رسول الله صلى الله عليه وسلم  " خلافة النبوة ثلاثون سنة ثم يؤتي الله الملك - أو ملكه - من يشاء " . قال سعيد قال لي سفينة أمسك عليك أبا بكر سن…`
  - `-- tirmidhi 2226 (num 2226/ar 2226) [Chapters On Al-Fitan] Ahmad Muhammad Shakir:Sahih;Al-Albani:Sahih;Bashar Awad Maarouf:Hasan;Zubair Ali Zai:Isnaad Hasan :: …سعيد بن جمهان، قال حدثني سفينة، قال قال رسول الله صلى الله عليه وسلم  " الخلافة في أمتي ثلاثون سنة ثم ملك بعد ذلك " . ثم قال لي سفينة أمسك خلافة أبي بكر وخلافة عمر وخلافة عثمان . ثم…`
  - `search «مدينة العلم» (all six books) → (none)`
- **SOURCE:** Bukhari 7222; Muslim 1821; Abu Dawud 4646; Tirmidhi 2226. Others: CANDIDATE / SOURCE-MISSING.
- **SOURCE_STATUS:** Items 1–2: VERIFIED (live). Items 3–4: «বর্ণিত আছে», PAGE-CHECK. Item 5: CANDIDATE (Hakim).
- **PROPOSED_ACTION:**
  Replace the bullet with:
  «•  «আমার পর বারো জন খলিফা, সবাই কুরাইশ» — সহীহ বুখারি ৭২২২ («اثنا عشر أميرا»), সহীহ মুসলিম ১৮২১ («اثنا عشر خليفة»); «খিলাফত ৩০ বছর» — সুনান আবু দাউদ ৪৬৪৬ («خلافة النبوة ثلاثون سنة»; আলবানী: হাসান সহিহ), জামে তিরমিযি ২২২৬ («الخلافة في أمتي ثلاثون سنة»; আলবানী: সহিহ); «তুমি আমার ওসী ও খলিফা», «প্রত্যেক নবীর ওসী আছে, আমার ওসী আলী» — বর্ণিত আছে, PAGE-CHECK; «আমি জ্ঞানের নগরী, আলী তার দরজা» — বর্ণিত আছে (আল-হাকিম, আল-মুস্তাদরাক — PAGE-CHECK; তিরমিযিতে এই শব্দ নেই) (তাকাভির তালিকা)।»
- **PATCH_TYPE:** SPLIT_CLAIM
- **CONFIDENCE:** HIGH
- **REQUIRES_HUMAN_REVIEW:** YES

### PB1-075

- **PATCH_ID:** PB1-075
- **PART:** 9
- **CHAPTER:** ০৮  সূরা দুখানের বরকতময় রাত কোনটি?
- **PAGE:** PAGE-CHECK (docx not available); ¶8557
- **PARAGRAPH/LOCATION:** Ledger REF-242 · Paragraph_Index 8557 · source-note bullet (chapter source block) · register HAD-THAQALAYN
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  সাকালাইন — সহীহ মুসলিম ২৪০৮ («أهل بيتي», CONFIRMED, সংস্করণ-পাঠ); «কখনো পথভ্রষ্ট হবে না» — জামে তিরমিযি ৩৭৮৬ (CONFIRMED, সংস্করণ-পাঠ; মান নিয়ে মতভেদ)। খাতার «তিরমিযি ৩৭৮৮» PAGE-CHECK।
  Relevant clause: «খাতার «তিরমিযি ৩৭৮৮» PAGE-CHECK।»
- **PROBLEM:** Same as REF-206: «খাতার «তিরমিযি ৩৭৮৮» PAGE-CHECK» is now verified, and its graders disagree (HAD-THAQALAYN).
- **EVIDENCE:**
  - `-- tirmidhi 3788 (num 3788/ar 3788) [Chapters on Virtues] Ahmad Muhammad Shakir:Sahih;Al-Albani:Sahih;Zubair Ali Zai:Daif :: …من الآخر كتاب الله حبل ممدود من السماء إلى الأرض وعترتي أهل بيتي ولن يتفرقا حتى يردا على الحوض فانظروا كيف تخلفوني فيهما " . هذا حديث حسن غريب .…`
- **SOURCE:** Jami' al-Tirmidhi 3788.
- **SOURCE_STATUS:** VERIFIED (live); Shakir/Albani sahih, Zubair da'if.
- **PROPOSED_ACTION:**
  Replace that closing clause with:
  «খাতার «তিরমিযি ৩৭৮৮» — CONFIRMED («عترتي أهل بيتي… لن يتفرقا حتى يردا علي الحوض»; মান নিয়ে মতভেদ: আলবানী ও আহমাদ শাকির: সহিহ; যুবাইর আলী যাঈ: যয়ীফ)।»
- **PATCH_TYPE:** CORRECT_CITATION
- **CONFIDENCE:** HIGH
- **REQUIRES_HUMAN_REVIEW:** YES

### PB1-076

- **PATCH_ID:** PB1-076
- **PART:** 9
- **CHAPTER:** ০৮  সূরা দুখানের বরকতময় রাত কোনটি?
- **PAGE:** PAGE-CHECK (docx not available); ¶8559
- **PARAGRAPH/LOCATION:** Ledger REF-244 · Paragraph_Index 8559 · source-note bullet (chapter source block) · register HAD-NUR-AWWAL
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  «আমি, আলী, ফাতিমা, হাসান, হুসাইন আরশের কাছে ছিলাম… আদমের এক হাজার বছর আগে» — বর্ণিত আছে; PAGE-CHECK।
- **PROBLEM:** UNIDENTIFIED (BUG-25): no classical source located. The note is already attribution-only («বর্ণিত আছে») and carries no kitab name; prose that depends on it must not rise above «বর্ণিত আছে». Register HAD-NUR-AWWAL (REF-041, REF-154).
- **EVIDENCE:**
  - No source evidence exists in this repo for this row (audit v1.1 BUG-25 list). KNOWLEDGE-ONLY (research layer / audit v1.1 candidate; not verifiable from this environment).
- **SOURCE:** None located (ledger Candidate_Source: see CSV).
- **SOURCE_STATUS:** SOURCE-MISSING · বর্ণিত আছে · PRINT BLOCKED (book gate)
- **PROPOSED_ACTION:**
  Retain the current wording verbatim (no kitab name may be added). Author decides: keep as attribution-only, or delete the item (BUG-25). If a sanad is later found, re-open as ADD_SOURCE with PAGE-CHECK.
- **PATCH_TYPE:** PRESERVE_WITH_PAGE_CHECK
- **CONFIDENCE:** LOW
- **REQUIRES_HUMAN_REVIEW:** YES

### PB1-077

- **PATCH_ID:** PB1-077
- **PART:** 9
- **CHAPTER:** ০৮  সূরা দুখানের বরকতময় রাত কোনটি?
- **PAGE:** PAGE-CHECK (docx not available); ¶8560
- **PARAGRAPH/LOCATION:** Ledger REF-245 · Paragraph_Index 8560 · source-note bullet (chapter source block) · register HAD-MADINAT-ILM
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  «আমি জ্ঞানের শহর, আলী তার দরজা» — বর্ণিত আছে; PAGE-CHECK।
- **PROBLEM:** DUPLICATE (HAD-MADINAT-ILM). Same as REF-207.
- **EVIDENCE:**
  - `search «مدينة العلم» (all six books) → (none)`
  - Hakim locations: KNOWLEDGE-ONLY (research layer / audit v1.1 candidate; not verifiable from this environment).
- **SOURCE:** al-Hakim, al-Mustadrak (CANDIDATE).
- **SOURCE_STATUS:** CANDIDATE — EDITION-LOCK PENDING.
- **PROPOSED_ACTION:**
  Replace the bullet with:
  «•  «আমি জ্ঞানের শহর, আলী তার দরজা» — বর্ণিত আছে; আল-হাকিম, আল-মুস্তাদরাক, ⟦edition⟧, খণ্ড ⟦ ⟧, হাদীস ⟦ ⟧ — PAGE-CHECK; এই শব্দে সিহাহ সিত্তায় নেই (তিরমিযি ৩৭২৩-এর শব্দ ভিন্ন: «দারুল হিকমা»)।»
- **PATCH_TYPE:** ADD_SOURCE
- **CONFIDENCE:** MEDIUM
- **REQUIRES_HUMAN_REVIEW:** YES

### PB1-078

- **PATCH_ID:** PB1-078
- **PART:** 9
- **CHAPTER:** ০৯  ফুঁ দিয়ে কি আল্লাহর আলো নেভানো যায়?
- **PAGE:** PAGE-CHECK (docx not available); ¶8677
- **PARAGRAPH/LOCATION:** Ledger REF-248 · Paragraph_Index 8677 · source-note bullet (chapter source block)
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  ফেরেশতাদের ইবলিসকে ঘিরে ফেলা ও সমুদ্রে নিক্ষেপ — বর্ণিত আছে; PAGE-CHECK।
- **PROBLEM:** UNIDENTIFIED (BUG-25): no classical source located. The note is already attribution-only («বর্ণিত আছে») and carries no kitab name; prose that depends on it must not rise above «বর্ণিত আছে».
- **EVIDENCE:**
  - No source evidence exists in this repo for this row (audit v1.1 BUG-25 list). KNOWLEDGE-ONLY (research layer / audit v1.1 candidate; not verifiable from this environment).
- **SOURCE:** None located (ledger Candidate_Source: see CSV).
- **SOURCE_STATUS:** SOURCE-MISSING · বর্ণিত আছে · PRINT BLOCKED (book gate)
- **PROPOSED_ACTION:**
  Retain the current wording verbatim (no kitab name may be added). Author decides: keep as attribution-only, or delete the item (BUG-25). If a sanad is later found, re-open as ADD_SOURCE with PAGE-CHECK.
- **PATCH_TYPE:** PRESERVE_WITH_PAGE_CHECK
- **CONFIDENCE:** LOW
- **REQUIRES_HUMAN_REVIEW:** YES

### PB1-079

- **PATCH_ID:** PB1-079
- **PART:** 9
- **CHAPTER:** ১০  রাসূলুল্লাহ ﷺ তাঁর মেয়েকে কোন চোখে দেখতেন
- **PAGE:** PAGE-CHECK (docx not available); ¶8816
- **PARAGRAPH/LOCATION:** Ledger REF-252 · Paragraph_Index 8816 · source-note bullet (chapter source block) · register HAD-QIYAM-FATIMA
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  আয়িশার বর্ণনা (দাঁড়িয়ে যাওয়া, চুমু, আসনে বসানো) — সুনান আবু দাউদ ও তিরমিযিতে বর্ণিত; PAGE-CHECK। চাদর বিছানো — বর্ণিত আছে; PAGE-CHECK।
- **PROBLEM:** Abu Dawud and Tirmidhi are cited without numbers. The verified numbers are Abu Dawud 5217 («قام إليها فأخذ بيدها وقبلها وأجلسها في مجلسه») and Tirmidhi 3872 (HAD-QIYAM-FATIMA, with REF-068).
- **EVIDENCE:**
  - `-- abudawud 5217 (num 5217/ar 5217) [General Behavior (Kitab Al-Adab)] Al-Albani:Sahih;Muhammad Muhyi Al-Din Abdul Hamid:Sahih;Shuaib Al Arnaut:Hasan Sahih;Zubair Ali Zai:Isnaad Hasan :: …ت والهدى والدل - برسول الله صلى الله عليه وسلم من فاطمة كرم الله وجهها كانت إذا دخلت عليه قام إليها فأخذ بيدها وقبلها وأجلسها في مجلسه وكان إذا دخل عليها قامت إليه فأخذت بيده فقبلته وأجلسته…`
  - `-- tirmidhi 3872 (num 3872/ar 3872) [Chapters on Virtues] Ahmad Muhammad Shakir:Sahih;Al-Albani:Sahih;Bashar Awad Maarouf:Hasan Sahih;Zubair Ali Zai:Sahih :: …طمة بنت رسول الله صلى الله عليه وسلم . قالت وكانت إذا دخلت على النبي صلى الله عليه وسلم قام إليها فقبلها وأجلسها في مجلسه وكان النبي صلى الله عليه وسلم إذا دخل عليها قامت من مجلسها فقبلته…`
- **SOURCE:** Sunan Abi Dawud 5217; Jami' al-Tirmidhi 3872 (Aisha).
- **SOURCE_STATUS:** VERIFIED (live); sahih / hasan sahih.
- **PROPOSED_ACTION:**
  Replace the bullet with:
  «•  আয়িশার বর্ণনা (দাঁড়িয়ে যাওয়া, চুমু, আসনে বসানো) — সুনান আবু দাউদ ৫২১৭; জামে তিরমিযি ৩৮৭২। চাদর বিছানো — বর্ণিত আছে; PAGE-CHECK।»
- **PATCH_TYPE:** CORRECT_HADITH_NUMBER
- **CONFIDENCE:** HIGH
- **REQUIRES_HUMAN_REVIEW:** NO

### PB1-080

- **PATCH_ID:** PB1-080
- **PART:** 9
- **CHAPTER:** ১০  রাসূলুল্লাহ ﷺ তাঁর মেয়েকে কোন চোখে দেখতেন
- **PAGE:** PAGE-CHECK (docx not available); ¶8819
- **PARAGRAPH/LOCATION:** Ledger REF-255 · Paragraph_Index 8819 · source-note bullet (chapter source block) · register HAD-UMM-ABIHA
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  «উম্মু আবিহা» — বিহারুল আনওয়ার খণ্ড ৪৩, অধ্যায় ২ (মাকাতিলুত তালিবিয়্যিন থেকে, ইমাম জাফর আস-সাদিক (আলাইহিস্ সালাম)-এর সূত্রে), আগের পাসের পাঠ; PAGE-CHECK।
- **PROBLEM:** DUPLICATE (HAD-UMM-ABIHA). This wording is the register canonical (see REF-155). Only the internal marker «আগের পাসের পাঠ» needs removing.
- **EVIDENCE:**
  - `search «أم أبيها» (all six books) → (none)`
  - Bihar 43 location: KNOWLEDGE-ONLY (research layer / audit v1.1 candidate; not verifiable from this environment).
- **SOURCE:** al-Majlisi, Bihar al-Anwar 43, ch. 2 (from Maqatil al-Talibiyyin).
- **SOURCE_STATUS:** SHIA-PAGE-CHECK — EDITION-LOCK PENDING.
- **PROPOSED_ACTION:**
  Replace the bullet with:
  «•  «উম্মু আবিহা» — বিহারুল আনওয়ার খণ্ড ৪৩, অধ্যায় ২ (মাকাতিলুত তালিবিয়্যিন থেকে, ইমাম জাফর আস-সাদিক (আলাইহিস্ সালাম)-এর সূত্রে) — PAGE-CHECK।»
- **PATCH_TYPE:** PRESERVE_WITH_PAGE_CHECK
- **CONFIDENCE:** MEDIUM
- **REQUIRES_HUMAN_REVIEW:** YES

### PB1-081

- **PATCH_ID:** PB1-081
- **PART:** 9
- **CHAPTER:** ১১  আহলুল বাইত কি জাহান্নামে যেতে পারেন?
- **PAGE:** PAGE-CHECK (docx not available); ¶8968
- **PARAGRAPH/LOCATION:** Ledger REF-258 · Paragraph_Index 8968 · source-note bullet (chapter source block) · register HAD-THAQALAYN
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  সাকালাইন: সহীহ মুসলিম ২৪০৮ (মূল অংশ, CONFIRMED, সংস্করণ-পাঠ); «কখনো পথভ্রষ্ট হবে না» — তিরমিযি ৩৭৮৬ (CONFIRMED, সংস্করণ-পাঠ); «কিয়ামত পর্যন্ত একসাথে থাকবে» — তিরমিযি ৩৭৮৮ (PAGE-CHECK)। খাতায় পুরোটা «সহিহ মুসলিম» বলা — সংশোধিত।
  Relevant clause: ««কিয়ামত পর্যন্ত একসাথে থাকবে» — তিরমিযি ৩৭৮৮ (PAGE-CHECK)।»
- **PROBLEM:** The Tirmidhi 3788 clause is left PAGE-CHECK although it is verified. The Bengali gloss «কিয়ামত পর্যন্ত একসাথে থাকবে» paraphrases «لن يتفرقا حتى يردا علي الحوض», so the original wording should be shown. Graders disagree.
- **EVIDENCE:**
  - `-- tirmidhi 3788 (num 3788/ar 3788) [Chapters on Virtues] Ahmad Muhammad Shakir:Sahih;Al-Albani:Sahih;Zubair Ali Zai:Daif :: …من الآخر كتاب الله حبل ممدود من السماء إلى الأرض وعترتي أهل بيتي ولن يتفرقا حتى يردا على الحوض فانظروا كيف تخلفوني فيهما " . هذا حديث حسن غريب .…`
- **SOURCE:** Jami' al-Tirmidhi 3788.
- **SOURCE_STATUS:** VERIFIED (live); Shakir/Albani sahih, Zubair da'if.
- **PROPOSED_ACTION:**
  Replace that clause with:
  ««কিয়ামত পর্যন্ত একসাথে থাকবে» (মূল শব্দ: «لن يتفرقا حتى يردا علي الحوض») — তিরমিযি ৩৭৮৮ (CONFIRMED; মান নিয়ে মতভেদ: আলবানী ও আহমাদ শাকির: সহিহ; যুবাইর আলী যাঈ: যয়ীফ)।»
- **PATCH_TYPE:** CORRECT_CITATION
- **CONFIDENCE:** HIGH
- **REQUIRES_HUMAN_REVIEW:** YES

### PB1-082

- **PATCH_ID:** PB1-082
- **PART:** 9
- **CHAPTER:** ১১  আহলুল বাইত কি জাহান্নামে যেতে পারেন?
- **PAGE:** PAGE-CHECK (docx not available); ¶8971
- **PARAGRAPH/LOCATION:** Ledger REF-261 · Paragraph_Index 8971 · source-note bullet (chapter source block)
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  হাদীসে কুদসি «হে আদম সন্তান… আকাশমণ্ডলের মতো গুনাহ» — জামে তিরমিযিতে বর্ণিত; PAGE-CHECK।
- **PROBLEM:** Tirmidhi is cited without a number; the verified number is 3540 (Anas).
- **EVIDENCE:**
  - `-- tirmidhi 3540 (num 3540/ar 3540) [Chapters on Supplication] Ahmad Muhammad Shakir:Sahih;Al-Albani:Sahih;Bashar Awad Maarouf:Hasan;Zubair Ali Zai:Isnaad Hasan :: …ا ابن آدم إنك ما دعوتني ورجوتني غفرت لك على ما كان فيك ولا أبالي يا ابن آدم لو بلغت ذنوبك عنان السماء ثم استغفرتني غفرت لك ولا أبالي يا ابن آدم إنك لو أتيتني بقراب الأرض خطايا ثم لقيتني لا تش…`
- **SOURCE:** Jami' al-Tirmidhi 3540.
- **SOURCE_STATUS:** VERIFIED (live); sahih (Shakir, Albani) / hasan (Bashar, Zubair isnad hasan).
- **PROPOSED_ACTION:**
  Replace the bullet with:
  «•  হাদীসে কুদসি «হে আদম সন্তান… আকাশমণ্ডলের মতো গুনাহ» — জামে তিরমিযি ৩৫৪০ (আনাস; আলবানী ও আহমাদ শাকির: সহিহ)।»
- **PATCH_TYPE:** CORRECT_HADITH_NUMBER
- **CONFIDENCE:** HIGH
- **REQUIRES_HUMAN_REVIEW:** NO

### PB1-083

- **PATCH_ID:** PB1-083
- **PART:** 9
- **CHAPTER:** ১১  আহলুল বাইত কি জাহান্নামে যেতে পারেন?
- **PAGE:** PAGE-CHECK (docx not available); ¶8973
- **PARAGRAPH/LOCATION:** Ledger REF-262 · Paragraph_Index 8973 · source-note bullet (chapter source block) · register HAD-QIYAM-FATIMA
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  আয়িশার বর্ণনা (চাল-চলনে সাদৃশ্য; স্ত্রীদের মজলিসে আগমন, «স্বাগতম, হে আমার কন্যা») — সহীহ বুখারি/মুসলিম ও সুনান গ্রন্থে বর্ণিত; আনাসের বর্ণনা (হাসান ও ফাতিমার সাদৃশ্য) — PAGE-CHECK।
- **PROBLEM:** The six-book references are given generically. The verified numbers are: resemblance, Abu Dawud 5217 / Tirmidhi 3872; «مرحبا بابنتي», Bukhari 3623 / Muslim 2450; Anas on al-Hasan's resemblance, Bukhari 3752. Bukhari 3752 concerns al-Hasan only, so the «ও ফাতিমার» part stays PAGE-CHECK.
- **EVIDENCE:**
  - `-- tirmidhi 3872 (num 3872/ar 3872) [Chapters on Virtues] Ahmad Muhammad Shakir:Sahih;Al-Albani:Sahih;Bashar Awad Maarouf:Hasan Sahih;Zubair Ali Zai:Sahih :: …ابن حبيب، عن المنهال بن عمرو، عن عائشة بنت طلحة، عن عائشة أم المؤمنين، قالت ما رأيت أحدا أشبه سمتا ودلا وهديا برسول الله في قيامها وقعودها من فاطمة بنت رسول الله صلى الله عليه وسلم . قال…`
  - `-- bukhari 3623 (num 3623/ar 3623) []  :: …بلت فاطمة تمشي، كأن مشيتها مشى النبي صلى الله عليه وسلم فقال النبي صلى الله عليه وسلم " مرحبا بابنتي ". ثم أجلسها عن يمينه أو عن شماله، ثم أسر إليها حديثا، فبكت فقلت لها لم تبكين ثم أسر…`
  - `-- muslim 2450 (num 6313/ar 2450.02) [The Book of the Merits of the Co]  :: …تمشي ما تخطئ مشيتها من مشية رسول الله صلى الله عليه وسلم شيئا فلما رآها رحب بها فقال " مرحبا بابنتي " . ثم أجلسها عن يمينه أو عن شماله ثم سارها فبكت بكاء شديدا فلما رأى جزعها سارها الثا…`
  - `-- bukhari 3752 (num 3752/ar 3752) [Companions of the Prophet]  :: …عن الزهري، عن أنس،. وقال عبد الرزاق أخبرنا معمر، عن الزهري، أخبرني أنس، قال لم يكن أحد أشبه بالنبي صلى الله عليه وسلم من الحسن بن علي.…`
- **SOURCE:** Abu Dawud 5217; Tirmidhi 3872; Bukhari 3623; Muslim 2450; Bukhari 3752.
- **SOURCE_STATUS:** VERIFIED (live) except the Fatima part of the Anas clause (PAGE-CHECK).
- **PROPOSED_ACTION:**
  Replace the bullet with:
  «•  আয়িশার বর্ণনা (চাল-চলনে সাদৃশ্য; স্ত্রীদের মজলিসে আগমন, «স্বাগতম, হে আমার কন্যা») — সাদৃশ্য: সুনান আবু দাউদ ৫২১৭, জামে তিরমিযি ৩৮৭২; «স্বাগতম, হে আমার কন্যা»: সহীহ বুখারি ৩৬২৩, সহীহ মুসলিম ২৪৫০; আনাসের বর্ণনা (হাসানের সাদৃশ্য) — সহীহ বুখারি ৩৭৫২; ফাতিমার সাদৃশ্য-অংশ — PAGE-CHECK।»
- **PATCH_TYPE:** CORRECT_HADITH_NUMBER
- **CONFIDENCE:** HIGH
- **REQUIRES_HUMAN_REVIEW:** NO

---

## Part 10

### PB1-084

- **PATCH_ID:** PB1-084
- **PART:** 10
- **CHAPTER:** ০১  নামাজে আল্লাহর সঙ্গে কথা বলা
- **PAGE:** PAGE-CHECK (docx not available); ¶9050
- **PARAGRAPH/LOCATION:** Ledger REF-265 · Paragraph_Index 9050 · source-note bullet (chapter source block)
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  «কুরআন পড়ো, আল্লাহ কথা বলবেন; দোয়া করো, তুমি কথা বলবে» — বর্ণিত আছে; PAGE-CHECK।
- **PROBLEM:** UNIDENTIFIED (BUG-25): no classical source located. The note is already attribution-only («বর্ণিত আছে») and carries no kitab name; prose that depends on it must not rise above «বর্ণিত আছে». Prose REF-263 (¶9003) keeps «বর্ণিত আছে» — matches.
- **EVIDENCE:**
  - No source evidence exists in this repo for this row (audit v1.1 BUG-25 list). KNOWLEDGE-ONLY (research layer / audit v1.1 candidate; not verifiable from this environment).
- **SOURCE:** None located (ledger Candidate_Source: see CSV).
- **SOURCE_STATUS:** SOURCE-MISSING · বর্ণিত আছে · PRINT BLOCKED (book gate)
- **PROPOSED_ACTION:**
  Retain the current wording verbatim (no kitab name may be added). Author decides: keep as attribution-only, or delete the item (BUG-25). If a sanad is later found, re-open as ADD_SOURCE with PAGE-CHECK.
- **PATCH_TYPE:** PRESERVE_WITH_PAGE_CHECK
- **CONFIDENCE:** LOW
- **REQUIRES_HUMAN_REVIEW:** YES

### PB1-085

- **PATCH_ID:** PB1-085
- **PART:** 10
- **CHAPTER:** ০১  নামাজে আল্লাহর সঙ্গে কথা বলা
- **PAGE:** PAGE-CHECK (docx not available); ¶9051
- **PARAGRAPH/LOCATION:** Ledger REF-266 · Paragraph_Index 9051 · source-note bullet (chapter source block)
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  «নামাজ মুমিনের মেরাজ» — বহুল প্রচলিত উক্তি; হাদীস-গ্রন্থে সূত্র খোঁজা বাকি, তাই «বলা হয়»; PAGE-CHECK।
- **PROBLEM:** UNIDENTIFIED (BUG-25): no classical source located. The note is already attribution-only («বর্ণিত আছে») and carries no kitab name; prose that depends on it must not rise above «বর্ণিত আছে». Already uses «বলা হয়» — the target wording.
- **EVIDENCE:**
  - No source evidence exists in this repo for this row (audit v1.1 BUG-25 list). KNOWLEDGE-ONLY (research layer / audit v1.1 candidate; not verifiable from this environment).
- **SOURCE:** None located (ledger Candidate_Source: see CSV).
- **SOURCE_STATUS:** SOURCE-MISSING · বর্ণিত আছে · PRINT BLOCKED (book gate)
- **PROPOSED_ACTION:**
  Retain the current wording verbatim (no kitab name may be added). Author decides: keep as attribution-only, or delete the item (BUG-25). If a sanad is later found, re-open as ADD_SOURCE with PAGE-CHECK.
- **PATCH_TYPE:** PRESERVE_WITH_PAGE_CHECK
- **CONFIDENCE:** LOW
- **REQUIRES_HUMAN_REVIEW:** YES

### PB1-086

- **PATCH_ID:** PB1-086
- **PART:** 10
- **CHAPTER:** ০২  নয় মাস ধরে মেয়ের দরজায় রাসূলুল্লাহ ﷺ
- **PAGE:** PAGE-CHECK (docx not available); ¶9159
- **PARAGRAPH/LOCATION:** Ledger REF-271 · Paragraph_Index 9159 · source-note bullet (chapter source block)
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  «নামাজ জান্নাতের চাবি», «জান্নাতের চাবি নামাজ, নামাজের চাবি ওজু» (জাবির) — বর্ণিত আছে (মুসনাদে আহমাদ/তিরমিযিতে প্রসিদ্ধ); PAGE-CHECK।
- **PROBLEM:** The note is left as «বর্ণিত আছে (মুসনাদে আহমাদ/তিরমিযিতে প্রসিদ্ধ)», but the report is Tirmidhi 4. Its graders disagree (BUG-22).
- **EVIDENCE:**
  - `-- tirmidhi 4 (num 4/ar 4) [The Book on Purification] Ahmad Muhammad Shakir:Sahih Lighairihi;Al-Albani:Sahih;Zubair Ali Zai:Daif :: …، عن مجاهد، عن جابر بن عبد الله، رضى الله عنهما قال قال رسول الله صلى الله عليه وسلم  " مفتاح الجنة الصلاة ومفتاح الصلاة الوضوء " .…`
- **SOURCE:** Jami' al-Tirmidhi 4 (Jabir); Musnad Ahmad (PAGE-CHECK).
- **SOURCE_STATUS:** VERIFIED (live); Albani sahih / Shakir sahih li-ghayrihi / Zubair da'if.
- **PROPOSED_ACTION:**
  Replace the bullet with:
  «•  «নামাজ জান্নাতের চাবি», «জান্নাতের চাবি নামাজ, নামাজের চাবি ওজু» (জাবির) — জামে তিরমিযি, হাদীস ৪ (মান নিয়ে মতভেদ: আলবানী: সহিহ; আহমাদ শাকির: সহিহ লিগাইরিহি; যুবাইর আলী যাঈ: যয়ীফ); মুসনাদে আহমাদ — PAGE-CHECK।»
- **PATCH_TYPE:** CORRECT_HADITH_NUMBER
- **CONFIDENCE:** HIGH
- **REQUIRES_HUMAN_REVIEW:** YES

### PB1-087

- **PATCH_ID:** PB1-087
- **PART:** 10
- **CHAPTER:** ০২  নয় মাস ধরে মেয়ের দরজায় রাসূলুল্লাহ ﷺ
- **PAGE:** PAGE-CHECK (docx not available); ¶9160
- **PARAGRAPH/LOCATION:** Ledger REF-272 · Paragraph_Index 9160 · source-note bullet (chapter source block)
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  আলী (আলাইহিস্ সালাম)-এর বাজার-পরিদর্শন — বর্ণিত আছে; PAGE-CHECK। «নামাজ যেদিকে, আমি সেদিকে» — বর্ণিত আছে; উৎস পাওয়া যায়নি।
- **PROBLEM:** UNIDENTIFIED (BUG-25): no classical source located. The note is already attribution-only («বর্ণিত আছে») and carries no kitab name; prose that depends on it must not rise above «বর্ণিত আছে». Prose REF-267 (¶9097) keeps «বর্ণিত আছে» — matches.
- **EVIDENCE:**
  - No source evidence exists in this repo for this row (audit v1.1 BUG-25 list). KNOWLEDGE-ONLY (research layer / audit v1.1 candidate; not verifiable from this environment).
- **SOURCE:** None located (ledger Candidate_Source: see CSV).
- **SOURCE_STATUS:** SOURCE-MISSING · বর্ণিত আছে · PRINT BLOCKED (book gate)
- **PROPOSED_ACTION:**
  Retain the current wording verbatim (no kitab name may be added). Author decides: keep as attribution-only, or delete the item (BUG-25). If a sanad is later found, re-open as ADD_SOURCE with PAGE-CHECK.
- **PATCH_TYPE:** PRESERVE_WITH_PAGE_CHECK
- **CONFIDENCE:** LOW
- **REQUIRES_HUMAN_REVIEW:** YES

### PB1-088

- **PATCH_ID:** PB1-088
- **PART:** 10
- **CHAPTER:** ০২  নয় মাস ধরে মেয়ের দরজায় রাসূলুল্লাহ ﷺ
- **PAGE:** PAGE-CHECK (docx not available); ¶9161
- **PARAGRAPH/LOCATION:** Ledger REF-273 · Paragraph_Index 9161 · source-note bullet (chapter source block)
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  নবীর ডাকে সাড়া না দেওয়া সাহাবি — সহীহ বুখারিতে আবু সাঈদ ইবনুল মুআল্লার বর্ণনা (৮:২৪ প্রসঙ্গে), খাতামতো; PAGE-CHECK। সালমানের দেখানোর অংশ — বর্ণিত আছে; উৎস পাওয়া যায়নি।
  Relevant clause: «নবীর ডাকে সাড়া না দেওয়া সাহাবি — সহীহ বুখারিতে আবু সাঈদ ইবনুল মুআল্লার বর্ণনা (৮:২৪ প্রসঙ্গে), খাতামতো; PAGE-CHECK।»
- **PROBLEM:** Bukhari is cited without a number; the verified number is 4474 (Abu Sa'id b. al-Mu'alla).
- **EVIDENCE:**
  - `-- bukhari 4474 (num 4474/ar 4474) [Prophetic Commentary on the Qur']  :: …ا مسدد، حدثنا يحيى، عن شعبة، قال حدثني خبيب بن عبد الرحمن، عن حفص بن عاصم، عن أبي سعيد بن المعلى، قال كنت أصلي في المسجد فدعاني رسول الله صلى الله عليه وسلم فلم أجبه، فقلت يا رسول الله إ…`
- **SOURCE:** Sahih al-Bukhari 4474.
- **SOURCE_STATUS:** VERIFIED (live). Salman part: unchanged (source not found).
- **PROPOSED_ACTION:**
  Replace that clause with:
  «নবীর ডাকে সাড়া না দেওয়া সাহাবি — সহীহ বুখারি ৪৪৭৪ (আবু সাঈদ ইবনুল মুআল্লা; ৮:২৪ প্রসঙ্গে)।»
- **PATCH_TYPE:** CORRECT_HADITH_NUMBER
- **CONFIDENCE:** HIGH
- **REQUIRES_HUMAN_REVIEW:** NO

### PB1-089

- **PATCH_ID:** PB1-089
- **PART:** 10
- **CHAPTER:** ০২  নয় মাস ধরে মেয়ের দরজায় রাসূলুল্লাহ ﷺ
- **PAGE:** PAGE-CHECK (docx not available); ¶9162
- **PARAGRAPH/LOCATION:** Ledger REF-274 · Paragraph_Index 9162 · source-note bullet (chapter source block) · register HAD-BAB-FATIMA-SALAT
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  ফজরে মা সাইয়্যিদা (আলাইহাস্ সালাম)-এর দরজায় «আস-সালাত, হে আহলুল বাইত» — জামে তিরমিযিতে আনাস থেকে (ছয় মাস); অন্য বর্ণনায় আট/নয় মাস; PAGE-CHECK।
- **PROBLEM:** Tirmidhi is cited without a number or grade. The report is Tirmidhi 3206 (six months), which is da'if (BUG-22).
- **EVIDENCE:**
  - `-- tirmidhi 3206 (num 3206/ar 3206) [Chapters on Tafsir] Ahmad Muhammad Shakir:Daif;Al-Albani:Daif;Zubair Ali Zai:Daif :: …مة، أخبرنا علي بن زيد، عن أنس بن مالك، أن رسول الله صلى الله عليه وسلم كان يمر بباب فاطمة ستة أشهر إذا خرج إلى صلاة الفجر يقول " الصلاة يا أهل البيت : ( إنما يريد الله ليذهب عنكم الر…`
- **SOURCE:** Jami' al-Tirmidhi 3206 (Anas).
- **SOURCE_STATUS:** VERIFIED (live); da'if (Shakir, Albani, Zubair).
- **PROPOSED_ACTION:**
  Replace the bullet with:
  «•  ফজরে মা সাইয়্যিদা (আলাইহাস্ সালাম)-এর দরজায় «আস-সালাত, হে আহলুল বাইত» — জামে তিরমিযি ৩২০৬, আনাস থেকে (ছয় মাস; সনদ দুর্বল — আলবানী, আহমাদ শাকির ও যুবাইর আলী যাঈ: যয়ীফ); অন্য বর্ণনায় আট/নয় মাস — PAGE-CHECK।»
- **PATCH_TYPE:** CORRECT_CITATION
- **CONFIDENCE:** HIGH
- **REQUIRES_HUMAN_REVIEW:** NO

### PB1-090

- **PATCH_ID:** PB1-090
- **PART:** 10
- **CHAPTER:** ০৪  আঠারো হাজার ওয়াক্তের পরও হারিয়ে গেল?
- **PAGE:** PAGE-CHECK (docx not available); ¶9288
- **PARAGRAPH/LOCATION:** Ledger REF-276 · Paragraph_Index 9288 · prose / dialogue line · register HAD-BASRA-SALAT
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > “এমনকি,” বুরুল্লাহ বলল, “বর্ণিত আছে, সাহাবারা কুফার মসজিদে আলাপ করতেন, ‘এতদিন পর আমরা আলীর ইমামতে রাসূলের নামাজের রূপ ফিরে পেলাম।’”
  Relevant clause: «বর্ণিত আছে, সাহাবারা কুফার মসজিদে আলাপ করতেন,»
- **PROBLEM:** The prose places the remark in «কুফার মসজিদে». The cited source (REF-279) is Bukhari 784/786, where Imran b. Husayn prays behind Ali «بالبصرة», in BASRA (BUG-11). Also note that in 784 the speaker is Imran (with Mutarrif), not «সাহাবারা» generally. That is left to the author.
- **EVIDENCE:**
  - `-- bukhari 784 (num 784/ar 784) [Call to Prayers (Adhaan)]  :: …خالد، عن الجريري، عن أبي العلاء، عن مطرف، عن عمران بن حصين، قال صلى مع علي رضى الله عنه بالبصرة فقال ذكرنا هذا الرجل صلاة كنا نصليها مع رسول الله صلى الله عليه وسلم. فذكر أنه كان يكبر…`
  - `-- bukhari 786 (num 786/ar 786) [Call to Prayers (Adhaan)]  :: …حدثنا أبو النعمان، قال حدثنا حماد، عن غيلان بن جرير، عن مطرف بن عبد الله، قال صليت خلف علي بن أبي طالب رضى الله عنه أنا وعمران بن حصين،، فكان إذا سجد كبر، وإذا رفع رأسه كبر، وإذا…`
- **SOURCE:** Sahih al-Bukhari 784, 786.
- **SOURCE_STATUS:** VERIFIED (live) — location CORRECTED.
- **PROPOSED_ACTION:**
  Change only the place in the attribution clause:
  «বর্ণিত আছে, সাহাবারা বসরায় আলাপ করতেন,»
  The dialogue that follows is unchanged. Alternative, if the author holds a separate source for a Kufa scene: keep «কুফার মসজিদে», cite that source with PAGE-CHECK, and stop citing Bukhari 784/786 for it.
- **PATCH_TYPE:** CORRECT_LOCATION
- **CONFIDENCE:** HIGH
- **REQUIRES_HUMAN_REVIEW:** YES

### PB1-091

- **PATCH_ID:** PB1-091
- **PART:** 10
- **CHAPTER:** ০৪  আঠারো হাজার ওয়াক্তের পরও হারিয়ে গেল?
- **PAGE:** PAGE-CHECK (docx not available); ¶9322
- **PARAGRAPH/LOCATION:** Ledger REF-277 · Paragraph_Index 9322 · source-note bullet (chapter source block)
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  «তোমরা আমাকে যেভাবে নামাজ আদায় করতে দেখেছ…» — সহীহ বুখারী (মালিক ইবনুল হুওয়াইরিস); খণ্ড/নম্বর PAGE-CHECK।
- **PROBLEM:** Bukhari is cited without a number; the verified number is 631.
- **EVIDENCE:**
  - `-- bukhari 631 (num 631/ar 631) [Call to Prayers (Adhaan)]  :: …ارجعوا إلى أهليكم فأقيموا فيهم وعلموهم ومروهم وذكر أشياء أحفظها أو لا أحفظها وصلوا كما رأيتموني أصلي، فإذا حضرت الصلاة فليؤذن لكم أحدكم وليؤمكم أكبركم ".…`
- **SOURCE:** Sahih al-Bukhari 631 (Malik b. al-Huwayrith).
- **SOURCE_STATUS:** VERIFIED (live).
- **PROPOSED_ACTION:**
  Replace the bullet with:
  «•  «তোমরা আমাকে যেভাবে নামাজ আদায় করতে দেখেছ…» — সহীহ বুখারী ৬৩১ (মালিক ইবনুল হুওয়াইরিস)।»
- **PATCH_TYPE:** CORRECT_HADITH_NUMBER
- **CONFIDENCE:** HIGH
- **REQUIRES_HUMAN_REVIEW:** NO

### PB1-092

- **PATCH_ID:** PB1-092
- **PART:** 10
- **CHAPTER:** ০৪  আঠারো হাজার ওয়াক্তের পরও হারিয়ে গেল?
- **PAGE:** PAGE-CHECK (docx not available); ¶9324
- **PARAGRAPH/LOCATION:** Ledger REF-278 · Paragraph_Index 9324 · source-note bullet (chapter source block)
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  আনাস ইবনে মালিকের উক্তি ও দামেশকে কান্না (যুহরীর বর্ণনা) — সহীহ বুখারী, «নামাজের ওয়াক্ত» অধ্যায় (খাতামতো); নম্বর PAGE-CHECK।
- **PROBLEM:** Bukhari is cited without a number; the verified number is 530.
- **EVIDENCE:**
  - `-- bukhari 530 (num 530/ar 530) [Times of the Prayers]  :: …ة الحداد، عن عثمان بن أبي رواد، أخي عبد العزيز قال سمعت الزهري، يقول دخلت على أنس بن مالك بدمشق وهو يبكي فقلت ما يبكيك فقال لا أعرف شيئا مما أدركت إلا هذه الصلاة، وهذه الصلاة قد ضيعت.…`
- **SOURCE:** Sahih al-Bukhari 530 (al-Zuhri ← Anas).
- **SOURCE_STATUS:** VERIFIED (live).
- **PROPOSED_ACTION:**
  Replace the bullet with:
  «•  আনাস ইবনে মালিকের উক্তি ও দামেশকে কান্না (যুহরীর বর্ণনা) — সহীহ বুখারী, «নামাজের ওয়াক্ত» অধ্যায়, হাদীস ৫৩০।»
- **PATCH_TYPE:** CORRECT_HADITH_NUMBER
- **CONFIDENCE:** HIGH
- **REQUIRES_HUMAN_REVIEW:** NO

### PB1-093

- **PATCH_ID:** PB1-093
- **PART:** 10
- **CHAPTER:** ০৪  আঠারো হাজার ওয়াক্তের পরও হারিয়ে গেল?
- **PAGE:** PAGE-CHECK (docx not available); ¶9325
- **PARAGRAPH/LOCATION:** Ledger REF-279 · Paragraph_Index 9325 · source-note bullet (chapter source block) · register HAD-BASRA-SALAT
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  ইমরান ইবনে হুসাইন, আলী (আলাইহিস্ সালাম)-এর পেছনে নামাজ — সহীহ বুখারী (খাতামতো); নম্বর PAGE-CHECK। কুফার মসজিদের আলাপ — খাতায় «মেশকাতুল মাসাবিহ, তাজরীদুল বুখারী»; PAGE-CHECK, তাই দৃশ্যে «বর্ণিত আছে»।
- **PROBLEM:** The note backs a «কুফার মসজিদ» scene with Imran b. Husayn's report, which is set in BASRA (Bukhari 784 «صلى مع علي بالبصرة»; 786 Mutarrif) (BUG-11). Mishkat and Tajrid al-Bukhari are secondary works standing in for the primary (BUG-29).
- **EVIDENCE:**
  - `-- bukhari 784 (num 784/ar 784) [Call to Prayers (Adhaan)]  :: …خالد، عن الجريري، عن أبي العلاء، عن مطرف، عن عمران بن حصين، قال صلى مع علي رضى الله عنه بالبصرة فقال ذكرنا هذا الرجل صلاة كنا نصليها مع رسول الله صلى الله عليه وسلم. فذكر أنه كان يكبر…`
  - `-- bukhari 786 (num 786/ar 786) [Call to Prayers (Adhaan)]  :: …حدثنا أبو النعمان، قال حدثنا حماد، عن غيلان بن جرير، عن مطرف بن عبد الله، قال صليت خلف علي بن أبي طالب رضى الله عنه أنا وعمران بن حصين،، فكان إذا سجد كبر، وإذا رفع رأسه كبر، وإذا…`
- **SOURCE:** Sahih al-Bukhari 784, 786.
- **SOURCE_STATUS:** VERIFIED (live) — location CORRECTED.
- **PROPOSED_ACTION:**
  Replace the bullet with:
  «•  ইমরান ইবনে হুসাইন, আলী (আলাইহিস্ সালাম)-এর পেছনে নামাজ (বসরায়: «صلى مع علي بالبصرة») — সহীহ বুখারী ৭৮৪ ও ৭৮৬ (মুতাররিফ ইবনে আবদুল্লাহ থেকে)। নামাজ শেষে রাসূলুল্লাহ ﷺ-এর নামাজের কথা মনে পড়ার উক্তি — একই বর্ণনা।»
  If the author keeps a Kufa scene (see REF-276 alternative), add its own source with PAGE-CHECK. Move «মেশকাতুল মাসাবিহ, তাজরীদুল বুখারী» to the ledger as secondary.
- **PATCH_TYPE:** CORRECT_LOCATION
- **CONFIDENCE:** HIGH
- **REQUIRES_HUMAN_REVIEW:** YES

### PB1-094

- **PATCH_ID:** PB1-094
- **PART:** 10
- **CHAPTER:** ০৪  আঠারো হাজার ওয়াক্তের পরও হারিয়ে গেল?
- **PAGE:** PAGE-CHECK (docx not available); ¶9326
- **PARAGRAPH/LOCATION:** Ledger REF-280 · Paragraph_Index 9326 · source-note bullet (chapter source block) · register HAD-HAQQ-ALI
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  «আলী হকের সাথে, হক আলীর সাথে» — আল-হাকিম, আল-মুসতাদরাক (হাকিমের মতে সহীহ, যাহাবীর আপত্তি); PAGE-CHECK।
- **PROBLEM:** The wording «আলী হকের সাথে, হক আলীর সাথে» (علي مع الحق والحق مع علي) is credited to al-Hakim. al-Hakim and Tirmidhi 3714 carry a different wording, «رحم الله عليا، اللهم أدر الحق معه حيث دار», which Tirmidhi 3714 grades very weak. The «علي مع الحق» wording is in al-Khatib, Tarikh Baghdad (BUG-19). Quote each wording with its own source.
- **EVIDENCE:**
  - `-- tirmidhi 3714 (num 3714/ar 3714) [Chapters on Virtues] Ahmad Muhammad Shakir:Very Daif;Al-Albani:Very Daif;Zubair Ali Zai:Daif :: …الحق وإن كان مرا تركه الحق وماله صديق رحم الله عثمان تستحييه الملائكة رحم الله عليا اللهم أدر الحق معه حيث دار " . قال أبو عيسى هذا حديث غريب لا نعرفه إلا من هذا الوجه . والمختار بن…`
  - `search «علي مع الحق» (all six books) → (none)`
  - al-Khatib 14:321; Hakim 3:124 h. 4629: KNOWLEDGE-ONLY (research layer / audit v1.1 candidate; not verifiable from this environment).
- **SOURCE:** «أدر الحق معه»: Jami' al-Tirmidhi 3714; al-Hakim (CANDIDATE). «علي مع الحق»: al-Khatib, Tarikh Baghdad (CANDIDATE).
- **SOURCE_STATUS:** Tirmidhi 3714: VERIFIED (live), very da'if (Shakir, Albani) / da'if (Zubair). Hakim, Khatib: CANDIDATE — PAGE-CHECK.
- **PROPOSED_ACTION:**
  Replace the bullet with:
  «•  «আলী হকের সাথে, হক আলীর সাথে» (علي مع الحق والحق مع علي) — আল-খতিব আল-বাগদাদি, তারিখু বাগদাদ, ⟦edition⟧, খণ্ড ⟦ ⟧, পৃ. ⟦ ⟧ — PAGE-CHECK। আল-হাকিমের আল-মুস্তাদরাক ও জামে তিরমিযিতে শব্দ ভিন্ন: «আল্লাহ আলীর ওপর রহম করুন; হে আল্লাহ, সে যেদিকে যায় হককে তার সঙ্গে ঘুরিয়ে দাও» (رحم الله عليا، اللهم أدر الحق معه حيث دار) — জামে তিরমিযি ৩৭১৪ (তিরমিযি: «غريب»; আলবানী ও আহমাদ শাকির: অত্যন্ত দুর্বল); আল-মুস্তাদরাক, খণ্ড ⟦ ⟧, হাদীস ⟦ ⟧ (হাকিমের মতে সহীহ, যাহাবীর আপত্তি) — PAGE-CHECK।»
  If the prose uses «আলী হকের সাথে…», its source block must name al-Khatib, not al-Hakim.
- **PATCH_TYPE:** SPLIT_CLAIM
- **CONFIDENCE:** MEDIUM
- **REQUIRES_HUMAN_REVIEW:** YES

### PB1-095

- **PATCH_ID:** PB1-095
- **PART:** 10
- **CHAPTER:** ০৮  নব্বই বছরের ইবাদত কেন হার মানল?
- **PAGE:** PAGE-CHECK (docx not available); ¶9547
- **PARAGRAPH/LOCATION:** Ledger REF-292 · Paragraph_Index 9547 · source-note bullet (chapter source block)
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  মুবাহালা ও নাজরানের প্রতিনিধিদল — খাতামতো; পাদ্রির «নব্বই বছর» উক্তির সূত্র খাতায় নেই, PAGE-CHECK।
- **PROBLEM:** UNIDENTIFIED (BUG-25): no classical source located. The note is already attribution-only («বর্ণিত আছে») and carries no kitab name; prose that depends on it must not rise above «বর্ণিত আছে».
- **EVIDENCE:**
  - No source evidence exists in this repo for this row (audit v1.1 BUG-25 list). KNOWLEDGE-ONLY (research layer / audit v1.1 candidate; not verifiable from this environment).
- **SOURCE:** None located (ledger Candidate_Source: see CSV).
- **SOURCE_STATUS:** SOURCE-MISSING · বর্ণিত আছে · PRINT BLOCKED (book gate)
- **PROPOSED_ACTION:**
  Retain the current wording verbatim (no kitab name may be added). Author decides: keep as attribution-only, or delete the item (BUG-25). If a sanad is later found, re-open as ADD_SOURCE with PAGE-CHECK.
- **PATCH_TYPE:** PRESERVE_WITH_PAGE_CHECK
- **CONFIDENCE:** LOW
- **REQUIRES_HUMAN_REVIEW:** YES

### PB1-096

- **PATCH_ID:** PB1-096
- **PART:** 10
- **CHAPTER:** ০৮  নব্বই বছরের ইবাদত কেন হার মানল?
- **PAGE:** PAGE-CHECK (docx not available); ¶9549
- **PARAGRAPH/LOCATION:** Ledger REF-294 · Paragraph_Index 9549 · source-note bullet (chapter source block) · register HAD-FATIMA-IBADA
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  ইমাম হাসান (আলাইহিস্ সালাম) ও হাসান বসরীর উক্তি — খাতায় «Fatima Zahra in the Words of the Infallibles»; PAGE-CHECK।
- **PROBLEM:** A secondary English anthology («Fatima Zahra in the Words of the Infallibles») stands in for the primary source (BUG-29).
- **EVIDENCE:**
  - Bihar 43:76 (from Manaqib Ibn Shahrashub 3:341): KNOWLEDGE-ONLY (research layer / audit v1.1 candidate; not verifiable from this environment).
- **SOURCE:** Primary (CANDIDATE): al-Majlisi, Bihar al-Anwar 43, quoting Ibn Shahrashub, al-Manaqib.
- **SOURCE_STATUS:** CANDIDATE — EDITION-LOCK PENDING.
- **PROPOSED_ACTION:**
  Replace the bullet with:
  «•  ইমাম হাসান (আলাইহিস্ সালাম) ও হাসান বসরীর উক্তি — বিহারুল আনওয়ার, খণ্ড ৪৩, পৃ. ⟦ ⟧ (ইবনে শাহরাশুব, আল-মানাকিব থেকে) — PAGE-CHECK।»
  Move the anthology to the ledger as a secondary pointer.
- **PATCH_TYPE:** CORRECT_SOURCE
- **CONFIDENCE:** MEDIUM
- **REQUIRES_HUMAN_REVIEW:** YES

### PB1-097

- **PATCH_ID:** PB1-097
- **PART:** 10
- **CHAPTER:** ০৮  নব্বই বছরের ইবাদত কেন হার মানল?
- **PAGE:** PAGE-CHECK (docx not available); ¶9550
- **PARAGRAPH/LOCATION:** Ledger REF-295 · Paragraph_Index 9550 · source-note bullet (chapter source block)
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  রাসূলুল্লাহ ﷺ ও মা সাইয়্যিদার কথোপকথন (ইবাদতের তৌফিক) — খাতামতো; সূত্র নেই, «বর্ণিত আছে» ধাঁচে; PAGE-CHECK।
- **PROBLEM:** UNIDENTIFIED (BUG-25): no classical source located. The note is already attribution-only («বর্ণিত আছে») and carries no kitab name; prose that depends on it must not rise above «বর্ণিত আছে».
- **EVIDENCE:**
  - No source evidence exists in this repo for this row (audit v1.1 BUG-25 list). KNOWLEDGE-ONLY (research layer / audit v1.1 candidate; not verifiable from this environment).
- **SOURCE:** None located (ledger Candidate_Source: see CSV).
- **SOURCE_STATUS:** SOURCE-MISSING · বর্ণিত আছে · PRINT BLOCKED (book gate)
- **PROPOSED_ACTION:**
  Retain the current wording verbatim (no kitab name may be added). Author decides: keep as attribution-only, or delete the item (BUG-25). If a sanad is later found, re-open as ADD_SOURCE with PAGE-CHECK.
- **PATCH_TYPE:** PRESERVE_WITH_PAGE_CHECK
- **CONFIDENCE:** LOW
- **REQUIRES_HUMAN_REVIEW:** YES

### PB1-098

- **PATCH_ID:** PB1-098
- **PART:** 10
- **CHAPTER:** ০৮  নব্বই বছরের ইবাদত কেন হার মানল?
- **PAGE:** PAGE-CHECK (docx not available); ¶9551
- **PARAGRAPH/LOCATION:** Ledger REF-296 · Paragraph_Index 9551 · source-note bullet (chapter source block)
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  মা সাইয়্যিদার দুই রাকাত নামাজ — ইমাম জাফর সাদিক (আলাইহিস্ সালাম) থেকে, খাতায় al-islam.org; PAGE-CHECK।
- **PROBLEM:** A website (al-islam.org) stands in for the primary source (BUG-29).
- **EVIDENCE:**
  - al-Tusi, Misbah al-Mutahajjid (p. 300 region); Ibn Tawus, Jamal al-Usbu': KNOWLEDGE-ONLY (research layer / audit v1.1 candidate; not verifiable from this environment).
- **SOURCE:** Primary (CANDIDATE): al-Tusi, Misbah al-Mutahajjid.
- **SOURCE_STATUS:** CANDIDATE — EDITION-LOCK PENDING.
- **PROPOSED_ACTION:**
  Replace the bullet with:
  «•  মা সাইয়্যিদার দুই রাকাত নামাজ — ইমাম জাফর সাদিক (আলাইহিস্ সালাম) থেকে; শেখ তূসী, মিসবাহুল মুতাহাজ্জিদ, ⟦edition⟧, পৃ. ⟦ ⟧ — PAGE-CHECK।»
  If the primary cannot be confirmed, keep the present wording (al-islam.org) and leave it PAGE-CHECK.
- **PATCH_TYPE:** CORRECT_SOURCE
- **CONFIDENCE:** MEDIUM
- **REQUIRES_HUMAN_REVIEW:** YES

### PB1-099

- **PATCH_ID:** PB1-099
- **PART:** 10
- **CHAPTER:** ০৯  ইবাদতকে ভালোবাসা যায় কীভাবে?
- **PAGE:** PAGE-CHECK (docx not available); ¶9629
- **PARAGRAPH/LOCATION:** Ledger REF-298 · Paragraph_Index 9629 · source-note bullet (chapter source block)
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  ইহসানের হাদীস («যেন তুমি তাঁকে দেখছ») — সহীহ মুসলিম, কিতাবুল ঈমান (জিবরাইলের হাদীস); নম্বর PAGE-CHECK।
- **PROBLEM:** Muslim is cited without a number; the verified number is 8 (Hadith Jibril).
- **EVIDENCE:**
  - `-- muslim 8 (num 93/ar 8.01) [The Book of Faith]  :: …ؤمن بالقدر خيره وشره " . قال صدقت . قال فأخبرني عن الإحسان . قال " أن تعبد الله كأنك تراه فإن لم تكن تراه فإنه يراك " . قال فأخبرني عن الساعة . قال " ما المسئول عنها بأعلم…`
- **SOURCE:** Sahih Muslim 8.
- **SOURCE_STATUS:** VERIFIED (live).
- **PROPOSED_ACTION:**
  Replace the bullet with:
  «•  ইহসানের হাদীস («যেন তুমি তাঁকে দেখছ») — সহীহ মুসলিম, কিতাবুল ঈমান, হাদীস ৮ (জিবরাইলের হাদীস)।»
- **PATCH_TYPE:** CORRECT_HADITH_NUMBER
- **CONFIDENCE:** HIGH
- **REQUIRES_HUMAN_REVIEW:** NO

### PB1-100

- **PATCH_ID:** PB1-100
- **PART:** 10
- **CHAPTER:** ০৯  ইবাদতকে ভালোবাসা যায় কীভাবে?
- **PAGE:** PAGE-CHECK (docx not available); ¶9630
- **PARAGRAPH/LOCATION:** Ledger REF-299 · Paragraph_Index 9630 · source-note bullet (chapter source block)
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  «দাসত্ব পাঁচটি জিনিস দিয়ে গঠিত» — ইমাম আলী (আলাইহিস্ সালাম), মিজানুল হিকমার বরাতে; PAGE-CHECK।
- **PROBLEM:** Mizan al-Hikma, a modern compilation, stands in for the primary (BUG-29). The research-layer candidate primary (Misbah al-Shari'a) is itself of disputed attribution, and the saying is not confirmed there in Ali's name. So the source cannot be safely replaced yet.
- **EVIDENCE:**
  - Misbah al-Shari'a candidate: KNOWLEDGE-ONLY (research layer / audit v1.1 candidate; not verifiable from this environment).
- **SOURCE:** Secondary: Mizan al-Hikma. Primary: not locked.
- **SOURCE_STATUS:** CANDIDATE — PAGE-CHECK.
- **PROPOSED_ACTION:**
  Retain the current wording verbatim; it already names Mizan al-Hikma as the source of the attribution. Editor: trace Mizan al-Hikma's own footnote to its primary and record which Imam it names. Re-open as CORRECT_SOURCE once that is done.
- **PATCH_TYPE:** PRESERVE_WITH_PAGE_CHECK
- **CONFIDENCE:** LOW
- **REQUIRES_HUMAN_REVIEW:** YES

---

## Part 11

### PB1-101

- **PATCH_ID:** PB1-101
- **PART:** 11
- **CHAPTER:** ০২  স্বভাব চেনার চার উপাদান
- **PAGE:** PAGE-CHECK (docx not available); ¶9904
- **PARAGRAPH/LOCATION:** Ledger REF-304 · Paragraph_Index 9904 · prose / dialogue line · register HAD-GHADAB-WUDU
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > রাহাত পড়ল, আঙুল লাইনে রেখে: “বর্ণিত আছে, রাসূলুল্লাহ ﷺ বলেছেন, রাগ শয়তান থেকে, শয়তান আগুনের তৈরি, আর আগুন নেভে পানিতে। তাই রাগ উঠলে ওজু করো। দাঁড়িয়ে থাকলে বসে পড়ো, বসে থাকলে শুয়ে পড়ো।”
  Relevant clause: «বর্ণিত আছে, রাসূলুল্লাহ ﷺ বলেছেন, রাগ শয়তান থেকে, শয়তান আগুনের তৈরি, আর আগুন নেভে পানিতে। তাই রাগ উঠলে ওজু করো। দাঁড়িয়ে থাকলে বসে পড়ো, বসে থাকলে শুয়ে পড়ো।»
- **PROBLEM:** One «রাসূলুল্লাহ ﷺ বলেছেন» quote merges two hadiths with different status. «রাগ শয়তান থেকে… ওজু করো» is Abu Dawud 4784, da'if per Albani, Arna'ut and Abd al-Hamid (Zubair: isnad hasan). «দাঁড়িয়ে থাকলে বসে পড়ো…» is Abu Dawud 4782, sahih. Merging them lends the weak part the sound part's certainty.
- **EVIDENCE:**
  - `-- abudawud 4784 (num 4784/ar 4784) [General Behavior (Kitab Al-Adab)] Al-Albani:Daif;Muhammad Muhyi Al-Din Abdul Hamid:Daif;Shuaib Al Arnaut:Daif;Zubair Ali Zai:Isnaad Hasan :: …أ ثم رجع وقد توضأ فقال حدثني أبي عن جدي عطية قال قال رسول الله صلى الله عليه وسلم  " إن الغضب من الشيطان وإن الشيطان خلق من النار وإنما تطفأ النار بالماء فإذا غضب أحدكم فليتوضأ " .…`
  - `-- abudawud 4782 (num 4782/ar 4782) [General Behavior (Kitab Al-Adab)] Al-Albani:Sahih;Muhammad Muhyi Al-Din Abdul Hamid:Sahih;Zubair Ali Zai:Sahih :: …لأسود، عن أبي ذر، قال إن رسول الله صلى الله عليه وسلم قال لنا  " إذا غضب أحدكم وهو قائم فليجلس فإن ذهب عنه الغضب وإلا فليضطجع " .…`
- **SOURCE:** Sunan Abi Dawud 4784 (Atiyya al-Sa'di); 4782 (Abu Dharr).
- **SOURCE_STATUS:** VERIFIED (live). 4784 da'if (disputed by Zubair); 4782 sahih.
- **PROPOSED_ACTION:**
  Change only the two attribution clauses; the dialogue words are unchanged:
  «আবু দাউদের একটি বর্ণনায় (সনদ দুর্বল) আছে, রাসূলুল্লাহ ﷺ বলেছেন, রাগ শয়তান থেকে, শয়তান আগুনের তৈরি, আর আগুন নেভে পানিতে। তাই রাগ উঠলে ওজু করো। আর সহিহ বর্ণনায় আছে— দাঁড়িয়ে থাকলে বসে পড়ো, বসে থাকলে শুয়ে পড়ো।»
- **PATCH_TYPE:** SPLIT_CLAIM
- **CONFIDENCE:** HIGH
- **REQUIRES_HUMAN_REVIEW:** YES

### PB1-102

- **PATCH_ID:** PB1-102
- **PART:** 11
- **CHAPTER:** ০২  স্বভাব চেনার চার উপাদান
- **PAGE:** PAGE-CHECK (docx not available); ¶9957
- **PARAGRAPH/LOCATION:** Ledger REF-305 · Paragraph_Index 9957 · source-note bullet (chapter source block) · register HAD-GHADAB-WUDU
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  রাগ ও ওজু: সুনানে আবু দাউদ (কিতাবুল আদব, রাগের সময় যা বলতে হয়); বসা/শোয়া: একই কিতাব — নম্বর PAGE-CHECK।
- **PROBLEM:** The Abu Dawud numbers are missing. 4784 (anger → wudu) is weak and needs its grade printed (BUG-22); 4782 (sit/lie down) is sahih.
- **EVIDENCE:**
  - `-- abudawud 4784 (num 4784/ar 4784) [General Behavior (Kitab Al-Adab)] Al-Albani:Daif;Muhammad Muhyi Al-Din Abdul Hamid:Daif;Shuaib Al Arnaut:Daif;Zubair Ali Zai:Isnaad Hasan :: …أ ثم رجع وقد توضأ فقال حدثني أبي عن جدي عطية قال قال رسول الله صلى الله عليه وسلم  " إن الغضب من الشيطان وإن الشيطان خلق من النار وإنما تطفأ النار بالماء فإذا غضب أحدكم فليتوضأ " .…`
  - `-- abudawud 4782 (num 4782/ar 4782) [General Behavior (Kitab Al-Adab)] Al-Albani:Sahih;Muhammad Muhyi Al-Din Abdul Hamid:Sahih;Zubair Ali Zai:Sahih :: …لأسود، عن أبي ذر، قال إن رسول الله صلى الله عليه وسلم قال لنا  " إذا غضب أحدكم وهو قائم فليجلس فإن ذهب عنه الغضب وإلا فليضطجع " .…`
- **SOURCE:** Sunan Abi Dawud 4784, 4782 (Kitab al-Adab).
- **SOURCE_STATUS:** VERIFIED (live). 4784: da'if (Albani, Arna'ut, Abd al-Hamid) / isnad hasan (Zubair). 4782: sahih.
- **PROPOSED_ACTION:**
  Replace the bullet with:
  «•  রাগ ও ওজু: সুনানে আবু দাউদ, কিতাবুল আদব, হাদীস ৪৭৮৪ (আতিয়্যা আস-সা'দি; সনদ দুর্বল — আলবানী, শুআইব আরনাউত ও মুহিউদ্দীন আবদুল হামিদ: যয়ীফ; যুবাইর আলী যাঈ: সনদ হাসান); বসা/শোয়া: একই কিতাব, হাদীস ৪৭৮২ (আবু যর; আলবানী: সহিহ)।»
- **PATCH_TYPE:** CORRECT_CITATION
- **CONFIDENCE:** HIGH
- **REQUIRES_HUMAN_REVIEW:** YES

### PB1-103

- **PATCH_ID:** PB1-103
- **PART:** 11
- **CHAPTER:** ০৪  নিদর্শন দেখেও মানুষ মুখ ফেরায় কেন?
- **PAGE:** PAGE-CHECK (docx not available); ¶10127
- **PARAGRAPH/LOCATION:** Ledger REF-307 · Paragraph_Index 10127 · source-note bullet (chapter source block)
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  চাঁদ দ্বিখণ্ডনের ঘটনা — সহীহ বুখারী (কিতাবুল মানাকিব, ইনশিকাকুল কামার) ও সহীহ মুসলিম (সিফাতুল মুনাফিকীন); খাতার বিবরণ (আকাবা, ১৪ জন) PAGE-CHECK।
- **PROBLEM:** Bukhari and Muslim are cited by chapter only. The verified numbers are Bukhari 3636 and Muslim 2800.
- **EVIDENCE:**
  - `-- bukhari 3636 (num 3636/ar 3636) [Virtues and Merits of the Prophe]  :: …انشق القمر على عهد رسول الله صلى الله عليه وسلم شقتين فقال النبي صلى الله عليه وسلم  " اشهدوا ".…`
  - `-- muslim 2800 (num 7071/ar 2800.01) [Characteristics of the Day of Ju]  :: …حرب، قالا حدثنا سفيان بن عيينة، عن ابن أبي، نجيح عن مجاهد، عن أبي معمر، عن عبد الله، قال انشق القمر على عهد رسول الله صلى الله عليه وسلم بشقتين فقال رسول الله صلى الله عليه وسلم  " اشهدوا…`
- **SOURCE:** Sahih al-Bukhari 3636 (Ibn Mas'ud); Sahih Muslim 2800.
- **SOURCE_STATUS:** VERIFIED (live). «আকাবা, ১৪ জন» detail: PAGE-CHECK (unchanged).
- **PROPOSED_ACTION:**
  Replace the bullet with:
  «•  চাঁদ দ্বিখণ্ডনের ঘটনা — সহীহ বুখারী ৩৬৩৬ (কিতাবুল মানাকিব, ইনশিকাকুল কামার); সহীহ মুসলিম ২৮০০ (সিফাতুল মুনাফিকীন); খাতার বিবরণ (আকাবা, ১৪ জন) PAGE-CHECK।»
- **PATCH_TYPE:** CORRECT_HADITH_NUMBER
- **CONFIDENCE:** HIGH
- **REQUIRES_HUMAN_REVIEW:** NO

### PB1-104

- **PATCH_ID:** PB1-104
- **PART:** 11
- **CHAPTER:** ০৬  প্রশান্ত আত্মার দিকে পথ
- **PAGE:** PAGE-CHECK (docx not available); ¶10290
- **PARAGRAPH/LOCATION:** Ledger REF-309 · Paragraph_Index 10290 · source-note bullet (chapter source block) · register HAD-MADINAT-ILM
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  «আমি জ্ঞানের নগরী, আলী তার দরজা» — আল-হাকিম, আল-মুসতাদরাক (কিতাবু মারিফাতিস সাহাবা); জামে তিরমিযী (মানাকিব, «আমি হিকমতের ঘর»); নম্বর PAGE-CHECK।
- **PROBLEM:** The «জ্ঞানের নগরী» wording is cited to al-Hakim AND Tirmidhi. Tirmidhi carries only «أنا دار الحكمة وعلي بابها» (3723, which Tirmidhi himself calls «غريب منكر»). «مدينة العلم» is absent from all six books (BUG-18). The two wordings need two sources and must never be merged.
- **EVIDENCE:**
  - `search «مدينة العلم» (all six books) → (none)`
  - `-- tirmidhi 3723 (num 3723/ar 3723) [Chapters on Tafsir] Ahmad Muhammad Shakir:Daif;Al-Albani:Daif;Zubair Ali Zai:Daif :: …بن غفلة، عن الصنابحي، عن علي، رضى الله عنه قال قال رسول الله صلى الله عليه وسلم  " أنا دار الحكمة وعلي بابها " . هذا حديث غريب منكر . وروى بعضهم هذا الحديث عن شريك ولم يذكروا فيه عن…`
  - Hakim, Kitab Ma'rifat al-Sahaba (3:126–127, h. 4637–4639): KNOWLEDGE-ONLY (research layer / audit v1.1 candidate; not verifiable from this environment).
- **SOURCE:** «مدينة العلم»: al-Hakim, al-Mustadrak (CANDIDATE). «دار الحكمة»: Jami' al-Tirmidhi 3723.
- **SOURCE_STATUS:** Tirmidhi 3723: VERIFIED (live), da'if. Hakim: CANDIDATE — EDITION-LOCK PENDING.
- **PROPOSED_ACTION:**
  Replace the bullet with:
  «•  «আমি জ্ঞানের নগরী, আলী তার দরজা» (أنا مدينة العلم وعلي بابها) — আল-হাকিম, আল-মুস্তাদরাক (কিতাবু মারিফাতিস সাহাবা), ⟦edition⟧, খণ্ড ⟦ ⟧, হাদীস ⟦ ⟧ — PAGE-CHECK; এই শব্দে সিহাহ সিত্তায় নেই। জামে তিরমিযিতে (মানাকিব) ভিন্ন শব্দ: «আমি হিকমতের ঘর, আলী তার দরজা» (أنا دار الحكمة وعلي بابها) — হাদীস ৩৭২৩ (তিরমিযি: «غريب منكر»; আলবানী, আহমাদ শাকির ও যুবাইর আলী যাঈ: যয়ীফ)।»
  Prose REF-308 keeps «বর্ণিত আছে, রাসূলুল্লাহ ﷺ বলেছেন…»; no change.
- **PATCH_TYPE:** SPLIT_CLAIM
- **CONFIDENCE:** HIGH
- **REQUIRES_HUMAN_REVIEW:** YES

### PB1-105

- **PATCH_ID:** PB1-105
- **PART:** 11
- **CHAPTER:** ১৮ মাকামে তিন ধাপেতে নফসের আত্মশুদ্ধি হয়,
- **PAGE:** PAGE-CHECK (docx not available); ¶10656
- **PARAGRAPH/LOCATION:** Ledger REF-321 · Paragraph_Index 10656 · source-note bullet (chapter source block) · register HAD-NUQTA
- **CURRENT_TEXT:** (ledger `Text`, verbatim)
  > •  «আমি বিসমিল্লাহর বা-এর নিচের বিন্দু» — আলী (আলাইহিস্ সালাম)-এর নামে প্রচলিত; নির্ভরযোগ্য সূত্র পাওয়া যায়নি, PAGE-CHECK।
- **PROBLEM:** UNIDENTIFIED (BUG-25): no classical source located. The note is already attribution-only («বর্ণিত আছে») and carries no kitab name; prose that depends on it must not rise above «বর্ণিত আছে». Consistent with REF-024/REF-033 («এটা হাদিসের কিতাবের কথা নয়»); keep as an irfani saying, never as a hadith.
- **EVIDENCE:**
  - No source evidence exists in this repo for this row (audit v1.1 BUG-25 list). KNOWLEDGE-ONLY (research layer / audit v1.1 candidate; not verifiable from this environment).
- **SOURCE:** None located (ledger Candidate_Source: see CSV).
- **SOURCE_STATUS:** SOURCE-MISSING · বর্ণিত আছে · PRINT BLOCKED (book gate)
- **PROPOSED_ACTION:**
  Retain the current wording verbatim (no kitab name may be added). Author decides: keep as attribution-only, or delete the item (BUG-25). If a sanad is later found, re-open as ADD_SOURCE with PAGE-CHECK.
- **PATCH_TYPE:** PRESERVE_WITH_PAGE_CHECK
- **CONFIDENCE:** LOW
- **REQUIRES_HUMAN_REVIEW:** YES

---

## 4. NO_CHANGE rows

223 rows. These need no manuscript text change in this plan. PAGE-CHECK / edition lock remains where the ledger has it, and the gate stays PRINT BLOCKED.

| REF | Part | Chapter | ¶ | Triage | PATCH_TYPE | Note |
|---|---|---|---|---|---|---|
| REF-001 | 1 | ০৩ | 197 | PROSE | NO_CHANGE | Prose certainty («বর্ণিত আছে») does not exceed the source status; dialogue unchanged. |
| REF-003 | 1 | ০৪ | 320 | SPC | NO_CHANGE | Shia source correctly named; vol/page/hadith lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-007 | 1 | ০৬ | 499 | CAND | NO_CHANGE | Candidate source identified (research layer); page/number lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-008 | 1 | ০৬ | 500 | CAND | NO_CHANGE | Candidate source identified (research layer); page/number lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-010 | 1 | ০৭ | 580 | VL | NO_CHANGE | Number + text verified live; number already printed; no grade to add. |
| REF-012 | 1 | ০৭ | 582 | VL | NO_CHANGE | Number + text verified live; number already printed; no grade to add. |
| REF-015 | 1 | ১১ | 818 | HIST | NO_CHANGE | Non-hadith (history / geography / literature / chapter note); page lock only. |
| REF-016 | 2 | ০১ | 1018 | CAND | NO_CHANGE | Candidate source identified (research layer); page/number lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-017 | 2 | ০২ | 1081 | HIST | NO_CHANGE | Non-hadith (history / geography / literature / chapter note); page lock only. |
| REF-018 | 2 | ০৩ | 1095 | PROSE | NO_CHANGE | Prose certainty («বর্ণিত আছে») does not exceed the source status; dialogue unchanged. |
| REF-019 | 2 | ০৩ | 1158 | CAND | NO_CHANGE | Candidate source identified (research layer); page/number lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-021 | 2 | ০৫ | 1318 | SPC | NO_CHANGE | Shia source correctly named; vol/page/hadith lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-023 | 2 | ০৬ | 1425 | PROSE | NO_CHANGE | Prose certainty («বর্ণিত আছে») does not exceed the source status; dialogue unchanged. |
| REF-024 | 2 | ০৬ | 1428 | PROSE | NO_CHANGE | Prose certainty («বর্ণিত আছে») does not exceed the source status; dialogue unchanged. |
| REF-025 | 2 | ০৬ | 1447 | PROSE | NO_CHANGE | Prose already «বর্ণিত আছে»; REF-034 states the long version is from the author's manuscript as «বর্ণিত আছে». |
| REF-026 | 2 | ০৬ | 1553 | PROSE | NO_CHANGE | Prose certainty («বর্ণিত আছে») does not exceed the source status; dialogue unchanged. |
| REF-027 | 2 | ০৬ | 1572 | PROSE | NO_CHANGE | Prose certainty («বর্ণিত আছে») does not exceed the source status; dialogue unchanged. |
| REF-028 | 2 | ০৬ | 1619 | HIST | NO_CHANGE | Non-hadith (history / geography / literature / chapter note); page lock only. |
| REF-029 | 2 | ০৬ | 1622 | SPC | NO_CHANGE | Shia source correctly named; vol/page/hadith lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-030 | 2 | ০৬ | 1623 | SPC | NO_CHANGE | Shia source correctly named; vol/page/hadith lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-031 | 2 | ০৬ | 1624 | CAND | NO_CHANGE | Candidate source identified (research layer); page/number lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-032 | 2 | ০৬ | 1625 | SPC | NO_CHANGE | Shia source correctly named; vol/page/hadith lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-033 | 2 | ০৬ | 1626 | SPC | NO_CHANGE | Shia source correctly named; vol/page/hadith lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-034 | 2 | ০৬ | 1627 | SPC | NO_CHANGE | Shia source correctly named; vol/page/hadith lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-035 | 2 | ০৬ | 1629 | SPC | NO_CHANGE | Shia source correctly named; vol/page/hadith lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-036 | 2 | ০৬ | 1630 | SPC | NO_CHANGE | Shia source correctly named; vol/page/hadith lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-037 | 2 | ০৬ | 1631 | SPC | NO_CHANGE | Shia source correctly named; vol/page/hadith lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-038 | 2 | ০৬ | 1634 | CAND | NO_CHANGE | Candidate source identified (research layer); page/number lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-040 | 2 | ০৬ | 1637 | SPC | NO_CHANGE | Shia source correctly named; vol/page/hadith lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-042 | 2 | ০৬ | 1640 | SPC | NO_CHANGE | Shia source correctly named; vol/page/hadith lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-043 | 2 | ০৬ | 1642 | VL | NO_CHANGE | Already prints Tirmidhi 3786 grader disagreement and Muslim 2408 «وأهل بيتي» ≠ «عترتي» — HAD-THAQALAYN canonical model. |
| REF-044 | 2 | ০৬ | 1643 | VL | NO_CHANGE | Number + text verified live; number already printed; no grade to add. |
| REF-045 | 2 | ০৬ | 1644 | VL | NO_CHANGE | Bukhari 936 / Muslim 863 verified live; «নম্বর PAGE-CHECK» may be cleared in the BUG-10 pass. |
| REF-046 | 2 | ০৬ | 1648 | SPC | NO_CHANGE | Shia source correctly named; vol/page/hadith lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-047 | 2 | ০৬ | 1650 | HIST | NO_CHANGE | Non-hadith (history / geography / literature / chapter note); page lock only. |
| REF-048 | 2 | ০৭ | 1808 | PROSE | NO_CHANGE | Prose «বর্ণিত আছে» ≤ source (Abu Dawud 2355/2356 added in REF-049 patch). |
| REF-050 | 2 | ০৮ | 1946 | PROSE | NO_CHANGE | Prose certainty («বর্ণিত আছে») does not exceed the source status; dialogue unchanged. |
| REF-051 | 2 | ০৮ | 2064 | PROSE | NO_CHANGE | Prose certainty («বর্ণিত আছে») does not exceed the source status; dialogue unchanged. |
| REF-052 | 2 | ০৮ | 2170 | HIST | NO_CHANGE | Non-hadith (history / geography / literature / chapter note); page lock only. |
| REF-053 | 2 | ০৮ | 2171 | VL | NO_CHANGE | Number + text verified live; number already printed; no grade to add. |
| REF-054 | 2 | ০৮ | 2172 | VL | NO_CHANGE | Number + text verified live; number already printed; no grade to add. |
| REF-055 | 2 | ০৮ | 2173 | SPC | NO_CHANGE | Shia source correctly named; vol/page/hadith lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-056 | 2 | ০৮ | 2182 | SPC | NO_CHANGE | Shia source correctly named; vol/page/hadith lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-057 | 2 | ০৮ | 2183 | SPC | NO_CHANGE | Shia source correctly named; vol/page/hadith lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-058 | 2 | ০৯ | 2240 | PROSE | NO_CHANGE | Prose certainty («বর্ণিত আছে») does not exceed the source status; dialogue unchanged. |
| REF-059 | 2 | ০৯ | 2273 | SPC | NO_CHANGE | Shia source correctly named; vol/page/hadith lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-060 | 2 | ০৯ | 2274 | CAND | NO_CHANGE | Candidate source identified (research layer); page/number lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-061 | 2 | ০৯ | 2275 | HIST | NO_CHANGE | Non-hadith (history / geography / literature / chapter note); page lock only. |
| REF-062 | 2 | ১০ | 2304 | PROSE | NO_CHANGE | Prose certainty («বর্ণিত আছে») does not exceed the source status; dialogue unchanged. |
| REF-063 | 2 | ১০ | 2355 | SPC | NO_CHANGE | Shia source correctly named; vol/page/hadith lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-064 | 2 | ১০ | 2356 | SPC | NO_CHANGE | Shia source correctly named; vol/page/hadith lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-065 | 3 | ০২ | 2509 | VL | NO_CHANGE | Number + text verified live; number already printed; no grade to add. |
| REF-066 | 3 | ০৩ | 2528 | PROSE | NO_CHANGE | Prose certainty («বর্ণিত আছে») does not exceed the source status; dialogue unchanged. |
| REF-067 | 3 | ০৩ | 2570 | VL | NO_CHANGE | Bukhari 3705 verified; HAD-TASBIH Kafi placement (2:536 vs 3:342-343, with REF-003) is an edition-lock decision, not a text error. |
| REF-068 | 3 | ০৩ | 2571 | VL | NO_CHANGE | Number + text verified live; number already printed; no grade to add. |
| REF-069 | 3 | ০৩ | 2572 | CAND | NO_CHANGE | Candidate source identified (research layer); page/number lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-070 | 3 | ০৪ | 2646 | SPC | NO_CHANGE | Shia source correctly named; vol/page/hadith lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-072 | 3 | ০৪ | 2649 | VL | NO_CHANGE | Bukhari 3714 verified; «অন্তরের ধন» already «বর্ণিত আছে». |
| REF-076 | 3 | ০৫ | 2731 | VL | NO_CHANGE | Bukhari 3714 verified; «যার প্রতি সে সন্তুষ্ট» already «বর্ণিত আছে». |
| REF-077 | 3 | ০৫ | 2732 | HIST | NO_CHANGE | Non-hadith (history / geography / literature / chapter note); page lock only. |
| REF-080 | 3 | ০৬ | 2815 | VL | NO_CHANGE | Number + text verified live; number already printed; no grade to add. |
| REF-083 | 3 | ০৭ | 2879 | VL | NO_CHANGE | Muslim 1851 «بيعة» wording verified live and kept separate from Kafi «لا يعرف إمامه» (BUG-06 already applied). |
| REF-085 | 3 | ০৯ | 2988 | VL | NO_CHANGE | Number + text verified live; number already printed; no grade to add. |
| REF-088 | 4 | ০৬ | 3597 | SPC | NO_CHANGE | Shia source correctly named; vol/page/hadith lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-089 | 4 | ০৬ | 3598 | SPC | NO_CHANGE | Shia source correctly named; vol/page/hadith lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-092 | 4 | ০৭ | 3706 | SPC | NO_CHANGE | Shia source correctly named; vol/page/hadith lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-093 | 4 | ০৭ | 3707 | CAND | NO_CHANGE | Candidate source identified (research layer); page/number lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-094 | 4 | ০৮ | 3828 | CAND | NO_CHANGE | Candidate source identified (research layer); page/number lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-095 | 4 | ০৮ | 3829 | CAND | NO_CHANGE | Candidate source identified (research layer); page/number lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-098 | 5 | ০৩ | 4091 | CAND | NO_CHANGE | Candidate source identified (research layer); page/number lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-099 | 5 | ০৩ | 4092 | CAND | NO_CHANGE | Candidate source identified (research layer); page/number lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-102 | 5 | ০৪ | 4179 | HIST | NO_CHANGE | Non-hadith (history / geography / literature / chapter note); page lock only. |
| REF-103 | 5 | ০৪ | 4180 | CAND | NO_CHANGE | Candidate source identified (research layer); page/number lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-104 | 5 | ০৪ | 4181 | CAND | NO_CHANGE | Candidate source identified (research layer); page/number lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-106 | 5 | ০৫ | 4271 | CAND | NO_CHANGE | Candidate source identified (research layer); page/number lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-108 | 5 | ০৬ | 4351 | CAND | NO_CHANGE | Candidate source identified (research layer); page/number lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-109 | 5 | ০৬ | 4352 | CAND | NO_CHANGE | Candidate source identified (research layer); page/number lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-111 | 6 | ০১ | 4620 | HIST | NO_CHANGE | Non-hadith (history / geography / literature / chapter note); page lock only. |
| REF-112 | 6 | ০২ | 4711 | PROSE | NO_CHANGE | Prose certainty («বর্ণিত আছে») does not exceed the source status; dialogue unchanged. |
| REF-113 | 6 | ০২ | 4749 | SPC | NO_CHANGE | Shia source correctly named; vol/page/hadith lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-114 | 6 | ০২ | 4750 | SPC | NO_CHANGE | Shia source correctly named; vol/page/hadith lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-116 | 6 | ০৩ | 4900 | HIST | NO_CHANGE | Non-hadith (history / geography / literature / chapter note); page lock only. |
| REF-117 | 6 | ০৪ | 5160 | SPC | NO_CHANGE | Shia source correctly named; vol/page/hadith lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-118 | 6 | ০৪ | 5162 | SPC | NO_CHANGE | Shia source correctly named; vol/page/hadith lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-119 | 6 | ০৪ | 5163 | SPC | NO_CHANGE | Shia source correctly named; vol/page/hadith lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-120 | 6 | ০৪ | 5164 | CAND | NO_CHANGE | Candidate source identified (research layer); page/number lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-121 | 6 | ০৫ | 5290 | CAND | NO_CHANGE | Candidate source identified (research layer); page/number lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-124 | 6 | ০৫ | 5293 | SPC | NO_CHANGE | Shia source correctly named; vol/page/hadith lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-127 | 6 | ০৭ | 5447 | Q | NO_CHANGE | Quran 30:38 «فَآتِ» vs 17:26 «وَآتِ» — already distinguished; check which verse the prose quotes. |
| REF-128 | 6 | ০৭ | 5448 | SPC | NO_CHANGE | Shia source correctly named; vol/page/hadith lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-129 | 6 | ০৭ | 5449 | CAND | NO_CHANGE | Candidate source identified (research layer); page/number lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-130 | 6 | ০৭ | 5450 | SPC | NO_CHANGE | Shia source correctly named; vol/page/hadith lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-132 | 6 | ০৯ | 5619 | VL | NO_CHANGE | Number + text verified live; number already printed; no grade to add. |
| REF-133 | 6 | ০৯ | 5620 | CAND | NO_CHANGE | Candidate source identified (research layer); page/number lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-136 | 6 | ১০ | 5755 | SPC | NO_CHANGE | Shia source correctly named; vol/page/hadith lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-137 | 6 | ১০ | 5756 | CAND | NO_CHANGE | Candidate source identified (research layer); page/number lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-138 | 6 | ১০ | 5757 | CAND | NO_CHANGE | Candidate source identified (research layer); page/number lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-139 | 6 | ১০ | 5758 | SPC | NO_CHANGE | Shia source correctly named; vol/page/hadith lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-141 | 6 | ১০ | 5760 | CAND | NO_CHANGE | Candidate source identified (research layer); page/number lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-142 | 7 | ০২ | 5947 | VL | NO_CHANGE | «যে তাকে খুশি করে…» stays «অন্য বর্ণনায়, PAGE-CHECK» — no «يسرني ما يسرها/يبسطني» in six books (live search); do NOT map it to Muslim 2449. |
| REF-146 | 7 | ০৪ | 6119 | CAND | NO_CHANGE | Candidate source identified (research layer); page/number lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-147 | 7 | ০৪ | 6120 | CAND | NO_CHANGE | Candidate source identified (research layer); page/number lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-148 | 7 | ০৪ | 6121 | CAND | NO_CHANGE | Candidate source identified (research layer); page/number lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-149 | 7 | ০৪ | 6122 | CAND | NO_CHANGE | Candidate source identified (research layer); page/number lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-150 | 7 | ০৪ | 6123 | CAND | NO_CHANGE | Candidate source identified (research layer); page/number lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-151 | 7 | ০৪ | 6124 | CAND | NO_CHANGE | Candidate source identified (research layer); page/number lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-154 | 7 | ০৫ | 6245 | CAND | NO_CHANGE | Candidate source identified (research layer); page/number lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-156 | 7 | ০৬ | 6392 | CAND | NO_CHANGE | Candidate source identified (research layer); page/number lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-160 | 7 | ০৭ | 6495 | CAND | NO_CHANGE | Candidate source identified (research layer); page/number lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-161 | 7 | ০৭ | 6496 | CAND | NO_CHANGE | Candidate source identified (research layer); page/number lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-162 | 7 | ০৮ | 6511 | PROSE | NO_CHANGE | Prose certainty («বর্ণিত আছে») does not exceed the source status; dialogue unchanged. |
| REF-163 | 7 | ০৮ | 6581 | CAND | NO_CHANGE | Candidate source identified (research layer); page/number lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-165 | 7 | ০৮ | 6583 | SPC | NO_CHANGE | Shia source correctly named; vol/page/hadith lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-166 | 7 | ০৮ | 6584 | SPC | NO_CHANGE | Shia source correctly named; vol/page/hadith lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-167 | 7 | ০৯ | 6655 | PROSE | NO_CHANGE | Prose certainty («বর্ণিত আছে») does not exceed the source status; dialogue unchanged. |
| REF-169 | 7 | ০৯ | 6674 | SPC | NO_CHANGE | Shia source correctly named; vol/page/hadith lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-170 | 7 | ০৯ | 6675 | SPC | NO_CHANGE | Shia source correctly named; vol/page/hadith lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-171 | 7 | ০৯ | 6676 | CAND | NO_CHANGE | Candidate source identified (research layer); page/number lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-172 | 7 | ১০ | 6724 | PROSE | NO_CHANGE | Prose certainty («বর্ণিত আছে») does not exceed the source status; dialogue unchanged. |
| REF-173 | 7 | ১০ | 6737 | SPC | NO_CHANGE | Shia source correctly named; vol/page/hadith lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-174 | 7 | ১০ | 6738 | SPC | NO_CHANGE | Shia source correctly named; vol/page/hadith lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-176 | 7 | ১১ | 6758 | PROSE | NO_CHANGE | Prose certainty («বর্ণিত আছে») does not exceed the source status; dialogue unchanged. |
| REF-177 | 7 | ১১ | 6787 | CAND | NO_CHANGE | Candidate source identified (research layer); page/number lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-178 | 7 | ১১ | 6788 | SPC | NO_CHANGE | Shia source correctly named; vol/page/hadith lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-179 | 8 | ০১ | 6907 | CAND | NO_CHANGE | Candidate source identified (research layer); page/number lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-180 | 8 | ০১ | 6908 | CAND | NO_CHANGE | Candidate source identified (research layer); page/number lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-181 | 8 | ০২ | 6975 | CAND | NO_CHANGE | Candidate source identified (research layer); page/number lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-182 | 8 | ০২ | 6976 | SPC | NO_CHANGE | Shia source correctly named; vol/page/hadith lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-183 | 8 | ০২ | 6977 | SPC | NO_CHANGE | Shia source correctly named; vol/page/hadith lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-184 | 8 | ০২ | 6978 | SPC | NO_CHANGE | Shia source correctly named; vol/page/hadith lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-185 | 8 | ০২ | 6979 | HIST | NO_CHANGE | Non-hadith (history / geography / literature / chapter note); page lock only. |
| REF-187 | 8 | ০৩ | 7046 | CAND | NO_CHANGE | Register HAD-BAB-FATIMA-SALAT; Shawahid/Tabarani page lock only; grade printed in REF-144/274. |
| REF-189 | 8 | ০৪ | 7110 | CAND | NO_CHANGE | Register HAD-BAB-FATIMA-SALAT; Shawahid page lock only. |
| REF-190 | 8 | ০৪ | 7111 | SPC | NO_CHANGE | Shia source correctly named; vol/page/hadith lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-191 | 8 | ০৪ | 7112 | CAND | NO_CHANGE | Register HAD-SAFINA; already «বর্ণিত আছে, PAGE-CHECK (মুস্তাদরাক হাকিম)» — consistent with REF-011 canonical; Hakim number lock (BUG-21). |
| REF-192 | 8 | ০৬ | 7222 | SPC | NO_CHANGE | Shia source correctly named; vol/page/hadith lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-193 | 8 | ০৮ | 7348 | CAND | NO_CHANGE | Candidate source identified (research layer); page/number lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-194 | 8 | ০৮ | 7349 | SPC | NO_CHANGE | Shia source correctly named; vol/page/hadith lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-195 | 8 | ০৯ | 7420 | SPC | NO_CHANGE | Shia source correctly named; vol/page/hadith lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-197 | 8 | ০৯ | 7422 | SPC | NO_CHANGE | Shia source correctly named; vol/page/hadith lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-198 | 8 | ১০ | 7477 | HIST | NO_CHANGE | Non-hadith (history / geography / literature / chapter note); page lock only. |
| REF-200 | 8 | ১০ | 7479 | CAND | NO_CHANGE | Candidate source identified (research layer); page/number lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-202 | 8 | ১১ | 7523 | VL | NO_CHANGE | Number + text verified live; number already printed; no grade to add. |
| REF-203 | 8 | ১১ | 7524 | HIST | NO_CHANGE | Non-hadith (history / geography / literature / chapter note); page lock only. |
| REF-204 | 8 | ১২ | 7581 | SPC | NO_CHANGE | Shia source correctly named; vol/page/hadith lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-205 | 9 | ০১ | 7687 | PROSE | NO_CHANGE | Prose certainty («বর্ণিত আছে») does not exceed the source status; dialogue unchanged. |
| REF-210 | 9 | ০১ | 7736 | Q | NO_CHANGE | Quran text check only. |
| REF-211 | 9 | ০২ | 7789 | PROSE | NO_CHANGE | Prose certainty («বর্ণিত আছে») does not exceed the source status; dialogue unchanged. |
| REF-212 | 9 | ০২ | 7877 | SPC | NO_CHANGE | Shia source correctly named; vol/page/hadith lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-213 | 9 | ০২ | 7878 | SPC | NO_CHANGE | Shia source correctly named; vol/page/hadith lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-214 | 9 | ০২ | 7879 | SPC | NO_CHANGE | Shia source correctly named; vol/page/hadith lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-216 | 9 | ০৩ | 7936 | PROSE | NO_CHANGE | Prose certainty («বর্ণিত আছে») does not exceed the source status; dialogue unchanged. |
| REF-217 | 9 | ০৩ | 8008 | SPC | NO_CHANGE | Shia source correctly named; vol/page/hadith lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-218 | 9 | ০৩ | 8009 | SPC | NO_CHANGE | Shia source correctly named; vol/page/hadith lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-221 | 9 | ০৩ | 8012 | SPC | NO_CHANGE | Shia source correctly named; vol/page/hadith lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-226 | 9 | ০৪ | 8112 | SPC | NO_CHANGE | Shia source correctly named; vol/page/hadith lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-227 | 9 | ০৫ | 8206 | SPC | NO_CHANGE | Shia source correctly named; vol/page/hadith lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-229 | 9 | ০৫ | 8208 | CAND | NO_CHANGE | Candidate source identified (research layer); page/number lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-230 | 9 | ০৫ | 8209 | CAND | NO_CHANGE | Candidate source identified (research layer); page/number lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-232 | 9 | ০৫ | 8211 | CAND | NO_CHANGE | Candidate source identified (research layer); page/number lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-233 | 9 | ০৬ | 8262 | PROSE | NO_CHANGE | Prose certainty («বর্ণিত আছে») does not exceed the source status; dialogue unchanged. |
| REF-234 | 9 | ০৬ | 8268 | PROSE | NO_CHANGE | Prose certainty («বর্ণিত আছে») does not exceed the source status; dialogue unchanged. |
| REF-235 | 9 | ০৬ | 8348 | SPC | NO_CHANGE | Shia source correctly named; vol/page/hadith lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-236 | 9 | ০৬ | 8349 | VL | NO_CHANGE | Number + text verified live; number already printed; no grade to add. |
| REF-237 | 9 | ০৬ | 8350 | VL | NO_CHANGE | Tirmidhi 3713 verified; Ahmad congratulation number (CANDIDATE 18479) to lock — no text change now. |
| REF-238 | 9 | ০৬ | 8351 | SPC | NO_CHANGE | Shia source correctly named; vol/page/hadith lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-241 | 9 | ০৬ | 8354 | CAND | NO_CHANGE | Candidate source identified (research layer); page/number lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-243 | 9 | ০৮ | 8558 | SPC | NO_CHANGE | Shia source correctly named; vol/page/hadith lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-246 | 9 | ০৯ | 8643 | PROSE | NO_CHANGE | Prose certainty («বর্ণিত আছে») does not exceed the source status; dialogue unchanged. |
| REF-247 | 9 | ০৯ | 8676 | SPC | NO_CHANGE | Shia source correctly named; vol/page/hadith lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-249 | 9 | ০৯ | 8678 | SPC | NO_CHANGE | Shia source correctly named; vol/page/hadith lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-250 | 9 | ১০ | 8814 | VL | NO_CHANGE | Bukhari 3714 verified; internal «SOURCE_REGISTER CL-HAD-008» marker for BUG-10 pass. |
| REF-251 | 9 | ১০ | 8815 | CAND | NO_CHANGE | Candidate source identified (research layer); page/number lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-253 | 9 | ১০ | 8817 | CAND | NO_CHANGE | Candidate source identified (research layer); page/number lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-254 | 9 | ১০ | 8818 | SPC | NO_CHANGE | Shia source correctly named; vol/page/hadith lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-256 | 9 | ১১ | 8874 | PROSE | NO_CHANGE | Prose «বর্ণিত আছে»; source (Tabarani/Hakim/Kanz) CANDIDATE — not live-gradable here. |
| REF-257 | 9 | ১১ | 8903 | PROSE | NO_CHANGE | Prose «বলে বর্ণিত আছে»; notebook already records Tabarani «সনদ দুর্বল» (REF-260). |
| REF-259 | 9 | ১১ | 8969 | CAND | NO_CHANGE | Candidate source identified (research layer); page/number lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-260 | 9 | ১১ | 8970 | CAND | NO_CHANGE | Candidate source identified (research layer); page/number lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-263 | 10 | ০১ | 9003 | PROSE | NO_CHANGE | Prose certainty («বর্ণিত আছে») does not exceed the source status; dialogue unchanged. |
| REF-264 | 10 | ০১ | 9049 | VL | NO_CHANGE | Number + text verified live; number already printed; no grade to add. |
| REF-267 | 10 | ০২ | 9097 | PROSE | NO_CHANGE | Prose certainty («বর্ণিত আছে») does not exceed the source status; dialogue unchanged. |
| REF-268 | 10 | ০২ | 9105 | PROSE | NO_CHANGE | Prose certainty («বর্ণিত আছে») does not exceed the source status; dialogue unchanged. |
| REF-269 | 10 | ০২ | 9124 | PROSE | NO_CHANGE | Prose «বর্ণিত আছে»; grade of Tirmidhi 3206 printed via REF-144/274. |
| REF-270 | 10 | ০২ | 9158 | SPC | NO_CHANGE | Shia source correctly named; vol/page/hadith lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-275 | 10 | ০৩ | 9251 | VL | NO_CHANGE | Number + text verified live; number already printed; no grade to add. |
| REF-281 | 10 | ০৫ | 9358 | PROSE | NO_CHANGE | Prose certainty («বর্ণিত আছে») does not exceed the source status; dialogue unchanged. |
| REF-282 | 10 | ০৫ | 9402 | CAND | NO_CHANGE | Candidate source identified (research layer); page/number lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-283 | 10 | ০৫ | 9403 | CAND | NO_CHANGE | Candidate source identified (research layer); page/number lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-284 | 10 | ০৫ | 9404 | SPC | NO_CHANGE | Shia source correctly named; vol/page/hadith lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-285 | 10 | ০৬ | 9467 | VL | NO_CHANGE | Number + text verified live; number already printed; no grade to add. |
| REF-286 | 10 | ০৮ | 9509 | SPC | NO_CHANGE | Shia source correctly named; vol/page/hadith lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-287 | 10 | ০৮ | 9518 | PROSE | NO_CHANGE | Prose certainty («বর্ণিত আছে») does not exceed the source status; dialogue unchanged. |
| REF-288 | 10 | ০৮ | 9520 | PROSE | NO_CHANGE | Prose certainty («বর্ণিত আছে») does not exceed the source status; dialogue unchanged. |
| REF-289 | 10 | ০৮ | 9527 | PROSE | NO_CHANGE | Prose certainty («বর্ণিত আছে») does not exceed the source status; dialogue unchanged. |
| REF-290 | 10 | ০৮ | 9544 | CAND | NO_CHANGE | Candidate source identified (research layer); page/number lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-291 | 10 | ০৮ | 9545 | SPC | NO_CHANGE | Shia source correctly named; vol/page/hadith lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-293 | 10 | ০৮ | 9548 | VL | NO_CHANGE | Bukhari 6463 verified; Muslim 2818 (2818.01 «لن يدخل الجنة أحدا عمله») verified live. |
| REF-297 | 10 | ০৯ | 9628 | HIST | NO_CHANGE | Already labels Mizan al-Hikma as the conduit and every item PAGE-CHECK; primaries cannot be traced here (BUG-29 open). |
| REF-300 | 10 | ১০ | 9665 | PROSE | NO_CHANGE | Prose certainty («বর্ণিত আছে») does not exceed the source status; dialogue unchanged. |
| REF-301 | 10 | ১০ | 9696 | CAND | NO_CHANGE | Candidate source identified (research layer); page/number lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-302 | 11 | ০১ | 9825 | PROSE | NO_CHANGE | Prose certainty («বর্ণিত আছে») does not exceed the source status; dialogue unchanged. |
| REF-303 | 11 | ০১ | 9856 | CAND | NO_CHANGE | Candidate source identified (research layer); page/number lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-306 | 11 | ০৪ | 10069 | PROSE | NO_CHANGE | Prose certainty («বর্ণিত আছে») does not exceed the source status; dialogue unchanged. |
| REF-308 | 11 | ০৬ | 10267 | PROSE | NO_CHANGE | Prose «বর্ণিত আছে»; source split handled in REF-309. |
| REF-310 | 11 | ০৭ | 10311 | PROSE | NO_CHANGE | Prose certainty («বর্ণিত আছে») does not exceed the source status; dialogue unchanged. |
| REF-311 | 11 | ০৭ | 10331 | PROSE | NO_CHANGE | Prose certainty («বর্ণিত আছে») does not exceed the source status; dialogue unchanged. |
| REF-312 | 11 | ০৭ | 10371 | VL | NO_CHANGE | Number + text verified live; number already printed; no grade to add. |
| REF-313 | 11 | ০৭ | 10372 | VL | NO_CHANGE | Number + text verified live; number already printed; no grade to add. |
| REF-314 | 11 | ০৮ | 10393 | PROSE | NO_CHANGE | Prose certainty («বর্ণিত আছে») does not exceed the source status; dialogue unchanged. |
| REF-315 | 11 | ০৮ | 10401 | PROSE | NO_CHANGE | Prose certainty («বর্ণিত আছে») does not exceed the source status; dialogue unchanged. |
| REF-316 | 11 | ০৮ | 10442 | VL | NO_CHANGE | Number + text verified live; number already printed; no grade to add. |
| REF-317 | 11 | ০৮ | 10443 | VL | NO_CHANGE | Bukhari 3267 verified; Muslim 2989 now verified live via Abd al-Baqi prefix (2989.01 «فتندلق أقتاب بطنه») — six-book report's ⚠ can be cleared. |
| REF-318 | 11 | ০৮ | 10444 | CAND | NO_CHANGE | Candidate source identified (research layer); page/number lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-319 | 11 | ১৮ | 10598 | PROSE | NO_CHANGE | Prose certainty («বর্ণিত আছে») does not exceed the source status; dialogue unchanged. |
| REF-320 | 11 | ১৮ | 10655 | CAND | NO_CHANGE | Candidate source identified (research layer); page/number lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-322 | 11 | ১৮ | 10657 | HIST | NO_CHANGE | Non-hadith (history / geography / literature / chapter note); page lock only. |
| REF-323 | 11 | ১৮ | 10658 | HIST | NO_CHANGE | Non-hadith (history / geography / literature / chapter note); page lock only. |
| REF-324 | 11 | ১১ | 10707 | PROSE | NO_CHANGE | Prose certainty («বর্ণিত আছে») does not exceed the source status; dialogue unchanged. |
| REF-325 | 11 | ১১ | 10711 | PROSE | NO_CHANGE | Prose certainty («বর্ণিত আছে») does not exceed the source status; dialogue unchanged. |
| REF-326 | 11 | ১১ | 10740 | VL | NO_CHANGE | Number + text verified live; number already printed; no grade to add. |
| REF-327 | 11 | ১১ | 10741 | CAND | NO_CHANGE | Candidate source identified (research layer); page/number lock pending — PAGE-CHECK stays; no text change in this plan. |
| REF-328 | 11 | ১১ | 10742 | SPC | NO_CHANGE | Shia source correctly named; vol/page/hadith lock pending — PAGE-CHECK stays; no text change in this plan. |

## 5. Apply order (suggested)

1. HIGH + REVIEW=NO blocks: pure number and grade insertions (live evidence).
1. The MM blocks: Basra/Kufa (REF-276/279), the Abu Dawud 5021 fix, the Ark/Ahmad fix, «الجنة طيبة», the «مدينة العلم» split, REF-131.
1. S-181 rows (REF-078/079/081/082/122) together with the existing Part 3 Ch 06 patch and the «হাদী» amendment.
1. DUP normalisation by register key.
1. UNID keep-or-drop decisions (author).
1. Edition lock for every ⟦…⟧ slot. Re-run `tools/verify_sunni.py batch` with the fixed Muslim lookup. The gate stays **PRINT BLOCKED** until all of this is done.
