#!/bin/bash
# episode.sh — ONE hermetic episode: prepare · assert · run claude · extract patch · meter · archive.
#   usage: ARM=<a0|a1|s0|...> episode.sh <instance_id> [--dry]
#   env:   ARM (REQUIRED, env not argv — never in the process table) · BENCH (~/bench: harness/state/logs)
#          EPROOT (~/work: the ONLY tree the agent is meant to see) · H · CFG (~/.claude-bench)
#          MODEL · EFFORT · MAX_TURNS (40) · WALL_S (5400) · TOKEN_CEILING (8000000 = R x 200k per-call sub-cap,
#          so --max-turns is the binding stop) · PROMPT_OVERRIDE (smoke probe only) · LANDINGS (landings.log|dry.log)
# Runs on the Studio under bash 3.2. Prints EPISODE <ep> first, LANDED <ep> ... last; writes <STATE>/<ep>/manifest.json.
# ⛔ ARM-BLINDNESS IS BY AUDIT, NOT BY CONSTRUCTION (refuter F1): the agent runs as the same uid with a docker
#    socket in reach, so nothing on this host is unreadable to it. What this script guarantees: the arm name is
#    in no file, no argv and no env while claude runs (manifest is written AFTER exit); the agent-visible tree
#    <EPROOT> holds ONLY this episode; every tool call is audited post hoc (meter.py) and an escape VOIDs.
set -u
IID="${1:?instance_id}"; DRY="${2:-}"
arm="${ARM:?ARM must be set in the environment}"; unset ARM
BENCH="${BENCH:-$HOME/bench}"; H="${H:-$BENCH/harness}"; CFG="${CFG:-$HOME/.claude-bench}"; EPROOT="${EPROOT:-$HOME/work}"
MODEL="${MODEL:-claude-sonnet-5}"; EFFORT="${EFFORT:-high}"; MAX_TURNS="${MAX_TURNS:-40}"
WALL_S="${WALL_S:-5400}"; TOKEN_CEILING="${TOKEN_CEILING:-8000000}"; LANDINGS="${LANDINGS:-landings.log}"
REAL_HOME="$HOME"
ep="ep-$(head -c 4 /dev/urandom | od -An -tx1 | tr -d ' \n')"
EP="$EPROOT/$ep"; ST="$BENCH/state/$ep"; CTR="$ep"
mkdir -p "$EP" "$ST/extract" "$BENCH/logs" "$EPROOT"
log() { printf '%s %s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$*" | tee -a "$ST/episode.log"; }
now() { date -u +%s; }
term="UNSET"; t0=$(now); crc=""; SID=""; JSONL=""; killed=""
CLAUDE_BIN=$(command -v claude); DOCKER_BIN=$(command -v docker)
# the agent's PATH: the Studio's login PATH (measured by the smoke probe from inside the agent), stated not assumed
AGENT_PATH="${AGENT_PATH:-/usr/local/bin:/opt/homebrew/bin:/usr/bin:/bin:/usr/sbin:/sbin:$REAL_HOME/.local/bin}"
die() { log "HARNESS_ERROR $*"; term="HARNESS_ERROR"; finish 1; }
printf 'EPISODE %s\n' "$ep"

# ── metadata: ONLY the projection file (problem_statement, base_commit, repo, version) is on this host
#    during episodes; the full dataset (patch, test_patch, hints, F2P/P2P) is here only for control/scoring phases
[ -e "$H/data/verified.json" ] && { echo "REFUSE: the full dataset is present at $H/data/verified.json during an episode (studio_phase.sh out first)"; exit 3; }
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
  rc="${1:-0}"
  "$DOCKER_BIN" rm -f "$CTR" >/dev/null 2>&1
  # the agent-visible tree is archived (evidence), never left for the next episode to read (refuter L4)
  [ -d "$EP" ] && mv "$EP" "$ST/eptree" 2>/dev/null
  t1=$(now)
  ARMV="$arm" python3 - "$ST" "$IID" "$IMG" "$DIG" "$BASE" "$term" "$rc" "$t0" "$t1" "$MODEL" "$EFFORT" "$MAX_TURNS" "$WALL_S" "$TOKEN_CEILING" "$H" "$CFG" "$CLAUDE_BIN" "$ep" "${SID:-}" "$AGENT_PATH" <<'PY'
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
rt_calls=rt_ok=0
try:
    for l in open(os.path.join(st,"rt.log")):
        if "\tEND\t" in l:
            rt_calls+=1; rt_ok+= ("\trc=0\t" in l)
except Exception: pass
armfile=os.path.join(h,"arms",arm+".md")
m={"episode":ep,"instance_id":iid,"arm":arm,"image":img,"digest":dig,"base_commit":base,
   "termination":term,"claude_exit_code":int(rc),"start_utc":int(t0),"end_utc":int(t1),"wall_s":int(t1)-int(t0),
   "model_requested":model,"effort":effort,"max_turns":int(mt),"wall_ceiling_s":int(wall),"token_ceiling":int(ceil),
   "session_id":sid,"claude_bin":cbin,"claude_version":ver(),"host_arch":os.uname().machine,"docker_platform":"linux/amd64",
   "agent_path":apath,"autocompact":"default (auto), not pinned",
   "arm_rendering_sha256":hashlib.sha256(open(os.path.join(h,"base.md"),"rb").read()+open(armfile,"rb").read()).hexdigest(),
   "arm_block_bytes":os.path.getsize(armfile),"claude_md_sha256":sha(os.path.join(st,"eptree","CLAUDE.md")),
   "prompt_sha256":pm.get("prompt_sha256"),"prompt_sha256_canonical":pm.get("prompt_sha256_canonical"),
   "problem_statement_sha256":pm.get("problem_statement_sha256"),
   "settings_sha256":sha(os.path.join(cfg,"settings.json")),"hook_sha256":sha(os.path.join(h,"hook-deny-network.sh")),
   "model_patch_sha256":sha(os.path.join(st,"model_patch.diff")),
   "model_patch_bytes":(os.path.getsize(os.path.join(st,"model_patch.diff")) if os.path.exists(os.path.join(st,"model_patch.diff")) else None),
   "agent_made_git":os.path.exists(os.path.join(st,"eptree","repo",".git")),
   "rt_calls":rt_calls,"rt_calls_rc0":rt_ok,
   "metered_sum":mt_.get("metered_sum"),"metered_sum_governing":(mt_.get("crosscheck") or {}).get("metered_sum_governing"),
   "calls":mt_.get("calls"),"void_reasons":mt_.get("void_reasons"),"compactions":mt_.get("compactions"),
   "flags":["-p <prompt>","--model",model,"--effort",effort,"--max-turns",mt,"--dangerously-skip-permissions",
            "--disallowedTools","WebFetch,WebSearch,Agent,Task,Workflow,Skill","--strict-mcp-config",
            "--setting-sources","user,project","--output-format","json","--session-id <uuid>"]}
json.dump(m,open(os.path.join(st,"manifest.json"),"w"),indent=1,sort_keys=True)
PY
  log "LANDED $ep task=$IID arm=$arm term=$term rc=$rc wall=$(( $(now)-t0 ))s metered=$(python3 -c "import json;print(json.load(open('$ST/manifest.json'))['metered_sum'])" 2>/dev/null)"
  printf '%s %s %s %s\n' "$ep" "$IID" "$arm" "$term" >> "$BENCH/logs/$LANDINGS"
  exit "$rc"
}

