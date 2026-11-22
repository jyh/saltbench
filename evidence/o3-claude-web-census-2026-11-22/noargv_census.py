#!/usr/bin/env python3
"""The launch.log files with NO `ARGV` line: classify each by its cell's ctl/client (claude / agy / absent) and by whether
the log shows a launch at all (LAUNCHING), so the ARGV census's population gap is named, not assumed. Each class prints its root-family split (the cells root's
first path component, with the cell's own directory when it sits in the shared pilot root `cells`)."""
import glob, os, re, collections

def re_family(x):
    """Collapse rerun/aside suffixes so a family prints once: cells-l8-lzw-pro-salt-sc-rerun -> cells-l8."""
    m = re.match(r'(cells-l8zf|cells-l8)-', x)
    return m.group(1) if m else x

home = os.path.expanduser('~')
logs = sorted(set(glob.glob(home + '/cells*/**/ctl/launch.log', recursive=True)))
t = collections.Counter()
fam = collections.defaultdict(collections.Counter)
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
    parts = os.path.relpath(f, home).split(os.sep)
    family = parts[0] if parts[0] != 'cells' else '/'.join(parts[:-2])
    fam[k][re_family(family)] += 1
print('launch.log without ARGV: %d' % sum(t.values()))
for k, v in sorted(t.items(), key=lambda kv: -kv[1]):
    print('%6d  %s' % (v, ' · '.join(k)))
    for name, n in fam[k].most_common():
        print('          %5d  %s' % (n, name))
