#!/bin/bash
# halt_watch.sh — THE BUDGET/WALL ENFORCER for a stage run (amendment 11, 2026-09-01, desk row AS).
#
# ⛔ WHY THIS FILE IS IN THE REPO AND NOT IN A SCRATCHPAD. This seat has now written the same watch three
# times (amend3_watch.sh, the a8watch, and this) and every previous one lived in a session-scoped scratchpad,
# so it died with its head and the next head rewrote it from a bank paragraph. Banked twice as a law —
# "an enforcer that lives in a session which must exit has an expiry date" — and repaired only now. The
# DESIGN was inherited; the ARTIFACT was not, and only the artifact can be re-armed in one command.
#
# WHAT IT DOES, AND THE ONE THING IT NEVER DOES. It writes $BENCH/HALT and nothing else. The driver reads
# that file INSIDE its arm loop (run_s2_stage0.sh:120) and exits 4 after the episode in flight. This watch
# never signals, never kills: stopping a run mid-episode corrupts the landing the stop rule exists to protect.
#
# THE ARMS, and why each exists:
#   BUDGET   Σ metered_sum over this run's OWN landings ≥ TOK_MAX          ⇒ HALT
#   WALL     now − start ≥ WALL_H hours                                     ⇒ HALT
#   STALL    landings, meter AND the in-flight transcript all static for STALL_MIN minutes ⇒ EVENT (never a
#            HALT: a long episode and a dead driver look identical to an end-of-unit instrument, which is the
#            08/30 law — landings and the meter BOTH move only at episode end, so a healthy 26-minute episode
#            is byte-identical to a corpse unless you read the transcript. Reporting is honest; halting on it
#            would throw away a live episode.)
#   DEAD     no claude process AND no DONE line in the run log, two consecutive polls ⇒ EVENT
#   PROBE    a poll that could not read the state at all ⇒ EVENT (a failed probe must never read as a quiet
#            run — that is how a dead ssh becomes "nothing to report")
#
# usage: halt_watch.sh <BENCH> <STAGE> <ARMS csv> <TOK_MAX> <WALL_H> [--poll SEC] [--stall-min MIN] [--log F]
#                      [--since EPOCH] [--once]
#        halt_watch.sh --selftest
# exit 0 (driver reached DONE, or the watch was asked to stop) · 3 HALT written · 2 REFUSE (bad args)
set -u

usage() { sed -n '2,40p' "$0"; }

# ── the measurement, factored out so the selftest drives THE SAME code the watch runs ──
#    (meter.py's 08/30 defect: its cases passed an argument its caller never passes. One code path only.)
measure() {  # $1=BENCH $2=STAGE $3=ARMS csv $4=since_epoch  -> "<tokens> <landed> <newest_mtime>"
  python3 - "$1" "$2" "$3" "$4" <<'PY'
import json, os, sys
bench, stage, arms, since = sys.argv[1], sys.argv[2], sys.argv[3].split(","), float(sys.argv[4])
tok = landed = 0; newest = 0.0
root = os.path.join(bench, "state")
for dirpath, dirnames, filenames in os.walk(root):
    if "manifest.json" not in filenames: continue
    p = os.path.join(dirpath, "manifest.json")
    try: m = json.load(open(p))
    except Exception: continue
    if m.get("stage") != stage or m.get("arm") not in arms: continue
    # Only THIS run's landings: a shared state root carries earlier stages' episodes and counting them would
    # halt a run that has spent nothing. mtime, not end_utc — a synthetic landing has no end_utc.
    try: mt = os.path.getmtime(p)
    except OSError: continue
    if mt < since: continue
    landed += 1; tok += int(m.get("metered_sum") or 0); newest = max(newest, mt)
print("%d %d %.0f" % (tok, landed, newest))
PY
}

