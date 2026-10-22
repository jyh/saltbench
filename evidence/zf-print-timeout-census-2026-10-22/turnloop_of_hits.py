"""For every ZF cell root with >= 1 "print timeout" in its agy stderr, print the turn loop record of each cell.
Run on the run box from the home directory: python3 - < turnloop_of_hits.py > turnloop-of-hit-roots.tsv
(the -env- files also match the glob and print None rows; those rows are dropped from the tsv)."""
import glob,json,os
H=os.path.expanduser('~')
rows=[]
for root in sorted(glob.glob(H+'/cells-*zf-*')):
    if 'DISCARDED' in root: continue
    for cell in sorted(glob.glob(root+'/*/ctl')):
        hits=0
        for f in glob.glob(cell+'/agy-stderr-*.txt'):
            hits+=open(f,errors='replace').read().count('print timeout')
        if not hits: continue
        for t in sorted(glob.glob(cell+'/agy-turnloop-*.json')):
            ph=t.rsplit('-',1)[1].split('.')[0]
            try: j=json.load(open(t))
            except Exception as e: print(os.path.basename(root),ph,'UNREADABLE',e); continue
            print('\t'.join(map(str,[os.path.basename(root),ph,hits,j.get('done_reason'),j.get('turns_sent'),j.get('turns_no_output'),j.get('landed'),round(j.get('wall_seconds') or 0)])))
