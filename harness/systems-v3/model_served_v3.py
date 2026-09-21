#!/usr/bin/env python3
"""model_served_v3.py <run-dir> [--selftest] — derive the MODEL SERVED, per cell, from each cell's
own `served-<cell>.out` receipt.

⛔⛔ WHY THIS EXISTS. ADDENDUM 12 of CENSUS-full-matrix-2026-09-14.md had to correct a whole block's
  MODEL ATTRIBUTION after the fact: ADDENDUM 11 counted block SB's ten conditions under
  `claude-opus-5` and they are `claude-sonnet-5`. The per-cell table of record has 24 columns and
  NO MODEL COLUMN, so `RESULT-...-verify.py` re-derived every figure it could reach and its green
  was accurate about everything except the one field that was wrong.
  ⇒ 🔑 A VERIFIER CANNOT CONTRADICT A FIELD ITS TABLE DOES NOT CARRY, AND ITS GREEN READS AS
    COVERAGE OF THE WHOLE ROW.
  The result of record for block SB names this column as the durable fix and says it is cheapest to
  land BEFORE the remaining harvested blocks are written up. This is that column.

⛔ IT REFUSES RATHER THAN PICKS (rc 1):
     · a cell whose HEAD served more than one model — an ambiguous attribution is never silently
       collapsed to its first value, which is precisely how a wrong model becomes a clean number
     · a cell whose `launch phase1:` model is not among the models actually SERVED — the launch
       records intent and the head records what answered; a result may not quote one for the other
     · a receipt with no `served head` line at all — an absence is never a smaller n

✅ ARMS (--selftest), each driven against a fixture this file writes, with the mutation VERIFIED to
  have landed before the arm's verdict is read:
     1 control   an unmutated pair                       -> rc 0
     2 mutant    a head serving TWO models               -> rc 1   (the ADDENDUM-12 class)
     3 mutant    `launch` naming a model never served    -> rc 1
     4 mutant    a receipt with the head line removed    -> rc 1
  ⚠️ ARM 2 IS IN THIS SUITE BECAUSE IT FIRST READ GREEN WHILE TESTING NOTHING: the mutation was a
    `sed` carrying a HAND-TYPED token count from a DIFFERENT cell, so it matched no line and the
    fixture was never mutated. A fixture built by not-writing is not a fixture. Every arm below
    asserts its own mutation landed before it reads the tool's exit code."""
import re, sys, os, collections, tempfile, subprocess

def parse(run):
    rows, bad = [], []
    for fn in sorted(os.listdir(run)):
        m = re.match(r'^served-(\w+)\.out$', fn)
        if not m:
            continue
        cell = m.group(1)
        txt = open(os.path.join(run, fn), errors='replace').read()
        head = re.findall(r'^\s*served head\s+(.*)$', txt, re.M)
        models = set()
        if head:
            models = set(re.findall(r'([A-Za-z0-9._-]+)=\d+', head[0]))
        launch = re.findall(r'^\s*launch\s+phase1:([A-Za-z0-9._-]+)', txt, re.M)
        verdict = re.findall(r'set_verdict\s+(\w+)', txt)
        if not models:
            bad.append((cell, 'no `served head` model — an absence, not a smaller n'))
            continue
        rows.append({'cell': cell, 'block': cell[3], 'models': sorted(models),
                     'launch': launch[0] if launch else '-',
                     'verdict': verdict[0] if verdict else '-'})
        if len(models) > 1:
            bad.append((cell, 'head served %d models: %s' % (len(models), sorted(models))))
        elif launch and launch[0] not in models:
            bad.append((cell, 'launch %s not among served %s' % (launch[0], sorted(models))))
    return rows, bad

