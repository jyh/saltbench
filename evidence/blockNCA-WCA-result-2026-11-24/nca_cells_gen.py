"""Blocks NCA and WCA per-cell table of record, and every figure their results quote. Nothing is typed.
  population      manifests/{NCA,WCA}-{flash,argon}-all.tsv beside this file: byte copies of the hand's chain manifests (96 rows).
                  The population is the manifests, never the receipts found, so a cell not yet scored reads UNSCORED, never absent
  score receipts  ~/.fleet/executors/gemini.runs/<dir>/<root>.p2.score.txt (the hand's, score_wave_v3.sh), over every dir named
                  {nca,wca}-*-score*. A root with two receipts is admitted only when they AGREE on every scored field (both are then
                  cited); two that disagree REFUSE (WA's abandoned-dir hazard): neither is ever chosen
  cell facts      cell_facts.json beside this file (nca_facts.py, read on the run box from each cell's own ctl/; `--fetch` writes it)
A value that cannot be read is UNREAD, never blank and never zero.
  python3 nca_cells_gen.py --fetch HOST   -> runs nca_facts.py on HOST over the 96 rows, writes cell_facts.json
  python3 nca_cells_gen.py                -> the per-cell table (TSV, stdout)
  python3 nca_cells_gen.py --summary      -> the figure lines the results quote, from the table's own rows
  python3 nca_cells_gen.py --check <md>   -> rc 0 iff every --summary line occurs verbatim in that file (rc 1 names the missing)
LIMIT: TESTS / REGRESSIONS / CLAUSE are the receipt's words; Liveness CLAUSE figures carry census ADDENDUM 46 NOTE 1 (NCA ADDENDUM 4)
and are never read as a premium. Nothing here compares arms, models or blocks."""
import glob, json, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
RUNS = os.environ.get('NCA_RUNS') or os.path.expanduser('~/.fleet/executors/gemini.runs')   # NCA_RUNS: a test root only
MANIFESTS = ('NCA-flash-all', 'NCA-argon-all', 'WCA-flash-all', 'WCA-argon-all')
COLS = ['block', 'root', 'id', 'problem', 'arm', 'p2_model', 'p2_client16', 'p2_export', 'hook16', 'source', 'T', 'turns_sent',
        'continue_turns', 'cut_turns_all', 'wall_seconds', 'done_reason', 'landed', 'false_done_claims', 'end2', 'verdict', 'TESTS',
        'REGRESSIONS', 'CLAUSE', 'truncated', 'interface', 'score_receipt']
NOSCORE = dict(verdict='UNSCORED', TESTS='UNSCORED', REGRESSIONS='UNSCORED', CLAUSE='UNSCORED', truncated='UNSCORED',
               interface='UNSCORED', score_receipt='UNSCORED')


def population():
    rows = []
    for m in MANIFESTS:
        for l in open(os.path.join(HERE, 'manifests', m + '.tsv')):
            if l.startswith('#') or not l.strip():
                continue
            f = l.rstrip('\n').split('\t')
            if len(f) != 8:
                sys.exit('REFUSE: %s row has %d fields, not 8: %r' % (m, len(f), l))
            rows.append(dict(block=m.replace('-all', ''), root=f[0], problem=f[1], arm=f[2], prefix=f[4], copy_from=f[7]))
    if len(rows) != 96 or len({r['root'] for r in rows}) != 96:
        sys.exit('REFUSE: the manifests read %d rows, %d distinct roots; 96 and 96 expected' % (len(rows), len({r['root'] for r in rows})))
    return rows


def receipts():
    out = {}
    dirs = sorted(d for d in glob.glob(os.path.join(RUNS, '*-score*')) if os.path.isdir(d) and re.match(r'(nca|wca)-', os.path.basename(d)))
    for f in [g for d in dirs for g in sorted(glob.glob(os.path.join(d, '*.p2.score.txt')))]:
        root = os.path.basename(f)[:-len('.p2.score.txt')]
        text = open(f, errors='replace').read()
        iface = re.search(r'share interface (\w+)', text)
        tr = re.search(r'TRUNCATED (\d+)', text)
        rec = dict(NOSCORE, score_receipt=os.path.relpath(f, RUNS), interface=iface.group(1)[:16] if iface else 'UNREAD',
                   truncated=('yes' if int(tr.group(1)) else 'no') if tr else 'UNREAD')
        hits = [m for m in (re.match(r'([a-z0-9]+)\s+\S+\s+\S+\s+\S+\s+(PASS|FAIL|NOT-LANDED|NOT-SCORED)\b(.*)$', x) for x in text.splitlines()) if m]
        if len(hits) != 1:
            rec.update(verdict='UNREAD-%d-ROWS' % len(hits))
        else:
            m = hits[0]
            g = lambda k: (re.search(k + r' (\d+/\d+)', m.group(3)) or [None, 'UNREAD'])[1]
            rec.update(cell=m.group(1), verdict=m.group(2), TESTS=g('TESTS'), REGRESSIONS=g('REGRESSIONS'), CLAUSE=g('CLAUSE_TESTS'))
        if root in out:
            same = all(out[root].get(k) == rec.get(k) for k in ('cell', 'verdict', 'TESTS', 'REGRESSIONS', 'CLAUSE', 'interface', 'truncated'))
            if not same:
                sys.exit('REFUSE: root %s has two receipts that DISAGREE (%s and %s)' % (root, out[root]['score_receipt'], rec['score_receipt']))
            out[root]['score_receipt'] += ',' + rec['score_receipt']   # a re-score that agrees on every scored field: both are cited
            continue
        out[root] = rec
    return out


