#!/bin/bash
# o90_selftest.sh — the O90 stage-1 amendment's run-shaped dry (desk AEY, 2026-10-23). Runs ON THE RUN BOX, against a
# SCRATCH bench under ~/bench-dry/o90-2026-10-23 (never ~/bench, ~/bench-a8 or the live views), the PINNED harness copied
# there, the real shared Lean project, and a stub client (o90_stub.sh). The kernel check is REAL: stage B is fed amendment 8's
# recorded passing body for problem 31 (a0), so a pass here is the kernel's, not the stub's.
#   usage: bash o90_selftest.sh <harness dir to test> [--mutant M1|M2]      prints one PASS/FAIL line per arm and a summary.
# Arms: R1 a5@C refuses · R2 a6@A refuses · A1 a0/a5 stage A identical prompt + CLAUDE.md · B1 a0@B passes, B.artifact
# written without EXPLAIN · B2 a5@B passes, prompt = prompt_B + prompt_B_pu exactly, EXPLAIN captured beside bodies, absent
# from bodies.json, B.artifact carries it · C1 a6@C gets prior/ = a0's artifact, prompt + prior paragraph · C2 a7@C gets a5's
# artifact incl. EXPLAIN.md · C3 a0@C (C0) has no prior/ and the plain prompt · R3 a tampered artifact refuses (a7@C) ·
# D1 the driver lands NOT_RUN(no_stage_B_artifact) for a6/a7 with no artifact. Added on systems' re-read: B2 feeds a DOCSTRINGED
# helper lemma through the real checker (F5) · C2 asserts a7's prompt · B3 a scored FAILED a0@B supersedes a0's artifact (F4) ·
# H1 the served-model check halts a substituted, haiku-only, empty or missing record and not a clean one (F3, G2) ·
# W1 the driver calls it after the first, hold and retry landings (G1).
# Mutants (red backwards, on a scratch copy only): M1 removes the arm paragraph mapping (B2/C1 must go red);
# M2 removes the EXPLAIN.md capture (B2 must go red). M3 removes the B.artifact supersede (B3 must go red).
# M4 silences the served-model check (H1 must go red). M5 unwires the RETRY site (W1 must go red). M6 stubs the driver's
# served_check body to `return 0` (W2 must go red, W1 and H1 stay green: the hole systems' K2 named).
set -u
SRC="${1:?harness dir}"; MUT="${3:-}"; [ "${2:-}" = "--mutant" ] || MUT=""
R="$HOME/bench-dry/o90-2026-10-23${MUT:+-$MUT}"; A8="$HOME/bench-a8"
[ -d "$A8/state/ep-7813014d" ] || { echo "FATAL: amendment 8's ep-7813014d (B a0 problem_31, passed) is not on this host"; exit 2; }
case "$R" in "$HOME/bench-dry/"*) ;; *) echo "FATAL: scratch root outside ~/bench-dry"; exit 2 ;; esac
[ -e "$R" ] && { echo "FATAL: $R exists; move it aside first (evidence, never deleted by this script)"; exit 2; }
mkdir -p "$R"/bench/logs "$R"/work "$R"/cfg "$R"/stub || exit 2
rsync -a --exclude='s2lean/views/' --exclude='__pycache__/' "$SRC/" "$R/bench/harness/" || exit 2
H="$R/bench/harness"; S2="$H/s2lean"
if [ -n "$MUT" ]; then
  case "$MUT" in
    M1) python3 - "$S2/episode_s2.sh" <<'PY' || exit 2
import sys; p=sys.argv[1]; s=open(p).read(); o='if extra: tmpl=tmpl+open(os.path.join(s2,extra)).read()\n'; assert s.count(o)==1; open(p,'w').write(s.replace(o,''))
PY
    ;;
    M2) python3 - "$S2/episode_s2.sh" <<'PY' || exit 2
import sys; p=sys.argv[1]; s=open(p).read(); o='[ -f "$EP/repo/EXPLAIN.md" ] && cp "$EP/repo/EXPLAIN.md" "$ST/EXPLAIN.md"\n'; assert s.count(o)==1; open(p,'w').write(s.replace(o,''))
PY
    ;;
    M3) python3 - "$S2/episode_s2.sh" <<'PY' || exit 2
