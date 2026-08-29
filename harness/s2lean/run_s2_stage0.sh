#!/bin/bash
# run_s2_stage0.sh — the S2-Lean stage-0 driver, one STAGE at a time over the first k problems of the seeded draw:
#   usage: run_s2_stage0.sh <A|B|C> <k> [start_index]     env: BENCH · H · EPROOT (~/work) · ARMS ("a0 a1")
#          DRY_RUN=1 (the run-shaped dry: REQUIRES CLAUDE_BIN=<stub> CLAUDE_BIN_STUB=1; lands in dryexec.log, bodies under
#          state/s2-dry, no smoke gate) — without DRY_RUN every probe/dry variable is unset as in S1.
# Order: all stage-A episodes (both arms, task-major, arm order alternating per problem) → the seat ships the ground-truth
# views → all stage-B → all stage-C. Same terminality/retry/hold rules as S1's driver; no predictions written here
# (s2_morning_line.py reads manifests). Episode ids come from the episode's own EPISODE line.
# REPAIR ROUND 1: refuses to start without SMOKE PASS S1–S5 carrying THIS episode_s2.sh sha (D13); sweeps leftover ~/work/ep-*
# and .DS_Store into state/orphans before the loop (M7); stage B without a scored stage-A pass lands the synthetic
# `<none> <task> B <arm> NOT_PROVEN(no_stage_A_pass) 0` (D5, never a skip — M8/F11); stage C of a C-dead view (view_status.json
# c_dead, D7) lands `<none> <task> C <arm> NOT_RUN(view_dead) 0`; a REFUSE from the episode halts at once (it is deterministic).
set -u
STAGE="${1:?A|B|C}"; K="${2:?k}"; START="${3:-1}"; BENCH="${BENCH:-$HOME/bench}"; H="${H:-$BENCH/harness}"; ARMS="${ARMS:-a0 a1}"; EPROOT="${EPROOT:-$HOME/work}"
DRY="${DRY_RUN:-}"
if [ "$DRY" = "1" ]; then
  [ -n "${CLAUDE_BIN_STUB:-}" ] && [ -n "${CLAUDE_BIN:-}" ] && [ -x "$CLAUDE_BIN" ] || { echo "REFUSE: DRY_RUN=1 needs CLAUDE_BIN=<executable stub> and CLAUDE_BIN_STUB=1"; exit 3; }
  unset MAX_TURNS PROMPT_OVERRIDE LANDINGS AGENT_PATH MODEL EFFORT WALL_S TOKEN_CEILING
  L="$BENCH/logs/dryexec.log"; RL="$BENCH/logs/run_s2_stage0.dry.log"; SROOT="$BENCH/state/s2-dry"
else
  [ -z "${DRY}" ] || { echo "REFUSE: DRY_RUN must be 1 or unset"; exit 3; }
  unset MAX_TURNS PROMPT_OVERRIDE LANDINGS AGENT_PATH MODEL EFFORT CLAUDE_BIN CLAUDE_BIN_STUB WALL_S TOKEN_CEILING REFUSE_GIT_CHECK
  L="$BENCH/logs/s2-landings.log"; RL="$BENCH/logs/run_s2_stage0.log"; SROOT="$BENCH/state/s2"
fi
if [ -z "${CAFFEINATED:-}" ] && command -v caffeinate >/dev/null 2>&1; then exec env CAFFEINATED=1 caffeinate -dims bash "$0" "$@"; fi
mkdir -p "$BENCH/logs" "$BENCH/state" "$EPROOT"; touch "$L"
stamp() { date -u +%Y-%m-%dT%H:%M:%SZ; }
# the smoke gate (D13): five PASS lines from THIS freeze's episode_s2.sh, else nothing starts
if [ "$DRY" != "1" ]; then
  esha=$(shasum -a 256 "$H/s2lean/episode_s2.sh" | cut -d' ' -f1); miss=""
  for id in S1 S2 S3 S4 S5; do v=$(grep -E "^SMOKE (PASS|FAIL) $id " "$BENCH/logs/smoke.log" 2>/dev/null | tail -1); printf '%s\n' "$v" | grep -Eq "^SMOKE PASS $id .*episode_s2\.sh=$esha" || miss="$miss $id"; done   # LAST verdict per id, not any PASS (EDH-3)
  [ -z "$miss" ] || { echo "REFUSE: smoke.log lacks SMOKE PASS for$miss from episode_s2.sh=$esha (run smoke_s2.sh first)"; exit 3; }
  echo "$(stamp) SMOKE GATE OK episode_s2.sh=$esha" | tee -a "$RL"
  # controls gate (F7/FN-5): the D14 checker controls must have passed before any scored episode
  cj="$BENCH/state/s2-controls.json"
  python3 -c "import json,sys;sys.exit(0 if json.load(open('$cj')).get('controls_pass') else 1)" 2>/dev/null || { echo "REFUSE: $cj missing or controls_pass!=true (run s2_controls.sh first)"; exit 3; }
  echo "$(stamp) CONTROLS GATE OK" | tee -a "$RL"
else
  echo "$(stamp) DRY_RUN=1: smoke gate skipped; stub=$CLAUDE_BIN; landings=$L; bodies under $SROOT" | tee -a "$RL"
