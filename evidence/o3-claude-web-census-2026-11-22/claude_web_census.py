#!/usr/bin/env python3
"""Census: Claude-lane cell transcripts on the run box, every WebSearch / WebFetch tool_use and its tool_result.
Population: every *.jsonl under ~/.claude-account-*/projects/<slug> where <slug> names a cell root (contains 'cells').
Per call: SERVED (result present, not is_error, no refusal text) / REFUSED (is_error or a permission/deny text) / NO-RESULT.
Control: the same parse counts Bash tool_use, which every cell makes; a zero there means the parser is broken."""
import glob, json, os, re, sys, collections

home = os.path.expanduser('~')
dirs = [d for d in glob.glob(home + '/.claude*/projects/*') if 'cells' in os.path.basename(d)]
WEB = {'WebSearch', 'WebFetch'}
REFUSE = re.compile(r'permission|denied|not allowed|blocked|disallowed', re.I)
calls = {}          # tool_use id -> (cell slug, tool name, file)
results = {}        # tool_use id -> (is_error, text)
bash_n = 0
files = 0
for d in dirs:
    for f in glob.glob(d + '/**/*.jsonl', recursive=True):
        files += 1
        try:
            fh = open(f, encoding='utf-8', errors='replace')
        except OSError:
            continue
        for line in fh:
            if 'tool_use' not in line and 'tool_result' not in line:
                continue
            try:
                rec = json.loads(line)
            except ValueError:
                continue
            msg = rec.get('message') or {}
            content = msg.get('content')
            if not isinstance(content, list):
                continue
            for c in content:
                if not isinstance(c, dict):
                    continue
                if c.get('type') == 'tool_use':
                    if c.get('name') == 'Bash':
                        bash_n += 1
                    if c.get('name') in WEB:
                        calls[c.get('id')] = (os.path.basename(d), c.get('name'), f)
                elif c.get('type') == 'tool_result':
                    t = c.get('content')
                    if isinstance(t, list):
                        t = ' '.join(x.get('text', '') for x in t if isinstance(x, dict))
                    results[c.get('tool_use_id')] = (bool(c.get('is_error')), str(t)[:300])
print('cell project dirs %d · transcript files %d · control Bash tool_use %d' % (len(dirs), files, bash_n))
tally = collections.Counter()
for tid, (cell, name, f) in calls.items():
    r = results.get(tid)
    if r is None:
        v = 'NO-RESULT'
    elif r[0] or REFUSE.search(r[1]):
        v = 'REFUSED'
    else:
        v = 'SERVED'
    tally[(name, v)] += 1
    print('%s\t%s\t%s\t%s' % (v, name, cell[-60:], (r[1] if r else '')[:160].replace('\n', ' ')))
print('WEB CALLS %d · %s' % (len(calls), dict(tally)))
