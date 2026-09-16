#!/bin/bash
# drive_column.sh — red-first drive of budget_read_column.py's §3b COLUMN against REAL cells.
# Expected values come from census.out (two methods agreeing), never from the tool under test.
COL=${COL:-$HOME/.fleet/saltbench/budget_read_column.py}
CFG=$HOME/<run-config-dir>
fail=0; n=0
check(){ # $1 cell dir  $2 expected column token
  local c=$1 want=$2 slug f got
  slug="$CFG/projects/$(cd "$c/repo" && pwd -P | tr '/' '-')"
  f=$(ls -- "$slug"/*.jsonl 2>/dev/null | head -1)
  got=$(python3 "$COL" "$f" 2>&1 | sed -n 's/^ *§3b COLUMN *: *\([A-Z-]*\).*/\1/p')
  n=$((n+1))
  if [ "$got" = "$want" ]; then echo "PASS $(basename $c) column=$got"; else echo "FAIL $(basename $c) want=$want got=${got:-<none>}"; fail=$((fail+1)); fi
}
check $HOME/cells-hc1-paxos-saltdiet/hc1ps02    READ-NOT-SEEN
check $HOME/cells-hc1-freelist-saltdiet/hc1fs01 READ-SAW
check $HOME/cells-hc1-crc32-saltdiet/hc1cs01    READ-SAW
check $HOME/cells-hc1-crc32-placebo/hc1cb01     READ-NOT-SEEN
check $HOME/cells-hc1-freelist-plain/hc1fp02    READ-SAW
echo "arms=$n fail=$fail"
[ "$fail" = 0 ]
