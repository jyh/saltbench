#!/usr/bin/env python3
# t-sections.py <tasks-root> <out-dir> — each problem's statement section = the ```rust block under the card's `## Statement` heading,
# from the release export's own card.md (block T ADDENDUM 1: cmp-EQUAL to extract_statement_v3.py --check --carry-consts output).
import sys, re, os
root, out = sys.argv[1], sys.argv[2]; os.makedirs(out, exist_ok=True)
for p in ['Luby', 'AES', 'Liveness', 'MaxFlow', 'BinomialHeap', 'LinearScan']:
    t = open(f'{root}/{p}/card.md').read()
    i = t.index('\n## Statement'); m = re.search(r'```rust\n(.*?)```', t[i:], re.S)
    open(f'{out}/{p.lower()}-section.rs', 'w').write(m.group(1))
    print(p, len(m.group(1).encode()), 'bytes')
