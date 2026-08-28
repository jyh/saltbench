#!/bin/bash
# run_stage0.sh — the stage-0 driver: first k pilot tasks in draw order, TASK-MAJOR, arm order
# alternating per task (odd tasks a0 then a1; even tasks a1 then a0), strictly sequential.
#   usage: run_stage0.sh <k> [start_index]     env: BENCH · H · ARMS (default "a0 a1")
# Each landing appends to $BENCH/logs/landings.log and a predictions line to predictions-<arm>.jsonl.
# A stopped run resumes with start_index; a task already landed for an arm is skipped (idempotent).
set -u
K="${1:?k}"; START="${2:-1}"; BENCH="${BENCH:-$HOME/bench}"; H="${H:-$BENCH/harness}"; ARMS="${ARMS:-a0 a1}"
mkdir -p "$BENCH/logs" "$BENCH/state"
ids=$(python3 -c "import json;print(' '.join(json.load(open('$H/TASKLIST.json'))['pilot'][:$K]))")
n=0
for iid in $ids; do
  n=$((n+1)); [ "$n" -lt "$START" ] && continue
  if [ $((n % 2)) -eq 1 ]; then order="$ARMS"; else order=$(printf '%s\n' $ARMS | tail -r | tr '\n' ' '); fi
  for arm in $order; do
    if grep -q " $iid $arm " "$BENCH/logs/landings.log" 2>/dev/null; then echo "skip $iid $arm (landed)"; continue; fi
    echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) START task#$n $iid arm=$arm" | tee -a "$BENCH/logs/run_stage0.log"
    H="$H" BENCH="$BENCH" bash "$H/episode.sh" "$iid" "$arm" 2>&1 | tee -a "$BENCH/logs/run_stage0.log" | grep -E "LANDED|HARNESS_ERROR|WATCHDOG"
    ep=$(tail -1 "$BENCH/logs/landings.log" | cut -d' ' -f1)
    if [ -s "$BENCH/state/$ep/model_patch.diff" ]; then
      python3 - "$BENCH/state/$ep/model_patch.diff" "$iid" "$arm" >> "$BENCH/state/predictions-$arm.jsonl" <<'PY'
import json,sys
print(json.dumps({"instance_id":sys.argv[2],"model_name_or_path":"stage0-"+sys.argv[3],"model_patch":open(sys.argv[1]).read()}))
PY
    else
      printf '{"instance_id":"%s","model_name_or_path":"stage0-%s","model_patch":""}\n' "$iid" "$arm" >> "$BENCH/state/predictions-$arm.jsonl"
    fi
  done
done
echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) STAGE0 DRIVER DONE k=$K" | tee -a "$BENCH/logs/run_stage0.log"
