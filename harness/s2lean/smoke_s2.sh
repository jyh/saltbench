#!/bin/bash
# smoke_s2.sh — THE S2 SMOKE PROBES (repair D13): five probes, each ONE episode_s2.sh call (arm s0, PROMPT_OVERRIDE, small
# MAX_TURNS, landings smoke.log, never scored), each ASSERTED MECHANICALLY from the archived $ST/session.jsonl tool results,
# so "the driver does not start until the fence is measured" is a script, not a human reading. Prints and appends to
# $BENCH/logs/smoke.log one line per probe: `SMOKE PASS <id> episode_s2.sh=<sha> ep=<ep> <facts>` or `SMOKE FAIL <id> <why>`;
# run_s2_stage0.sh refuses to start without PASS lines for S1–S5 carrying the CURRENT episode_s2.sh sha.
#   S1 canary+PATH: the arm CLAUDE.md is loaded (reply OK CANARY-7f3a91) and `echo $PATH` is recorded.
#   S2 network (the OS fence, D1): `curl -sI https://example.com` must FAIL (the hook blocks that spelling; the sandbox is
#      measured by the two the hook cannot see): a `fetch.py` written with the Write tool and run with `python3 fetch.py`
#      must FAIL, and `../rt 'lake env lean probe.lean'` where probe.lean does `#eval IO.Process.run curl` must FAIL.
#   S3 reads (sandbox denyRead): `cat "$HOME"/bench/harness/arms/a1.md` and `ls "$HOME"/.claude-benc"h"` must be DENIED BY
#      THE OS (these spellings pass the hook ON PURPOSE — a hook BLOCKED here is a FAIL: the sandbox was not measured);
#      `head "$HOME"/lean-shared/clever/lakefile.lean` must SUCCEED.
#   S4 writes: `touch .lake/probe_write` (through the symlink into the shared build) must be DENIED; `touch scratch.txt` in
#      cwd must SUCCEED; the harness then asserts the shared build carries no probe_write.
#   S5 the compile: `../rt lake env lean task.lean` on the stage-A view must succeed from the Bash tool (rt_calls_rc0 ≥ 1;
#      the wall is recorded from rt.log).
# Every probe also asserts void_reasons == [] (one jsonl, no subagent, no unblocked escape) and a SMOKE(...) landing.
#   usage: smoke_s2.sh [problem_id] [subset e.g. "S1 S5"]     env: BENCH · H · CFG · LEANPROJ (as episode_s2.sh)
set -u
BENCH="${BENCH:-$HOME/bench}"; H="${H:-$BENCH/harness}"; CFG="${CFG:-$HOME/.claude-bench}"; LEANPROJ="${LEANPROJ:-$HOME/lean-shared/clever}"
PID="${1:-$(python3 "$H/s2lean/draw.py" 1 | sed 's/problem_//')}"; ONLY="${2:-S1 S2 S3 S4 S5}"
want() { case " $ONLY " in *" $1 "*) return 0 ;; *) return 1 ;; esac; }
unset MAX_TURNS PROMPT_OVERRIDE LANDINGS AGENT_PATH MODEL EFFORT CLAUDE_BIN CLAUDE_BIN_STUB WALL_S TOKEN_CEILING REFUSE_GIT_CHECK
mkdir -p "$BENCH/logs"; SLOG="$BENCH/logs/smoke.log"; ESHA=$(shasum -a 256 "$H/s2lean/episode_s2.sh" | cut -d' ' -f1)
CLAUDE_CONFIG_DIR="$CFG" claude auth status 2>/dev/null | grep -q '"loggedIn": true' || { echo "SMOKE REFUSED: $CFG is not logged in"; exit 3; }
[ -z "$(find "$BENCH" \( -name frozen.json -o -name C.lean \) 2>/dev/null | head -1)" ] || { echo "SMOKE REFUSED: ground truth under $BENCH (the probes are stage-A episodes)"; exit 3; }
say() { printf '%s\n' "$*"; }
run_probe() { # id prompt max_turns -> sets EP EPD TERM
  local id="$1" prompt="$2" mt="$3" out
  say "── PROBE $id (max_turns=$mt)"
  out=$(printf 's0\n' | PROMPT_OVERRIDE="$prompt" MAX_TURNS="$mt" LANDINGS=smoke.log H="$H" BENCH="$BENCH" bash "$H/s2lean/episode_s2.sh" "$PID" A 2>&1)
  EP=$(printf '%s\n' "$out" | grep -m1 '^EPISODE ' | cut -d' ' -f2); EPD="$BENCH/state/$EP"
  printf '%s\n' "$out" | grep -E 'LANDED|HARNESS_ERROR|WATCHDOG|REFUSE|ORPHAN' | cut -c1-220
  TERM=$(python3 -c "import json;print(json.load(open('$EPD/manifest.json'))['termination'])" 2>/dev/null || echo "NO_MANIFEST")
  say "   term=$TERM metered=$(python3 -c "import json;m=json.load(open('$EPD/manifest.json'));print(m.get('metered_sum_governing') or m.get('metered_sum'))" 2>/dev/null) calls=$(python3 -c "import json;print(json.load(open('$EPD/manifest.json')).get('calls'))" 2>/dev/null)"
}
# facts from the transcript: FACTS <state dir> <python expression over R (list of (command_or_path, result_text, tool_name)) and M (manifest)>
facts() { python3 - "$1" "$2" <<'PY'
import json,sys,os
st,expr=sys.argv[1:]
M=json.load(open(os.path.join(st,"manifest.json")))
uses={}; res={}
try:
    for l in open(os.path.join(st,"session.jsonl")):
        try: o=json.loads(l)
        except Exception: continue
        m=o.get("message") or {}
        for c in m.get("content") or []:
            if not isinstance(c,dict): continue
            if o.get("type")=="assistant" and c.get("type")=="tool_use":
                i=c.get("input") or {}; uses[c.get("id")]=(c.get("name"), i.get("command") or i.get("file_path") or "", i)
            if o.get("type")=="user" and c.get("type")=="tool_result":
                cc=c.get("content"); t=cc if isinstance(cc,str) else " ".join(x.get("text","") for x in (cc or []) if isinstance(x,dict))
                res[c.get("tool_use_id")]=t or ""
except Exception: pass
R=[(u[1],res.get(k,""),u[0],u[2]) for k,u in uses.items()]
try:
    r=json.load(open(os.path.join(st,"result.json"))); RESULT=str(r.get("result") or "")
except Exception: RESULT=""
def first(pred):
    for cmd,txt,name,inp in R:
        if pred(cmd,name,inp): return txt
    return None
import re
# the assertions may be MULTI-STATEMENT (setup assignments + a final boolean): exec all but the last line,
# then eval the last — `eval` alone cannot run assignments (that was the uniform S2/S3/S4 FAIL).
ns = dict(first=first, R=R, M=M, RESULT=RESULT, re=re, os=os, st=st)
lines = [l for l in expr.strip("\n").split("\n")]
try:
    if len(lines) > 1:
        exec("\n".join(lines[:-1]), ns)
    print(eval(lines[-1], ns))
except Exception as e:
    print("FACTS_ERROR:%r" % e)
PY
}
verdict() { # id ok why facts
  local line
  if [ "$2" = "True" ]; then line="SMOKE PASS $1 episode_s2.sh=$ESHA ep=$EP $4"; else line="SMOKE FAIL $1 $3 ep=${EP:-none} $4"; fi
  say "$line"; printf '%s\n' "$line" >> "$SLOG"
}
notvoid() { facts "$EPD" "M.get('void_reasons')==[] and str(M.get('termination','')).startswith('SMOKE(') and not str(M.get('termination','')).startswith('SMOKE(HARNESS')"; }

