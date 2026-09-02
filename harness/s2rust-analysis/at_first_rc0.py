#!/usr/bin/env python3
"""atfirst.py — per-episode METERED-AT-FIRST-rc0 and the referee-call index of that run.

⛔ Two units are reported and NEITHER is MAX_TURNS's. `calls_to_first_rc0` counts REFEREE invocations;
`metered_at_first_rc0` counts tokens. The cap is on model turns, and this seat has already been caught once
publishing a turn-shaped number that was not in the cap's unit — so neither of these is offered as a cap.
They price ITERATION: what reaching a first clean proof actually costs.
"""
import glob, json, os, statistics as st
rows=[]
for d in sorted(glob.glob(os.path.expanduser("~/bench-rust/state/ep-*"))):
    j=os.path.join(d,"session.jsonl"); m=os.path.join(d,"manifest.json")
    if not (os.path.exists(j) and os.path.exists(m)): continue
    man=json.load(open(m))
    if man.get("arm")!="a0" or str(man.get("termination","")).startswith("DRYEXEC"): continue
    seen=set(); cum=0; rc0_cum=None; refcalls=0; rc0_call=None
    for line in open(j):
        try: dd=json.loads(line)
        except Exception: continue
        msg=dd.get("message") or {}
        u=msg.get("usage") or {}; mid=msg.get("id")
        if u and mid and mid not in seen:
            seen.add(mid)
            cum += (u.get("input_tokens",0)+u.get("cache_creation_input_tokens",0)
                    +u.get("cache_read_input_tokens",0)+u.get("output_tokens",0))
        for b in (msg.get("content") or []):
            if isinstance(b,dict) and b.get("type")=="tool_result":
                c=b.get("content"); txt=c if isinstance(c,str) else json.dumps(c)
                if "verification results::" in txt:
                    refcalls+=1
                    if "0 errors" in txt and rc0_cum is None:
                        rc0_cum=cum; rc0_call=refcalls
    rows.append(dict(ep=os.path.basename(d), cls=man.get("check_class"), total=man.get("metered_sum"),
                     refcalls=refcalls, rc0_call=rc0_call, rc0_cum=rc0_cum))
print("%-13s %-13s %11s %6s %6s %13s %7s" % ("episode","class","total tok","refs","@ref","tok@first rc0","% of tot"))
for r in rows:
    pct = ("%.0f%%" % (100*r["rc0_cum"]/r["total"])) if (r["rc0_cum"] and r["total"]) else "-"
    print("%-13s %-13s %11s %6s %6s %13s %7s" % (r["ep"], r["cls"], f"{r['total']:,}", r["refcalls"],
          r["rc0_call"] or "NEVER", f"{r['rc0_cum']:,}" if r["rc0_cum"] else "-", pct))
got=[r for r in rows if r["rc0_cum"]]
if got:
    v=[r["rc0_cum"] for r in got]; c=[r["rc0_call"] for r in got]
    print("\nSIGHTED n=%d" % len(got))
    print("  referee calls to first rc0 : median %s  p90 %s  max %s" % (st.median(c), sorted(c)[int(.9*len(c))], max(c)))
    print("  metered at first rc0       : median %s  p90 %s  max %s" %
          (f"{st.median(v):,.0f}", f"{sorted(v)[int(.9*len(v))]:,}", f"{max(v):,}"))
    frac=[r["rc0_cum"]/r["total"] for r in got if r["total"]]
    print("  fraction of the episode spent BEFORE the first clean run: median %.0f%%" % (100*st.median(frac)))
