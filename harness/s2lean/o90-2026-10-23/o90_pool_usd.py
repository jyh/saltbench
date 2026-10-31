#!/usr/bin/env python3
"""o90_pool_usd.py CONFIG_DIR T0 T1 -> API-equivalent USD of every billed request in CONFIG_DIR/projects/**/*.jsonl with timestamp in (T0,T1] (UTC ISO).
Dedupe by requestId GLOBALLY (largest output observation kept). Prices: claude-api skill table (cached 2026-10-06);
cache-write 5m = 1.25x input, 1h = 2x input. Unknown models are counted apart, never priced."""
import json, sys, glob, os, collections
P = {'claude-opus-5': (5, 25, .50), 'claude-opus-5-5': (4, 20, .20), 'claude-fable-5-1': (10, 50, .25),
     'claude-fable-5': (10, 50, 1.0), 'claude-sonnet-5-5': (2, 10, .20), 'claude-sonnet-5': (2, 10, .20), 'claude-haiku-5-5': (.10, .50, .01)}
root, t0, t1 = sys.argv[1], sys.argv[2], sys.argv[3]
best = {}
files = glob.glob(os.path.join(root, 'projects', '**', '*.jsonl'), recursive=True)
for f in files:
    for line in open(f, errors='replace'):
        if '"usage"' not in line: continue
        try: d = json.loads(line)
        except ValueError: continue
        m = d.get('message') or {}
        u = m.get('usage'); ts = d.get('timestamp', '')
        if not u or not (t0 < ts <= t1): continue
        rid = d.get('requestId') or m.get('id') or line[:80]
        k = (u.get('output_tokens') or 0)
        if rid not in best or k > best[rid][0]: best[rid] = (k, m.get('model'), u)
usd = collections.Counter(); unk = collections.Counter(); n = collections.Counter()
for k, model, u in best.values():
    if model not in P: unk[model] += 1; continue
    i, o, cr = P[model]
    cc = u.get('cache_creation') or {}
    w1h = cc.get('ephemeral_1h_input_tokens'); w5 = cc.get('ephemeral_5m_input_tokens')
    if w1h is None and w5 is None: w5, w1h = u.get('cache_creation_input_tokens') or 0, 0
    c = ((u.get('input_tokens') or 0) * i + (u.get('output_tokens') or 0) * o + (w5 or 0) * i * 1.25 + (w1h or 0) * i * 2
         + (u.get('cache_read_input_tokens') or 0) * cr) / 1e6
    usd[model] += c; n[model] += 1
print('files %d requests %d' % (len(files), len(best)))
for mdl in sorted(usd): print('%-20s n=%6d usd=%10.4f' % (mdl, n[mdl], usd[mdl]))
print('TOTAL usd=%.4f' % sum(usd.values()))
if unk: print('UNPRICED', dict(unk))
