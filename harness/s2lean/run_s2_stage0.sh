#!/bin/bash
# run_s2_stage0.sh — the S2-Lean stage-0 driver, one STAGE at a time over the first k problems of the seeded draw:
#   usage: run_s2_stage0.sh <A|B|C> <k> [start_index]     env: BENCH · H · ARMS ("a0 a1")
# Order: all stage-A episodes (both arms, task-major, arm order alternating per problem) → the seat ships the
# ground-truth views → all stage-B → all stage-C. Same terminality/retry/hold rules as S1's driver; no predictions
# written here (s2_morning_line.py reads manifests). Episode ids come from the episode's own EPISODE line.
set -u
STAGE="${1:?A|B|C}"; K="${2:?k}"; START="${3:-1}"; BENCH="${BENCH:-$HOME/bench}"; H="${H:-$BENCH/harness}"; ARMS="${ARMS:-a0 a1}"
unset MAX_TURNS PROMPT_OVERRIDE LANDINGS AGENT_PATH MODEL EFFORT CLAUDE_BIN CLAUDE_BIN_STUB WALL_S TOKEN_CEILING
if [ -z "${CAFFEINATED:-}" ] && command -v caffeinate >/dev/null 2>&1; then exec env CAFFEINATED=1 caffeinate -dims bash "$0" "$@"; fi
mkdir -p "$BENCH/logs" "$BENCH/state"; L="$BENCH/logs/s2-landings.log"; RL="$BENCH/logs/run_s2_stage0.log"; touch "$L"
ids=$(python3 "$H/s2lean/draw.py" "$K")
stamp() { date -u +%Y-%m-%dT%H:%M:%SZ; }
is_terminal() { case "$1" in DONE*|ROUNDS_EXHAUSTED*|WALLCLOCK*|TOKEN_CEILING*|VOID\(*) return 0 ;; *) return 1 ;; esac; }
has_terminal() { grep -E "^[^ ]+ $1 $2 $3 (VOID\(|DONE|ROUNDS_EXHAUSTED|WALLCLOCK|TOKEN_CEILING)" "$L" >/dev/null 2>&1; }
run_one() { local t="$1" arm="$2" out ep land
  out=$(printf '%s\n' "$arm" | H="$H" BENCH="$BENCH" bash "$H/s2lean/episode_s2.sh" "${t#problem_}" "$STAGE" 2>&1 | tee -a "$RL")
  ep=$(printf '%s\n' "$out" | grep -m1 '^EPISODE ' | cut -d' ' -f2); land=$(tail -1 "$L")
  case "$land" in "$ep $t $STAGE $arm "*) printf '%s\n' "${land#$ep $t $STAGE $arm }" | cut -d' ' -f1 ;; *) echo "MISMATCH($ep:$land)" ;; esac; }
n=0
for t in $ids; do
  n=$((n+1)); [ "$n" -lt "$START" ] && continue
  if [ $((n % 2)) -eq 1 ]; then order="$ARMS"; else order=$(printf '%s\n' $ARMS | tail -r | tr '\n' ' '); fi
  for arm in $order; do
    if has_terminal "$t" "$STAGE" "$arm"; then echo "skip $t $STAGE $arm (terminal landing exists)"; continue; fi
    if [ "$STAGE" = "B" ] && [ ! -s "$BENCH/state/s2/$t/$arm/A.bodies.json" ]; then echo "$(stamp) skip $t B $arm (no stage-A body)" | tee -a "$RL"; continue; fi
    echo "$(stamp) START #$n $t stage=$STAGE" | tee -a "$RL"
    term=$(run_one "$t" "$arm"); echo "$(stamp) LANDED #$n $t $STAGE arm=$arm term=$term" | tee -a "$RL"
    if ! is_terminal "$term"; then
      case "$term" in QUOTA*|AUTH*) held=0; while ! is_terminal "$term" && [ "$held" -lt 12 ]; do held=$((held+1)); echo "$(stamp) HOLD #$n $t ($term) step $held/12" | tee -a "$RL"; sleep 1800; term=$(run_one "$t" "$arm"); echo "$(stamp) LANDED(hold) #$n $t $STAGE arm=$arm term=$term" | tee -a "$RL"; done ;;
        *) echo "$(stamp) RETRY #$n $t after $term" | tee -a "$RL"; sleep 60; term=$(run_one "$t" "$arm"); echo "$(stamp) LANDED(retry) #$n $t $STAGE arm=$arm term=$term" | tee -a "$RL" ;; esac
      if ! is_terminal "$term"; then echo "$(stamp) HALT: non-terminal ($term) after retry/hold" | tee -a "$RL"; exit 2; fi
    fi
  done
done
echo "$(stamp) S2 STAGE $STAGE DRIVER DONE k=$K" | tee -a "$RL"
