import os,re,json,glob
D='/Users/jyh/clever-gt/src/lean4/human_eval'
def sec(txt,name):
    m=re.search(r'-- start_def %s\n(.*?)-- end_def %s'%(re.escape(name),re.escape(name)),txt,re.S)
    return m.group(1) if m else None
out={}
for p in sorted(glob.glob(os.path.join(D,'problem_*.lean'))):
    pid=os.path.basename(p)[:-5]
    t=open(p).read()
    impl=sec(t,'implementation'); pf=sec(t,'correctness_proof')
    def strip(s):
        if s is None: return None
        s=re.sub(r'--[^\n]*','',s); s=re.sub(r'/-.*?-/','',s,flags=re.S)
        return s
    si,sp=strip(impl),strip(pf)
    out[pid]=dict(
        has_impl=bool(si and si.strip()),
        impl_sorry=bool(si and re.search(r'\bsorry\b',si)),
        proof_present=pf is not None,
        proof_sorry=bool(sp and re.search(r'\bsorry\b',sp)),
        proof_chars=len(sp.strip()) if sp else 0)
print(json.dumps(out))