import sys; p=sys.argv[1]; s=open(p).read(); o='[ -e "$BA" ] && { rm -rf -- "${ABDIR:?}/B.artifact"; log "B_ARTIFACT superseded'; assert s.count(o)==1; open(p,'w').write(s.replace(o,'[ -e "$BA" ] && { log "B_ARTIFACT superseded'))
PY
    ;;
    M4) python3 - "$S2/served_model_check.py" <<'PY' || exit 2
import sys; p=sys.argv[1]; s=open(p).read(); o='    r = check(m)\n    if r: print(r)'; assert s.count(o)==1; open(p,'w').write(s.replace(o,'    r = check(m)'))
PY
    ;;
    M5) python3 - "$S2/run_s2_stage0.sh" <<'PY' || exit 2
import sys; p=sys.argv[1]; s=open(p).read(); o='| tee -a "$RL"; is_terminal "$term" && served_check "$t" "$arm" ;; esac'; assert s.count(o)==1; open(p,'w').write(s.replace(o,'| tee -a "$RL" ;; esac'))
PY
    ;;
    M6) python3 - "$S2/run_s2_stage0.sh" <<'PY' || exit 2
import sys; p=sys.argv[1]; s=open(p).read(); o='served_check() { [ "$DRY" = "1" ] && return 0'; assert s.count(o)==1; open(p,'w').write(s.replace(o,'served_check() { return 0'))
PY
    ;;
    *) echo "FATAL: unknown mutant $MUT"; exit 2 ;;
  esac
  for f in episode_s2.sh run_s2_stage0.sh served_model_check.py; do ns=$(shasum -a 256 "$S2/$f" | cut -d' ' -f1); sed -i '' "s|^s2lean/$f .*|s2lean/$f $ns|" "$H/HASHES.txt"; done
  echo "MUTANT $MUT applied to the scratch copy (episode_s2.sh re-pinned in the scratch HASHES only)"
fi
cp "$H/settings.s2.json" "$R/cfg/settings.json"; cp "$S2/o90-2026-10-23/o90_stub.sh" "$R/stub/o90_stub.sh"; chmod +x "$R/stub/o90_stub.sh"
# views: B/C need the ground truth (a COPY, so the check's pristine cache writes land in scratch); A must see NONE of it
mkdir -p "$R/views" "$R/viewsA"; for d in "$HOME/bench/s2views"/problem_*; do t=$(basename "$d"); cp -R "$d" "$R/views/$t"; mkdir -p "$R/viewsA/$t"; cp "$d/A.lean" "$d/frozenA.json" "$R/viewsA/$t/"; done
pass=0; fail=0
ok() { echo "PASS $*"; pass=$((pass+1)); }
no() { echo "FAIL $*"; fail=$((fail+1)); }
EPOUT="$R/ep.last"
ep() { # ep <arm> <pid> <stage> <views>: runs one episode; sets erc and writes its EPISODE/REFUSE line to $EPOUT
  printf '%s\n' "$1" | env BENCH="$R/bench" H="$H" VIEWS="$4" CFG="$R/cfg" EPROOT="$R/work" MODEL=claude-opus-5 \
      CLAUDE_BIN="$R/stub/o90_stub.sh" CLAUDE_BIN_STUB=1 bash "$S2/episode_s2.sh" "$2" "$3" > "$R/ep.out" 2>&1; erc=$?
  cat "$R/ep.out" >> "$R/episodes.log"; grep -m1 -E '^EPISODE |REFUSE:' "$R/ep.out" > "$EPOUT"; }
