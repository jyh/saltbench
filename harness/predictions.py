#!/usr/bin/env python3
"""predictions.py — build predictions-<arm>.jsonl from <STATE>/*/manifest.json AFTER the batch.
Scorable terminations: DONE, ROUNDS_EXHAUSTED, WALLCLOCK, TOKEN_CEILING (NO_PATCH variants score as
empty patches = unsolved). VOID / QUOTA / ERROR / HARNESS_ERROR / DRY / SMOKE rows are NEVER scored:
they are listed in predictions-excluded.json with their reason. One row per (instance, arm): the latest
terminal manifest wins; duplicates are reported.   usage: predictions.py <STATE dir> <out dir>"""
import glob, json, os, sys
SCORABLE = ("DONE", "ROUNDS_EXHAUSTED", "WALLCLOCK", "TOKEN_CEILING")
st, out = sys.argv[1], sys.argv[2]
ARMS = set(sys.argv[3].split(",")) if len(sys.argv) > 3 else {"a0", "a1"}   # smoke arms (s*) are never scored
rows, excl, dups = {}, [], []
mans = [json.load(open(mp)) | {"_dir": os.path.dirname(mp)} for mp in glob.glob(os.path.join(st, "*", "manifest.json"))]
excl_ids = set()
cj = os.path.join(st, "controls.json")
if os.path.exists(cj):
    excl_ids = {r["instance_id"] for r in json.load(open(cj)) if r.get("excluded")}
for m in sorted(mans, key=lambda m: (m.get("end_utc") or 0)):   # LATEST BY END TIME wins, never by random episode id (refuter RI3-R3)
    mp = os.path.join(m["_dir"], "manifest.json"); t = m.get("termination", ""); key = (m["instance_id"], m["arm"])
    if m["instance_id"] in excl_ids:
        excl.append({"episode": m["episode"], "instance_id": m["instance_id"], "arm": m["arm"], "termination": t, "reason": "EXCLUDED by pre-flight/gold-control"}); continue
    if m["arm"] not in ARMS or t.startswith(("SMOKE", "DRY")):   # DRY and DRYEXEC rows are never scored
        continue
    base = t.split("+")[0]
    if base in SCORABLE:
        if key in rows: dups.append({"key": key, "kept": m["episode"], "kept_end_utc": m.get("end_utc"), "dropped": rows[key]["episode"], "dropped_end_utc": rows[key].get("end_utc")})
        patch = open(os.path.join(os.path.dirname(mp), "model_patch.diff")).read() if m.get("model_patch_bytes") else ""
        rows[key] = {"episode": m["episode"], "end_utc": m.get("end_utc"), "instance_id": m["instance_id"], "model_name_or_path": "stage0-" + m["arm"], "model_patch": patch, "termination": t}
    else:
        excl.append({"episode": m["episode"], "instance_id": m["instance_id"], "arm": m["arm"], "termination": t})
arms = sorted({a for (_, a) in rows})
for a in arms:
    with open(os.path.join(out, "predictions-%s.jsonl" % a), "w") as f:
        for (i, arm), r in sorted(rows.items()):
            if arm == a: f.write(json.dumps({k: r[k] for k in ("instance_id", "model_name_or_path", "model_patch")}) + "\n")
json.dump({"excluded": excl, "duplicates": [{"key": list(d["key"]), "kept": d["kept"], "kept_end_utc": d["kept_end_utc"], "dropped": d["dropped"], "dropped_end_utc": d["dropped_end_utc"]} for d in dups]}, open(os.path.join(out, "predictions-excluded.json"), "w"), indent=1)
print("scorable rows:", {a: sum(1 for (_, x) in rows if x == a) for a in arms}, "excluded:", len(excl), "duplicates:", len(dups))
