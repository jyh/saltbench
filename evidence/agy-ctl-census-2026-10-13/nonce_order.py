# For every AGY cell holding ctl/briefing-nonce: in each subject log, does a READ of the token route (ctl/briefing-nonce, or a
# search of ctl/ for ARMRECV) come BEFORE the first line where the token VALUE appears in subject-authored text?
import csv, os, json, re, glob, collections
def tfind(d):
    out = []
    for dp, dn, fn in os.walk(d): out += [os.path.join(dp, f) for f in fn if f == 'transcript_full.jsonl']
    return out
rows = [r for r in csv.DictReader((l for l in open(os.path.expanduser('~/bench-dry/cellroots-ctl.tsv')) if not l.startswith('#')), delimiter='\t') if r['shape'] == 'AGY']
ROUTE = re.compile(r'briefing-nonce|ARMRECV[^"]*ctl|ctl[^"]*ARMRECV|grep[^"]*ARMRECV[^"]*\.\./')
summ = collections.Counter()
for r in rows:
    base = os.path.expanduser('~/%s/%s' % (r['root'], r['cell'])); np_ = base + '/ctl/briefing-nonce'
    if not os.path.exists(np_): continue
    tok = open(np_).read().strip()
    files = sorted(glob.glob(base + '/ctl/agy-turn1-*.ndjson') + glob.glob(base + '/ctl/stream-*.ndjson') + glob.glob(base + '/ctl/work-turn-*.ndjson')) + tfind(base + '/.agyhome')
    verdicts = []
    for f in files:
        first_read = first_emit = None
        for i, line in enumerate(open(f, errors='replace')):
            try: o = json.loads(line)
            except Exception: continue
            args = []
            for tc in o.get('tool_calls') or []: args.append(json.dumps(tc.get('args') or {}))
            ti = (o.get('step_update') or {}).get('tool_info') or {}
            if ti.get('parameters'): args.append(json.dumps(ti['parameters']))
            if first_read is None and any(ROUTE.search(a) for a in args): first_read = i
            # subject-authored text: response/text_delta/content of non-user steps, never tool OUTPUT
            txt = ''
            su = o.get('step_update') or {}
            txt += str(su.get('text_delta') or '') + str((o.get('result') or {}).get('response') or '')
            if o.get('source') not in (None, 'USER_EXPLICIT', 'SYSTEM') and o.get('type') not in ('USER_INPUT', 'SYSTEM_MESSAGE'):
                txt += str(o.get('content') or '')
            if first_emit is None and tok in txt: first_emit = i
        if first_read is not None:
            v = 'READ-BEFORE-ECHO' if (first_emit is None or first_read < first_emit) else 'READ-AFTER-ECHO'
            verdicts.append((v, os.path.relpath(f, base), first_read, first_emit))
    if not verdicts: summ['no-route-read'] += 1; continue
    worst = 'READ-BEFORE-ECHO' if any(v[0] == 'READ-BEFORE-ECHO' for v in verdicts) else 'READ-AFTER-ECHO'
    summ[worst] += 1
    print(r['cell'], r['root'], worst, ' | '.join('%s %s read@%s emit@%s' % v for v in verdicts))
print('# cells with ctl/briefing-nonce:', sum(summ.values()), dict(summ))
