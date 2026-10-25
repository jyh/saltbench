#!/usr/bin/env python3
"""o90_sentences.py — the O90 truth axis's SENTENCE POPULATION (stage 1, AMENDMENT-O90-stage1 ADDENDUM 3): every prose
sentence of every scored stage-B artifact, split by a rule frozen here, before any truth read.
Sources, per artifact (<state>/problem_<id>/<arm>/B.artifact/): `stageB.lean`'s doc comments (`/-- … -/` and `/-! … -/`) and,
where present, `EXPLAIN.md`. Nothing else is prose for this axis: `--` line comments and Lean code are not read.
Rules, in order (each one an arm of --selftest):
  1. EXPLAIN.md AND each doc comment's body: fenced code blocks (``` … ```) and heading lines (`#…`) are dropped; a bullet or
     numbered-list marker is stripped and each list item starts a new sentence; a blank line ends a paragraph.
  2. A paragraph or list item is split after `.`, `!` or `?` FOLLOWED BY WHITESPACE, except inside a backtick span (Lean's
     `xs[i]! ` stays whole) and after `i.e.` or `e.g.`; so dotted Lean names (`List.sum`) and decimals never split.
     Whitespace inside a sentence is collapsed to one space.
  3. A piece with fewer than 3 alphabetic words is DROPPED, and counted per artifact (never silently).
  4. A sentence present VERBATIM (whitespace-collapsed) in any file of its problem's task view (<views>/problem_<id>/) is
     GIVEN: the task's own prose copied into the artifact, not the arm's. It is marked `given=yes`, kept in the TSV, and read
     by no one (ADDENDUM 3, systems' B1). Verbatim is a lower bound on copied text.
  5. Each kept sentence gets the id `<source>:<n>` (source `doc` or `explain`, n from 1 in reading order) and the sha256 of
     its bytes as written to the TSV; the artifact's `b_episode` comes from its `B.artifact.json` (refuse if absent).
  usage: o90_sentences.py <state_root> <views_root> > sentences.tsv   ·   o90_sentences.py --selftest
Output: a header, one row per sentence (problem arm b_episode sentence sentence_sha256 given text), then one `# DROPPED` line per
artifact and `# TOTAL` lines. The flag log (o90_flaglog.py) keys on (b_episode, sentence) and sentence_sha256 from here."""
import glob, hashlib, json, os, re, sys

MIN_WORDS = 3
SPLIT = re.compile(r'(?<=[.!?])\s+')
ABBREV = ('i.e.', 'e.g.')
DOC = re.compile(r'/-[-!](.*?)-/', re.S)
BULLET = re.compile(r'^\s*(?:[-*+]|\d+[.)])\s+')


def pieces_of_explain(text):
    out, para, fence = [], [], False
    def flush():
        if para: out.append(' '.join(para)); para.clear()
    for line in text.splitlines():
        if line.strip().startswith('```'):
            flush(); fence = not fence; continue
        if fence: continue
        if line.lstrip().startswith('#'):
            flush(); continue
        if not line.strip():
            flush(); continue
        if BULLET.match(line):
            flush(); para.append(BULLET.sub('', line, count=1).strip()); continue
        para.append(line.strip())
    flush()
    return out


def pieces_of_lean(text):
    return [p for m in DOC.finditer(text) for p in pieces_of_explain(m.group(1))]


def split(piece):
    out, start = [], 0
    for m in SPLIT.finditer(piece):
        head = piece[start:m.start()]
        if piece[:m.start()].count('`') % 2 or head.endswith(ABBREV): continue
        out.append(head); start = m.end()
    out.append(piece[start:])
    return out


def sentences(pieces):
    kept, dropped = [], 0
    for p in pieces:
        for s in split(' '.join(p.split())):
            s = s.strip()
            if not s: continue
            if len(re.findall(r'[A-Za-z]{2,}', s)) < MIN_WORDS: dropped += 1; continue
            kept.append(s)
    return kept, dropped


