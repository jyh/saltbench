#!/bin/bash
# episode.sh — ONE hermetic episode: prepare · assert · run claude · extract patch · meter · archive.
#   usage: episode.sh <instance_id> <arm-id a0|a1|...> [--dry]
#   env:   BENCH (default ~/bench) · H (harness dir, default $BENCH/harness) · MODEL · EFFORT · MAX_TURNS
#          WALL_S (default 5400) · TOKEN_CEILING (default 3000000) · CFG (default ~/.claude-bench)
# Runs on the Studio under bash 3.2. Prints one final LANDED line; writes <STATE>/<ep>/manifest.json.
# ⛔ The arm name is never written to disk while the agent runs: it lives in this process until the
#    claude process has exited (arm-blindness by construction, SCOUT-STAGE0 §4).
set -u
IID="${1:?instance_id}"; ARM="${2:?arm}"; DRY="${3:-}"
BENCH="${BENCH:-$HOME/bench}"; H="${H:-$BENCH/harness}"; CFG="${CFG:-$HOME/.claude-bench}"
MODEL="${MODEL:-claude-sonnet-5}"; EFFORT="${EFFORT:-high}"; MAX_TURNS="${MAX_TURNS:-40}"
WALL_S="${WALL_S:-5400}"; TOKEN_CEILING="${TOKEN_CEILING:-3000000}"
ep="ep-$(head -c 4 /dev/urandom | od -An -tx1 | tr -d ' \n')"
EP="$BENCH/ep/$ep"; ST="$BENCH/state/$ep"; CTR="$ep"
mkdir -p "$EP" "$ST/home" "$ST/extract"
log() { printf '%s %s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$*" | tee -a "$ST/episode.log"; }
die() { log "HARNESS_ERROR $*"; term="HARNESS_ERROR"; finish 1; }
now() { date -u +%s; }
term="UNSET"; t0=$(now)

# ── metadata from the pinned tables (instance id is the only dataset argument) ──────────────────
read -r IMG DIG BASE < <(python3 - "$IID" "$H" <<'PY'
import json,sys
iid,h=sys.argv[1],sys.argv[2]
d=json.load(open(h+"/IMAGE-DIGESTS.json"))["images"][iid]
row=[r for r in json.load(open(h+"/data/verified.json")) if r["instance_id"]==iid][0]
print(d["image"], d["digest"], row["base_commit"])
PY
) || { echo "no metadata for $IID"; exit 1; }
log "EPISODE $ep task=$IID image=$IMG@$DIG base=$BASE"

finish() {
  rc="${1:-0}"
  docker rm -f "$CTR" >/dev/null 2>&1
  t1=$(now)
  python3 - "$ST" "$EP" "$IID" "$ARM" "$IMG" "$DIG" "$BASE" "$term" "$rc" "$t0" "$t1" "$MODEL" "$EFFORT" "$MAX_TURNS" "$WALL_S" "$TOKEN_CEILING" "$H" "$CFG" <<'PY'
import json,sys,hashlib,os,subprocess
(st,ep,iid,arm,img,dig,base,term,rc,t0,t1,model,effort,mt,wall,ceil,h,cfg)=sys.argv[1:]
def sha(p):
    try: return hashlib.sha256(open(p,'rb').read()).hexdigest()
    except Exception: return None
def ver(): 
    try: return subprocess.check_output(["claude","--version"]).decode().strip()
    except Exception: return None
pm={}
try: pm=json.load(open(os.path.join(st,"prompt_meta.json")))
except Exception: pass
m={"episode":os.path.basename(st),"instance_id":iid,"arm":arm,"image":img,"digest":dig,"base_commit":base,
   "termination":term,"claude_exit_code":int(rc),"start_utc":int(t0),"end_utc":int(t1),"wall_s":int(t1)-int(t0),
   "model_requested":model,"effort":effort,"max_turns":int(mt),"wall_ceiling_s":int(wall),"token_ceiling":int(ceil),
   "claude_version":ver(),"host_arch":os.uname().machine,"docker_platform":"linux/amd64",
   "claude_md_sha256":pm.get("claude_md_sha256"),"claude_md_bytes":pm.get("claude_md_bytes"),"arm_block_bytes":pm.get("arm_block_bytes"),
   "prompt_sha256":pm.get("prompt_sha256"),"problem_statement_sha256":pm.get("problem_statement_sha256"),
   "settings_sha256":sha(os.path.join(cfg,"settings.json")),"hook_sha256":sha(os.path.join(h,"hook-deny-network.sh")),
   "model_patch_sha256":sha(os.path.join(st,"model_patch.diff")),
   "model_patch_bytes":(os.path.getsize(os.path.join(st,"model_patch.diff")) if os.path.exists(os.path.join(st,"model_patch.diff")) else None),
   "agent_made_git":os.path.exists(os.path.join(ep,"wc",".git")),
   "flags":["-p <prompt>","--model",model,"--effort",effort,"--max-turns",mt,"--dangerously-skip-permissions","--disallowedTools","WebFetch,WebSearch,Agent,Task","--strict-mcp-config","--setting-sources","user","--output-format","json","--session-id <uuid>"]}
json.dump(m,open(os.path.join(st,"manifest.json"),"w"),indent=1,sort_keys=True)
PY
  log "LANDED $ep task=$IID arm=$ARM term=$term rc=$rc wall=$(( $(now)-t0 ))s metered=$(python3 -c "import json;print(json.load(open('$ST/meter.json'))['metered_sum'])" 2>/dev/null || echo NA)"
  printf '%s\n' "$ep $IID $ARM $term" >> "$BENCH/logs/landings.log"
  exit "$rc"
}

# ── 1. image present and IS the pinned digest ───────────────────────────────────────────────────
docker image inspect "$IMG@$DIG" >/dev/null 2>&1 || die "image $IMG@$DIG not present (pull_pilot.sh first)"
# ── 2. extract /testbed from a fresh container of the pinned image, drop every .git ──────────────
docker rm -f "x-$ep" >/dev/null 2>&1
docker create --platform linux/amd64 --name "x-$ep" "$IMG@$DIG" >/dev/null 2>&1 || die "docker create failed"
docker cp "x-$ep:/testbed" "$ST/extract/" >/dev/null 2>&1 || die "docker cp /testbed failed"
docker rm -f "x-$ep" >/dev/null 2>&1
find "$ST/extract/testbed" -name .git -prune -exec rm -rf {} + 2>/dev/null
find "$ST/extract/testbed" -name packed-refs -exec rm -f {} + 2>/dev/null
mv "$ST/extract/testbed" "$EP/wc" || die "mv wc"
rmdir "$ST/extract" 2>/dev/null
# ── 3. CHECK 2b on the host copy (+ RepoDigests) ────────────────────────────────────────────────
bash "$H/check2b.sh" "$EP/wc" "$DIG" "$IMG" > "$ST/check2b.host.log" 2>&1 || { cat "$ST/check2b.host.log"; die "CHECK2B host FAIL"; }
# ── 4. shadow git (outside the agent's tree; GIT_DIR only in this process) ──────────────────────
SG="$ST/shadow.git"
git --git-dir="$SG" --work-tree="$EP/wc" init -q || die "shadow init"
git --git-dir="$SG" -c user.name=harness -c user.email=harness@bench --work-tree="$EP/wc" add -A || die "shadow add"
git --git-dir="$SG" -c user.name=harness -c user.email=harness@bench --work-tree="$EP/wc" commit -q -m base || die "shadow commit"
git --git-dir="$SG" tag base >/dev/null 2>&1
bash "$H/check2b.sh" "$EP/wc" >/dev/null 2>&1 || die "CHECK2B host FAIL after shadow init (object store reachable)"
# ── 5. prompt + arm file + wrapper; the episode dir holds EXACTLY CLAUDE.md rt wc ────────────────
python3 "$H/build_prompt.py" --instance "$IID" --arm "$ARM" --ep "$EP" --out "$ST" --data "$H/data/verified.json" > /dev/null || die "build_prompt"
sed -e "s|__ST__|$ST|g" -e "s|__CTR__|$CTR|g" "$H/rt.template" > "$EP/rt" && chmod +x "$EP/rt"
[ "$(ls -A "$EP" | sort | tr '\n' ' ')" = "CLAUDE.md rt wc " ] || die "episode dir holds more than CLAUDE.md rt wc: $(ls -A "$EP")"
# ── 6. hermeticity assertions ───────────────────────────────────────────────────────────────────
p="$EP"; while [ "$p" != "/" ]; do p=$(dirname "$p"); [ -e "$p/CLAUDE.md" ] && die "CLAUDE.md above the episode at $p"; done
[ -e "$CFG/CLAUDE.md" ] && die "CLAUDE.md in the config dir"
[ -z "$(find "$CFG/projects" -type d -name memory 2>/dev/null)" ] || die "memory dir in config dir projects/"
want_s=$(grep '^settings.json ' "$H/HASHES.txt" | cut -d' ' -f2); have_s=$(shasum -a 256 "$CFG/settings.json" | cut -d' ' -f1)
[ "$want_s" = "$have_s" ] || die "settings.json sha $have_s != pinned $want_s"
want_h=$(grep '^hook-deny-network.sh ' "$H/HASHES.txt" | cut -d' ' -f2); have_h=$(shasum -a 256 "$H/hook-deny-network.sh" | cut -d' ' -f1)
[ "$want_h" = "$have_h" ] || die "hook sha $have_h != pinned $want_h"
# the arm rendering is pinned in its UN-substituted form (base + arm block, literal __EP__); the per-episode
# CLAUDE.md differs from it only by the episode path — re-render and compare, and record both shas.
want_a=$(grep "^rendered-$ARM(__EP__) " "$H/HASHES.txt" | cut -d' ' -f2); have_a=$(cat "$H/base.md" "$H/arms/$ARM.md" | shasum -a 256 | cut -d' ' -f1)
[ -n "$want_a" ] && [ "$want_a" = "$have_a" ] || die "arm $ARM rendering sha $have_a != pinned '$want_a'"
[ "$(sed "s|$EP|__EP__|g" "$EP/CLAUDE.md" | shasum -a 256 | cut -d' ' -f1)" = "$have_a" ] || die "episode CLAUDE.md is not the pinned rendering with the path substituted"
# ── 7. container: pinned image, NO network, the working copy mounted over /testbed ───────────────
docker run -d --platform linux/amd64 --network none --name "$CTR" -v "$EP/wc:/testbed" -w /testbed "$IMG@$DIG" tail -f /dev/null >/dev/null 2>&1 || die "docker run"
docker exec -i "$CTR" bash -s -- /testbed < "$H/check2b.sh" > "$ST/check2b.container.log" 2>&1 || { cat "$ST/check2b.container.log"; die "CHECK2B container FAIL"; }
docker exec "$CTR" bash -lc 'source /opt/miniconda3/bin/activate testbed >/dev/null 2>&1 || { source /opt/miniconda3/etc/profile.d/conda.sh && conda activate testbed; }; python -c "import sys; print(sys.version.split()[0])"' > "$ST/env_python.txt" 2>&1 || die "conda env testbed not activatable"
log "PREPARED wc=$(du -sh "$EP/wc" | cut -f1) python=$(cat "$ST/env_python.txt") check2b=host+container PASS"
[ "$DRY" = "--dry" ] && { term="DRY"; finish 0; }
# ── 8. run claude, watched ─────────────────────────────────────────────────────────────────────
SID=$(uuidgen | tr 'A-Z' 'a-z')
( cd "$EP/wc" && env -i HOME="$ST/home" CLAUDE_CONFIG_DIR="$CFG" PATH=/usr/bin:/bin:/usr/sbin:/sbin:/opt/homebrew/bin \
    TERM=dumb LANG=en_US.UTF-8 USER="$USER" LOGNAME="$USER" TMPDIR="$ST/home" \
    claude -p "$(cat "$ST/prompt.md")" --model "$MODEL" --effort "$EFFORT" --max-turns "$MAX_TURNS" \
      --dangerously-skip-permissions --disallowedTools "WebFetch,WebSearch,Agent,Task" --strict-mcp-config \
      --setting-sources user --output-format json --session-id "$SID" > "$ST/result.json" 2> "$ST/claude.stderr" ) &
CPID=$!
log "CLAUDE started pid=$CPID session=$SID"
JSONL=""; killed=""
while kill -0 "$CPID" 2>/dev/null; do
  sleep 20
  el=$(( $(now) - t0 ))
  [ -z "$JSONL" ] && JSONL=$(find "$CFG/projects" -name "$SID.jsonl" 2>/dev/null | head -1)
  if [ "$el" -gt "$WALL_S" ]; then killed="WALLCLOCK"; fi
  if [ -n "$JSONL" ] && [ -z "$killed" ]; then
    ms=$(python3 "$H/meter.py" "$JSONL" --live 2>/dev/null | python3 -c "import json,sys; print(json.load(sys.stdin)['metered_sum'])" 2>/dev/null || echo 0)
    [ "${ms:-0}" -ge "$TOKEN_CEILING" ] && killed="TOKEN_CEILING"
  fi
  if [ -n "$killed" ]; then log "WATCHDOG $killed at ${el}s"; kill -TERM "$CPID" 2>/dev/null; sleep 10; kill -KILL "$CPID" 2>/dev/null; break; fi
done
wait "$CPID"; crc=$?
[ -z "$JSONL" ] && JSONL=$(find "$CFG/projects" -name "$SID.jsonl" 2>/dev/null | head -1)
# ── 9. termination, patch, meter, audit, archive ────────────────────────────────────────────────
if [ -n "$killed" ]; then term="$killed"
elif [ -z "$JSONL" ]; then term="HARNESS_ERROR"
else
  sub=$(python3 -c "import json;print(json.load(open('$ST/result.json')).get('subtype',''))" 2>/dev/null)
  case "$sub" in *max_turns*) term="ROUNDS_EXHAUSTED" ;; success) term="DONE" ;; "") term="HARNESS_ERROR" ;; *) term="DONE_$sub" ;; esac
