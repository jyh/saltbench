#!/usr/bin/env python3
"""Desk KS part 3 (bench, 2026-10-01): T beside the per-cell dollars of RESULT-HC1-crc32-2026-09-15 and RESULT-HC1-paxos-2026-09-16.
Source: hc1_post_end.tsv (each cell's own ctl/post-end-1.tsv, read by gather_hc1.sh). A published dollar takes a cell's final_T ONLY when
that cell's final_COST, to the cent, equals it uniquely among the problem's cells; otherwise UNMEASURED. Medians are each column's own.
Run from the repo root."""
import csv, re, statistics
cells = list(csv.DictReader([l for l in open('evidence/ks-tokens-2026-10-01/hc1_post_end.tsv') if not l.startswith('#')], delimiter='\t'))
for prob, f in (('crc32', 'harness/systems-v3/RESULT-HC1-crc32-2026-09-15.md'), ('paxos', 'harness/systems-v3/RESULT-HC1-paxos-2026-09-16.md')):
    pool = [c for c in cells if c['root_arm'].startswith(prob + '-') and c['final_COST'] != 'MISSING']
    print('## %s' % prob)
    print('arm\tpublished\tcell\tfinal_COST\tfinal_T')
    for line in open(f):
        m = re.match(r'\s+(plain|placebo|salt-diet)\s+((?:\$[\d.]+\S*\s*·\s*){2}\$[\d.]+\S*)', line)
        if not m:
            continue
        ts = []
        for d in re.findall(r'\$([\d.]+)', m.group(2)):
            hit = [c for c in pool if '%.2f' % float(c['final_COST']) == d]
            if len(hit) == 1:
                ts.append(int(hit[0]['final_T']))
                print('%s\t$%s\t%s\t%s\t%s' % (m.group(1), d, hit[0]['cell'], hit[0]['final_COST'], hit[0]['final_T']))
            else:
                print('%s\t$%s\t-\t-\tUNMEASURED (%d cells at this cent)' % (m.group(1), d, len(hit)))
        if len(ts) == 3:
            print('# %s %s: median T %d (the T column\'s own median)' % (prob, m.group(1), statistics.median(ts)))
