#!/bin/bash
# episode.sh — ONE hermetic episode: prepare · assert · run claude · extract patch · meter · archive.
#   usage: printf '%s' <arm> | episode.sh <instance_id> [--dry]        (the arm arrives on STDIN: never argv,
#          never env — an env var survives `unset` in the kernel's saved exec environment and shows in `ps -E`)
#   env:   BENCH (~/bench: harness/state/logs) · EPROOT (~/work: the ONLY tree the agent is meant to see) · H · CFG
#          MODEL · EFFORT · MAX_TURNS (40) · WALL_S (5400) · TOKEN_CEILING (8000000 = R x 200k per-call sub-cap, so
#          --max-turns is the binding stop) · PROMPT_OVERRIDE (smoke probes: lands as SMOKE(...)) · LANDINGS
#          CLAUDE_BIN + CLAUDE_BIN_STUB=1 (ONLY for --dry-exec: a stub in place of claude so the post-launch path executes)
# Runs on the Studio under bash 3.2. Prints EPISODE <ep> first, LANDED <ep> ... last; writes <STATE>/<ep>/manifest.json.
# ⛔ ARM-BLINDNESS IS BY AUDIT, NOT BY CONSTRUCTION (refuter F1): the agent runs as the same uid with a docker
#    socket in reach. What this script guarantees: the arm name is in no argv, no env, and in no file the hook or
#    the audit permits while claude runs (manifest is written AFTER exit); <EPROOT> holds ONLY this episode; every
#    tool call is audited post hoc (meter.py) and an escape VOIDs. Any abnormal exit still lands (EXIT trap).
set -u
IID="${1:?instance_id}"; DRY="${2:-}"
read -r arm || true; [ -n "${arm:-}" ] || { echo "REFUSE: the arm must arrive on stdin"; exit 4; }
case "$arm" in a[0-9]|a[0-9][0-9]|s[0-9]) ;; *) echo "REFUSE: bad arm id '$arm'"; exit 4 ;; esac
BENCH="${BENCH:-$HOME/bench}"; H="${H:-$BENCH/harness}"; CFG="${CFG:-$HOME/.claude-bench}"; EPROOT="${EPROOT:-$HOME/work}"
MODEL="${MODEL:-claude-sonnet-5}"; EFFORT="${EFFORT:-high}"; MAX_TURNS="${MAX_TURNS:-40}"
WALL_S="${WALL_S:-5400}"; TOKEN_CEILING="${TOKEN_CEILING:-8000000}"; LANDINGS="${LANDINGS:-landings.log}"
PROMPT_OVERRIDE="${PROMPT_OVERRIDE:-}"; REAL_HOME="$HOME"
# a stub-driven run can never land where the driver reads (refuter RI3-F1): it is typed DRYEXEC(...) and logged apart
[ -n "${CLAUDE_BIN_STUB:-}" ] && LANDINGS="dryexec.log"
ep="ep-$(head -c 4 /dev/urandom | od -An -tx1 | tr -d ' \n')"
EP="$EPROOT/$ep"; ST="$BENCH/state/$ep"; CTR="$ep"
mkdir -p "$EP" "$ST/extract" "$BENCH/logs" "$EPROOT"
log() { printf '%s %s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$*" | tee -a "$ST/episode.log"; }
now() { date -u +%s; }
term="UNSET"; t0=$(now); crc=""; SID=""; JSONL=""; killed=""; finished=""; CPID=""
CLAUDE_BIN="${CLAUDE_BIN:-$(command -v claude)}"; DOCKER_BIN=$(command -v docker)
PINNED_CLAUDE=$(grep '^claude-version ' "$H/HASHES.txt" | cut -d' ' -f2)
# the agent's PATH: the Studio's login PATH (measured by smoke probe A1 from inside the agent), stated not assumed
AGENT_PATH="${AGENT_PATH:-/usr/local/bin:/opt/homebrew/bin:/usr/bin:/bin:/usr/sbin:/sbin:$REAL_HOME/.local/bin}"
die() { log "HARNESS_ERROR $*"; term="HARNESS_ERROR"; finish 1; }
printf 'EPISODE %s\n' "$ep"

# ── the harness that runs must be the harness that is pinned (refuter RI-2) ─────────────────────
self_sha=$(shasum -a 256 "$0" | cut -d' ' -f1); want_self=$(grep '^episode.sh ' "$H/HASHES.txt" | cut -d' ' -f2)
[ "$self_sha" = "$want_self" ] || { echo "REFUSE: episode.sh sha $self_sha is not the pinned $want_self (hashes.sh + sync_studio.sh first)"; rm -rf "$EP" "$ST"; exit 5; }
# ── ONLY the projection is on this host during episodes; no gold-bearing harness log either ──────
[ -e "$H/data/verified.json" ] && { echo "REFUSE: the full dataset is present at $H/data/verified.json during an episode (studio_phase.sh out first)"; rm -rf "$EP" "$ST"; exit 3; }
[ -z "$(find "$BENCH/state/controls" "$BENCH/state/scoring" -path '*run_evaluation*' -type f 2>/dev/null | head -1)" ] || { echo "REFUSE: gold-bearing harness logs remain under state/controls|scoring (studio_phase.sh out first)"; rm -rf "$EP" "$ST"; exit 3; }
read -r IMG DIG BASE < <(python3 - "$IID" "$H" <<'PY'
import json,sys
iid,h=sys.argv[1],sys.argv[2]
d=json.load(open(h+"/IMAGE-DIGESTS.json"))["images"][iid]
row=[r for r in json.load(open(h+"/data/problem_statements.json")) if r["instance_id"]==iid][0]
print(d["image"], d["digest"], row["base_commit"])
PY
) || { echo "no metadata for $IID"; rm -rf "$EP" "$ST"; exit 1; }
log "task=$IID image=$IMG@$DIG base=$BASE"

finish() {
  [ -n "$finished" ] && return 0
  finished=1; rc="${1:-0}"
  # a container that died under the agent makes every later rt call plumbing, whatever its rc (refuter RI3-R1) —
  # measured BEFORE the container is removed (the first amendment cut measured after, and always read dead)
  container_alive=""
  if [ -n "$SID" ]; then container_alive=$("$DOCKER_BIN" inspect -f '{{.State.Running}}' "$CTR" 2>/dev/null); [ "$container_alive" = "true" ] || term="HARNESS_ERROR(container_dead:$term)"; fi
  "$DOCKER_BIN" rm -f "$CTR" >/dev/null 2>&1
  [ -d "$EP" ] && mv "$EP" "$ST/eptree" 2>/dev/null   # the agent-visible tree is archived, never left for the next episode
  # smoke probes are never scored: they land as SMOKE(...) in their own log (refuter RI-8)
  [ -n "$PROMPT_OVERRIDE" ] && term="SMOKE($term)"
  [ -n "${CLAUDE_BIN_STUB:-}" ] && term="DRYEXEC($term)"
  t1=$(now)
  ARMV="$arm" CONTAINER_ALIVE="$container_alive" python3 - "$ST" "$IID" "$IMG" "$DIG" "$BASE" "$term" "$rc" "$t0" "$t1" "$MODEL" "$EFFORT" "$MAX_TURNS" "$WALL_S" "$TOKEN_CEILING" "$H" "$CFG" "$CLAUDE_BIN" "$ep" "${SID:-}" "$AGENT_PATH" <<'PY'
import json,sys,hashlib,os,subprocess
(st,iid,img,dig,base,term,rc,t0,t1,model,effort,mt,wall,ceil,h,cfg,cbin,ep,sid,apath)=sys.argv[1:]
arm=os.environ.get("ARMV")
def sha(p):
    try: return hashlib.sha256(open(p,'rb').read()).hexdigest()
    except Exception: return None
def ver():
    try: return subprocess.check_output([cbin,"--version"]).decode().strip()
    except Exception: return None
def jl(p):
    try: return json.load(open(p))
    except Exception: return {}
pm=jl(os.path.join(st,"prompt_meta.json")); mt_=jl(os.path.join(st,"meter.json"))
starts=ends=ok=0
try:
    for l in open(os.path.join(st,"rt.log")):
        if "\tSTART\t" in l: starts+=1
        if "\tEND\t" in l:
            ends+=1; ok+= ("\trc=0\t" in l)
except Exception: pass
armfile=os.path.join(h,"arms",arm+".md")
m={"episode":ep,"instance_id":iid,"arm":arm,"image":img,"digest":dig,"base_commit":base,
   "termination":term,"claude_exit_code":int(rc),"start_utc":int(t0),"end_utc":int(t1),"wall_s":int(t1)-int(t0),
   "model_requested":model,"effort":effort,"max_turns":int(mt),"wall_ceiling_s":int(wall),"token_ceiling":int(ceil),
   "session_id":sid,"claude_bin":cbin,"claude_bin_target":(os.path.realpath(cbin) if cbin else None),"claude_version":ver(),
   "host_arch":os.uname().machine,"docker_platform":"linux/amd64","agent_path":apath,"autocompact":"CLI default (auto) at the recorded claude_version; not pinned",
   "arm_rendering_sha256":hashlib.sha256(open(os.path.join(h,"base.md"),"rb").read()+open(armfile,"rb").read()).hexdigest(),
   "arm_block_bytes":os.path.getsize(armfile),"claude_md_sha256":sha(os.path.join(st,"eptree","CLAUDE.md")),
   "prompt_sha256":pm.get("prompt_sha256"),"prompt_sha256_canonical":pm.get("prompt_sha256_canonical"),
   "prompt_override_sha256":sha(os.path.join(st,"prompt_override.txt")),
   "problem_statement_sha256":pm.get("problem_statement_sha256"),
   "settings_sha256":sha(os.path.join(cfg,"settings.json")),"hook_sha256":sha(os.path.join(h,"hook-deny-network.sh")),"episode_sh_sha256":sha(os.path.join(h,"episode.sh")),
   "model_patch_sha256":sha(os.path.join(st,"model_patch.diff")),
   "model_patch_bytes":(os.path.getsize(os.path.join(st,"model_patch.diff")) if os.path.exists(os.path.join(st,"model_patch.diff")) else None),
   "agent_made_git":os.path.exists(os.path.join(st,"eptree","repo",".git")),
   "rt_calls":ends,"rt_calls_rc0":ok,"rt_unfinished":max(0,starts-ends),
   "metered_sum":mt_.get("metered_sum"),"metered_sum_governing":(mt_.get("crosscheck") or {}).get("metered_sum_governing"),
   "metered_sum_incl_compaction_floor":mt_.get("metered_sum_incl_compaction_floor"),
   "calls":mt_.get("calls"),"void_reasons":mt_.get("void_reasons"),"compactions":mt_.get("compactions"),
   "models":mt_.get("models"),"service_tiers":mt_.get("service_tiers"),"tool_timeouts":mt_.get("tool_timeouts"),
   "first_call_usage":mt_.get("first_call_usage"),"unknown_tools":mt_.get("unknown_tools"),
   "quota_evidence":(open(os.path.join(st,"quota_evidence.txt")).read().strip() if os.path.exists(os.path.join(st,"quota_evidence.txt")) else None),
   "freeze_commit":(open(os.path.join(h,"FREEZE-COMMIT")).read().strip() if os.path.exists(os.path.join(h,"FREEZE-COMMIT")) else None),
   "container_running_at_end":os.environ.get("CONTAINER_ALIVE"),

   "flags":["-p <prompt>","--model",model,"--effort",effort,"--max-turns",mt,"--dangerously-skip-permissions",
            "--disallowedTools","WebFetch,WebSearch,Agent,Task,Workflow,Skill,Monitor,CronCreate,CronDelete,CronList,RemoteTrigger,SendMessage,ListAgents,PushNotification,SendUserFile,EnterWorktree,ExitWorktree",
            "--strict-mcp-config","--setting-sources","user,project","--output-format","json","--session-id <uuid>"]}
json.dump(m,open(os.path.join(st,"manifest.json"),"w"),indent=1,sort_keys=True)
PY
  ( cd "$ST" && find . -type f ! -name SHA256SUMS -exec shasum -a 256 {} + > SHA256SUMS 2>/dev/null )
  log "LANDED $ep task=$IID arm=$arm term=$term rc=$rc wall=$(( $(now)-t0 ))s metered=$(python3 -c "import json;m=json.load(open('$ST/manifest.json'));print(m['metered_sum_governing'] or m['metered_sum'])" 2>/dev/null)"
  printf '%s %s %s %s %s\n' "$ep" "$IID" "$arm" "$term" "$(python3 -c "import json;m=json.load(open('$ST/manifest.json'));print(m['metered_sum_governing'] or m['metered_sum'] or 0)" 2>/dev/null)" >> "$BENCH/logs/$LANDINGS"
  exit "$rc"
}
# any abnormal exit still cleans up and lands (refuter RI-1): the trap fires on the way out with a typed reason
trap '[ -z "$finished" ] && { term="HARNESS_ERROR(abort:line$LINENO:$term)"; finish 1; }' EXIT
trap '[ -n "${CPID:-}" ] && { kill -TERM "$CPID" 2>/dev/null; sleep 5; kill -KILL "$CPID" 2>/dev/null; }; term="HARNESS_ERROR(signal)"; finish 1' INT TERM

# ── 1. image present and IS the pinned digest; claude is the pinned version and no updater may move it ────
"$DOCKER_BIN" image inspect "$IMG@$DIG" >/dev/null 2>&1 || die "image $IMG@$DIG not present (pull_pilot.sh first)"
[ -n "$CLAUDE_BIN" ] || die "claude not found"
if [ -z "${CLAUDE_BIN_STUB:-}" ]; then
  cv=$("$CLAUDE_BIN" --version 2>/dev/null | cut -d' ' -f1); [ "$cv" = "$PINNED_CLAUDE" ] || die "claude version '$cv' is not the pinned $PINNED_CLAUDE"
fi
# ── 2. extract /testbed; assert the image's history is the post-fix shape BEFORE dropping it (refuter L3) ──
"$DOCKER_BIN" rm -f "x-$ep" >/dev/null 2>&1
"$DOCKER_BIN" create --platform linux/amd64 --name "x-$ep" "$IMG@$DIG" >/dev/null 2>&1 || die "docker create failed"
"$DOCKER_BIN" cp "x-$ep:/testbed" "$ST/extract/" >/dev/null 2>&1 || die "docker cp /testbed failed"
"$DOCKER_BIN" rm -f "x-$ep" >/dev/null 2>&1
[ -d "$ST/extract/testbed/.git" ] || die "image /testbed carries no .git: the checkout-is-base assertion cannot run"
G="git --git-dir=$ST/extract/testbed/.git"
p1=$($G rev-parse HEAD~1 2>/dev/null); bt=$($G show -s --format=%ci "$BASE" 2>/dev/null)
nafter=$($G log --all --format=%H --since="$bt" 2>/dev/null | grep -v "^$($G rev-parse HEAD 2>/dev/null)$" | grep -vc "^$BASE$"); nafter=${nafter:-0}
ntags=$($G tag 2>/dev/null | wc -l | tr -d ' ')
printf 'HEAD~1=%s base=%s commits_at_or_after_base_excl_base_and_HEAD=%s tags=%s\n' "$p1" "$BASE" "$nafter" "$ntags" > "$ST/image_history.txt"
{ [ "$p1" = "$BASE" ] && [ "$nafter" -eq 0 ]; } || die "image history is not the post-fix shape: $(cat "$ST/image_history.txt")"
find "$ST/extract/testbed" -name .git -prune -exec rm -rf {} + 2>/dev/null
find "$ST/extract/testbed" -name packed-refs -exec rm -f {} + 2>/dev/null
for f in CLAUDE.md CLAUDE.local.md .claude .mcp.json; do [ -e "$ST/extract/testbed/$f" ] && die "image tree carries $f (would be loaded by the agent)"; done
mv "$ST/extract/testbed" "$EP/repo" || die "mv repo"
rmdir "$ST/extract" 2>/dev/null
# ── 3. CHECK 2b on the host copy (+ RepoDigests) ────────────────────────────────────────────────
bash "$H/check2b.sh" "$EP/repo" "$DIG" "$IMG" > "$ST/check2b.host.log" 2>&1 || { cat "$ST/check2b.host.log"; die "CHECK2B host FAIL"; }
# ── 4. shadow git (outside the agent's tree; GIT_DIR only in this process) ──────────────────────
SG="$ST/shadow.git"
git --git-dir="$SG" --work-tree="$EP/repo" init -q || die "shadow init"
git --git-dir="$SG" -c user.name=harness -c user.email=harness@bench --work-tree="$EP/repo" add -A || die "shadow add"
git --git-dir="$SG" -c user.name=harness -c user.email=harness@bench --work-tree="$EP/repo" commit -q -m base || die "shadow commit"
git --git-dir="$SG" tag base >/dev/null 2>&1
bash "$H/check2b.sh" "$EP/repo" >/dev/null 2>&1 || die "CHECK2B host FAIL after shadow init (object store reachable)"
# ── 5. prompt + arm file + wrapper; the episode dir holds EXACTLY CLAUDE.md repo rt ─────────────
ARM_FOR_BUILD="$arm" python3 "$H/build_prompt.py" --instance "$IID" --ep "$EP" --out "$ST" --data "$H/data/problem_statements.json" > /dev/null || die "build_prompt"
if [ -n "$PROMPT_OVERRIDE" ]; then printf '%s\n' "$PROMPT_OVERRIDE" > "$ST/prompt.md"; cp "$ST/prompt.md" "$ST/prompt_override.txt"; fi
sed -e "s|__ST__|$ST|g" -e "s|__CTR__|$CTR|g" -e "s|__DOCKER__|$DOCKER_BIN|g" "$H/rt.template" > "$EP/rt" && chmod +x "$EP/rt"
[ "$(ls -A "$EP" | sort | tr '\n' ' ')" = "CLAUDE.md repo rt " ] || die "episode dir holds more than CLAUDE.md repo rt: $(ls -A "$EP")"
[ "$(ls -A "$EPROOT" | tr '\n' ' ')" = "$ep " ] || die "EPROOT holds more than this episode: $(ls -A "$EPROOT")"
# ── 6. hermeticity assertions ───────────────────────────────────────────────────────────────────
p="$EP"; while [ "$p" != "/" ]; do p=$(dirname "$p"); [ -e "$p/CLAUDE.md" ] && die "CLAUDE.md above the episode at $p"; done
[ -e "$CFG/CLAUDE.md" ] && die "CLAUDE.md in the config dir"
[ -z "$(ls -A "$CFG/projects" 2>/dev/null)" ] || die "config dir projects/ is not empty before the episode: $(ls -A "$CFG/projects")"
for d in file-history session-env sessions todos shell-snapshots debug; do [ -z "$(ls -A "$CFG/$d" 2>/dev/null)" ] || die "config dir $d/ is not empty before the episode"; done
# agent-influencing entries are refused outright; anything else unknown is recorded, not fatal (refuter T-F3)
for f in CLAUDE.md commands agents skills rules hooks .mcp.json; do [ -e "$CFG/$f" ] && die "config dir carries agent-influencing entry $f"; done
ls -A "$CFG" | grep -Ev '^(\.claude\.json|\.claude\.json\.bak[^ ]*|settings\.json|projects|sessions|backups|cache|plugins|history\.jsonl|shell-snapshots|todos|debug|statsig|file-history|\.last-[^ ]*|session-env)$' > "$ST/configdir_unexpected.txt" || true
want_s=$(grep '^settings.json ' "$H/HASHES.txt" | cut -d' ' -f2); have_s=$(shasum -a 256 "$CFG/settings.json" | cut -d' ' -f1)
[ "$want_s" = "$have_s" ] || die "settings.json sha $have_s != pinned $want_s"
want_h=$(grep '^hook-deny-network.sh ' "$H/HASHES.txt" | cut -d' ' -f2); have_h=$(shasum -a 256 "$H/hook-deny-network.sh" | cut -d' ' -f1)
[ "$want_h" = "$have_h" ] || die "hook sha $have_h != pinned $want_h"
want_a=$(grep -F "rendered-$arm(__EP__) " "$H/HASHES.txt" | cut -d' ' -f2); have_a=$(cat "$H/base.md" "$H/arms/$arm.md" | shasum -a 256 | cut -d' ' -f1)
[ -n "$want_a" ] && [ "$want_a" = "$have_a" ] || die "arm rendering sha $have_a != pinned '$want_a'"
[ "$(sed "s|$EP|__EP__|g" "$EP/CLAUDE.md" | shasum -a 256 | cut -d' ' -f1)" = "$have_a" ] || die "episode CLAUDE.md is not the pinned rendering with the path substituted"
want_p=$(grep -F "prompt-canonical $IID " "$H/HASHES.txt" | cut -d' ' -f3); have_p=$(python3 -c "import json;print(json.load(open('$ST/prompt_meta.json'))['prompt_sha256_canonical'])")
[ -n "$want_p" ] && [ "$want_p" = "$have_p" ] || die "canonical prompt sha $have_p != pinned '$want_p' for $IID"
# ── 7. container: pinned image, NO network, the working copy mounted over /testbed ───────────────
"$DOCKER_BIN" run -d --platform linux/amd64 --network none --name "$CTR" -v "$EP/repo:/testbed" -w /testbed "$IMG@$DIG" tail -f /dev/null >/dev/null 2>&1 || die "docker run"
"$DOCKER_BIN" exec -i "$CTR" bash -s -- /testbed < "$H/check2b.sh" > "$ST/check2b.container.log" 2>&1 || { cat "$ST/check2b.container.log"; die "CHECK2B container FAIL"; }
# the wrapper must work under the AGENT's exact environment (refuter F3/L6); its log line is the probe's, not the agent's
( cd "$EP/repo" && env -i HOME="$REAL_HOME" USER="$USER" LOGNAME="$USER" PATH="$AGENT_PATH" TERM=dumb LANG=en_US.UTF-8 "$EP/rt" 'python -c "import sys; print(sys.version.split()[0])"' ) > "$ST/env_python.txt" 2>&1 || { cat "$ST/env_python.txt"; die "rt wrapper fails under the agent environment"; }
mv "$ST/rt.log" "$ST/rt.probe.log" 2>/dev/null
log "PREPARED repo=$(du -sh "$EP/repo" | cut -f1) python=$(tail -1 "$ST/env_python.txt") check2b=host+container PASS history=$(cut -c1-90 "$ST/image_history.txt")"
[ "$DRY" = "--dry" ] && { term="DRY"; finish 0; }
# ── 8. run claude, watched; $! IS claude (exec), so the watchdog kills the agent, not a shell ─────
SID=$(uuidgen | tr 'A-Z' 'a-z')
( cd "$EP/repo" && exec env -i HOME="$REAL_HOME" USER="$USER" LOGNAME="$USER" PATH="$AGENT_PATH" TERM=dumb LANG=en_US.UTF-8 \
    TMPDIR="${TMPDIR:-/tmp}" CLAUDE_CONFIG_DIR="$CFG" BENCH_EP="$EP" \
    DISABLE_AUTOUPDATER=1 DISABLE_UPDATES=1 CLAUDE_CODE_DISABLE_FILE_CHECKPOINTING=1 \
    "$CLAUDE_BIN" -p "$(cat "$ST/prompt.md")" --model "$MODEL" --effort "$EFFORT" --max-turns "$MAX_TURNS" \
      --dangerously-skip-permissions \
      --disallowedTools "WebFetch,WebSearch,Agent,Task,Workflow,Skill,Monitor,CronCreate,CronDelete,CronList,RemoteTrigger,SendMessage,ListAgents,PushNotification,SendUserFile,EnterWorktree,ExitWorktree" \
      --strict-mcp-config --setting-sources user,project --output-format json --session-id "$SID" > "$ST/result.json" 2> "$ST/claude.stderr" ) &
CPID=$!
log "CLAUDE started pid=$CPID session=$SID"
while kill -0 "$CPID" 2>/dev/null; do
  sleep 20
  el=$(( $(now) - t0 ))
  [ -z "$JSONL" ] && JSONL=$(find "$CFG/projects" -name "$SID.jsonl" 2>/dev/null | head -1)
  [ "$el" -gt "$WALL_S" ] && killed="WALLCLOCK"
  if [ -n "$JSONL" ] && [ -z "$killed" ]; then
    ms=$(python3 "$H/meter.py" "$JSONL" --live 2>/dev/null | python3 -c "import json,sys; print(json.load(sys.stdin)['metered_sum'])" 2>/dev/null || echo 0)
    [ "${ms:-0}" -ge "$TOKEN_CEILING" ] && killed="TOKEN_CEILING"
  fi
  if [ -n "$killed" ]; then
    log "WATCHDOG $killed at ${el}s"; kill -TERM "$CPID" 2>/dev/null; sleep 10; kill -KILL "$CPID" 2>/dev/null; break
  fi
done
wait "$CPID"; crc=$?
sleep 2
if pgrep -f -- "--session-id $SID" >/dev/null 2>&1; then pkill -KILL -f -- "--session-id $SID"; log "ORPHAN_KILLED: a process still held $SID after wait"; fi
[ -z "$JSONL" ] && JSONL=$(find "$CFG/projects" -name "$SID.jsonl" 2>/dev/null | head -1)
# ── 9. termination, patch, meter, audit, archive ────────────────────────────────────────────────
# classify from the CLI's MESSAGE TEXT and stderr only — never from numeric fields (refuter RI-5)
python3 - "$ST" > "$ST/cli_text.txt" 2>/dev/null <<'PY'
import json,sys,os
st=sys.argv[1]
try:
    r=json.load(open(os.path.join(st,"result.json")))
    print(("ERR:" if r.get("is_error") else "")+str(r.get("subtype","")))
    print(str(r.get("result") or "")[:2000].replace("\n"," "))
    print(json.dumps(r.get("error","") or "")[:500])
except Exception:
    print("")
PY
sub=$(head -1 "$ST/cli_text.txt" 2>/dev/null); msgs="$(sed -n 3p "$ST/cli_text.txt" 2>/dev/null) $(cat "$ST/claude.stderr" 2>/dev/null)"
quota_rx='rate.?limit|usage limit|hit your [a-z ]*limit|limit[^a-z]*resets|limit will reset|usage credits|extra usage|spend.?limit|quota|overloaded|billing|too many requests|(^|[^0-9])429([^0-9]|$)'
auth_rx='not logged in|invalid api key|authentication (error|failed)|unlock-keychain|keychain|please run /login|(^|[^a-z])log ?in( |$)|unauthori[sz]ed'
if [ -n "$killed" ]; then term="$killed"
elif [ -z "$JSONL" ]; then
  if printf '%s' "$msgs" | grep -Eqi "$auth_rx"; then term="AUTH"; elif printf '%s' "$msgs" | grep -Eqi "$quota_rx"; then term="QUOTA"; else term="HARNESS_ERROR"; fi
else
  case "$sub" in
    success) term="DONE" ;;
    error_max_turns|ERR:error_max_turns) term="ROUNDS_EXHAUSTED" ;;
    "") term="HARNESS_ERROR" ;;
    *) if printf '%s' "$msgs" | grep -Eqi "$auth_rx"; then term="AUTH"
       elif printf '%s' "$msgs" | grep -Eqi "$quota_rx"; then term="QUOTA"
       else term="ERROR_${sub#ERR:}"; fi ;;
  esac
