#!/usr/bin/env python3
"""ctl_census.py: a read-only census of agy subjects' tool calls that NAME the cell's harness directory ctl/.

The data is the brain transcript, the client's own conversation record, as for the web census
(evidence/o37-agy-web-served-2026-11-20/):
  <cell>/.agyhome/.gemini/antigravity-cli/brain/<conversation>/.system_generated/logs/transcript_full.jsonl
One tool call is one entry in a record's `tool_calls` list.

WHAT COUNTS AS NAMING ctl/. A call counts when one of its PATH-ROLE arguments, or its command line, has a path
component equal to `ctl`. The path-role arguments are the keys matching path|file|dir|uri|url|target|cwd, so
`read_file Path=<cell>/ctl/x` counts, and so does `list_dir DirectoryPath=../ctl`. In a command line a token counts
when it reads `ctl`, `ctl/…`, `../ctl…` or `…/ctl/…`. Written CONTENT never counts: a write_file whose body says
"ctl" names nothing, and naaefs01's LANDING.md is the case that showed it.

WHAT IT CANNOT SEE (printed in the trailer, beside every verdict):
  a call that reaches ctl/ WITHOUT naming it. A recursive grep or ls from the cell root does that, for example
  `grep -r X ..` from repo/. Such calls are counted separately as PARENT-REACH: a path argument or command token that
  is `..`, or ends in `/..`, or is the cell directory itself. They are a candidate list for a reader and never a
  CTL-READ. So NONE-NAMED is a LOWER BOUND on contact with ctl/. It does not mean "never touched".

STATES per cell of record:
  CTL-NAMED    >= 1 call names ctl/ (each one is printed in the hits file, to be read)
  NONE-NAMED   >= 1 transcript read, 0 calls name ctl/
  UNMEASURED   no transcript, or no cell directory. Never printed as 0.

usage:
  python3 -I ctl_census.py --join JOIN.tsv --home DIR --out CENSUS.tsv --hits HITS.tsv
      JOIN.tsv is the web census's join.tsv: block id model arm how root ... A cell is <home>/<root>/<id>.
  python3 -I ctl_census.py --cells DIR...   (an ad-hoc list; it prints rows to stdout)
  python3 -I ctl_census.py --selftest       (planted fixtures, each arm must land in its own state)
Read-only on the cells. It writes only --out and --hits.
"""
import glob, json, os, re, sys, tempfile

PATH_KEY = re.compile(r'path|file|dir|uri|url|target|cwd', re.I)
CONTENT_KEY = re.compile(r'content|code|text|body|replacement|instruction|summary|query|pattern', re.I)
# a token boundary in a command line: start, whitespace, quote, = : ( ; | & < >
CMD_CTL = re.compile(r'''(?:^|[\s'"=:(;|&<>])(?:[^\s'"=:(;|&<>]*/)?ctl(?=$|[/\s'"=:);|&<>])''')
CMD_PARENT = re.compile(r'''(?:^|[\s'"=:(;|&<>])(?:\.\.|[^\s'"=:(;|&<>]*/\.\.)(?=$|/?[\s'"=:);|&<>]|/?$)''')
TRANSCRIPT = os.path.join('.agyhome', '.gemini', 'antigravity-cli', 'brain', '*', '.system_generated', 'logs',
                          'transcript_full.jsonl')


def strval(v):
    if isinstance(v, str):
        # some clients double-encode an argument as a JSON string
        s = v
        if len(s) >= 2 and s[0] == '"' and s[-1] == '"':
            try:
                s2 = json.loads(s)
                if isinstance(s2, str):
                    s = s2
            except Exception:
                pass
        return s
    return json.dumps(v)


def path_names_ctl(p, cell):
    parts = [x for x in re.split(r'[/\\]', p) if x]
    return 'ctl' in parts


def path_is_parent(p, cell):
    q = p.rstrip('/')
    if q == '..' or q.endswith('/..'):
        return True
    return any(c is not None and os.path.normpath(q) == os.path.normpath(c)
               for c in (cell if isinstance(cell, list) else [cell]))


