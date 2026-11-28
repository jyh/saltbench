#!/usr/bin/env python3
"""names_lines.py CTL_CENSUS_PY JOIN CENSUS: read-only probe for kent's FINDING 1 on #474. For every OTHER-RECORD
call, print each RESULT line that names an outside literal path and is NOT classed CONTENT by other_seen.py's rule,
with the call's tool name, so the line shapes (grep form, view_file header, listing) can be read. Also prints, per cell,
the lines whose first token starts with '/' and holds a space or ':' before its ':<digits>:' (kent's two shapes)."""
import collections, importlib.util, json, os, re, sys
H = os.path.expanduser('~')
spec = importlib.util.spec_from_file_location('cc', sys.argv[1]); cc = importlib.util.module_from_spec(spec); spec.loader.exec_module(cc)
DEN = re.compile(r'Operation not permitted|Permission denied|permission check failed|denied permission|BLOCKED')
OLD = lambda line: re.search(r'File Path: `file://([^`]+)`', line) or re.match(r'\s*(/[^:\s]+):\d*:?\s*\S', line)
fams = {}
for l in open(sys.argv[2]):
    if l.startswith('#') or not l.strip(): continue
    f = l.rstrip('\n').split('\t'); fams[f[1]] = [os.path.join(H, x, f[1]) for x in f[5].split(',') if x and x != '-']
rows = [l.rstrip('\n').split('\t') for l in open(sys.argv[3]) if not l.startswith('#')]
shapes = collections.Counter()
for r in rows:
    cid, state = r[1], r[5]
    if 'OTHER-RECORD' not in state: continue
    cells = fams[cid]
    for c in cells:
        for d in (c, os.path.join(os.path.dirname(c), '_aside', cid)):
            for p in cc.walk_transcripts(d):
                recs = []
                for raw in open(p, 'rb'):
                    try: recs.append(json.loads(raw.decode('utf-8', 'replace')))
                    except Exception: recs.append(None)
                for i, rec in enumerate(recs):
                    if not isinstance(rec, dict): continue
                    for tc in rec.get('tool_calls') or []:
                        n, par, outs, oth, til = cc.classify_call(tc, cells if len(cells) > 1 else c, H)
                        if not oth: continue
                        name = tc.get('name') or (tc.get('function') or {}).get('name') or '?'
                        res = ''
                        for r2 in recs[i + 1:i + 4]:
                            if isinstance(r2, dict) and r2.get('type') == 'GENERIC':
                                res = str(r2.get('content'))[:200000]; break
                        for line in re.split(r'\r?\n', res):
                            o = [p2 for p2, lit in cc.home_paths(line, H) if lit and cc.is_outside(p2, cells, H) and cc.is_other_record(p2, H)]
                            if not o or DEN.search(line): continue
                            m = OLD(line)
                            src = m.group(1) if m else None
                            ok = bool(src) and src.startswith(H + '/') and cc.is_outside(src, cells, H) and cc.is_other_record(src, H)
                            if ok: continue
                            s = line.lstrip()
                            kshape = ''
                            if s.startswith('/'):
                                mm = re.match(r'(/.+?):(\d+):', s)
                                if mm and (' ' in mm.group(1) or ':' in mm.group(1)): kshape = 'KENT-SHAPE'
                            shapes[(name, 'starts/' if s.startswith('/') else 'other', kshape)] += 1
                            print('%s\t%s\t%s\t%s' % (cid, name, kshape or '-', line.replace(H, '~')[:220]))
print('#SHAPES ' + ' · '.join('%s|%s|%s=%d' % (k + (v,)) for k, v in sorted(shapes.items())))
