#!/usr/bin/env python3
"""Join: each Claude cell transcript directory (the web census's population) to a recorded launch ARGV for the same cell id.
Cell id = the slug's last '-'-token before '-repo' (the cell's own directory name). Classes: ARGV-FOUND (and its web surface
class) / NO-ARGV (no launch.log line names this id). Control: the number of transcript dirs equals the web census's 748."""
import glob, os, re, collections, sys

home = os.path.expanduser('~')
ARGV = re.compile(r'\bARGV (\S+) phase (\S+): (.*)$')
surf = collections.defaultdict(set)
for f in glob.glob(home + '/cells*/**/ctl/launch.log', recursive=True):
    for line in open(f, encoding='utf-8', errors='replace'):
        m = ARGV.search(line)
        if not m:
            continue
        cid, _, rest = m.groups()
        tm = re.search(r'--tools (\S+)', rest)
        if tm is None:
            surf[cid].add('NO-TOOLS-FLAG')
        elif any(w in tm.group(1).split(',') for w in ('WebSearch', 'WebFetch')):
            surf[cid].add('WEB-OFFERED')
        else:
            surf[cid].add('WEB-NOT-OFFERED')
dirs = [d for d in glob.glob(home + '/.claude*/projects/*') if 'cells' in os.path.basename(d)]
t = collections.Counter()
missing = []
for d in dirs:
    b = os.path.basename(d)
    m = re.search(r'-([^-]+)-repo$', b)
    cid = m.group(1) if m else None
    if cid and cid in surf:
        t['ARGV-FOUND ' + '+'.join(sorted(surf[cid]))] += 1
    else:
        t['NO-ARGV'] += 1
        missing.append(b.replace('-Users-jyh-', ''))
print('transcript dirs %d · cell ids with an ARGV line %d' % (len(dirs), len(surf)))
for k, v in sorted(t.items(), key=lambda kv: -kv[1]):
    print('%6d  %s' % (v, k))
fams = collections.Counter(re.sub(r'-[^-]+-repo$', '', x) for x in missing)
for k, v in fams.most_common():
    print('   NO-ARGV family %4d  %s' % (v, k))