fi
printf '%s' "$msgs" | grep -Eio "$quota_rx|$auth_rx" | head -3 | tr '\n' ' ' > "$ST/quota_evidence.txt"
git --git-dir="$SG" -c user.name=harness -c user.email=harness@bench --work-tree="$EP/repo" add -A 2>/dev/null
git --git-dir="$SG" --work-tree="$EP/repo" diff --cached --binary base > "$ST/model_patch.diff" 2>/dev/null
[ -s "$ST/model_patch.diff" ] || { term="${term}+NO_PATCH"; : > "$ST/model_patch.diff"; }
if [ -n "$JSONL" ]; then
  cp "$JSONL" "$ST/session.jsonl"
  bash "$H/hook-deny-network.sh" --pattern-escape > "$ST/escape_pattern.txt"; bash "$H/hook-deny-network.sh" --pattern-url > "$ST/url_pattern.txt"
  nj=$(find "$CFG/projects" -name '*.jsonl' | wc -l | tr -d ' '); nsub=$(find "$CFG/projects" -type d -name subagents | wc -l | tr -d ' ')
  extra_j=$(find "$CFG/projects" -name '*.jsonl' ! -name "$SID.jsonl" 2>/dev/null | tr '\n' ' ')
  python3 "$H/meter.py" "$ST/session.jsonl" --result "$ST/result.json" --ep "$EP" --escape-file "$ST/escape_pattern.txt" --url-file "$ST/url_pattern.txt" ${extra_j:+--extra $extra_j} > "$ST/meter.json" 2> "$ST/meter.err"
  [ -s "$ST/meter.json" ] || term="HARNESS_ERROR(meter:$term)"
  python3 -c "import json;m=json.load(open('$ST/meter.json'));print('\n'.join(m['escape_unblocked']+['BLOCKED: '+x for x in m['escape_attempts_blocked']]))" > "$ST/network_audit.txt" 2>/dev/null
  if [ "$nj" != "1" ] || [ "$nsub" != "0" ]; then term="VOID(SUBAGENT:${term})"
  elif python3 -c "import json,sys;sys.exit(0 if json.load(open('$ST/meter.json'))['void'] else 1)" 2>/dev/null; then
    term="VOID($(python3 -c "import json;print(','.join(json.load(open('$ST/meter.json'))['void_reasons']))"):${term})"
  fi
  # a run that landed a jsonl but no metered call is a stall, not a result: QUOTA unless typed otherwise (refuter P2)
  if [ "$(python3 -c "import json;print(json.load(open('$ST/meter.json')).get('calls',0))" 2>/dev/null)" = "0" ]; then case "$term" in AUTH*|QUOTA*|HARNESS*|VOID*) ;; *) term="QUOTA(no_call:$term)" ;; esac; fi
fi
# the config dir carries nothing across episodes but credentials: archive its projects/ subtree, then remove it — UNCONDITIONALLY
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
# an episode whose every agent rt call failed could not test in either arm: plumbing, not the agent (refuter L6; rc!=0 of
# a legitimately failing test is NOT plumbing, so the rule keys on rc=127/126 — command not found / not executable)
rtc=$(grep -c $'\tEND\t' "$ST/rt.log" 2>/dev/null); rtc=${rtc:-0}
rt127=$(grep -Ec $'\trc=12[67]\t' "$ST/rt.log" 2>/dev/null); rt127=${rt127:-0}
[ "$rtc" -gt 0 ] && [ "$rt127" -eq "$rtc" ] && term="HARNESS_ERROR(rt_all_failed:${term})"
finish "$crc"
