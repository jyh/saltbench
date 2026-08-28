#!/bin/bash
# run_stage0.sh — the stage-0 driver: first k pilot tasks in draw order, TASK-MAJOR, arm order alternating
# per task (odd tasks a0 then a1; even tasks a1 then a0), strictly sequential.
#   usage: caffeinate -dims run_stage0.sh <k> [start_index]     env: BENCH · H · ARMS ("a0 a1")
# Rules (refuters P2/F7/R1/R2/R3/T-R3): a task-arm is SKIPPED only on a TERMINAL landing (DONE|ROUNDS_EXHAUSTED|
# WALLCLOCK|TOKEN_CEILING, with or without a VOID(...) wrapper or +NO_PATCH — VOID is terminal and reported, never
# re-run); HARNESS_ERROR/ERROR_* get exactly ONE retry after 60 s; QUOTA/AUTH are a HOLD, not a halt: the driver
# waits in 30-minute steps for at most 6 h (a hold with a release condition and a timeout), re-runs the SAME
# task-arm once per step, then continues; after the hold expires, or after a retry that is still non-terminal,
# it HALTS for an operator. NO predictions are written here (predictions.py, after the batch). The arm never
# appears in a log line before the episode has landed. The episode id is taken from the episode's own EPISODE
# line and the landing must name (ep, iid, arm) exactly, else HALT.
set -u
K="${1:?k}"; START="${2:-1}"; BENCH="${BENCH:-$HOME/bench}"; H="${H:-$BENCH/harness}"; ARMS="${ARMS:-a0 a1}"
# probe/dry environment never reaches a real episode (refuter T3-R6/RI3-F1); the machine may not sleep (T-R6)
unset MAX_TURNS PROMPT_OVERRIDE LANDINGS AGENT_PATH MODEL EFFORT CLAUDE_BIN CLAUDE_BIN_STUB WALL_S TOKEN_CEILING
if [ -z "${CAFFEINATED:-}" ] && command -v caffeinate >/dev/null 2>&1; then exec env CAFFEINATED=1 caffeinate -dims bash "$0" "$@"; fi
mkdir -p "$BENCH/logs" "$BENCH/state"; L="$BENCH/logs/landings.log"; RL="$BENCH/logs/run_stage0.log"; touch "$L"
ids=$(python3 -c "import json;print(' '.join(json.load(open('$H/TASKLIST.json'))['pilot'][:$K]))")
# the arm-independent exclusions of EXCLUSIONS.md are CONSUMED here (refuter T3-F1): a task excluded by pre-flight/gold never runs
[ -f "$BENCH/state/controls.json" ] || { echo "REFUSE: $BENCH/state/controls.json missing — pre-flight/gold-control (step 4) has not run"; exit 3; }
excluded=$(python3 -c "import json;print(' '.join(r['instance_id'] for r in json.load(open('$BENCH/state/controls.json')) if r['excluded']))")
stamp() { date -u +%Y-%m-%dT%H:%M:%SZ; }
is_terminal() { case "$1" in DONE*|ROUNDS_EXHAUSTED*|WALLCLOCK*|TOKEN_CEILING*|VOID\(*) return 0 ;; *) return 1 ;; esac; }
has_terminal() { grep -E "^[^ ]+ $1 $2 (VOID\(|DONE|ROUNDS_EXHAUSTED|WALLCLOCK|TOKEN_CEILING)" "$L" >/dev/null 2>&1; }
run_one() { # iid arm -> prints term
  local iid="$1" arm="$2" out ep land
  out=$(printf '%s\n' "$arm" | H="$H" BENCH="$BENCH" bash "$H/episode.sh" "$iid" 2>&1 | tee -a "$RL")
  ep=$(printf '%s\n' "$out" | grep -m1 '^EPISODE ' | cut -d' ' -f2)
  land=$(tail -1 "$L")
  case "$land" in "$ep $iid $arm "*) printf '%s\n' "${land#$ep $iid $arm }" | cut -d' ' -f1 ;; *) echo "MISMATCH($ep:$land)" ;; esac
}
n=0
for iid in $ids; do
  n=$((n+1)); [ "$n" -lt "$START" ] && continue
  if [ $((n % 2)) -eq 1 ]; then order="$ARMS"; else order=$(printf '%s\n' $ARMS | tail -r | tr '\n' ' '); fi
  case " $excluded " in *" $iid "*) echo "$(stamp) skip task#$n $iid (EXCLUDED by pre-flight/gold-control)" | tee -a "$RL"; continue ;; esac
  for arm in $order; do
    if has_terminal "$iid" "$arm"; then echo "skip $iid $arm (terminal landing exists)"; continue; fi
    echo "$(stamp) START task#$n $iid" | tee -a "$RL"
    term=$(run_one "$iid" "$arm"); echo "$(stamp) LANDED task#$n $iid arm=$arm term=$term" | tee -a "$RL"
    if ! is_terminal "$term"; then
      case "$term" in
        QUOTA*|AUTH*)
          held=0
          while ! is_terminal "$term" && [ "$held" -lt 12 ]; do
            held=$((held+1)); echo "$(stamp) HOLD task#$n $iid ($term) — step $held/12, 30 min" | tee -a "$RL"; sleep 1800
            term=$(run_one "$iid" "$arm"); echo "$(stamp) LANDED(hold) task#$n $iid arm=$arm term=$term" | tee -a "$RL"
          done ;;
        *)
          echo "$(stamp) RETRY task#$n $iid after $term" | tee -a "$RL"; sleep 60
          term=$(run_one "$iid" "$arm"); echo "$(stamp) LANDED(retry) task#$n $iid arm=$arm term=$term" | tee -a "$RL" ;;
      esac
      if ! is_terminal "$term"; then echo "$(stamp) HALT: non-terminal landing ($term) after retry/hold — operator's eyes, not a third try" | tee -a "$RL"; exit 2; fi
    fi
  done
done
echo "$(stamp) STAGE0 DRIVER DONE k=$K" | tee -a "$RL"
