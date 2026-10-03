#!/usr/bin/env python3
"""Verify numbered Sunni hadith references against the six canonical collections.

Data source: fawazahmed0/hadith-api (GitHub), Arabic editions, sparse-cloned into
tools/_hadith-api/ (git-ignored). Numbering: Bukhari / Abu Dawud / Tirmidhi /
Ibn Majah / Nasa'i follow the standard (sunnah.com) numbering; Muslim is matched
on `arabicnumber` (Abd al-Baqi numbering, e.g. 2408.01).

usage:
  python3 tools/verify_sunni.py fetch                 # sparse clone the JSON editions
  python3 tools/verify_sunni.py show bukhari 4240     # print one hadith (+grades)
  python3 tools/verify_sunni.py search "مدينة العلم"  # substring search, all six books
  python3 tools/verify_sunni.py batch                 # run the ledger's full check list

Why this exists: sunnah.com, dorar.net and jsDelivr are blocked by the cloud
environment's egress policy; GitHub is not. Results feed
audit/verification/sunni_six_books_check_<date>.md.
"""
import json, sys, re, subprocess
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parent
DATA = ROOT / "_hadith-api" / "editions"
EDS = ["bukhari","muslim","abudawud","tirmidhi","ibnmajah","nasai"]

def fetch():
    tgt = ROOT / "_hadith-api"
    if not tgt.exists():
        subprocess.run(["git","clone","--quiet","--depth","1","--filter=blob:none","--sparse",
                        "https://github.com/fawazahmed0/hadith-api.git", str(tgt)], check=True)
    subprocess.run(["git","-C",str(tgt),"sparse-checkout","set","--no-cone"]+[f"/editions/ara-{e}.json" for e in EDS], check=True)
    print("fetched:", sorted(p.name for p in DATA.glob("*.json")))

B = {}
def load():
    if B: return
    for ed in EDS:
        f = DATA / f"ara-{ed}.json"
        if not f.exists():
            sys.exit("editions missing - run: python3 tools/verify_sunni.py fetch")
        j = json.load(open(f, encoding="utf-8"))
        B[ed] = (j["hadiths"], j["metadata"].get("sections", {}))
def norm(s): return re.sub(r'[ً-ْٰـ]','',s)
def find(ed,n):
    """Match by the collection's standard number.

    Muslim: the corpus stores Abd al-Baqi numbers as arabicnumber with a sub-report
    suffix (e.g. 1759.01, 1759.02, or 2424 when single). Match on the integer part
    so `show muslim 1759` returns every sub-report of 1759 — never fall back to the
    corpus' sequential hadithnumber, which is a different numbering.
    Other books: standard number == hadithnumber == arabicnumber."""
    load(); hs,_=B[ed]
    n=str(n).strip()
    def intpart(x):
        x=str(x)
        return x.split(".")[0] if x not in ("None","") else ""
    out=[h for h in hs if intpart(h.get("arabicnumber"))==n]
    if out: return out
    if ed=="muslim":
        return []   # no silent fallback for Muslim
    return [h for h in hs if str(h.get("hadithnumber"))==n]
def show(ed,n,w=230):
    hs=find(ed,n)
    if not hs: print(f"-- {ed} {n}: NOT FOUND"); return
    for h in hs[:4]:
        sec=B[ed][1].get(str(h["reference"]["book"]),"")
        g=";".join(f'{x["name"]}:{x["grade"]}' for x in h.get("grades",[]))
        print(f"-- {ed} {n} (num {h['hadithnumber']}/ar {h.get('arabicnumber')}) [{sec[:40]}] {g}\n   {norm(h['text'])[:w]}")
def search(term,eds=None,w=200,limit=6):
    load(); print(f"\n#### search «{term}»")
    c=0
    for ed in (eds or B):
        for h in B[ed][0]:
            if term in norm(h["text"]):
                print(f"-- {ed} ar{h.get('arabicnumber')}: {norm(h['text'])[:w]}"); c+=1
                if c>=limit: return
    if c==0: print("   (none)")

BATCH = {"bukhari":[7171,784,4966,1954,4240,956,957,936,1129,2010,1385,3705,3714,3624,3706,3110,1350,7222,528,6463,7083,3267,1,631,530,786,4474,3752,3636,110,6993,3093,6726,114,4431,2035,3101,5230],
   "muslim":[91,2175,761,2404,1851,1759,2424,2450,1821,2408,395,705,667,2818,2581,2888,1905,2989,1907,8,2266,1637,1015,863,2449],
   "abudawud":[5021,5019,5023,5217,4213,2968,2972,3652,4784,4782,4646],
   "tirmidhi":[3775,3713,3768,3786,3788,3872,3874,3868,3819,614,2616,3206,3723,3871,3205,3787,3540,2951,2952,3714,4,2226,1621,3462],
   "ibnmajah":[2198,224,3973]}
TERMS = ["الجنة طيبة","سفينة نوح","مدينة العلم","خردل من كبر","مقاريض","الشرك الأصغر","بزفرة","أحصنت فرجها","بخ بخ","البتراء","مفتاح الجنة الصلاة","دار الحكمة","يغضب لغضبك","أم أبيها","ذريتي في صلب","خير البرية","مات على حب","مبلغ الدم","اثنا عشر خليفة","يؤذيني ما آذاها"]

if __name__ == "__main__":
    a = sys.argv[1:]
    if not a or a[0] == "batch":
        for ed, ns in BATCH.items():
            print(f"\n######## {ed.upper()}")
            for n in ns: show(ed, n)
        for t in TERMS: search(t)
    elif a[0] == "fetch": fetch()
    elif a[0] == "show": show(a[1], a[2])
    elif a[0] == "search": search(a[1])
