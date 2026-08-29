#!/bin/bash
# episode_s2.sh — ONE hermetic S2-Lean episode (stage A, B or C of one CLEVER problem): prepare · assert · run
# claude · extract bodies · check (kernel) · meter · archive. Same discipline and the same audit as harness/episode.sh
# (S1), with the environment being a native Lean project instead of a container (no Docker on this substrate).
#   usage: printf '%s\n' <arm> | episode_s2.sh <problem_id> <A|B|C> [--dry]
#   env:   BENCH · EPROOT (~/work) · H (~/bench/harness) · CFG · LEANPROJ (~/bench/lean/clever/src/lean4, the
#          shared prebuilt project: Imports only, human_eval/sample_examples ABSENT) · VIEWS (~/bench/s2views)
#          MODEL EFFORT MAX_TURNS(40) WALL_S(5400) TOKEN_CEILING(8000000) PROMPT_OVERRIDE LANDINGS CLAUDE_BIN(+_STUB)
# Stage B needs the SAME ARM's stage-A body for this problem: <BENCH>/state/s2/<problem>/<arm>/A.bodies.json.
set -u
PID="${1:?problem_id}"; STAGE="${2:?A|B|C}"; DRY="${3:-}"
read -r arm || true; [ -n "${arm:-}" ] || { echo "REFUSE: the arm must arrive on stdin"; exit 4; }
case "$arm" in a[0-9]|a[0-9][0-9]|s[0-9]) ;; *) echo "REFUSE: bad arm id '$arm'"; exit 4 ;; esac
case "$STAGE" in A|B|C) ;; *) echo "REFUSE: stage must be A, B or C"; exit 4 ;; esac
BENCH="${BENCH:-$HOME/bench}"; H="${H:-$BENCH/harness}"; S2="$H/s2lean"; CFG="${CFG:-$HOME/.claude-bench}"; EPROOT="${EPROOT:-$HOME/work}"
LEANPROJ="${LEANPROJ:-$BENCH/lean/clever/src/lean4}"; VIEWS="${VIEWS:-$BENCH/s2views}"
MODEL="${MODEL:-claude-sonnet-5}"; EFFORT="${EFFORT:-high}"; MAX_TURNS="${MAX_TURNS:-40}"
WALL_S="${WALL_S:-5400}"; TOKEN_CEILING="${TOKEN_CEILING:-8000000}"; LANDINGS="${LANDINGS:-s2-landings.log}"
PROMPT_OVERRIDE="${PROMPT_OVERRIDE:-}"; REAL_HOME="$HOME"
[ -n "${CLAUDE_BIN_STUB:-}" ] && LANDINGS="dryexec.log"
ep="ep-$(head -c 4 /dev/urandom | od -An -tx1 | tr -d ' \n')"
EP="$EPROOT/$ep"; ST="$BENCH/state/$ep"; TASK="problem_$PID"
mkdir -p "$EP" "$ST" "$BENCH/logs" "$EPROOT" "$BENCH/state/s2/$TASK/$arm"
log() { printf '%s %s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$*" | tee -a "$ST/episode.log"; }
now() { date -u +%s; }
term="UNSET"; t0=$(now); crc=""; SID=""; JSONL=""; killed=""; finished=""; CPID=""
CLAUDE_BIN="${CLAUDE_BIN:-$(command -v claude)}"
PINNED_CLAUDE=$(grep '^claude-version ' "$H/HASHES.txt" | cut -d' ' -f2)
AGENT_PATH="${AGENT_PATH:-/usr/local/bin:/opt/homebrew/bin:/usr/bin:/bin:/usr/sbin:/sbin:$REAL_HOME/.local/bin}"
die() { log "HARNESS_ERROR $*"; term="HARNESS_ERROR"; finish 1; }
printf 'EPISODE %s\n' "$ep"
self_sha=$(shasum -a 256 "$0" | cut -d' ' -f1); want_self=$(grep '^s2lean/episode_s2.sh ' "$H/HASHES.txt" | cut -d' ' -f2)
[ "$self_sha" = "$want_self" ] || { echo "REFUSE: episode_s2.sh sha $self_sha is not the pinned $want_self"; rm -rf "$EP" "$ST"; exit 5; }
# the raw CLEVER sources (full solutions) must NOT be on this host during episodes; the shared project holds Imports only
[ -e "$LEANPROJ/human_eval" ] || [ -e "$LEANPROJ/sample_examples" ] && { echo "REFUSE: $LEANPROJ carries human_eval/ or sample_examples/ (full solutions)"; rm -rf "$EP" "$ST"; exit 3; }
[ -d "$LEANPROJ/.lake/build/lib/lean/Imports" ] || { echo "REFUSE: shared project is not built (Imports olean missing)"; rm -rf "$EP" "$ST"; exit 3; }
[ -z "$(ls "$LEANPROJ/.lake/build/lib/lean/human_eval" 2>/dev/null)" ] || { echo "REFUSE: human_eval oleans present in the shared build"; rm -rf "$EP" "$ST"; exit 3; }
# stage A must run with NO ground-truth spec on the host: the BC views are shipped only after every stage-A landing
if [ "$STAGE" = "A" ]; then [ -e "$VIEWS/$TASK/frozen.json" ] && { echo "REFUSE: frozen.json (ground truth) present on the host during stage A"; rm -rf "$EP" "$ST"; exit 3; }; fi
[ -e "$VIEWS/$TASK/A.lean" ] || { echo "REFUSE: no A view for $TASK"; rm -rf "$EP" "$ST"; exit 3; }

finish() {
  [ -n "$finished" ] && return 0
  finished=1; rc="${1:-0}"
  [ -d "$EP" ] && mv "$EP" "$ST/eptree" 2>/dev/null
  [ -n "$PROMPT_OVERRIDE" ] && term="SMOKE($term)"
  [ -n "${CLAUDE_BIN_STUB:-}" ] && term="DRYEXEC($term)"
  t1=$(now)
  ARMV="$arm" python3 - "$ST" "$PID" "$STAGE" "$term" "$rc" "$t0" "$t1" "$MODEL" "$EFFORT" "$MAX_TURNS" "$WALL_S" "$TOKEN_CEILING" "$H" "$CFG" "$CLAUDE_BIN" "$ep" "${SID:-}" "$AGENT_PATH" "$LEANPROJ" <<'PY'
import json,sys,hashlib,os,subprocess
(st,pid,stage,term,rc,t0,t1,model,effort,mt,wall,ceil,h,cfg,cbin,ep,sid,apath,proj)=sys.argv[1:]
arm=os.environ.get("ARMV")
def sha(p):
    try: return hashlib.sha256(open(p,'rb').read()).hexdigest()
    except Exception: return None
def jl(p):
    try: return json.load(open(p))
    except Exception: return {}
pm=jl(os.path.join(st,"prompt_meta.json")); mt_=jl(os.path.join(st,"meter.json")); ck=jl(os.path.join(st,"check.json"))
starts=ends=ok=0
try:
    for l in open(os.path.join(st,"rt.log")):
        if "\tSTART\t" in l: starts+=1
        if "\tEND\t" in l:
            ends+=1; ok+= ("\trc=0\t" in l)
except Exception: pass
armfile=os.path.join(h,"arms",arm+".md")
def ver():
    try: return subprocess.check_output([cbin,"--version"]).decode().strip()
    except Exception: return None
m={"episode":ep,"substrate":"S2-Lean/CLEVER","instance_id":"problem_%s"%pid,"stage":stage,"arm":arm,
   "termination":term,"claude_exit_code":int(rc),"start_utc":int(t0),"end_utc":int(t1),"wall_s":int(t1)-int(t0),
   "model_requested":model,"effort":effort,"max_turns":int(mt),"wall_ceiling_s":int(wall),"token_ceiling":int(ceil),
   "session_id":sid,"claude_bin":cbin,"claude_bin_target":(os.path.realpath(cbin) if cbin else None),"claude_version":ver(),
   "host_arch":os.uname().machine,"lean_toolchain":(open(os.path.join(proj,"lean-toolchain")).read().strip() if os.path.exists(os.path.join(proj,"lean-toolchain")) else None),
   "agent_path":apath,"freeze_commit":(open(os.path.join(h,"FREEZE-COMMIT")).read().strip() if os.path.exists(os.path.join(h,"FREEZE-COMMIT")) else None),
   "arm_rendering_sha256":hashlib.sha256(open(os.path.join(h,"s2lean","base.md"),"rb").read()+open(armfile,"rb").read()).hexdigest(),
   "arm_block_bytes":os.path.getsize(armfile),"claude_md_sha256":sha(os.path.join(st,"eptree","CLAUDE.md")),
   "prompt_sha256":pm.get("prompt_sha256"),"prompt_sha256_canonical":pm.get("prompt_sha256_canonical"),"view_sha256":pm.get("view_sha256"),
   "settings_sha256":sha(os.path.join(cfg,"settings.json")),"hook_sha256":sha(os.path.join(h,"hook-deny-network.sh")),"episode_sh_sha256":sha(os.path.join(h,"s2lean","episode_s2.sh")),
   "task_file_sha256":sha(os.path.join(st,"eptree","repo","task.lean")),"bodies_sha256":sha(os.path.join(st,"bodies.json")),
   "rt_calls":ends,"rt_calls_rc0":ok,"rt_unfinished":max(0,starts-ends),
   "metered_sum":mt_.get("metered_sum"),"metered_sum_governing":(mt_.get("crosscheck") or {}).get("metered_sum_governing"),
   "calls":mt_.get("calls"),"void_reasons":mt_.get("void_reasons"),"compactions":mt_.get("compactions"),"models":mt_.get("models"),
   "tool_timeouts":mt_.get("tool_timeouts"),"first_call_usage":mt_.get("first_call_usage"),
   "check":{k:ck.get(k) for k in ("compiled","sorry_lines","axioms","axioms_ok","forbidden","passed","rc","wall_s")} if ck else None,
   "passed":bool(ck.get("passed")) if ck else False,
   "flags":["-p <prompt>","--model",model,"--effort",effort,"--max-turns",mt,"--dangerously-skip-permissions","--disallowedTools","WebFetch,WebSearch,Agent,Task,Workflow,Skill,Monitor,CronCreate,CronDelete,CronList,RemoteTrigger,SendMessage,ListAgents,PushNotification,SendUserFile,EnterWorktree,ExitWorktree","--strict-mcp-config","--setting-sources","user,project","--output-format","json","--session-id <uuid>"]}
json.dump(m,open(os.path.join(st,"manifest.json"),"w"),indent=1,sort_keys=True)
PY
  ( cd "$ST" && find . -type f ! -name SHA256SUMS -exec shasum -a 256 {} + > SHA256SUMS 2>/dev/null )
  log "LANDED $ep task=$TASK stage=$STAGE arm=$arm term=$term passed=$(python3 -c "import json;print(json.load(open('$ST/manifest.json'))['passed'])" 2>/dev/null) rc=$rc wall=$(( $(now)-t0 ))s metered=$(python3 -c "import json;m=json.load(open('$ST/manifest.json'));print(m['metered_sum_governing'] or m['metered_sum'])" 2>/dev/null)"
  printf '%s %s %s %s %s %s\n' "$ep" "$TASK" "$STAGE" "$arm" "$term" "$(python3 -c "import json;m=json.load(open('$ST/manifest.json'));print(m['metered_sum_governing'] or m['metered_sum'] or 0)" 2>/dev/null)" >> "$BENCH/logs/$LANDINGS"
  exit "$rc"
}
trap '[ -z "$finished" ] && { term="HARNESS_ERROR(abort:line$LINENO:$term)"; finish 1; }' EXIT
trap '[ -n "${CPID:-}" ] && { kill -TERM "$CPID" 2>/dev/null; sleep 5; kill -KILL "$CPID" 2>/dev/null; }; term="HARNESS_ERROR(signal)"; finish 1' INT TERM

[ -n "$CLAUDE_BIN" ] || die "claude not found"
if [ -z "${CLAUDE_BIN_STUB:-}" ]; then cv=$("$CLAUDE_BIN" --version 2>/dev/null | cut -d' ' -f1); [ "$cv" = "$PINNED_CLAUDE" ] || die "claude version '$cv' is not the pinned $PINNED_CLAUDE"; fi
# ── 1. the working copy: a project dir with the lakefile + Imports SOURCE, `.lake` → the shared read-only build ──
mkdir -p "$EP/repo" && cp "$LEANPROJ/lakefile.lean" "$LEANPROJ/lake-manifest.json" "$LEANPROJ/lean-toolchain" "$EP/repo/" && cp -R "$LEANPROJ/Imports" "$EP/repo/Imports" || die "project copy"
ln -s "$LEANPROJ/.lake" "$EP/repo/.lake" || die "lake link"
# ── 2. the task file for this stage ──────────────────────────────────────────────────────────────
case "$STAGE" in
  A) cp "$VIEWS/$TASK/A.lean" "$EP/repo/task.lean" || die "A view" ;;
  C) cp "$VIEWS/$TASK/C.lean" "$EP/repo/task.lean" || die "C view" ;;
  B) AB="$BENCH/state/s2/$TASK/$arm/A.bodies.json"; [ -s "$AB" ] || die "no stage-A body for $TASK/$arm"
     python3 - "$VIEWS/$TASK/frozen.json" "$AB" "$S2/build_views.py" > "$EP/repo/task.lean" <<'PY' || die "B assemble"
