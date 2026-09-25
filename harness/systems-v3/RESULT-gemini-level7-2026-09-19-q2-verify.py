"""Re-derive ADDENDUM A of RESULT-gemini-level7-2026-09-19 from the two §Q2 rows and the published l7cfss01 row, and compare with the
document's bytes (whitespace collapsed). Nothing is typed from the prose."""
import csv, sys
D = 'harness/systems-v3/RESULT-gemini-level7-2026-09-19.md'
FLAT = ' '.join(open(D).read().split())
q2 = list(csv.DictReader(open('harness/systems-v3/RESULT-gemini-level7-2026-09-19-q2-cells.tsv'), delimiter='\t'))
pub = [r for r in csv.DictReader(open('harness/systems-v3/RESULT-gemini-level7-2026-09-19-cells.tsv'), delimiter='\t') if r['cell'] == 'l7cfss01']
assert len(q2) == 2 and len(pub) == 1
fails = []
def check(name, needle):
    ok = ' '.join(needle.split()) in FLAT
    print(('  OK  ' if ok else '  RED ') + name)
    if not ok: fails.append(name)
roots = {'l7cfss01': 'cells-l7-crc32-flash-salt-stmt-bf'}
for r in pub + q2:
    root = roots.get(r['cell'], r['cond'])
    check('row ' + r['cell'], '%s %s %s %s %s %s %s %s %s %s %s' % (r['cell'], root, '{:,}'.format(int(r['T'])), r['wall_s'], r['verdicts'],
          r['tests'], r['retained'], r['ret_class'], r['given'], r['w1_fenced'], r['tokenscan']))
cells = pub + q2
assert all(r['given'] == 'GIVEN-OK' and r['w1_fenced'] == 'COVERED' and r['tokenscan'] == 'CLEAN' and r['n_leak'] == '0' for r in cells), 'a validity column fails'
landed = sum(r['done_reason'] == 'LANDED' for r in cells); full = sum(r['verdicts'] == 'PASS' for r in cells)
check('headline', '%d of %d LANDED · %d of %d FULL PASS' % (landed, len(cells), full, len(cells)))
low = [r for r in cells if float(r['retained']) < 0.20]
assert all(r['ret_class'] == 'REPLACED' for r in low) and all(r['ret_class'] != 'REPLACED' for r in cells if r not in low)
for r in low:
    check('replaced ' + r['cell'], '`%s` reads `retained` %s, below' % (r['cell'], r['retained']))
print('VERIFY %s — %d red' % ('GREEN' if not fails else 'RED', len(fails)))
sys.exit(1 if fails else 0)