# OUTSIDE: a path under $HOME that is not inside this cell. The toolchain stores a build legitimately reads are excepted.
TOOLCHAIN = {'.cargo', '.rustup', '.elan', '.cache', '.local', '.npm', '.gradle', '.m2', '.opam', 'verus-pin', '.verus', '.vargo'}


def home_paths(s, home):
    """every path in s rooted at the box home -> [(resolved path, literal)]. literal=True: the box home written out, which
    is unambiguous. literal=False: ~ / $HOME / ${HOME}, resolved AS IF the subject's HOME were the box home. That reading is
    not fixed by the record: the subject's HOME was <cell>/.agyhome in some eras and clients and the box home in others
    (measured 11-25: env output of taafs101 and zfafbss201 vs l8rfss03's `find ~`), so a tilde path never sets OTHER-RECORD."""
    if not home:
        return []
    h = home.rstrip('/')
    tail = r'(?=$|[/\s\'";|&<>)])(/[^\s\'";|&<>)`*]*)?'
    out = [(h + (m.group(1) or ''), True) for m in re.finditer(re.escape(h) + tail, s)]
    out += [(h + (m.group(1) or ''), False) for m in re.finditer(r'(?:(?<![\w./-])~|\$\{?HOME\}?)' + tail, s)]
    return out


TOOLCHAIN_PREFIX = ('bench-src/cargo-root',)   # the cells' vstd/cargo source root, a build input


def is_outside(p, cell, home):
    """`cell` is one directory or a list: a record held in several families (a copied cell) is inside ANY of them"""
    h = home.rstrip('/')
    q = os.path.normpath(p)
    for c in (cell if isinstance(cell, list) else [cell]):
        if c and (q == os.path.normpath(c) or q.startswith(os.path.normpath(c) + os.sep)):
            return False
    rest = q[len(h):].lstrip('/')
    if rest.split('/')[0] in TOOLCHAIN or rest.startswith(TOOLCHAIN_PREFIX):
        return False
    return True


def is_other_record(p, home):
    """an OUTSIDE path that is not $HOME itself and not a dotfile/dot-dir: another cell, a preserved or evidence
    tree, a project checkout. HOME-ENV is the rest (ls ~, ~/.gitconfig)."""
    rest = os.path.normpath(p)[len(home.rstrip('/')):].lstrip('/')
    top = rest.split('/')[0]
    return bool(top) and not top.startswith('.')


def classify_call(tc, cell, home=None):
    """-> (names_ctl, parent_reach, outside, other_record, tilde): outside/other_record from LITERAL paths only;
    tilde = a ~/$HOME path that is outside the cell only under the box-home reading"""
    args = tc.get('args') if isinstance(tc, dict) else None
    if not isinstance(args, dict):
        return False, False, False, False, False
    names = parent = outside = other = tilde = False
    for k, v in args.items():
        s = strval(v)
        if k.lower() in ('commandline', 'command', 'cmd'):
            if CMD_CTL.search(s):
                names = True
            if CMD_PARENT.search(s) or any(c and re.search(re.escape(c.rstrip('/')) + r'(?=$|[\s\'";|&)])', s)
                                           for c in (cell if isinstance(cell, list) else [cell])):
                parent = True
            for p, lit in home_paths(s, home):
                if is_outside(p, cell, home):
                    if lit:
                        outside = True
                        other = other or is_other_record(p, home)
                    else:
                        tilde = True
        elif PATH_KEY.search(k) and not CONTENT_KEY.search(k):
            for p in ([s] if not isinstance(v, list) else [strval(x) for x in v]):
                if path_names_ctl(p, cell):
                    names = True
                if path_is_parent(p, cell):
                    parent = True
                for x, lit in home_paths(p, home):
                    if is_outside(x, cell, home):
                        if lit:
                            outside = True
                            other = other or is_other_record(x, home)
                        else:
                            tilde = True
    return names, parent, outside, other, tilde