fi
git --git-dir="$SG" -c user.name=harness -c user.email=harness@bench --work-tree="$EP/wc" add -A 2>/dev/null
git --git-dir="$SG" --work-tree="$EP/wc" diff --cached --binary base > "$ST/model_patch.diff" 2>/dev/null
[ -s "$ST/model_patch.diff" ] || { term="${term}+NO_PATCH"; : > "$ST/model_patch.diff"; }
if [ -n "$JSONL" ]; then
  cp "$JSONL" "$ST/session.jsonl"
  bash "$H/hook-deny-network.sh" --pattern > "$ST/network_pattern.txt"
  python3 "$H/meter.py" "$ST/session.jsonl" --result "$ST/result.json" --pattern-file "$ST/network_pattern.txt" > "$ST/meter.json" 2> "$ST/meter.err"
  python3 -c "import json;m=json.load(open('$ST/meter.json'));print('\n'.join(m['network_hits']))" > "$ST/network_audit.txt" 2>/dev/null
  if python3 -c "import json,sys;sys.exit(0 if json.load(open('$ST/meter.json'))['void'] else 1)" 2>/dev/null; then term="VOID(${term})"; fi
  # the config dir carries nothing across episodes but credentials: archive its projects/ subtree, then remove it
  mkdir -p "$ST/configdir-projects" && cp -R "$CFG/projects/." "$ST/configdir-projects/" 2>/dev/null && rm -rf "$CFG/projects"/* 2>/dev/null
fi
[ "$term" = "DONE" ] || [ "$term" = "ROUNDS_EXHAUSTED" ] || [ "${term#VOID}" != "$term" ] || [ "${term#DONE_}" != "$term" ] || [ "${term#*+NO_PATCH}" != "$term" ] || true
finish "$crc"
