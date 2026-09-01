import json,os,glob,statistics as st
U15=['problem_%d'%i for i in [73,0,146,16,4,38,142,96,112,141,31,54,127,18,74]]
rows=[]
for r in ['/Users/jyh/bench-a8']:
    for m in glob.glob(os.path.join(r,'state','ep-*','manifest.json')):
        d=json.load(open(m))
        if d.get('instance_id') not in U15: continue
        mj=os.path.join(os.path.dirname(m),'meter.json')
        tot=None
        if os.path.exists(mj):
            try:
                md=json.load(open(mj)); tot=md.get('total') or md.get('metered_total') or md.get('sum')
                if tot is None:
                    c=md.get('classes') or {}
                    tot=sum(v for v in c.values() if isinstance(v,(int,float)))
            except Exception: pass
        rows.append(dict(stage=d.get('stage'),arm=d.get('arm'),pid=d['instance_id'],calls=d.get('calls'),
            wall=d.get('wall_s') or d.get('wall'),tok=tot,term=d.get('termination'),
            passed=(d.get('check') or {}).get('passed')))
print(json.dumps(rows))
