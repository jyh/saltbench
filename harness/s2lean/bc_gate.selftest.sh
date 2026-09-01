#!/bin/bash
# bc_gate.selftest.sh — the RED-FIRST gate for amendment 10. Every arm drives bc_gate.py AS A SUBPROCESS ON THE
# REAL ARGV (this repo's law: a self-test that never makes the call its caller makes is a self-test of a
# different program), over fixture roots built here. Arm 2 is the one that matters: it reproduces the EXACT state
# of 2026-08-31 — a root whose log carries "S2 STAGE A DRIVER DONE" and whose state holds NOTHING — and drives
# BOTH the FROZEN predicate and the new gate on it, so the flip is shown rather than asserted.
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"; G="$HERE/bc_gate.py"
T="$(mktemp -d "${TMPDIR:-/tmp}/bcgate-XXXXXX")"; trap 'rm -rf "$T"' EXIT
NOW=1788220000; PASS=0; FAIL=0
say() { printf '%-5s arm %-2s %-52s %s\n' "$1" "$2" "$3" "$4"; }
arm() { # arm <n> <want-rc> <desc> <cmd...>
  local n="$1" want="$2" desc="$3"; shift 3
  local out; out="$("$@" 2>&1)"; local rc=$?
  if [ "$rc" = "$want" ]; then PASS=$((PASS+1)); say ok "$n" "$desc" "rc=$rc"
  else FAIL=$((FAIL+1)); say FAIL "$n" "$desc" "rc=$rc want=$want"; echo "$out" | sed 's/^/        /'; fi
}

# ---- fixture builder: a root with a complete, content-consistent stage A ----
mkroot() { # mkroot <dir> <end_utc> <ids...>
  local R="$1" END="$2"; shift 2
  mkdir -p "$R/logs" "$R/state/s2"
  echo "S2 STAGE A DRIVER DONE k=27" >> "$R/logs/run_s2_stage0.log"
  for pid in "$@"; do
    for a in a0 a2; do
      local ep="ep-fix${pid}${a}"
      mkdir -p "$R/state/$ep" "$R/state/s2/problem_$pid/$a"
      printf '{"generated_spec_body":"-- body %s %s"}' "$pid" "$a" > "$R/state/$ep/bodies.json"
      local sha; sha=$(shasum -a 256 "$R/state/$ep/bodies.json" | cut -d' ' -f1)
      printf '{"stage":"A","instance_id":"problem_%s","arm":"%s","end_utc":%s,"episode":"%s"}' \
        "$pid" "$a" "$END" "$ep" > "$R/state/$ep/manifest.json"
      printf '{"generated_spec_body":"-- body %s %s","a_episode":"%s","a_bodies_sha256":"%s","a_termination":"DONE","a_passed":true}' \
        "$pid" "$a" "$ep" "$sha" > "$R/state/s2/problem_$pid/$a/A.bodies.json"
    done
  done
}
IDS="73 0 146"; ARMS="a0,a2"
mkroot "$T/good"   $((NOW-3600))   73 0 146     # 1 h old
mkroot "$T/stale"  $((NOW-400000)) 73 0 146     # 111 h old
mkdir -p "$T/donebutempty/logs" "$T/donebutempty/state/s2"
echo "S2 STAGE A DRIVER DONE k=27" > "$T/donebutempty/logs/run_s2_stage0.log"   # THE 2026-08-31 STATE, exactly
cp -R "$T/good" "$T/missing";  rm -rf "$T/missing/state/s2/problem_146/a2"
cp -R "$T/good" "$T/notpass";  python3 - "$T/notpass/state/s2/problem_0/a0/A.bodies.json" <<'PY'
import json,sys; p=sys.argv[1]; o=json.load(open(p)); o["a_passed"]=False; json.dump(o,open(p,"w"))
PY
cp -R "$T/good" "$T/emptyfile"; : > "$T/emptyfile/state/s2/problem_73/a0/A.bodies.json"
cp -R "$T/good" "$T/crossroot"; rm -rf "$T/crossroot/state/ep-fix73a0"   # the leftover from ANOTHER root
cp -R "$T/good" "$T/tampered"; python3 - "$T/tampered/state/ep-fix0a2/bodies.json" <<'PY'
import sys; open(sys.argv[1],"w").write('{"generated_spec_body":"-- SWAPPED AFTER THE FACT"}')
PY
cp -R "$T/good" "$T/wrongstage"; python3 - "$T/wrongstage/state/ep-fix146a0/manifest.json" <<'PY'
import json,sys; p=sys.argv[1]; o=json.load(open(p)); o["stage"]="B"; json.dump(o,open(p,"w"))
PY
cp -R "$T/good" "$T/noclock"; python3 - "$T/noclock/state/ep-fix73a2/manifest.json" <<'PY'
import json,sys; p=sys.argv[1]; o=json.load(open(p)); del o["end_utc"]; json.dump(o,open(p,"w"))
PY

