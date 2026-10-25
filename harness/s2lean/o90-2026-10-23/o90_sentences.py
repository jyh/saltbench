#!/usr/bin/env python3
"""o90_sentences.py — the O90 truth axis's SENTENCE POPULATION (stage 1, AMENDMENT-O90-stage1 ADDENDUM 3): every prose
sentence of every scored stage-B artifact, split by a rule frozen here, before any truth read.
Sources, per artifact (<state>/problem_<id>/<arm>/B.artifact/): `stageB.lean`'s doc comments (`/-- … -/` and `/-! … -/`) and,
where present, `EXPLAIN.md`. Nothing else is prose for this axis: `--` line comments and Lean code are not read.
Rules, in order (each one an arm of --selftest):
  1. EXPLAIN.md: fenced code blocks (``` … ```) and heading lines (`#…`) are dropped; a bullet or numbered-list marker is
     stripped and each list item starts a new sentence; a blank line ends a paragraph.
  2. A paragraph, list item or doc comment is split after `.`, `!` or `?` FOLLOWED BY WHITESPACE, so dotted Lean names
     (`List.sum`) and decimals never split. Whitespace inside a sentence is collapsed to one space.
  3. A piece with fewer than 3 alphabetic words is DROPPED, and counted per artifact (never silently).
  4. Each kept sentence gets the id `<source>:<n>` (source `doc` or `explain`, n from 1 in reading order) and the sha256 of
     its bytes as written to the TSV; the artifact's `b_episode` comes from its `B.artifact.json` (refuse if absent).
  usage: o90_sentences.py <state_root> > sentences.tsv   ·   o90_sentences.py --selftest
Output: a header, one row per sentence (problem arm b_episode sentence sentence_sha256 text), then one `# DROPPED` line per
artifact and a `# TOTAL` line. The flag log (o90_flaglog.py) keys on (b_episode, sentence) and sentence_sha256 from here."""
import glob, hashlib, json, os, re, sys

MIN_WORDS = 3
SPLIT = re.compile(r'(?<=[.!?])\s+')
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
    return [m.group(1) for m in DOC.finditer(text)]


def sentences(pieces):
    kept, dropped = [], 0
    for p in pieces:
        for s in SPLIT.split(' '.join(p.split())):
            s = s.strip()
            if not s: continue
            if len(re.findall(r'[A-Za-z]{2,}', s)) < MIN_WORDS: dropped += 1; continue
            kept.append(s)
    return kept, dropped


def artifact_rows(d):
    meta = os.path.join(d, 'B.artifact.json')
    try: ep = json.load(open(meta))['b_episode']
    except (OSError, KeyError, ValueError) as e: raise SystemExit('REFUSE: no b_episode in %s (%s)' % (meta, type(e).__name__))
    parts = d.rstrip('/').split('/'); prob, arm = parts[-3].replace('problem_', ''), parts[-2]
    rows, drops = [], 0
    for src, path, fn in (('doc', 'stageB.lean', pieces_of_lean), ('explain', 'EXPLAIN.md', pieces_of_explain)):
        p = os.path.join(d, path)
        if not os.path.exists(p): continue
        kept, dr = sentences(fn(open(p, encoding='utf-8', errors='replace').read())); drops += dr
        for n, s in enumerate(kept, 1):
            rows.append((prob, arm, ep, '%s:%d' % (src, n), hashlib.sha256(s.encode()).hexdigest(), s))
    return rows, drops, (prob, arm, ep)


def build(state):
    dirs = sorted(glob.glob(os.path.join(state, 'problem_*', 'a*', 'B.artifact')))
    if not dirs: raise SystemExit('REFUSE: no B.artifact under %s' % state)
    out, notes, total, tdrop = ['problem\tarm\tb_episode\tsentence\tsentence_sha256\ttext'], [], 0, 0
    for d in dirs:
        rows, drops, (prob, arm, ep) = artifact_rows(d)
        for r in rows:
            assert '\t' not in r[5] and '\n' not in r[5], r
            out.append('\t'.join(r))
        notes.append('# DROPPED %s %s %s: %d pieces under %d words; kept %d' % (prob, arm, ep, drops, MIN_WORDS, len(rows)))
        total += len(rows); tdrop += drops
    return out + notes + ['# TOTAL artifacts %d · sentences %d · dropped %d' % (len(dirs), total, tdrop)]


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
    arm('a heading line is dropped', not any('Heading' in s for s in k))
    arm('a fenced code block is dropped', not any('trivial' in s or 'Not prose' in s for s in k))
    arm('a dotted Lean name does not split', 'The proof uses `List.sum` on the input.' in k)
    arm('a decimal does not split', 'Value 3.5 stays whole in this sentence.' in k)
    arm('list items start new sentences, markers stripped',
        'First item states one thing.' in k and 'Second item states another thing!' in k and 'Numbered item is a sentence.' in k)
    arm('a piece under 3 words is dropped and counted', 'Too short.' not in k and 'It ends here.' in k and dr == 2)
    lean = 'def f := 1\n/-- The function returns one. Always. -/\ntheorem t : f = 1 := rfl\n/-! Module note says this file proves t. -/\n-- a line comment is never read here\n'
    kl, dl = sentences(pieces_of_lean(lean))
    arm('doc comments are read, line comments are not',
        kl == ['The function returns one.', 'Module note says this file proves t.'] and dl == 1)
    with tempfile.TemporaryDirectory() as t:
        d = os.path.join(t, 'problem_7', 'a5', 'B.artifact'); os.makedirs(d)
        open(os.path.join(d, 'stageB.lean'), 'w').write(lean); open(os.path.join(d, 'EXPLAIN.md'), 'w').write(ex)
        json.dump({'b_episode': 'ep-test'}, open(os.path.join(d, 'B.artifact.json'), 'w'))
        out = build(t); rows = [l.split('\t') for l in out[1:] if not l.startswith('#')]
        arm('ids are unique and carry their source', len({r[3] for r in rows}) == len(rows) and rows[0][3] == 'doc:1'
            and any(r[3].startswith('explain:') for r in rows))
        arm('sha256 is of the text as written', all(r[4] == hashlib.sha256(r[5].encode()).hexdigest() for r in rows))
        arm('the run is deterministic', build(t) == out)
        os.remove(os.path.join(d, 'B.artifact.json')); json.dump({}, open(os.path.join(d, 'B.artifact.json'), 'w'))
        try: build(t); refused = False
        except SystemExit: refused = True
        arm('an artifact without b_episode refuses', refused)
    print('SELFTEST %d/%d' % (ok, n))
    return ok == n


if __name__ == '__main__':
    if sys.argv[1:] == ['--selftest']: sys.exit(0 if selftest() else 1)
    if len(sys.argv) != 2: raise SystemExit(__doc__)
    sys.stdout.write('\n'.join(build(sys.argv[1])) + '\n')
