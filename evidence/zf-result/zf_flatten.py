# zf_flatten.py — one row per ZF cell, from extract_legs.py's zt.json and the run box's turnloop census (empty_census.py v2).
# bench, 2026-10-24. Read-only. A missing census row prints UNREAD, never 0.
import json,sys
zt,emp,out=sys.argv[1:4]
E={}
for l in open(emp):
    f=l.rstrip('\n').split('\t')
    if f[2] in('agy-turnloop-1.json','agy-turnloop-2.json'): E[('final',f[1])]=(f[5],f[6])
    elif f[2]=='P1:agy-turnloop-1.json': E[('p1',f[1])]=(f[5],f[6])
H=['z','cid','problem','field','card','arm','rep','model','done_reason','score_phase','belt','trunc','scored','fault','end','verdict','tests','empty_final','empty_final_idx','empty_p1','empty_p1_idx','wall_s','turns','score_dir']
o=open(out,'w'); o.write('# ZF cells, one row per harvested leg; built by zf_flatten.py from extract_legs.py (zt.json) + empty_census.py v2 (run box)\n'+'\t'.join(H)+'\n')
for r in json.load(open(zt)):
    v=r['verd'][0]; ef=E.get(('final',r['cid']),('UNREAD','UNREAD'))
    ep=E.get(('p1',r['cid']),('UNREAD','UNREAD')) if r['sc'] else ('-','-')
    row=[r['z'],r['cid'],r['prob'],r['field'],r['card'],r['arm'],r['rep'],r['model'],r['dr'],v[0],v[1],v[2] or '-',v[3],v[4],v[5],v[6],v[7] or '-',
         ef[0],ef[1].replace(' ',''),ep[0],ep[1].replace(' ',''),str(r['wall']),str(r['turns']),r['sd']]
    assert all('\t' not in x and '\n' not in x for x in row),row
    o.write('\t'.join(row)+'\n')
