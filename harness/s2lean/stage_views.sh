#!/bin/bash
# stage_views.sh — run FROM THE SEAT. `gen` regenerates harness/s2lean/views from the pinned CLEVER clone;
# `ship A` puts ONLY the stage-A views + frozenA.json on the Studio (no ground truth on the host while stage A runs);
# `ship BC` adds frozen.json + C.lean after every stage-A landing; `check` prints what the Studio holds.
set -u
STUDIO="${STUDIO:-kriterion-lan}"; REPO="$(cd "$(dirname "$0")/../.." && pwd)"; V="$REPO/harness/s2lean/views"
case "${1:?gen|ship A|ship BC|check}" in
  gen) CL="${2:?path to clever clone src/lean4}"; rm -rf "$V"; python3 "$REPO/harness/s2lean/build_views.py" "$CL" "$V" && ls "$V" | wc -l ;;
  ship) case "${2:?A|BC}" in
    A)  rsync -a --delete -e "ssh -o ConnectTimeout=10" --include='*/' --include='A.lean' --include='frozenA.json' --exclude='*' "$V/" "$STUDIO:~/bench/s2views/" && ssh "$STUDIO" 'find ~/bench/s2views -name frozen.json -o -name C.lean | wc -l; ls ~/bench/s2views | wc -l' ;;
    BC) rsync -a -e "ssh -o ConnectTimeout=10" --include='*/' --include='frozen.json' --include='C.lean' --exclude='*' "$V/" "$STUDIO:~/bench/s2views/" && ssh "$STUDIO" 'find ~/bench/s2views -name frozen.json | wc -l' ;;
    esac ;;
  check) ssh "$STUDIO" 'echo A=$(find ~/bench/s2views -name A.lean | wc -l) frozenA=$(find ~/bench/s2views -name frozenA.json | wc -l) frozen=$(find ~/bench/s2views -name frozen.json | wc -l) C=$(find ~/bench/s2views -name C.lean | wc -l)' ;;
esac