import json,sys,importlib.util
fz=json.load(open(sys.argv[1])); bd=json.load(open(sys.argv[2]))
spec=importlib.util.spec_from_file_location("bv",sys.argv[3]); bv=importlib.util.module_from_spec(spec); spec.loader.exec_module(bv)
sys.stdout.write(bv.assemble_B(fz, bd["generated_spec_body"]))
PY
     ;;
esac
bash "$H/check2b.sh" "$EP/repo" > "$ST/check2b.host.log" 2>&1 || { cat "$ST/check2b.host.log"; die "CHECK2B host FAIL"; }
# ── 3. prompt + arm file + wrapper; the episode dir holds EXACTLY CLAUDE.md repo rt ─────────────
python3 - "$STAGE" "$EP" "$ST" "$H/s2lean" "$arm" <<'PY' || die "prompt/arm build"
import json,sys,hashlib,os
stage,ep,st,s2,arm=sys.argv[1:]
tmpl=open(os.path.join(s2,"prompt_%s.md"%stage)).read()
prompt=tmpl.replace("__EP__",ep); canon=tmpl
base=open(os.path.join(s2,"base.md")).read().replace("__EP__",ep); armb=open(os.path.join(os.path.dirname(s2),"arms",arm+".md")).read()
open(os.path.join(st,"prompt.md"),"w").write(prompt); open(os.path.join(ep,"CLAUDE.md"),"w").write(base+armb)
view=open(os.path.join(ep,"repo","task.lean"),"rb").read()
json.dump({"stage":stage,"prompt_sha256":hashlib.sha256(prompt.encode()).hexdigest(),"prompt_sha256_canonical":hashlib.sha256(canon.encode()).hexdigest(),"view_sha256":hashlib.sha256(view).hexdigest()},open(os.path.join(st,"prompt_meta.json"),"w"),indent=1)
PY
if [ -n "$PROMPT_OVERRIDE" ]; then printf '%s\n' "$PROMPT_OVERRIDE" > "$ST/prompt.md"; cp "$ST/prompt.md" "$ST/prompt_override.txt"; fi
sed -e "s|__ST__|$ST|g" -e "s|__EP__|$EP|g" "$S2/rt.template" > "$EP/rt" && chmod +x "$EP/rt"
[ "$(ls -A "$EP" | sort | tr '\n' ' ')" = "CLAUDE.md repo rt " ] || die "episode dir holds more than CLAUDE.md repo rt: $(ls -A "$EP")"
[ "$(ls -A "$EPROOT" | tr '\n' ' ')" = "$ep " ] || die "EPROOT holds more than this episode: $(ls -A "$EPROOT")"
# ── 4. hermeticity assertions (as S1) ───────────────────────────────────────────────────────────
p="$EP"; while [ "$p" != "/" ]; do p=$(dirname "$p"); [ -e "$p/CLAUDE.md" ] && die "CLAUDE.md above the episode at $p"; done
[ -e "$CFG/CLAUDE.md" ] && die "CLAUDE.md in the config dir"
[ -z "$(ls -A "$CFG/projects" 2>/dev/null)" ] || die "config dir projects/ is not empty before the episode"
for d in file-history session-env sessions todos shell-snapshots debug; do [ -z "$(ls -A "$CFG/$d" 2>/dev/null)" ] || die "config dir $d/ is not empty before the episode"; done
for f in CLAUDE.md commands agents skills rules hooks .mcp.json; do [ -e "$CFG/$f" ] && die "config dir carries agent-influencing entry $f"; done
want_s=$(grep '^settings.json ' "$H/HASHES.txt" | cut -d' ' -f2); [ "$want_s" = "$(shasum -a 256 "$CFG/settings.json" | cut -d' ' -f1)" ] || die "settings.json sha drift"
want_h=$(grep '^hook-deny-network.sh ' "$H/HASHES.txt" | cut -d' ' -f2); [ "$want_h" = "$(shasum -a 256 "$H/hook-deny-network.sh" | cut -d' ' -f1)" ] || die "hook sha drift"
want_a=$(grep -F "rendered-s2-$arm(__EP__) " "$H/HASHES.txt" | cut -d' ' -f2); have_a=$(cat "$S2/base.md" "$H/arms/$arm.md" | shasum -a 256 | cut -d' ' -f1)
[ -n "$want_a" ] && [ "$want_a" = "$have_a" ] || die "arm rendering sha $have_a != pinned '$want_a'"
[ "$(sed "s|$EP|__EP__|g" "$EP/CLAUDE.md" | shasum -a 256 | cut -d' ' -f1)" = "$have_a" ] || die "episode CLAUDE.md is not the pinned rendering"
want_v=$(grep -F "view-$STAGE $TASK " "$H/HASHES.txt" | cut -d' ' -f3); have_v=$(python3 -c "import json;print(json.load(open('$ST/prompt_meta.json'))['view_sha256'])")
if [ "$STAGE" != "B" ]; then [ -n "$want_v" ] && [ "$want_v" = "$have_v" ] || die "view sha $have_v != pinned '$want_v' for $TASK/$STAGE"; fi
# the wrapper under the agent's exact environment: Mathlib import must succeed (the slow first load happens HERE, not in the episode)
( cd "$EP/repo" && env -i HOME="$REAL_HOME" USER="$USER" LOGNAME="$USER" PATH="$AGENT_PATH" TERM=dumb LANG=en_US.UTF-8 "$EP/rt" 'printf "import Imports.AllImports\n#eval 6*7\n" > /tmp/rtprobe_'"$ep"'.lean && lake env lean /tmp/rtprobe_'"$ep"'.lean' ) > "$ST/env_probe.txt" 2>&1 || { cat "$ST/env_probe.txt"; die "rt wrapper (lake env lean) fails under the agent environment"; }
rm -f "/tmp/rtprobe_$ep.lean"; mv "$ST/rt.log" "$ST/rt.probe.log" 2>/dev/null
log "PREPARED task=$TASK stage=$STAGE lean=$(cat "$EP/repo/lean-toolchain") probe=$(tail -1 "$ST/env_probe.txt")"
[ "$DRY" = "--dry" ] && { term="DRY"; finish 0; }
# ── 5. run claude, watched (identical to S1) ────────────────────────────────────────────────────
SID=$(uuidgen | tr 'A-Z' 'a-z')
( cd "$EP/repo" && exec env -i HOME="$REAL_HOME" USER="$USER" LOGNAME="$USER" PATH="$AGENT_PATH" TERM=dumb LANG=en_US.UTF-8 \
    TMPDIR="${TMPDIR:-/tmp}" CLAUDE_CONFIG_DIR="$CFG" BENCH_EP="$EP" DISABLE_AUTOUPDATER=1 DISABLE_UPDATES=1 CLAUDE_CODE_DISABLE_FILE_CHECKPOINTING=1 \
    "$CLAUDE_BIN" -p "$(cat "$ST/prompt.md")" --model "$MODEL" --effort "$EFFORT" --max-turns "$MAX_TURNS" --dangerously-skip-permissions \
      --disallowedTools "WebFetch,WebSearch,Agent,Task,Workflow,Skill,Monitor,CronCreate,CronDelete,CronList,RemoteTrigger,SendMessage,ListAgents,PushNotification,SendUserFile,EnterWorktree,ExitWorktree" \
      --strict-mcp-config --setting-sources user,project --output-format json --session-id "$SID" > "$ST/result.json" 2> "$ST/claude.stderr" ) &