def walk_transcripts(d):
    out = []
    for dp, dn, fn in os.walk(d):
        out += [os.path.join(dp, x) for x in fn if x == 'transcript_full.jsonl']
    return out


def census_cell(cell, home=None):
    """-> dict(state, transcripts, calls, named, parent, hits[list of (kind, tool, argjson)])
    `cell` is one directory or a list of them: a by-id record found in more than one family is read in every
    family, as record_join.py reads it."""
    out = dict(state='UNMEASURED', transcripts=0, calls=0, named=0, parent=0, outside=0, other=0, tilde=0, hits=[], why='')
    cells = [c for c in (cell if isinstance(cell, list) else [cell]) if os.path.isdir(c)]
    if not cells:
        out['why'] = 'no cell directory'
        return out
    # EVERY transcript_full.jsonl under the cell AND under its family's _aside/<id>/ (a two-phase cell's phase-1
    # conversation is moved there). The one-depth brain glob missed 213 transcripts in 108 cells of record (11-25).
    ts = sorted(set((c, p) for c in cells for d in (c, os.path.join(os.path.dirname(c), '_aside', os.path.basename(c)))
                    for p in walk_transcripts(d)))
    if not ts:
        out['why'] = 'no brain transcript'
        return out
    for cell, p in ts:
        try:
            fh = open(p, 'rb')
        except Exception as e:
            out['why'] = 'unreadable transcript: %s' % e
            out['state'] = 'UNMEASURED'
            return out
        with fh:
            for line in fh:
                try:
                    r = json.loads(line.decode('utf-8', 'replace'))
                except Exception:
                    continue
                if not isinstance(r, dict):
                    continue
                for tc in r.get('tool_calls') or []:
                    out['calls'] += 1
                    n, par, outs, oth, til = classify_call(tc, cells if len(cells) > 1 else cell, home)
                    if n or par or outs or til:
                        # an argument is shown to its first newline: hits.tsv shows the paths a call names, and an inline
                        # script body is not one (it also carries escaped text a path gate misreads as a separator)
                        shown = {k: (strval(v).split('\n', 1)[0] + (' …' if '\n' in strval(v) else ''))
                                 for k, v in (tc.get('args') or {}).items()} if isinstance(tc.get('args'), dict) else {}
                        a = json.dumps(shown, ensure_ascii=True)[:300]
                        if home:
                            a = a.replace(home.rstrip('/'), '~')
                        # a checkout under ~/projects is a private record on the run box: written as a role, never a path
                        a = re.sub(r'~/projects/[^\s"\\\']*', '~/<a project checkout>', a)
                        out['hits'].append(('+'.join(k for k, v in (('CTL', n), ('OTHER-RECORD' if oth else 'HOME-ENV', outs), ('TILDE', til and not outs), ('PARENT', par)) if v), str(tc.get('name')), a))
                    out['named'] += n
                    out['parent'] += par
                    out['outside'] += outs
                    out['other'] += oth
                    out['tilde'] += til
        out['transcripts'] += 1
    flags = [k for k, v in (('CTL-NAMED', out['named']), ('OTHER-RECORD', out['other']),
                            ('HOME-ENV', out['outside'] and not out['other']),
                            ('TILDE', out['tilde'] and not out['outside'])) if v]
    out['state'] = '+'.join(flags) or 'NONE-NAMED'
    return out


LIMIT = ('#LIMIT NONE-NAMED is a lower bound on contact with ctl/: a call that reaches ctl/ without naming it '
         '(a recursive read from a parent) is invisible here; PARENT counts those candidates and is never a CTL-READ.')


