#!/bin/bash
# episode_s2.sh — ONE hermetic S2-Lean episode (stage A, B or C of one CLEVER problem): refuse · prepare · assert · run
# claude · extract bodies · check (kernel) · meter · archive. Same discipline and the same audit as harness/episode.sh
# (S1), the environment being a native Lean project instead of a container. REPAIR ROUND 1 (2026-08-28, refuter pass on
# 86f9e04): THE FENCE IS THE OS (Claude Code's Seatbelt sandbox from settings.s2.json — network denied, reads of the
# harness trees denied, writes only in cwd; D1), THE HOOK IS THE AUDIT (D12); the shared Lean project is a git-free
# export under $HOME/lean-shared with no ground truth anywhere above or below it (D2); ground truth is NEVER on the host
# during stage A (D3: any frozen.json/C.lean under $BENCH or $VIEWS refuses); stage B assembles from the SCORED stage-A
# body with provenance (D5: A.bodies.json); claude runs in its own process group and the watchdog/traps kill the group,
# no lean/lake may survive the episode (D11); every harness file the episode depends on is sha-asserted (FN-10, F10).
#   usage: printf '%s\n' <arm> | episode_s2.sh <problem_id> <A|B|C> [--dry]
#   env:   BENCH (~/bench) · H (~/bench/harness) · CFG (~/.claude-bench) · EPROOT (~/work) · LEANPROJ (~/lean-shared/clever)
#          VIEWS (~/bench/s2views) · MODEL EFFORT MAX_TURNS(40) WALL_S(5400) TOKEN_CEILING(8000000) PROMPT_OVERRIDE LANDINGS
#          CLAUDE_BIN + CLAUDE_BIN_STUB=1 (the run-shaped dry: dry_exec_stub_s2.sh; lands DRYEXEC(...) in dryexec.log and
#          keeps its bodies under state/s2-dry, never state/s2) · REFUSE_GIT_CHECK=skip (honoured ONLY with CLAUDE_BIN_STUB
#          or --dry: lets a seat dry run against a LEANPROJ that sits inside a git clone; a real episode ignores it and refuses)
# Stage B needs the SAME ARM's scored stage-A body: <state root>/<problem>/<arm>/A.bodies.json (written ONLY by a stage-A
# episode whose termination is scored and whose check passed; otherwise deleted). The driver lands the synthetic
# `<none> <task> B <arm> NOT_PROVEN(no_stage_A_pass) 0` when it is absent; this script only refuses.
set -u
PID="${1:?problem_id}"; STAGE="${2:?A|B|C}"; DRY="${3:-}"
read -r arm || true; [ -n "${arm:-}" ] || { echo "REFUSE: the arm must arrive on stdin"; exit 4; }
case "$arm" in a[0-9]|a[0-9][0-9]|s[0-9]) ;; *) echo "REFUSE: bad arm id '$arm'"; exit 4 ;; esac
case "$STAGE" in A|B|C) ;; *) echo "REFUSE: stage must be A, B or C"; exit 4 ;; esac
case "$PID" in ''|*[!0-9]*) echo "REFUSE: problem_id must be a number"; exit 4 ;; esac
BENCH="${BENCH:-$HOME/bench}"; H="${H:-$BENCH/harness}"; S2="$H/s2lean"; CFG="${CFG:-$HOME/.claude-bench}"; EPROOT="${EPROOT:-$HOME/work}"
LEANPROJ="${LEANPROJ:-$HOME/lean-shared/clever}"; VIEWS="${VIEWS:-$BENCH/s2views}"
MODEL="${MODEL:-claude-sonnet-5}"; EFFORT="${EFFORT:-high}"; MAX_TURNS="${MAX_TURNS:-40}"
WALL_S="${WALL_S:-5400}"; TOKEN_CEILING="${TOKEN_CEILING:-8000000}"; LANDINGS="${LANDINGS:-s2-landings.log}"
PROMPT_OVERRIDE="${PROMPT_OVERRIDE:-}"; REAL_HOME="$HOME"; STUB="${CLAUDE_BIN_STUB:-}"
# a stub-driven run can never land where the driver reads, nor seed real state (refuter RI3-F1, M5)
SROOT="$BENCH/state/s2"; [ -n "$STUB" ] && { LANDINGS="dryexec.log"; SROOT="$BENCH/state/s2-dry"; }
GITCHK="${REFUSE_GIT_CHECK:-}"
ep="ep-$(head -c 4 /dev/urandom | od -An -tx1 | tr -d ' \n')"
EP="$EPROOT/$ep"; ST="$BENCH/state/$ep"; TASK="problem_$PID"; ABDIR="$SROOT/$TASK/$arm"
mkdir -p "$EP" "$ST" "$BENCH/logs" "$EPROOT" "$ABDIR"
log() { printf '%s %s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$*" | tee -a "$ST/episode.log"; }
now() { date -u +%s; }
term="UNSET"; t0=$(now); crc=""; SID=""; JSONL=""; killed=""; finished=""; CPID=""; orphans=0
CLAUDE_BIN="${CLAUDE_BIN:-$(command -v claude)}"
PINNED_CLAUDE=$(grep '^claude-version ' "$H/HASHES.txt" | cut -d' ' -f2)
AGENT_PATH="${AGENT_PATH:-/usr/local/bin:/opt/homebrew/bin:/usr/bin:/bin:/usr/sbin:/sbin:$REAL_HOME/.local/bin}"
sha() { shasum -a 256 "$1" 2>/dev/null | cut -d' ' -f1; }
pin2() { grep -F -- "$1 " "$H/HASHES.txt" | grep -E "^$1 " | head -1 | cut -d' ' -f2; }     # `<key> <sha>`
pin3() { grep -F -- "$1 $2 " "$H/HASHES.txt" | grep -E "^$1 $2 " | head -1 | cut -d' ' -f3; } # `<key> <task> <sha>`
refuse() { echo "REFUSE: $*"; rm -rf "$EP" "$ST"; exit "${1:+3}"; }
die() { log "HARNESS_ERROR $*"; term="HARNESS_ERROR"; finish 1; }
printf 'EPISODE %s\n' "$ep"
# ── 0. the harness that runs must be the harness that is pinned (refuter RI-2; FN-10 extends it to every S2 file) ──
self_sha=$(sha "$0"); want_self=$(pin2 s2lean/episode_s2.sh)
[ "$self_sha" = "$want_self" ] || { echo "REFUSE: episode_s2.sh sha $self_sha is not the pinned $want_self (hashes.sh + sync_studio.sh first)"; rm -rf "$EP" "$ST"; exit 5; }
for f in "$S2"/*; do
  [ -f "$f" ] || continue; b=$(basename "$f"); case "$b" in *.pyc) continue ;; esac
  want=$(pin2 "s2lean/$b"); [ -n "$want" ] || refuse "s2lean/$b is on the host but not pinned in HASHES.txt"
  [ "$want" = "$(sha "$f")" ] || refuse "s2lean/$b sha drift: host $(sha "$f") pinned $want"
done
want_s=$(pin2 settings.s2.json); [ -n "$want_s" ] && [ "$want_s" = "$(sha "$CFG/settings.json")" ] || refuse "$CFG/settings.json is not the pinned settings.s2.json (want '$want_s')"
want_h=$(pin2 hook-deny-network.sh); [ -n "$want_h" ] && [ "$want_h" = "$(sha "$H/hook-deny-network.sh")" ] || refuse "hook sha drift"
want_m=$(pin2 meter.py); [ -n "$want_m" ] && [ "$want_m" = "$(sha "$H/meter.py")" ] || refuse "meter.py sha drift"
command -v perl >/dev/null 2>&1 || refuse "perl missing (rt bound)"; command -v lsof >/dev/null 2>&1 || refuse "lsof missing (orphan sweep)"
# ── 1. THE SHARED PROJECT (D2): an export, not a clone; no ground truth above or below it; its three files pinned ──
[ -d "$LEANPROJ" ] && [ -f "$LEANPROJ/lakefile.lean" ] || refuse "LEANPROJ $LEANPROJ is not a lake project"
LP_REAL=$(cd "$LEANPROJ" && pwd -P); LS_ROOT=$(dirname "$LP_REAL")
[ -e "$LEANPROJ/human_eval" ] || [ -e "$LEANPROJ/sample_examples" ] && refuse "$LEANPROJ carries human_eval/ or sample_examples/ (full solutions)"
[ -f "$LEANPROJ/.lake/build/lib/lean/Imports/AllImports.olean" ] || refuse "shared project is not built (Imports/AllImports.olean missing)"
[ -z "$(ls "$LEANPROJ/.lake/build/lib/lean/human_eval" "$LEANPROJ/.lake/build/lib/lean/sample_examples" 2>/dev/null)" ] || refuse "human_eval/sample_examples oleans present in the shared build"
[ -z "$(find "$LS_ROOT" \( -name 'problem_*.lean' -o -name human_eval -o -name sample_examples \) -not -path '*/.lake/packages/*' 2>/dev/null | head -1)" ] || refuse "solution-bearing file under $LS_ROOT"
if [ "$GITCHK" = "skip" ]; then
  [ -n "$STUB" ] || [ "$DRY" = "--dry" ] || refuse "REFUSE_GIT_CHECK=skip is honoured only with CLAUDE_BIN_STUB or --dry"
  log "WARNING REFUSE_GIT_CHECK=skip: the .git-ancestry assertions on $LEANPROJ are SKIPPED (seat dry only)"
else
  git -C "$LEANPROJ" rev-parse --git-dir >/dev/null 2>&1 && refuse "$LEANPROJ is inside a git repository ($(git -C "$LEANPROJ" rev-parse --git-dir 2>/dev/null))"
  [ -z "$(find "$LS_ROOT" -name .git -not -path '*/.lake/packages/*/.git' 2>/dev/null | head -1)" ] || refuse ".git under $LS_ROOT: $(find "$LS_ROOT" -name .git -not -path '*/.lake/packages/*/.git' | head -1)"
  [ -z "$(find "$LS_ROOT" -name packed-refs -not -path '*/.lake/packages/*' 2>/dev/null | head -1)" ] || refuse "packed-refs under $LS_ROOT"
fi
# the packages' own .git (mathlib etc.) must stay — Lake checks `git rev-parse HEAD` against the manifest on every load
# (lake/Lake/Load/Materialize.lean:233 at v4.27.0) and would re-clone without it; none of them may be CLEVER
for g in "$LEANPROJ"/.lake/packages/*/.git; do [ -e "$g" ] || continue
  u=$(git --git-dir="$g" config --get remote.origin.url 2>/dev/null); case "$u" in *clever*|*CLEVER*) refuse "package $(basename "$(dirname "$g")") is a CLEVER clone ($u)" ;; esac; done