CPID=$!; log "CLAUDE started pid=$CPID session=$SID"
while kill -0 "$CPID" 2>/dev/null; do
  sleep 20; el=$(( $(now) - t0 ))
  [ -z "$JSONL" ] && JSONL=$(find "$CFG/projects" -name "$SID.jsonl" 2>/dev/null | head -1)
  [ "$el" -gt "$WALL_S" ] && killed="WALLCLOCK"
  if [ -n "$JSONL" ] && [ -z "$killed" ]; then ms=$(python3 "$H/meter.py" "$JSONL" --live 2>/dev/null | python3 -c "import json,sys; print(json.load(sys.stdin)['metered_sum'])" 2>/dev/null || echo 0); [ "${ms:-0}" -ge "$TOKEN_CEILING" ] && killed="TOKEN_CEILING"; fi
  if [ -n "$killed" ]; then log "WATCHDOG $killed at ${el}s"; kill -TERM "$CPID" 2>/dev/null; sleep 10; kill -KILL "$CPID" 2>/dev/null; break; fi
done
wait "$CPID"; crc=$?; sleep 2
if pgrep -f -- "--session-id $SID" >/dev/null 2>&1; then pkill -KILL -f -- "--session-id $SID"; log "ORPHAN_KILLED"; fi
[ -z "$JSONL" ] && JSONL=$(find "$CFG/projects" -name "$SID.jsonl" 2>/dev/null | head -1)
# ── 6. termination (as S1), then the KERNEL: extract bodies → assemble canonical file → check ────
python3 - "$ST" > "$ST/cli_text.txt" 2>/dev/null <<'PY'
import json,sys,os
st=sys.argv[1]
try:
    r=json.load(open(os.path.join(st,"result.json"))); print(("ERR:" if r.get("is_error") else "")+str(r.get("subtype",""))); print(str(r.get("result") or "")[:2000].replace("\n"," ")); print(json.dumps(r.get("error","") or "")[:500])
