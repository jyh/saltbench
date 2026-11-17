import sys,re,collections,csv
cm,streams,hits=sys.argv[1:4]
st=collections.defaultdict(set)
for s in [l.rstrip("\n") for l in open(streams) if l.strip()]:
    p=s.split("\t"); st[p[1]].add(p[0])
hit=set(tuple(l.split('\t')[:2]) for l in open(hits) if l.strip())
rows=list(csv.DictReader(open(cm),delimiter='\t'))
agg=collections.Counter(); out=[]
for r in rows:
    if not r['model'].startswith('gemini'): continue
    c=r['cell']; m=re.search(r'root=([^,|]+)',r['sources']); root=m.group(1) if m else None
    fams=st.get(c,set())
    if root: how='root-named'; fam={root}&fams
    else: how='id-only'; fam=fams
    if not fam: state='NO-STREAM'
    else:
        h=[f for f in fam if (f,c) in hit]
        state='HIT' if (h and (how=='root-named' or len(fam)==1)) else ('HIT-AMBIG' if h else 'clean')
    k=(r['model'],r['arm'])
    agg[k+(state,)]+=1
    out.append('\t'.join([r['model'],r['problem'],r['field'],r['arm'],r['extras'],c,root or '-',how,','.join(sorted(fam)) or '-',state]))
open(sys.argv[4],'w').write('model\tproblem\tfield\tarm\textras\tcell\troot_in_cellmap\tmatch\tstream_families\tstate\n'+'\n'.join(out)+'\n')
ks=sorted({k[:2] for k in agg})
print('model\tarm\tHIT\tHIT-AMBIG\tclean\tNO-STREAM\ttotal')
for k in ks:
    v=[agg[k+(s,)] for s in ('HIT','HIT-AMBIG','clean','NO-STREAM')]; print('\t'.join(k+tuple(map(str,v))+(str(sum(v)),)))
print('matched by root',sum(1 for o in out if o.split('\t')[7]=='root-named'),'of',len(out))
