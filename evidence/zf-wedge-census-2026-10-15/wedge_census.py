#!/usr/bin/env python3
"""ZF ADDENDUM 6: census of the WEDGE shape over every agy cell stream on the run box.

A result event is keyed by (conversation_id, duration_seconds, usage). A stream FIRES at K when K
consecutive results are each identical to the one before. Reads the result ENVELOPE only, never the
response text, so it cannot read either arm's vocabulary. Prints one row per stream, then the totals.
Usage: python3 wedge_census.py [K] [GLOB]   (default K=2, GLOB=~/cells*/*/ctl/stream-*.ndjson)
"""
import glob, json, os, sys

K = int(sys.argv[1]) if len(sys.argv) > 1 else 2
pat = sys.argv[2] if len(sys.argv) > 2 else "~/cells*/*/ctl/stream-*.ndjson"
home = os.path.expanduser("~") + os.sep
rows = []
for f in sorted(glob.glob(os.path.expanduser(pat))):
    res = []
    for line in open(f, errors="replace"):
        try:
            d = json.loads(line)
        except Exception:
            continue
        if d.get("event") == "result":
            r = d["result"]
            res.append((r.get("conversation_id"), r.get("duration_seconds"),
                        json.dumps(r.get("usage"), sort_keys=True)))
    run = maxrun = 0
    fired = None
    for i in range(1, len(res)):
        run = run + 1 if res[i] == res[i - 1] else 0
        maxrun = max(maxrun, run)
        if run >= K and fired is None:
            fired = i + 1
    armf = os.path.join(os.path.dirname(f), "arm")
    arm = open(armf).read().strip() if os.path.exists(armf) else "NO-ARM-FILE"
    rows.append((f.replace(home, "~/"), arm, len(res), maxrun, fired))

print("K\t%d" % K)
print("stream\tarm\tresults\tmax_identical_run\tfires_at_result")
for r in rows:
    print("\t".join(str(x) for x in r))
for arm in sorted({r[1] for r in rows}):
    sub = [r for r in rows if r[1] == arm]
    print("TOTAL\t%s\tstreams=%d\tfires=%d" % (arm, len(sub), sum(1 for r in sub if r[4])))
print("MAX-RUN-AMONG-NON-FIRING\t%d" % max([r[3] for r in rows if not r[4]] or [0]))
