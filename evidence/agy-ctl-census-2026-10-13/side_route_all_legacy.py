#!/usr/bin/env python3
# Extends the 2026-09-16 level-5 P-DELIVERY ordering census (desk PW: routes ctl/launch.log + ctl/briefing-nonce) to EVERY
# legacy-layout agy cell of record (ctl/briefing-nonce present), s3 and b4 included. Per cell, over every transcript_full.jsonl
# conversation: first tool-call step naming the arm file, and first naming a side route. A cell is UNSUPPORTED when a side route
# comes before any arm-file touch in the conversation that carries the receipt request. Run on the run box.
# usage: side_route_all_legacy.py cellroots.tsv
import csv, json, os, re, sys, collections
ARM = re.compile(r'repo/(AGENTS|CLAUDE)\.md|AGENTS\.md')
SIDE = re.compile(r'briefing-nonce|launch\.log|ARMRECV')
rows = [r for r in csv.DictReader((l for l in open(sys.argv[1]) if not l.startswith('#')), delimiter='\t') if r['shape'] == 'AGY']
summ = collections.Counter()
for r in rows:
    base = os.path.expanduser('~/%s/%s' % (r['root'], r['cell']))
    if not os.path.exists(base + '/ctl/briefing-nonce'): continue
    level = r['cell'][:2]; best = None
    for dp, dn, fn in os.walk(base + '/.agyhome'):
        if 'transcript_full.jsonl' not in fn: continue
        arm = side = None; receipt_conv = False
        for i, l in enumerate(open(os.path.join(dp, 'transcript_full.jsonl'), errors='replace')):
            try: o = json.loads(l)
            except Exception: continue
            if i == 0 and 'Receipt' in str(o.get('content') or ''): receipt_conv = True
            for t in o.get('tool_calls') or []:
                a = json.dumps(t.get('args') or {})
                if arm is None and ARM.search(a): arm = i
                if side is None and SIDE.search(a): side = i
        if not receipt_conv: continue
        v = 'NO-SIDE' if side is None else ('ARM-FIRST' if arm is not None and arm < side else 'UNSUPPORTED')
        best = (v, dp.split('brain/')[1][:8], arm, side)
    if best is None: v = 'NO-RECEIPT-CONVERSATION'; best = (v, '-', None, None)
    summ[(level, best[0])] += 1
    if best[0] != 'NO-SIDE': print(r['cell'], r['root'], *best)
print('# legacy-layout cells:', sum(summ.values()), ' · '.join('%s %s %d' % (k[0], k[1], n) for k, n in sorted(summ.items())))
