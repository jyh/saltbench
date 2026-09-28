"""Build block NA's per-cell table of record (AMENDMENT-O37-nine-greenfield-agy-2026-09-25.md §NA6 = level 6 §H8's list, plus
the tree-hash line per cell and the x86-lane concurrency column; ADDENDUM 4's cut outcome and CUT-BOUND column).
`served` is the model and `cond` the condition (problem-arm, per served model), the two columns pilot-grid reads.

Nothing is typed. Every column is read from a file:
  score receipts   ~/.fleet/executors/gemini.runs/<label>-score/cells-na-*.p1.score.txt   (verdict, TESTS, TRUNCATED, SELF-NOT, interface)
  cell facts       evidence/blockNA-2026-09-28/cell_facts.json   (cell_facts.py, read on the run box from each cell's own ctl/)
  tree hashes      evidence/blockNA-2026-09-28/tree_hashes.tsv   (git rev-parse <export>:tasks/systems-v3/<P>, against e54f35a)
  x86 windows      evidence/blockNA-2026-09-28/x86_windows.tsv   (x86_windows.py, from the x86 agy waves' ledgers)
  rulings          evidence/blockNA-2026-09-28/rulings.tsv       (a classification that is a RULING, with where it lives; one cell each)
A value that could not be read is UNREAD, never blank and never zero.

  python3 RESULT-gemini-blockNA-cells-gen.py              -> the per-cell table (stdout)
  python3 RESULT-gemini-blockNA-cells-gen.py --conditions -> one row per (served, cond), from the per-cell table's own rows
  python3 RESULT-gemini-blockNA-cells-gen.py --arms       -> ADDENDUM 4's outcome: cut turns / turns and truncated / cells, per model per arm
"""
import csv, glob, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
EV = os.path.join(HERE, '..', '..', 'evidence', 'blockNA-2026-09-28')
RUNS = os.path.expanduser('~/.fleet/executors/gemini.runs')
COLS = ['id', 'root', 'cond', 'served', 'problem', 'arm', 'export_sha', 'task_tree', 'tree_vs_e54f35a', 'interface',
        'T', 'turns_sent', 'continue_turns', 'persist_sent', 'cut_turns', 'wall_s', 'done_reason', 'landed', 'false_done',
        'client_reaped', 'end1', 'score_status', 'verdict', 'TESTS', 'truncated', 'self_not', 'non_landing', 'x86_concurrent',
        'in_registered_n', 'ruling', 'score_receipt']
FINAL = ('PASS', 'FAIL', 'NOT-LANDED', 'NOT-SCORED')


def tsv(path):
    rows = [l.rstrip('\n').split('\t') for l in open(path) if l.strip() and not l.startswith('#')]
    return [dict(zip(rows[0], r)) for r in rows[1:]]


def scores():
    """id -> the score receipt's reading. A cell's final verdict is its PASS/FAIL/NOT-LANDED/NOT-SCORED line; TRUNCATED and
    SELF-NOT lines are separate facts about the same cell. The interface hash is the receipt's POOLABLE line."""
    out = {}
    for f in sorted(glob.glob(os.path.join(RUNS, '*-score', 'cells-na-*.p1.score.txt'))):
        text = open(f, errors='replace').read()
        m = re.search(r'share interface (\w+)', text)
        iface = m.group(1) if m else 'UNREAD'
        for l in text.splitlines():
            c = re.match(r'(na[a-z0-9]+)\s+(\S+)\s+\S+\s+(\S+)\s+(\S+)(.*)', l)
            if not c:
                continue
            cid, status, verdict, rest = c.group(1), c.group(2), c.group(4), c.group(5)
            d = out.setdefault(cid, dict(score_status='UNREAD', verdict='UNREAD', TESTS='-', truncated='no', self_not='no',
                                         interface=iface, score_receipt=os.path.relpath(f, RUNS)))
            if verdict == 'TRUNCATED':
                d['truncated'] = 'yes'
            elif verdict == 'SELF-NOT':
                d['self_not'] = 'yes'
            elif verdict in FINAL:
                t = re.search(r'TESTS (\S+)', rest)
                d.update(score_status=status, verdict=verdict, TESTS=t.group(1) if t else '-')
    return out


def overlaps(start, end, wins):
    if 'UNREAD' in (start, end):
        return 'UNREAD'
    hit = sorted({w['wave'] for w in wins if start < w['end'] and end > w['start']})
    return ','.join(hit) if hit else 'none'