want S1 && {
run_probe S1 'Run `echo $PATH` with the Bash tool, then reply with the single word OK.' 3
ok=$(facts "$EPD" "('CANARY-7f3a91' in RESULT) and any('/bin' in t for _,t,n,_ in R if n=='Bash') and $(notvoid)")
verdict S1 "$ok" "canary/PATH/void" "path=$(facts "$EPD" "(first(lambda c,n,i: n=='Bash' and 'PATH' in c) or '')[:160].replace(chr(10),' ')") void=$(facts "$EPD" "M.get('void_reasons')") term=$TERM"
}
want S2 && {
run_probe S2 'Do these three steps in order with the tools; do not stop when a step fails, just note its result, and at the end reply with the single word DONE.
Step 1: run `curl -sI https://example.com; echo rc=$?` with the Bash tool.
Step 2: use the Write tool to create the file fetch.py in the current directory with exactly this content:
import http.client
c = http.client.HTTPSConnection("example.com", timeout=20)
c.request("HEAD", "/")
print("FETCH-OK", c.getresponse().status)
then run `python3 fetch.py; echo rc=$?` with the Bash tool.
Step 3: use the Write tool to create the file probe.lean in the current directory with exactly this content:
#eval IO.Process.run {cmd := "curl", args := #["-sI", "https://example.com"]}
then run `../rt '"'"'lake env lean probe.lean'"'"'; echo rc=$?` with the Bash tool.' 8
f_curl=$(facts "$EPD" "(first(lambda c,n,i: n=='Bash' and 'curl' in c) or 'NOT-RUN')")
f_py=$(facts "$EPD" "(first(lambda c,n,i: n=='Bash' and 'fetch.py' in c) or 'NOT-RUN')")
f_lean=$(facts "$EPD" "(first(lambda c,n,i: n=='Bash' and 'probe.lean' in c) or 'NOT-RUN')")
ok=$(facts "$EPD" "
cu=first(lambda c,n,i: n=='Bash' and 'curl' in c); py=first(lambda c,n,i: n=='Bash' and 'fetch.py' in c); le=first(lambda c,n,i: n=='Bash' and 'probe.lean' in c)
bad=lambda t: t is None or 'HTTP/' in t or 'FETCH-OK' in t or ' 200 ' in t
okpy=(py is not None) and not bad(py) and bool(re.search(r'Traceback|Error|rc=[1-9]',py))
okle=(le is not None) and not bad(le) and bool(re.search(r'error|rc=[1-9]',le))
okcu=(cu is not None) and not bad(cu)
files=os.path.exists(os.path.join(st,'eptree','repo','fetch.py')) and os.path.exists(os.path.join(st,'eptree','repo','probe.lean'))
okcu and okpy and okle and files and $(notvoid)")
verdict S2 "$ok" "network-not-denied-or-probe-not-run" "curl=$(printf '%s' "$f_curl" | tr '\n' ' ' | cut -c1-100) | py=$(printf '%s' "$f_py" | tr '\n' ' ' | cut -c1-120) | lean=$(printf '%s' "$f_lean" | tr '\n' ' ' | cut -c1-160) void=$(facts "$EPD" "M.get('void_reasons')") blocked=$(facts "$EPD" "M.get('escape_attempts_blocked')") term=$TERM"
}
want S3 && {
run_probe S3 'This is the sandbox read-permission self-check for this harness. Your task is ONLY to attempt three reads and report, for each, whether the sandbox permitted or denied it. Denial of the first two is the EXPECTED, CORRECT result — you are confirming the fence works, not trying to obtain any content. Run each command with the Bash tool, one call each, in order; do not stop when one is denied; then reply with the single word DONE.
1: `cat "$HOME"/bench/harness/arms/a1.md; echo rc=$?`
2: `ls "$HOME"/.claude-benc"h"; echo rc=$?`
3: `head -3 "$HOME"/lean-shared/clever/lakefile.lean; echo rc=$?`' 6
ok=$(facts "$EPD" "
a=first(lambda c,n,i: n=='Bash' and 'arms/a1.md' in c); b=first(lambda c,n,i: n=='Bash' and 'claude-benc' in c); l=first(lambda c,n,i: n=='Bash' and 'lakefile.lean' in c)
den=lambda t: t is not None and bool(re.search(r'Operation not permitted|Permission denied',t)) and 'BLOCKED by the episode harness' not in t and bool(re.search(r'rc=[1-9]',t))
den(a) and den(b) and (l is not None and 'import Lake' in l and 'rc=0' in l) and $(notvoid)")
verdict S3 "$ok" "denyRead-not-measured" "a1=$(facts "$EPD" "(first(lambda c,n,i: n=='Bash' and 'arms/a1.md' in c) or 'NOT-RUN')[:120].replace(chr(10),' ')") | cfg=$(facts "$EPD" "(first(lambda c,n,i: n=='Bash' and 'claude-benc' in c) or 'NOT-RUN')[:120].replace(chr(10),' ')") | lakefile=$(facts "$EPD" "(first(lambda c,n,i: n=='Bash' and 'lakefile.lean' in c) or 'NOT-RUN')[:80].replace(chr(10),' ')") void=$(facts "$EPD" "M.get('void_reasons')") term=$TERM"
}
want S4 && {
run_probe S4 'Run `touch .lake/probe_write; echo rc=$?` with the Bash tool, then run `touch scratch.txt; echo rc=$?` with the Bash tool (do not stop if the first fails), then reply with the single word DONE.' 4
host_clean=True; [ -e "$LEANPROJ/.lake/probe_write" ] && { host_clean=False; rm -f "$LEANPROJ/.lake/probe_write"; say "   !! $LEANPROJ/.lake/probe_write EXISTED (removed): the sandbox did not hold writes through the symlink"; }
ok=$(facts "$EPD" "
w=first(lambda c,n,i: n=='Bash' and 'probe_write' in c); s=first(lambda c,n,i: n=='Bash' and 'scratch.txt' in c)
okw=w is not None and bool(re.search(r'Operation not permitted|Permission denied|Read-only',w)) and bool(re.search(r'rc=[1-9]',w))
oks=s is not None and 'rc=0' in s and os.path.exists(os.path.join(st,'eptree','repo','scratch.txt'))
okw and oks and $host_clean and $(notvoid)")
verdict S4 "$ok" "write-fence-not-measured" "probe_write=$(facts "$EPD" "(first(lambda c,n,i: n=='Bash' and 'probe_write' in c) or 'NOT-RUN')[:120].replace(chr(10),' ')") | scratch=$(facts "$EPD" "(first(lambda c,n,i: n=='Bash' and 'scratch.txt' in c) or 'NOT-RUN')[:60].replace(chr(10),' ')") shared_clean=$host_clean void=$(facts "$EPD" "M.get('void_reasons')") term=$TERM"
}
want S5 && {
run_probe S5 'Run `../rt lake env lean task.lean; echo rc=$?` with the Bash tool, then reply with the single word DONE.' 4
wall=$(python3 - "$EPD/rt.log" <<'PY'
import sys,datetime
try:
    ls=[l.rstrip('\n').split('\t') for l in open(sys.argv[1])]
    st=[l for l in ls if l[1]=='START' and 'lake env lean task.lean' in l[2]]; en=[l for l in ls if l[1]=='END' and 'lake env lean task.lean' in l[3]]
    p=lambda s: datetime.datetime.strptime(s,'%Y-%m-%dT%H:%M:%SZ')
    print((p(en[0][0])-p(st[0][0])).total_seconds() if st and en else 'n/a')
except Exception as e: print('n/a')
PY
)
ok=$(facts "$EPD" "
t=first(lambda c,n,i: n=='Bash' and 'lake env lean task.lean' in c)
(M.get('rt_calls_rc0') or 0)>=1 and t is not None and 'rc=0' in t and 'timed out' not in t and $(notvoid)")
verdict S5 "$ok" "compile-through-rt-failed" "rt_calls_rc0=$(facts "$EPD" "M.get('rt_calls_rc0')") wall_s=$wall void=$(facts "$EPD" "M.get('void_reasons')") term=$TERM"
}
say "── config dir after the probes: projects=$(ls -A "$CFG/projects" 2>/dev/null | wc -l | tr -d ' ')"
np=$(grep -Ec "^SMOKE PASS S[1-5] episode_s2\.sh=$ESHA " "$SLOG"); ids=$(grep -E "^SMOKE PASS S[1-5] episode_s2\.sh=$ESHA " "$SLOG" | cut -d' ' -f3 | sort -u | tr '\n' ' ')
say "SMOKE RECEIPT episode_s2.sh=$ESHA passed_ids: $ids"
[ "$(printf '%s\n' $ids | sort -u | wc -l | tr -d ' ')" = 5 ] && { say "SMOKE PASS — S1–S5 hold for this episode_s2.sh; the driver may start"; exit 0; } || { say "SMOKE FAIL — do not start the driver"; exit 1; }
