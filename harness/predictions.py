#!/usr/bin/env python3
"""predictions.py — build predictions-<arm>.jsonl from <STATE>/*/manifest.json AFTER the batch.
Scorable terminations: DONE, ROUNDS_EXHAUSTED, WALLCLOCK, TOKEN_CEILING (NO_PATCH variants score as
empty patches = unsolved). VOID / QUOTA / ERROR / HARNESS_ERROR / DRY / SMOKE rows are NEVER scored:
they are listed in predictions-excluded.json with their reason. One row per (instance, arm): the latest
terminal manifest wins; duplicates are reported.   usage: predictions.py <STATE dir> <out dir>"""
import glob, json, os, sys
SCORABLE = ("DONE", "ROUNDS_EXHAUSTED", "WALLCLOCK", "TOKEN_CEILING")
st, out = sys.argv[1], sys.argv[2]
rows, excl, dups = {}, [], []
for mp in sorted(glob.glob(os.path.join(st, "*", "manifest.json"))):
    m = json.load(open(mp)); t = m.get("termination", ""); key = (m["instance_id"], m["arm"])
    base = t.split("+")[0]
    if base in SCORABLE and not t.startswith("VOID") and not t.startswith("HARNESS_ERROR"):
        if key in rows: dups.append({"key": key, "kept": m["episode"], "dropped": rows[key]["episode"]})
        patch = open(os.path.join(os.path.dirname(mp), "model_patch.diff")).read() if m.get("model_patch_bytes") else ""
        rows[key] = {"episode": m["episode"], "instance_id": m["instance_id"], "model_name_or_path": "stage0-" + m["arm"], "model_patch": patch, "termination": t}
    else:
        excl.append({"episode": m["episode"], "instance_id": m["instance_id"], "arm": m["arm"], "termination": t})
arms = sorted({a for (_, a) in rows})
for a in arms:
    with open(os.path.join(out, "predictions-%s.jsonl" % a), "w") as f:
        for (i, arm), r in sorted(rows.items()):
            if arm == a: f.write(json.dumps({k: r[k] for k in ("instance_id", "model_name_or_path", "model_patch")}) + "\n")
json.dump({"excluded": excl, "duplicates": [{"key": list(d["key"]), "kept": d["kept"], "dropped": d["dropped"]} for d in dups]}, open(os.path.join(out, "predictions-excluded.json"), "w"), indent=1)
print("scorable rows:", {a: sum(1 for (_, x) in rows if x == a) for a in arms}, "excluded:", len(excl), "duplicates:", len(dups))