inflight() {  # $1=CFGDIR -> total bytes of the newest transcript + its mtime, "0 0" when there is none
  python3 - "$1" <<'PY'
import os, sys
root = os.path.expanduser(os.path.join(sys.argv[1], "projects"))
best = (0.0, 0)
for dirpath, _d, files in os.walk(root):
    for f in files:
        if not f.endswith(".jsonl"): continue
        p = os.path.join(dirpath, f)
        try: st = os.stat(p)
        except OSError: continue
        if st.st_mtime > best[0]: best = (st.st_mtime, st.st_size)
print("%d %.0f" % (best[1], best[0]))
PY
}

main() {
  BENCH="${1:?BENCH root}"; STAGE="${2:?A|B|C}"; ARMS="${3:?arms csv}"; TOK_MAX="${4:?token max}"; WALL_H="${5:?wall hours}"
  shift 5
  POLL=60; STALL_MIN=12; LOGF=""; CFGDIR="${CFGDIR:-$HOME/.claude-bench}"; ONCE=0; SINCE=""
  while [ $# -gt 0 ]; do case "$1" in
    --poll) POLL="$2"; shift 2 ;; --stall-min) STALL_MIN="$2"; shift 2 ;; --log) LOGF="$2"; shift 2 ;;
    --once) ONCE=1; shift ;; --since) SINCE="$2"; shift 2 ;;
    *) echo "REFUSE: unknown arg $1" >&2; exit 2 ;; esac; done
  case "$SINCE" in ''|*[!0-9]*) [ -z "$SINCE" ] || { echo "REFUSE: --since must be a whole epoch second" >&2; exit 2; } ;; esac
  case "$BENCH" in /*) ;; *) echo "REFUSE: BENCH must be absolute (a relative root is how a watch ends up guarding the wrong run)" >&2; exit 2 ;; esac
  [ -d "$BENCH" ] || { echo "REFUSE: $BENCH does not exist" >&2; exit 2; }
  case "$STAGE" in A|B|C) ;; *) echo "REFUSE: STAGE must be A, B or C" >&2; exit 2 ;; esac
  case "$TOK_MAX" in ''|*[!0-9]*) echo "REFUSE: TOK_MAX must be a whole number of tokens" >&2; exit 2 ;; esac
  printf '%s' "$WALL_H" | grep -Eq '^[0-9]+(\.[0-9]+)?$' || { echo "REFUSE: WALL_H must be a number of hours" >&2; exit 2; }
  [ "$TOK_MAX" -gt 0 ] || { echo "REFUSE: TOK_MAX must be > 0 — a zero budget halts before the first episode" >&2; exit 2; }
  [ -n "$LOGF" ] || LOGF="$BENCH/logs/halt_watch.log"
  mkdir -p "$(dirname "$LOGF")"
  RUNLOG="$BENCH/logs/run_s2_stage0.log"
  # ⛔ TWO CLOCKS, DELIBERATELY SEPARATED. START is the WALL arm's origin. SINCE is the spend window's floor —
  # which landing counts as this run's. They are the same by default and MUST be separable, because a landing
  # written in the same second the watch arms is on the wrong side of an integer boundary: the selftest went
  # INTERMITTENT on exactly that race (3 arms red on one run in ten, green on the rest). An intermittent gate
  # is worse than a red one — a red gate is read, a flaky one is re-run until it agrees.
  START=$(date +%s); SINCE="${SINCE:-$START}"
  WALL_S=$(python3 -c "print(int(float('$WALL_H')*3600))")
  say() { printf '%s %s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$*" | tee -a "$LOGF"; }
  halt() {  # $1 = reason
    printf '%s %s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$1" > "$BENCH/HALT"
    say "HALT WRITTEN → $BENCH/HALT :: $1"
    exit 3
  }
  say "ARMED bench=$BENCH stage=$STAGE arms=$ARMS tok_max=$TOK_MAX wall_h=$WALL_H poll=${POLL}s stall=${STALL_MIN}m since=$SINCE log=$LOGF"
  [ -f "$BENCH/HALT" ] && say "NOTE: $BENCH/HALT ALREADY EXISTS — the driver will stop at its next arm check. Not overwriting."

  last_sig=""; still=0; deadpolls=0
  while :; do
    if ! m=$(measure "$BENCH" "$STAGE" "$ARMS" "$SINCE" 2>/dev/null); then
      say "PROBE-FAILED — could not read $BENCH/state this poll (a failed probe is NOT a quiet run)"
      [ "$ONCE" = 1 ] && return 0; sleep "$POLL"; continue
    fi
    set -- $m; tok="$1"; landed="$2"
    tr=$(inflight "$CFGDIR" 2>/dev/null || echo "0 0"); set -- $tr; trbytes="$1"; trmtime="$2"
    nclaude=$(pgrep -f 'claude' 2>/dev/null | wc -l | tr -d ' ')
    elapsed=$(( $(date +%s) - START ))
    say "POLL tok=$tok/$TOK_MAX landed=$landed elapsed=${elapsed}s/${WALL_S}s claude=$nclaude transcript=${trbytes}B"

    [ "$tok" -ge "$TOK_MAX" ] && halt "BUDGET: metered $tok >= $TOK_MAX over $landed landings (stage $STAGE, arms $ARMS)"
    [ "$elapsed" -ge "$WALL_S" ] && halt "WALL: ${elapsed}s >= ${WALL_S}s (${WALL_H} h) since ARMED"

    sig="$tok|$landed|$trbytes|$trmtime"
    if [ "$sig" = "$last_sig" ]; then still=$((still + POLL)); else still=0; last_sig="$sig"; fi
    if [ "$still" -ge $((STALL_MIN * 60)) ]; then
      say "STALL-EVENT: landings, meter AND transcript static for ${still}s (>= ${STALL_MIN}m) — REPORTED, NOT HALTED (a long episode and a dead driver are the same shape to an end-of-unit instrument)"
      still=0
    fi
    if [ "$nclaude" = "0" ] && ! grep -q "S2 STAGE $STAGE DRIVER DONE" "$RUNLOG" 2>/dev/null; then
      deadpolls=$((deadpolls + 1))
      [ "$deadpolls" -ge 2 ] && { say "DEAD-EVENT: no claude process and no DRIVER DONE in $RUNLOG, $deadpolls consecutive polls"; deadpolls=0; }
    else
      deadpolls=0
    fi
    if grep -q "S2 STAGE $STAGE DRIVER DONE" "$RUNLOG" 2>/dev/null; then
      say "DRIVER DONE seen in $RUNLOG — watch exits 0 (tok=$tok landed=$landed)"; return 0
    fi
    [ "$ONCE" = 1 ] && return 0
    sleep "$POLL"
  done
}

# ─────────────────────────────── selftest: every arm a subprocess on the real argv ───────────────────────────────
selftest() {
  ME="$(cd "$(dirname "$0")" && pwd)/$(basename "$0")"
  W="$(mktemp -d "${TMPDIR:-/tmp}/haltwatch.XXXXXX")"; arms=0; fails=0
  ck() { arms=$((arms+1)); if [ "$2" = "1" ]; then printf '  PASS   %s\n' "$1"; else printf '  FAIL   %s   << %s\n' "$1" "${3:-}"; fails=$((fails+1)); fi; }
  mkroot() {  # $1=root  $2=stage  $3=arm  $4..=metered sums
    local r="$1" st="$2" arm="$3"; shift 3; local i=0
    mkdir -p "$r/logs"
    for tokv in "$@"; do
      i=$((i+1)); mkdir -p "$r/state/ep-$st$arm$i"
      printf '{"substrate":"S2-Lean/CLEVER","stage":"%s","arm":"%s","instance_id":"problem_%d","episode":"ep-%s%s%d","termination":"DONE","passed":true,"metered_sum":%s}\n' \
        "$st" "$arm" "$i" "$st" "$arm" "$i" "$tokv" > "$r/state/ep-$st$arm$i/manifest.json"
    done
  }
  # 1–5 REFUSE arms
  out=$(bash "$ME" rel B a0 100 1 --once 2>&1); ck "refuse/relative-bench" "$([ $? -ne 0 ] && echo 1 || echo 0)" "$out"
  out=$(bash "$ME" "$W/nope" B a0 100 1 --once 2>&1); ck "refuse/missing-bench" "$([ $? -ne 0 ] && echo 1 || echo 0)" "$out"
  mkdir -p "$W/r0/logs"
  out=$(bash "$ME" "$W/r0" Z a0 100 1 --once 2>&1); ck "refuse/bad-stage" "$([ $? -ne 0 ] && echo 1 || echo 0)" "$out"
  out=$(bash "$ME" "$W/r0" B a0 lots 1 --once 2>&1); ck "refuse/non-numeric-budget" "$([ $? -ne 0 ] && echo 1 || echo 0)" "$out"
  out=$(bash "$ME" "$W/r0" B a0 0 1 --once 2>&1); ck "refuse/zero-budget" "$([ $? -ne 0 ] && echo 1 || echo 0)" "$out"
  out=$(bash "$ME" "$W/r0" B a0 100 1 --nope 2>&1); ck "refuse/unknown-arg" "$([ $? -ne 0 ] && echo 1 || echo 0)" "$out"

  # 6 GREEN: under budget, no HALT file written
  mkroot "$W/r1" C a0 100 200 300
  bash "$ME" "$W/r1" C a0 100000 12 --once --poll 1 --since 0 >"$W/r1.out" 2>&1; rc=$?
  ck "green/under-budget rc=0" "$([ $rc -eq 0 ] && echo 1 || echo 0)" "rc=$rc"
  ck "green/no HALT file" "$([ ! -f "$W/r1/HALT" ] && echo 1 || echo 0)" "HALT exists"
  ck "green/measured 600 over 3" "$(grep -q 'tok=600/100000 landed=3' "$W/r1.out" && echo 1 || echo 0)" "$(tail -1 "$W/r1.out")"

  # 7 RED: over budget ⇒ HALT written, rc 3, reason recorded IN the file
  mkroot "$W/r2" C a0 5000 6000
  bash "$ME" "$W/r2" C a0 10000 12 --once --poll 1 --since 0 >"$W/r2.out" 2>&1; rc=$?
  ck "red/over-budget rc=3" "$([ $rc -eq 3 ] && echo 1 || echo 0)" "rc=$rc"
  ck "red/HALT file written" "$([ -f "$W/r2/HALT" ] && echo 1 || echo 0)" "no HALT"
  ck "red/HALT names the budget" "$(grep -q 'BUDGET: metered 11000 >= 10000' "$W/r2/HALT" 2>/dev/null && echo 1 || echo 0)" "$(cat "$W/r2/HALT" 2>/dev/null)"

  # 8 the WALL arm fires on its own, with the budget nowhere near
  mkroot "$W/r3" C a0 1
  bash "$ME" "$W/r3" C a0 999999999 0 --once --poll 1 --since 0 >"$W/r3.out" 2>&1; rc=$?
  ck "red/wall rc=3" "$([ $rc -eq 3 ] && echo 1 || echo 0)" "rc=$rc"
  ck "red/wall reason, not budget" "$(grep -q '^.*WALL:' "$W/r3/HALT" 2>/dev/null && echo 1 || echo 0)" "$(cat "$W/r3/HALT" 2>/dev/null)"

  # 9 SCOPE: the same tokens under a DIFFERENT stage/arm must not count — a watch that counts the previous
  #   stage's landings halts a run that has spent nothing, and it would look exactly like a real breach.
  mkroot "$W/r4" B a0 9999999
  mkroot "$W/r4" C a2 9999999
  bash "$ME" "$W/r4" C a0 10000 12 --once --poll 1 --since 0 >"$W/r4.out" 2>&1; rc=$?
  ck "scope/other stage+arm not counted" "$([ $rc -eq 0 ] && echo 1 || echo 0)" "$(tail -2 "$W/r4.out")"
  ck "scope/measured zero" "$(grep -q 'tok=0/10000 landed=0' "$W/r4.out" && echo 1 || echo 0)" "$(tail -1 "$W/r4.out")"

  # 10 SINCE: a landing older than the spend window is not this run's spend — driven BOTH ways on one fixture,
  #    so the arm proves the filter works rather than that the fixture happened to be old.
  mkroot "$W/r5" C a0 9999999
  find "$W/r5/state" -name manifest.json -exec touch -t 202001010000 {} \;
  bash "$ME" "$W/r5" C a0 10000 12 --once --poll 1 >"$W/r5.out" 2>&1; rc=$?
  ck "since/pre-window landing not counted (default clock)" "$([ $rc -eq 0 ] && echo 1 || echo 0)" "$(tail -2 "$W/r5.out")"
  bash "$ME" "$W/r5" C a0 10000 12 --once --poll 1 --since 0 >"$W/r5b.out" 2>&1; rc=$?
  ck "since/the SAME fixture DOES breach with --since 0" "$([ $rc -eq 3 ] && echo 1 || echo 0)" "$(tail -2 "$W/r5b.out")"
  out=$(bash "$ME" "$W/r5" C a0 10000 12 --once --since notanumber 2>&1); ck "refuse/bad --since" "$([ $? -ne 0 ] && echo 1 || echo 0)" "$out"

  # 11 DONE: the driver's DONE line exits the watch 0, and for the RIGHT stage only
  mkroot "$W/r6" C a0 10
  printf 'x\nS2 STAGE B DRIVER DONE k=12\n' > "$W/r6/logs/run_s2_stage0.log"
  bash "$ME" "$W/r6" C a0 10000 12 --once --poll 1 --since 0 >"$W/r6.out" 2>&1
  ck "done/other stage's DONE is not mine" "$(grep -q 'DRIVER DONE seen' "$W/r6.out" && echo 0 || echo 1)" "$(tail -1 "$W/r6.out")"
  printf 'x\nS2 STAGE C DRIVER DONE k=12\n' > "$W/r6/logs/run_s2_stage0.log"
  bash "$ME" "$W/r6" C a0 10000 12 --poll 1 --since 0 >"$W/r6b.out" 2>&1; rc=$?
  ck "done/my stage's DONE exits 0" "$([ $rc -eq 0 ] && grep -q 'DRIVER DONE seen' "$W/r6b.out" && echo 1 || echo 0)" "rc=$rc $(tail -1 "$W/r6b.out")"

  # 12 an existing HALT file is REPORTED and NOT overwritten (it may carry someone else's reason)
  mkroot "$W/r7" C a0 10; printf 'someone else\n' > "$W/r7/HALT"
  bash "$ME" "$W/r7" C a0 10000 12 --once --poll 1 --since 0 >"$W/r7.out" 2>&1
  ck "halt/pre-existing reported" "$(grep -q 'ALREADY EXISTS' "$W/r7.out" && echo 1 || echo 0)" "$(head -3 "$W/r7.out")"
  ck "halt/pre-existing not overwritten" "$([ "$(cat "$W/r7/HALT")" = "someone else" ] && echo 1 || echo 0)" "$(cat "$W/r7/HALT")"

  rm -rf "$W"
  printf 'halt_watch selftest: %d arms, %d failed\n' "$arms" "$fails"
  [ "$fails" -eq 0 ]
}

case "${1:-}" in
  --selftest) selftest ;;
  ""|-h|--help) usage; exit 2 ;;
  *) main "$@" ;;
esac
