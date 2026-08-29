#!/bin/bash
# sync_studio.sh — run FROM THE SEAT: mirror harness/ (+ the two pinned tables) to the Studio. --delete on the
# harness tree is deliberate (a stale script on the Studio is the thing this prevents); the tables are copied
# AFTER it because they live at the repo root, not under harness/. Prints the Studio-side shas of the files the
# agent's run depends on, for the sync receipt.   env: STUDIO (ssh host)
# REPAIR ROUND 1 (D3, refuter GT-2/NF2/FN-3/MT-R1): harness/s2lean/views/ is EXCLUDED — the ground truth (frozen.json,
# C.lean) reaches the Studio ONLY through stage_views.sh, after every stage-A landing; the sync asserts no view file
# exists anywhere under ~/bench/harness afterwards. The receipt covers the S2 pinned files too (FN-10).
set -u
STUDIO="${STUDIO:-kriterion-lan}"; REPO="$(cd "$(dirname "$0")/.." && pwd)"
SSH="ssh -o ConnectTimeout=10"
# only a COMMITTED harness may reach the Studio (refuter RI3-R4): refuse a dirty tree, and name the commit the copy came from
if [ -n "$(git -C "$REPO" status --porcelain harness/ TASKLIST.json IMAGE-DIGESTS.json)" ]; then echo "REFUSE: harness/ (or a table) has uncommitted changes — commit first, then sync"; exit 3; fi
git -C "$REPO" diff --quiet HEAD -- harness/HASHES.txt || { echo "REFUSE: HASHES.txt differs from HEAD"; exit 3; }
git -C "$REPO" rev-parse HEAD > "$REPO/harness/FREEZE-COMMIT"
$SSH "$STUDIO" 'rm -rf ~/bench/harness/s2lean/views' 2>/dev/null   # purge: the exclude below protects a STALE views dir from --delete (EDH-4)
rsync -a --delete --exclude='s2lean/views/' --exclude='__pycache__/' --exclude='.DS_Store' -e "$SSH" "$REPO/harness/" "$STUDIO:~/bench/harness/" || exit 1
rm -f "$REPO/harness/FREEZE-COMMIT"
rsync -a -e "$SSH" "$REPO/TASKLIST.json" "$REPO/IMAGE-DIGESTS.json" "$STUDIO:~/bench/harness/" || exit 1
# receipt: the Studio-side shas of the files the run depends on must EQUAL the pinned ones (refuter RI-2; FN-10 for S2)
for f in episode.sh hook-deny-network.sh settings.bench.json settings.s2.json meter.py build_prompt.py \
         s2lean/episode_s2.sh s2lean/check.py s2lean/extract.py s2lean/assemble.py s2lean/screen.py s2lean/s2audit.lean s2lean/sandbox_check.sb s2lean/rt.template s2lean/run_s2_stage0.sh s2lean/smoke_s2.sh \
         leanproj-lakefile leanproj-manifest leanproj-toolchain draw-30; do
  want=$(grep "^$f " "$REPO/harness/HASHES.txt" | head -1 | cut -d' ' -f2)   # head -1: a table with a duplicate line must not make want a two-line string (P2C2-01)
  [ -n "$want" ] || { echo "SYNC MISSING-PIN $f (not in HASHES.txt — run hashes.sh with CLEVER_SRC set first)"; exit 2; }
  case "$f" in leanproj-*|draw-30) echo "SYNC PIN  $f ${want:0:16} (a pin line, not a shipped file — presence asserted)"; continue ;; esac
  have=$($SSH "$STUDIO" "shasum -a 256 ~/bench/harness/$f 2>/dev/null | cut -d' ' -f1")
  [ "$want" = "$have" ] && echo "SYNC OK   $f ${have:0:16}" || { echo "SYNC DRIFT $f studio=${have:0:16} pinned=${want:0:16}"; exit 2; }
done
ngt=$($SSH "$STUDIO" 'find ~/bench/harness \( -name frozen.json -o -name C.lean -o -name A.lean \) 2>/dev/null | wc -l | tr -d " "')
[ "$ngt" = "0" ] && echo "SYNC OK   no view files under ~/bench/harness" || { echo "SYNC FAIL $ngt view files under ~/bench/harness (views must travel by stage_views.sh only)"; exit 2; }
$SSH "$STUDIO" 'ls ~/bench/harness/data/ 2>/dev/null; echo "freeze-commit on Studio: $(cat ~/bench/harness/FREEZE-COMMIT)"'