LP_LF=$(sha "$LEANPROJ/lakefile.lean"); LP_MF=$(sha "$LEANPROJ/lake-manifest.json"); LP_TC=$(sha "$LEANPROJ/lean-toolchain")
[ "$LP_LF" = "$(pin2 leanproj-lakefile)" ] || refuse "lakefile.lean sha $LP_LF != pinned '$(pin2 leanproj-lakefile)'"
[ "$LP_MF" = "$(pin2 leanproj-manifest)" ] || refuse "lake-manifest.json sha $LP_MF != pinned '$(pin2 leanproj-manifest)'"
[ "$LP_TC" = "$(pin2 leanproj-toolchain)" ] || refuse "lean-toolchain sha $LP_TC != pinned '$(pin2 leanproj-toolchain)'"
# ── 2. THE VIEWS (D3, F10, M8, GT-7): stage A with NO ground truth ANYWHERE on the host; every frozen file pinned ──
if [ "$STAGE" = "A" ]; then
  gt=$(find "$BENCH" "$VIEWS" \( -name frozen.json -o -name C.lean \) 2>/dev/null | head -3 | tr '\n' ' ')
  [ -z "$gt" ] || refuse "ground truth on the host during stage A: $gt"
  # a cached B/C pristine file carries problem_spec too (check.py --pristine-cache): none may remain while stage A runs
  pc=$(find "$VIEWS/.pristine-cache" \( -path '*/B/*' -o -path '*/C/*' \) -name canonical.lean 2>/dev/null | head -3 | tr '\n' ' ')
  [ -z "$pc" ] || refuse "B/C pristine cache (carries problem_spec) present during stage A: $pc"
  [ -s "$VIEWS/$TASK/A.lean" ] || refuse "no A view for $TASK"
  [ -s "$VIEWS/$TASK/frozenA.json" ] || refuse "no frozenA.json for $TASK"
  FZ="$VIEWS/$TASK/frozenA.json"; want_f=$(pin3 frozenA "$TASK"); [ -n "$want_f" ] && [ "$want_f" = "$(sha "$FZ")" ] || refuse "frozenA.json sha $(sha "$FZ") != pinned '$want_f' for $TASK"
