import json,os,glob,hashlib
U15=['problem_%d'%i for i in [73,0,146,16,4,38,142,96,112,141,31,54,127,18,74]]
n=0;first=0;fb=0;same=0;miss=0
for root in ['/Users/jyh/bench','/Users/jyh/bench-a8']:
    for m in glob.glob(os.path.join(root,'state','ep-*','manifest.json')):
        d=json.load(open(m))
        if d.get('stage')!='B': continue
        pid=d.get('instance_id')
        if pid not in U15: continue
        n+=1
        p=os.path.join(root,'state','s2',pid,d['arm'],'A.bodies.json')
        a=d.get('a_bodies_sha256')
        if os.path.exists(p) and a and hashlib.sha256(open(p,'rb').read()).hexdigest()==a: first+=1
        else:
            ae=d.get('a_episode'); p2=os.path.join(root,'state',ae,'bodies.json') if ae else None
            if p2 and os.path.exists(p2):
                fb+=1
                g1=json.load(open(p)).get('generated_spec_body') if os.path.exists(p) else None
                g2=json.load(open(p2)).get('generated_spec_body')
                if g1==g2: same+=1
            else: miss+=1
print(json.dumps(dict(stageB_U15_rows=n, first_branch_taken=first, fallback_taken=fb,
                      fallback_text_equals_staged=same, neither=miss)))
