#!/usr/bin/env python3
"""o90_split_by_k.py ROWS SPLIT -> A9.6 (1)'s print: read 1's per-arm FLAG rate split by k (chunk reads vs split reads).
A row is a SPLIT read when its reader session is a session in split.tsv (each split single has its own session, A9.7)."""
import sys, collections
rows = [l.rstrip('\n').split('\t') for l in open(sys.argv[1])]; h = rows[0]; rows = [dict(zip(h, r)) for r in rows[1:]]
ss = {l.split('\t')[2] for l in list(open(sys.argv[2]))[1:]}
c = collections.Counter()
for r in rows:
    k = 'split' if r['reader'] in ss else 'chunk'
    if r['verdict'] in ('OK', 'FALSE'): c[(r['arm'], k, 'scored')] += 1
    if r['verdict'] == 'FALSE': c[(r['arm'], k, 'FALSE')] += 1
    if r['verdict'] not in ('OK', 'FALSE'): c[(r['arm'], k, 'unscored')] += 1
print('A9.6 (1) FLAG RATE split by k, read 1 (gemini): FALSE flags / scored reads [unscored]')
for arm in ('a0', 'a5'):
    for k in ('chunk', 'split'):
        print('  %s %-5s %d / %d  [%d]' % (arm, k, c[(arm, k, 'FALSE')], c[(arm, k, 'scored')], c[(arm, k, 'unscored')]))
print('split sessions in split.tsv: %d · rows matched to one: %d' % (len(ss), sum(1 for r in rows if r['reader'] in ss)))