def table():
    pop = population()
    facts = {f['root']: f for f in json.load(open(os.path.join(HERE, 'cell_facts.json')))} if os.path.exists(os.path.join(HERE, 'cell_facts.json')) else {}
    sc = receipts()
    stray = sorted(set(sc) - {p['root'] for p in pop})
    if stray:
        sys.exit('REFUSE: receipts for roots outside the 96: %s' % ' '.join(stray))
    rows = []
    for p in pop:
        r = {k: 'UNREAD' for k in COLS}
        r.update({k: p[k] for k in ('block', 'root', 'problem', 'arm')})
        r.update({k: v for k, v in facts.get(p['root'], {}).items() if k in COLS and k != 'root'})
        s = sc.get(p['root'], NOSCORE)
        if 'cell' in s and r['id'] not in ('UNREAD', s['cell']):
            sys.exit('REFUSE: %s receipt names cell %s, the facts name %s' % (p['root'], s['cell'], r['id']))
        r.update({k: v for k, v in s.items() if k in COLS})
        rows.append(r)
    return rows


def summary(rows):
    scored = lambda rs: [r for r in rs if r['verdict'] in ('PASS', 'FAIL')]
    L = ['rows %d · scored %d · receipts %d · facts %d' % (len(rows), len(scored(rows)), sum(r['score_receipt'] != 'UNSCORED' for r in rows),
                                                       sum(r['id'] not in ('UNREAD', 'NO-CELL', 'TWO-CELLS') for r in rows))]
    for k in ('p2_model', 'p2_client16', 'p2_export', 'hook16', 'done_reason'):
        v = {}
        for r in rows:
            x = str(r[k])[:12] if k == 'p2_export' else str(r[k]); v[x] = v.get(x, 0) + 1
        L.append('%s %s' % (k, ' '.join('%s=%d' % kv for kv in sorted(v.items()))))
    for b in ('NCA-flash', 'NCA-argon', 'WCA-flash', 'WCA-argon'):
        for pr in sorted({r['problem'] for r in rows if r['block'] == b}):
            for a in ('plain', 'salt-diet'):
                rs = [r for r in rows if r['block'] == b and r['problem'] == pr and r['arm'] == a]
                if not rs:
                    continue
                sr = scored(rs)
                ct = [r['cut_turns_all'] for r in sr]
                L.append('%s %s %s: PASS %d of %d scored, of %d registered [%s] · cut turns %s · truncated %d of %d scored' % (
                    b, pr, a, sum(r['verdict'] == 'PASS' for r in sr), len(sr), len(rs),
                    ' '.join('T%s R%s C%s' % (r['TESTS'], r['REGRESSIONS'], r['CLAUSE']) for r in sr) or '-',
                    ('%d' % sum(ct) if all(isinstance(x, int) for x in ct) else 'UNREAD') if sr else '-',   # over SCORED cells only, never a 0 for none
                    sum(r['truncated'] == 'yes' for r in sr), len(sr)))
    return L


def fetch(host):
    rows = population()
    src = open(os.path.join(HERE, 'nca_facts.py')).read()
    remote = '~/bench-dry/nca-facts-%d.py' % os.getpid()
    subprocess.run(['ssh', host, 'mkdir -p ~/bench-dry && cat > ' + remote], input=src, text=True, check=True)
    stdin = ''.join('%s\t%s\t%s\n' % (r['root'], r['prefix'], r['copy_from']) for r in rows)
    p = subprocess.run(['ssh', host, '/usr/bin/python3 -I ' + remote + '; rc=$?; rm -f ' + remote + '; exit $rc'], input=stdin,
                       capture_output=True, text=True)
    if p.returncode != 0:
        sys.exit('REFUSE: nca_facts.py rc %d on %s: %s' % (p.returncode, host, p.stderr[-400:]))
    facts = json.loads(p.stdout)
    if len(facts) != 96:
        sys.exit('REFUSE: %d fact records for 96 rows' % len(facts))
    with open(os.path.join(HERE, 'cell_facts.json'), 'w') as f:
        json.dump(facts, f, indent=1, sort_keys=True); f.write('\n')
    print('cell_facts.json: %d records from %s' % (len(facts), host))


if __name__ == '__main__':
    a = sys.argv[1:]
    if a[:1] == ['--fetch'] and len(a) == 2:
        fetch(a[1])
    elif a == ['--summary']:
        print('\n'.join(summary(table())))
    elif a[:1] == ['--check'] and len(a) == 2:
        body = open(a[1]).read(); S = summary(table())
        miss = [l for l in S if l not in body]
        for l in miss:
            print('MISSING: ' + l)
        print('check: %d of %d summary lines present' % (len(S) - len(miss), len(S)))
        sys.exit(1 if miss else 0)
    elif not a:
        print('\t'.join(COLS))
        for r in table():
            print('\t'.join(str(r[c]) for c in COLS))
    else:
        sys.exit(__doc__)
