# Read-only census of every cells-zf-* root's agy-turnloop-*.json on the run box (the 10-18 empty.tsv's columns):
# root cid file done_reason turns_sent turns_no_output turns_no_output_index turns_error_empty
import glob,json,os
# v2 (2026-10-24): spec-change roots are cells-l8zf-*, and phase 1 is <root>/_aside/<cell>/phase1/ctl/ (sc_phase1.py);
# v1 globbed cells-zf-* alone and missed all 40 spec-change legs. Phase-1 rows carry file 'P1:<name>'.
H=os.path.expanduser('~')
ps=sorted(glob.glob(H+'/cells-zf-*/*/ctl/agy-turnloop*.json')+glob.glob(H+'/cells-l8zf-*/*/ctl/agy-turnloop*.json')
          +glob.glob(H+'/cells-l8zf-*/_aside/*/phase1/ctl/agy-turnloop*.json'))
for p in ps:
    parts=p.split('/')
    if parts[-3]=='phase1': root,cid,f=parts[-6],parts[-4],'P1:'+parts[-1]
    else: root,cid,f=parts[-4],parts[-3],parts[-1]
    try: d=json.load(open(p))
    except Exception as e: print('\t'.join([root,cid,f,'UNREADABLE:'+type(e).__name__]+['None']*4)); continue
    g=lambda k: str(d.get(k))
    print('\t'.join([root,cid,f,g('done_reason'),g('turns_sent'),g('turns_no_output'),g('turns_no_output_index'),g('turns_error_empty')]))
