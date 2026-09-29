"""Block NA per-cell facts, read on the run box from each cell's own ctl/ record. Nothing is typed.
T and requested_model from agy-meter-1.json; turns/wall/done_reason/landed/false_done/client_reaped/rc from agy-turnloop-1.json;
CUT turns = the count of lines carrying `print timeout` in the client's stderr ctl/agy-stderr-1.txt (ADDENDUM 4: the stderr is the
source for a cut, never the turn loop's TURN-DENIED line); export_sha, problem, arm, built_at from ctl/built-from.tsv; the END line
from ctl/end-1; the first and last stamps of ctl/fire.log bound the cell's span. A value that cannot be read is UNREAD.
usage: python3 cell_facts.py <root>/<id> ...   (paths relative to $HOME)  -> JSON list on stdout"""
import json, os, sys
H = os.path.expanduser('~')

def kv(path):
    try:
        return dict(l.rstrip('\n').split('\t', 1) for l in open(path) if '\t' in l)
    except OSError:
        return {}

def first_last_stamp(path):
    try:
        ls = [l.split()[0] for l in open(path, errors='replace') if l[:2] == '20' and 'T' in l[:20]]
        return (ls[0], ls[-1]) if ls else ('UNREAD', 'UNREAD')
    except OSError:
        return ('UNREAD', 'UNREAD')

out = []
for rel in sys.argv[1:]:
    root, cid = rel.split('/')
    c = os.path.join(H, root, cid, 'ctl')
    rec = {'root': root, 'id': cid, 'cell_dir_exists': os.path.isdir(c)}
    try:
        m = json.load(open(os.path.join(c, 'agy-meter-1.json')))
        rec.update(T=m.get('T', 'UNREAD'), requested_model=m.get('requested_model', 'UNREAD'), meter_verdict=m.get('verdict', 'UNREAD'))
    except (OSError, ValueError):
        rec.update(T='UNREAD', requested_model='UNREAD', meter_verdict='UNREAD')
    try:
        t = json.load(open(os.path.join(c, 'agy-turnloop-1.json')))
        for k in ('turns_sent', 'wall_seconds', 'done_reason', 'landed', 'false_done_claims', 'client_reaped', 'rc', 'turns_no_output', 'continue_turns', 'persist_sent', 'persist_answered'):
            rec[k] = t.get(k, 'UNREAD')
    except (OSError, ValueError):
        for k in ('turns_sent', 'wall_seconds', 'done_reason', 'landed', 'false_done_claims', 'client_reaped', 'rc', 'turns_no_output', 'continue_turns', 'persist_sent', 'persist_answered'):
            rec[k] = 'UNREAD'
    try:
        rec['cut_turns'] = sum('print timeout' in l for l in open(os.path.join(c, 'agy-stderr-1.txt'), errors='replace'))
    except OSError:
        rec['cut_turns'] = 'UNREAD'
    b = kv(os.path.join(c, 'built-from.tsv'))
    for k in ('export_sha', 'problem', 'arm', 'built_at'):
        rec[k] = b.get(k, 'UNREAD')
    try:
        rec['end1'] = open(os.path.join(c, 'end-1')).readline().strip() or 'UNREAD'
    except OSError:
        rec['end1'] = 'UNREAD'
    rec['fire_first'], rec['fire_last'] = first_last_stamp(os.path.join(c, 'fire.log'))
    out.append(rec)
print(json.dumps(out))