def view_text(views, prob):
    d = os.path.join(views, 'problem_%s' % prob)
    if not os.path.isdir(d): raise SystemExit('REFUSE: no task view %s' % d)
    txt = ''
    for f in sorted(glob.glob(d + '/*')):
        if os.path.isfile(f): txt += ' ' + open(f, encoding='utf-8', errors='replace').read()
    return ' '.join(txt.split())


def artifact_rows(d, views):
    meta = os.path.join(d, 'B.artifact.json')
    try: ep = json.load(open(meta))['b_episode']
    except (OSError, KeyError, ValueError) as e: raise SystemExit('REFUSE: no b_episode in %s (%s)' % (meta, type(e).__name__))
    parts = d.rstrip('/').split('/'); prob, arm = parts[-3].replace('problem_', ''), parts[-2]
    rows, drops, vt = [], 0, view_text(views, prob)
    for src, path, fn in (('doc', 'stageB.lean', pieces_of_lean), ('explain', 'EXPLAIN.md', pieces_of_explain)):
        p = os.path.join(d, path)
        if not os.path.exists(p): continue
        kept, dr = sentences(fn(open(p, encoding='utf-8', errors='replace').read())); drops += dr
        for n, s in enumerate(kept, 1):
            rows.append((prob, arm, ep, '%s:%d' % (src, n), hashlib.sha256(s.encode()).hexdigest(), 'yes' if s in vt else 'no', s))
    return rows, drops, (prob, arm, ep)


def build(state, views):
    dirs = sorted(glob.glob(os.path.join(state, 'problem_*', 'a*', 'B.artifact')))
    if not dirs: raise SystemExit('REFUSE: no B.artifact under %s' % state)
    out, notes, tdrop = ['problem\tarm\tb_episode\tsentence\tsentence_sha256\tgiven\ttext'], [], 0
    per = {}
    for d in dirs:
        rows, drops, (prob, arm, ep) = artifact_rows(d, views)
        for r in rows:
            assert '\t' not in r[6] and '\n' not in r[6], r
            out.append('\t'.join(r))
            c = per.setdefault(arm, {'art': set(), 'zero': set(), 'written': 0, 'given': 0, 'wdoc': 0})
            c['given' if r[5] == 'yes' else 'written'] += 1; c['wdoc'] += r[5] == 'no' and r[3].startswith('doc:')
        c = per.setdefault(arm, {'art': set(), 'zero': set(), 'written': 0, 'given': 0, 'wdoc': 0}); c['art'].add(ep)
        w = sum(r[5] == 'no' for r in rows)
        if not w: c['zero'].add(ep)
        notes.append('# DROPPED %s %s %s: %d pieces under %d words; kept %d (written %d · given %d)' % (prob, arm, ep, drops, MIN_WORDS, len(rows), w, len(rows) - w))
        tdrop += drops
    tot = ['# TOTAL artifacts %d · dropped %d' % (len(dirs), tdrop)]
    for arm in sorted(per):
        c = per[arm]
        tot.append('# TOTAL %s artifacts %d · written %d (doc comments %d) · given %d · artifacts with no written sentence %d'
                   % (arm, len(c['art']), c['written'], c['wdoc'], c['given'], len(c['zero'])))
    return out + notes + tot


