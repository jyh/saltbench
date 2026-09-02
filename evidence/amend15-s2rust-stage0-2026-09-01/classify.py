import json, re, collections, sys
P="/Users/jyh/bench-src/verus-proof-synthesis/benchmarks/VeruSAGE-Bench/tasks.jsonl"

def find_fn_items(text, name):
    """Locate every `fn <name>` item. Return list of dicts with mode, body span."""
    out=[]
    for m in re.finditer(r'\bfn\s+'+re.escape(name)+r'\s*[<(]', text):
        ls = text.rfind('\n',0,m.start())+1
        head_prefix = text[ls:m.start()]
        if re.search(r'\bproof\s*$', head_prefix): mode='proof'
        elif re.search(r'\bspec\s*$', head_prefix) or re.search(r'\bspec\s*\([^)]*\)\s*$',head_prefix): mode='spec'
        elif re.search(r'\bexec\s*$', head_prefix): mode='exec'
        else: mode='bare'
        # find the body: first '{' at depth0 after the signature, skipping generics/params
        i=m.end()-1; depth=0; body_start=None
        # scan forward for the top-level '{' that opens the body
        d_par=0; d_ang=0; d_brk=0
        j=m.end()-1
        n=len(text)
        while j<n:
            ch=text[j]
            if ch=='(': d_par+=1
            elif ch==')': d_par-=1
            elif ch=='[': d_brk+=1
            elif ch==']': d_brk-=1
            elif ch=='{':
                if d_par==0 and d_brk==0:
                    body_start=j; break
            elif ch==';' and d_par==0 and d_brk==0:
                body_start=None; break
            j+=1
        if body_start is None:
            out.append(dict(mode=mode,body=None,start=ls)); continue
        # brace match
        k=body_start; depth=0
        while k<n:
            if text[k]=='{': depth+=1
            elif text[k]=='}':
                depth-=1
                if depth==0: break
            k+=1
        out.append(dict(mode=mode, body=text[body_start:k+1], start=ls, bs=body_start, be=k))
    return out

recs=[json.loads(l) for l in open(P)]
pop=[r for r in recs if r["project"] in ("AC","NR")]
cls=collections.Counter(); detail=collections.defaultdict(list)
bodyshapes=collections.Counter()
for r in pop:
    t=r["task"]; name=r["target_function"]
    items=find_fn_items(t,name)
    if not items:
        cls["TARGET_ABSENT"]+=1; detail["TARGET_ABSENT"].append(r["task_id"]); continue
    # lynette rule: candidates = items whose body does NOT contain unimplemented!()
    cands=[it for it in items if it["body"] is not None and "unimplemented!()" not in it["body"]]
    if len(cands)!=1:
        cls["TARGET_AMBIGUOUS(%d of %d)"%(len(cands),len(items))]+=1
        detail["AMB"].append((r["task_id"],len(cands),len(items))); continue
    it=cands[0]
    if it["mode"]!="proof":
        cls["EXEC_OR_OTHER:"+it["mode"]]+=1; detail["nonproof"].append((r["task_id"],it["mode"])); continue
    b=it["body"]
    bodyshapes[repr(b) if len(b)<12 else "OTHER(%d B)"%len(b)]+=1
    if b=="{\n}":
        cls["PROOF_OK"]+=1
    else:
        cls["SHAPE"]+=1; detail["SHAPE"].append((r["task_id"],repr(b[:60])))
print("AC u NR =",len(pop))
for k,v in cls.most_common(): print(f"  {k:32s} {v}")
print()
print("target proof-fn body shapes:")
for k,v in bodyshapes.most_common(8): print(f"  {k:24s} {v}")
print()
print("TARGET_ABSENT sample:", detail["TARGET_ABSENT"][:3])
print("AMBIG sample:", detail["AMB"][:5])
print("nonproof sample:", detail["nonproof"][:5])
print("SHAPE sample:", detail["SHAPE"][:5])
