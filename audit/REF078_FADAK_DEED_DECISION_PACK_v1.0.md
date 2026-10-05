# REF-078 — Fadak Deed Authorship Decision Pack v1.0

**Date:** 2026-10-05
**Tip baseline:** `cce7fcc597131856b5d8606fdcbe50de809fe066`
**DOCX:** `book1/source/B1_P01-11_reader.docx`
**SHA256:** `337c70ea468a587ab248f5eb49ffacc0c167cfd421a76d145c02dbc8c0595ecc`
**Locks:** MANUSCRIPT_WRITE=FALSE · PRINT BLOCKED · NO auto author decision · NO silent reconcile

## Status

| Item | Value |
|---|---|
| Conflict | **OPEN** |
| Harvest marker | `REF-078-DEED-AUTHORSHIP` / Fadak control `REF078_Conflict_Open=YES` |
| Claim_ID | B1-C00217 (¶2790) + related deed dialogue paras |
| Author_Decision | *(blank — AUTHOR DECISION REQUIRED)* |
| Print_Safe | **NO** |

## Exact manuscript wording (live DOCX)

### Ledger / harvest claim (REF-078 → B1-C00217, ¶2790)

> ভাঙা কাপটা তিনি নিজের হাতে রাখলেন। এক চুমুক দিলেন। তারপর বললেন, "এক নম্বর কথা। রাসূলুল্লাহ ﷺ নিজে মেয়েকে ফাদাক দিয়ে গেছেন। বর্ণিত আছে, লিখেও দিয়ে গেছেন। যাঁর কথা কুরআনের পরেই চূড়ান্ত, তাঁর দেওয়া জিনিসের জন্য আবার সাক্ষী লাগবে? এটা মেয়ের জন্য অপমান না?"

**Live DOCX ¶2790:**

> ভাঙা কাপটা তিনি নিজের হাতে রাখলেন। এক চুমুক দিলেন। তারপর বললেন, "এক নম্বর কথা। রাসূলুল্লাহ ﷺ নিজে মেয়েকে ফাদাক দিয়ে গেছেন। বর্ণিত আছে, লিখেও দিয়ে গেছেন। যাঁর কথা কুরআনের পরেই চূড়ান্ত, তাঁর দেওয়া জিনিসের জন্য আবার সাক্ষী লাগবে? এটা মেয়ের জন্য অপমান না?"

### Other live DOCX deed-writing loci (not silent-merged)

- **¶5239:** বইয়ের পাতায় লেখা ছিল—প্রথম জন শুরুতে মা সাইয়্যিদা ফাতিমাতুয্ যাহরা (আলাইহাস্ সালাম)-এর দাবিকে স্বীকার করে একটি লিখিত দলিল প্রদান করেছিলেন, কিন্তু দ্বিতীয় জন সেই দলিলটি ছিঁড়ে ফেলেন।
- **¶5577:** রাকিকা: (কৌতূহলী চোখে) কিন্তু চাচা, ৭ হিজরীতে যখন এই জমিটি রাসূলুল্লাহ ﷺ-এর মালিকানায় আসে, তিনি তো দলিল করে নিজ হাতে লিখে এবং সাক্ষর করে মা সাইয়্যিদা ফাতিমাতুয্ যাহরা (আলাইহাস্ সালাম)-কে দিয়ে দেন! তাহলে ওরা কীভাবে সেটা অস্বীকার করল?
- **¶5580:** খিজির: (গভীর কণ্ঠে, দৃঢ় স্বরে) অবশ্যই! তিনি জানতেন। তিনি জানতেন যে সত্যের আলো নেভানোর জন্য মুনাফিকরা একের পর এক ষড়যন্ত্র করবে। তাই তিনি দলিল লিখে, সাক্ষর করে ও উম্মাহর সামনে প্রকাশ্যে ঘোষণা দিয়ে ফাদাককে মা সাইয়্যিদা ফাতিমাতুয্ যাহরা (আলাইহাস্ সালাম)-এর হাতে তুলে দিয়েছিলেন—যাতে সত্যের কোনো বিকৃতি না ঘটে।

## Opposing source line (do not reconcile)

