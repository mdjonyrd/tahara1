# B1_P01-11 — UMM AYMAN CONTROL v1.0 (Phase 6)

**Date:** 2026-10-03
**Gate:** `BOOK 1 · PARTS 1–11 — PRINT BLOCKED` (unchanged)
**Inputs:** `sources/S-181_UMM_AYMAN_FADAK_VERIFICATION.md` (read in full) · `manuscript-patches/B1_P03_C06_FADAK_S-181_PATCH.md` · ledger `audit/B1_P01-11_UNIDENTIFIED_REFERENCES_AUDIT_v1.2.csv` · audit v1.0 (BUG-01…03) and v1.1 · six-book corpus (`tools/_hadith-api`, read on 2026-10-03)
**Companion files:** `audit/B1_P01-11_FADAK_EVIDENCE_MAP_v1.0.csv` (rows C03/C04/C05) · `audit/B1_P01-11_SHIA_SOURCE_CONTROL_v1.0.csv` (REF-081/082 rows)

### Limits of this control
- The manuscript DOCX is **not available**. "Manuscript formulation now" means (a) the ledger `Text` column, which carries source-note bullets and a few prose lines, and (b) the "আগে" (before) text in the patch for p. 213 prose. Whether the patch has been applied to the DOCX **cannot be checked here**. Pages: ledger `Paragraph_Index` only; page = `PAGE-CHECK (docx not available)`.
- `VERIFIED-S181-URL` means S-181 cites a URL for the wording. That URL was **not** reopened here, because the network policy blocks it.
- `VERIFIED-LIVE` means I read the text today in the six-book Arabic corpus.

---

## 1. Passage inventory: every mention and the units it touches

Searched for উম্মে আইমান · আইমান · أم أيمن · Umm Ayman · জান্নাতি · কোলে · পিঠে · সাক্ষী · সাক্ষ্য · স্ত্রী · উম্মে হানী. Units: **ID** = identity · **REL** = relationship to the Prophet ﷺ · **PAR** = Paradise report · **FAD** = Fadak testimony · **FAM** = later marriage/family.

| Passage | Para. idx | What it says now | Units touched | Blending? |
|---|---|---|---|---|
| Ledger **REF-081** (P3 Ch06 source block) | 2816 | «উম্মে আইমানের সাক্ষ্য, আলী (আ.)-এর সাক্ষ্য, মসজিদে আবু বকরের সাথে বিতর্ক, আউস ইবনুল হাদাসান — কিতাবু সুলাইম…; আল-ইহতিজাজ ১ — PAGE-CHECK» | FAD | **YES (pre-patch):** Aus ibn al-Hadathan is in the same list as Umm Ayman/Ali. Ledger v1.1 splits this into 081a/081b, but the manuscript text is still merged until patch B is applied. |
| Ledger **REF-082** (P3 Ch06 source block) | 2817 | «"উম্মে আইমান জান্নাতি" — ইবনে সা'দ, আত-তাবাকাত — PAGE-CHECK» | PAR | No grade is printed. The «জান্নাতি» claim is unqualified (BUG-03). |
| Ledger **REF-078** (P3 Ch06 prose dialogue) | 2762 | «…বর্ণিত আছে, লিখেও দিয়ে গেছেন… আবার সাক্ষী লাগবে?» | FAD (deed context) | **YES:** the ledger maps «লিখেও দিয়ে গেছেন» (the Prophet wrote it) to al-Ihtijaj, where the writer is **Abu Bakr** (S-181 §3-D). See flag F-1. |
| Ledger **REF-122** (P6 Ch05) | 5291 | «আবু বকরের রাষ্ট্রীয় সম্পত্তি ঘোষণা — বালাযুরী; তাবারী … দলিল ছিঁড়ে ফেলা — সুয়ূতী…; ইবনে আবিল হাদীদ ১৬» | FAD (register HAD-FADAK-TESTIMONY) | **Risk:** Baladhuri (no deed) sits in the same bullet as the deed-tearing (al-Ihtijaj/IAH material). See flag F-6. |
| Ledger **REF-141** (P6 Ch10) | 5760 | «উম্মে হানী ও আবু বকরের কথোপকথন — জাওহারী…» | none (control) | **Name risk:** Umm **Hani** shares register key HAD-FADAK-TESTIMONY with the Umm **Ayman** rows. See flag F-7. |
| Ledger REF-085 (P3 Ch09) | 2988 | «ফাতিমা জান্নাতি নারীদের সর্দার» (Bukhari 3624) | none: refers to Fatima | Keep apart from the Umm Ayman «জান্নাতি» report. No blending found. |
| Ledger REF-027, REF-148 | 1572, 6121 | «সাক্ষী» = Ahl al-Bayt witnessed creation / 40,000 angels witnessed the marriage | none | Unrelated. |
| Ledger REF-106 | 4271 | «হুসাইন কোলে» (Mubahala) | none | Unrelated. **«কোলে-পিঠে মানুষ» does not occur in the ledger or the patch.** If the DOCX uses it for Umm Ayman, see unit REL. PAGE-CHECK in the DOCX. |
| Patch **A-1** (p. 213) | — | Before: «উম্মে আইমান — নবীজির স্ত্রী» → After: «…রাসূলুল্লাহ ﷺ-এর হাদী ও ঘনিষ্ঠ সেবিকা; পরে যায়েদ ইবনে হারিসা (রা.)-এর স্ত্রী এবং উসামা… মা» | ID, REL, FAM | Fixed in the patch. Lexical flag F-5 on «হাদী». |
| Patch **A-2** (p. 213) | — | Before: «রাসূলুল্লাহ ﷺ বলেছেন, উম্মে আইমান জান্নাতি নারী।» → After: option (ক) Ibn Sa'd mursal / option (খ) Bihar 29 Shia | PAR | Fixed in the patch. Flag F-3: option (খ) has no named speaker. |
| Patch **A-3** (p. 213) | — | Before: «উম্মে আইমান, আলী (আ.) আর আউস ইবনুল হাদাসান সাক্ষ্য দিলেন…» → After: separate sentences; Aus moved to the opposing side | FAD | Fixed. Flag F-4: the Aus sentence has no tradition attribution. |
| Patch **B** bullets 1–4 (p. 217) | — | Replacement source block | ID, REL, PAR, FAD, FAM | Flags F-2, F-8, F-9. |
| S-181 §1 / §2 / §3 | — | Research findings | all | S-181 itself keeps the units apart (§0, §2-D note, §3-F). |

