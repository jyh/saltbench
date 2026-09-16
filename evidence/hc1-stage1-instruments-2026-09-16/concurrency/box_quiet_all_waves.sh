#!/bin/bash
# box_quiet_all_waves.sh — PREDICTIONS-HC-stage1 §6.3 item 3 AS REGISTERED: "no cell of ANY wave running".
#
# WHY IT EXISTS (bench, 2026-09-16, relight 57): bench-hc1-fire.sh's quiet guard asked HC1 cells only, so the
# instrument was one word narrower than the registration. Census (~/bench-dry/hc1-concurrency-2026-09-16): 23 of
# 44 HC1 cells shared the box with agy cells and 19 of 44 were not quiet at fire. Nothing reported it.
#
# AN agy CELL HAS NO watch.beat, so the HC1 rule (beat fresher than 180 s) cannot see it. The rule here:
#   a non-HC1 cell is LIVE iff it has ctl/launch.log, NO ctl/end-<N>, and some file under ctl/ was written
#   within QUIET_WINDOW seconds (default 2400 = the agy print timeout 1800 s + 600 s; a Flash or Pro turn can be
#   legitimately silent for its whole print timeout, so a shorter window reads a working cell as quiet).
# ⇒ It FAILS TOWARD REFUSAL: a halted cell with no end marker reads live for up to 40 min after its last write.
#   That costs a wait. The opposite error costs a comparability deviation on a registered cell.
# ⛔ NO PROCESS-TABLE NEEDLES (see bench-hc1-fire.sh:64-78): it asks the cells' own files.
# usage: box_quiet_all_waves.sh            rc 0 quiet · rc 1 live cells named on stderr · rc 2 cannot read
#        QUIET_HOME=<dir> QUIET_WINDOW=<s>  for the fixture arms only
set -u
HOMEDIR="${QUIET_HOME:-$HOME}"
WIN="${QUIET_WINDOW:-2400}"
now=$(date +%s)
[ -d "$HOMEDIR" ] || { echo "box_quiet_all_waves: cannot read $HOMEDIR" >&2; exit 2; }
live=0; desc=""; seen=0
for c in "$HOMEDIR"/cells-*/*; do
  [ -f "$c/ctl/launch.log" ] || continue
  case "$c" in "$HOMEDIR"/cells-hc1-*/hc1*) continue ;; esac     # HC1 cells: the beat guard in the fire script
  seen=$((seen+1))
  ls "$c/ctl"/end-[0-9]* >/dev/null 2>&1 && continue            # terminal
  newest=$(find "$c/ctl" -type f -exec stat -f %m {} + 2>/dev/null | sort -n | tail -1)
  [ -n "$newest" ] || { echo "box_quiet_all_waves: cannot stat $c/ctl" >&2; exit 2; }
  age=$((now - newest))
  if [ "$age" -lt "$WIN" ]; then live=$((live+1)); desc="$desc ${c#"$HOMEDIR"/}(last write ${age}s ago)"; fi
done
if [ "$live" != 0 ]; then
  echo "NOT QUIET — $live non-HC1 cell(s) live by their own ctl/ writes (window ${WIN}s, no end marker):$desc" >&2
  exit 1
fi
echo "QUIET (all waves) — $seen non-HC1 launched cell(s) read; none without an end marker written within ${WIN}s"