except Exception: print("")
PY
sub=$(head -1 "$ST/cli_text.txt" 2>/dev/null); msgs="$(sed -n 3p "$ST/cli_text.txt" 2>/dev/null) $(cat "$ST/claude.stderr" 2>/dev/null)"
quota_rx='rate.?limit|usage limit|hit your [a-z ]*limit|limit[^a-z]*resets|limit will reset|usage credits|extra usage|spend.?limit|quota|overloaded|billing|too many requests|(^|[^0-9])429([^0-9]|$)'
auth_rx='not logged in|invalid api key|authentication (error|failed)|unlock-keychain|keychain|please run /login|(^|[^a-z])log ?in( |$)|unauthori[sz]ed'
if [ -n "$killed" ]; then term="$killed"
elif [ -z "$JSONL" ]; then if printf '%s' "$msgs" | grep -Eqi "$auth_rx"; then term="AUTH"; elif printf '%s' "$msgs" | grep -Eqi "$quota_rx"; then term="QUOTA"; else term="HARNESS_ERROR"; fi
else case "$sub" in success) term="DONE" ;; error_max_turns|ERR:error_max_turns) term="ROUNDS_EXHAUSTED" ;; "") term="HARNESS_ERROR" ;;
  *) if printf '%s' "$msgs" | grep -Eqi "$auth_rx"; then term="AUTH"; elif printf '%s' "$msgs" | grep -Eqi "$quota_rx"; then term="QUOTA"; else term="ERROR_${sub#ERR:}"; fi ;; esac
