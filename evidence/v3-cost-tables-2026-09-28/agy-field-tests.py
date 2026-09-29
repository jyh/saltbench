import json,sys,glob,os,csv
# ADDENDUM 2's two per-request field tests, over every agy stream of record (each DONE step with usage, deduped by conversation and step):
#   (a) is thinking > output?   If output INCLUDES thinking, no request can show it.
#   (b) is cache_read > input?  If input INCLUDES cache reads, no request can show it.
# usage: agy-field-tests.py <cellroots.tsv> [cache]   (the second argument selects test (b))
n=gt=eq=zero_t=0; mx=0.0; ex=None
paths=[]
for row in csv.DictReader((l for l in open(sys.argv[1]) if not l.startswith('#')),delimiter='\t'):
    if row['shape']!='AGY': continue
    for base in (os.path.expanduser('~/%s/%s/ctl'%(row['root'],row['cell'])),)+tuple(glob.glob(os.path.expanduser('~/%s/_aside/%s/phase*/ctl'%(row['root'],row['cell'])))):
        paths+=glob.glob(base+'/stream-*.ndjson')
seen=set()
for p in paths:
    for l in open(p,errors='replace'):
        try: r=json.loads(l)
        except Exception: continue
        su=r.get('step_update')
        if not isinstance(su,dict) or su.get('state')!='DONE' or not su.get('usage'): continue
        k=(su.get('conversation_id'),su.get('step_index'))
        if k in seen: continue
        seen.add(k); u=su['usage']; o,t=((int(u.get('input_tokens',0) or 0),int(u.get('cache_read_tokens',0) or 0)) if len(sys.argv)>2 else (int(u.get('output_tokens',0) or 0),int(u.get('thinking_tokens',0) or 0)))
        n+=1
        if t==0: zero_t+=1
        if t>o: gt+=1; ex=ex or (p.split('/')[-3],k[1],o,t)
        if t==o: eq+=1
        if o: mx=max(mx,t/o)
a,b=('input','cache_read') if len(sys.argv)>2 else ('output','thinking')
print(json.dumps({'test':'(b) cache_read vs input' if len(sys.argv)>2 else '(a) thinking vs output','streams':len(paths),'steps':n,
  '%s_gt_%s'%(b,a):gt,'%s_eq_%s'%(b,a):eq,'%s_zero'%b:zero_t,'max_%s_over_%s'%(b,a):round(mx,4),'first_gt':ex}))
