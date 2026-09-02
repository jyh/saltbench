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
# ⛔ TWO LAYERS, AND ONLY ONE OF THEM IS COMPLETE BY CONSTRUCTION. The FILESYSTEM FENCE (settings.json's
# sandbox.filesystem.denyRead, rendered below) is the FIRST layer and must be complete ON ITS OWN, because it
# is the only layer that applies to every tool. The PreToolUse hook is a SECOND layer and its matcher is
# `Bash|Monitor` — IT COVERS ONLY THE TOOLS IT MATCHES. On 09/02 that difference was measured rather than
# reasoned about: `ep-c392a7ac` asked for one path two ways, the hook BLOCKED the Bash form, and the Read
# tool — which the hook does not match — was served, because the filesystem layer had a hole.
#   ⇒ 🔑 A SECOND LAYER THAT COVERS A SUBSET OF THE TOOLS CANNOT BE READ AS EVIDENCE THE FIRST LAYER HOLDS;
#     it will pass exactly the probes written in the language it matches.
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
# ⛔ THE HARNESS-SIDE PATH MUST CARRY rustup TOO, not just the agent's. `verus` is a shim that resolves its
# toolchain by RUNNING rustup, so every harness-side invocation — the smoke gate, check_verus's fence
# rendering — needs it on PATH exactly as the agent does. On the Studio rustup was TRANSPORTED, not installed
# by rustup-init, so no login profile mentions it and the ambient PATH does not carry it.
# The pilot's three episodes REFUSED on precisely this, before any model call. That is the gate working; the
# defect was that the harness and the agent were being given two different machines to run on.
CARGO_BIN="${CARGO_BIN:-$REAL_HOME/.cargo/bin}"
case ":$PATH:" in *":$CARGO_BIN:"*) ;; *) PATH="$CARGO_BIN:$PATH" ;; esac
export PATH
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
# ⛔ --cfg IS NOT OPTIONAL AND IS NOT DERIVED FROM --check's DIRNAME. The fence must DENY the very directory
# holding the credentials this episode authenticates with, and until 09/02 it did not: the deny list named
# `~/.claude-bench` (S2-Lean's) while S2-Rust runs on `~/.claude-bench-rust`, its SIBLING. `ep-c392a7ac` read
# a file inside its own config dir and was served. The renderer REFUSES an unset --cfg rather than defaulting.
python3 "$S2R/render_settings_verus.py" --check "$CFG/settings.json" --bench "$BENCH" --cfg "$CFG" > "$ST/settings_check.txt" 2>&1 \
  || { cat "$ST/settings_check.txt"; refuse "$CFG/settings.json is not the pinned fence template rendered at BENCH=$BENCH CFG=$CFG"; }

# ⛔⛔ THE AGENT'S WORKSPACE MUST NOT BE INSIDE THE FENCE'S OWN DENY SET, AND THIS ASSERTION EXISTS BECAUSE
# TWO EPISODES PASSED WITHOUT IT. Row CO's repair makes `denyRead` DERIVE from `$BENCH` so the fence follows
# the state root; it becomes self-defeating the moment the episode tree is placed INSIDE that root, because
# the agent's own `rt` wrapper and task file then sit in a denied subpath. Measured on `ep-3fba0475`:
# `denyRead` carried `/Users/jyh/bench-rust`, `EPROOT` was `$BENCH/work`, and the agent tried `../rt` THREE
# times, failed silently every time (rt never even logged a START), and spent ten Bash calls hunting for a
# `verus` it was never going to find. It then wrote a proof BLIND — and the proof PASSED.
#   ⇒ 🔑 A FENCE DERIVED FROM THE RUN ROOT MUST NOT CONTAIN THE AGENT'S OWN WORKSPACE. Deriving the deny set
#     was right; what made it wrong was placing the workspace inside the thing being denied. S2-Lean never
#     hit this only because its EPROOT (`$HOME/work`) happens to sit outside `~/bench`.
#   ⇒ 🔑 AND THE EPISODE STILL SCORED. A blind agent that passes is not a cheap pass — it is a measurement of
#     a DIFFERENT TASK than the one registered, and nothing downstream could have told the difference.
# This is a REFUSAL and not a warning: an episode the agent cannot check its work in must not be scored.
python3 - "$CFG/settings.json" "$EP" <<'PY' || refuse "the episode workspace is inside the agent fence's deny set (see above)"
import json, os, sys
cfg, ep = sys.argv[1], os.path.realpath(sys.argv[2])
deny = json.load(open(cfg))["sandbox"]["filesystem"].get("denyRead") or []
hit = [d for d in deny if ep == d or ep.startswith(os.path.realpath(os.path.expanduser(d)) + os.sep)]
if hit:
    print("FENCE SELF-BLOCK: the episode dir %s is inside denied path(s) %s" % (ep, hit))
    print("  the agent could not read or execute its own rt wrapper; set EPROOT outside $BENCH")
    sys.exit(2)
