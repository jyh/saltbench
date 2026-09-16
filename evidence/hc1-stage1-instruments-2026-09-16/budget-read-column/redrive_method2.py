import glob, io, json, os, re, collections
CFG="$HOME/<run-config-dir>"
cells=sorted(c for c in glob.glob("$HOME/cells-hc1-*/hc1*") if os.path.isdir(c) and os.path.exists(c+"/ctl/end-1"))
tally=collections.Counter(); samples=collections.defaultdict(list)
for c in cells:
    slug=os.path.join(CFG,"projects",os.path.realpath(c+"/repo").replace("/","-"))
    f=sorted(glob.glob(slug+"/*.jsonl"))[0]
    uses={}; res={}
    for l in io.open(f,encoding="utf-8",errors="replace"):
        r=json.loads(l); cont=(r.get("message") or {}).get("content")
        if not isinstance(cont,list): continue
        for b in cont:
            if not isinstance(b,dict): continue
            if b.get("type")=="tool_use" and "BUDGET.md" in json.dumps(b.get("input") or {}): uses[b["id"]]=json.dumps(b.get("input"))[:160]
            if b.get("type")=="tool_result": res[b.get("tool_use_id")]=json.dumps(b.get("content"))
    for i,inp in uses.items():
        t=res.get(i,"")
        # METHOD 2: broad content words from the file's own header and body, not the countdown regex
        has=[w for w in ("written by the harness","spent","remaining","cost (USD)") if w in t]
        k="ANY-BUDGET-WORD" if has else "NONE"
        tally[k]+=1
        if len(samples[k])<4:
            j=t.find("BUDGET"); samples[k].append((os.path.basename(c), inp[:90], t[max(0,j-40):j+120] if j>=0 else t[-120:]))
print("ALL BUDGET.md tool_uses in head transcripts (reads AND mentions), by method 2:", dict(tally))
for k,v in samples.items():
    print("==",k)
    for s in v: print("  ",s)
