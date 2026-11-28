"""Blocks NCA and WCA per-cell PHASE-2 facts, read on the run box from each cell's own ctl/ record. Nothing is typed.
Block NA's cell_facts.py read phase 1 (the `-1` files); a spec-change cell's scored phase is 2, so this reads the `-2` files:
  T, requested_model, meter_verdict   ctl/agy-meter-2.json
  turns_sent ... persist_answered     ctl/agy-turnloop-2.json
  cut_turns_all                       lines carrying `print timeout` across agy-stderr-2.txt AND agy-turnloop-stderr-2.txt (WA's rule)
  p2_model, p2_client16               ctl/launch.log's LAST `LAUNCHING phase 2 model <m> client <16hex>` line. ⛔ NOT built-from-2.tsv:
                                      a COPY carries NA's (export e10f420d, built 2026-09-26, measured on nalvfp01's copy 2026-11-24)
  p2_export                           a copy: copied-from.tsv phase2_export; a fresh cell: built-from.tsv export_sha (built for NCA)
  end1, end2                          ctl/end-1, ctl/end-2 first lines
  source, hook16                      ctl/copied-from.tsv: source, web_deny_replaced's sha256 first 16 hex
                                      (a fresh cell has no copied-from.tsv: both read FRESH)
  p2_gate                             the §A9.2 gate's OWN verdict, written outside the cell: the LAST `phase2-landed-gate <id> rc=N
                                      <VERDICT>` line over ~/agy-widen-*.log whose id is the cell's AND whose receipt= is the first 12 hex of
                                      THIS cell's repo/.seat/landing-1 (ids recur across roots: ncalvap01 is in two; a line carries no
                                      root), as `rc=N VERDICT` plus `tag=… receipt=…` on a refusal. NONE = no matching line (or no receipt
                                      in the cell); UNREAD = no widen log readable.
                                      ⛔ NOT .seat/landing-N: a healthy two-phase cell carries landing-1..N across both phases
The cell is FOUND: a copy root holds one cell, the basename of the manifest's copy_from; a fresh root holds the one dir whose name
starts with the manifest's prefix. Zero or two candidates is NO-CELL / TWO-CELLS, never a guess. A value that cannot be read is UNREAD.
usage (on the run box):  python3 -I nca_facts.py < rows   (rows: root TAB prefix TAB copy_from, one per manifest row) -> JSON list"""
import glob, json, os, re, sys

H = os.path.expanduser('~')
LOOP = ('turns_sent', 'continue_turns', 'wall_seconds', 'done_reason', 'landed', 'false_done_claims', 'persist_sent', 'persist_answered')


def kv(path):
    try:
        return dict(l.rstrip('\n').split('\t', 1) for l in open(path) if '\t' in l)
    except OSError:
        return {}


def first_line(path):
    try:
        return open(path).readline().strip() or 'UNREAD'
    except OSError:
        return 'UNREAD'


def gate_lines():
    out, seen = {}, 0
    for f in sorted(glob.glob(os.path.join(H, 'agy-widen-*.log'))):
        try:
            for l in open(f, errors='replace'):
                m = re.match(r'phase2-landed-gate (\S+) rc=(\d+) (\S+)(.*)$', l.strip())
                if m:
                    head = m.group(4).split('|')[0]
                    rc = re.search(r'receipt=([0-9a-f]{12})', head)
                    v = 'rc=%s %s' % (m.group(2), m.group(3))
                    if m.group(2) != '0':
                        v += ''.join(' ' + x for x in re.findall(r'(?:tag|receipt)=\S+', head)[:2])
                    out[(m.group(1), rc.group(1) if rc else None)] = v     # the LAST line for an (id, receipt) wins
            seen += 1
        except OSError:
            pass
    return out, seen


