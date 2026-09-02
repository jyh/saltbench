#!/bin/bash
# episode_s2rust.sh — ONE hermetic S2-Rust episode: refuse · prepare · assert · run claude · extract · check
# (Verus) · meter · archive. Same discipline as s2lean/episode_s2.sh, on a substrate with no build project:
# the working copy is a single `task.rs` and a pinned wrapper, and the referee is a machine checker, so there
# is no kernel replay and no axiom audit (see check_verus.py's TOMBSTONES).
#
#   usage: printf '%s\n' <arm> | episode_s2rust.sh <task_id> [--dry]
#   env:   BENCH (~/bench) · H ($BENCH/harness) · CFG (~/.claude-bench) · EPROOT (~/work) · VIEWS ($BENCH/s2rviews)
#          VERUS_ROOT LYNETTE_BIN · MODEL EFFORT MAX_TURNS(40) WALL_S(5400) TOKEN_CEILING RT_TIMEOUT(900)
#          PROMPT_OVERRIDE LANDINGS · CLAUDE_BIN + CLAUDE_BIN_STUB=1 (the run-shaped dry)
#
# ⛔⛔ THE ONE STAGE. S2-Lean has A/B/C and a provenance chain between them; S2-Rust has ONE: complete the
# proof. There is no `--a-bodies`, no `A.bodies.json`, no NOT_PROVEN(no_stage_A_pass) — those are S2-Lean
# classes with no successor here, and inventing an empty stage machinery "for symmetry" would be scaffolding
# that only ever reports on itself.
#
# ⛔ THE AGENT FENCE IS RENDERED, NOT PINNED AS A FILE (row CO, built in). `settings.s2.json` names `~/bench`
# statically and does not reach a SIBLING state root; here the fence is rendered from $BENCH by
# render_settings_verus.py and the episode asserts the config dir's settings.json EQUALS that rendering. What
# is pinned is the TEMPLATE. A fence that names a path instead of deriving one stops protecting the day the
# work moves.
#
# ⛔ GROUND TRUTH NEVER REACHES THIS HOST. build_views_verus.py writes `gt/` BESIDE `views/` on the SEAT — 207
# reference bodies — and the view directories themselves carry only task.rs + frozen.json. The episode runs
# gt_leak_check over $BENCH and $VIEWS and REFUSES on any hit, so the split is asserted per episode rather
# than trusted to the transport that made it.
set -u
TASK_ID="${1:?task_id}"; DRY="${2:-}"
read -r arm || true; [ -n "${arm:-}" ] || { echo "REFUSE: the arm must arrive on stdin"; exit 4; }
case "$arm" in a[0-9]|a[0-9][0-9]|s[0-9]) ;; *) echo "REFUSE: bad arm id '$arm'"; exit 4 ;; esac
case "$TASK_ID" in ''|*[!A-Za-z0-9_]*) echo "REFUSE: task_id must be [A-Za-z0-9_]"; exit 4 ;; esac

