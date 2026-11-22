#!/bin/bash
# ta-tnames.sh <export-dir> <block-T sections dir> <out-dir> — tnames v2 over block TA's 36 plain cells, on the run box.
#   Re-derives the six Statement sections from the export (t-sections.py, block T's) and cmps them with block T's; then runs tnames.sh
#   (beside this file) over each plain cell under $HOME/cells-ta-<problem>-<flash|argon>-plain-r<n>/. The run of record wrote
#   ta-tnames-2026-11-22.out; tamfp2a201 (the cell of record after the 503 re-queue, root ...-r2-a2) was read by hand and added.
#   ⚠️ The run of record used an earlier text of this file that wrote out the run box's export and scratch paths; this text takes them
#   as arguments and is otherwise the same loop.
set -u
EXP=${1:?export dir}; SEC=${2:?block T sections dir}; D=${3:?out dir}; H=$(cd "$(dirname "$0")" && pwd)
mkdir -p "$D" || exit 2
python3 "$H/../../blockT-result-2026-11-22/t-sections.py" "$EXP" "$D/sec" > "$D/sec.log" 2>&1
for f in "$SEC"/*.rs; do b=$(basename "$f"); cmp -s "$f" "$D/sec/$b" && echo "SECTION EQUAL $b" || echo "SECTION DIFF $b"; done
for P in Luby AES Liveness MaxFlow BinomialHeap LinearScan; do p=$(echo $P | tr A-Z a-z)
  for w in flash argon; do for r in 1 2 3; do
    for c in "$HOME"/cells-ta-$p-$w-plain-r$r/ta*p*; do [ -d "$c/repo" ] && bash "$H/tnames.sh" "$SEC/$p-section.rs" "$c"; done
  done; done
done
