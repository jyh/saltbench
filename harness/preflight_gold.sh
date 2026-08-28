#!/bin/bash
# preflight_gold.sh — the two ARM-INDEPENDENT controls of EXCLUSIONS.md, run BEFORE either arm, on
# every task in the subset: (i) pre-flight = EMPTY patch must give all-F2P-fail + all-P2P-pass;
# (ii) gold-control = the gold patch must resolve. Both through the pinned official harness in the
# bridged images. Rows are written for ALL tasks, survivors included.
#   usage: preflight_gold.sh <ids...>      env: BENCH · H · PY (python with swebench==4.1.0)
set -u
BENCH="${BENCH:-$HOME/bench}"; H="${H:-$BENCH/harness}"; PY="${PY:-$BENCH/venv/bin/python}"
OUT="$BENCH/state/controls"; mkdir -p "$OUT"; cd "$OUT" || exit 1
[ $# -ge 1 ] || { echo "usage: preflight_gold.sh <instance_ids...>"; exit 2; }
"$PY" -c "import swebench,importlib.metadata as m; assert m.version('swebench')=='4.1.0', m.version('swebench')" || exit 3
bash "$H/bridge_assert.sh" "$@" || exit 4
# ⛔ swebench 4.1.0 DROPS empty-patch predictions before evaluation (run_evaluation.py: empty_patch_ids), so
# the pre-flight is a NO-OP patch: it applies, touches no code, and the harness grades the unmodified tree
# (refuter F4). The marker file is outside every test path.
: > noop_preds.jsonl
NOOP='diff --git a/.swebench_preflight b/.swebench_preflight\nnew file mode 100644\nindex 0000000..e69de29\n'
for i in "$@"; do printf '{"instance_id":"%s","model_name_or_path":"noop","model_patch":"%s"}\n' "$i" "$NOOP" >> noop_preds.jsonl; done
"$PY" -m swebench.harness.run_evaluation -d "$H/data/verified.json" -s test -i "$@" -p noop_preds.jsonl \
   --namespace swebench --instance_image_tag latest --max_workers 1 --timeout 1800 --cache_level instance -id preflight --report_dir "$OUT" > preflight.out 2>&1; rc1=$?
tail -3 preflight.out; [ "$rc1" = 0 ] || { echo "preflight harness rc=$rc1"; exit 5; }
"$PY" -m swebench.harness.run_evaluation -d "$H/data/verified.json" -s test -i "$@" -p gold \
   --namespace swebench --instance_image_tag latest --max_workers 1 --timeout 1800 --cache_level instance -id goldcontrol --report_dir "$OUT" > goldcontrol.out 2>&1; rc2=$?
tail -3 goldcontrol.out; [ "$rc2" = 0 ] || { echo "goldcontrol harness rc=$rc2"; exit 5; }
"$PY" - "$OUT" "$@" <<'PY'
import json,sys,glob,os
out=sys.argv[1]; ids=sys.argv[2:]
def rep(run,i):
    for p in glob.glob(os.path.join("logs","run_evaluation",run,"*",i,"report.json")):
        return json.load(open(p)).get(i,{})
    return None
rows=[]
for i in ids:
    pf=rep("preflight",i) or {}; gd=rep("goldcontrol",i) or {}
    t=pf.get("tests_status",{})
    f2p_fail_all = pf and not t.get("FAIL_TO_PASS",{}).get("success") and t.get("FAIL_TO_PASS",{}).get("failure")
    p2p_pass_all = pf and not t.get("PASS_TO_PASS",{}).get("failure")
    row={"instance_id":i,"preflight_ok":bool(f2p_fail_all and p2p_pass_all),"preflight_report":bool(pf),
         "gold_resolved":bool(gd.get("resolved")),"gold_report":bool(gd),
         "excluded": not (bool(f2p_fail_all and p2p_pass_all) and bool(gd.get("resolved")))}
    rows.append(row); print(json.dumps(row,sort_keys=True))
json.dump(rows,open(os.path.join(out,"controls.json"),"w"),indent=1,sort_keys=True)
print("EXCLUDED:",[r["instance_id"] for r in rows if r["excluded"]])
PY