fi
# leftover episode dirs (SIGKILL, power loss, a Finder .DS_Store) would make every episode die at the EPROOT assertion (M7)
for d in "$EPROOT"/ep-* "$EPROOT"/.DS_Store; do [ -e "$d" ] || continue; mkdir -p "$BENCH/state/orphans"; mv "$d" "$BENCH/state/orphans/$(date -u +%Y%m%dT%H%M%SZ)-$(basename "$d")"; echo "$(stamp) SWEPT leftover $d -> state/orphans" | tee -a "$RL"; done
ids=$(python3 "$H/s2lean/draw.py" "$K") || { echo "REFUSE: draw.py failed"; exit 3; }
if [ "$STAGE" = "C" ]; then
  [ -s "$H/s2lean/view_status.json" ] || { echo "REFUSE: $H/s2lean/view_status.json missing — the C-dead list (D7) is not pre-registered"; exit 3; }
  cdead=$(python3 -c "import json;print(' '.join('problem_%s'%i for i in json.load(open('$H/s2lean/view_status.json')).get('c_dead',[])))")
  echo "$(stamp) C-DEAD (view_status.json): $cdead" | tee -a "$RL"
fi
is_terminal() { case "$1" in DONE*|ROUNDS_EXHAUSTED*|WALLCLOCK*|TOKEN_CEILING*|VOID\(*|NOT_PROVEN\(*|NOT_RUN\(*) return 0 ;; *) return 1 ;; esac; }
has_terminal() { grep -E "^[^ ]+ $1 $2 $3 (DRYEXEC\()?(VOID\(|DONE|ROUNDS_EXHAUSTED|WALLCLOCK|TOKEN_CEILING|NOT_PROVEN\(|NOT_RUN\()" "$L" >/dev/null 2>&1; }
synthetic() { printf '<none> %s %s %s %s 0\n' "$1" "$2" "$3" "$4" >> "$L"; echo "$(stamp) SYNTHETIC $1 $2 $3 $4" | tee -a "$RL"; }
run_one() { local t="$1" arm="$2" out ep land term
  out=$(printf '%s\n' "$arm" | H="$H" BENCH="$BENCH" EPROOT="$EPROOT" bash "$H/s2lean/episode_s2.sh" "${t#problem_}" "$STAGE" 2>&1 | tee -a "$RL")
  case "$out" in *"REFUSE:"*) printf 'REFUSED(%s)\n' "$(printf '%s\n' "$out" | grep -m1 'REFUSE:' | cut -c1-160)"; return ;; esac
  ep=$(printf '%s\n' "$out" | grep -m1 '^EPISODE ' | cut -d' ' -f2); land=$(tail -1 "$L")
  case "$land" in "$ep $t $STAGE $arm "*) term=$(printf '%s\n' "${land#$ep $t $STAGE $arm }" | cut -d' ' -f1) ;; *) term="MISMATCH($ep:$land)" ;; esac
  if [ "$DRY" = "1" ]; then case "$term" in DRYEXEC\(*) term="${term#DRYEXEC(}"; term="${term%)}" ;; esac; fi
  printf '%s\n' "$term"; }
n=0
for id in $ids; do
  t="problem_${id#problem_}"
  n=$((n+1)); [ "$n" -lt "$START" ] && continue
  if [ $((n % 2)) -eq 1 ]; then order="$ARMS"; else order=$(printf '%s\n' $ARMS | tail -r | tr '\n' ' '); fi
  for arm in $order; do
    if has_terminal "$t" "$STAGE" "$arm"; then echo "skip $t $STAGE $arm (terminal landing exists)"; continue; fi
    if [ "$STAGE" = "B" ] && [ ! -s "$SROOT/$t/$arm/A.bodies.json" ]; then synthetic "$t" B "$arm" "NOT_PROVEN(no_stage_A_pass)"; continue; fi
    if [ "$STAGE" = "C" ]; then case " $cdead " in *" $t "*) synthetic "$t" C "$arm" "NOT_RUN(view_dead)"; continue ;; esac; fi
    echo "$(stamp) START #$n $t stage=$STAGE" | tee -a "$RL"
    term=$(run_one "$t" "$arm"); echo "$(stamp) LANDED #$n $t $STAGE arm=$arm term=$term" | tee -a "$RL"
    case "$term" in REFUSED*) echo "$(stamp) HALT: the episode refused ($term) — deterministic, not retried" | tee -a "$RL"; exit 2 ;; esac
    if ! is_terminal "$term"; then
      case "$term" in QUOTA*|AUTH*) held=0; while ! is_terminal "$term" && [ "$held" -lt 12 ]; do held=$((held+1)); echo "$(stamp) HOLD #$n $t ($term) step $held/12" | tee -a "$RL"; sleep 1800; term=$(run_one "$t" "$arm"); echo "$(stamp) LANDED(hold) #$n $t $STAGE arm=$arm term=$term" | tee -a "$RL"; done ;;
        *) echo "$(stamp) RETRY #$n $t after $term" | tee -a "$RL"; sleep "${RETRY_SLEEP_S:-60}"; term=$(run_one "$t" "$arm"); echo "$(stamp) LANDED(retry) #$n $t $STAGE arm=$arm term=$term" | tee -a "$RL" ;; esac
      if ! is_terminal "$term"; then echo "$(stamp) HALT: non-terminal ($term) after retry/hold" | tee -a "$RL"; exit 2; fi
    fi
  done
done
echo "$(stamp) S2 STAGE $STAGE DRIVER DONE k=$K" | tee -a "$RL"