def run_join(join, home, out_path, hits_path):
    rows = [l.rstrip('\n').split('\t') for l in open(join) if l.strip() and not l.startswith('#')]
    tot = {}
    with open(out_path, 'w') as fo, open(hits_path, 'w') as fh:
        fo.write('#block\tid\tmodel\tarm\tcell\tstate\ttranscripts\tcalls\tctl_named\tother_record\thome_env_or_other\ttilde\tparent_reach\twhy\n')
        fh.write('#block\tid\tkind\ttool\targs\n')
        for r in rows:
            block, cid, model, arm, _how, root = r[:6]
            # join.tsv's root column is the family list record_join.py read (comma-separated when a by-id record
            # was found in more than one family); every family is read, never the joined string as one path.
            fams = [x for x in root.split(',') if x and x != '-']
            c = census_cell([os.path.join(home, f, cid) for f in fams], home)
            rel = ','.join('~/' + f + '/' + cid for f in fams) or '-'
            tc = c['transcripts'] if c['state'] != 'UNMEASURED' else '-'
            fo.write('\t'.join(map(str, [block, cid, model, arm, rel, c['state'], tc, c['calls'] if tc != '-' else '-',
                                         c['named'] if tc != '-' else '-', c['other'] if tc != '-' else '-',
                                         c['outside'] if tc != '-' else '-', c['tilde'] if tc != '-' else '-',
                                         c['parent'] if tc != '-' else '-',
                                         c['why'] or '-'])) + '\n')
            for h in c['hits']:
                fh.write('\t'.join([block, cid] + list(h)) + '\n')
            t = tot.setdefault(block, {})
            t[c['state']] = t.get(c['state'], 0) + 1
        allt = {}
        for b in tot:
            for s, n in tot[b].items():
                allt[s] = allt.get(s, 0) + n
        summ = ' '.join('%s:%s' % (b, ','.join('%s=%d' % kv for kv in sorted(tot[b].items()))) for b in tot)
        fo.write('#POPULATION rows=%d %s all:%s\n' % (len(rows), summ, ','.join('%s=%d' % kv for kv in sorted(allt.items()))))
        fo.write(LIMIT + '\n')
    print('rows=%d' % len(rows), ' '.join('%s=%d' % kv for kv in sorted(allt.items())))
    print(LIMIT)