def selftest():
    import tempfile
    ok = n = 0
    def arm(name, cond):
        nonlocal ok, n
        n += 1; ok += bool(cond); print(('PASS ' if cond else 'FAIL ') + name)
    ex = ('# Heading that is a claim about everything\n\nThe proof uses `List.sum` on the input. It ends here.\n\n'
          '```lean\ntheorem x : True := by trivial. Not prose at all here.\n```\n'
          '- First item states one thing.\n- Second item states another thing! And a third.\n1. Numbered item is a sentence.\n'
          'Too short.\n\nValue 3.5 stays whole in this sentence.\n')
    k, dr = sentences(pieces_of_explain(ex))
    k2, _ = sentences(['Returns `xs[i]! + 1` for each i. It holds, i.e. the bound is tight here.'])
    arm('no split inside a backtick span or after i.e.', k2 == ['Returns `xs[i]! + 1` for each i.', 'It holds, i.e. the bound is tight here.'])
    arm('a heading line is dropped', not any('Heading' in s for s in k))
    arm('a fenced code block is dropped', not any('trivial' in s or 'Not prose' in s for s in k))
    arm('a dotted Lean name does not split', 'The proof uses `List.sum` on the input.' in k)
    arm('a decimal does not split', 'Value 3.5 stays whole in this sentence.' in k)
    arm('list items start new sentences, markers stripped',
        'First item states one thing.' in k and 'Second item states another thing!' in k and 'Numbered item is a sentence.' in k)
    arm('a piece under 3 words is dropped and counted', 'Too short.' not in k and 'It ends here.' in k and dr == 2)
    lean = ('def f := 1\n/-- The function returns one. Always. -/\ntheorem t : f = 1 := rfl\n/-! Module note says this file proves t. -/\n'
            '-- a line comment is never read here\n/-- Facts:\n- the first listed fact holds\n- the second listed fact holds\n-/\n')
    kl, dl = sentences(pieces_of_lean(lean))
    arm('doc comments are read, line comments are not',
        kl[:2] == ['The function returns one.', 'Module note says this file proves t.'] and not any('line comment' in s for s in kl))
    # `Always.` and the one-word `Facts:` line are the two drops
    arm('rule 1 applies inside a doc comment (list items split)',
        kl[2:] == ['the first listed fact holds', 'the second listed fact holds'] and dl == 2)
    with tempfile.TemporaryDirectory() as t:
        d = os.path.join(t, 'problem_7', 'a5', 'B.artifact'); os.makedirs(d)
        v = os.path.join(t, 'views'); os.makedirs(os.path.join(v, 'problem_7'))
        open(os.path.join(v, 'problem_7', 'A.lean'), 'w').write('/--  The   function returns\n one.  -/ def f := 1')
        open(os.path.join(d, 'stageB.lean'), 'w').write(lean); open(os.path.join(d, 'EXPLAIN.md'), 'w').write(ex)
        json.dump({'b_episode': 'ep-test'}, open(os.path.join(d, 'B.artifact.json'), 'w'))
        out = build(os.path.join(t), v); rows = [l.split('\t') for l in out[1:] if not l.startswith('#')]
        g = {r[6]: r[5] for r in rows}
        arm('a sentence verbatim in the task view is GIVEN, others written',
            g.get('The function returns one.') == 'yes' and g.get('Module note says this file proves t.') == 'no')
        arm('ids are unique and carry their source', len({r[3] for r in rows}) == len(rows) and rows[0][3] == 'doc:1'
            and any(r[3].startswith('explain:') for r in rows))
        arm('sha256 is of the text as written', all(r[4] == hashlib.sha256(r[6].encode()).hexdigest() for r in rows))
        arm('the run is deterministic', build(t, v) == out)
        try: build(t, os.path.join(t, 'no-views')); refused_v = False
        except SystemExit: refused_v = True
        arm('a missing task view refuses', refused_v)
        os.remove(os.path.join(d, 'B.artifact.json')); json.dump({}, open(os.path.join(d, 'B.artifact.json'), 'w'))
        try: build(t, v); refused = False
        except SystemExit: refused = True
        arm('an artifact without b_episode refuses', refused)
    print('SELFTEST %d/%d' % (ok, n))
    return ok == n


if __name__ == '__main__':
    if sys.argv[1:] == ['--selftest']: sys.exit(0 if selftest() else 1)
    if len(sys.argv) != 3: raise SystemExit(__doc__)
    sys.stdout.write('\n'.join(build(sys.argv[1], sys.argv[2])) + '\n')
