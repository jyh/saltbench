import json, re, collections, statistics, sys
P="/Users/jyh/bench-src/verus-proof-synthesis/benchmarks/VeruSAGE-Bench/tasks.jsonl"
recs=[json.loads(l) for l in open(P)]
print("records:", len(recs))
print("fields:", sorted(recs[0].keys()))
print()
c=collections.Counter(r["project"] for r in recs)
for k,v in c.most_common(): print(f"  project {k!r:40s} {v}")
print()
cn=collections.Counter(r.get("project_name") for r in recs)
for k,v in cn.most_common(): print(f"  project_name {k!r:40s} {v}")