else
  [ -s "$VIEWS/$TASK/frozen.json" ] || refuse "no frozen.json for $TASK (stage_views.sh ship BC first)"
  FZ="$VIEWS/$TASK/frozen.json"; want_f=$(pin3 frozen "$TASK"); [ -n "$want_f" ] && [ "$want_f" = "$(sha "$FZ")" ] || refuse "frozen.json sha $(sha "$FZ") != pinned '$want_f' for $TASK"
  [ "$STAGE" = "C" ] && { [ -s "$VIEWS/$TASK/C.lean" ] || refuse "no C view for $TASK"; }
  [ "$STAGE" = "B" ] && { [ -s "$ABDIR/A.bodies.json" ] || refuse "no scored stage-A pass for $TASK/$arm (the driver lands NOT_PROVEN(no_stage_A_pass))"; }
fi
FROZEN_SHA=$(sha "$FZ")

finish() {
  [ -n "$finished" ] && return 0
  finished=1; rc="${1:-0}"
  [ -f "$EP/repo/.rt.log" ] && [ ! -f "$ST/rt.log" ] && mv "$EP/repo/.rt.log" "$ST/rt.log" 2>/dev/null
  [ -d "$EP" ] && mv "$EP" "$ST/eptree" 2>/dev/null
  [ -n "$PROMPT_OVERRIDE" ] && term="SMOKE($term)"
  [ -n "$STUB" ] && term="DRYEXEC($term)"
  t1=$(now)
  ARMV="$arm" ORPHANS="$orphans" LP_REAL="$LP_REAL" LP_LF="$LP_LF" LP_MF="$LP_MF" LP_TC="$LP_TC" FROZEN_SHA="$FROZEN_SHA" ABDIR="$ABDIR" ARMFILE="$ARMFILE" \
  python3 - "$ST" "$PID" "$STAGE" "$term" "$rc" "$t0" "$t1" "$MODEL" "$EFFORT" "$MAX_TURNS" "$WALL_S" "$TOKEN_CEILING" "$H" "$CFG" "$CLAUDE_BIN" "$ep" "${SID:-}" "$AGENT_PATH" "$LEANPROJ" <<'PY'
import json,sys,hashlib,os,subprocess
(st,pid,stage,term,rc,t0,t1,model,effort,mt,wall,ceil,h,cfg,cbin,ep,sid,apath,proj)=sys.argv[1:]
E=os.environ; arm=E.get("ARMV")
def sha(p):
    try: return hashlib.sha256(open(p,'rb').read()).hexdigest()
    except Exception: return None
def jl(p):
    try: return json.load(open(p))
    except Exception: return {}
pm=jl(os.path.join(st,"prompt_meta.json")); mt_=jl(os.path.join(st,"meter.json")); ck=jl(os.path.join(st,"check.json"))
ab=jl(os.path.join(E["ABDIR"],"A.bodies.json")) if stage=="B" else {}
vs=jl(os.path.join(h,"s2lean","view_status.json")).get("problem_%s"%pid)
starts=ends=ok=0
try:
    for l in open(os.path.join(st,"rt.log")):
        if "\tSTART\t" in l: starts+=1
        if "\tEND\t" in l:
            ends+=1; ok+= ("\trc=0\t" in l)
except Exception: pass
armfile=E["ARMFILE"]
def ver():
    try: return subprocess.check_output([cbin,"--version"]).decode().strip()
    except Exception: return None
CK=("class","compiled","rc","passed","screen","replay_ok","statements_identical","statement_diffs","axioms_ok","axioms","tests_in_file","a_body_value_identical","compile_wall_s","audit_wall_s","sorry_lines","forbidden","wall_s")
m={"episode":ep,"substrate":"S2-Lean/CLEVER","instance_id":"problem_%s"%pid,"stage":stage,"arm":arm,
   "termination":term,"claude_exit_code":int(rc),"start_utc":int(t0),"end_utc":int(t1),"wall_s":int(t1)-int(t0),
   "model_requested":model,"effort":effort,"max_turns":int(mt),"wall_ceiling_s":int(wall),"token_ceiling":int(ceil),
   "session_id":sid,"claude_bin":cbin,"claude_bin_target":(os.path.realpath(cbin) if cbin else None),"claude_version":ver(),
   "host_arch":os.uname().machine,"lean_toolchain":(open(os.path.join(proj,"lean-toolchain")).read().strip() if os.path.exists(os.path.join(proj,"lean-toolchain")) else None),
   "leanproj":proj,"leanproj_realpath":E.get("LP_REAL"),"leanproj_sha":{"lakefile":E.get("LP_LF"),"manifest":E.get("LP_MF"),"toolchain":E.get("LP_TC"),
   "combined":hashlib.sha256((E.get("LP_LF","")+E.get("LP_MF","")+E.get("LP_TC","")).encode()).hexdigest()},
   "agent_path":apath,"freeze_commit":(open(os.path.join(h,"FREEZE-COMMIT")).read().strip() if os.path.exists(os.path.join(h,"FREEZE-COMMIT")) else None),
   "arm_rendering_sha256":hashlib.sha256(open(os.path.join(h,"s2lean","base.md"),"rb").read()+open(armfile,"rb").read()).hexdigest(),
   "arm_file":os.path.relpath(armfile,h),"arm_block_bytes":os.path.getsize(armfile),"claude_md_sha256":sha(os.path.join(st,"eptree","CLAUDE.md")),
   "prompt_sha256":pm.get("prompt_sha256"),"prompt_sha256_canonical":pm.get("prompt_sha256_canonical"),"view_sha256":pm.get("view_sha256"),
   "prompt_override_sha256":sha(os.path.join(st,"prompt_override.txt")),"frozen_sha256":E.get("FROZEN_SHA"),"view_status":vs,
   "settings_sha256":sha(os.path.join(cfg,"settings.json")),"hook_sha256":sha(os.path.join(h,"hook-deny-network.sh")),"episode_sh_sha256":sha(os.path.join(h,"s2lean","episode_s2.sh")),
   "checker_sha256":{f:sha(os.path.join(h,"s2lean",f)) for f in ("check.py","extract.py","assemble.py","s2audit.lean","screen.py","sandbox_check.sb","rt.template","build_views.py")},
   "task_file_sha256":sha(os.path.join(st,"eptree","repo","task.lean")),"bodies_sha256":sha(os.path.join(st,"bodies.json")),
   "a_episode":ab.get("a_episode"),"a_bodies_sha256":ab.get("a_bodies_sha256"),"a_termination":ab.get("a_termination"),"a_view_sha256":ab.get("a_view_sha256"),
   "rt_calls":ends,"rt_calls_rc0":ok,"rt_unfinished":max(0,starts-ends),"orphans_killed":int(E.get("ORPHANS") or 0),
   "metered_sum":mt_.get("metered_sum"),"metered_sum_governing":(mt_.get("crosscheck") or {}).get("metered_sum_governing"),
   "metered_sum_incl_compaction_floor":mt_.get("metered_sum_incl_compaction_floor"),
   "calls":mt_.get("calls"),"void_reasons":mt_.get("void_reasons"),"compactions":mt_.get("compactions"),"models":mt_.get("models"),
   "service_tiers":mt_.get("service_tiers"),"tool_timeouts":mt_.get("tool_timeouts"),"first_call_usage":mt_.get("first_call_usage"),"unknown_tools":mt_.get("unknown_tools"),
   "escape_attempts_blocked":len(mt_.get("escape_attempts_blocked") or []),"url_mentions":mt_.get("url_mentions"),
   "quota_evidence":(open(os.path.join(st,"quota_evidence.txt")).read().strip() if os.path.exists(os.path.join(st,"quota_evidence.txt")) else None),
   "check":{k:ck.get(k) for k in CK if k in ck} if ck else None,
   "passed":bool(ck.get("passed")) if ck else False,
   "flags":["-p <prompt>","--model",model,"--effort",effort,"--max-turns",mt,"--dangerously-skip-permissions","--disallowedTools","WebFetch,WebSearch,Agent,Task,Workflow,Skill,Monitor,CronCreate,CronDelete,CronList,RemoteTrigger,SendMessage,ListAgents,PushNotification,SendUserFile,EnterWorktree,ExitWorktree","--strict-mcp-config","--setting-sources","user,project","--output-format","json","--session-id <uuid>"]}
json.dump(m,open(os.path.join(st,"manifest.json"),"w"),indent=1,sort_keys=True)
PY
  landed="$(date -u +%Y-%m-%dT%H:%M:%SZ) LANDED $ep task=$TASK stage=$STAGE arm=$arm term=$term passed=$(python3 -c "import json;print(json.load(open('$ST/manifest.json'))['passed'])" 2>/dev/null) rc=$rc wall=$(( $(now)-t0 ))s metered=$(python3 -c "import json;m=json.load(open('$ST/manifest.json'));print(m['metered_sum_governing'] or m['metered_sum'])" 2>/dev/null)"
  printf '%s\n' "$landed" >> "$ST/episode.log"
  # SHA256SUMS LAST (D11): nothing is appended to an archived file after this line (the LANDED line is already in episode.log)
  ( cd "$ST" && find . -type f ! -name SHA256SUMS -exec shasum -a 256 {} + > SHA256SUMS 2>/dev/null )
  printf '%s\n' "$landed"
  printf '%s %s %s %s %s %s\n' "$ep" "$TASK" "$STAGE" "$arm" "$term" "$(python3 -c "import json;m=json.load(open('$ST/manifest.json'));print(m['metered_sum_governing'] or m['metered_sum'] or 0)" 2>/dev/null)" >> "$BENCH/logs/$LANDINGS"
  exit "$rc"
}
killgroup() { [ -n "${CPID:-}" ] || return 0; kill -TERM -- "-$CPID" 2>/dev/null; sleep "${1:-5}"; kill -KILL -- "-$CPID" 2>/dev/null; }
trap '[ -z "$finished" ] && { term="HARNESS_ERROR(abort:line$LINENO:$term)"; finish 1; }' EXIT
trap 'killgroup 5; term="HARNESS_ERROR(signal)"; finish 1' INT TERM HUP