echo "=== the gate's own arms (bc_gate.py, real argv, subprocess) ==="
arm 1  0 "complete, fresh, content-consistent root -> PASS"        python3 "$G" --root "$T/good"         --arms "$ARMS" --ids "$IDS" --now $NOW
arm 2  3 "DONE line present, state EMPTY (the 08/31 state)"        python3 "$G" --root "$T/donebutempty" --arms "$ARMS" --ids "$IDS" --now $NOW
arm 3  3 "one cell has no A.bodies.json"                           python3 "$G" --root "$T/missing"      --arms "$ARMS" --ids "$IDS" --now $NOW
arm 4  3 "a_passed=false"                                          python3 "$G" --root "$T/notpass"      --arms "$ARMS" --ids "$IDS" --now $NOW
arm 5  3 "A.bodies.json is a 0-byte file"                          python3 "$G" --root "$T/emptyfile"    --arms "$ARMS" --ids "$IDS" --now $NOW
arm 6  3 "provenance episode is NOT in this root (cross-root)"     python3 "$G" --root "$T/crossroot"    --arms "$ARMS" --ids "$IDS" --now $NOW
arm 7  3 "episode bodies swapped after the fact (receipt)"         python3 "$G" --root "$T/tampered"     --arms "$ARMS" --ids "$IDS" --now $NOW
arm 8  3 "provenance episode is stage B, not A"                    python3 "$G" --root "$T/wrongstage"   --arms "$ARMS" --ids "$IDS" --now $NOW
arm 9  3 "manifest has no end_utc — a gate with no clock"          python3 "$G" --root "$T/noclock"      --arms "$ARMS" --ids "$IDS" --now $NOW
arm 10 3 "root is fresh-complete but 111 h old (the CLOCK arm)"    python3 "$G" --root "$T/stale"        --arms "$ARMS" --ids "$IDS" --now $NOW
arm 11 0 "...and the same stale root passes at --max-age-h 200"    python3 "$G" --root "$T/stale"        --arms "$ARMS" --ids "$IDS" --now $NOW --max-age-h 200
arm 12 3 "root does not exist (the WRONG-ROOT arm)"                python3 "$G" --root "$T/nosuchroot"   --arms "$ARMS" --ids "$IDS" --now $NOW
arm 13 2 "--root omitted: REFUSE, no default"                      python3 "$G"                          --arms "$ARMS" --ids "$IDS"
arm 14 2 "--ids omitted: REFUSE, no default"                       python3 "$G" --root "$T/good"         --arms "$ARMS"
arm 15 2 "--arms omitted: REFUSE, no default"                      python3 "$G" --root "$T/good"                        --ids "$IDS"
arm 16 2 "a non-numeric id"                                        python3 "$G" --root "$T/good"         --arms "$ARMS" --ids "73 abc"
arm 17 3 "an id that was never run"                                python3 "$G" --root "$T/good"         --arms "$ARMS" --ids "73 999"
arm 18 3 "an arm that was never run"                               python3 "$G" --root "$T/good"         --arms "a0,a1" --ids "$IDS"

echo
echo "=== THE FLIP, DRIVEN: the FROZEN predicate vs the new gate, on the SAME roots ==="
frozen() { grep -q "S2 STAGE A DRIVER DONE" "$1/logs/run_s2_stage0.log" 2>/dev/null; }
for r in donebutempty stale good; do
  frozen "$T/$r" && f=PASS || f=REFUSE
  python3 "$G" --root "$T/$r" --arms "$ARMS" --ids "$IDS" --now $NOW >/dev/null 2>&1 && n=PASS || n=REFUSE
  printf '  %-14s frozen-predicate=%-6s content-gate=%-6s %s\n' "$r" "$f" "$n" \
    "$([ "$f" != "$n" ] && echo '<= FLIP' || echo '')"
  case "$r" in
    donebutempty|stale) [ "$f" = PASS ] && [ "$n" = REFUSE ] && PASS=$((PASS+1)) || { FAIL=$((FAIL+1)); echo "        FAIL: expected frozen=PASS content=REFUSE"; } ;;
    good)               [ "$f" = PASS ] && [ "$n" = PASS ]   && PASS=$((PASS+1)) || { FAIL=$((FAIL+1)); echo "        FAIL: expected both PASS"; } ;;
  esac
done

echo
echo "bc_gate selftest: $PASS ok, $FAIL failed"
[ "$FAIL" = 0 ]