def selftest():
    """Each planted shape must land in its own state. Returns the failure count."""
    fails = 0
    d = tempfile.mkdtemp(prefix='ctlc-selftest-')

    def mk(name, calls, transcript=True):
        cell = os.path.join(d, name)
        os.makedirs(os.path.join(cell, 'ctl'))
        if transcript:
            t = os.path.join(cell, TRANSCRIPT.replace('*', 'conv-1'))
            os.makedirs(os.path.dirname(t))
            with open(t, 'w') as f:
                f.write(json.dumps({'type': 'PLANNER_RESPONSE', 'tool_calls': calls}) + '\n')
        return cell

    arms = [
        # name, calls, transcript?, expected state, expected named, expected parent, expected outside
        ('abs-read', lambda c: [{'name': 'read_file', 'args': {'Path': c + '/ctl/briefing-claim'}}], True, 'CTL-NAMED', 1, 0, 0),
        ('rel-dotdot', lambda c: [{'name': 'run_command', 'args': {'CommandLine': 'tail -n 30 ../ctl/launch.log'}}], True, 'CTL-NAMED', 1, 0, 0),
        ('bare-relative', lambda c: [{'name': 'run_command', 'args': {'CommandLine': 'cd .. && cat ctl/fault-gate-1'}}], True, 'CTL-NAMED', 1, 1, 0),
        ('ls-bare', lambda c: [{'name': 'run_command', 'args': {'CommandLine': 'ls ctl'}}], True, 'CTL-NAMED', 1, 0, 0),
        ('double-encoded', lambda c: [{'name': 'list_dir', 'args': {'DirectoryPath': '"../ctl"'}}], True, 'CTL-NAMED', 1, 0, 0),
        ('content-only', lambda c: [{'name': 'write_file', 'args': {'TargetFile': c + '/repo/LANDING.md', 'Content': 'see ../ctl/launch.log'}}], True, 'NONE-NAMED', 0, 0, 0),
        ('word-not-path', lambda c: [{'name': 'run_command', 'args': {'CommandLine': 'grep -rn ioctl src'}}], True, 'NONE-NAMED', 0, 0, 0),
        ('parent-grep', lambda c: [{'name': 'run_command', 'args': {'CommandLine': 'grep -rn ARMRECV ..'}}], True, 'NONE-NAMED', 0, 1, 0),
        ('clean', lambda c: [{'name': 'read_file', 'args': {'Path': c + '/repo/src/lib.rs'}}], True, 'NONE-NAMED', 0, 0, 0),
        ('no-transcript', lambda c: [], False, 'UNMEASURED', None, None, None),
        # OUTSIDE: l8rfss03's shapes (a home-wide find, then another cell's brain transcript), and what must not count
        ('other-cell', lambda c: [{'name': 'view_file', 'args': {'AbsolutePath': d + '/EVIDENCE-x--cells-y/l8rfpw01/.agyhome/brain/t.jsonl'}}], True, 'OTHER-RECORD', 0, 0, 1),
        ('find-home', lambda c: [{'name': 'run_command', 'args': {'CommandLine': 'find ~ -name "transcript*.jsonl" 2>/dev/null', 'Cwd': c + '/repo'}}], True, 'TILDE', 0, 0, 0),
        ('home-var', lambda c: [{'name': 'run_command', 'args': {'CommandLine': 'ls $HOME/agy-cells'}}], True, 'TILDE', 0, 0, 0),
        ('other-ctl', lambda c: [{'name': 'run_command', 'args': {'CommandLine': 'cat ' + d + '/cells-z/z01/ctl/briefing-file'}}], True, 'CTL-NAMED+OTHER-RECORD', 1, 0, 1),
        ('toolchain', lambda c: [{'name': 'view_file', 'args': {'AbsolutePath': d + '/.cargo/registry/src/x/lib.rs'}}], True, 'NONE-NAMED', 0, 0, 0),
        ('own-cell-tilde', lambda c: [{'name': 'run_command', 'args': {'CommandLine': 'ls -la ~/own-cell-tilde/repo', 'Cwd': c + '/repo'}}], True, 'NONE-NAMED', 0, 0, 0),
        ('dotfile', lambda c: [{'name': 'run_command', 'args': {'CommandLine': 'cat ~/.gitconfig'}}], True, 'TILDE', 0, 0, 0),
        ('literal-dotfile', lambda c: [{'name': 'run_command', 'args': {'CommandLine': 'cat ' + d + '/.gitconfig'}}], True, 'HOME-ENV', 0, 0, 1),
        ('literal-home', lambda c: [{'name': 'list_dir', 'args': {'DirectoryPath': d}}], True, 'HOME-ENV', 0, 0, 1),
        ('verus-pin', lambda c: [{'name': 'run_command', 'args': {'CommandLine': '~/verus-pin/verus-arm64-macos/verus x.rs'}}], True, 'NONE-NAMED', 0, 0, 0),
        ('cargo-root', lambda c: [{'name': 'view_file', 'args': {'AbsolutePath': d + '/bench-src/cargo-root-v3/vstd/seq.rs'}}], True, 'NONE-NAMED', 0, 0, 0),
        ('tilde-in-word', lambda c: [{'name': 'run_command', 'args': {'CommandLine': 'git diff HEAD~1 -- src/a~b.rs'}}], True, 'NONE-NAMED', 0, 0, 0),
    ]
    for name, f, tr, st, nn, pp, oo in arms:
        cell = os.path.join(d, name)
        mk(name, f(cell), tr)
        c = census_cell(cell, d)   # the fixture root plays $HOME
        ok = c['state'] == st and (nn is None or (c['named'] == nn and c['parent'] == pp and c['outside'] == oo))
        fails += not ok
        print('%s %-15s state=%s named=%s parent=%s outside=%s (want %s %s %s %s)' % ('ok  ' if ok else 'FAIL', name,
              c['state'], c['named'], c['parent'], c['outside'], st, nn, pp, oo))
    c = census_cell(os.path.join(d, 'absent'))
    ok = c['state'] == 'UNMEASURED'
    fails += not ok
    print('%s %-15s state=%s (want UNMEASURED)' % ('ok  ' if ok else 'FAIL', 'no-directory', c['state']))
    # a two-phase cell: phase 1's conversation moved to <family>/_aside/<id>/phase1/ (the 108 cells the first glob missed)
    fam = os.path.join(d, 'famP'); cp = os.path.join(fam, 'p01')
    mk(os.path.join('famP', 'p01'), [{'name': 'read_file', 'args': {'Path': cp + '/repo/src/lib.rs'}}])
    ta = os.path.join(fam, '_aside', 'p01', 'phase1', TRANSCRIPT.replace('*', 'conv-0'))
    os.makedirs(os.path.dirname(ta))
    with open(ta, 'w') as fh:
        fh.write(json.dumps({'type': 'PLANNER_RESPONSE', 'tool_calls': [{'name': 'view_file', 'args': {'AbsolutePath': cp + '/ctl/launch.log'}}]}) + '\n')
    c = census_cell(cp, d)
    ok = c['state'] == 'CTL-NAMED' and c['transcripts'] == 2
    fails += not ok
    print('%s %-15s state=%s transcripts=%s (want CTL-NAMED 2)' % ('ok  ' if ok else 'FAIL', 'aside-phase1', c['state'], c['transcripts']))
    # a copied record: the transcript in family B names its path in family A, which is the SAME record (l5cp01's shape)
    fa, fb = os.path.join(d, 'famA', 'x01'), os.path.join(d, 'famB', 'x01')
    os.makedirs(os.path.join(fa, 'repo'))
    mk(os.path.join('famB', 'x01'), [{'name': 'view_file', 'args': {'AbsolutePath': fa + '/repo/src/lib.rs'}}])
    c = census_cell([fa, fb], d)
    ok = c['state'] == 'NONE-NAMED' and c['outside'] == 0
    fails += not ok
    print('%s %-15s state=%s outside=%s (want NONE-NAMED 0)' % ('ok  ' if ok else 'FAIL', 'copied-record', c['state'], c['outside']))
    c = census_cell(fb, d)   # the same transcript judged against ONE family: family A is outside (the control)
    ok = c['state'] == 'OTHER-RECORD'
    fails += not ok
    print('%s %-15s state=%s (want OTHER-RECORD: one family only)' % ('ok  ' if ok else 'FAIL', 'copied-control', c['state']))
    # a by-id record in two families, one absent: the present family is read (the 10 rows the first run missed)
    c = census_cell([os.path.join(d, 'absent'), os.path.join(d, 'abs-read')])
    ok = c['state'] == 'CTL-NAMED' and c['named'] == 1
    fails += not ok
    print('%s %-15s state=%s named=%s (want CTL-NAMED 1)' % ('ok  ' if ok else 'FAIL', 'multi-family', c['state'], c['named']))
    n = len(arms) + 5
    print('SELFTEST %d/%d' % (n - fails, n))
    return fails


if __name__ == '__main__':
    a = sys.argv[1:]
    if a[:1] == ['--selftest']:
        sys.exit(1 if selftest() else 0)
    if a[:1] == ['--cells']:
        for cell in a[1:]:
            c = census_cell(cell, os.path.expanduser('~'))
            print('%s\t%s\ttranscripts=%d\tcalls=%d\tctl_named=%d\toutside=%d\tparent=%d\t%s' % (cell, c['state'],
                  c['transcripts'], c['calls'], c['named'], c['outside'], c['parent'], c['why'] or '-'))
            for h in c['hits']:
                print('  ' + '\t'.join(h))
        print(LIMIT)
        sys.exit(0)
    opts = dict(zip(a[::2], a[1::2]))
    for k in ('--join', '--home', '--out', '--hits'):
        if k not in opts:
            sys.exit('usage: see --help; missing ' + k)
    run_join(opts['--join'], opts['--home'], opts['--out'], opts['--hits'])
