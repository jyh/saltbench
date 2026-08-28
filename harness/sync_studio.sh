#!/bin/bash
# sync_studio.sh — run FROM THE SEAT: mirror harness/ (+ the two pinned tables) to the Studio. --delete on the
# harness tree is deliberate (a stale script on the Studio is the thing this prevents); the tables are copied
# AFTER it because they live at the repo root, not under harness/. Prints the Studio-side shas of the two
# files the agent's run depends on, for the sync receipt.   env: STUDIO (ssh host)
set -u
STUDIO="${STUDIO:-kriterion-lan}"; REPO="$(cd "$(dirname "$0")/.." && pwd)"
rsync -a --delete -e "ssh -o ConnectTimeout=10" "$REPO/harness/" "$STUDIO:~/bench/harness/" || exit 1
rsync -a -e "ssh -o ConnectTimeout=10" "$REPO/TASKLIST.json" "$REPO/IMAGE-DIGESTS.json" "$STUDIO:~/bench/harness/" || exit 1
# receipt: the Studio-side shas of the files the run depends on must EQUAL the pinned ones (refuter RI-2)
for f in episode.sh hook-deny-network.sh settings.bench.json meter.py build_prompt.py; do
  want=$(grep "^$f " "$REPO/harness/HASHES.txt" | cut -d' ' -f2)
  have=$(ssh -o ConnectTimeout=10 "$STUDIO" "shasum -a 256 ~/bench/harness/$f | cut -d' ' -f1")
  [ "$want" = "$have" ] && echo "SYNC OK   $f ${have:0:16}" || { echo "SYNC DRIFT $f studio=${have:0:16} pinned=${want:0:16}"; exit 2; }
done
ssh -o ConnectTimeout=10 "$STUDIO" 'ls ~/bench/harness/data/'

