#!/bin/bash
# stage_views.sh — run FROM THE SEAT. `gen` regenerates harness/s2lean/views from the pinned CLEVER clone;
# `ship A` puts ONLY the stage-A views + frozenA.json in the ACTIVE ROOT on the Studio and REMOVES any
# frozen.json/C.lean there (--delete-excluded: an extended draw can re-enter stage A — refuter MT-R1);
# `ship BC` adds frozen.json FIRST and C.lean SECOND (two rsyncs, so an interrupted ship never leaves C.lean
# without its frozen.json — GT-7) and only after the CONTENT GATE below is green; `check` prints what the WHOLE
# of the active root holds (GT-2: the harness mirror must carry no views — sync_studio.sh excludes
# s2lean/views/; this is the ONLY route for views).
#
# ⛔ RBENCH IS REQUIRED AND HAS NO DEFAULT (amendment 10, 2026-08-31). Until 2026-08-31 every path here was the
# literal `~/bench`, while amendment 8's run wrote `~/bench-a8` — so `ship BC`'s gate read a log the live run no
# longer touched and was measured GREEN on a DONE line printed by a run that executed ZERO episodes
# (FINDING-ship-bc-gate-2026-08-31.md). A default root is exactly the thing that let a stale root answer for a
# live one, so there is no default: the caller names the root or the tool refuses.
#
# ⛔ AND `ship BC`'s GATE NO LONGER READS A LOG AT ALL. It runs bc_gate.py in the ACTIVE ROOT over the drawn ids
# × the arms and verifies each stage-A artifact BY CONTENT (see bc_gate.py's header for the three defects and
# the three answers). A driver's DONE line is the driver's claim; this gate reads the state.
#
# usage: RBENCH=<remote abs path> stage_views.sh gen <clone src/lean4> | ship A | ship BC | check
#        ship BC additionally needs:  IDS="73 0 146 ..."  ARMS="a0,a2"   (BC_MAX_AGE_H defaults to 24)
set -u
STUDIO="${STUDIO:-kriterion-lan}"; REPO="$(cd "$(dirname "$0")/../.." && pwd)"; V="$REPO/harness/s2lean/views"
SSH="ssh -o ConnectTimeout=10"
need_root() {
  [ -n "${RBENCH:-}" ] || { echo "REFUSE: RBENCH is required and has no default (the absolute state root ON THE STUDIO, e.g. /Users/jyh/bench-a8)."; echo "        The 2026-08-31 green-light-on-nothing was a hardwired \`~/bench\` answering for a run that wrote \`~/bench-a8\`."; exit 2; }
  case "$RBENCH" in /*) ;; *) echo "REFUSE: RBENCH must be an ABSOLUTE remote path (got $RBENCH) — ~ does not expand inside the remote quoting."; exit 2;; esac
}
case "${1:?gen|ship A|ship BC|check}" in
  gen) CL="${2:?path to clever clone src/lean4}"; rm -rf "$V"; python3 "$REPO/harness/s2lean/build_views.py" "$CL" "$V" && ls "$V" | wc -l ;;
  ship) need_root; case "${2:?A|BC}" in
    A)  rsync -a --delete --delete-excluded -e "$SSH" --include='*/' --include='A.lean' --include='frozenA.json' --exclude='*' "$V/" "$STUDIO:$RBENCH/s2views/" || exit 1
        $SSH "$STUDIO" "echo \"gt files under $RBENCH (must be 0): \$(find $RBENCH \\( -name frozen.json -o -name C.lean \\) 2>/dev/null | wc -l | tr -d ' ')\"; echo \"problem dirs: \$(ls $RBENCH/s2views | wc -l | tr -d ' ')\"" ;;
    BC) if [ "${FORCE_BC:-}" != "1" ]; then
          [ -n "${IDS:-}" ] && [ -n "${ARMS:-}" ] || { echo "REFUSE: ship BC needs IDS and ARMS (the drawn population and the arms whose stage A must be complete IN $RBENCH). FORCE_BC=1 overrides, loudly."; exit 2; }
          $SSH "$STUDIO" "python3 - --root '$RBENCH' --arms '$ARMS' --ids '$IDS' --max-age-h '${BC_MAX_AGE_H:-24}'" < "$REPO/harness/s2lean/bc_gate.py" \
            || { echo "REFUSE: the BC content gate is not green in $RBENCH (FORCE_BC=1 to override)"; exit 3; }
        else echo "WARNING FORCE_BC=1: shipping ground truth WITHOUT the stage-A content gate"; fi
        rsync -a -e "$SSH" --include='*/' --include='frozen.json' --exclude='*' "$V/" "$STUDIO:$RBENCH/s2views/" || exit 1
        rsync -a -e "$SSH" --include='*/' --include='C.lean' --exclude='*' "$V/" "$STUDIO:$RBENCH/s2views/" || exit 1
        $SSH "$STUDIO" "echo \"frozen=\$(find $RBENCH/s2views -name frozen.json | wc -l | tr -d ' ') C=\$(find $RBENCH/s2views -name C.lean | wc -l | tr -d ' ')\"" ;;
    esac ;;
  check) need_root; $SSH "$STUDIO" "echo \"s2views: A=\$(find $RBENCH/s2views -name A.lean | wc -l | tr -d ' ') frozenA=\$(find $RBENCH/s2views -name frozenA.json | wc -l | tr -d ' ') frozen=\$(find $RBENCH/s2views -name frozen.json | wc -l | tr -d ' ') C=\$(find $RBENCH/s2views -name C.lean | wc -l | tr -d ' ')\"; echo \"gt files anywhere under $RBENCH: \$(find $RBENCH \\( -name frozen.json -o -name C.lean \\) 2>/dev/null | wc -l | tr -d ' ')\"; echo \"harness/s2lean/views on the Studio: \$(ls $RBENCH/harness/s2lean/views 2>/dev/null | wc -l | tr -d ' ') entries (must be 0)\"" ;;
  *) echo "usage: RBENCH=<abs remote root> stage_views.sh gen <clone src/lean4> | ship A | ship BC | check   (ship BC also needs IDS + ARMS)"; exit 2 ;;
esac
