#!/usr/bin/env python3
"""Desk KS part 2b (bench, 2026-10-01): T beside RESULT-statement-arm-2026-09-09 §3's per-cell dollars, WITHOUT re-reading the archive.
§3's dollars came from the archive's METER.txt on 09-09. A later reading carries T beside COST
(evidence/v3-cost-tables-2026-09-28/claude-cost-raw.tsv), and the archive can move between readings (desk KS's trap). So a cell's T is
taken from that file ONLY when its COST, rounded to the cent, equals the published dollar figure, uniquely among the st* rows. Equal
cents show the two readings agree on that cell. Any published figure with no unique match prints UNMEASURED. Run from the repo root."""
import csv, re

raw = [r for r in csv.DictReader([l for l in open('evidence/v3-cost-tables-2026-09-28/claude-cost-raw.tsv') if l.strip()], delimiter='\t')
       if r['cell'].startswith('st')]
txt = open('harness/systems-v3/RESULT-statement-arm-2026-09-09.md').read()
sec = txt.split('## §3')[1].split('## §4')[0]
print('problem\tarm\tpublished\tcell\tT\tvoid')
for line in sec.splitlines():
    m = re.match(r'\s+(\w+)\s+(plain|salt-diet)\s+3\s+((?:\$[\d.]+\s+){3})', line)
    if not m:
        continue
    for d in re.findall(r'\$([\d.]+)', m.group(3)):
        hit = [r for r in raw if '%.2f' % float(r['COST']) == d]
        if len(hit) == 1:
            print('%s\t%s\t$%s\t%s\t%s\t%s' % (m.group(1), m.group(2), d, hit[0]['cell'], hit[0]['T'], hit[0]['void'] or '-'))
        else:
            print('%s\t%s\t$%s\t-\tUNMEASURED\t%d tracked rows at this cent' % (m.group(1), m.group(2), d, len(hit)))