def standing(root):
    """The ATTEMPT that stands for a manifest root (L8 A2.2: the per-cell table carries each cell's attempt number). The canary
    supervisor discards a 503-touched attempt by RENAMING its root `<root>[-a<k>].DISCARDED-503-<utc>` and re-queues it as root
    `<root>-a<k+1>`, prefix `<prefix>a<k+1>`. So the standing attempt is the ONE of `<root>` (attempt 1) and `<root>-a<k>` (k >= 2)
    that exists as a directory. None is NO-ROOT and two is TWO-ATTEMPTS, never a guess. Returns (root, k, discarded-count)."""
    try:
        names = os.listdir(H)
    except OSError:
        return 'NO-ROOT', 0, 'UNREAD'
    cand = [(root, 1)] if root in names and os.path.isdir(os.path.join(H, root)) else []
    for n in names:
        m = re.fullmatch(re.escape(root) + r'-a([0-9]+)', n)
        if m and int(m.group(1)) >= 2 and os.path.isdir(os.path.join(H, n)):
            cand.append((n, int(m.group(1))))
    disc = sum(bool(re.fullmatch(re.escape(root) + r'(-a[0-9]+)?\.DISCARDED-503-.+', n)) for n in names)
    if len(cand) != 1:
        return ('NO-ROOT' if not cand else 'TWO-ATTEMPTS'), 0, disc
    return cand[0][0], cand[0][1], disc


def find(root, prefix, copy_from):
    d = os.path.join(H, root)
    if copy_from not in ('', '-'):
        cid = os.path.basename(copy_from)
        return cid if os.path.isdir(os.path.join(d, cid, 'ctl')) else 'NO-CELL'
    try:
        c = sorted(n for n in os.listdir(d) if n.startswith(prefix) and os.path.isdir(os.path.join(d, n, 'ctl')))
    except OSError:
        return 'NO-CELL'
    return c[0] if len(c) == 1 else ('NO-CELL' if not c else 'TWO-CELLS')


GBASE = os.path.join(H, 'bench-dry', 'nca-fresh-gbase-2026-11-25')


def gbase(sroot, cid):
    """NC rule 4's G baseline of a FRESH cell, read from its own record (gemini-fresh-gbase.sh, keyed by ROOT + ID; three legacy
    id-only dirs carry CELL-ROOT.txt). -> (g_tests, g_verdict, g_sha12, g_aborted). The verdict is the log's TESTS line read by
    gbase.sh's own rule (passed == total > 0); gbase.sh does not record run_tests.sh's rc, so the generator cross-checks every
    verdict that has a harvest ROW line (which does). NO-RECORD = no base dir; NO-LOG = a base dir and no log (gbase.sh refused before
    the clone, e.g. no landed-1 tag). g_aborted counts `<root>.ABORTED-*` dirs beside it (an attempt that did not complete)."""
    d = os.path.join(GBASE, sroot, cid)
    if not os.path.isdir(d):
        leg = os.path.join(GBASE, cid)
        d = leg if first_line(os.path.join(leg, 'CELL-ROOT.txt')) == sroot else None
    try:
        ab = sum(n.startswith(sroot + '.ABORTED-') for n in os.listdir(GBASE))
    except OSError:
        ab = 'UNREAD'
    if d is None:
        return 'NO-RECORD', 'NO-RECORD', 'NO-RECORD', ab
    log = os.path.join(d, 'logs', cid + '.G.log')
    try:
        tl = [l.strip() for l in open(log, errors='replace') if l.startswith('TESTS ')]
    except OSError:
        return 'NO-LOG', 'NO-LOG', 'NO-LOG', ab
    m = re.fullmatch(r'TESTS (\d+)/(\d+)', tl[-1]) if tl else None
    v = 'ELIGIBLE' if m and m.group(1) == m.group(2) and int(m.group(2)) > 0 else 'NOT-ELIGIBLE'
    head = first_line(os.path.join(d, 'work', cid, '.git', 'HEAD'))   # a detached checkout of landed-1 writes the sha here
    return ('%s/%s' % m.groups() if m else 'NO-TESTS-LINE'), v, (head[:12] if re.fullmatch(r'[0-9a-f]{40}', head) else 'UNREAD'), ab


