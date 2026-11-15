# result_files_map.py <repo-root> claude-join.tsv — for each distinct GATE-HIT cell: the RESULT-*.md files that name it as a whole word, plus
# the block result whose root holds it (cells-clb-<blk>-… → RESULT-claude-block<BLK>-*.md), since a block result may cite cells only in a TSV.
import sys, os, re, glob, collections
root, join = sys.argv[1:3]
hits = {}
for l in list(open(join))[1:]:
    f = l.rstrip('\n').split('\t')
    if f[7] == 'GATE-HIT': hits[f[5]] = f[6]
md = glob.glob(os.path.join(root, 'harness/*/RESULT-*.md'))
per = collections.defaultdict(set)
for c, projs in sorted(hits.items()):
    pat = re.compile(r'(?<![A-Za-z0-9_])' + re.escape(c) + r'(?![A-Za-z0-9_])')
    for f in md:
        if pat.search(open(f, encoding='utf-8', errors='replace').read()): per[os.path.relpath(f, root)].add(c)
    for m in re.finditer(r'cells-clb-([a-z]+)-', projs):
        for f in glob.glob(os.path.join(root, 'harness/systems-v3/RESULT-claude-block%s-*.md' % m.group(1).upper())):
            if re.search(r'block%s-\d' % m.group(1).upper(), f): per[os.path.relpath(f, root)].add(c)
for f in sorted(per): print('%s\t%s' % (f, ' '.join(sorted(per[f]))))
