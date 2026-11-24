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
The cell is FOUND: a copy root holds one cell, the basename of the manifest's copy_from; a fresh root holds the one dir whose name
starts with the manifest's prefix. Zero or two candidates is NO-CELL / TWO-CELLS, never a guess. A value that cannot be read is UNREAD.
usage (on the run box):  python3 -I nca_facts.py < rows   (rows: root TAB prefix TAB copy_from, one per manifest row) -> JSON list"""
import json, os, re, sys

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


out = []
for line in sys.stdin:
    if not line.strip():
        continue
    root, prefix, copy_from = (line.rstrip('\n').split('\t') + ['', ''])[:3]
    cid = find(root, prefix, copy_from)
    rec = {'root': root, 'id': cid}
    if cid in ('NO-CELL', 'TWO-CELLS'):   # nothing below is read from a cell that is not found: every field says so, none reads FRESH or 0
        out.append(dict(rec, **{k: cid for k in ('T', 'requested_model', 'meter_verdict', 'cut_turns_all', 'p2_model', 'p2_client16', 'end1',
                                                   'end2', 'source', 'p2_export', 'hook16') + LOOP}))
        continue
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
    rec['end1'], rec['end2'] = first_line(os.path.join(c, 'end-1')), first_line(os.path.join(c, 'end-2'))
    cf = os.path.join(c, 'copied-from.tsv')
    if os.path.exists(cf):
        k = kv(cf)
        h = re.match(r'sha256=([0-9a-f]{16})', k.get('web_deny_replaced', ''))
        rec.update(source=k.get('source', 'UNREAD'), p2_export=k.get('phase2_export', 'UNREAD'), hook16=h.group(1) if h else 'UNREAD')
    else:
        rec.update(source='FRESH', p2_export=kv(os.path.join(c, 'built-from.tsv')).get('export_sha', 'UNREAD'), hook16='FRESH')
    out.append(rec)
json.dump(out, sys.stdout, indent=1, sort_keys=True)
print()
