# claude_join.py CELLMAP projects.tsv gatest-hits.tsv OUT — join signature G (the salt-diet gate's selftest failing mkdtemp on its
# gatest.* dir, inside a tool result; every row of gatest-hits.tsv is a hit) to the matrix's Claude DONE rows, by the cell id as a
# token of the transcript's project name.
import sys, csv, re, collections
cm, projs, cen, outp = sys.argv[1:5]
P = [l.rstrip('\n').split('\t') for l in open(projs) if l.strip()]
C = collections.Counter()
for l in list(open(cen))[1:]:
    f = l.rstrip('\n').split('\t'); C[f[0]] += 1
agg = collections.Counter(); out = []
for r in csv.DictReader(open(cm), delimiter='\t'):
    if r['model'].startswith('gemini') or r['status'] != 'DONE': continue
    c = r['cell']; pat = re.compile(r'(?<![A-Za-z0-9])' + re.escape(c) + r'(?![A-Za-z0-9])')
    ps = [p for p in P if pat.search(p[0]) and int(p[1]) > 0]
    st = 'NO-TRANSCRIPT' if not ps else ('GATE-HIT' if any(C[p[0]] for p in ps) else 'clean')
    agg[(r['model'], r['arm'], st)] += 1
    out.append('\t'.join([r['model'], r['problem'], r['field'], r['arm'], r['extras'], c, ','.join(p[0] for p in ps) or '-', st]))
open(outp, 'w').write('model\tproblem\tfield\tarm\textras\tcell\tprojects\tstate\n' + '\n'.join(out) + '\n')
print('model\tarm\tGATE-HIT\tclean\tNO-TRANSCRIPT')
for m in sorted({k[:2] for k in agg}): print('\t'.join(m) + '\t' + '\t'.join(str(agg[m + (s,)]) for s in ('GATE-HIT', 'clean', 'NO-TRANSCRIPT')))
hit = sorted({o.split('\t')[5] for o in out if o.endswith('GATE-HIT')}); print('distinct GATE-HIT cells', len(hit), ' '.join(hit))
