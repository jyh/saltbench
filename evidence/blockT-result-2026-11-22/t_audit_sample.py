#!/usr/bin/env python3
"""Draw the sample for a non-author audit of block T's statement categories.

The categories in categories.tsv are READINGS made by the lead. This script picks the cells a reader
who is not the lead re-reads against each cell's code, by the rules in §5 of the two RESULTs.

The draw is deterministic and nothing in it is typed by hand:
  * the strata are model block x arm, read from cells.tsv (columns model_block, arm);
  * every cell whose end1_kind is not LANDED (CAP-COST, DIALOG) is always in the sample;
  * every category value present in categories.tsv is covered at least once;
  * each stratum is then filled to PER_STRATUM cells;
  * ties are broken by sha256(seed + cell id), where the seed is the git blob id of categories.tsv,
    computed from the file's own bytes.
The sample can therefore exceed 4 x PER_STRATUM: forced cells are never dropped to hit a count.

usage: t_audit_sample.py [--per-stratum N] [--check SAMPLE.tsv]
  prints the sample as TSV (cell, model_block, arm, problem, end1_kind, category, why).
  --check: exit 1 unless SAMPLE.tsv equals the fresh draw byte for byte.
"""
import csv
import hashlib
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def blob_id(path):
    data = open(path, 'rb').read()
    return hashlib.sha1(b'blob %d\0' % len(data) + data).hexdigest()


def read_tsv(path):
    with open(path, newline='') as f:
        return list(csv.DictReader(f, delimiter='\t'))


def draw(per_stratum):
    cats_path = os.path.join(HERE, 'categories.tsv')
    cells = read_tsv(os.path.join(HERE, 'cells.tsv'))
    cats = {r['cell']: r['category'] for r in read_tsv(cats_path)}
    ids = [c['cell'] for c in cells]
    if len(ids) != len(set(ids)) or set(ids) != set(cats):
        sys.exit('refuse: cells.tsv and categories.tsv do not name the same unique cells')
    seed = blob_id(cats_path)
    key = lambda cid: hashlib.sha256((seed + cid).encode()).hexdigest()
    by_id = {c['cell']: c for c in cells}
    stratum = lambda cid: (by_id[cid]['model_block'], by_id[cid]['arm'])
    strata = sorted({stratum(c) for c in ids})

    why = {}
    for cid in sorted(ids, key=key):
        if by_id[cid]['end1_kind'] != 'LANDED':
            why[cid] = 'end1=' + by_id[cid]['end1_kind']
    count = lambda s: sum(1 for c in why if stratum(c) == s)
    for cat in sorted(set(cats.values())):
        if any(cats[c] == cat for c in why):
            continue
        pool = sorted((c for c in ids if cats[c] == cat), key=lambda c: (count(stratum(c)), key(c)))
        why[pool[0]] = 'covers category'
    for s in strata:
        for cid in sorted((c for c in ids if stratum(c) == s and c not in why), key=key):
            if count(s) >= per_stratum:
                break
            why[cid] = 'fill'
    rows = []
    for cid in sorted(why, key=lambda c: (stratum(c), by_id[c]['problem'], c)):
        c = by_id[cid]
        rows.append([cid, c['model_block'], c['arm'], c['problem'], c['end1_kind'], cats[cid], why[cid]])
    return seed, rows


def render(seed, rows):
    out = ['# seed (blob of categories.tsv): ' + seed,
           '\t'.join(['cell', 'model_block', 'arm', 'problem', 'end1_kind', 'category', 'why'])]
    out += ['\t'.join(r) for r in rows]
    return '\n'.join(out) + '\n'


def main(argv):
    per, check = 3, None
    i = 0
    while i < len(argv):
        if argv[i] == '--per-stratum':
            per = int(argv[i + 1]); i += 2
        elif argv[i] == '--check':
            check = argv[i + 1]; i += 2
        else:
            sys.exit(__doc__)
    text = render(*draw(per))
    if check:
        ok = open(check).read() == text
        print('t_audit_sample --check: ' + ('EQUAL' if ok else 'DIFFERENT'))
        return 0 if ok else 1
    sys.stdout.write(text)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
