#!/usr/bin/env python3
# claude_tmp_census3.py OUT (run box) — as census2, but each signature is searched ONLY inside tool_result content (what a command
# printed back to the subject), never in system prompts, tool descriptions or the model's own text.
import os, re, glob, sys, json
home = os.path.expanduser('~'); rows = []; n = 0; nres = 0
def texts(c):
    if isinstance(c, str): yield c
    elif isinstance(c, list):
        for x in c:
            if isinstance(x, dict):
                if x.get('type') == 'text': yield x.get('text', '')
                elif 'content' in x: yield from texts(x['content'])
for d in sorted(set(glob.glob(home + '/.claude*/projects/*cells*'))):
    proj = os.path.basename(d); cfg = d.split('/')[3]
    for f in glob.glob(d + '/*.jsonl') + glob.glob(d + '/*/subagents/*.jsonl'):
        n += 1; A = B = C = False; k = 0
        for line in open(f, 'rb'):
            try: r = json.loads(line)
            except Exception: continue
            m = r.get('message') if isinstance(r, dict) else None
            if not isinstance(m, dict) or not isinstance(m.get('content'), list): continue
            for blk in m['content']:
                if not (isinstance(blk, dict) and blk.get('type') == 'tool_result'): continue
                k += 1
                for t in texts(blk.get('content')):
                    if not A: A = any('not permitted' in t[max(0, x.start()-200):x.end()+200].lower() for x in re.finditer(r'/tmp/claude', t))
                    Bm = re.findall(r"(?:mkdtemp failed on|can't create temp)[^\n]{0,120}", t)
                    if Bm: B = True; C = C or any(('/tmp/claude' in y) or ('/tmp/gate' in y) for y in Bm)
        nres += k
        if A or B: rows.append('%s\t%s\t%s\tA=%d\tB=%d\tC=%d' % (cfg, proj, f.split('/projects/')[1], A, B, C))
open(sys.argv[1], 'w').write('cfg\tproject\ttranscript\tA\tB\tC\n' + '\n'.join(rows) + '\n')
print('transcripts', n, 'tool_results read', nres, 'with any signature', len(rows))
