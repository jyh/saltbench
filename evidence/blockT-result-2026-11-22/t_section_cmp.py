#!/usr/bin/env python3
# t_section_cmp.py <cells-dir> <sections-dir> — §T7's VOID row: each cell's card AS BUILT (REQUIREMENTS.md at the repo's root commit)
# must carry, under `## Statement`, a rust block byte-equal to the section t-sections.py takes from the export's card.
import subprocess, re, os, sys, csv
cells, secd = sys.argv[1], sys.argv[2]; H = os.path.dirname(os.path.abspath(__file__))
bad = 0; n = 0
for r in csv.DictReader(open(f'{H}/cells.tsv'), delimiter='\t'):
    g = f"{cells}/{r['cell']}/repo"
    root = subprocess.run(['git', '-C', g, 'rev-list', '--max-parents=0', 'HEAD'], capture_output=True, text=True).stdout.split()
    t = subprocess.run(['git', '-C', g, 'show', f'{root[-1]}:REQUIREMENTS.md'], capture_output=True, text=True).stdout
    i = t.find('\n## Statement'); m = re.search(r'```rust\n(.*?)```', t[i:], re.S) if i >= 0 else None
    want = open(f"{secd}/{r['problem'].lower()}-section.rs").read()
    ok = bool(m) and m.group(1) == want; n += 1; bad += not ok
    print(r['cell'], r['problem'], root[-1][:12] if root else '-', 'EQUAL' if ok else 'DIFFERENT-OR-ABSENT', sep='\t')
print(f'cells {n} · section equal to the export card {n - bad} · VOID by §T7 {bad}')
sys.exit(1 if bad else 0)