[ -n "$CLAUDE_BIN" ] || die "claude not found"
if [ -z "$STUB" ]; then cv=$("$CLAUDE_BIN" --version 2>/dev/null | cut -d' ' -f1); [ "$cv" = "$PINNED_CLAUDE" ] || die "claude version '$cv' is not the pinned $PINNED_CLAUDE"; fi
# ── 3. the working copy: a project dir with the lakefile + Imports SOURCE, `.lake` → the shared read-only build ──
mkdir -p "$EP/repo" && cp "$LEANPROJ/lakefile.lean" "$LEANPROJ/lake-manifest.json" "$LEANPROJ/lean-toolchain" "$EP/repo/" && cp -R "$LEANPROJ/Imports" "$EP/repo/Imports" || die "project copy"
ln -s "$LEANPROJ/.lake" "$EP/repo/.lake" || die "lake link"
# ── 4. the task file for this stage ──────────────────────────────────────────────────────────────
case "$STAGE" in
  A) cp "$VIEWS/$TASK/A.lean" "$EP/repo/task.lean" || die "A view" ;;
  C) cp "$VIEWS/$TASK/C.lean" "$EP/repo/task.lean" || die "C view" ;;
  B) AB="$ABDIR/A.bodies.json"
     python3 - "$FZ" "$AB" "$S2/build_views.py" > "$EP/repo/task.lean" <<'PY' || die "B assemble"