| Side | Attribution | Content | Status |
|---|---|---|---|
| Manuscript dialogue | authorial / «বর্ণিত আছে» | Prophet wrote / signed the Fadak deed for Fatima | CONFLICT OPEN |
| al-Ihtijaj (Shia) | al-Tabarsi, *al-Ihtijaj* vol. 1 | Abu Bakr writes the deed; Umar tears it | S-181 URL-backed; **EDITION LOCK PENDING** (pp.90–92 vs Khurasan 119–127/~129) |
| Baladhuri (Sunni) | *Futuh al-Buldan* | Deed episode **absent** — do not insert Ihtijaj deed into Baladhuri | KEEP SEPARATE |

## Hard rules

1. Do **not** auto-pick Prophet-writer or Abu Bakr-writer.
2. Do **not** merge Sunni Baladhuri testimony chain with Shia Ihtijaj deed chain.
3. SOURCE_EXISTENCE (Ihtijaj exists) ≠ CLAIM_SUPPORT for the manuscript’s Prophet-writer dialogue.
4. Umm Ayman testimony ≠ Aus ibn al-Hadathan counter-testimony (separate control).
5. Leave PRINT BLOCKED until author decision + edition lock + final citation audit.

## Decision options for author (Jony) — not filled by agent

| Option | Description |
|---|---|
| A | Keep dialogue as-is with explicit «বর্ণিত আছে» / conflict note; cite Ihtijaj only as alternate recension |
| B | Reword dialogue so deed-writer matches locked Ihtijaj (Abu Bakr writes; Umar tears) — **requires manuscript patch later** |
| C | Split voices: dialogue = narrative; source block = Ihtijaj wording only |
| D | Other (author specifies) |

**AUTHOR_DECISION:** 

## Fadak control rows with REF078 open

| Fadak_Claim_ID | Work | Claim | Status | Notes |
|---|---|---|---|---|
| C01-H01 | al-Ihtijaj, vol. 1 | 1 · Fatima's claim to Fadak (as inheritance / as g | VERIFIED | Evidence = URL cited in sources/S-181 (research layer); URL not re-opened here (network policy). URLs: https://www.almer |
| C04-H01 | al-Ihtijaj, vol. 1 | 4 · Umm Ayman's testimony for Fatima | VERIFIED | S-181 elides the speaker before «أم أيمن امرأة من أهل الجنة» («فقال …») - do not render it as direct «রাসূল ﷺ বলেছেন» wi |
| C08-H01 | al-Ihtijaj, vol. 1 | 8 · Written-document (deed) episode | VERIFIED | Evidence = URL cited in sources/S-181 (research layer); URL not re-opened here (network policy). URLs: https://www.almer |
| C08-X01 | (none located) - manuscript dialogue REF-078, mapped by ledg | 8 · Written-document (deed) episode | PAGE-CHECK | SUBJECT MISMATCH: al-Ihtijaj (C08-H01) has Abu Bakr as writer, not the Prophet. Ledger Resolution_Note equates the two - |
| C08-S01 | Futuh al-Buldan (both recensions) | 8 · Written-document (deed) episode | VERIFIED | Absence row - the deed belongs to the al-Ihtijaj recension only; never insert it into Baladhuri. |
| C09-H01 | al-Ihtijaj, vol. 1 | 9 · Umar's intervention | VERIFIED | S-181 gives the tearing only in Bengali («উমর এসে দলিল নিয়ে যান/ছিঁড়ে ফেলেন») - exact Arabic of the tearing sentence P |
| C09-S04 | Sahih al-Bukhari, Kitab al-Maghazi | 9 · Umar's intervention | VERIFIED | This is the only Umar intervention in 4240 - it is about the reconciliation visit, NOT the Fadak deed. Text checked 2026 |
| REF-078-DEED-AUTHORSHIP | al-Ihtijaj | Fadak deed dialogue — who wrote the deed (Prophet  | CONFLICT | OPEN HUMAN DECISION: manuscript dialogue says Prophet wrote deed; al-Ihtijaj has Abu Bakr writing. Do not silently recon |

---
*Phase A artifact. No manuscript rewrite. No PRINT ALLOWED.*