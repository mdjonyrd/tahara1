# Live check — numbered Sunni references vs. the six canonical collections

**Date:** 2026-10-03
**Tool:** `tools/verify_sunni.py batch` → raw output `sunni_six_books_check_2026-10-03.raw.txt`
**Corpus:** fawazahmed0/hadith-api Arabic editions (GitHub sparse clone). Numbering = standard (sunnah.com) for Bukhari, Abu Dawud, Tirmidhi, Ibn Majah; Muslim matched on Abd al-Baqi `arabicnumber`.
**Why not sunnah.com / dorar.net:** both (and cdn.jsdelivr.net) are denied by this cloud environment's network policy; GitHub is allowed.
**Scope:** every hadith *number* the ledger cites in the six books, plus substring searches for wordings the ledger attributes to those books. Shia sources and Sunni works outside the six books (Hakim, Tabarani, Ahmad, Bayhaqi…) could **not** be checked here — they stay PAGE-CHECK / CANDIDATE.

Verdicts: ✅ number + text match the ledger's claim · ⚠ number right, grading/wording note needed · ❌ mismatch (correction given) · ∅ wording absent from all six books.

## A. Numbers checked

| Book | No. | Ledger rows | Content found | Grade shown | Verdict |
|---|---|---|---|---|---|
| Bukhari | 1 | 326 | إنما الأعمال بالنيات (Umar) | — | ✅ |
| Bukhari | 110 | 013, 201 | من رآني في المنام فقد رآني (Abu Hurayra) | — | ✅ |
| Bukhari | 114 / 4431 | 134, 158 | ائتوني بكتاب / يوم الخميس (Ibn Abbas) | — | ✅ |
| Bukhari | 528 | 285 | نهر بباب أحدكم (Abu Hurayra) | — | ✅ |
| Bukhari | 530 | 278 | al-Zuhri: Anas weeping in Damascus | — | ✅ |
| Bukhari | 631 | 277 | Malik b. al-Huwayrith, صلوا كما رأيتموني | — | ✅ |
| Bukhari | 784 / 786 | 276, 279 | Imran b. Husayn prayed with Ali **بالبصرة** | — | ❌ manuscript says Kufa |
| Bukhari | 936 | 045 | Jabir: twelve men remained (62:11) | — | ✅ |
| Bukhari | 956 / 957 | 044 | Eid: prayer before khutba (Abu Sa'id / Ibn Umar) | — | ✅ |
| Bukhari | 1129 | 053 | Aisha: خشيت أن تفرض عليكم | — | ✅ |
| Bukhari | 1350 | 202 | Jabir: Abdullah b. Ubayy, the shirt | — | ✅ |
| Bukhari | 1385 | 065 | كل مولود يولد على الفطرة | — | ✅ |
| Bukhari | 1954 | 049 | Umar: إذا أقبل الليل … فقد أفطر الصائم | — | ✅ (ledger's «1815» = Bengali ed.) |
| Bukhari | 2010 | 054 | نعمت البدعة هذه | — | ✅ |
| Bukhari | 2035 / 3101 / 7171 | 039 | Safiyya story (Ali b. Husayn) | — | ✅ 7171 is this story (Ahkam) |
| Bukhari | 3093 / 6726 | 123 | Fatima asks Abu Bakr for inheritance (Khumus / Fara'id) | — | ✅ |
| Bukhari | 3110 | 075 | Ali b. Husayn … فاطمة عليها السلام … جويرية فأقبلت تسعى | — | ✅ |
| Bukhari | 3267 | 317 | Usama: كالحمار يدور برحاه | — | ✅ |
| Bukhari | 3623 / 3624 | 085, 132, 262 | Aisha: مرحبا بابنتي … سيدة نساء | — | ✅ |
| Bukhari | 3636 | 307 | Ibn Mas'ud: moon split, اشهدوا | — | ✅ |
| Bukhari | 3705 | 067 | Ali: Fatima and the mill | — | ✅ |
| Bukhari | 3706 | 236 | بمنزلة هارون من موسى (Sa'd) | — | ✅ |
| Bukhari | 3714 | 072, 076, 142, 153, 250 | فاطمة بضعة مني فمن أغضبها أغضبني — **only this clause** | — | ✅ |
| Bukhari | 3752 | 262 | Anas: none resembled the Prophet more than Hasan | — | ✅ |
| Bukhari | 4240 | 079, 126, 131 | …فهجرته فلم تكلمه حتى توفيت … **دفنها زوجها علي ليلا ولم يؤذن بها أبا بكر** | — | ✅ night burial IS in 4240 |
| Bukhari | 4474 | 273 | Abu Sa'id b. al-Mu'alla did not answer the call | — | ✅ |
| Bukhari | 4966 | 105 | Ibn Abbas: الكوثر الخير الذي أعطاه الله | — | ✅ (ledger said no source) |
| Bukhari | 5230 | 142 | Miswar: يريبني ما أرابها (Ali's proposal) | — | ✅ |
| Bukhari | 6463 | 293 | لن ينجي أحدا منكم عمله | — | ✅ |
| Bukhari | 6993 | 201 | من رآني في المنام فسيراني في اليقظة | — | ✅ |
| Bukhari | 7083 | 313 | إذا التقى المسلمان بسيفيهما (Abu Bakra via Hasan) | — | ✅ |
| Bukhari | 7222 | 143, 152, 240 | يكون اثنا عشر أميرا … كلهم من قريش | — | ✅ |
| Muslim | 8 | 298 | Hadith Jibril (ihsan) | — | ✅ |
| Muslim | 91 | 087 | لا يدخل الجنة من في قلبه مثقال حبة من خردل من كبر | — | ✅ (ledger said no source) |
| Muslim | 395 | 264 | قسمت الصلاة بيني وبين عبدي | — | ✅ |
| Muslim | 667 | 285 | river example | — | ✅ |
| Muslim | 705 | 275 | Ibn Abbas: joined prayers in Madina | — | ✅ |
| Muslim | 761 | 053 | Aisha: tarawih, fear of obligation | — | ✅ |
| Muslim | 863 | 045 | Jabir: caravan on Friday | — | ✅ |
| Muslim | 1015 | 022 | إن الله طيب لا يقبل إلا طيبا | — | ∅ not the ledger's wording |
| Muslim | 1637 | 134, 158 | pen-and-paper (Ibn Abbas) | — | ✅ |
| Muslim | 1759 | 123 | Fatima → Abu Bakr; لا نورث (also 1757–1758) | — | ✅ |
| Muslim | 1821 / 1822 | 143, 240 | اثنا عشر خليفة | — | ✅ |
| Muslim | 1851 | 083 | من مات وليس في عنقه بيعة | — | ✅ |
| Muslim | 1905 | 316 | first three judged (Abu Hurayra) | — | ✅ |
| Muslim | 1907 | 326 | إنما الأعمال بالنية | — | ✅ |
| Muslim | 2175 | 039 | Safiyya: يبلغ من الإنسان مبلغ الدم | — | ⚠ wording differs from Bukhari's مجرى الدم |
| Muslim | 2266 | 201 | من رآني في المنام | — | ✅ |
| Muslim | 2404 | 080, 107, 236 | Sa'd: manzila + mubahala (هؤلاء أهلي) | — | ✅ |
| Muslim | 2408 | 043, 157, 206, 242, 258 | Zayd b. Arqam: وأهل بيتي أذكركم الله | — | ✅ |
| Muslim | 2424 | 096, 188 | Aisha: مرط مرحل, kisa | — | ✅ |
| Muslim | 2449 | 142 | Miswar: يؤذيني ما آذاها | — | ✅ |
| Muslim | 2450 | 132 | Aisha: Fatima's whispered secret | — | ✅ |
| Muslim | 2581 | 312 | أتدرون ما المفلس | — | ✅ |
| Muslim | 2816–2818 | 293 | لن ينجي أحدا منكم عمله | — | ✅ |
| Muslim | 2888 | 313 | إذا التقى المسلمان بسيفيهما | — | ✅ |
| Muslim | 2989 | 317 | (concordance no.; text not surfaced by search) | — | ⚠ PAGE-CHECK |
| Abu Dawud | 2968 | 079 | Fatima/Fadak inheritance | Sahih (Albani) | ✅ |
| Abu Dawud | 2972 | 079 | Umar b. Abd al-Aziz restores Fadak | **Da'if (Albani)** | ⚠ grade is al-Albani's (BUG-01) |
| Abu Dawud | 3652 | 225 | Jundub: من قال في القرآن برأيه فأصاب | Da'if | ⚠ print grade |
| Abu Dawud | 4213 | 071 | Thawban: last/first with Fatima on travel | **Da'if** (Albani, Arnaut, Zubair) | ⚠ print grade |
| Abu Dawud | 4646 | 240 | خلافة النبوة ثلاثون سنة | Hasan sahih | ✅ |
| Abu Dawud | 4782 | 305 | Abu Dharr: if angry standing, sit | Sahih | ✅ |
| Abu Dawud | 4784 | 305 | anger from Shaytan → wudu | **Da'if** (Albani, Arnaut) | ⚠ print grade |
| Abu Dawud | 5019 | 013 | Abu Hurayra: الرؤيا ثلاث | Sahih | ✅ correct no. for "three kinds" |
| Abu Dawud | 5021 | 013 | Abu Qatada: الرؤيا من الله والحلم من الشيطان | Sahih | ❌ not the ledger's claim |
| Abu Dawud | 5023 | 013 | Abu Hurayra: من رآني في المنام فقد رآني | Sahih | ✅ correct no. for "saw me" |
| Abu Dawud | 5217 | 068, 252, 262 | Aisha: resemblance; قام إليها | Sahih / hasan sahih | ✅ |
| Tirmidhi | 4 | 271 | Jabir: مفتاح الجنة الصلاة | Sahih (Albani) / Da'if (Zubair) | ⚠ print grade |
| Tirmidhi | 614 / 2616 | 004 | الصدقة تطفئ الخطيئة كما يطفئ الماء النار | Sahih | ✅ resolves REF-004 |
| Tirmidhi | 1621 | 094 | المجاهد من جاهد نفسه | Sahih | ✅ |
| Tirmidhi | 2226 | 240 | الخلافة في أمتي ثلاثون سنة | Sahih / hasan | ✅ |
| Tirmidhi | 2951 | 223, 224 | Ibn Abbas: اتقوا الحديث عني … برأيه | Da'if | ⚠ print grade |
| Tirmidhi | 2952 | 225 | Jundub (as Abu Dawud 3652) | Da'if | ⚠ |
| Tirmidhi | 3205 / 3787 / 3871 | 186 | Umar b. Abi Salama / Umm Salama: kisa, أنت على مكانك | Sahih | ✅ |
| Tirmidhi | 3206 | 144, 187, 189, 274 | Anas: ستة أشهر … الصلاة يا أهل البيت | **Da'if** | ⚠ print grade |
| Tirmidhi | 3462 | 022 | الجنة طيبة التربة عذبة الماء (Ibn Mas'ud) | — | ∅ not the ledger's wording |
| Tirmidhi | 3540 | 261 | Anas: hadith qudsi يا ابن آدم … عنان السماء | Sahih / hasan | ✅ |
| Tirmidhi | 3713 | 012, 237 | من كنت مولاه فعلي مولاه | Sahih | ✅ |
| Tirmidhi | 3714 | 280 | رحم الله عليا اللهم أدر الحق معه | **Very da'if** | ⚠ wording ≠ «علي مع الحق» |
| Tirmidhi | 3723 | 164, 309 | أنا دار الحكمة وعلي بابها | Da'if | ❌ ledger treats it as «مدينة العلم» |
| Tirmidhi | 3768 | 012, 085 | الحسن والحسين سيدا شباب أهل الجنة | Sahih | ✅ |
| Tirmidhi | 3775 | 010 | حسين مني وأنا من حسين | Hasan | ✅ |
| Tirmidhi | 3786 | 043, 157, 206, 242 | كتاب الله وعترتي أهل بيتي (Jabir) | Sahih (Albani) / Da'if (Zubair) | ✅ (grades differ – say so) |
| Tirmidhi | 3788 | 157, 206, 242, 258 | عترتي أهل بيتي … لن يتفرقا حتى يردا علي الحوض | Sahih (Albani) / Da'if (Zubair) | ✅ PAGE-CHECK → VERIFIED |
| Tirmidhi | 3819 | 073 | Usama: أحب أهلي إلي فاطمة | Da'if / isnad hasan | ⚠ print grade |
| Tirmidhi | 3868 | 073 | Buraydah: أحب النساء … فاطمة ومن الرجال علي | **Munkar** (Albani, Shakir) | ⚠ print grade |
| Tirmidhi | 3872 | 068, 252, 262 | Aisha: أشبه سمتا ودلا | Sahih | ✅ |
| Tirmidhi | 3874 | 073 | Jumay' b. Umayr: Aisha asked who was most beloved | **Munkar** (Albani, Shakir) | ⚠ print grade |
| Ibn Majah | 224 | 009 | طلب العلم فريضة … كمقلد الخنازير الجوهر — **no «China» clause** | **Very da'if** | ⚠ |
| Ibn Majah | 2198 | 005 | Anas: Ansari man, cup, axe | Da'if (Albani) / isnad hasan (Zubair) | ✅ |
| Ibn Majah | 3973 | 004 | Mu'adh: sadaqa extinguishes sin | Sahih | ✅ |

## B. Wordings searched across all six books

| Wording | Ledger attributes to | Result |
|---|---|---|
| الجنة طيبة لا يدخلها إلا الطيب | Sahih Muslim (REF-022) | ∅ absent — PRINT BLOCKED stands |
| مثل أهل بيتي … سفينة نوح | «Musnad Ahmad 3786» (REF-011) | ∅ absent from six books → Hakim / Tabarani |
| أنا مدينة العلم وعلي بابها | Tirmidhi / Hakim (REF-164, 207, 240, 245, 309) | ∅ absent → Hakim / Tabarani / Khatib; Tirmidhi has only «دار الحكمة» |
| مثقال حبة من خردل من كبر | «no source» (REF-087) | ✅ Muslim 91; Abu Dawud 4091; Tirmidhi 1998; Ibn Majah 59, 4173 |
| مقاريض (lips cut, Mi'raj) | Musnad Ahmad (REF-318) | ∅ not in six → Ahmad stands |
| الشرك الأصغر … الرياء | Musnad Ahmad (REF-320) | ∅ not in six → Ahmad stands |
| ولا بزفرة واحدة (mother at tawaf) | «hadith» (REF-171) | ∅ not in six → Kafi 2:162 / Bayhaqi Shu'ab |
| أحصنت فرجها / فطم | Kanz, Tabarani (REF-086, 259) | ∅ not in six → Hakim 4726 / Tabarani / Kanz |
| بخ بخ (Ghadir congratulation) | Musnad Ahmad (REF-237) | ∅ not in six → Ahmad 18479 |
| الصلاة البتراء / لا تصلوا علي | Sunni (REF-303) | ∅ not in six → al-Sawa'iq al-Muhriqa |
| يغضب لغضبك | Hakim 4730 (REF-251) | ∅ not in six (consistent with ledger) |
| أم أبيها | Bihar 43 (REF-069) | ∅ not in six → Isti'ab / Isaba / Bihar |
| ذريتي في صلب علي | Tabarani (REF-103) | ∅ not in six (consistent) |
| خير البرية (98:7 = Ali) | Durr al-Manthur (REF-099) | ∅ — the six-book «يا خير البرية — ذاك إبراهيم» (Muslim 2369) is a **different** hadith |
| مات على حب آل محمد | Kashshaf (REF-098) | ∅ not in six (consistent) |

## C. What this check does NOT cover
Shia collections (al-Kafi, Bihar, 'Ilal, Kamal al-Din, Tafsir al-Qummi/al-Ayyashi, al-Ihtijaj, Sulaym), Sunni works outside the six (al-Hakim, Tabarani, Ahmad, Bayhaqi, Kanz, tafsir works), and all edition page numbers. Those rows keep `PAGE-CHECK` / `CANDIDATE` in ledger v1.2.
