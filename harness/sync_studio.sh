#!/bin/bash
# sync_studio.sh — run FROM THE SEAT: mirror harness/ (+ the two pinned tables) to the Studio. --delete on the
# harness tree is deliberate (a stale script on the Studio is the thing this prevents); the tables are copied
# AFTER it because they live at the repo root, not under harness/. Prints the Studio-side shas of the two
# files the agent's run depends on, for the sync receipt.   env: STUDIO (ssh host)
set -u
STUDIO="${STUDIO:-kriterion-lan}"; REPO="$(cd "$(dirname "$0")/.." && pwd)"
rsync -a --delete -e "ssh -o ConnectTimeout=10" "$REPO/harness/" "$STUDIO:~/bench/harness/" || exit 1
rsync -a -e "ssh -o ConnectTimeout=10" "$REPO/TASKLIST.json" "$REPO/IMAGE-DIGESTS.json" "$STUDIO:~/bench/harness/" || exit 1
ssh -o ConnectTimeout=10 "$STUDIO" 'bash -lc "cd ~/bench/harness && shasum -a 256 settings.bench.json hook-deny-network.sh episode.sh HASHES.txt | cut -c1-16 | tr \"\\n\" \" \"; echo; ls data/"'