P1 = ('p1_model', 'p1_client16', 'p1_T', 'p1_wall_seconds', 'p1_done_reason', 'p1_turns_sent', 'p1_cut_turns_all')


def p1_launch(path):
    """(model, client16) from the LAST `LAUNCHING phase 1` line of a launch.log; NO-LOG if absent, NO-LINE if no such line."""
    try:
        hits = [m.groups() for m in (re.search(r'LAUNCHING phase 1 model (\S+) client ([0-9a-f]{16})', l) for l in open(path, errors='replace')) if m]
    except OSError:
        return 'NO-LOG', 'NO-LOG'
    return hits[-1] if hits else ('NO-LINE', 'NO-LINE')


def phase1(root, cid, source):
    """L8 §M10's phase-1 columns and §NCA8's phase-1 client, read from the cell's own record: the wave sets phase 1 aside at phase 2
    (`<root>/_aside/<id>/phase1/ctl/`, fresh cells and copies alike); the phase-1 meter stays in `<cell>/ctl/agy-meter-1.json`.
    A copy's aside launch line is cross-checked against its SOURCE's own ctl/launch.log: two that differ read DISAGREE, never one."""
    a = os.path.join(H, root, '_aside', cid, 'phase1', 'ctl')
    if not os.path.isdir(a):   # no phase 2 ran (a gate refused it), so phase 1 was never set aside: its record is still the cell's own ctl/
        a = os.path.join(H, root, cid, 'ctl')
    r = dict(zip(('p1_model', 'p1_client16'), p1_launch(os.path.join(a, 'launch.log'))))
    if source not in ('FRESH', 'UNREAD'):
        sm, sc = p1_launch(os.path.join(source, 'ctl', 'launch.log'))
        if r['p1_client16'] in ('NO-LOG', 'NO-LINE') and sc not in ('NO-LOG', 'NO-LINE'):   # the source fills an absent aside line; it never overwrites one state with another
            r['p1_model'], r['p1_client16'] = sm, sc
        elif sc not in ('NO-LOG', 'NO-LINE') and (sm, sc) != (r['p1_model'], r['p1_client16']):
            r['p1_model'] = r['p1_client16'] = 'DISAGREE'
    try:
        r['p1_T'] = json.load(open(os.path.join(H, root, cid, 'ctl', 'agy-meter-1.json'))).get('T', 'UNREAD')
    except (OSError, ValueError):
        r['p1_T'] = 'UNREAD'
    try:
        t = json.load(open(os.path.join(a, 'agy-turnloop-1.json')))
        r.update(p1_wall_seconds=t.get('wall_seconds', 'UNREAD'), p1_done_reason=t.get('done_reason', 'UNREAD'), p1_turns_sent=t.get('turns_sent', 'UNREAD'))
    except (OSError, ValueError):
        r.update(p1_wall_seconds='UNREAD', p1_done_reason='UNREAD', p1_turns_sent='UNREAD')
    n, seen = 0, 0
    for f in ('agy-stderr-1.txt', 'agy-turnloop-stderr-1.txt'):
        try:
            n += sum('print timeout' in l for l in open(os.path.join(a, f), errors='replace')); seen += 1
        except OSError:
            pass
    r['p1_cut_turns_all'] = n if seen == 2 else 'UNREAD'
    return r