fi
printf '%s' "$msgs" | grep -Eio "$quota_rx|$auth_rx" | head -3 | tr '\n' ' ' > "$ST/quota_evidence.txt"
python3 "$S2/extract.py" "$STAGE" "$EP/repo/task.lean" > "$ST/bodies.json" 2>"$ST/extract.err" || { : > "$ST/bodies.json"; term="${term}+NO_BODIES"; }
if [ -s "$ST/bodies.json" ] && [ -z "${CLAUDE_BIN_STUB:-}" ]; then
  FZ="$VIEWS/$TASK/frozen.json"; [ "$STAGE" = "A" ] && FZ="$VIEWS/$TASK/frozenA.json"   # stage A checks against the spec header only (no GT on the host)
  ( cd "$LEANPROJ" && PATH="$HOME/.elan/bin:$PATH" python3 "$S2/check.py" "$STAGE" "$FZ" "$ST/bodies.json" "$LEANPROJ" "$ST/canonical.lean" --timeout 900 ) > "$ST/check.json" 2> "$ST/check.err" || true
  [ -s "$ST/check.json" ] || term="HARNESS_ERROR(check:$term)"
  [ "$STAGE" = "A" ] && cp "$ST/bodies.json" "$BENCH/state/s2/$TASK/$arm/A.bodies.json"