print("fence/workspace disjoint: %s is outside every denyRead entry" % ep)
PY

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
   "metered_sum":mt_.get("metered_sum"),"metered_classes":mt_.get("classes"),"calls":mt_.get("calls"),
   # ⛔ THE INTEGRITY AUDIT IS IN THE RECORD, NOT ONLY IN A LOG BESIDE IT. These four fields are why the
   # transcript is archived at all: without them a scored episode carries its verdict and no evidence that
   # the verdict was earned inside the fence. `session_jsonl_sha256` ties the manifest to the exact
   # transcript that produced it, so a later audit reads the same bytes this run metered.
   "escape_attempts_blocked":mt_.get("escape_attempts_blocked"),
   "escape_unblocked":mt_.get("escape_unblocked"),
   "url_mentions":mt_.get("url_mentions"),
   "void":mt_.get("void"),"void_reasons":mt_.get("void_reasons"),
   "session_jsonl_sha256":sha(os.path.join(st,"session.jsonl")),
   # ⛔ `tool_uses` and `bash_commands` are the keys meter.py ACTUALLY emits. My first cut wrote
   # `tool_counts`, which meter.py has never produced — it would have recorded null in every manifest and
   # read, to anyone scanning the record, as "this episode used no tools". A DEAD FIELD IS NOT A CHEAP FIELD.
   # `bash_commands` is the field that answers the question I could not answer about the first PASS: whether
   # the agent invoked `rt` at all, or never tried.
   "tool_uses":mt_.get("tool_uses"),"bash_commands":mt_.get("bash_commands"),
   "unknown_tools":mt_.get("unknown_tools"),"compactions":mt_.get("compactions")}
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
# ⚠️ AND THE PROBE IS NOT SUFFICIENT ON ITS OWN, WHICH IT LOOKED LIKE UNTIL IT WASN'T. It runs HARNESS-side,
# unfenced, so it certifies that the wrapper works FOR THE HARNESS. On ep-3fba0475 this probe passed and the
# AGENT still could not execute the same wrapper, because the agent runs under a Seatbelt fence the harness
# does not. The structural assertion above (workspace disjoint from the deny set) is what actually covers
# the agent's case; this probe covers the wrapper's own correctness. Two claims, two checks — the same
# lesson the toolchain gate taught when its identity and capability halves disagreed about the machine.
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
# ⛔ THE TERMINATION IS PASSED TO THE CHECKER so a body captured mid-kill is not scored as a verdict.
# `ep-ecc1a8ee` was killed by the token watchdog after 6 referee calls and scored SCREEN on two `assume(`
# in the helpers region — ordinary proof development (assume a lemma, discharge it later) convicted as
# cheating because the agent never got to remove it. A HALT IS NOT A FAIL, and that has to bind where the
# verdict is written.
BENCH="$BENCH" python3 "$S2R/check_verus.py" --frozen "$FZ" --agent-file "$EP/repo/task.rs" \
   --verus "$VERUS_ROOT/verus" --lynette "$LYNETTE_BIN" --rlimit "$RLIMIT" --seed "$SEED" \
   --termination "$term" \
   --out "$ST/check.json" > "$ST/check.stdout" 2> "$ST/check.stderr"
ccrc=$?; [ "$ccrc" = 2 ] && log "CHECK HARNESS rc=$ccrc (see check.stderr)"
[ -s "$ST/check.json" ] && python3 -c "import json;json.load(open('$ST/check.json'))" 2>/dev/null || { : > "$ST/check.json"; term="HARNESS_ERROR(check:$term)"; }

