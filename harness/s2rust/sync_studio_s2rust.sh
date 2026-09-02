#!/bin/bash
# sync_studio_s2rust.sh — put the harness on the Studio UNDER ITS OWN ROOT, for the S2-Rust regime.
# Run FROM THE SEAT.   env: STUDIO (ssh host) · RROOT (the Studio-side root, default ~/bench-rust)
#
# ⛔⛔ WHY THIS EXISTS INSTEAD OF `sync_studio.sh`. That tool writes `~/bench/harness` — which on the Studio is
# THE ONLY HARNESS: `~/bench-c/harness` and `~/bench-aw/harness` are SYMLINKS to it, and it is frozen at the
# stage-C freeze commit `15cfdc2` whose 09/02 dispatch window is still open. Running it now would replace the
# harness a pending, already-authorized run is frozen against, in order to add a wave that has not started.
#   ⇒ THE 08/31 LAW "A NEW REGIME GETS A NEW STATE ROOT" BOUGHT ISOLATION FOR STATE AND NEVER FOR THE HARNESS.
#     This is the harness half, and it is why S2-Rust gets a REAL harness directory of its own rather than
#     another symlink into the shared one.
#
# 📌 I nearly justified this with a false precedent. My first probe printed "REAL DIR" for `~/bench-a8/harness`
# and I read that as "a per-root harness is already established practice" — but the probe was
# `readlink X || echo "REAL DIR"`, which prints the same thing for a path that DOES NOT EXIST, and a8 has no
# harness entry at all. Re-measured with an explicit -L/-d/-e classification: there is still exactly ONE
# harness on that machine.
#   ⇒ A PROBE WHOSE FALLBACK BRANCH MEANS TWO DIFFERENT THINGS IS NOT A MEASUREMENT.
#
# The receipt is CONTENT, not rsync's exit code (the 08/30 law, paid for by `ship A`'s silent hang): the whole
# tree is compared by set-hash, and `~/bench/harness` is asserted BYTE-UNCHANGED afterwards — the assertion is
# the point of the script, not a courtesy.
#
# usage: sync_studio_s2rust.sh [--verify]
set -u
STUDIO="${STUDIO:-kriterion-lan}"; RROOT="${RROOT:-/Users/jyh/bench-rust}"
SSH="ssh -o ConnectTimeout=10"
REPO="$(cd "$(dirname "$0")/../.." && pwd)"
VERIFY_ONLY=0; [ "${1:-}" = "--verify" ] && VERIFY_ONLY=1

fail(){ echo "SYNC REFUSE: $*" >&2; exit 3; }
# only a COMMITTED harness may reach the Studio
[ -z "$(git -C "$REPO" status --porcelain harness/)" ] || fail "harness/ has uncommitted changes — commit first"

# ⛔ the frozen harness's fingerprint is taken BEFORE and compared AFTER. Intending not to touch it is not the
# same as showing it was not touched.
TREEHASH='find . -type f -not -name "*.pyc" -print0 | xargs -0 shasum -a 256 | sed "s| \./| |" | sort | shasum -a 256 | cut -d" " -f1'
before=$($SSH "$STUDIO" "cd ~/bench/harness && $TREEHASH")
[ -n "$before" ] || fail "cannot fingerprint ~/bench/harness on $STUDIO"

if [ "$VERIFY_ONLY" = 0 ]; then
  $SSH "$STUDIO" "mkdir -p $RROOT/harness $RROOT/logs $RROOT/state" || fail "mkdir"
  $SSH "$STUDIO" "[ ! -L $RROOT/harness ]" || fail "$RROOT/harness is a SYMLINK — that is the defect this script exists to avoid"
  git -C "$REPO" rev-parse HEAD > "$REPO/harness/FREEZE-COMMIT"
  rsync -a --delete --exclude='__pycache__/' --exclude='.DS_Store' --exclude='s2lean/views/' \
        -e "$SSH" "$REPO/harness/" "$STUDIO:$RROOT/harness/" || { rm -f "$REPO/harness/FREEZE-COMMIT"; fail "rsync"; }
  rm -f "$REPO/harness/FREEZE-COMMIT"
fi

echo "== receipt: CONTENT, both ends =="
local_h=$(cd "$REPO/harness" && eval "$TREEHASH")
remote_h=$($SSH "$STUDIO" "cd $RROOT/harness && $TREEHASH")
# the seat's tree carries FREEZE-COMMIT only during the copy, so compare the PINNED files rather than the raw
# tree hash: every key in HASHES.txt must resolve to the same sha on the Studio.
rc=0; n=0; bad=0
while read -r key want; do
  case "$key" in s2rust/*|s2lean/*|'#'*) ;; *) continue ;; esac
  case "$key" in *.json|*.py|*.sh|*.sb|*.md|*.lean|*rt.template) ;; *) continue ;; esac
  have=$($SSH "$STUDIO" "shasum -a 256 '$RROOT/harness/$key' 2>/dev/null | cut -d' ' -f1")
  n=$((n+1)); [ "$want" = "$have" ] || { echo "  DRIFT $key studio=${have:0:16} pinned=${want:0:16}"; bad=$((bad+1)); rc=2; }
done < <(awk '!/^#/ && NF==2 {print $1, $2}' "$REPO/harness/HASHES.txt")
echo "  pinned files checked on the Studio: $n, drifted: $bad"

after=$($SSH "$STUDIO" "cd ~/bench/harness && $TREEHASH")
if [ "$before" = "$after" ]; then echo "  OK    ~/bench/harness BYTE-UNCHANGED (${before:0:16}) — stage C's freeze intact"
else echo "  FAIL  ~/bench/harness MOVED: ${before:0:16} -> ${after:0:16}"; rc=2; fi
fz=$($SSH "$STUDIO" "cat ~/bench/harness/FREEZE-COMMIT 2>/dev/null")
echo "  stage-C freeze commit on the Studio: ${fz:-<none>}"
ngt=$($SSH "$STUDIO" "find $RROOT/harness -name 'gt' -o -name 'tasks.jsonl' 2>/dev/null | wc -l | tr -d ' '")
[ "$ngt" = "0" ] && echo "  OK    no ground-truth carrier under $RROOT/harness" || { echo "  FAIL  $ngt ground-truth carrier(s) under $RROOT/harness"; rc=2; }

[ "$rc" = 0 ] && echo "SYNC OK ($RROOT)" || echo "SYNC FAILED (rc=$rc)"
exit $rc