import json,sys,importlib.util
fz=json.load(open(sys.argv[1])); ab=json.load(open(sys.argv[2]))
for k in ("generated_spec_body","a_episode","a_bodies_sha256","a_termination","a_passed"):
    if k not in ab: raise SystemExit("A.bodies.json lacks %s (not a D5 provenance object)" % k)
if not ab["a_passed"]: raise SystemExit("A.bodies.json says a_passed=false")
spec=importlib.util.spec_from_file_location("bv",sys.argv[3]); bv=importlib.util.module_from_spec(spec); spec.loader.exec_module(bv)
sys.stdout.write(bv.assemble_B(fz, ab["generated_spec_body"]))
PY
     ;;
esac
bash "$H/check2b.sh" "$EP/repo" > "$ST/check2b.host.log" 2>&1 || { cat "$ST/check2b.host.log"; die "CHECK2B host FAIL"; }
# ── 5. prompt + arm file + wrapper; the episode dir holds EXACTLY CLAUDE.md repo rt ─────────────
ARMFILE="$H/arms/$arm.md"; [ "$arm" = "a1" ] && [ -f "$S2/placebo.md" ] && ARMFILE="$S2/placebo.md"   # D15: a1 = BASE + placebo.md
ARMFILE="$ARMFILE" python3 - "$STAGE" "$EP" "$ST" "$S2" "$arm" <<'PY' || die "prompt/arm build"
import json,sys,hashlib,os
stage,ep,st,s2,arm=sys.argv[1:]
tmpl=open(os.path.join(s2,"prompt_%s.md"%stage)).read()
prompt=tmpl.replace("__EP__",ep); canon=tmpl
base=open(os.path.join(s2,"base.md")).read().replace("__EP__",ep); armb=open(os.environ["ARMFILE"]).read()
open(os.path.join(st,"prompt.md"),"w").write(prompt); open(os.path.join(ep,"CLAUDE.md"),"w").write(base+armb)
view=open(os.path.join(ep,"repo","task.lean"),"rb").read()
json.dump({"stage":stage,"prompt_sha256":hashlib.sha256(prompt.encode()).hexdigest(),"prompt_sha256_canonical":hashlib.sha256(canon.encode()).hexdigest(),"view_sha256":hashlib.sha256(view).hexdigest()},open(os.path.join(st,"prompt_meta.json"),"w"),indent=1)
PY
if [ -n "$PROMPT_OVERRIDE" ]; then printf '%s\n' "$PROMPT_OVERRIDE" > "$ST/prompt.md"; cp "$ST/prompt.md" "$ST/prompt_override.txt"; fi
sed -e "s|__EP__|$EP|g" "$S2/rt.template" > "$EP/rt" && chmod +x "$EP/rt"
grep -q '__ST__\|__EP__' "$EP/rt" && die "rt template not fully rendered"
[ "$(ls -A "$EP" | sort | tr '\n' ' ')" = "CLAUDE.md repo rt " ] || die "episode dir holds more than CLAUDE.md repo rt: $(ls -A "$EP")"
[ "$(ls -A "$EPROOT" | tr '\n' ' ')" = "$ep " ] || die "EPROOT holds more than this episode: $(ls -A "$EPROOT")"
# ── 6. hermeticity assertions (as S1) ───────────────────────────────────────────────────────────
p="$EP"; while [ "$p" != "/" ]; do p=$(dirname "$p"); [ -e "$p/CLAUDE.md" ] && die "CLAUDE.md above the episode at $p"; done
[ -e "$CFG/CLAUDE.md" ] && die "CLAUDE.md in the config dir"
[ -z "$(ls -A "$CFG/projects" 2>/dev/null)" ] || die "config dir projects/ is not empty before the episode"
for d in file-history session-env sessions todos shell-snapshots debug; do [ -z "$(ls -A "$CFG/$d" 2>/dev/null)" ] || die "config dir $d/ is not empty before the episode"; done
for f in CLAUDE.md commands agents skills rules hooks .mcp.json; do [ -e "$CFG/$f" ] && die "config dir carries agent-influencing entry $f"; done
ls -A "$CFG" | grep -Ev '^(\.claude\.json|\.claude\.json\.bak[^ ]*|settings\.json|projects|sessions|backups|cache|plugins|history\.jsonl|shell-snapshots|todos|debug|statsig|file-history|\.last-[^ ]*|session-env)$' > "$ST/configdir_unexpected.txt" || true
want_a=$(grep -F "rendered-s2-$arm(__EP__) " "$H/HASHES.txt" | cut -d' ' -f2); have_a=$(cat "$S2/base.md" "$ARMFILE" | shasum -a 256 | cut -d' ' -f1)
[ -n "$want_a" ] && [ "$want_a" = "$have_a" ] || die "arm rendering sha $have_a != pinned '$want_a'"
[ "$(sed "s|$EP|__EP__|g" "$EP/CLAUDE.md" | shasum -a 256 | cut -d' ' -f1)" = "$have_a" ] || die "episode CLAUDE.md is not the pinned rendering"
have_v=$(python3 -c "import json;print(json.load(open('$ST/prompt_meta.json'))['view_sha256'])")
if [ "$STAGE" != "B" ]; then want_v=$(pin3 "view-$STAGE" "$TASK"); [ -n "$want_v" ] && [ "$want_v" = "$have_v" ] || die "view sha $have_v != pinned '$want_v' for $TASK/$STAGE"; fi
# the wrapper under the agent's exact environment: Mathlib import must succeed (the slow first load happens HERE, not in
# the episode); the bound's rc passthrough is asserted too (refuter M1: a missing binary can never again pass the freeze)
( cd "$EP/repo" && env -i HOME="$REAL_HOME" USER="$USER" LOGNAME="$USER" PATH="$AGENT_PATH" TERM=dumb LANG=en_US.UTF-8 "$EP/rt" 'printf "import Imports.AllImports\n#eval 6*7\n" > /tmp/rtprobe_'"$ep"'.lean && lake env lean /tmp/rtprobe_'"$ep"'.lean' ) > "$ST/env_probe.txt" 2>&1 || { cat "$ST/env_probe.txt"; die "rt wrapper (lake env lean) fails under the agent environment"; }
rm -f "/tmp/rtprobe_$ep.lean"
( cd "$EP/repo" && env -i HOME="$REAL_HOME" USER="$USER" LOGNAME="$USER" PATH="$AGENT_PATH" TERM=dumb LANG=en_US.UTF-8 "$EP/rt" 'exit 3' ) >/dev/null 2>&1; [ "$?" = 3 ] || die "rt wrapper does not pass the command's rc through"
mv "$EP/repo/.rt.log" "$ST/rt.probe.log" 2>/dev/null
printf 'leanproj_realpath=%s\n' "$LP_REAL" >> "$ST/env_probe.txt"
log "PREPARED task=$TASK stage=$STAGE lean=$(cat "$EP/repo/lean-toolchain") probe=$(sed -n 1p "$ST/env_probe.txt")"
[ "$DRY" = "--dry" ] && { term="DRY"; finish 0; }
# ── 7. run claude in ITS OWN PROCESS GROUP (D11), watched; the watchdog kills the group ─────────
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
  if [ -n "$JSONL" ] && [ -z "$killed" ]; then ms=$(python3 "$H/meter.py" "$JSONL" --live 2>/dev/null | python3 -c "import json,sys; print(json.load(sys.stdin)['metered_sum'])" 2>/dev/null || echo 0); [ "${ms:-0}" -ge "$TOKEN_CEILING" ] && killed="TOKEN_CEILING"; fi
  if [ -n "$killed" ]; then log "WATCHDOG $killed at ${el}s"; killgroup 10; break; fi
