#!/usr/bin/env python3
"""Every tool_use in the Claude cell transcripts whose name is NOT on the launched --tools list, with its tool_result
(is_error + the first 160 characters): what the client did with a call to a tool the subject was not offered."""
import glob, json, os, collections

home = os.path.expanduser('~')
SURFACE = set('Bash,Read,Edit,Write,MultiEdit,NotebookEdit,Glob,Grep,Agent,Task,TodoWrite,TaskStop'.split(','))
calls, results = {}, {}
for d in [d for d in glob.glob(home + '/.claude*/projects/*') if 'cells' in os.path.basename(d)]:
    for f in glob.glob(d + '/**/*.jsonl', recursive=True):
        for line in open(f, encoding='utf-8', errors='replace'):
            if 'tool_use' not in line and 'tool_result' not in line:
                continue
            try:
                content = (json.loads(line).get('message') or {}).get('content')
            except ValueError:
                continue
            if not isinstance(content, list):
                continue
            for c in content:
                if not isinstance(c, dict):
                    continue
                if c.get('type') == 'tool_use' and c.get('name') not in SURFACE:
                    calls[c.get('id')] = (c.get('name'), os.path.basename(d).replace('-Users-jyh-', ''))
                elif c.get('type') == 'tool_result':
                    t = c.get('content')
                    if isinstance(t, list):
                        t = ' '.join(x.get('text', '') for x in t if isinstance(x, dict))
                    results[c.get('tool_use_id')] = (bool(c.get('is_error')), str(t)[:160].replace('\n', ' '))
for tid, (name, cell) in sorted(calls.items(), key=lambda kv: kv[1]):
    r = results.get(tid)
    print('%s\t%s\t%s\t%s' % (name, 'NO-RESULT' if r is None else ('is_error' if r[0] else 'ok'), cell[-50:], r[1] if r else ''))
print('OFF-SURFACE CALLS %d' % len(calls))
