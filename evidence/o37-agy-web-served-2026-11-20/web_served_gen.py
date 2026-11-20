#!/usr/bin/env python3
"""web_served_gen.py — print the README's tables from this directory's join.tsv and census.tsv (never typed).

  python3 web_served_gen.py            print the tables
  python3 web_served_gen.py --check    exit 1 unless every printed line is present, verbatim, in README.md
"""
import collections, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
out = []
rows = [l.rstrip("\n").split("\t") for l in open(os.path.join(HERE, "join.tsv")) if l.strip() and not l.startswith("#")]
order = ["MATRIX", "NA", "ZF", "WA", "WA-pro", "TA"]
tab = collections.defaultdict(collections.Counter)
for r in rows:
    tab[r[0]][r[10]] += 1
out.append("  block    cells of record   WEB-SERVED   CLEAN   UNMEASURED")
for b in order:
    t = tab[b]
    out.append(f"  {b:<8} {sum(t.values()):>15}   {t['WEB-SERVED']:>10}   {t['CLEAN']:>5}   {t['UNMEASURED']:>10}")
tot = collections.Counter()
for b in order:
    tot.update(tab[b])
out.append(f"  {'all':<8} {sum(tot.values()):>15}   {tot['WEB-SERVED']:>10}   {tot['CLEAN']:>5}   {tot['UNMEASURED']:>10}")
out.append("")
out.append("  block    cell           model                   arm         search results served   network calls denied")
served_total = 0
for r in rows:
    if r[10] == "WEB-SERVED":
        served_total += int(r[8])
        out.append(f"  {r[0]:<8} {r[1]:<14} {r[2]:<23} {r[3]:<11} {r[8]:>22}   {r[9]:>20}")
out.append(f"  served over the cells of record: {served_total}")
pop = [l for l in open(os.path.join(HERE, "census.tsv")) if l.startswith("#POPULATION")][0].strip()
out.append("  " + pop)
text = "\n".join(out)
if "--check" in sys.argv:
    readme = open(os.path.join(HERE, "README.md")).read()
    missing = [l for l in out if l.strip() and l not in readme]
    for l in missing:
        print("MISSING:", l)
    print(f"web_served_gen --check: {len([l for l in out if l.strip()])} line(s), {len(missing)} missing")
    sys.exit(1 if missing else 0)
print(text)
