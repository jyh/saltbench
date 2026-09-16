import glob, io, json, os, re, collections
CFG="$HOME/<run-config-dir>"
NEEDLE=re.compile(r"cost \(USD\): cap ([0-9.]+) spent ([0-9.]+) remaining (-?[0-9.]+)")
HEADER="# BUDGET (written by the harness)"
cells=sorted(c for c in glob.glob("$HOME/cells-hc1-*/hc1*") if os.path.isdir(c) and os.path.exists(c+"/ctl/end-1"))
x=collections.Counter()
for c in cells:
    slug=os.path.join(CFG,"projects",os.path.realpath(c+"/repo").replace("/","-"))
    f=sorted(glob.glob(slug+"/*.jsonl"))[0]
    uses=set(); res={}
    for l in io.open(f,encoding="utf-8",errors="replace"):
        r=json.loads(l); cont=(r.get("message") or {}).get("content")
        if not isinstance(cont,list): continue
        for b in cont:
            if not isinstance(b,dict): continue
            if b.get("type")=="tool_use" and "BUDGET.md" in json.dumps(b.get("input") or {}): uses.add(b["id"])
            if b.get("type")=="tool_result":
                cc=b.get("content"); res[b.get("tool_use_id")]=cc if isinstance(cc,str) else "\n".join((y.get("text") or "") if isinstance(y,dict) else str(y) for y in (cc or []))
    for i in uses:
        t=res.get(i,"")
        x[("countdown-regex" if NEEDLE.search(t) else "no-regex", "header" if HEADER in t else "no-header")]+=1
print("cross-tab over every BUDGET.md tool_use in 42 head transcripts (method 1 = countdown regex, method 2 = the file's own header line):")
for k,v in sorted(x.items()): print("  ",k,v)
