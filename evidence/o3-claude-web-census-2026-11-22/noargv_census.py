#!/usr/bin/env python3
"""The launch.log files with NO `ARGV` line: classify each by its cell's ctl/client (claude / agy / absent) and by whether
the log shows a launch at all (LAUNCHING), so the ARGV census's population gap is named, not assumed."""
import glob, os, re, collections

home = os.path.expanduser('~')
logs = sorted(set(glob.glob(home + '/cells*/**/ctl/launch.log', recursive=True)))
t = collections.Counter()
examples = collections.defaultdict(list)
for f in logs:
    s = open(f, encoding='utf-8', errors='replace').read()
    if re.search(r'\bARGV \S+ phase \S+: ', s):
        continue
    ctl = os.path.dirname(f)
    try:
        client = open(os.path.join(ctl, 'client')).read().split()[0]
    except (OSError, IndexError):
        client = 'NO-CLIENT-FILE'
    launched = 'LAUNCHING' in s
    stub = 'claude-stub' in s
    k = (client, 'launched' if launched else 'not-launched', 'stub' if stub else '-')
    t[k] += 1
    if len(examples[k]) < 2:
        examples[k].append(f.replace(home, '~'))
print('launch.log without ARGV: %d' % sum(t.values()))
for k, v in sorted(t.items(), key=lambda kv: -kv[1]):
    print('%6d  %s   e.g. %s' % (v, ' · '.join(k), ' | '.join(examples[k])))