# ── 1. image present and IS the pinned digest ───────────────────────────────────────────────────
"$DOCKER_BIN" image inspect "$IMG@$DIG" >/dev/null 2>&1 || die "image $IMG@$DIG not present (pull_pilot.sh first)"
# ── 2. extract /testbed from a fresh container of the pinned image; assert the image's history is
#       the post-fix shape BEFORE dropping .git (refuter L3): HEAD~1 == base, no commit after base but HEAD
"$DOCKER_BIN" rm -f "x-$ep" >/dev/null 2>&1
"$DOCKER_BIN" create --platform linux/amd64 --name "x-$ep" "$IMG@$DIG" >/dev/null 2>&1 || die "docker create failed"
"$DOCKER_BIN" cp "x-$ep:/testbed" "$ST/extract/" >/dev/null 2>&1 || die "docker cp /testbed failed"
"$DOCKER_BIN" rm -f "x-$ep" >/dev/null 2>&1
if [ -d "$ST/extract/testbed/.git" ]; then
  G="git --git-dir=$ST/extract/testbed/.git"
  p1=$($G rev-parse HEAD~1 2>/dev/null); bt=$($G show -s --format=%ci "$BASE" 2>/dev/null)
  # commits dated at/after base, EXCLUDING base itself and the synthetic HEAD the image recipe adds atop it
  nafter=$($G log --all --format=%H --since="$bt" 2>/dev/null | grep -v "^$($G rev-parse HEAD 2>/dev/null)$" | grep -vc "^$BASE$")
  ntags=$($G tag 2>/dev/null | wc -l | tr -d ' ')
  printf 'HEAD~1=%s base=%s commits_after_base_excl_HEAD=%s tags=%s\n' "$p1" "$BASE" "$nafter" "$ntags" > "$ST/image_history.txt"
  { [ "$p1" = "$BASE" ] && [ "${nafter:-1}" -eq 0 ]; } || die "image history is not the post-fix shape: $(cat "$ST/image_history.txt")"
