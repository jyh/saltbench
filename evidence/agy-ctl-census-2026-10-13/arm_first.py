#!/usr/bin/env python3
# For each cell nonce_order.py lists, in every transcript_full.jsonl conversation: the step of the first tool call naming the arm
# file (repo/AGENTS.md or repo/CLAUDE.md) and of the first naming the token route (briefing-nonce or ARMRECV). Run on the run box.
# usage: arm_first.py nonce-order.out
import json, os, re, sys
for line in open(sys.argv[1]):
    if line.startswith('#') or not line.strip(): continue
    cell, root = line.split()[:2]
    for dp, dn, fn in os.walk(os.path.expanduser('~/%s/%s/.agyhome' % (root, cell))):
        if 'transcript_full.jsonl' not in fn: continue
        arm = route = None
        for i, l in enumerate(open(os.path.join(dp, 'transcript_full.jsonl'))):
            o = json.loads(l)
            for t in o.get('tool_calls') or []:
                a = json.dumps(t.get('args') or {})
                if arm is None and re.search(r'repo/(AGENTS|CLAUDE)\.md', a): arm = i
                if route is None and re.search(r'briefing-nonce|ARMRECV', a): route = i
        if route is not None:
            conv = dp.split('brain/')[1][:8]
            print(cell, root, conv, 'arm@%s' % arm, 'route@%s' % route, 'ARM-FIRST' if arm is not None and arm < route else 'ROUTE-FIRST')