# ── 10. THE ARCHIVE AND THE INTEGRITY AUDIT ─────────────────────────────────────────────────────────────
# ⛔⛔ THIS WHOLE BLOCK WAS MISSING FROM THE FIRST PORT, AND ITS ABSENCE WAS INVISIBLE UNTIL AN EPISODE
# PASSED AND I TRIED TO AUDIT IT. `s2lean/episode_s2.sh` archives the transcript, runs the escape/url audit,
# detects VOID (subagents, extra jsonls, meter void_reasons), applies the QUOTA(no_call) rule, and CLEANS the
# config dir. My port kept the driver's SHAPE — refuse, prepare, launch, check, land — and silently dropped
# every one of those, because none of them is on the happy path and nothing downstream complained.
# What it cost, measured rather than imagined: the first scored episode landed `PASS` with `rt_calls=0`, and
# I could not tell whether the agent CHOSE not to run the referee or COULD NOT — because the transcript, the
# only artifact that answers it, had never been archived and was then deleted by the next episode's cleanup.
#   ⇒ 🔑 A PORT THAT KEEPS THE SHAPE AND DROPS THE EVIDENCE PRODUCES EPISODES THAT SCORE BUT CANNOT BE
#     AUDITED — and a result you cannot audit is not a cheaper result, it is a different kind of object.
# The config-dir cleanup lives HERE, in the episode that dirtied it, and not in the caller: a driver that
# depends on its caller to tidy up has made hermeticity someone else's job (my pilot script's hand-rolled
# reset is exactly what that looks like, and it killed two episodes before it killed the evidence).
if [ -n "$JSONL" ]; then
  cp "$JSONL" "$ST/session.jsonl"
  bash "$H/hook-deny-network.sh" --pattern-escape > "$ST/escape_pattern.txt"
  bash "$H/hook-deny-network.sh" --pattern-url   > "$ST/url_pattern.txt"
  nj=$(find "$CFG/projects" -name '*.jsonl' | wc -l | tr -d ' ')
  nsub=$(find "$CFG/projects" -type d -name subagents | wc -l | tr -d ' ')
  extra_j=$(find "$CFG/projects" -name '*.jsonl' ! -name "$SID.jsonl" 2>/dev/null | tr '\n' ' ')
  # --neutral names the paths a file tool may read WITHOUT it counting as an escape: the pinned toolchain and
  # the views the agent is supposed to read. S2-Lean neutralises its Lean project and elan for the same reason.
  python3 "$H/meter.py" "$ST/session.jsonl" --result "$ST/result.json" --ep "$EP" \
    --escape-file "$ST/escape_pattern.txt" --url-file "$ST/url_pattern.txt" \
    --neutral "$VERUS_ROOT" --neutral "$LYNETTE_BIN" --neutral "$REAL_HOME/.rustup" --neutral "$REAL_HOME/.cargo" \
    ${extra_j:+--extra $extra_j} > "$ST/meter.json" 2> "$ST/meter.err"
  [ -s "$ST/meter.json" ] || term="HARNESS_ERROR(meter:$term)"
  python3 -c "import json;m=json.load(open('$ST/meter.json'));print('\n'.join(m['escape_unblocked']+['BLOCKED: '+x for x in m['escape_attempts_blocked']]))" > "$ST/network_audit.txt" 2>/dev/null
  if [ "$nj" != "1" ] || [ "$nsub" != "0" ]; then term="VOID(SUBAGENT:${term})"
  elif python3 -c "import json,sys;sys.exit(0 if json.load(open('$ST/meter.json'))['void'] else 1)" 2>/dev/null; then
    term="VOID($(python3 -c "import json;print(','.join(json.load(open('$ST/meter.json'))['void_reasons']))"):${term})"; fi
  # ⛔ zero model calls is a QUOTA symptom, never a result: an episode that never reached the model must not
  # land as DONE with an empty body scored on its merits.
  if [ "$(python3 -c "import json;print(json.load(open('$ST/meter.json')).get('calls',0))" 2>/dev/null)" = "0" ]; then
    case "$term" in AUTH*|QUOTA*|HARNESS*|VOID*) ;; *) term="QUOTA(no_call:$term)" ;; esac; fi
else
  echo '{}' > "$ST/meter.json"
fi
# the config dir is archived and then RESET to its keep-list, by the episode that dirtied it
mkdir -p "$ST/configdir-projects" && cp -R "$CFG/projects/." "$ST/configdir-projects/" 2>/dev/null
for e in "$CFG"/* "$CFG"/.[!.]*; do
  [ -e "$e" ] || continue
  case "$(basename "$e")" in .claude.json|.credentials.json|settings.json|stub_mode) continue ;; esac
  rm -rf "$e"
done
mkdir -p "$CFG/projects"
finish 0