else
  echo "no .git in image /testbed" > "$ST/image_history.txt"
fi
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
# ── 5. prompt + arm file + wrapper; the episode dir holds EXACTLY CLAUDE.md rt repo ─────────────
ARM_FOR_BUILD="$arm" python3 "$H/build_prompt.py" --instance "$IID" --ep "$EP" --out "$ST" --data "$H/data/problem_statements.json" > /dev/null || die "build_prompt"
if [ -n "${PROMPT_OVERRIDE:-}" ]; then printf '%s\n' "$PROMPT_OVERRIDE" > "$ST/prompt.md"; fi
sed -e "s|__ST__|$ST|g" -e "s|__CTR__|$CTR|g" -e "s|__DOCKER__|$DOCKER_BIN|g" "$H/rt.template" > "$EP/rt" && chmod +x "$EP/rt"
[ "$(ls -A "$EP" | sort | tr '\n' ' ')" = "CLAUDE.md repo rt " ] || die "episode dir holds more than CLAUDE.md repo rt: $(ls -A "$EP")"
[ "$(ls -A "$EPROOT" | tr '\n' ' ')" = "$ep " ] || die "EPROOT holds more than this episode: $(ls -A "$EPROOT")"
# ── 6. hermeticity assertions ───────────────────────────────────────────────────────────────────
p="$EP"; while [ "$p" != "/" ]; do p=$(dirname "$p"); [ -e "$p/CLAUDE.md" ] && die "CLAUDE.md above the episode at $p"; done
[ -e "$CFG/CLAUDE.md" ] && die "CLAUDE.md in the config dir"
[ -z "$(ls -A "$CFG/projects" 2>/dev/null)" ] || die "config dir projects/ is not empty before the episode: $(ls -A "$CFG/projects")"
extra=$(ls -A "$CFG" | grep -Ev '^(\.claude\.json|\.claude\.json\.bak[^ ]*|settings\.json|projects|sessions|backups|cache|plugins|history\.jsonl|shell-snapshots|todos|debug|statsig|\.last-[^ ]*|session-env)$' || true)
[ -z "$extra" ] || die "config dir carries unexpected entries: $extra"
want_s=$(grep '^settings.json ' "$H/HASHES.txt" | cut -d' ' -f2); have_s=$(shasum -a 256 "$CFG/settings.json" | cut -d' ' -f1)
[ "$want_s" = "$have_s" ] || die "settings.json sha $have_s != pinned $want_s"
want_h=$(grep '^hook-deny-network.sh ' "$H/HASHES.txt" | cut -d' ' -f2); have_h=$(shasum -a 256 "$H/hook-deny-network.sh" | cut -d' ' -f1)
[ "$want_h" = "$have_h" ] || die "hook sha $have_h != pinned $want_h"
want_a=$(grep -F "rendered-$arm(__EP__) " "$H/HASHES.txt" | cut -d' ' -f2); have_a=$(cat "$H/base.md" "$H/arms/$arm.md" | shasum -a 256 | cut -d' ' -f1)
[ -n "$want_a" ] && [ "$want_a" = "$have_a" ] || die "arm rendering sha $have_a != pinned '$want_a'"
[ "$(sed "s|$EP|__EP__|g" "$EP/CLAUDE.md" | shasum -a 256 | cut -d' ' -f1)" = "$have_a" ] || die "episode CLAUDE.md is not the pinned rendering with the path substituted"
want_p=$(grep -F "prompt-canonical $IID " "$H/HASHES.txt" | cut -d' ' -f3); have_p=$(python3 -c "import json;print(json.load(open('$ST/prompt_meta.json'))['prompt_sha256_canonical'])")
[ -z "${PROMPT_OVERRIDE:-}" ] && { [ -n "$want_p" ] && [ "$want_p" = "$have_p" ] || die "canonical prompt sha $have_p != pinned '$want_p' for $IID"; }
# ── 7. container: pinned image, NO network, the working copy mounted over /testbed ───────────────
"$DOCKER_BIN" run -d --platform linux/amd64 --network none --name "$CTR" -v "$EP/repo:/testbed" -w /testbed "$IMG@$DIG" tail -f /dev/null >/dev/null 2>&1 || die "docker run"
"$DOCKER_BIN" exec -i "$CTR" bash -s -- /testbed < "$H/check2b.sh" > "$ST/check2b.container.log" 2>&1 || { cat "$ST/check2b.container.log"; die "CHECK2B container FAIL"; }
# the wrapper must work under the AGENT's exact environment (refuter F3/L6), asserted before any call
( cd "$EP/repo" && env -i HOME="$REAL_HOME" USER="$USER" LOGNAME="$USER" PATH="$AGENT_PATH" TERM=dumb LANG=en_US.UTF-8 "$EP/rt" 'python -c "import sys; print(sys.version.split()[0])"' ) > "$ST/env_python.txt" 2>&1 || { cat "$ST/env_python.txt"; die "rt wrapper fails under the agent environment"; }
log "PREPARED repo=$(du -sh "$EP/repo" | cut -f1) python=$(tail -1 "$ST/env_python.txt") check2b=host+container PASS history=$(cat "$ST/image_history.txt" | cut -c1-80)"
[ "$DRY" = "--dry" ] && { term="DRY"; finish 0; }
[ -n "$PROMPT_OVERRIDE" ] && [ -n "$(printf '%s' "$MAX_TURNS")" ] || true
# ── 8. run claude, watched; $! IS claude (exec), so the watchdog kills the agent, not a shell ─────
SID=$(uuidgen | tr 'A-Z' 'a-z')
( cd "$EP/repo" && exec env -i HOME="$REAL_HOME" USER="$USER" LOGNAME="$USER" PATH="$AGENT_PATH" TERM=dumb LANG=en_US.UTF-8 \
    TMPDIR="${TMPDIR:-/tmp}" CLAUDE_CONFIG_DIR="$CFG" BENCH_EP="$EP" \
    "$CLAUDE_BIN" -p "$(cat "$ST/prompt.md")" --model "$MODEL" --effort "$EFFORT" --max-turns "$MAX_TURNS" \
      --dangerously-skip-permissions --disallowedTools "WebFetch,WebSearch,Agent,Task,Workflow,Skill" --strict-mcp-config \
      --setting-sources user,project --output-format json --session-id "$SID" > "$ST/result.json" 2> "$ST/claude.stderr" ) &
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
sub=$(python3 -c "import json;r=json.load(open('$ST/result.json'));print(('ERR:' if r.get('is_error') else '')+str(r.get('subtype','')))" 2>/dev/null)
if [ -n "$killed" ]; then term="$killed"
elif [ -z "$JSONL" ]; then term="HARNESS_ERROR"
else
  case "$sub" in
    success) term="DONE" ;;
    error_max_turns|ERR:error_max_turns) term="ROUNDS_EXHAUSTED" ;;
    "") term="HARNESS_ERROR" ;;
    *) if grep -Eqi 'rate.?limit|quota|usage limit|overloaded|429|billing' "$ST/claude.stderr" "$ST/result.json" 2>/dev/null; then term="QUOTA"; else term="ERROR_${sub#ERR:}"; fi ;;
  esac
