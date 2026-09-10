#!/bin/bash
# studio_phase.sh — run FROM THE SEAT BOX: put the full dataset on the Studio for a control/scoring
# phase, or take it (and every gold-bearing harness log) OFF before episodes. episode.sh REFUSES to run
# while the full dataset is present.   usage: studio_phase.sh in|out   env: STUDIO (ssh host)
set -u
STUDIO="${STUDIO:-studio}"; REPO="$(cd "$(dirname "$0")/.." && pwd)"
case "${1:?in|out}" in
  in)  rsync -a "$REPO/data/verified.json" "$STUDIO:~/bench/harness/data/verified.json" && echo "dataset IN" ;;
  out) mkdir -p "$REPO/runs/studio-controls"
       # the exclusion verdict (booleans per id, no gold byte) STAYS on the Studio: the driver and the morning line consume it
       ssh "$STUDIO" 'cp ~/bench/state/controls/controls.json ~/bench/state/controls.json 2>/dev/null; true'
       rsync -a --remove-source-files "$STUDIO:~/bench/state/controls/" "$REPO/runs/studio-controls/" 2>/dev/null
       rsync -a --remove-source-files "$STUDIO:~/bench/state/scoring/" "$REPO/runs/studio-scoring/" 2>/dev/null
       ssh "$STUDIO" 'rm -f ~/bench/harness/data/verified.json; find ~/bench/state/controls ~/bench/state/scoring -type d -empty -delete 2>/dev/null; ls ~/bench/harness/data/; n=$(find ~/bench/state ~/bench/harness -type f -path "*run_evaluation*" 2>/dev/null | wc -l | tr -d " "); echo "gold-bearing files remaining: $n"; [ "$n" = 0 ]' && echo "dataset + gold logs OUT" || { echo "OUT FAILED: gold-bearing files remain on the Studio"; exit 1; } ;;
esac
