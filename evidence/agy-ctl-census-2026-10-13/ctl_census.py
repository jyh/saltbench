#!/usr/bin/env python3
# agy ctl/ census (the helm's order, bus @78,547,482): for every AGY-shape cell of record, did the SUBJECT write ctl/?
# Two arms, different axes: (T) every tool call in every agy transcript_full.jsonl (main + subagents) and every stream
# tool_info.parameters, searched for a reference to the cell's ctl dir; (M) mtimes of ctl files against each phase's
# subject window [mtime agy-turnloop-env-N.json, mtime agy-turnloop-N.json].
# usage: ctl_census.py cellroots.tsv   (reads ~/<root>/<cell>)
import csv, glob, json, os, re, sys, collections
def tfind(d):
    out = []
    for dp, dn, fn in os.walk(d):
        out += [os.path.join(dp, f) for f in fn if f == 'transcript_full.jsonl']
    return out
PROT = ('customer.log', 'card_extras', 'task', 'arm')
WRITE_TOOLS = re.compile(r'write|replace|edit|create|delete|move|rename', re.I)
SHELL_WRITE = re.compile(r'>(?!\s*/dev/null)(?!&)|\brm\b|\bmv\b|\bcp\b|\btouch\b|\btee\b|sed\s+-i|\bchmod\b|\btruncate\b|\bln\b|\bunlink\b|open\(.*[\'"]w', re.I)
def ctl_ref(s, cell, root):
    return bool(re.search(r'(^|[\s/\'"=])(\.\./)?ctl(/|\b)', s)) or ('/%s/ctl' % cell) in s
def calls(path, cell, root):
    out = []; calls.n = getattr(calls, 'n', 0)
    for line in open(path, errors='replace'):
        try: o = json.loads(line)
        except Exception: continue
        tcs = []
        for tc in o.get('tool_calls') or []: tcs.append((tc.get('name', '?'), tc.get('args') or {}))
        su = o.get('step_update') or {}
        ti = su.get('tool_info') or {}
        if ti.get('parameters'): tcs.append((ti.get('name') or su.get('tool_name') or '?', ti['parameters']))
        calls.n += len(tcs)
        for name, args in tcs:
            s = json.dumps(args, ensure_ascii=False)
            if ctl_ref(s, cell, root): out.append((name, s))
    return out
if sys.argv[1] == '--selftest':
    import tempfile; d = tempfile.mkdtemp(); p = d + '/t.jsonl'
    open(p, 'w').write(json.dumps({'tool_calls': [{'name': 'run_command', 'args': {'CommandLine': 'echo x > ../ctl/end-1'}}, {'name': 'write_to_file', 'args': {'TargetFile': '/home/u/R/c1/ctl/card_extras'}}, {'name': 'run_command', 'args': {'CommandLine': 'grep x ctl/* 2>/dev/null'}}]}) + '\n')
    h = calls(p, 'c1', 'R'); w = [x for x in h if WRITE_TOOLS.search(x[0]) or (re.search(r'command', x[0], re.I) and SHELL_WRITE.search(x[1]))]
    print('selftest: refs=%d writes=%d (expect 3, 2)' % (len(h), len(w))); sys.exit(0 if (len(h), len(w)) == (3, 2) else 1)
rows = [r for r in csv.DictReader((l for l in open(sys.argv[1]) if not l.startswith('#')), delimiter='\t') if r['shape'] == 'AGY']
summ = collections.Counter(); inwin = collections.Counter(); detail = []
for r in rows:
    cell, root = r['cell'], r['root']
    base = os.path.expanduser('~/%s/%s' % (root, cell)); aside = os.path.expanduser('~/%s/_aside/%s' % (root, cell))
    if not os.path.isdir(base + '/ctl'): summ['UNDECIDABLE-no-ctl'] += 1; detail.append((cell, root, 'UNDECIDABLE', 'no ctl dir')); continue
    tfiles = tfind(base + '/.agyhome') + tfind(aside)
    sfiles = glob.glob(base + '/ctl/stream-*.ndjson') + glob.glob(base + '/ctl/work-turn-*.ndjson') + glob.glob(aside + '/**/ctl/stream-*.ndjson', recursive=True)
    hits = []; calls.n = 0
    for f in tfiles + sfiles: hits += [(os.path.basename(f), n, s) for n, s in calls(f, cell, root)]
    writes = [h for h in hits if WRITE_TOOLS.search(h[1]) or (re.search(r'command', h[1], re.I) and SHELL_WRITE.search(h[2]))]
    # M arm
    flags = []
    for envf in glob.glob(base + '/ctl/agy-turnloop-env-*.json'):
        n = re.search(r'-(\d+)\.json$', envf).group(1); endf = base + '/ctl/agy-turnloop-%s.json' % n
        if not os.path.exists(endf): continue
        t0, t1 = os.path.getmtime(envf), os.path.getmtime(endf)
        for p in glob.glob(base + '/ctl/*'):
            if not os.path.isfile(p): continue
            m = os.path.getmtime(p); b = os.path.basename(p)
            if t0 < m < t1:
                inwin[re.sub(r'\d+', 'N', b)] += 1
                if b in PROT or re.match(r'end-\d+$', b): flags.append('%s@phase%s' % (b, n))
    ncalls = calls.n
    if not tfiles and not sfiles or ncalls == 0: v = 'UNDECIDABLE'; why = 'no tool call parsed (transcripts=%d streams=%d)' % (len(tfiles), len(sfiles))
    elif writes or flags: v = 'TOUCHED?'; why = 'writes=%d mtime=%s' % (len(writes), ','.join(flags) or '-')
    else: v = 'CLEAN'; why = 'transcripts=%d streams=%d calls=%d ctl-refs(read-only)=%d' % (len(tfiles), len(sfiles), ncalls, len(hits)); v = 'CLEAN-READS-CTL' if hits else 'CLEAN'
    summ[v] += 1; detail.append((cell, root, v, why))
    for h in writes[:20]: detail.append((cell, root, '  call', '%s %s %s' % (h[0], h[1], h[2][:400])))
print('# N=%d  %s' % (len(rows), ' · '.join('%s %d' % kv for kv in sorted(summ.items()))))
print('# ctl files with an mtime INSIDE a subject window (name, digits->N): ' + ' · '.join('%s %d' % kv for kv in inwin.most_common()))
for d in detail: print('\t'.join(d))
