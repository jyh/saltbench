# Usage: python3 evidence/blockNC-2026-11-13/read_baselines.py evidence/blockNC-2026-11-13/p1-baselines.tsv
# Read the NC baselines table against block N's record (tests column) and ADDENDUM 1's eligibility rule.
import csv, sys, collections, os
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
def rows(p):
    return list(csv.DictReader([l for l in open(p) if not l.startswith('#')], delimiter='\t'))
base0 = rows(sys.argv[1])
rec = {r['cell']: r for f in ('blockNO-cells.tsv', 'blockNS-cells.tsv')
       for r in rows(os.path.join(ROOT, 'evidence/claude-lane-blockN-2026-09-28', f))}
base = [b for b in base0 if b['cell'] in rec]
print('rows', len(base0), 'in record', len(base), 'not in record:', [b['cell'] for b in base0 if b['cell'] not in rec])
assert len(base) == 72, len(base)
elig = collections.Counter(); short = []; mism = []; srcchg = []
for b in base:
    r = rec[b['cell']]
    assert r['problem'] == b['problem'], b
    if b['src_tree_before'] != b['src_tree_after']: srcchg.append(b['cell'])
    ok = b['landed1'] == 'yes' and b['rc'] == '0' and '/' in b['TESTS'] and b['TESTS'].split('/')[0] == b['TESTS'].split('/')[1] and b['TESTS'].split('/')[1] != '0'
    key = (b['model'], b['problem'], b['arm'])
    elig[key] += ok
    # positive control: a landed cell's baseline must equal block N's recorded tests
    if b['landed1'] == 'yes' and r['tests'] != b['TESTS']: mism.append((b['cell'], r['tests'], b['TESTS'], b['rc']))
    if b['landed1'] == 'no' and r['run_state'] == 'ENDED: LANDED': mism.append((b['cell'], 'LANDED-but-no-tag'))
    print('%-6s %-12s %-8s %-9s landed1=%-3s rc=%-2s G %-6s blockN %-6s %s %s' % (b['model'], b['problem'], b['arm'], b['cell'], b['landed1'], b['rc'], b['TESTS'], r['tests'], r['run_state'][7:] if r['run_state'].startswith('ENDED') else r['run_state'], 'ELIGIBLE' if ok else 'not-eligible'))
print()
for k in sorted(elig): 
    if elig[k] < 3: short.append((k, 3 - elig[k]))
print('eligible per model x arm:', {f'{m} {a}': sum(v for (mm, p, aa), v in elig.items() if mm == m and aa == a) for m in ('Opus', 'Sonnet') for a in ('plain', 'saltdiet')})
print('eligible total', sum(elig.values()), 'of 72; shortfalls (fresh phase 1s):', sum(s for _, s in short))
for k, s in short: print('  SHORTFALL', k, s)
print('mismatches vs block N record:', mism or 'none')
print('sources changed:', srcchg or 'none')
