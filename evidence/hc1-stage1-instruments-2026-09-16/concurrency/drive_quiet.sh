#!/bin/bash
# red-first arms for box_quiet_all_waves.sh, on fixtures plus ONE live arm on the real box
set -u
G=~/.fleet/saltbench/box_quiet_all_waves.sh; F=$(mktemp -d ~/bench-dry/quiet-fixture.XXXXXX); pass=0; tot=0
arm() { tot=$((tot+1)); if [ "$2" = "$3" ]; then pass=$((pass+1)); echo "ok   $1 (rc $3)"; else echo "FAIL $1 (want rc $2, got $3)"; fi; }
mk() { mkdir -p "$F/$1/ctl"; echo "2026-09-16T00:00:00Z x" > "$F/$1/ctl/launch.log"; }
# A: ended fresh agy cell -> quiet
mk cells-a/c1; echo LANDED > "$F/cells-a/c1/ctl/end-1"; QUIET_HOME=$F "$G" >/dev/null 2>&1; arm "ended fresh cell is quiet" 0 $?
# B: fresh cell, no end -> live
mk cells-b/c2; QUIET_HOME=$F "$G" >/dev/null 2>&1; arm "fresh cell without end marker is LIVE" 1 $?
# C: same cell, older than the window -> quiet
touch -t 202609150000 "$F/cells-b/c2/ctl/launch.log"; QUIET_HOME=$F "$G" >/dev/null 2>&1; arm "stale cell without end marker is quiet" 0 $?
# D: HC1-named fresh cell is not this guard's population -> quiet
mk cells-hc1-x/hc1xx01; QUIET_HOME=$F "$G" >/dev/null 2>&1; arm "HC1 cell left to the beat guard" 0 $?
# E: an end-2 counts as terminal
mk cells-e/c5; echo x > "$F/cells-e/c5/ctl/end-2"; QUIET_HOME=$F "$G" >/dev/null 2>&1; arm "end-2 is terminal" 0 $?
# F: a quiet phase inside the window still reads live (a turn silent 20 min, window 40)
mk cells-f/c6; touch -A -002000 "$F/cells-f/c6/ctl/launch.log"; QUIET_HOME=$F "$G" >/dev/null 2>&1; arm "a cell silent 20 min reads LIVE" 1 $?
rm -rf -- "${F:?}/cells-f"
# MUTANT: drop the end-marker skip -> arm A must flip
M=$(mktemp ~/bench-dry/quiet-mutant.XXXXXX); grep -v 'end-\[0-9\]\*' "$G" > "$M"; chmod +x "$M"
rm -rf -- "${F:?}/cells-b" "${F:?}/cells-e"; QUIET_HOME=$F bash "$M" >/dev/null 2>&1; arm "MUTANT (no end skip) flips the ended-cell arm" 1 $?
# LIVE: the real box, with dgpwf01 running
"$G" 2>&1 | sed 's/^/     live: /'; rc=${PIPESTATUS[0]}; echo "     live rc=$rc"
rm -rf -- "${F:?}"; rm -f -- "${M:?}"
echo "ARMS $pass of $tot"
