import json,glob,os,sys
root=os.path.expanduser('~/bench-src/cargo-root-v3')
rows=[]
for p in sorted(glob.glob(os.path.expanduser('~/cells-l8*/*/ctl/srt-settings.json'))):
    cell=p.split('/')[-3]; cond=p.split('/')[-4]
    try: j=json.load(open(p))
    except Exception as e: rows.append((cond,cell,'UNREADABLE:'+type(e).__name__)); continue
    def walk(o):
        if isinstance(o,dict):
            for k,v in o.items():
                if k=='denyRead': yield from (v if isinstance(v,list) else [v])
                else: yield from walk(v)
        elif isinstance(o,list):
            for v in o: yield from walk(v)
    deny=[os.path.expanduser(d).rstrip('/') for d in walk(j) if isinstance(d,str)]
    hid=any(root==d or root.startswith(d+'/') for d in deny)
    rows.append((cond,cell,'HIDDEN' if hid else 'readable'))
for r in rows: print('\t'.join(r))
print('#N',len(rows),'HIDDEN',sum(r[2]=='HIDDEN' for r in rows),file=sys.stderr)
