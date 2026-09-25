"""Per cell and phase: T (agy-meter-N.json), wall/turns/done_reason/rc/landed (agy-turnloop-N.json).
Reads ctl/ first, then <root>/_aside/<id>/phase1/ (the aside moves phase 1's files there, §M1 F2). Prints the source used."""
import json, os, sys, glob
H = os.path.expanduser('~')
out = []
for cid in sys.argv[1:]:
    hits = glob.glob(os.path.join(H, 'cells-l8-*', cid))
    if len(hits) != 1:
        out.append({'id': cid, 'phase': 0, 'error': 'cell dirs found: %d' % len(hits)}); continue
    root = os.path.basename(os.path.dirname(hits[0]))
    for ph in (1, 2):
        rec = {'id': cid, 'phase': ph}
        for kind in ('meter', 'turnloop'):
            cands = [os.path.join(H, root, cid, 'ctl', 'agy-%s-%d.json' % (kind, ph)),
                     *glob.glob(os.path.join(H, root, '_aside', cid, 'phase%d' % ph, '**', 'agy-%s-%d.json' % (kind, ph)), recursive=True)]
            f = next((c for c in cands if os.path.exists(c)), None)
            rec[kind + '_src'] = os.path.relpath(f, H) if f else 'UNREAD'
            if f:
                j = json.load(open(f))
                if kind == 'meter':
                    rec['T'] = j.get('T', 'UNREAD')
                else:
                    for k in ('wall_seconds', 'turns_sent', 'done_reason', 'rc', 'landed', 'persist_sent', 'false_done_claims'):
                        rec[k] = j.get(k, 'UNREAD')
        out.append(rec)
print(json.dumps(out))