done
wait "$CPID"; crc=$?; sleep 2
if pgrep -f -- "--session-id $SID" >/dev/null 2>&1; then pkill -KILL -f -- "--session-id $SID"; orphans=$((orphans+1)); log "ORPHAN_KILLED claude still held $SID after wait"; fi
kill -KILL -- "-$CPID" 2>/dev/null
# no lean/lake (or anything) may keep running under the episode: every process whose cwd is inside $EP is an orphan
for op in $(lsof -a -d cwd -u "$USER" -Fpn 2>/dev/null | awk -v ep="$EP" '/^p/{p=substr($0,2)} /^n/{if (index(substr($0,2), ep)==1) print p}'); do
  [ "$op" = "$$" ] && continue; cn=$(ps -o comm= -p "$op" 2>/dev/null); kill -KILL "$op" 2>/dev/null && { orphans=$((orphans+1)); log "ORPHAN_KILLED pid=$op comm=$cn cwd under $EP"; }
done
[ -f "$EP/repo/.rt.log" ] && mv "$EP/repo/.rt.log" "$ST/rt.log"
[ -z "$JSONL" ] && JSONL=$(find "$CFG/projects" -name "$SID.jsonl" 2>/dev/null | head -1)
# ── 8. termination (as S1; reads `errors` (list) + `error` — refuter MT-R3), then the KERNEL ──────
python3 - "$ST" > "$ST/cli_text.txt" 2>/dev/null <<'PY'
import json,sys,os
st=sys.argv[1]
try:
    r=json.load(open(os.path.join(st,"result.json"))); print(("ERR:" if r.get("is_error") else "")+str(r.get("subtype",""))); print(str(r.get("result") or "")[:2000].replace("\n"," "))
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
python3 "$S2/extract.py" "$STAGE" "$EP/repo/task.lean" > "$ST/bodies.json" 2>"$ST/extract.err" || { : > "$ST/bodies.json"; term="${term}+NO_BODIES"; }
# the agent's whole task file is archived; the audit-relevant command tokens in it are counted (refuter NF4 tripwire)
grep -Ec '#eval|run_cmd|run_tac|run_elab|initialize|IO\.Process|IO\.FS|elab_rules|macro_rules|set_option' "$EP/repo/task.lean" > "$ST/task_meta_tokens.txt" 2>/dev/null
if [ -s "$ST/bodies.json" ]; then
  ABARG=""; if [ "$STAGE" = "B" ]; then
    if grep -q -- '--a-bodies' "$S2/check.py"; then ABARG="--a-bodies $ABDIR/A.bodies.json"
      # the scored stage-A episode's canonical.olean lets the audit record a_body_value_identical (D4, informational)
      aep=$(python3 -c "import json;print(json.load(open('$ABDIR/A.bodies.json')).get('a_episode',''))" 2>/dev/null)
      [ -n "$aep" ] && [ -f "$BENCH/state/$aep/canonical.olean" ] && ABARG="$ABARG --a-olean $BENCH/state/$aep/canonical.olean"
    else log "CHECK_FALLBACK check.py lacks --a-bodies: merging generated_spec_body into the check input (P1's contract not yet landed)"
      python3 - "$ST/bodies.json" "$ABDIR/A.bodies.json" <<'PY'
