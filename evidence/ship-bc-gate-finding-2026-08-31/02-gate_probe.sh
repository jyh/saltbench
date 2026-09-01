#!/bin/bash
# READ-ONLY probe of the ship-BC gate. Ships nothing, writes nothing.
G=$HOME/bench/logs/run_s2_stage0.log
echo "=== the gate predicate (stage_views.sh:17), run VERBATIM and READ-ONLY ==="
if grep -q "S2 STAGE A DRIVER DONE" "$G" 2>/dev/null; then
  echo "GATE = PASS — 'ship BC' would put ground truth on the host right now"
else
  echo "GATE = REFUSE"
fi
echo
echo "=== every DONE line in the file the gate reads ($G) ==="
grep -n "S2 STAGE A DRIVER DONE" "$G"
echo
echo "=== the NEWEST one in context: gates OK at 18:32:18Z, DONE at 18:32:19Z ==="
sed -n '731,738p' "$G"
echo
echo -n "START/LANDED lines between that invocation's gates and its DONE: "
awk '/2026-08-31T18:32:18Z SMOKE GATE OK/,/2026-08-31T18:32:19Z S2 STAGE A DRIVER DONE/' "$G" | grep -cE 'START #|LANDED #'
echo
echo "=== what the a8 run wrote INSTEAD, in its OWN root ==="
ls -la "$HOME/bench-a8/logs/"
echo -n "DONE lines in the a8 log: "
grep -c "S2 STAGE A DRIVER DONE" "$HOME/bench-a8/logs/run_s2_stage0.log"
grep -n "S2 STAGE A DRIVER DONE" "$HOME/bench-a8/logs/run_s2_stage0.log"
echo
echo "=== the views symlink: the ship TARGET is shared, only the GATE is stale ==="
ls -ld "$HOME/bench/s2views" "$HOME/bench-a8/s2views"
fz=$(find "$HOME/bench/s2views" -name frozen.json | wc -l)
cl=$(find "$HOME/bench/s2views" -name C.lean | wc -l)
tot=$(find "$HOME/bench" -name frozen.json -o -name C.lean 2>/dev/null | wc -l)
echo "bench/s2views frozen=$fz C=$cl | frozen+C anywhere under ~/bench = $tot"
