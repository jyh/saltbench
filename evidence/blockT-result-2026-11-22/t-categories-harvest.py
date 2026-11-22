import re, sys
# t-categories-harvest.py <bus file> <file of cell ids> — per cell, the statement category from the LAST lead read post whose subject's
# FIRST cell id is that cell (a post naming a sister cell is not attributed to it): a body CATEGORY line, else a body STATEMENT line, else
# the subject. Prints cell, byte offset of the post, where the label was found, the label, the line.
raw = open(sys.argv[1],'rb').read()
start = len(raw) - 30_000_000
starts = [m.start() + start + 1 for m in re.finditer(rb'\n\[\d\d/\d\d \d\d:\d\d:\d\d, bench=', raw[start:])]
CAT = re.compile(r'(USED(?: \((?:partial|unverified)\))?|EXEC USE(?: \(partial\))?|TEST ORACLE(?: \(partial\))?|WEAK TRACE|NO TRACE|SPEC TRANSCRIBED, CONTRACT ABSENT)')
ids = set(l.split()[0] for l in open(sys.argv[2]))
best = {}
for s in starts:
    e = raw.find(b'\n[', s + 1); post = raw[s:e if e > 0 else len(raw)].decode('utf-8', 'replace')
    head = post.split('\n', 1)[0]
    m = re.search(r'clb[a-z]{3}\d\d', head)
    if not m or m.group(0) not in ids: continue
    cid = m.group(0)
    body = post.split('\n')[1:]
    cl = [l for l in body if re.match(r'\s*-?\s*(CATEGORY|STATEMENT: [A-Z]|STATEMENT \(plain\)|Statement \(plain\))', l)]
    src = None
    for l in body:
        if re.match(r'\s*-?\s*CATEGORY', l):
            mm = CAT.search(l); src = ('body-CATEGORY', mm.group(1) if mm else '?', l.strip()[:120]); break
    if not src:
        for l in body:
            if re.match(r'\s*-?\s*STATEMENT: ', l):
                mm = CAT.search(l); src = ('body-STATEMENT', mm.group(1) if mm else '?', l.strip()[:120]); break
    if not src:
        mm = CAT.search(head)
        if mm: src = ('subject', mm.group(1), head[head.find(cid):][:120])
    if src: best[cid] = (s,) + src   # the LAST post wins (a later read supersedes)
for cid in sorted(ids):
    b = best.get(cid)
    print(cid, *(b if b else ('-', 'NONE', '-', '-')), sep='\t')
