# INPUT MANIFEST — Book 1 Source Harvest — 2026-10-05

## Result: **PASS**

| Field | Expected | Observed | Status |
|---|---|---|---|
| Repo | mdjonyrd/tahara1 | mdjonyrd/tahara1 | PASS |
| Branch tip (min) | `63b418aaa5d21fb57366789c0b7e406194c17a7c` | see `git rev-parse HEAD` | PASS |
| Canonical DOCX | `book1/source/B1_P01-11_reader.docx` | present | PASS |
| SHA256 | `337c70ea468a587ab248f5eb49ffacc0c167cfd421a76d145c02dbc8c0595ecc` | `337c70ea468a587ab248f5eb49ffacc0c167cfd421a76d145c02dbc8c0595ecc` | PASS |
| Size (bytes) | 825302 | 825302 | PASS |
| python-docx ¶ | 10856 | 10856 | PASS |
| w:p total | 10944 | 10944 | PASS |
| w:p nonempty | 10830 | 10830 | PASS |

## Locks acknowledged

- MANUSCRIPT_WRITE=FALSE
- PRINT BLOCKED stays
- Ledger = inherited anchors only
- SOURCE_EXISTENCE ≠ CLAIM_SUPPORT
- Sunni/Shia separate; Umm Ayman ≠ Aus counter-testimony
- No invented page numbers; NOT FOUND ≠ DOES NOT EXIST
- No Windows paths in publication-facing source records

## Note on nonempty counts

`python-docx` body paragraphs nonempty (10742) excludes nested table `w:p` nodes. The locked expected nonempty count **10830** is the document.xml `w:p` nonempty total.