def report(run):
    rows, bad = parse(run)
    print("cells parsed: %d   (run %s)" % (len(rows), run))
    print()
    print("PER BLOCK (cell-id letter) — the model actually SERVED, from each cell's own receipt")
    agg = collections.defaultdict(collections.Counter)
    vagg = collections.defaultdict(collections.Counter)
    for r in rows:
        agg[r['block']][r['models'][0]] += 1
        vagg[r['block']][r['verdict']] += 1
    for b in sorted(agg):
        served = ' · '.join('%s=%d' % kv for kv in sorted(agg[b].items()))
        verds = ' · '.join('%s=%d' % kv for kv in sorted(vagg[b].items()))
        flag = '' if len(agg[b]) == 1 else '   ⛔ MIXED MODELS IN ONE BLOCK'
        print("  block %s  n=%-3d %-34s verdict %s%s" % (b, sum(agg[b].values()), served, verds, flag))
    print()
    if bad:
        print("⛔ %d AMBIGUOUS OR UNPARSEABLE — this tool refuses rather than picks:" % len(bad))
        for c, w in bad[:40]:
            print("   %s  %s" % (c, w))
        return 1
    print("✅ every cell's head served exactly ONE model, and every launch matches what was served.")
    return 0

RECEIPT = """served_models: clean condition sonnet (table models-sonnet.tsv sha256/16=deadbeefdeadbeef) | set_verdict clean
  transcript  (--slug): 3 file(s), 102 line(s) read, synthetic 0, model-absent 0, unreadable 0
  served head      claude-sonnet-5=59
  served sidechain claude-sonnet-5=30
  launch      phase1:claude-sonnet-5
"""

def selftest():
    fails = []
    with tempfile.TemporaryDirectory() as d:
        def write(cell, txt):
            open(os.path.join(d, 'served-%s.out' % cell), 'w').write(txt)
        def run():
            return subprocess.call([sys.executable, os.path.abspath(__file__), d],
                                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        # ARM 1 — control
        write('clbbcp01', RECEIPT); write('clbbcp02', RECEIPT)
        rc = run()
        print("  arm 1 control (unmutated pair)                rc=%d  %s" % (rc, 'PASS' if rc == 0 else 'FAIL'))
        if rc != 0: fails.append(1)
        # ARM 2 — head serves two models. The mutation is ASSERTED to have landed.
        mutated = re.sub(r'(^\s*served head\s+claude-sonnet-5=\d+)', r'\1 claude-opus-5=11',
                         RECEIPT, count=1, flags=re.M)
        assert mutated != RECEIPT, "arm 2 fixture did not mutate — the arm would test nothing"
        write('clbbcp02', mutated)
        rc = run()
        print("  arm 2 mutant: head serves TWO models          rc=%d  %s" % (rc, 'PASS' if rc == 1 else 'FAIL'))
        if rc != 1: fails.append(2)
        # ARM 3 — launch names a model never served
        mutated = RECEIPT.replace('launch      phase1:claude-sonnet-5', 'launch      phase1:claude-opus-5')
        assert mutated != RECEIPT, "arm 3 fixture did not mutate"
        write('clbbcp02', mutated)
        rc = run()
        print("  arm 3 mutant: launch never served             rc=%d  %s" % (rc, 'PASS' if rc == 1 else 'FAIL'))
        if rc != 1: fails.append(3)
        # ARM 4 — the head line removed entirely
        mutated = '\n'.join(l for l in RECEIPT.splitlines() if 'served head' not in l) + '\n'
        assert mutated != RECEIPT, "arm 4 fixture did not mutate"
        write('clbbcp02', mutated)
        rc = run()
        print("  arm 4 mutant: no `served head` line           rc=%d  %s" % (rc, 'PASS' if rc == 1 else 'FAIL'))
        if rc != 1: fails.append(4)
    print()
    if fails:
        print("⛔ SELFTEST FAILED on arm(s) %s" % fails); return 1
    print("✅ SELFTEST 4/4 — the control is green and EVERY mutant reddens the arm it names.")
    return 0

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '--selftest':
        sys.exit(selftest())
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(2)
    sys.exit(report(sys.argv[1]))