fi
if [ -n "$JSONL" ]; then
  cp "$JSONL" "$ST/session.jsonl"
  bash "$H/hook-deny-network.sh" --pattern-escape > "$ST/escape_pattern.txt"; bash "$H/hook-deny-network.sh" --pattern-url > "$ST/url_pattern.txt"
  nj=$(find "$CFG/projects" -name '*.jsonl' | wc -l | tr -d ' '); nsub=$(find "$CFG/projects" -type d -name subagents | wc -l | tr -d ' ')
  extra_j=$(find "$CFG/projects" -name '*.jsonl' ! -name "$SID.jsonl" 2>/dev/null | tr '\n' ' ')
  python3 "$H/meter.py" "$ST/session.jsonl" --result "$ST/result.json" --ep "$EP" --escape-file "$ST/escape_pattern.txt" --url-file "$ST/url_pattern.txt" ${extra_j:+--extra $extra_j} > "$ST/meter.json" 2> "$ST/meter.err"
  [ -s "$ST/meter.json" ] || term="HARNESS_ERROR(meter:$term)"
  python3 -c "import json;m=json.load(open('$ST/meter.json'));print('\n'.join(m['escape_unblocked']+['BLOCKED: '+x for x in m['escape_attempts_blocked']]))" > "$ST/network_audit.txt" 2>/dev/null
  if [ "$nj" != "1" ] || [ "$nsub" != "0" ]; then term="VOID(SUBAGENT:${term})"
  elif python3 -c "import json,sys;sys.exit(0 if json.load(open('$ST/meter.json'))['void'] else 1)" 2>/dev/null; then term="VOID($(python3 -c "import json;print(','.join(json.load(open('$ST/meter.json'))['void_reasons']))"):${term})"; fi
  if [ "$(python3 -c "import json;print(json.load(open('$ST/meter.json')).get('calls',0))" 2>/dev/null)" = "0" ]; then case "$term" in AUTH*|QUOTA*|HARNESS*|VOID*) ;; *) term="QUOTA(no_call:$term)" ;; esac; fi
