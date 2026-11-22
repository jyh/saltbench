#!/bin/bash
# surface_probe.sh <client-version> — RUN ON THE RUN BOX. Reads the client's OWN offered tool list (the stream-json
# `system/init` record) in four arms, one `-p` turn each, prompt asks for no tool, every arm under the cell sandbox:
#   cell       the Claude-lane launch line: --tools + --disallowedTools + the cell fence (permissions.deny names both web tools)
#   fence      the cell fence alone, no tool flags
#   flags      the tool flags alone, with a fence copy whose permissions.deny no longer names WebFetch/WebSearch
#   control    that fence copy alone, no tool flags: it MUST list a web tool, or the init list cannot see one (arms VOID)
# The fence is block T cell clbvrs01's ctl/fence.json. CLAUDE_CONFIG_DIR comes from the caller (a logged-in pool). Output: <OUT>/surface-<ver>.out plus each arm's stream.
set -u
VER=${1:?client version}
OUT=$HOME/bench-dry/claude-webcensus-2026-11-22/surface-probe; mkdir -p "$OUT/wd"
BIN=$HOME/.local/share/claude/versions/$VER
FENCE=$HOME/cells-clb-to-linearscan-saltdiet/clbvrs01/ctl/fence.json
export CLAUDE_CONFIG_DIR=${CLAUDE_CONFIG_DIR:?set CLAUDE_CONFIG_DIR to the logged-in config dir of a pool other than the live cell uses}
[ -e "$HOME/.fleet/watch/COUNCIL-OPEN" ] && { echo "HOLD: council open"; exit 9; }
[ -x "$BIN" ] && [ -r "$FENCE" ] || { echo "REFUSE: client $BIN or fence missing"; exit 2; }
/usr/bin/python3 -c '
import json,sys
f=json.load(open(sys.argv[1])); d=f["permissions"]["deny"]
f["permissions"]["deny"]=[x for x in d if x not in ("WebFetch","WebSearch")]
assert len(d)-len(f["permissions"]["deny"])==2
json.dump(f, open(sys.argv[2],"w"), indent=2)' "$FENCE" "$OUT/fence-noweb.json" || { echo "REFUSE: fence copy"; exit 2; }
TOOLS=Bash,Read,Edit,Write,MultiEdit,NotebookEdit,Glob,Grep,Agent,Task,TodoWrite,TaskStop
DIS=Workflow,WebFetch,WebSearch,AskUserQuestion,EnterWorktree,ExitWorktree,SendMessage,ListAgents,PushNotification,SendUserFile,RemoteTrigger,CronCreate,CronDelete,CronList,Monitor,Skill,Artifact,DesignSync,SendFeedback,ToolSearch
P='Reply with the single word OK. Do not call any tool.'
cd "$OUT/wd" || exit 3
R=$OUT/surface-$VER.out; : > "$R"
run() { # $1 arm, $2 fence, rest = extra args
  local A=$1 F=$2; shift 2
  local S=$OUT/$VER-$A.jsonl
  "$BIN" --dangerously-skip-permissions --model claude-sonnet-5 --effort low --strict-mcp-config \
    --setting-sources user,project --settings "$F" "$@" -p "$P" --output-format stream-json --verbose \
    > "$S" 2> "$OUT/$VER-$A.err" < /dev/null &
  local pid=$! n=0
  while kill -0 $pid 2>/dev/null && [ $n -lt 180 ]; do sleep 1; n=$((n+1)); done
  kill -0 $pid 2>/dev/null && { kill $pid; echo "$A TIMEOUT" >> "$R"; }
  wait $pid; local rc=$?
  /usr/bin/python3 -c '
import json,sys
a,ver,rc=sys.argv[2],sys.argv[3],sys.argv[4]
for line in open(sys.argv[1], errors="replace"):
    try: r=json.loads(line)
    except ValueError: continue
    if r.get("type")=="system" and r.get("subtype")=="init":
        t=r.get("tools") or []; w=[x for x in t if x in ("WebSearch","WebFetch")]
        print("%-8s client %s rc=%s · %d tools · web=%s · %s" % (a, r.get("claude_code_version"), rc, len(t), "+".join(w) or "NONE", ",".join(t))); break
else: print("%-8s rc=%s NO INIT RECORD" % (a, rc))' "$S" "$A" "$VER" "$rc" >> "$R"
}
run cell    "$FENCE"              --tools "$TOOLS" --disallowedTools "$DIS"
run fence   "$FENCE"
run flags   "$OUT/fence-noweb.json" --tools "$TOOLS" --disallowedTools "$DIS"
run control "$OUT/fence-noweb.json"
grep -q '^control .*web=Web' "$R" && echo "INSTRUMENT: control lists a web tool — the arms are readable" >> "$R" \
  || echo "INSTRUMENT VOID: control lists no web tool — no arm's NONE means anything" >> "$R"
cat "$R"