GATE, GATE_LOGS = gate_lines()
out = []
for line in sys.stdin:
    if not line.strip():
        continue
    root, prefix, copy_from = (line.rstrip('\n').split('\t') + ['', ''])[:3]
    sroot, k, disc = standing(root)
    # a fresh attempt k >= 2 is built with prefix <prefix>a<k>; a copy keeps its source's id (the wave strips a<k> before its check)
    cid = sroot if sroot in ('NO-ROOT', 'TWO-ATTEMPTS') else find(sroot, prefix + ('a%d' % k if k >= 2 else ''), copy_from)
    rec = {'root': root, 'id': cid, 'standing_root': sroot, 'attempt': k if k else sroot, 'discarded': disc}
    if cid in ('NO-CELL', 'TWO-CELLS', 'NO-ROOT', 'TWO-ATTEMPTS'):   # nothing below is read from a cell that is not found: every field says so, none reads FRESH or 0
        out.append(dict(rec, **{k: cid for k in ('T', 'requested_model', 'meter_verdict', 'cut_turns_all', 'p2_model', 'p2_client16', 'end1',
                                                   'end2', 'source', 'p2_export', 'hook16', 'p2_gate', 'g_tests', 'g_verdict', 'g_sha12', 'g_aborted') + LOOP + P1}))
        continue
    root = sroot   # every read below is of the standing attempt's cell; rec['root'] stays the manifest row's
    c = os.path.join(H, root, cid, 'ctl')
    try:
        m = json.load(open(os.path.join(c, 'agy-meter-2.json')))
        rec.update(T=m.get('T', 'UNREAD'), requested_model=m.get('requested_model', 'UNREAD'), meter_verdict=m.get('verdict', 'UNREAD'))
    except (OSError, ValueError):
        rec.update(T='UNREAD', requested_model='UNREAD', meter_verdict='UNREAD')
    try:
        t = json.load(open(os.path.join(c, 'agy-turnloop-2.json')))
        rec.update({k: t.get(k, 'UNREAD') for k in LOOP})
    except (OSError, ValueError):
        rec.update({k: 'UNREAD' for k in LOOP})
    n, seen = 0, 0
    for f in ('agy-stderr-2.txt', 'agy-turnloop-stderr-2.txt'):
        try:
            n += sum('print timeout' in l for l in open(os.path.join(c, f), errors='replace')); seen += 1
        except OSError:
            pass
    rec['cut_turns_all'] = n if seen == 2 else 'UNREAD'
    rec['p2_model'] = rec['p2_client16'] = 'UNREAD'
    try:
        for l in open(os.path.join(c, 'launch.log'), errors='replace'):
            m = re.search(r'LAUNCHING phase 2 model (\S+) client ([0-9a-f]{16})', l)
            if m:
                rec['p2_model'], rec['p2_client16'] = m.group(1), m.group(2)
    except OSError:
        pass
    r1 = first_line(os.path.join(H, root, cid, 'repo', '.seat', 'landing-1'))
    rec['p2_gate'] = 'UNREAD' if not GATE_LOGS else ('NONE' if not re.fullmatch(r'[0-9a-f]{40}', r1) else GATE.get((cid, r1[:12]), 'NONE'))
    rec['end1'], rec['end2'] = first_line(os.path.join(c, 'end-1')), first_line(os.path.join(c, 'end-2'))
    cf = os.path.join(c, 'copied-from.tsv')
    if os.path.exists(cf):
        k = kv(cf)
        h = re.match(r'sha256=([0-9a-f]{16})', k.get('web_deny_replaced', ''))
        rec.update(source=k.get('source', 'UNREAD'), p2_export=k.get('phase2_export', 'UNREAD'), hook16=h.group(1) if h else 'UNREAD')
    else:
        rec.update(source='FRESH', p2_export=kv(os.path.join(c, 'built-from.tsv')).get('export_sha', 'UNREAD'), hook16='FRESH')
    rec.update(phase1(root, cid, rec['source']))
    if rec['source'] == 'FRESH':
        rec['g_tests'], rec['g_verdict'], rec['g_sha12'], rec['g_aborted'] = gbase(root, cid)
    else:   # a copy's source was made eligible by the census (ADDENDUM 1); it owes no fresh G baseline
        rec['g_tests'] = rec['g_verdict'] = rec['g_sha12'] = 'COPY'; rec['g_aborted'] = 0
    out.append(rec)
json.dump(out, sys.stdout, indent=1, sort_keys=True)
print()
