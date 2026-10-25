# The A7.2 command (evidence/zf-print-timeout-census-2026-10-22/tally.py docstring), restricted to ZF roots, one line per root.
for d in ~/cells-zf-* ~/cells-l8zf-*; do
  n=$(ls "$d"/*/ctl/agy-stderr-*.txt 2>/dev/null | wc -l | tr -d ' ')
  h=$(cat "$d"/*/ctl/agy-stderr-*.txt 2>/dev/null | grep -c -F "print timeout")
  echo "$(basename "$d") files=$n hits=$h"
done
