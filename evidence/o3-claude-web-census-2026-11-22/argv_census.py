#!/usr/bin/env python3
"""Census of the Claude-lane tool surface as LAUNCHED: every `ARGV <id> phase N:` line in every ctl/launch.log under the
run box's cells roots. Per launch: is WebSearch / WebFetch in --tools (offered), in --disallowedTools (struck), is
--tools present at all, is --settings <fence> present. Control: count of ARGV lines and of launch.log files read.
A launch line with no --tools flag offers the client's DEFAULT surface, which includes the web tools; it is its own class."""
import glob, os, re, shlex, collections, sys

home = os.path.expanduser('~')
logs = sorted(set(glob.glob(home + '/cells*/**/ctl/launch.log', recursive=True)))
ARGV = re.compile(r'\bARGV (\S+) phase (\S+): (.*)$')
WEB = ('WebSearch', 'WebFetch')
tally = collections.Counter()
rows = []
nlines = 0
for f in logs:
    try:
        text = open(f, encoding='utf-8', errors='replace').read().splitlines()
    except OSError:
        tally['UNREADABLE-LOG'] += 1
        continue
    for line in text:
        m = ARGV.search(line)
        if not m:
            continue
        nlines += 1
        cid, phase, rest = m.groups()
        try:
            argv = shlex.split(rest)
        except ValueError:
            argv = rest.split()
        def val(flag):
            for i, a in enumerate(argv):
                if a == flag and i + 1 < len(argv):
                    return argv[i + 1]
                if a.startswith(flag + '='):
                    return a.split('=', 1)[1]
            return None
        tools, dis = val('--tools'), val('--disallowedTools')
        fence = val('--settings')
        offered = None if tools is None else [w for w in WEB if w in tools.split(',')]
        struck = [] if dis is None else [w for w in WEB if w in dis.split(',')]
        if tools is None:
            cls = 'NO-TOOLS-FLAG'
        elif offered:
            cls = 'WEB-OFFERED'
        else:
            cls = 'WEB-NOT-OFFERED'
        key = (cls, 'struck=' + '+'.join(struck) if struck else 'struck=none', 'fence' if fence else 'no-fence',
               'skip-perms' if '--dangerously-skip-permissions' in argv else 'no-skip')
        tally[key] += 1
        rows.append('\t'.join([cls, cid, phase, '+'.join(struck) or '-', 'fence' if fence else '-']))
print('launch.log files %d · ARGV lines %d' % (len(logs), nlines))
for k, v in sorted(tally.items(), key=lambda kv: -kv[1]):
    print('%6d  %s' % (v, ' · '.join(k) if isinstance(k, tuple) else k))
if len(sys.argv) > 1:
    open(sys.argv[1], 'w').write('class\tcell\tphase\tstruck\tfence\n' + '\n'.join(rows) + '\n')
