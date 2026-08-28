#!/bin/bash
# run_stage0.sh — the stage-0 driver: first k pilot tasks in draw order, TASK-MAJOR, arm order alternating
# per task (odd tasks a0 then a1; even tasks a1 then a0), strictly sequential.
#   usage: run_stage0.sh <k> [start_index]     env: BENCH · H · ARMS ("a0 a1")
# Rules (refuter P2/F7/R1/R2/R3): a task-arm is SKIPPED only on a terminal landing (DONE|ROUNDS_EXHAUSTED|
# WALLCLOCK|TOKEN_CEILING, VOID variants included — a VOID is terminal and reported, never re-run);
# QUOTA/ERROR/HARNESS_ERROR get exactly ONE retry, then the driver HALTS (no scoring of half a night);
# the driver HALTS after 2 consecutive non-terminal landings; NO predictions are written here —
# predictions.py builds them from manifests after the batch. The episode id is taken from the episode's own
# EPISODE line and the landing must name (ep, iid, arm) exactly, else HALT.
set -u
K="${1:?k}"; START="${2:-1}"; BENCH="${BENCH:-$HOME/bench}"; H="${H:-$BENCH/harness}"; ARMS="${ARMS:-a0 a1}"
mkdir -p "$BENCH/logs" "$BENCH/state"; L="$BENCH/logs/landings.log"; RL="$BENCH/logs/run_stage0.log"; touch "$L"
ids=$(python3 -c "import json;print(' '.join(json.load(open('$H/TASKLIST.json'))['pilot'][:$K]))")
n=0; badrun=0
terminal() { grep -E "^[^ ]+ $1 $2 (VOID\([^)]*:)?(DONE|ROUNDS_EXHAUSTED|WALLCLOCK|TOKEN_CEILING)" "$L" >/dev/null 2>&1; }
run_one() { # iid arm -> prints term
  local iid="$1" arm="$2" out ep land
  out=$(ARM="$arm" H="$H" BENCH="$BENCH" bash "$H/episode.sh" "$iid" 2>&1 | tee -a "$RL")
  ep=$(printf '%s\n' "$out" | grep -m1 '^EPISODE ' | cut -d' ' -f2)
  land=$(tail -1 "$L")
  case "$land" in "$ep $iid $arm "*) printf '%s\n' "${land#$ep $iid $arm }" ;; *) echo "MISMATCH($ep:$land)" ;; esac
}
for iid in $ids; do
  n=$((n+1)); [ "$n" -lt "$START" ] && continue
  if [ $((n % 2)) -eq 1 ]; then order="$ARMS"; else order=$(printf '%s\n' $ARMS | tail -r | tr '\n' ' '); fi
  for arm in $order; do
    if terminal "$iid" "$arm"; then echo "skip $iid $arm (terminal landing exists)"; continue; fi
    echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) START task#$n $iid arm=$arm" | tee -a "$RL"
    term=$(run_one "$iid" "$arm"); echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) LANDED task#$n $iid arm=$arm term=$term" | tee -a "$RL"
    case "$term" in
      DONE*|ROUNDS_EXHAUSTED*|WALLCLOCK*|TOKEN_CEILING*|VOID*) badrun=0 ;;
      *) echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) RETRY task#$n $iid arm=$arm after $term" | tee -a "$RL"; sleep 60
         term=$(run_one "$iid" "$arm"); echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) LANDED(retry) task#$n $iid arm=$arm term=$term" | tee -a "$RL"
         case "$term" in DONE*|ROUNDS_EXHAUSTED*|WALLCLOCK*|TOKEN_CEILING*|VOID*) badrun=0 ;; *) badrun=$((badrun+1)) ;; esac ;;
    esac
    if [ "$badrun" -ge 1 ]; then echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) HALT: non-terminal landing after retry ($term) — operator's eyes, not a third try" | tee -a "$RL"; exit 2; fi
  done
done
echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) STAGE0 DRIVER DONE k=$K" | tee -a "$RL"
