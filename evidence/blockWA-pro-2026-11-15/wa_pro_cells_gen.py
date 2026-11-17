"""Block WA (Pro half, gemini-4-argon-high) per-cell table of record, and every figure the result quotes. Nothing is typed.
  score receipts  ~/.fleet/executors/gemini.runs/<SCORE_DIRS>/*.p1.score.txt   (the hand's, score_wave_v3.sh), the three dirs named in
                  SCORE_DIRS and no glob over the runs root: T-WA-P's re-fire wawas1r201 (its own dir), then the WHT and NTT waves. The
                  voided wawas101 and the not-of-record wawas1r01 (WA ADDENDA 3 and 5) have receipts in OTHER dirs, and are not read.
  Built from the Flash half's wa_cells_gen.py (evidence/blockWA-2026-11-14/); the changes: the dirs, the receipt glob, an end-1 kinds
  line, the receipt's cell count taken over DISTINCT ids, and cost pairs that mark a TRUNCATED cell (T) and name the untruncated pairs without an inequality (helm ruling 2026-09-11).
  cell facts      cell_facts.json beside this file (wa_facts.py, read on the run box from each cell's own ctl/)
A value that cannot be read is UNREAD, never blank and never zero.
  python3 wa_cells_gen.py            -> the per-cell table (TSV, stdout)
  python3 wa_cells_gen.py --summary  -> the figure lines RESULT-gemini-blockWA-pro-2026-11-15.md quotes, from the table's own rows
  python3 wa_cells_gen.py --check <result.md>  -> rc 0 iff every --summary line occurs verbatim in that file (rc 1 names the missing)"""
import glob, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
RUNS = os.environ.get('WA_RUNS') or os.path.expanduser('~/.fleet/executors/gemini.runs')   # WA_RUNS: a test root only
SCORE_DIRS = ('wa-twap-argon-r2-2026-11-15-score', 'wa-pro-wht-argon-2026-11-15-score', 'wa-pro-ntt-argon-2026-11-15-score')
COLS = ['id', 'root', 'problem', 'arm', 'requested_model', 'init_model', 'client_sha256', 'export_sha', 'T', 'turns_sent',
        'cut_turns', 'cut_turns_all', 'wall_seconds', 'done_reason', 'landed', 'false_done_claims', 'end1', 'verdict', 'TESTS',
        'truncated', 'interface', 'landed_tags', 'score_receipt']


def receipts():
    out = {}
    for f in [g for d in SCORE_DIRS for g in sorted(glob.glob(os.path.join(RUNS, d, '*.p1.score.txt')))]:
        text = open(f, errors='replace').read()
        iface = re.search(r'share interface (\w+)', text)
        tr = re.search(r'TRUNCATED (\d+)', text)
        ncell = len(set(re.findall(r'^(wa[a-z0-9]+)\s', text, re.M)))   # DISTINCT cells: a TRUNCATED cell's receipt carries its id on 3 rows, and
                                                                       #   the Flash generator's row count read every such cell UNREAD (no Flash cell was cut)
        for line in text.splitlines():
            m = re.match(r'(wa[a-z0-9]+)\s+\S+\s+\S+\s+\S+\s+(PASS|FAIL|NOT-LANDED|NOT-SCORED)\b(.*)$', line)
            if m:
                if m.group(1) in out:
                    sys.exit('REFUSE: cell %s has two receipts (%s and %s)' % (m.group(1), out[m.group(1)]['score_receipt'], os.path.relpath(f, RUNS)))
                t = re.search(r'TESTS (\d+/\d+)', m.group(3))
                out[m.group(1)] = dict(verdict=m.group(2), TESTS=t.group(1) if t else 'UNREAD',
                                       truncated=('UNREAD' if not tr or ncell != 1 else ('yes' if int(tr.group(1)) else 'no')),
                                       interface=iface.group(1)[:16] if iface else 'UNREAD',
                                       score_receipt=os.path.relpath(f, RUNS))
    return out


def table():
    facts = json.load(open(os.path.join(HERE, 'cell_facts.json')))
    sc = receipts()
    rows = []
    for f in facts:
        r = {k: f.get(k, 'UNREAD') for k in COLS}
        r.update(sc.get(f['id'], dict(verdict='UNREAD', TESTS='UNREAD', truncated='UNREAD', interface='UNREAD', score_receipt='UNREAD')))
        rows.append(r)
    return rows


