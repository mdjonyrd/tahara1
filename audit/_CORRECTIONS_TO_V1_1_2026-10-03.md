# Corrections to audit v1.1 / S-181 patch found by the v1.2 work package (all confirmed in the six-book corpus, 2026-10-03)

| # | Earlier claim (where) | Corpus shows | Consequence |
|---|---|---|---|
| C-01 | Abu Dawud 5023 = «من رآني في المنام فقد رآني» (BUG-13, HAD-RUYA) | 5023 reads «من رآني في المنام **فسيراني في اليقظة** … ولا يتمثل الشيطان بي» | The «فقد رآني» wording is Bukhari 110 (and Muslim 2266 variants); cite 5023 only for «فسيراني في اليقظة» |
| C-02 | «وهي جويرية فأقبلت تسعى» = Bukhari 3110 (BUG-12 mapping for REF-075) | It is **Bukhari 520** (Ibn Mas'ud, Salat); 3110 has no such wording | Fix the REF-075 number map |
| C-03 | «الدعاء هو العبادة» = Tirmidhi 3370 (REF-016) | **Tirmidhi 3372** (Nu'man b. Bashir) | Fix number |
| C-04 | REF-224 = Tirmidhi 2951 | Ibn Abbas «من قال في القرآن بغير علم» is **Tirmidhi 2950**; 2951 is «اتقوا الحديث عني» | Two numbers, two wordings |
| C-05 | «أنت على مكانك وأنت على خير» = Tirmidhi 3871 (REF-186) | 3871 is the Umm Salama kisa report without that phrase; the phrase is **Tirmidhi 3205** («وأنت على خير») and **3787** («وأنت إلي خير») | Cite 3205/3787 for the phrase, 3871 for the cloak |
| C-06 | Bukhari 2010: «نعمت البدعة هذه» (REF-054) | Corpus: «**نعم** البدعة هذه» | Spelling per the cited edition |
| C-07 | v1.0 BUG-05: Bukhari 3767 = «سيدة نساء» | 3767 = «فاطمة بضعة مني» (Miswar); «سيدة نساء» is 3624 | Fix BUG-05 |
| C-08 | BUG-30: Muslim 2175 «يبلغ» vs Bukhari «يجري» | Muslim 2175 has **both** («يجري» 2175.01, «يبلغ» 2175.02, explicitly «ولم يقل يجري»); Bukhari 2035 has «يبلغ» | Wording varies within each book — quote the sub-report |
| C-09 | Muslim 2408 CONFIRMED for «ইতরাত» (REF-157) | Muslim has no «عترتي» anywhere; 2408 has «ثقلين … وأهل بيتي» | «عترتي» rests on Tirmidhi 3786/3788 only |
| C-10 | Tirmidhi 3723 «دار الحكمة» graded da'if by later scholars | Tirmidhi himself: «هذا حديث **غريب منكر**» (compiler grade in corpus text) | Print compiler grade |
| C-11 | Abu Dawud 2972 CONFIRMED in S-181 patch | Text: Umar b. Abd al-Aziz … «**فأبى**» — the Prophet declined Fatima's request; graded da'if by three graders | It is a *contrary* report; cite with that content and grade |
| C-12 | «معاشر الأنبياء لا نورث» on Bukhari/Muslim numbers (REF-123 wording) | Six books have «لا نورث ما تركنا صدقة»; «معاشر الأنبياء» is the al-Ihtijaj wording | Separate the two wordings |
| C-13 | Muslim 2989 PAGE-CHECK (tool fallback) | 2989.02 (Usama, Abu Wa'il) is the mill-donkey report | ✅ |
| C-14 | Tool: `show muslim N` fell back to sequential numbering | Fixed; all Muslim numbers re-verified by Abd al-Baqi integer | Evidence trail restored |
| C-15 | Tirmidhi 3206 cited for the «নয় মাস» chapter (REF-274/269) | 3206 says **six** months, fajr only, da'if | Nine-month claim needs Shawahid al-Tanzil / Tabarani |
| C-16 | Malik b. Aws b. al-Hadathan vs Aus ibn al-Hadathan | Sunni narrator of the Fadak dispute (Bukhari 3094, Muslim 1757) ≠ Shia counter-witness Aus | Never conflate |
| C-17 | Basra correction rests on Bukhari 784 **and** 786 | Only **784** contains «بالبصرة»; 786 (Mutarrif) names no place | Cite 784 for the place; 786 only for the takbir detail |
| C-18 | Muslim 91 = verbatim «مثقال حبة من خردل من كبر» (BUG-16) | Muslim 91 reads «ذرة من كبر» / «حبة خردل من كبرياء»; the verbatim wording is Abu Dawud 4091, Tirmidhi 1998, Ibn Majah 59 / 4173 | Cite the book whose wording is quoted |
| C-19 | Bukhari 7083 / Muslim 2888 «إذا التقى المسلمان بسيفيهما» (REF-313) | 7083 and 2888.01 read «إذا **تواجه** المسلمان بسيفيهما»; «التقى» is Bukhari 31, 6875 and Muslim 2888.02 | Quote the sub-report actually cited |
| C-20 | Tirmidhi 3871 for «أنت على مكانك» (REF-186) | 3871 reads «إنك على خير»; «أنت على مكانك» is 3205 / 3787 | (as C-05) |
| C-21 | `show muslim 2816` complete | The first two 2816 sub-reports are unnumbered in the corpus; use `search` for them | Tool caveat recorded in tools/README |
| C-22 | HAD-MADINAT-ILM = 5 rows (BUG-26) | 6 rows incl. prose REF-308 | Register updated |
| C-23 | CL-HAD-008 single hadith | Used for two different hadiths (REF-250 Bukhari 3714; REF-251 Hakim 4730) | Split the CL id |
| C-24 | REF-158 Ahmad «3/364» vs candidate «3/346» | Page conflict inside the ledger | Lock from Musnad edition |
