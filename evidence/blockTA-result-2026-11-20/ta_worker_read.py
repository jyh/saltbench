#!/usr/bin/env python3
"""ta_worker_read.py — read-only, run on the run box from $HOME. For each swarm worker a TA cell's subject added (the ids are the
`conversation_id`s in its main stream's swarm `add` outputs, swarm.tsv's population), read the worker's OWN record, which the client keeps
in the cell's agy home: <cell>/.agyhome/.gemini/antigravity-cli/brain/<worker id>/.system_generated/logs/transcript_full.jsonl
(transcript.jsonl when the _full file is absent). Per worker: the window (first and last created_at), the models its responses carry,
token sums, every tool call by name with its path/command argument cut to 100 chars, and any error. Every tool-call argument
naming the solution or a non-test source file is printed in context (a READ and a WRITE are told apart by the reader, not by this
script). Then the cell's repo commits inside each worker window (`git log` in <cell>/repo), and the files the final tree carries under
tests/refute and docs/reviews (the workers' write targets) with the commit that added each.
A worker whose record is absent prints ABSENT with the paths looked at. Paths are printed relative to $HOME.
usage: python3 -I ta_worker_read.py <root>/<id> ..."""
import json, os, re, subprocess, sys

H = os.path.expanduser('~')
ARGKEYS = ('Path', 'TargetFile', 'AbsolutePath', 'path', 'file_path', 'CommandLine', 'command', 'Cwd', 'SearchPath', 'Query', 'action', 'Url')


def workers(cell):
    out = []
    for line in open(os.path.join(H, cell, 'ctl', 'stream-1.ndjson'), errors='replace'):
        try:
            e = json.loads(line)
        except ValueError:
            continue
        su = e.get('step_update') or {}
        ti = su.get('tool_info') or {}
        if su.get('tool_name') == 'swarm' and su.get('state') == 'DONE' and (ti.get('parameters') or {}).get('action') == 'add':
            o = ti.get('output') or ''
            try:
                d = json.loads(o[o.find('{'):])
                out.append((d.get('name'), d.get('model'), d.get('conversation_id')))
            except ValueError:
                out.append(('UNREAD', 'UNREAD', None))
    return out


for cell in sys.argv[1:]:
    print('== %s' % cell)
    for name, model, wid in workers(cell):
        base = os.path.join(H, cell, '.agyhome', '.gemini', 'antigravity-cli', 'brain', str(wid), '.system_generated', 'logs')
        f = next((os.path.join(base, n) for n in ('transcript_full.jsonl', 'transcript.jsonl') if os.path.isfile(os.path.join(base, n))), None)
        if not f:
            print('  worker %s (%s) %s: ABSENT, looked in %s' % (name, model, wid, base.replace(H, '~')))
            continue
        recs = []
        for l in open(f, errors='replace'):
            try:
                recs.append(json.loads(l))
            except ValueError:
                pass
        ts = sorted(r.get('created_at') for r in recs if r.get('created_at'))
        models = sorted({r.get('model') for r in recs if r.get('model')})
        tok = {k: sum(int(r.get(k) or 0) for r in recs) for k in ('input_tokens', 'cache_read_tokens', 'output_tokens')}
        print('  worker %s requested %s id %s · record %s · %d records · window %s .. %s · response models %s · tokens %s' % (
            name, model, wid[:8], os.path.relpath(f, H)[-60:], len(recs), ts[0] if ts else '?', ts[-1] if ts else '?', models, tok))
        for r in recs:
            for tc in r.get('tool_calls') or []:
                nm = tc.get('name') or tc.get('tool_name') or '?'
                a = tc.get('args') or tc.get('arguments') or tc.get('input') or {}
                if isinstance(a, str):
                    try:
                        a = json.loads(a)
                    except ValueError:
                        a = {'raw': a}
                arg = ' '.join('%s=%s' % (k, str(a[k]).replace('\n', ' ')[:100]) for k in ARGKEYS if k in a) or str(sorted(a))[:100]
                print('    step %s %s: %s' % (r.get('step_index'), nm, arg.replace(H, '~')))
            if r.get('error'):
                print('    step %s ERROR %s' % (r.get('step_index'), str(r.get('error')).replace(H, '~').replace('\n', ' ')[:160]))
            for tc in r.get('tool_calls') or []:   # every argument naming the solution or a non-test source file, in full context
                a = json.dumps(tc.get('args') or tc.get('arguments') or tc.get('input') or {})
                for m in re.finditer(r'(solution\.rs|src/[A-Za-z_]+\.rs|interface\.rs|LANDING[A-Za-z_.]*)', a):
                    print('    step %s SOURCE-PATH MENTION: %s' % (r.get('step_index'), a[max(0, m.start() - 70):m.end() + 15].replace(H, '~').replace('\\n', ' ')))
        if ts:
            g = subprocess.run(['git', '-C', os.path.join(H, cell, 'repo'), 'log', '--all', '--format=%cI %an %s',
                                '--since=' + ts[0], '--until=' + ts[-1]], capture_output=True, text=True)
            print('    repo commits inside the window: %d%s' % (len(g.stdout.splitlines()), ''.join('\n      ' + x for x in g.stdout.splitlines()[:5])))
    # what the cell's final tree carries under tests/refute (the workers' write target) and the commits that first added each file
    rp = os.path.join(H, cell, 'repo')
    ls = subprocess.run(['git', '-C', rp, 'ls-tree', '-r', '--name-only', 'HEAD', '--', 'tests/refute'], capture_output=True, text=True).stdout.split()
    ls += subprocess.run(['git', '-C', rp, 'ls-tree', '-r', '--name-only', 'HEAD', '--', 'docs/reviews'], capture_output=True, text=True).stdout.split()
    for fn in ls:
        a = subprocess.run(['git', '-C', rp, 'log', '--diff-filter=A', '--format=%cI %an %h', '--', fn], capture_output=True, text=True).stdout.strip()
        print('  final tree carries %s, added by commit %s' % (fn, a or 'UNREAD'))
    if not ls:
        print('  final tree carries nothing under tests/refute or docs/reviews')