def summary(rows):
    L = []
    L.append('cells %d · scored %d · receipts read %d' % (len(rows), sum(r['verdict'] in ('PASS', 'FAIL') for r in rows),
                                                          sum(r['score_receipt'] != 'UNREAD' for r in rows)))
    for k in ('requested_model', 'init_model', 'client_sha256', 'export_sha', 'done_reason'):
        vals = {}
        for r in rows:
            vals[str(r[k])[:12] if k == 'export_sha' else str(r[k])] = vals.get(str(r[k])[:12] if k == 'export_sha' else str(r[k]), 0) + 1
        L.append('%s %s' % (k, ' '.join('%s=%d' % kv for kv in sorted(vals.items()))))
    for p in ('WHT', 'NTT'):
        for a in ('plain', 'salt-diet'):
            rs = [r for r in rows if r['problem'] == p and r['arm'] == a]
            L.append('%s %s: FULL PASS %d of %d scored, of %d fired [%s] · cut turns %d of %d sent · truncated %d · interface %s' % (
                p, a, sum(r['verdict'] == 'PASS' and r['TESTS'].split('/')[0] == r['TESTS'].split('/')[-1] for r in rs),
                sum(r['verdict'] in ('PASS', 'FAIL') for r in rs), len(rs), ' '.join(r['TESTS'] for r in rs),
                sum(int(r['cut_turns_all']) for r in rs), sum(int(r['turns_sent']) for r in rs),
                sum(r['truncated'] == 'yes' for r in rs), ','.join(sorted({r['interface'] for r in rs}))))
    ek = {}
    for r in rows:
        k = str(r['end1']).split()[1] if len(str(r['end1']).split()) > 1 else 'UNREAD'
        ek[k] = ek.get(k, 0) + 1
    L.append('end-1 kinds: %s' % ' '.join('%s=%d' % kv for kv in sorted(ek.items())))
    l2 = [r['id'] for r in rows if 'landed-2' in str(r['landed_tags']).split(',')]
    L.append('landed-2 tag present in %d of %d cells: %s' % (len(l2), len(rows), ' '.join(l2)))
    for p in ('WHT', 'NTT'):
        rep = lambda r: r['id'][5]   # wa<w|n><p|s><rep>01, and a re-fire wa…s<rep>r<k>01: the rep digit is the sixth character
        pl = {rep(r): r for r in rows if r['problem'] == p and r['arm'] == 'plain'}
        sd = {rep(r): r for r in rows if r['problem'] == p and r['arm'] == 'salt-diet'}
        assert sorted(pl) == sorted(sd) == ['1', '2', '3'], (p, sorted(pl), sorted(sd))
        mk = lambda r, k: '%s%s' % (r[k], ' (T)' if r['truncated'] == 'yes' else '')
        clean = [n for n in pl if pl[n]['truncated'] == 'no' and sd[n]['truncated'] == 'no']
        for k, lab in (('T', 'T'), ('wall_seconds', 'wall_s')):
            L.append('%s %s by rep (plain / salt-diet; (T) = TRUNCATED, not poolable): %s · untruncated pairs %d (%s)' % (
                p, lab, ' · '.join('#%s %s / %s' % (n, mk(pl[n], k), mk(sd[n], k)) for n in sorted(pl)),
                len(clean), ' '.join('#' + n for n in sorted(clean)) or 'none'))   # no inequality is printed: one pair carries no sign (kent's read of #446)
    return L


if __name__ == '__main__':
    rows = table()
    if len(sys.argv) > 1 and sys.argv[1] == '--summary':
        print('\n'.join(summary(rows)))
    elif len(sys.argv) > 2 and sys.argv[1] == '--check':
        body = open(sys.argv[2]).read()
        miss = [l for l in summary(rows) if l not in body]
        for l in miss:
            print('MISSING: ' + l)
        print('check: %d of %d summary lines present' % (len(summary(rows)) - len(miss), len(summary(rows))))
        sys.exit(1 if miss else 0)
    else:
        print('\t'.join(COLS))
        for r in rows:
            print('\t'.join(str(r[c]) for c in COLS))
