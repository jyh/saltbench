# Phase-1 complement to the A7.2 command: a spec-change root's phase-1 client stderr lives in _aside/<cell>/phase1/ctl/ (A7.4 (2)).
for d in ~/cells-l8zf-*; do
  n=$(ls "$d"/_aside/*/phase1/ctl/agy-stderr-*.txt 2>/dev/null | wc -l | tr -d ' ')
  h=$(cat "$d"/_aside/*/phase1/ctl/agy-stderr-*.txt 2>/dev/null | grep -c -F "print timeout")
  echo "$(basename "$d") p1files=$n p1hits=$h"
done