fi
mkdir -p "$ST/configdir-projects" && cp -R "$CFG/projects/." "$ST/configdir-projects/" 2>/dev/null; rm -rf "$CFG/projects"/* 2>/dev/null
rm -rf "$CFG/todos" "$CFG/shell-snapshots" "$CFG/debug" "$CFG/file-history" "$CFG/session-env" "$CFG/sessions" 2>/dev/null; : > "$CFG/history.jsonl" 2>/dev/null
python3 - "$CFG/.claude.json" "$EPROOT" <<'PY' 2>/dev/null
import json,sys
p,root=sys.argv[1],sys.argv[2]
try:
    o=json.load(open(p)); pr=o.get("projects") or {}
    for k in [k for k in pr if k.startswith(root)]: del pr[k]
    json.dump(o,open(p,"w"),indent=2)
except Exception: pass
PY
rtc=$(grep -c $'\tEND\t' "$ST/rt.log" 2>/dev/null); rtc=${rtc:-0}; rt127=$(grep -Ec $'\trc=12[67]\t' "$ST/rt.log" 2>/dev/null); rt127=${rt127:-0}
[ "$rtc" -gt 0 ] && [ "$rt127" -eq "$rtc" ] && term="HARNESS_ERROR(rt_all_failed:${term})"
finish "$crc"
