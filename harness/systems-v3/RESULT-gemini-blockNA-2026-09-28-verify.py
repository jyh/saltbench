"""Verify block NA's per-cell table of record (RESULT-gemini-blockNA-2026-09-28-cells.tsv) against its sources, by a SECOND path.

  1  REGENERATE   the generator run now must reproduce the tracked TSV byte for byte (a hand edit or a stale input fails).
  2  RECEIPTS     each cell's verdict and TESTS are re-read from its score receipt by a plain line match written HERE, not the
                  generator's parser (needs ~/.fleet/executors/gemini.runs; reported SKIPPED, never PASS, where it is absent).
  3  TREES        every cell's task_tree is re-derived from tree_hashes.tsv by (export, problem), and a DIFFERENT tree must be
                  LinearScan on 8ed8cb3 (NA ADDENDUM 5), never anything else.
  4  CONDITIONS   per (served, cond): fired = in-n cells; the in-n count never exceeds 3 (§NA0 row 2); an outside-n cell enters
                  no count but its own.

  python3 RESULT-gemini-blockNA-2026-09-28-verify.py            -> rc 0 only if every check holds
  python3 RESULT-gemini-blockNA-2026-09-28-verify.py --selftest -> mutants that MUST go red, and an x86 window planted over a known
                                                                   cell that MUST be detected (the column's zero is otherwise untested)
"""
import csv, importlib.util, io, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
TSV = os.path.join(HERE, 'RESULT-gemini-blockNA-2026-09-28-cells.tsv')
RUNS = os.path.expanduser('~/.fleet/executors/gemini.runs')

spec = importlib.util.spec_from_file_location('gen', os.path.join(HERE, 'RESULT-gemini-blockNA-cells-gen.py'))
gen = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gen)


def read(text):
    return list(csv.DictReader(io.StringIO(text), delimiter='\t'))


def check(rows, text_now=None, text_tracked=None):
    bad = []
    if text_now is not None and text_now != text_tracked:
        bad.append('REGENERATE: the generator no longer reproduces the tracked TSV')
    trees = {(r['export_sha'][:12], r['problem']): r for r in gen.tsv(os.path.join(gen.EV, 'tree_hashes.tsv'))}
    receipts_read = 0
    for r in rows:
        t = trees.get((r['export_sha'], r['problem']))
        if not t or t['tree'] != r['task_tree'] or t['same'] != r['tree_vs_e54f35a']:
            bad.append('TREES: %s tree %s does not match tree_hashes.tsv' % (r['id'], r['task_tree']))
        if r['tree_vs_e54f35a'] != 'SAME' and not (r['problem'] == 'LinearScan' and r['export_sha'].startswith('8ed8cb3')):
            bad.append('TREES: %s runs a task tree that differs from e54f35a outside NA ADDENDUM 5' % r['id'])
        rp = os.path.join(RUNS, r['score_receipt'])
        if os.path.exists(rp):
            receipts_read += 1
            lines = [l for l in open(rp, errors='replace') if l.startswith(r['id'] + ' ')]
            final = [l for l in lines if re.search(r'\s(PASS|FAIL|NOT-LANDED|NOT-SCORED)\s', l)]
            if len(final) != 1 or (' %s ' % r['verdict']) not in final[0]:
                bad.append('RECEIPTS: %s verdict %s is not its receipt line' % (r['id'], r['verdict']))
            elif r['TESTS'] != '-' and ('TESTS %s' % r['TESTS']) not in final[0]:
                bad.append('RECEIPTS: %s TESTS %s is not its receipt line' % (r['id'], r['TESTS']))
    counts = {}
    for r in rows:
        if r['in_registered_n'] == 'yes':
            counts[(r['served'], r['cond'])] = counts.get((r['served'], r['cond']), 0) + 1
    for k, v in counts.items():
        if v > 3:
            bad.append('CONDITIONS: %s has %d cells in the registered n (§NA0 row 2 says 3)' % (k, v))
    return bad, receipts_read


def selftest():
    rows = read(open(TSV).read())
    arms = []
    m = [dict(r) for r in rows]
    i = next(k for k, r in enumerate(m) if r['verdict'] == 'PASS' and os.path.exists(os.path.join(RUNS, r['score_receipt'])))
    m[i]['verdict'] = 'FAIL'
    arms.append(('a PASS flipped to FAIL is caught at its receipt', bool(check(m)[0])))
    m = [dict(r) for r in rows]
    j = next(k for k, r in enumerate(m) if r['in_registered_n'] == 'no')
    m[j]['in_registered_n'] = 'yes'
    arms.append(('an outside-n cell admitted into the n is caught', any('CONDITIONS' in b for b in check(m)[0])))
    m = [dict(r) for r in rows]
    k = next(k for k, r in enumerate(m) if r['problem'] == 'AES')
    m[k]['tree_vs_e54f35a'] = 'DIFFERENT'
    arms.append(('a DIFFERENT tree outside ADDENDUM 5 is caught', any('TREES' in b for b in check(m)[0])))
    arms.append(('the unmutated table is GREEN', not check(rows)[0]))
    c = next(r for r in gen.cells() if r['end1'] != 'UNREAD')
    facts = {f['id']: f for f in __import__('json').load(open(os.path.join(gen.EV, 'cell_facts.json')))}
    s, e = facts[c['id']]['built_at'], c['end1'].split()[0]
    arms.append(('an x86 window planted inside a known cell IS detected',
                 gen.overlaps(s, e, [dict(wave='PLANT', start=s, end=e)]) == 'PLANT'))
    arms.append(('a window that ends before the cell starts is NOT detected',
                 gen.overlaps(s, e, [dict(wave='PLANT', start='2000-01-01T00:00:00Z', end=s)]) == 'none'))
    for name, ok in arms:
        print('%s  %s' % ('ok  ' if ok else 'FAIL', name))
    print('selftest: %d/%d' % (sum(ok for _, ok in arms), len(arms)))
    return all(ok for _, ok in arms)


if __name__ == '__main__':
    if '--selftest' in sys.argv:
        sys.exit(0 if selftest() else 1)
    tracked = open(TSV).read()
    buf = io.StringIO()
    old, sys.stdout = sys.stdout, buf
    gen.write(gen.cells(), gen.COLS)
    sys.stdout = old
    bad, n = check(read(tracked), buf.getvalue(), tracked)
    rows = read(tracked)
    print('verify: %d cells · receipts re-read %s · %d problem(s)' % (len(rows), n if n else 'SKIPPED (no runs dir)', len(bad)))
    for b in bad:
        print('  ' + b)
    sys.exit(1 if bad else 0)