import json,sys
b=json.load(open(sys.argv[1])); a=json.load(open(sys.argv[2])); b["generated_spec_body"]=a["generated_spec_body"]; b["_a_bodies_sha256"]=a.get("a_bodies_sha256"); json.dump(b,open(sys.argv[1],"w"))
PY
    fi; fi
  ( cd "$LEANPROJ" && PATH="$REAL_HOME/.elan/bin:$PATH" python3 "$S2/check.py" "$STAGE" "$FZ" "$ST/bodies.json" "$LEANPROJ" "$ST/canonical.lean" --timeout 900 --pristine-cache "$VIEWS/.pristine-cache" $ABARG ) > "$ST/check.json" 2> "$ST/check.err" || true
  [ -s "$ST/check.json" ] && python3 -c "import json;json.load(open('$ST/check.json'))" 2>/dev/null || { : > "$ST/check.json"; term="HARNESS_ERROR(check:$term)"; }
fi
if [ -n "$JSONL" ]; then
  cp "$JSONL" "$ST/session.jsonl"
  bash "$H/hook-deny-network.sh" --pattern-escape > "$ST/escape_pattern.txt"; bash "$H/hook-deny-network.sh" --pattern-url > "$ST/url_pattern.txt"
  nj=$(find "$CFG/projects" -name '*.jsonl' | wc -l | tr -d ' '); nsub=$(find "$CFG/projects" -type d -name subagents | wc -l | tr -d ' ')
  extra_j=$(find "$CFG/projects" -name '*.jsonl' ! -name "$SID.jsonl" 2>/dev/null | tr '\n' ' ')
  python3 "$H/meter.py" "$ST/session.jsonl" --result "$ST/result.json" --ep "$EP" --escape-file "$ST/escape_pattern.txt" --url-file "$ST/url_pattern.txt" \
    --neutral "$LP_REAL" --neutral "$LEANPROJ" --neutral "$REAL_HOME/.elan" ${extra_j:+--extra $extra_j} > "$ST/meter.json" 2> "$ST/meter.err"
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
# the shared build must be exactly what it was (refuter M6): the olean the next episode imports
[ -f "$LEANPROJ/.lake/build/lib/lean/Imports/AllImports.olean" ] || term="VOID(BUILD_DAMAGED:${term})"
# ── 9. D5: A.bodies.json is written ONLY for a scored, passed stage A; otherwise the stale one for (task, arm) goes ──
if [ "$STAGE" = "A" ] && [ -z "$PROMPT_OVERRIDE" ]; then
  scored=""; case "$term" in DONE|ROUNDS_EXHAUSTED|WALLCLOCK|TOKEN_CEILING) scored=1 ;; esac
  passed=$(python3 -c "import json;print(bool(json.load(open('$ST/check.json')).get('passed')))" 2>/dev/null)
  if [ -n "$scored" ] && [ "$passed" = "True" ]; then
    python3 - "$ST/bodies.json" "$ABDIR/A.bodies.json" "$ep" "$term" "$(python3 -c "import json;print(json.load(open('$ST/prompt_meta.json'))['view_sha256'])")" <<'PY' && log "A_BODIES written $ABDIR/A.bodies.json" || term="HARNESS_ERROR(a_bodies:$term)"
import json,sys,hashlib
bp,out,ep,term,vsha=sys.argv[1:]
raw=open(bp,"rb").read(); b=json.loads(raw)
json.dump({"generated_spec_body":b["generated_spec_body"],"a_episode":ep,"a_bodies_sha256":hashlib.sha256(raw).hexdigest(),"a_termination":term,"a_passed":True,"a_view_sha256":vsha},open(out,"w"),indent=1)
PY
  else
    [ -e "$ABDIR/A.bodies.json" ] && { rm -f "$ABDIR/A.bodies.json"; log "A_BODIES stale copy deleted for $TASK/$arm (term=$term passed=$passed)"; }
  fi
fi
finish "$crc"
