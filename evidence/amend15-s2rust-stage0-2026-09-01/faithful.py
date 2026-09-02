import json, re, collections
exec(open('/private/tmp/claude-501/-Users-jyh-projects-claude-saltbench/e8874a3b-1986-465f-94d6-7f406589d989/scratchpad/classify.py').read().split('recs=[json.loads')[0])
P="/Users/jyh/bench-src/verus-proof-synthesis/benchmarks/VeruSAGE-Bench/tasks.jsonl"
recs=[json.loads(l) for l in open(P)]
pop=[r for r in recs if r["project"] in ("AC","NR")]

survivors=[]; shape_ws=0; shape_content=0; shape_examples=[]
for r in pop:
    items=find_fn_items(r["task"], r["target_function"])
    if not items: continue
    cands=[it for it in items if it["body"] is not None and "unimplemented!()" not in it["body"]]
    if len(cands)!=1: continue
    it=cands[0]
    if it["mode"]!="proof": continue
    inner=it["body"][1:-1]
    if inner.strip()=="":
        shape_ws += (it["body"]!="{\n}")
        survivors.append((r,it))
    else:
        shape_content+=1
        shape_examples.append((r["task_id"], inner.strip()[:70]))
print("proof-fn targets, body EMPTY modulo whitespace :", len(survivors), "  (of which NOT literally '{\\n}':", shape_ws, ")")
print("proof-fn targets, body carries CONTENT         :", shape_content)
print()
print("CONTENT examples:")
for a,b in shape_examples[:6]: print("   ", a[:55], "->", repr(b))
print()
# UNFAITHFUL test: is gt == task with target body replaced?
ok=0; bad=0; badex=[]
for r,it in survivors:
    gitems=find_fn_items(r["ground_truth"], r["target_function"])
    gc=[x for x in gitems if x["body"] is not None and "unimplemented!()" not in x["body"]]
    if len(gc)!=1: bad+=1; badex.append((r["task_id"],"gt-target-not-unique")); continue
    g=gc[0]
    rebuilt = r["task"][:it["bs"]] + g["body"] + r["task"][it["be"]+1:]
    if rebuilt == r["ground_truth"]: ok+=1
    else: bad+=1; badex.append((r["task_id"], "task!=gt outside the body"))
print("SELF-TEST  assemble(task-skeleton, gt body) == ground_truth :")
print("   REPRODUCES byte-for-byte :", ok)
print("   DOES NOT                 :", bad)
c=collections.Counter(x[1] for x in badex)
for k,v in c.most_common(): print("     ",k,v)
print("   sample:", [x[0][:60] for x in badex[:4]])