eid() { sed -n 's/^EPISODE //p' "$EPOUT"; }
st() { echo "$R/bench/state/$1"; }
SR="$R/bench/state/s2-dry/problem_31"
# R1 / R2: arm-stage pairs that must refuse
ep a5 31 C "$R/views"; o=$(cat "$EPOUT"); if [ "$erc" = 4 ] && case "$o" in *"does not run stage C"*) true;; *) false;; esac; then ok "R1 a5@C refused rc 4"; else no "R1 rc=$erc ($o)"; fi
ep a6 31 A "$R/viewsA"; o=$(cat "$EPOUT"); if [ "$erc" = 4 ] && case "$o" in *"does not run stage A"*) true;; *) false;; esac; then ok "R2 a6@A refused rc 4"; else no "R2 rc=$erc ($o)"; fi
# A1: stage A, both arms, same prompt and CLAUDE.md
ep a0 31 A "$R/viewsA"; ea0=$(eid); ep a5 31 A "$R/viewsA"; ea5=$(eid)
if [ -n "$ea0" ] && [ -n "$ea5" ]; then
  p0=$(python3 -c "import json;print(json.load(open('$(st $ea0)/prompt_meta.json'))['prompt_sha256_canonical'])"); p5=$(python3 -c "import json;print(json.load(open('$(st $ea5)/prompt_meta.json'))['prompt_sha256_canonical'])")
  c0=$(python3 -c "import json;print(json.load(open('$(st $ea0)/manifest.json'))['arm_rendering_sha256'])"); c5=$(python3 -c "import json;print(json.load(open('$(st $ea5)/manifest.json'))['arm_rendering_sha256'])")
  if [ "$p0" = "$p5" ] && [ "$c0" = "$c5" ]; then ok "A1 stage A: a0/a5 canonical prompt ${p0:0:12} and arm rendering ${c0:0:12} identical"; else no "A1 prompt $p0/$p5 rendering $c0/$c5"; fi
else no "A1 stage-A episodes did not start ($ea0/$ea5)"; fi
# B: seed BOTH arms' A.bodies from amendment 8's scored a0 stage A (same generated_spec), feed A8's passing B body
mkdir -p "$SR/a0" "$SR/a5"; cp "$A8/state/s2/problem_31/a0/A.bodies.json" "$SR/a0/A.bodies.json"; cp "$A8/state/s2/problem_31/a0/A.bodies.json" "$SR/a5/A.bodies.json"
python3 -c "import json;b=json.load(open('$A8/state/ep-7813014d/bodies.json'));json.dump({k:v for k,v in b.items() if not k.startswith('_')},open('$R/stub/stub-bodies.json','w'))"
ep a0 31 B "$R/views"; eb0=$(eid)
python3 -c "import json;p='$R/stub/stub-bodies.json';b=json.load(open(p));b['iso_helper_lemmas']=(b.get('iso_helper_lemmas') or '')+'\n/-- States that True holds. -/\ntheorem o90_docstring_probe : True := trivial\n';json.dump(b,open(p,'w'))"
printf '# EXPLAIN (stub)\nThe theorem `spec_isomorphism` states that for every implementation, problem_spec holds iff generated_spec holds.\n' > "$R/stub/stub-EXPLAIN.md"
ep a5 31 B "$R/views"; eb5=$(eid)
mkdir -p "$R/stub-used"; mv "$R/stub/stub-bodies.json" "$R/stub/stub-EXPLAIN.md" "$R/stub-used/"
pb0=$(python3 -c "import json;print(json.load(open('$(st $eb0)/manifest.json'))['passed'])" 2>/dev/null)
if [ "$pb0" = True ] && [ -s "$SR/a0/B.artifact/stageB.lean" ] && [ ! -e "$SR/a0/B.artifact/EXPLAIN.md" ] && cmp -s "$SR/a0/B.artifact/stageB.lean" "$(st $eb0)/canonical.lean" \
  && cmp -s "$(st $eb0)/prompt.md" <(sed "s|__EP__|$R/work/$eb0|g" "$S2/prompt_B.md"); then
  ok "B1 a0@B passed (kernel), B.artifact = its canonical.lean, no EXPLAIN, prompt = prompt_B.md"; else no "B1 passed=$pb0 artifact/prompt (ep $eb0)"; fi