fi
git --git-dir="$SG" -c user.name=harness -c user.email=harness@bench --work-tree="$EP/repo" add -A 2>/dev/null
git --git-dir="$SG" --work-tree="$EP/repo" diff --cached --binary base > "$ST/model_patch.diff" 2>/dev/null
[ -s "$ST/model_patch.diff" ] || { term="${term}+NO_PATCH"; : > "$ST/model_patch.diff"; }
if [ -n "$JSONL" ]; then
  cp "$JSONL" "$ST/session.jsonl"
  bash "$H/hook-deny-network.sh" --pattern-escape > "$ST/escape_pattern.txt"; bash "$H/hook-deny-network.sh" --pattern-url > "$ST/url_pattern.txt"
  nj=$(find "$CFG/projects" -name '*.jsonl' | wc -l | tr -d ' '); nsub=$(find "$CFG/projects" -type d -name subagents | wc -l | tr -d ' ')
  extra_j=$(find "$CFG/projects" -name '*.jsonl' ! -name "$SID.jsonl" 2>/dev/null | tr '\n' ' ')
  python3 "$H/meter.py" "$ST/session.jsonl" --result "$ST/result.json" --ep "$EP" --escape-file "$ST/escape_pattern.txt" --url-file "$ST/url_pattern.txt" ${extra_j:+--extra $extra_j} > "$ST/meter.json" 2> "$ST/meter.err"
  [ -s "$ST/meter.json" ] || { term="HARNESS_ERROR(meter)"; }
  python3 -c "import json;m=json.load(open('$ST/meter.json'));print('\n'.join(m['escape_unblocked']+['BLOCKED: '+x for x in m['escape_attempts_blocked']]))" > "$ST/network_audit.txt" 2>/dev/null
  if [ "$nj" != "1" ] || [ "$nsub" != "0" ]; then term="VOID(SUBAGENT:${term})"
  elif python3 -c "import json,sys;sys.exit(0 if json.load(open('$ST/meter.json'))['void'] else 1)" 2>/dev/null; then
    term="VOID($(python3 -c "import json;print(','.join(json.load(open('$ST/meter.json'))['void_reasons']))"):${term})"
  fi
fi
# the config dir carries nothing across episodes but credentials: archive its projects/ subtree, then remove it — UNCONDITIONALLY
mkdir -p "$ST/configdir-projects" && cp -R "$CFG/projects/." "$ST/configdir-projects/" 2>/dev/null; rm -rf "$CFG/projects"/* 2>/dev/null
rm -rf "$CFG/todos" "$CFG/shell-snapshots" "$CFG/debug" 2>/dev/null; : > "$CFG/history.jsonl" 2>/dev/null
# an episode whose every rt call failed could not test in either arm: plumbing, not the agent (refuter L6)
rtc=$(grep -c $'\tEND\t' "$ST/rt.log" 2>/dev/null || echo 0); rt0=$(grep -c $'\trc=0\t' "$ST/rt.log" 2>/dev/null || echo 0)
[ "${rtc:-0}" -gt 0 ] && [ "${rt0:-0}" -eq 0 ] && term="HARNESS_ERROR(rt_all_failed:${term})"
finish "$crc"