BENCH="${BENCH:-$HOME/bench}"; H="${H:-$BENCH/harness}"; S2R="$H/s2rust"; CFG="${CFG:-$HOME/.claude-bench}"
EPROOT="${EPROOT:-$HOME/work}"; VIEWS="${VIEWS:-$BENCH/s2rviews}"
VERUS_ROOT="${VERUS_ROOT:-$HOME/verus-pin/verus-arm64-macos}"; LYNETTE_BIN="${LYNETTE_BIN:-$HOME/verus-pin/lynette}"
MODEL="${MODEL:-claude-sonnet-5}"; EFFORT="${EFFORT:-high}"; MAX_TURNS="${MAX_TURNS:-40}"
WALL_S="${WALL_S:-5400}"; TOKEN_CEILING="${TOKEN_CEILING:-8000000}"; RT_TIMEOUT="${RT_TIMEOUT:-900}"
LANDINGS="${LANDINGS:-s2rust-landings.log}"; PROMPT_OVERRIDE="${PROMPT_OVERRIDE:-}"
REAL_HOME="$HOME"; STUB="${CLAUDE_BIN_STUB:-}"
# a stub-driven run can never land where the driver reads, nor seed real state (S2-Lean's refuter RI3-F1/M5)
[ -n "$STUB" ] && LANDINGS="dryexec.log"
ep="ep-$(head -c 4 /dev/urandom | od -An -tx1 | tr -d ' \n')"
EP="$EPROOT/$ep"; ST="$BENCH/state/$ep"
mkdir -p "$EP" "$ST" "$BENCH/logs" "$EPROOT"
log() { printf '%s %s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$*" | tee -a "$ST/episode.log"; }
now() { date -u +%s; }
term="UNSET"; t0=$(now); crc=""; SID=""; JSONL=""; killed=""; finished=""; CPID=""; orphans=0; ARMFILE=""
CLAUDE_BIN="${CLAUDE_BIN:-$(command -v claude)}"
PINNED_CLAUDE=$(grep '^claude-version ' "$H/HASHES.txt" | cut -d' ' -f2)
AGENT_PATH="${AGENT_PATH:-/usr/local/bin:/opt/homebrew/bin:/usr/bin:/bin:/usr/sbin:/sbin:$REAL_HOME/.cargo/bin:$REAL_HOME/.local/bin}"
sha() { shasum -a 256 "$1" 2>/dev/null | cut -d' ' -f1; }
pin2() { grep -F -- "$1 " "$H/HASHES.txt" | grep -E "^$1 " | head -1 | cut -d' ' -f2; }
refuse() { echo "REFUSE: $*"; rm -rf "$EP" "$ST"; exit 3; }
die() { log "HARNESS_ERROR $*"; term="HARNESS_ERROR"; finish 1; }
printf 'EPISODE %s\n' "$ep"

# ── 0. the harness that runs must be the harness that is pinned ─────────────────────────────────────────
self_sha=$(sha "$0"); want_self=$(pin2 s2rust/episode_s2rust.sh)
[ "$self_sha" = "$want_self" ] || { echo "REFUSE: episode_s2rust.sh sha $self_sha is not the pinned $want_self (hashes.sh + sync first)"; rm -rf "$EP" "$ST"; exit 5; }
for f in "$S2R"/*; do
  [ -f "$f" ] || continue; b=$(basename "$f"); case "$b" in *.pyc|HASHES*) continue ;; esac
  want=$(pin2 "s2rust/$b"); [ -n "$want" ] || refuse "s2rust/$b is on the host but not pinned in HASHES.txt"
  [ "$want" = "$(sha "$f")" ] || refuse "s2rust/$b sha drift: host $(sha "$f") pinned $want"
done
want_h=$(pin2 hook-deny-network.sh); [ -n "$want_h" ] && [ "$want_h" = "$(sha "$H/hook-deny-network.sh")" ] || refuse "hook sha drift"
want_m=$(pin2 meter.py); [ -n "$want_m" ] && [ "$want_m" = "$(sha "$H/meter.py")" ] || refuse "meter.py sha drift"
command -v perl >/dev/null 2>&1 || refuse "perl missing (rt bound)"; command -v lsof >/dev/null 2>&1 || refuse "lsof missing (orphan sweep)"

# ⛔ THE AGENT FENCE, ASSERTED AS A RENDERING OF THE PINNED TEMPLATE AT THIS RUN'S ROOT. This is the whole of
# row CO on the agent side: the check is not "is this file the pinned bytes" (it cannot be — it carries $BENCH)
# but "is this file what the pinned template renders to HERE".
python3 "$S2R/render_settings_verus.py" --check "$CFG/settings.json" --bench "$BENCH" > "$ST/settings_check.txt" 2>&1 \
  || { cat "$ST/settings_check.txt"; refuse "$CFG/settings.json is not the pinned fence template rendered at BENCH=$BENCH"; }

# ── 1. THE TOOLCHAIN — identity AND capability, before anything is prepared ──────────────────────────────
HASHES="$H/HASHES.txt" VERUS_ROOT="$VERUS_ROOT" LYNETTE_BIN="$LYNETTE_BIN" \
  bash "$S2R/smoke_toolchain_verus.sh" > "$ST/toolchain.txt" 2>&1 \
  || { cat "$ST/toolchain.txt"; refuse "toolchain gate FAILED (see $ST/toolchain.txt)"; }

# ── 2. THE VIEWS: rebuilt, verified by SET-HASH, and carrying NO ground truth ────────────────────────────
[ -s "$VIEWS/views/$TASK_ID/task.rs" ] || refuse "no task.rs view for $TASK_ID under $VIEWS"
[ -s "$VIEWS/views/$TASK_ID/frozen.json" ] || refuse "no frozen.json for $TASK_ID"
# ⛔ The views are NOT pinned file by file — they are a pure function of the pinned jsonl and the pinned
# builder, so what is pinned is the SET. A per-file pin table for 207 multi-hundred-KB views would be a
# second representation of the same fact, and the two would drift.
want_vs=$(grep '^views-set-sha256 ' "$H/HASHES.txt" | head -1 | cut -d' ' -f2)
have_vs=$(python3 "$S2R/views_sethash.py" "$VIEWS" | cut -d' ' -f1)
[ -n "$want_vs" ] && [ "$want_vs" = "$have_vs" ] || refuse "views set-hash $have_vs != pinned '$want_vs'"
# ⛔ GROUND TRUTH ANYWHERE ON THIS HOST IS A REFUSAL, ASSERTED PER EPISODE. The builder writes `gt/` beside
# `views/` on the SEAT; if a transport ever carries it here, this is what catches it.
python3 "$S2R/gt_leak_check.py" "$VIEWS" > "$ST/gt_fence.txt" 2>&1 || { cat "$ST/gt_fence.txt"; refuse "ground truth under $VIEWS"; }
python3 "$S2R/gt_leak_check.py" "$BENCH/state" > "$ST/gt_fence_state.txt" 2>&1 || { cat "$ST/gt_fence_state.txt"; refuse "ground truth under $BENCH/state"; }
FZ="$VIEWS/views/$TASK_ID/frozen.json"; FROZEN_SHA=$(sha "$FZ")

finish() {
  [ -n "$finished" ] && return 0
  finished=1; rc="${1:-0}"
  [ -f "$EP/repo/.rt.log" ] && [ ! -f "$ST/rt.log" ] && mv "$EP/repo/.rt.log" "$ST/rt.log" 2>/dev/null
  [ -d "$EP" ] && mv "$EP" "$ST/eptree" 2>/dev/null
  [ -n "$PROMPT_OVERRIDE" ] && term="SMOKE($term)"
  [ -n "$STUB" ] && term="DRYEXEC($term)"
  t1=$(now)
  ARMV="$arm" ORPHANS="$orphans" FROZEN_SHA="$FROZEN_SHA" ARMFILE="$ARMFILE" VIEWS="$VIEWS" \
  VERUS_ROOT="$VERUS_ROOT" LYNETTE_BIN="$LYNETTE_BIN" \
  python3 - "$ST" "$TASK_ID" "$term" "$rc" "$t0" "$t1" "$MODEL" "$EFFORT" "$MAX_TURNS" "$WALL_S" "$TOKEN_CEILING" "$H" "$CFG" "$CLAUDE_BIN" "$ep" "${SID:-}" "$AGENT_PATH" <<'PY'
import json,sys,hashlib,os,subprocess
(st,task,term,rc,t0,t1,model,effort,mt,wall,ceil,h,cfg,cbin,ep,sid,apath)=sys.argv[1:]
E=os.environ; arm=E.get("ARMV")
def sha(p):
    try: return hashlib.sha256(open(p,'rb').read()).hexdigest()
    except Exception: return None
def jl(p):
    try: return json.load(open(p))
    except Exception: return {}
pm=jl(os.path.join(st,"prompt_meta.json")); mt_=jl(os.path.join(st,"meter.json")); ck=jl(os.path.join(st,"check.json"))
starts=ends=ok=refused=0
try:
    for l in open(os.path.join(st,"rt.log")):
        if "\tSTART\t" in l: starts+=1
        if "\tREFUSED\t" in l: refused+=1
        if "\tEND\t" in l:
            ends+=1; ok+= ("\trc=0\t" in l)
except Exception: pass
def ver():
    try: return subprocess.check_output([cbin,"--version"]).decode().strip()
    except Exception: return None
# ⛔ The recorded check keys are the ones check_verus actually emits. `fenced` and `profile_sha256` are here
# BECAUSE the fence was once claimed only in a docstring: a scored record must carry whether it was fenced,
# so the claim is auditable from the record rather than from the code that happened to be checked out.
CK=("class","passed","screen_violations","helpers_shape_violations","count_guard","lynette_rc",
    "canonical_bytes","rlimit","seed","referee","profile_sha256","_present")
m={"episode":ep,"substrate":"S2-Rust/VeruSAGE","task_id":task,"stage":"P","arm":arm,
   "termination":term,"claude_exit_code":int(rc),"start_utc":int(t0),"end_utc":int(t1),"wall_s":int(t1)-int(t0),
   "model_requested":model,"effort":effort,"max_turns":int(mt),"wall_ceiling_s":int(wall),"token_ceiling":int(ceil),
   "session_id":sid,"claude_bin":cbin,"claude_version":ver(),"host_arch":os.uname().machine,
   "agent_path":apath,"orphans_killed":int(E.get("ORPHANS","0")),
   "frozen_sha256":E.get("FROZEN_SHA"),"arm_file":E.get("ARMFILE"),
   "settings_sha256":sha(os.path.join(cfg,"settings.json")),
   "hook_sha256":sha(os.path.join(h,"hook-deny-network.sh")),
   "episode_sh_sha256":sha(os.path.join(h,"s2rust","episode_s2rust.sh")),
   "checker_sha256":sha(os.path.join(h,"s2rust","check_verus.py")),
   "screen_sha256":sha(os.path.join(h,"s2rust","screen_verus.py")),
   "profile_template_sha256":sha(os.path.join(h,"s2rust","sandbox_verus.sb")),
   "verus_sha256":sha(os.path.join(E["VERUS_ROOT"],"verus")),
   "z3_sha256":sha(os.path.join(E["VERUS_ROOT"],"z3")),
   "lynette_sha256":sha(E["LYNETTE_BIN"]),
   "rt_calls":starts,"rt_ends":ends,"rt_calls_rc0":ok,"rt_refused":refused,
   "prompt_sha256":pm.get("prompt_sha256"),"prompt_sha256_canonical":pm.get("prompt_sha256_canonical"),
   "view_sha256":pm.get("view_sha256"),
   "metered_sum":mt_.get("metered_sum"),"metered_classes":mt_.get("classes"),"calls":mt_.get("calls")}
for k in CK: m["check_"+k]=ck.get(k)
json.dump(m,open(os.path.join(st,"manifest.json"),"w"),indent=1)
print("LANDED %s %s %s %s %s %s" % (ep, task, arm, term, ck.get("class") or "NO_CHECK", mt_.get("metered_sum") or 0))
PY
  tail -1 "$ST/manifest.json" >/dev/null 2>&1
  line=$(python3 -c "
import json;m=json.load(open('$ST/manifest.json'))
print('%s %s %s %s %s %s' % (m['episode'],m['task_id'],m['arm'],m['termination'],m.get('check_class') or 'NO_CHECK',m.get('metered_sum') or 0))" 2>/dev/null)
  [ -n "$line" ] && printf '%s\n' "$line" | tee -a "$BENCH/logs/$LANDINGS"
  exit "$rc"
}
trap 'die "signal"' INT TERM
killgroup() { [ -n "$CPID" ] && { kill -TERM -- "-$CPID" 2>/dev/null; sleep "${1:-10}"; kill -KILL -- "-$CPID" 2>/dev/null; }; }

[ -n "$CLAUDE_BIN" ] || die "claude not found"
if [ -z "$STUB" ]; then cv=$("$CLAUDE_BIN" --version 2>/dev/null | cut -d' ' -f1); [ "$cv" = "$PINNED_CLAUDE" ] || die "claude version '$cv' is not the pinned $PINNED_CLAUDE"; fi

# ── 3. the working copy: ONE file. No project, no build, no symlink into a shared tree. ──────────────────
mkdir -p "$EP/repo" && cp "$VIEWS/views/$TASK_ID/task.rs" "$EP/repo/task.rs" || die "view copy"

# ── 4. prompt + arm file + wrapper ──────────────────────────────────────────────────────────────────────
ARMFILE="$H/arms/$arm.md"; [ "$arm" = "a1" ] && [ -f "$H/s2lean/placebo.md" ] && ARMFILE="$H/s2lean/placebo.md"
TARGET=$(python3 -c "import json;print(json.load(open('$FZ')).get('target_name') or json.load(open('$FZ')).get('task_id') or '$TASK_ID')" 2>/dev/null || echo "$TASK_ID")
ARMFILE="$ARMFILE" TARGET="$TARGET" python3 - "$EP" "$ST" "$S2R" "$arm" <<'PY' || die "prompt/arm build"
import json,sys,hashlib,os
ep,st,s2r,arm=sys.argv[1:]
tmpl=open(os.path.join(s2r,"prompt_P.md")).read()
prompt=tmpl.replace("__EP__",ep).replace("__TARGET__",os.environ["TARGET"])
# ⛔ the CANONICAL form keeps __EP__ AND __TARGET__ unsubstituted: the per-task text differs by design, so the
# canonical sha proves two ARMS got the same prompt shape, which is the comparison the campaign actually makes.
canon=tmpl
base=open(os.path.join(s2r,"base.md")).read().replace("__EP__",ep); armb=open(os.environ["ARMFILE"]).read()
open(os.path.join(st,"prompt.md"),"w").write(prompt); open(os.path.join(ep,"CLAUDE.md"),"w").write(base+armb)
view=open(os.path.join(ep,"repo","task.rs"),"rb").read()
json.dump({"stage":"P","prompt_sha256":hashlib.sha256(prompt.encode()).hexdigest(),
           "prompt_sha256_canonical":hashlib.sha256(canon.encode()).hexdigest(),
           "view_sha256":hashlib.sha256(view).hexdigest()},
          open(os.path.join(st,"prompt_meta.json"),"w"),indent=1)
PY
[ -n "$PROMPT_OVERRIDE" ] && { printf '%s\n' "$PROMPT_OVERRIDE" > "$ST/prompt.md"; cp "$ST/prompt.md" "$ST/prompt_override.txt"; }
RLIMIT=$(pin2 verus-rlimit); SEED=$(pin2 verus-seed)
[ -n "$RLIMIT" ] && [ -n "$SEED" ] || die "verus-rlimit/verus-seed not pinned"
sed -e "s|__EP__|$EP|g" -e "s|__VERUS__|$VERUS_ROOT/verus|g" -e "s|__RLIMIT__|$RLIMIT|g" \
    -e "s|__SEED__|$SEED|g" -e "s|__RT_TIMEOUT__|$RT_TIMEOUT|g" "$S2R/rt.template" > "$EP/rt" && chmod +x "$EP/rt"
grep -q '__EP__\|__VERUS__\|__RLIMIT__\|__SEED__\|__RT_TIMEOUT__' "$EP/rt" && die "rt template not fully rendered"
[ "$(ls -A "$EP" | sort | tr '\n' ' ')" = "CLAUDE.md repo rt " ] || die "episode dir holds more than CLAUDE.md repo rt: $(ls -A "$EP")"
[ "$(ls -A "$EPROOT" | tr '\n' ' ')" = "$ep " ] || die "EPROOT holds more than this episode: $(ls -A "$EPROOT")"

# ── 5. hermeticity assertions ───────────────────────────────────────────────────────────────────────────
p="$EP"; while [ "$p" != "/" ]; do p=$(dirname "$p"); [ -e "$p/CLAUDE.md" ] && die "CLAUDE.md above the episode at $p"; done
[ -e "$CFG/CLAUDE.md" ] && die "CLAUDE.md in the config dir"
[ -z "$(ls -A "$CFG/projects" 2>/dev/null)" ] || die "config dir projects/ is not empty before the episode"
for d in file-history session-env sessions todos shell-snapshots debug; do [ -z "$(ls -A "$CFG/$d" 2>/dev/null)" ] || die "config dir $d/ is not empty before the episode"; done
for f in CLAUDE.md commands agents skills rules hooks .mcp.json; do [ -e "$CFG/$f" ] && die "config dir carries agent-influencing entry $f"; done
want_a=$(grep -F "rendered-s2rust-$arm(__EP__) " "$H/HASHES.txt" | cut -d' ' -f2)
have_a=$(cat "$S2R/base.md" "$ARMFILE" | shasum -a 256 | cut -d' ' -f1)
[ -n "$want_a" ] && [ "$want_a" = "$have_a" ] || die "arm rendering sha $have_a != pinned '$want_a'"
[ "$(sed "s|$EP|__EP__|g" "$EP/CLAUDE.md" | shasum -a 256 | cut -d' ' -f1)" = "$have_a" ] || die "episode CLAUDE.md is not the pinned rendering"

# ── 6. the wrapper under the agent's EXACT environment, before the model is paid for ─────────────────────
# ⛔ The probe runs the REAL referee on the REAL task file. A wrapper that only works in the harness's own
# environment fails on the agent's first call, after the spend has started.
( cd "$EP/repo" && env -i HOME="$REAL_HOME" USER="$USER" LOGNAME="$USER" PATH="$AGENT_PATH" TERM=dumb LANG=en_US.UTF-8 "$EP/rt" verus task.rs ) > "$ST/env_probe.txt" 2>&1
pr=$?; printf 'rt_probe_rc=%s\n' "$pr" >> "$ST/env_probe.txt"
# the UNSOLVED view is expected to FAIL verification (its proof body is empty) — what must work is the
# WRAPPER: a front-end refusal (no results line) or an exec failure is a harness fault, a VERIFY_FAIL is not.
grep -q 'verification results::' "$ST/env_probe.txt" || { cat "$ST/env_probe.txt"; die "rt wrapper produced no results line under the agent environment"; }
( cd "$EP/repo" && env -i HOME="$REAL_HOME" USER="$USER" PATH="$AGENT_PATH" "$EP/rt" bogus args ) >/dev/null 2>&1; [ "$?" = 64 ] || die "rt wrapper does not REFUSE a non-pinned command line"
mv "$EP/repo/.rt.log" "$ST/rt.probe.log" 2>/dev/null
log "PREPARED task=$TASK_ID arm=$arm verus=$(basename "$VERUS_ROOT") rlimit=$RLIMIT seed=$SEED probe_rc=$pr"
[ "$DRY" = "--dry" ] && { term="DRY"; finish 0; }

# ── 7. run claude in ITS OWN PROCESS GROUP, watched ─────────────────────────────────────────────────────
SID=$(uuidgen | tr 'A-Z' 'a-z')
( cd "$EP/repo" && exec /usr/bin/perl -e 'setpgrp(0,0); exec @ARGV; exit 127' env -i HOME="$REAL_HOME" USER="$USER" LOGNAME="$USER" PATH="$AGENT_PATH" TERM=dumb LANG=en_US.UTF-8 \
    TMPDIR="${TMPDIR:-/tmp}" CLAUDE_CONFIG_DIR="$CFG" BENCH_EP="$EP" DISABLE_AUTOUPDATER=1 DISABLE_UPDATES=1 CLAUDE_CODE_DISABLE_FILE_CHECKPOINTING=1 \
    "$CLAUDE_BIN" -p "$(cat "$ST/prompt.md")" --model "$MODEL" --effort "$EFFORT" --max-turns "$MAX_TURNS" --dangerously-skip-permissions \
      --disallowedTools "WebFetch,WebSearch,Agent,Task,Workflow,Skill,Monitor,CronCreate,CronDelete,CronList,RemoteTrigger,SendMessage,ListAgents,PushNotification,SendUserFile,EnterWorktree,ExitWorktree" \
      --strict-mcp-config --setting-sources user,project --output-format json --session-id "$SID" > "$ST/result.json" 2> "$ST/claude.stderr" ) &
CPID=$!; log "CLAUDE started pid=$CPID pgid=$CPID session=$SID"
while kill -0 "$CPID" 2>/dev/null; do
  sleep 20; el=$(( $(now) - t0 ))
  [ -z "$JSONL" ] && JSONL=$(find "$CFG/projects" -name "$SID.jsonl" 2>/dev/null | head -1)
  [ "$el" -gt "$WALL_S" ] && killed="WALLCLOCK"
  if [ -n "$JSONL" ] && [ -z "$killed" ]; then
    ms=$(python3 "$H/meter.py" "$JSONL" --live 2>/dev/null | python3 -c "import json,sys; print(json.load(sys.stdin)['metered_sum'])" 2>/dev/null || echo 0)
    [ "${ms:-0}" -ge "$TOKEN_CEILING" ] && killed="TOKEN_CEILING"
  fi
  if [ -n "$killed" ]; then log "WATCHDOG $killed at ${el}s"; killgroup 10; break; fi
done
wait "$CPID"; crc=$?; sleep 2
if pgrep -f -- "--session-id $SID" >/dev/null 2>&1; then pkill -KILL -f -- "--session-id $SID"; orphans=$((orphans+1)); log "ORPHAN_KILLED claude still held $SID after wait"; fi
kill -KILL -- "-$CPID" 2>/dev/null
# ⛔ nothing may keep running under the episode dir — verus and z3 are FORKED children of the rt wrapper, so
# a tool-level kill that misses them leaves a solver burning the Studio's CPU into the next episode.
for op in $(lsof -a -d cwd -u "$USER" -Fpn 2>/dev/null | awk -v ep="$EP" '/^p/{p=substr($0,2)} /^n/{if (index(substr($0,2), ep)==1) print p}'); do
  [ "$op" = "$$" ] && continue; cn=$(ps -o comm= -p "$op" 2>/dev/null); kill -KILL "$op" 2>/dev/null && { orphans=$((orphans+1)); log "ORPHAN_KILLED pid=$op comm=$cn cwd under $EP"; }
done
[ -f "$EP/repo/.rt.log" ] && mv "$EP/repo/.rt.log" "$ST/rt.log"
[ -z "$JSONL" ] && JSONL=$(find "$CFG/projects" -name "$SID.jsonl" 2>/dev/null | head -1)

# ── 8. termination ──────────────────────────────────────────────────────────────────────────────────────
python3 - "$ST" > "$ST/cli_text.txt" 2>/dev/null <<'PY'
import json,sys,os
st=sys.argv[1]
try:
    r=json.load(open(os.path.join(st,"result.json"))); print(("ERR:" if r.get("is_error") else "")+str(r.get("subtype","")))
    print(str(r.get("result") or "")[:2000].replace("\n"," "))
    errs=r.get("errors") or []; errs=errs if isinstance(errs,list) else [errs]
    print((" ".join(str(x) for x in errs)+" "+str(r.get("error") or "")).replace("\n"," ")[:800])
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

# ── 9. THE CHECK. ⚠️ read off the file the AGENT wrote (amendment 14's law) ──────────────────────────────
cp "$EP/repo/task.rs" "$ST/agent_task.rs" 2>/dev/null
python3 "$S2R/extract_verus.py" "$EP/repo/task.rs" > "$ST/bodies.json" 2>"$ST/extract.err" || { : > "$ST/bodies.json"; term="${term}+NO_BODIES"; }
BENCH="$BENCH" python3 "$S2R/check_verus.py" --frozen "$FZ" --agent-file "$EP/repo/task.rs" \
   --verus "$VERUS_ROOT/verus" --lynette "$LYNETTE_BIN" --rlimit "$RLIMIT" --seed "$SEED" \
   --out "$ST/check.json" > "$ST/check.stdout" 2> "$ST/check.stderr"
ccrc=$?; [ "$ccrc" = 2 ] && log "CHECK HARNESS rc=$ccrc (see check.stderr)"
python3 "$H/meter.py" "$JSONL" --ep "$ep" > "$ST/meter.json" 2>/dev/null || echo '{}' > "$ST/meter.json"
finish 0
