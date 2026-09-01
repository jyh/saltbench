import json,os,sys,glob,hashlib
roots=sys.argv[1:]
U15=['problem_%d'%i for i in [73,0,146,16,4,38,142,96,112,141,31,54,127,18,74]]
SCORED={'DONE','ROUNDS_EXHAUSTED','WALLCLOCK','TOKEN_CEILING'}
out=[]
for r in roots:
    for m in sorted(glob.glob(os.path.join(r,'state','ep-*','manifest.json'))):
        try: d=json.load(open(m))
        except Exception: continue
        if d.get('stage')!='B': continue
        pid=d.get('instance_id') or d.get('problem_id')
        if pid not in U15: continue
        term=str(d.get('termination') or '')
        base=term.split('+')[0]
        ep=os.path.basename(os.path.dirname(m))
        ck=d.get('check') or {}
        bod=os.path.join(os.path.dirname(m),'bodies.json')
        b={}
        if os.path.exists(bod):
            try: b=json.load(open(bod))
            except Exception: b={}
        out.append(dict(root=os.path.basename(r),ep=ep,pid=pid,arm=d.get('arm'),cls=ck.get('class'),
            passed=ck.get('passed'),term=term,base=base,scored=base in SCORED,end=d.get('end_utc'),
            calls=d.get('calls'),a_ep=d.get('a_episode'),a_sha=d.get('a_bodies_sha256'),
            sorry_lines=ck.get('sorry_lines'),axioms=ck.get('axioms'),screen=ck.get('screen'),
            body_keys=sorted(b.keys()), bodies=b))
print(json.dumps(out))