def cells():
    facts = json.load(open(os.path.join(EV, 'cell_facts.json')))
    trees = {(r['export_sha'], r['problem']): r for r in tsv(os.path.join(EV, 'tree_hashes.tsv'))}
    wins = tsv(os.path.join(EV, 'x86_windows.tsv'))
    rulings = {r['id']: r for r in tsv(os.path.join(EV, 'rulings.tsv'))}
    sc = scores()
    out = []
    for f in sorted(facts, key=lambda r: (r['requested_model'], r['problem'], r['arm'], r['id'])):
        cid = f['id']
        s = sc.get(cid, {})
        t = trees.get((f['export_sha'], f['problem']), {})
        ru = rulings.get(cid, {})
        end = f['end1'].split()[0] if f['end1'] != 'UNREAD' else 'UNREAD'
        if f['landed'] is True:
            nl = '-'
        elif f['landed'] is False:
            nl = 'NOT-LANDED %s; cut %s of %s turns sent' % (f['done_reason'], f['cut_turns'], f['turns_sent'])
        else:
            nl = 'UNREAD'
        out.append(dict(
            id=cid, root=f['root'], cond='%s-%s' % (f['problem'], f['arm']), served=f['requested_model'],
            problem=f['problem'], arm=f['arm'], export_sha=f['export_sha'][:12], task_tree=t.get('tree', 'UNREAD'),
            tree_vs_e54f35a=t.get('same', 'UNREAD'), interface=s.get('interface', 'UNREAD'),
            T=f['T'], turns_sent=f['turns_sent'], continue_turns=f.get('continue_turns', 'UNREAD'),
            persist_sent=f.get('persist_sent', 'UNREAD'), cut_turns=f['cut_turns'], wall_s=f['wall_seconds'],
            done_reason=f['done_reason'], landed=f['landed'], false_done=f['false_done_claims'],
            client_reaped=f['client_reaped'], end1=f['end1'],
            score_status=s.get('score_status', 'UNREAD'), verdict=s.get('verdict', 'UNREAD'), TESTS=s.get('TESTS', 'UNREAD'),
            truncated=s.get('truncated', 'UNREAD'), self_not=s.get('self_not', 'UNREAD'), non_landing=nl,
            x86_concurrent=overlaps(f['built_at'], end, wins),
            in_registered_n=ru.get('in_registered_n', 'yes'), ruling=ru.get('class', '-'),
            score_receipt=s.get('score_receipt', 'UNREAD')))
    return out


def write(rows, cols):
    w = csv.writer(sys.stdout, delimiter='\t', lineterminator='\n')
    w.writerow(cols)
    for r in rows:
        w.writerow([r[c] for c in cols])


def conditions(rows):
    """One row per (served, cond), over the cells IN the registered n only. A ruling that classifies a cell a RESULT puts it in
    `fired` and in its non-landing column; a cell outside the registered n is counted in `outside_n` and nowhere else."""
    groups = {}
    for r in rows:
        groups.setdefault((r['served'], r['cond']), []).append(r)
    out = []
    for (served, cond), rs in sorted(groups.items()):
        n = [r for r in rs if r['in_registered_n'] == 'yes']
        landed = [r for r in n if r['landed'] is True]
        scored = [r for r in n if r['verdict'] in ('PASS', 'FAIL') and r['landed'] is True]
        cutbound = [r for r in n if 'CUT-BOUND' in r['ruling']]
        other_nl = [r for r in n if r['landed'] is False and 'CUT-BOUND' not in r['ruling']]
        out.append(dict(served=served, cond=cond, fired=len(n), landed=len(landed), scored=len(scored),
                        full_pass=sum(r['verdict'] == 'PASS' for r in scored), truncated=sum(r['truncated'] == 'yes' for r in n),
                        cut_bound=len(cutbound), not_landed_other=len(other_nl),
                        outside_n=len(rs) - len(n), interfaces=','.join(sorted({r['interface'] for r in rs})),
                        x86_concurrent=sum(r['x86_concurrent'] not in ('none', 'UNREAD') for r in n)))
    return out


def arms(rows):
    """ADDENDUM 4: per model, per arm, cut turns / turns and truncated cells / cells, source the client's stderr. In-n cells only."""
    groups = {}
    for r in rows:
        if r['in_registered_n'] == 'yes':
            groups.setdefault((r['served'], r['arm']), []).append(r)
    return [dict(served=s, arm=a, cells=len(rs), cut_turns=sum(r['cut_turns'] for r in rs),
                 turns_sent=sum(r['turns_sent'] for r in rs), truncated=sum(r['truncated'] == 'yes' for r in rs),
                 cut_bound=sum('CUT-BOUND' in r['ruling'] for r in rs))
            for (s, a), rs in sorted(groups.items())]


if __name__ == '__main__':
    rows = cells()
    if '--conditions' in sys.argv:
        c = conditions(rows)
        write(c, list(c[0]))
    elif '--arms' in sys.argv:
        a = arms(rows)
        write(a, list(a[0]))
    else:
        write(rows, COLS)