pb5=$(python3 -c "import json;print(json.load(open('$(st $eb5)/manifest.json'))['passed'])" 2>/dev/null)
xs=$(python3 -c "import json;print(json.load(open('$(st $eb5)/manifest.json')).get('explain_sha256'))" 2>/dev/null)
b2=""; [ "$pb5" = True ] || b2="$b2 not-passed"
cmp -s "$(st $eb5)/prompt.md" <(cat "$S2/prompt_B.md" "$S2/prompt_B_pu.md" | sed "s|__EP__|$R/work/$eb5|g") || b2="$b2 prompt"
{ [ -s "$(st $eb5)/EXPLAIN.md" ] && [ "$xs" = "$(shasum -a 256 "$(st $eb5)/EXPLAIN.md" | cut -d' ' -f1)" ]; } || b2="$b2 explain-capture"
grep -q 'EXPLAIN (stub)' "$(st $eb5)/bodies.json" && b2="$b2 explain-in-bodies"
grep -q 'o90_docstring_probe' "$(st $eb5)/bodies.json" || b2="$b2 docstring-helper-not-in-bodies"
cmp -s "$SR/a5/B.artifact/EXPLAIN.md" "$(st $eb5)/EXPLAIN.md" || b2="$b2 artifact-explain"
if [ -z "$b2" ]; then ok "B2 a5@B passed (kernel) WITH a docstringed helper lemma in its body, prompt = prompt_B + prompt_B_pu, EXPLAIN.md captured (${xs:0:12}), not in bodies.json, in B.artifact"; else no "B2:$b2 (ep $eb5)"; fi
# C: U3 arms
ep a6 31 C "$R/views"; ec6=$(eid); ep a7 31 C "$R/views"; ec7=$(eid); ep a0 31 C "$R/views"; ec0=$(eid)
c1=""; cmp -s "$(st $ec6)/eptree/repo/prior/stageB.lean" "$SR/a0/B.artifact/stageB.lean" || c1="$c1 prior"
[ -e "$(st $ec6)/eptree/repo/prior/EXPLAIN.md" ] && c1="$c1 unexpected-explain"
[ "$(python3 -c "import json;print(json.load(open('$(st $ec6)/manifest.json'))['prior']['b_episode'])" 2>/dev/null)" = "$eb0" ] || c1="$c1 provenance"
cmp -s "$(st $ec6)/prompt.md" <(cat "$S2/prompt_C.md" "$S2/prompt_C_prior.md" | sed "s|__EP__|$R/work/$ec6|g") || c1="$c1 prompt"
if [ -z "$c1" ]; then ok "C1 a6@C: prior/stageB.lean = a0's artifact (b_episode $eb0), prompt = prompt_C + prompt_C_prior"; else no "C1:$c1 (ep $ec6)"; fi
c2=""; cmp -s "$(st $ec7)/eptree/repo/prior/EXPLAIN.md" "$SR/a5/B.artifact/EXPLAIN.md" || c2="$c2 explain"
[ "$(python3 -c "import json;print(json.load(open('$(st $ec7)/manifest.json'))['prior']['b_episode'])" 2>/dev/null)" = "$eb5" ] || c2="$c2 provenance"
cmp -s "$(st $ec7)/prompt.md" <(cat "$S2/prompt_C.md" "$S2/prompt_C_prior.md" | sed "s|__EP__|$R/work/$ec7|g") || c2="$c2 prompt"
if [ -z "$c2" ]; then ok "C2 a7@C: prior/ = a5's artifact incl. EXPLAIN.md (b_episode $eb5), prompt = prompt_C + prompt_C_prior"; else no "C2:$c2 (ep $ec7)"; fi
c3=""; [ -e "$(st $ec0)/eptree/repo/prior" ] && c3="$c3 prior-present"
cmp -s "$(st $ec0)/prompt.md" <(sed "s|__EP__|$R/work/$ec0|g" "$S2/prompt_C.md") || c3="$c3 prompt"
[ "$(python3 -c "import json;print(json.load(open('$(st $ec0)/manifest.json'))['prior'])" 2>/dev/null)" = None ] || c3="$c3 manifest-prior"
if [ -z "$c3" ]; then ok "C3 a0@C (C0): no prior/, prompt = prompt_C.md, manifest prior=None"; else no "C3:$c3 (ep $ec0)"; fi
# R3: a tampered artifact refuses at preparation (HARNESS_ERROR prior provenance), and is restored after
cp "$SR/a5/B.artifact/stageB.lean" "$R/stageB.keep"; printf '\n-- tampered\n' >> "$SR/a5/B.artifact/stageB.lean"
ep a7 31 C "$R/views"; er=$(eid); cp "$R/stageB.keep" "$SR/a5/B.artifact/stageB.lean"
tr3=$(python3 -c "import json;print(json.load(open('$(st $er)/manifest.json'))['termination'])" 2>/dev/null)
case "$tr3" in *HARNESS_ERROR*) if grep -q 'prior provenance' "$(st $er)/episode.log"; then ok "R3 tampered artifact: $tr3, 'prior provenance' in the log"; else no "R3 term $tr3 without the reason"; fi ;; *) no "R3 tampered artifact ran: term=$tr3";; esac
# B3 (F4): a SCORED, FAILED a0@B (the base stub's wrong proof) supersedes a0's artifact
[ -s "$SR/a0/B.artifact/B.artifact.json" ] || no "B3 precondition: no a0 artifact to supersede"
ep a0 31 B "$R/views"; eb3=$(eid)
pb3=$(python3 -c "import json;m=json.load(open('$(st $eb3)/manifest.json'));print(m['passed'],m['termination'])" 2>/dev/null)
if [ ! -e "$SR/a0/B.artifact" ] && grep -q 'B_ARTIFACT superseded' "$(st $eb3)/episode.log"; then ok "B3 a scored failed a0@B ($pb3) removed a0's B.artifact, logged"; else no "B3 artifact still present after a scored fail ($pb3, ep $eb3)"; fi
# H1 (F3, G2): the served-model check tool: its own selftest, then a clean manifest silent and four bad ones halting
hs=$(python3 "$S2/served_model_check.py" --selftest 2>&1); mkdir -p "$R/h1"; h1=""
for c in 'clean:{"model_requested":"claude-opus-5","calls":9,"models":{"claude-opus-5":8,"claude-haiku-4-5":1}}:0' \
         'substituted:{"model_requested":"claude-opus-5","calls":9,"models":{"claude-sonnet-5":8}}:1' \
         'haiku_only:{"model_requested":"claude-opus-5","calls":9,"models":{"claude-haiku-4-5":9}}:1' \
         'empty:{"model_requested":"claude-opus-5","calls":9,"models":{}}:1' 'missing:{"model_requested":"claude-opus-5","calls":9}:1'; do
  nm="${c%%:*}"; rest="${c#*:}"; js="${rest%:*}"; want="${rest##*:}"; printf '%s' "$js" > "$R/h1/$nm.json"
  out=$(python3 "$S2/served_model_check.py" "$R/h1/$nm.json" 2>&1); got=0; [ -n "$out" ] && got=1; [ "$got" = "$want" ] || h1="$h1 $nm"; done