---

## 2. Unit control table

Status vocabulary: VERIFIED-LIVE · VERIFIED-S181-URL · PAGE-CHECK · CANDIDATE · NOT VERIFIED · EDITION-LOCK PENDING.

| Unit | Manuscript formulation now (ledger/patch) | Allowed formulation | Forbidden formulation | Source + status | Rows |
|---|---|---|---|---|---|
| **IDENTITY** | Pre-patch p. 213: «উম্মে আইমান — নবীজির স্ত্রী». Patch A-1: «উম্মে আইমান (বারাকা বিনতে সা'লাবা) …». No ledger row carries the name/identity. | «উম্মে আইমান (বারাকা বিনতে সা'লাবা)», with the source attributed. | **«উম্মে আইমান ছিলেন রাসূলের স্ত্রী»** / «নবীজির স্ত্রী» (S-181 §1: FALSE). Any specific owner claim such as «আমিনার দাসী» (S-181 §1-D: not safe). | Name «بركة بنت ثعلبة … وهي أم أيمن»: Ibn Abd al-Barr, *al-Isti'ab*, **VERIFIED-S181-URL**; pagination conflict (vol. 12 pp. 221–223 vs pp. 876–877): PAGE-CHECK. Ibn Hajar, *al-Isaba* 4/415–416: VERIFIED-S181-URL, edition PAGE-CHECK. Name not checked in the six books, which use only «أم أيمن». | Patch A-1, B•1; S-181 §1 |
| **RELATIONSHIP TO PROPHET** | Patch A-1: «রাসূলুল্লাহ ﷺ-এর হাদী ও ঘনিষ্ঠ সেবিকা». Patch B•1: «রাসূল ﷺ-এর হাদী ও মাওলা». «কোলে-পিঠে মানুষ» is not attested in the ledger or patch (PAGE-CHECK in DOCX). | «রাসূল ﷺ-এর মাওলা (মুক্ত দাসী) ও লালনকারিণী (হাদিনা, حاضنة)». A literary paraphrase such as «যাঁর কোলে-পিঠে নবীজি বড় হয়েছেন» is acceptable only as narration of «حاضنة», not as a quotation. | «স্ত্রী» in any form. «মা» stated as fact, because «أم أيمن أمي بعد أمي» is a report in *al-Isti'ab* whose grade is not established in the repo. It may be quoted only as «আল-ইসতি'আবে বর্ণিত», never as flat «রাসূল ﷺ বলেছেন». Do not use «হাদী» alone (flag F-5). | **VERIFIED-LIVE:** Bukhari 2630 / Muslim 1771.01 «أم أيمن **مولاته** أم أسامة بن زيد». Bukhari 3737 «وكانت **حاضنة** النبي ﷺ». This comes in an appended remark («وحدثني بعض أصحابي عن سليمان»), so cite it as Bukhari's appended note. Muslim 2453 (the Prophet visits her); Muslim 2454 = Ibn Majah 1635 (Sahih per corpus): Abu Bakr and Umar visit her «كما كان رسول الله ﷺ يزورها». **VERIFIED-S181-URL:** al-Isaba «مولاة النبي ﷺ وحاضنته». | Patch A-1, B•1; S-181 §1-C/§1-D |
| **PARADISE REPORT (a) Sunni: Ibn Sa'd** | REF-082: «"উম্মে আইমান জান্নাতি" — ইবনে সা'দ — PAGE-CHECK». Pre-patch prose: «রাসূলুল্লাহ ﷺ বলেছেন, উম্মে আইমান জান্নাতি নারী». Patch A-2(ক) and B•2 correct this. | «ইবনে সা'দের *আত-তাবাকাতুল কুবরা*-তে একটি **মুরসাল** বর্ণনায় এসেছে — "যে জান্নাতের একজন নারীকে বিবাহ করতে চায়, সে উম্মে আইমানকে বিবাহ করুক।"» The grade goes in the source block: «সুফইয়ান ইবনে উকবা থেকে; মুরসাল — সুয়ূতী: মুরসাল; আলবানী: যয়ীফ (সিলসিলাতুয যয়ীফা ২২৬০ — PAGE-CHECK)». | **Unqualified «উম্মে আইমান জান্নাতি» stated as a sahih fact.** «সহিহ হাদিসে রাসূল ﷺ বলেছেন…». Flat «রাসূল ﷺ বলেছেন» (Global Law: no weak report as a flat saying). Paraphrasing it as «তিনি জান্নাতি» without the conditional «যে বিবাহ করতে চায়…» frame. | Wording «من سره أن يتزوج امرأة من أهل الجنة فليتزوج أم أيمن» (sanad: عبيد الله بن موسى ← فضيل بن مرزوق ← سفيان بن عقبة): **VERIFIED-S181-URL** (dorar.net/h/ipCT1d90). Transmission: **mursal** (Sufyan b. Uqbah, no Companion); al-Suyuti: **مرسل**; al-Albani: **ضعيف**, *Silsilat al-Da'ifa* no. 2260 (reported, PAGE-CHECK; grading record dorar.net/h/R71ZmTA4). Location: «vol. 8, p. 224» vs biography in «vol. 10»: **EDITION-LOCK PENDING** (two editions mixed; S-181 §1-A). | REF-082; Patch A-2(ক), B•2; S-181 §2-A/2-B |
| **PARADISE REPORT (b) Shia: Bihar 29** | Patch A-2(খ): «শিয়া সূত্রে ফাদাকের বর্ণনার ভিতরেই আছে — উম্মে আইমান জান্নাতের নারী (বিহারুল আনওয়ার, খণ্ড ২৯)». Not in the ledger as a separate row (REF-082's resolution note). | «শিয়া সূত্রে, ফাদাকের বর্ণনার ভিতরে এসেছে: "إن أم أيمن امرأة من أهل الجنة"» (Bihar 29), with Shia attribution every time. | Merging (a) and (b) into one statement, as if one report had a Sunni and a Shia chain. Presenting (b) as a direct saying of the Prophet ﷺ: S-181 does not identify the speaker in the quoted line (flag F-3). Citing (b) for the marriage wording. | al-Majlisi, *Bihar al-Anwar* 29, bab 11 «نزول الآيات في أمر فدك»: **VERIFIED-S181-URL** (najafdesertlibrary …/v/29/p/176). p. 176 (online) vs p. 128 (other edition): **EDITION-LOCK PENDING**. al-Ihtijaj carries the parallel «أم أيمن امرأة من أهل الجنة» inside the Fadak narrative (S-181 §3-D; the speaker is elided as «فقال …»). | REF-082 (note), REF-081; Patch A-2(খ), B•2; S-181 §2-D |
| **PARADISE REPORT (c) al-Hakim** | Not in the current ledger text. REF-082's ledger status says «Hakim NOT VERIFIED». S-181 §2-C rules that if the DOCX names al-Hakim for this claim, the citation is removed. PAGE-CHECK in the DOCX. | Nothing. Do not mention al-Hakim with this claim. | Any «হাকিম / আল-মুস্তাদরাক» citation for the Paradise wording. | **NOT VERIFIED / PRINT BLOCKED** (S-181 §2-C). The Mustadrak Umm Ayman biography reports (reported as h. 6910–6912 / 7084–7087) are not this report. | S-181 §2-C; patch checklist C |
| **FADAK TESTIMONY** | REF-081: Umm Ayman + Ali + debate + Aus in one bullet (pre-patch). Pre-patch prose: «উম্মে আইমান, আলী (আ.) আর আউস ইবনুল হাদাসান সাক্ষ্য দিলেন». Patch A-3 / B•3–4 separate them. | Each recension under its own attribution: **Sunni, Baladhuri R1:** Ali, then Umm Ayman; Abu Bakr: «لا تجوز إلا شهادة رجلين أو رجل وامرأتين». **Baladhuri R2:** Umm Ayman + **Rabah**; «لا تجوز فيه إلا شهادة رجل وامرأتين». **Shia, al-Ihtijaj:** Umm Ayman, then Ali; Abu Bakr writes a deed; Umar takes/tears it and says «أم أيمن… امرأة صالحة، لو كان معها غيرها لنظرنا فيه». **Shia, Sulaym:** «ولم يصدقها، ولا صدق أم أيمن». **Ibn Abi al-Hadid 16:** «إن أم أيمن تشهد لي بأن رسول الله أعطاني فدك». Aus ibn al-Hadathan appears **only** in a separate sentence, as a counter-witness with Aisha and Hafsa (Shia: Qurb al-Isnad; al-Ihtijaj), with «শিয়া সূত্রে» attribution. | Aus ibn al-Hadathan as Umm Ayman's or Ali's co-witness. A composite of Baladhuri and al-Ihtijaj, or of R1 and R2 (for example «Ali + Umm Ayman + Rabah»). «Baladhuri: deed torn». Citing any six-book hadith for Umm Ayman's testimony: string search «فدك»+«أم أيمن» gives 0 hits (NOT FOUND ≠ does not exist). Equating Sunni **Malik** b. Aws b. al-Hadathan, narrator of Umar's adjuration (Bukhari 3094, Muslim 1757), with the Shia «Aus b. al-Hadathan» witness. | Baladhuri R1/R2: **VERIFIED-S181-URL**, edition PAGE-CHECK. al-Ihtijaj 1: **VERIFIED-S181-URL**, EDITION-LOCK PENDING (pp. 90–92 vs 119–127). Sulaym: **VERIFIED-S181-URL** (digital), print PAGE-CHECK. IAH 16/213–214, 216, 225, 273–275: **VERIFIED-S181-URL**, edition PAGE-CHECK. Bihar 29: **VERIFIED-S181-URL**. Aus: Qurb al-Isnad h. 99/335 **VERIFIED-S181-URL**; Bihar 22/101 h. 59 PAGE-CHECK. Detail in the Fadak map, rows C03–C07. | REF-081, REF-078, REF-122, REF-141 (control); Patch A-3, B•3–4; S-181 §3 |
| **LATER MARRIAGE / FAMILY** | Patch A-1: «পরে যায়েদ ইবনে হারিসা (রা.)-এর স্ত্রী এবং উসামা ইবনে যায়েদ (রা.)-এর মা». No ledger row. | «পরে তিনি যায়েদ ইবনে হারিসা (রা.)-কে বিবাহ করেন এবং উসামা ইবনে যায়েদ (রা.)-এর মা হন», citing the biography sources. Optional: earlier marriage to Ubayd al-Habashi and son Ayman (al-Isti'ab). | Using the **mursal** Paradise report as the source for the marriage. That report ends «فتزوجها زيد بن حارثة فولدت له أسامة», but the reason it gives for the marriage belongs to the mursal report and must not be presented as an established motive. Any wording that makes her the Prophet's wife. | **VERIFIED-LIVE:** Bukhari 2630 / Muslim 1771.01 «أم أسامة بن زيد». Bukhari 3736 «أيمن ابن أم أيمن أخا أسامة لأمه» (Ayman is Usama's maternal half-brother). **VERIFIED-S181-URL:** Ibn Sa'd «وتزوجها زيد بن حارثة بعد النبوة فولدت له أسامة» (amuslim mirror); al-Isti'ab «تزوجها زيد بن حارثة بعد عبيد الحبشي، فولدت له أسامة». Edition: PAGE-CHECK. | Patch A-1, B•1; S-181 §1 |

---

## 3. Six-book live evidence found in this pass (not in S-181)

| Number | Wording (corpus) | Unit | Use |
|---|---|---|---|
| Bukhari 2630 | «فأعطاهن النبي ﷺ أم أيمن مولاته أم أسامة بن زيد» | REL, FAM | Primary Sunni proof of *mawla* status and Usama's mother. |
| Muslim 1771.01 | «فأعطاها رسول الله ﷺ أم أيمن مولاته أم أسامة بن زيد» | REL, FAM | Same. |
| Bukhari 3737 | «…وكانت حاضنة النبي ﷺ» (appended remark) | REL | Supports «লালনকারিণী». Note that it is an appended remark. |
| Bukhari 3736 | «أيمن ابن أم أيمن أخا أسامة لأمه» | FAM | Her son Ayman. |
| Muslim 2453; Muslim 2454 = Ibn Majah 1635 (Sahih per corpus) | the Prophet visits her; Abu Bakr and Umar visit her after his death «كما كان رسول الله ﷺ يزورها» | REL | Shows her closeness to the Prophet. Not Fadak evidence. |
| Bukhari 4120 / Muslim 1771.02 | the Prophet gave her date palms (an Ansari gift) and compensated her about tenfold when they were reclaimed | REL | **Not Fadak.** Never cite it for the Fadak grant or testimony. |

The six books contain **no** Umm Ayman Fadak testimony and **no** Paradise report about her, based on string searches for «أم أيمن», «فدك»+«أم أيمن», «أهل الجنة»+«أم أيمن».

---

## 4. Residual blending flags

| # | Where | Problem | Required action |
|---|---|---|---|
| **F-1** | Ledger REF-078 resolution note (and the patch, which does not address REF-078's sentence) | The manuscript says the **Prophet** «লিখেও দিয়ে গেছেন». The ledger equates this with the al-Ihtijaj deed, whose writer is **Abu Bakr** («فكتب لها كتابا ودفعه إليها»). The two claims are different. | Keep «বর্ণিত আছে» with no al-Ihtijaj citation for the Prophet-wrote version, **or** change the dialogue to the Ihtijaj recension with «শিয়া সূত্রে» attribution. This is the author's decision; I made no rewrite. |
| **F-2** | Patch B•2 | The Ibn Sa'd (Sunni, mursal) report and the Bihar 29 (Shia) report sit in **one bullet**. Each has its own attribution, which is acceptable, but they must never collapse into one citation line or one «জান্নাতি» sentence. | Keep the line break and the «শিয়া সূত্রে:» marker. |
| **F-3** | Patch A-2(খ); S-181 §2-D/§3-D | The quoted Shia line «إن أم أيمن امرأة من أهل الجنة» has **no identified speaker** in S-181. In al-Ihtijaj the speaker is elided («فقال …»). | Do not turn it into «রাসূল ﷺ বলেছেন» until the page is read. PAGE-CHECK the speaker in Bihar 29 / al-Ihtijaj. |
| **F-4** | Patch A-3 optional Aus sentence | «অন্য পক্ষে আয়েশা, হাফসা ও আউস ইবনুল হাদাসান — এঁরা সাক্ষ্য দিলেন…» carries **no tradition attribution**, although the patch's own rule requires «সুন্নি…/শিয়া…» every time. The wording «আমরা নবীরা…» matches al-Ihtijaj («إنا معاشر الأنبياء لا نورث»). Qurb al-Isnad has the singular «لا أورث». | Prefix «শিয়া সূত্রে (কুরবুল ইসনাদ; আল-ইহতিজাজ)…» and quote the wording of the source cited. |
| **F-5** | Patch A-1, B•1, S-181 §1 Bengali wording | «হাদী» is meant for حاضنة (nurse). In Bengali it reads as হাদী = هادي (guide), the same word the book uses for Ali in REF-179 («তুমিই পথপ্রদর্শক / الهادي»). This is a lexical ambiguity, not a source error. | Prefer «লালনকারিণী (হাদিনা)». Author's choice. |
| **F-6** | Ledger REF-122 | In one bullet, Baladhuri/Tabari («state property») stand next to the deed-tearing (Suyuti; IAH 16). S-181 §3-F: Baladhuri has **no deed**, because Abu Bakr rejects the testimony. «Suyuti, Tarikh al-Khulafa» for the tearing was **not located**. | Split the bullet. Cite the tearing only to al-Ihtijaj (VERIFIED-S181-URL) or to IAH 16 once the page is found (CANDIDATE). Drop Suyuti unless a page is found. |
| **F-7** | Register key HAD-FADAK-TESTIMONY (REF-078, 081, 122, 141) | One "canonical lock = S-181" covers four different units: deed (078), testimony (081), state property/tearing (122), and **Umm Hani** (141, a different woman). Normalising them to one citation would merge narrations. | Split the register into sub-keys, for example FADAK-TESTIMONY-BALADHURI / -IHTIJAJ / FADAK-DEED / FADAK-COUNTER-AUS / FADAK-UMM-HANI. This is a recommendation only. |
| **F-8** | Patch B•1 vs register HAD-UMM-ABIHA | Edition mixing across the book. *al-Isaba* «4/415–416» for Umm Ayman (a 4-volume-style numbering) vs *al-Isaba* «8:262» for Fatima (REF-069/155/255). *al-Isti'ab*: «vol. 12 / pp. 876–877» (S-181) vs «4:1899» (HAD-UMM-ABIHA). Ibn Sa'd: «vol. 8 p. 224» vs «vol. 10» (S-181 §1-A) vs «8:24» (REF-150). | Lock **one** edition per work for the whole book (S-181 §5 checklist + BUG-26). |
| **F-9** | Patch B•3 | Kitab Sulaym is cited under «ফাদাকে আলী ও উম্মে আইমানের সাক্ষ্য», but the Sulaym text S-181 quotes covers only the bayyina demand and Umm Ayman not being believed. Ali's testimony in Sulaym is **not quoted anywhere** in the repo. | PAGE-CHECK Sulaym for Ali before the bullet implies it. |
| **F-10** | Patch B•1 parenthesis «أم أيمن أمي بعد أمي» | It is printed inside the identity citation with no grade. Its transmission status is not established in the repo. | Either give its grade or attribute it as «আল-ইসতি'আবে বর্ণিত». Never as a flat saying. |

No blending was found in: REF-085 (Fatima «জান্নাতি নারীদের সর্দার»), REF-027/148 («সাক্ষী»), REF-106 («কোলে»).

---

## 5. What could not be verified here
- None of the S-181 URLs could be reopened (dorar.net and other sites are blocked). Every `VERIFIED-S181-URL` therefore rests on the S-181 research layer.
- Edition and page locks for: Ibn Sa'd (vol. 8 vs 10), al-Isti'ab (vol. 12 / 876–877), al-Isaba 4/415–416, Baladhuri (p. 30/35 vs 44–45 vs «527»), Bihar 29 (p. 128 vs 176), Bihar 22/101 h. 59, Qurb al-Isnad (h. 99 vs 335), al-Ihtijaj 1 (pp. 90–92 vs 119–127), Sulaym (printed page), Ibn Abi al-Hadid 16 (edition), al-Albani *Silsilat al-Da'ifa* 2260.
- The speaker of «إن أم أيمن امرأة من أهل الجنة» in Bihar 29 and al-Ihtijaj.
- Whether the DOCX still contains «নবীজির স্ত্রী», «রাসূলুল্লাহ ﷺ বলেছেন… জান্নাতি», the merged Aus sentence, any Hakim attribution, or «কোলে-পিঠে মানুষ». The DOCX is not available, and whether the patch has been applied is unknown.
- The grade of «أم أيمن أمي بعد أمي».
