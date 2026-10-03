#!/usr/bin/env python3
"""Print status counts for a ledger CSV (v1.0 or v1.1).

usage: python3 tools/ledger_stats.py audit/<ledger>.csv
Counts both the raw Status strings and the normalized marker classes used in the
audit MD (PAGE-CHECK, বর্ণিত আছে, সূত্র নেই, PRINT BLOCKED, NOT VERIFIED, CONFLICT,
VERIFIED/CONFIRMED). For v1.1 files the Status_v1_1 column is used.
"""
import csv
import sys
from collections import Counter
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

MARKERS = [
    "PAGE-CHECK", "বর্ণিত আছে", "সূত্র নেই", "মেলানো বাকি", "PRINT BLOCKED",
    "NOT VERIFIED", "CONFLICT", "EDITION-LOCK PENDING", "VERIFIED", "CORRECTED", "ATTRIBUTED",
]


def main(path: str) -> int:
    with Path(path).open(encoding="utf-8-sig", newline="") as fh:
        rows = list(csv.DictReader(fh))
    col = "Status_v1_1" if rows and "Status_v1_1" in rows[0] else "Status"
    raw = Counter(r[col] for r in rows)
    marks = Counter()
    for r in rows:
        for m in MARKERS:
            if m in r[col]:
                marks[m] += 1
    resolved = sum(1 for r in rows if col == "Status_v1_1" and r["Resolution_Ref"])
    print(f"file     : {path}")
    print(f"rows     : {len(rows)}")
    print(f"column   : {col}")
    print(f"resolved : {resolved}")
    print("\nmarker classes:")
    for m in MARKERS:
        if marks[m]:
            print(f"  {marks[m]:4d}  {m}")
    print("\ntop raw statuses:")
    for s, n in raw.most_common(8):
        print(f"  {n:4d}  {s}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1] if len(sys.argv) > 1 else "audit/B1_P01-11_UNIDENTIFIED_REFERENCES_AUDIT_v1.1.csv"))
