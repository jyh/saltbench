#!/bin/bash
# smoke.sh — the four declared smoke probes (SCOUT-STAGE0 §7.3 as amended), run THROUGH episode.sh and ASSERTED
# mechanically, so "the driver does not start until all four have landed with the expected facts" is a script, not a
# human reading (refuter F0 residual). Each probe is a SMOKE(...) landing in smoke.log, never scored. Exit 0 only if
# every expected fact holds; the failing fact is printed. usage: smoke.sh [task_id]   (default: the first pilot task)
set -u
BENCH="${BENCH:-$HOME/bench}"; H="${H:-$BENCH/harness}"; CFG="${CFG:-$HOME/.claude-bench}"
IID="${1:-$(python3 -c "import json;print(json.load(open('$H/TASKLIST.json'))['pilot'][0])")}"
unset MAX_TURNS PROMPT_OVERRIDE LANDINGS AGENT_PATH MODEL EFFORT CLAUDE_BIN CLAUDE_BIN_STUB WALL_S TOKEN_CEILING
CLAUDE_CONFIG_DIR="$CFG" claude auth status 2>/dev/null | grep -q '"loggedIn": true' || { echo "SMOKE REFUSED: $CFG is not logged in"; exit 3; }
fail=0; say() { printf '%s\n' "$*"; }
run_probe() { # name prompt max_turns -> sets EPD (state dir of the landing)
  local name="$1" prompt="$2" mt="$3" out ep
  say "── PROBE $name (max_turns=$mt)"
  out=$(printf 's0\n' | PROMPT_OVERRIDE="$prompt" MAX_TURNS="$mt" LANDINGS=smoke.log H="$H" BENCH="$BENCH" bash "$H/episode.sh" "$IID" 2>&1)
  ep=$(printf '%s\n' "$out" | grep -m1 '^EPISODE ' | cut -d' ' -f2); EPD="$BENCH/state/$ep"
  printf '%s\n' "$out" | grep -E 'LANDED|HARNESS_ERROR|WATCHDOG|REFUSE' | cut -c1-200
  say "   metered=$(python3 -c "import json;m=json.load(open('$EPD/manifest.json'));print(m.get('metered_sum_governing') or m.get('metered_sum'))" 2>/dev/null) calls=$(python3 -c "import json;print(json.load(open('$EPD/manifest.json')).get('calls'))" 2>/dev/null) term=$(python3 -c "import json;print(json.load(open('$EPD/manifest.json'))['termination'])" 2>/dev/null)"
}
jq_() { python3 -c "import json,sys;d=json.load(open('$1'));print(eval(sys.argv[1]))" "$2" 2>/dev/null; }
check() { if [ "$1" = "$2" ]; then say "   PASS $3 ($2)"; else say "   FAIL $3: got '$1' want '$2'"; fail=1; fi; }

# A1 — PATH from inside the agent + the canary proves the arm file is loaded
run_probe A1 'Run `echo $PATH` with the Bash tool, then reply with the single word OK.' 3
res=$(jq_ "$EPD/result.json" "d.get('result','')"); check "$(printf '%s' "$res" | grep -c 'CANARY-7f3a91')" 1 "A1 canary string in the result (arm CLAUDE.md loaded)"
check "$(jq_ "$EPD/manifest.json" "str(d['void_reasons'])")" "[]" "A1 not void"
say "   agent PATH (from the transcript): $(python3 -c "
import json
for l in open('$EPD/session.jsonl'):
    o=json.loads(l)
    if o.get('type')=='user':
        for c in (o.get('message') or {}).get('content') or []:
            if isinstance(c,dict) and c.get('type')=='tool_result':
                t=c.get('content'); t=t if isinstance(t,str) else ' '.join(x.get('text','') for x in (t or []) if isinstance(x,dict))
                if '/bin' in t: print(t.strip()[:300]); raise SystemExit
" 2>/dev/null)"
# A2 — the tripwire fires from inside the agent and is an ATTEMPT, not a void
run_probe A2 'Run `docker version` with the Bash tool, then reply with the single word OK.' 3
check "$(jq_ "$EPD/meter.json" "len(d['escape_attempts_blocked'])>=1")" True "A2 hook BLOCKED docker (attempt recorded)"
check "$(jq_ "$EPD/meter.json" "d['void']")" False "A2 not void"
# B — the cap: one turn, error_max_turns, num_turns == distinct message.id
run_probe B 'Run `ls` with the Bash tool, then reply with the single word OK.' 1
check "$(jq_ "$EPD/result.json" "d.get('subtype')")" error_max_turns "B error_max_turns fired at --max-turns 1"
check "$(jq_ "$EPD/meter.json" "d['crosscheck']['num_turns_matches_calls']")" True "B num_turns == distinct message.id"
say "   B usage cross-check: cli_minus_jsonl=$(jq_ "$EPD/meter.json" "d['crosscheck']['cli_minus_jsonl']") foreign_models=$(jq_ "$EPD/meter.json" "d['crosscheck'].get('foreign_models_in_modelUsage')")"
# C — the wrapper works under the agent's own Bash tool
run_probe C 'Run `../rt '"'"'python -c "print(6*7)"'"'"'` with the Bash tool, then reply with the single word OK.' 3
check "$(jq_ "$EPD/manifest.json" "d['rt_calls_rc0']")" 1 "C rt call succeeded from inside the agent"
check "$(jq_ "$EPD/manifest.json" "d['void_reasons']==[]")" True "C not void (../rt is not an escape)"
say "── config dir after the probes: projects=$(ls -A "$CFG/projects" | wc -l | tr -d ' ') file-history=$(ls -A "$CFG/file-history" 2>/dev/null | wc -l | tr -d ' ')"
if [ "$fail" = 0 ]; then say "SMOKE PASS — all four probes landed with the expected facts; the driver may start"; else say "SMOKE FAIL — do not start the driver"; fi
exit $fail
