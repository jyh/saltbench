#!/bin/bash
# score.sh — batch scoring of one arm's predictions through the pinned official harness.
#   usage: score.sh <arm-id> <run_id>     reads $BENCH/state/predictions-<arm>.jsonl
set -u
BENCH="${BENCH:-$HOME/bench}"; H="${H:-$BENCH/harness}"; PY="${PY:-$BENCH/venv/bin/python}"
ARM="${1:?arm}"; RUN="${2:?run_id}"; P="$BENCH/state/predictions-$ARM.jsonl"
[ -s "$P" ] || { echo "no predictions at $P"; exit 2; }
ids=$(python3 -c "import json;print(' '.join(json.loads(l)['instance_id'] for l in open('$P') if l.strip()))")
OUT="$BENCH/state/scoring"; mkdir -p "$OUT"; cd "$OUT" || exit 1
"$PY" -c "import importlib.metadata as m; assert m.version('swebench')=='4.1.0'" || exit 3
bash "$H/bridge_assert.sh" $ids || exit 4
"$PY" -m swebench.harness.run_evaluation -d "$H/data/verified.json" -s test -i $ids -p "$P" \
   --namespace swebench --instance_image_tag latest --max_workers 1 --timeout 1800 --cache_level instance -id "$RUN" --report_dir "$OUT" 2>&1 | tail -8
ls "$OUT"/*"$RUN"*.json 2>/dev/null