if printf '%s\n' "$hs" | grep -qE '^SELFTEST PASS \([0-9]+ cases\)$' && [ -z "$h1" ]; then ok "H1 served-model check: $hs; clean silent; substituted, haiku-only, empty, missing all halt"; else no "H1 selftest='$hs' wrong:$h1"; fi
# W1 (G1): the driver calls the check after EVERY run_one landing — first run, HOLD re-run, RETRY re-run (structural: the
# check is off under DRY_RUN, so the wiring is read from the driver's text, three named sites)
w1=""; for site in 'LANDED #$n $t $STAGE arm=$arm term=$term" | tee -a "$RL"; is_terminal "$term" && served_check' 'LANDED(hold) #$n $t $STAGE arm=$arm term=$term" | tee -a "$RL"; is_terminal "$term" && served_check' 'LANDED(retry) #$n $t $STAGE arm=$arm term=$term" | tee -a "$RL"; is_terminal "$term" && served_check'; do
  grep -qF -- "$site" "$S2/run_s2_stage0.sh" || w1="$w1 [${site%%#*}]"; done
if [ -z "$w1" ] && grep -qF 'python3 "$H/s2lean/served_model_check.py"' "$S2/run_s2_stage0.sh"; then ok "W1 driver: served_check after the first, hold and retry landings (3 of 3 sites)"; else no "W1 unwired:$w1"; fi
# W2 (K2): the driver's OWN served_check body, extracted verbatim with is_terminal and stamp, run with DRY unset on fixture
# landings: a substituted model exits 4 and writes HALT · a clean one returns 0 · a QUOTA landing with no transcript, behind the
# call site's own is_terminal gate (K1), returns 0 and writes no HALT
mkdir -p "$R/w2"; awk '/^stamp\(\) \{/{print} /^is_terminal\(\) \{/{print} /^served_check\(\) \{/{f=1} f{print} f&&/; \}$/{f=0}' "$S2/run_s2_stage0.sh" > "$R/w2/fns.sh"
w2=""; for c in 'substituted|{"model_requested":"claude-opus-5","calls":9,"models":{"claude-sonnet-5":8}}|DONE|4|halt' \
               'clean|{"model_requested":"claude-opus-5","calls":9,"models":{"claude-opus-5":8}}|DONE|0|nohalt' \
               'quota_nojsonl|{"model_requested":"claude-opus-5","calls":null,"models":null}|QUOTA(429)|0|nohalt'; do
  IFS='|' read -r nm js tm want hw <<<"$c"; B="$R/w2/$nm"; mkdir -p "$B/state/ep-w2$nm" "$B/logs"; printf '%s' "$js" > "$B/state/ep-w2$nm/manifest.json"
  printf 'ep-w2%s problem_31 B a0 %s 0\n' "$nm" "$tm" > "$B/logs/l.log"
  ( DRY=""; BENCH="$B"; H="$H"; STAGE=B; L="$B/logs/l.log"; RL="$B/logs/rl.log"; term="$tm"; t=problem_31; arm=a0
    . "$R/w2/fns.sh"; is_terminal "$term" && served_check "$t" "$arm"; exit 0 ) > /dev/null 2>&1; got=$?
  hal=nohalt; [ -f "$B/HALT" ] && hal=halt; [ "$got" = "$want" ] && [ "$hal" = "$hw" ] || w2="$w2 $nm(rc=$got,$hal)"; done
