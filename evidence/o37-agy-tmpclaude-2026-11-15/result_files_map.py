# result_files_map.py <repo-root> <census-hits.tsv> — for each hit (family, cell), the RESULT-* files whose text holds the cell id as a whole word
import sys, os, re, collections
root, hits = sys.argv[1:3]
files = []
for d, _, fs in os.walk(os.path.join(root, 'harness')):
    files += [os.path.join(d, f) for f in fs if f.startswith('RESULT-')]
text = {f: open(f, encoding='utf-8', errors='replace').read() for f in files}
per = collections.defaultdict(lambda: collections.Counter()); n_unc = 0
print('family\tcell\tdir_arm\tresult_files')
for l in open(hits):
    if not l.strip(): continue
    fam, cell, ph, era, arm = l.rstrip('\n').split('\t')[:5]
    pat = re.compile(r'(?<![A-Za-z0-9_])' + re.escape(cell) + r'(?![A-Za-z0-9_])')
    hit = sorted(os.path.relpath(f, root) for f, t in text.items() if pat.search(t))
    n_unc += not hit
    for f in hit: per[f][arm] += 1
    print('%s\t%s\t%s\t%s' % (fam, cell, arm, ','.join(hit) or '-'))
print('# cited by no RESULT file: %d' % n_unc)
for f in sorted(per): print('# %s\t%s' % (f, ' '.join('%s=%d' % kv for kv in sorted(per[f].items()))))
