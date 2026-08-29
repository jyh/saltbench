#!/bin/bash
# stage_views.sh — run FROM THE SEAT. `gen` regenerates harness/s2lean/views from the pinned CLEVER clone;
# `ship A` puts ONLY the stage-A views + frozenA.json on the Studio and REMOVES any frozen.json/C.lean there
# (--delete-excluded: an extended draw can re-enter stage A — refuter MT-R1); `ship BC` adds frozen.json FIRST and C.lean
# SECOND (two rsyncs, so an interrupted ship never leaves C.lean without its frozen.json — GT-7) and only after the
# Studio's stage-A driver has printed DONE (FORCE_BC=1 overrides, loudly); `check` prints what the WHOLE of ~/bench holds
# (GT-2: the harness mirror must carry no views — sync_studio.sh excludes s2lean/views/; this is the ONLY route for views).
set -u
STUDIO="${STUDIO:-kriterion-lan}"; REPO="$(cd "$(dirname "$0")/../.." && pwd)"; V="$REPO/harness/s2lean/views"
SSH="ssh -o ConnectTimeout=10"
case "${1:?gen|ship A|ship BC|check}" in
  gen) CL="${2:?path to clever clone src/lean4}"; rm -rf "$V"; python3 "$REPO/harness/s2lean/build_views.py" "$CL" "$V" && ls "$V" | wc -l ;;
  ship) case "${2:?A|BC}" in
    A)  rsync -a --delete --delete-excluded -e "$SSH" --include='*/' --include='A.lean' --include='frozenA.json' --exclude='*' "$V/" "$STUDIO:~/bench/s2views/" || exit 1
        $SSH "$STUDIO" 'echo "gt files under ~/bench (must be 0): $(find ~/bench \( -name frozen.json -o -name C.lean \) 2>/dev/null | wc -l | tr -d " ")"; echo "problem dirs: $(ls ~/bench/s2views | wc -l | tr -d " ")"' ;;
    BC) if [ "${FORCE_BC:-}" != "1" ]; then
          $SSH "$STUDIO" 'grep -q "S2 STAGE A DRIVER DONE" ~/bench/logs/run_s2_stage0.log 2>/dev/null' || { echo "REFUSE: the Studio's stage-A driver has not printed DONE (FORCE_BC=1 to override)"; exit 3; }
        else echo "WARNING FORCE_BC=1: shipping ground truth without the stage-A DONE line"; fi
        rsync -a -e "$SSH" --include='*/' --include='frozen.json' --exclude='*' "$V/" "$STUDIO:~/bench/s2views/" || exit 1
        rsync -a -e "$SSH" --include='*/' --include='C.lean' --exclude='*' "$V/" "$STUDIO:~/bench/s2views/" || exit 1
        $SSH "$STUDIO" 'echo "frozen=$(find ~/bench/s2views -name frozen.json | wc -l | tr -d " ") C=$(find ~/bench/s2views -name C.lean | wc -l | tr -d " ")"' ;;
    esac ;;
  check) $SSH "$STUDIO" 'echo "s2views: A=$(find ~/bench/s2views -name A.lean | wc -l | tr -d " ") frozenA=$(find ~/bench/s2views -name frozenA.json | wc -l | tr -d " ") frozen=$(find ~/bench/s2views -name frozen.json | wc -l | tr -d " ") C=$(find ~/bench/s2views -name C.lean | wc -l | tr -d " ")"; echo "gt files anywhere under ~/bench: $(find ~/bench \( -name frozen.json -o -name C.lean \) 2>/dev/null | wc -l | tr -d " ")"; echo "harness/s2lean/views on the Studio: $(ls ~/bench/harness/s2lean/views 2>/dev/null | wc -l | tr -d " ") entries (must be 0)"' ;;
  *) echo "usage: stage_views.sh gen <clone src/lean4> | ship A | ship BC | check"; exit 2 ;;
esac