if [ -s "$R/w2/fns.sh" ] && grep -q '^served_check()' "$R/w2/fns.sh" && [ -z "$w2" ]; then ok "W2 the driver's served_check body: substituted rc 4 + HALT · clean 0 · QUOTA with no transcript 0, no HALT (K1)"; else no "W2:$w2 (fns $(wc -l < "$R/w2/fns.sh") lines)"; fi
# D1: the driver, no artifact for problem 82 in either source arm
(cd "$R" && env BENCH="$R/bench" H="$H" EPROOT="$R/work" DRY_RUN=1 CLAUDE_BIN="$R/stub/o90_stub.sh" CLAUDE_BIN_STUB=1 ARMS="a6 a7" ONLY_IDS=82 CAFFEINATED=1 bash "$S2/run_s2_stage0.sh" C 30 > "$R/driver.out" 2>&1)
if grep -q '^<none> problem_82 C a6 NOT_RUN(no_stage_B_artifact) 0$' "$R/bench/logs/dryexec.log" && grep -q '^<none> problem_82 C a7 NOT_RUN(no_stage_B_artifact) 0$' "$R/bench/logs/dryexec.log"; then
  ok "D1 driver: a6/a7 on problem_82 land NOT_RUN(no_stage_B_artifact)"; else no "D1 driver"; tail -5 "$R/driver.out"; fi
echo "SUMMARY o90_selftest${MUT:+ MUTANT $MUT}: $pass PASS, $fail FAIL  (scratch $R; episodes.log there)"
[ "$fail" = 0 ]
