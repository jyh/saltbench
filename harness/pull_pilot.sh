#!/bin/bash
# pull_pilot.sh — pull the pilot-30 SWE-bench images BY DIGEST (linux/amd64 under Rosetta) and
# apply the pre-registered BRIDGE: tag <image>@<digest> as the harness's instance key <image>:latest.
# Order = TASKLIST.json pilot draw order. Idempotent: an image whose digest is already present is skipped.
set -u
cd ~/bench/images || exit 1
LOG=~/bench/logs/pull.log
python3 - <<'PY' > pilot_pull_list.txt
import json
d=json.load(open('IMAGE-DIGESTS.json'))['images']; p=json.load(open('TASKLIST.json'))['pilot']
for i in p: print(i, d[i]['image'], d[i]['digest'])
PY
n=0; ok=0; fail=0
while read -r iid img dig; do
  n=$((n+1))
  if docker image inspect "$img@$dig" >/dev/null 2>&1; then
    echo "$(date '+%m/%d %H:%M:%S') [$n/30] PRESENT $iid $dig" >> "$LOG"
  else
    echo "$(date '+%m/%d %H:%M:%S') [$n/30] PULL    $iid $img@$dig" >> "$LOG"
    if docker pull --platform linux/amd64 "$img@$dig" >> "$LOG" 2>&1; then
      echo "$(date '+%m/%d %H:%M:%S') [$n/30] PULLED  $iid" >> "$LOG"
    else
      echo "$(date '+%m/%d %H:%M:%S') [$n/30] FAILED  $iid rc=$?" >> "$LOG"; fail=$((fail+1)); continue
    fi
  fi
  # BRIDGE: the pinned harness resolves images by KEY; bind the key to the certified digest.
  docker tag "$img@$dig" "$img:latest" && ok=$((ok+1)) \
    && echo "$(date '+%m/%d %H:%M:%S') [$n/30] BRIDGED $img:latest -> $dig  arch=$(docker image inspect --format '{{.Os}}/{{.Architecture}}' "$img@$dig")" >> "$LOG"
done < pilot_pull_list.txt
echo "$(date '+%m/%d %H:%M:%S') DONE bridged=$ok failed=$fail of $n" >> "$LOG"
