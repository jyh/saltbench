#!/usr/bin/env python3
# gatest_census.py OUT (run box) — signature G: inside tool_result content only, the literal 'mkdtemp failed on' followed (same match) by a
# path whose last component starts 'gatest.' — the salt-diet gate's selftest temp dir; also records whether 'gate: selftest' follows.
import os, re, glob, sys, json
home = os.path.expanduser('~'); rows = []; n = 0
G = re.compile(r"mkdtemp failed on (\S*/gatest\.[A-Za-z0-9]+)")
for d in sorted(set(glob.glob(home + '/.claude*/projects/*cells*'))):
    proj = re.sub(r'^-Users-[a-z]+-', '', os.path.basename(d))
    for f in glob.glob(d + '/*.jsonl') + glob.glob(d + '/*/subagents/*.jsonl'):
        n += 1; g = 0; sel = 0
        for line in open(f, 'rb'):
            try: r = json.loads(line)
            except Exception: continue
            m = r.get('message') if isinstance(r, dict) else None
            if not isinstance(m, dict) or not isinstance(m.get('content'), list): continue
            for b in m['content']:
                if isinstance(b, dict) and b.get('type') == 'tool_result':
                    s = json.dumps(b.get('content'))
                    for x in G.finditer(s):
                        g += 1; sel += 'gate: selftest' in s[x.end():x.end() + 200]
        if g: rows.append('%s\t%s\tG=%d\tselftest_follows=%d' % (proj, os.path.basename(f), g, sel))
open(sys.argv[1], 'w').write('project\ttranscript\tG\tselftest_follows\n' + '\n'.join(rows) + '\n')
print('transcripts', n, 'with G', len(rows))
