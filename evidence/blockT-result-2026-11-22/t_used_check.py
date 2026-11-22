#!/usr/bin/env python3
# t_used_check.py — a MECHANICAL cross-check of the salt-diet categories (categories.tsv, a reading) against cells.tsv: does the subject's
# latest CLEAN Verus run (0 errors, by record timestamp) come at or after solution.rs's last write? USED expects yes; USED (unverified)
# expects no; USED (partial) is verified but weaker than the card (a stub's ensures, a weaker clause), so it may read either way.
import csv, os, sys
H = os.path.dirname(os.path.abspath(__file__))
cats = {r['cell']: r['category'] for r in csv.DictReader(open(f'{H}/categories.tsv'), delimiter='\t')}
bad = 0; n = 0
for r in csv.DictReader(open(f'{H}/cells.tsv'), delimiter='\t'):
    if r['arm'] != 'salt-diet': continue
    n += 1; lc = r['verus_last_clean']; t = lc.split('|')[0] if lc != '-' else '-'
    after = t != '-' and t[:19] >= r['sol_mtime'][:19]; c = cats[r['cell']]
    ok = (c == 'USED' and after) or (c == 'USED (unverified)' and not after) or c == 'USED (partial)'
    bad += not ok
    print(r['cell'], r['problem'], c, 'clean-run-after-last-write' if after else 'NO-clean-run-after-last-write', 'ok' if ok else 'CONFLICT', sep='\t')
print(f'salt-diet cells {n} · conflicts {bad}')
sys.exit(1 if bad else 0)
