#!/bin/bash
# selftest_dry_s2rust.sh — THE RUN-SHAPED DRY, as a repeatable gate. ZERO MODEL TOKENS.
#
# It builds a production-SHAPED bench root in a scratch dir and drives episode_s2rust.sh end to end once per
# outcome class, each with its verdict PREDICTED AND REGISTERED HERE before it is run. Every line of the
# driver after the launch executes for real: the pin assertions, the rendered-fence check, the toolchain
# gate, the views set-hash, the ground-truth fence, the rt probe, the process-group launch, the orphan sweep,
# extract, screen, lynette, the fenced referee, the meter and the landing.
#
# ⛔ WHY A MATRIX AND NOT ONE HAPPY RUN. A dry that only ever produces one verdict proves the machinery
# starts, not that it DISCRIMINATES — and this campaign's whole output is a classification. The first version
# of this matrix returned the SAME class six times and looked entirely healthy; see D0.
#
# THE REGISTERED PREDICTIONS (a miss is a finding, not a failure to hide):
#   proof   -> VERIFY_FAIL       a sorry-free wrong proof reaches the referee and loses
#   clean   -> VERIFY_FAIL       the shipped empty body proves nothing
#   screen  -> SCREEN            `assume(false)` never reaches the referee
#   helper  -> VERIFY_FAIL       a VALID helper proof fn is accepted — the arm-correlation guard (amendment
#                                15 FATAL 3): if this ever turns SCREEN or STATEMENT_ALTERED, the instrument
#                                has started punishing the salt arm for doing what the salt arm does
#   badhelp -> SCREEN            ⛔ REGISTERED AS HELPERS_SHAPE, MEASURED AS SCREEN. The prediction was wrong
#                                and the instrument right: the screen already carries the helpers table, so
#                                it fires first. Under `--no-screen` the same artifact returns HELPERS_SHAPE,
#                                which is exactly what that layer is for. Corrected, not deleted.
#   damage  -> SCAFFOLD_DAMAGED  a deleted end marker is a marker-pair fact, never a content fact
#
# usage: selftest_dry_s2rust.sh [--keep]        env: VERUS_ROOT LYNETTE_BIN VIEWS_SRC H
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"; H="${H:-$(cd "$HERE/.." && pwd)}"
VERUS_ROOT="${VERUS_ROOT:-$HOME/bench-src/verus-release-pin/verus-arm64-macos}"
LYNETTE_BIN="${LYNETTE_BIN:-$HOME/bench-src/verus-proof-synthesis/utils/lynette/source/target/release/lynette}"
VIEWS_SRC="${VIEWS_SRC:-}"
KEEP=0; [ "${1:-}" = "--keep" ] && KEEP=1

[ -x "$VERUS_ROOT/verus" ] || { echo "DRY REFUSED: no verus at $VERUS_ROOT (a fixture that cannot be built proves nothing — refuse, never skip)"; exit 3; }
[ -x "$LYNETTE_BIN" ] || { echo "DRY REFUSED: no lynette at $LYNETTE_BIN"; exit 3; }
[ -n "$VIEWS_SRC" ] && [ -d "$VIEWS_SRC/views" ] || { echo "DRY REFUSED: set VIEWS_SRC=<dir built by build_views_verus.py>"; exit 3; }

ROOT=$(mktemp -d /tmp/s2rustdry.XXXXXX)
cleanup(){ [ "$KEEP" = 1 ] && { echo "kept: $ROOT"; return; }; rm -rf "$ROOT"; }
trap cleanup EXIT

# ⛔ THE VIEWS ROOT IS BUILT GROUND-TRUTH-FREE, BY CONSTRUCTION, because that is the Studio's shape:
# build_views_verus.py writes `gt/` BESIDE `views/` on the seat, and only `views/` ever travels. Copying the
# whole build dir here would make the dry pass against a tree the real host must never have.
mkdir -p "$ROOT/views"; cp -R "$VIEWS_SRC/views" "$ROOT/views/views"
BENCH="$ROOT/bench"; CFG="$ROOT/cfg"; EPROOT="$ROOT/work"
mkdir -p "$BENCH/logs" "$BENCH/state" "$CFG/projects" "$EPROOT"
ln -sfn "$H" "$BENCH/harness"     # production shape: the harness lives under the run's own root
# ⛔ --cfg IS THE DRY'S JOB TOO: the dry exists to be RUN-SHAPED, and since 09/02 the run passes --cfg. A dry
# that renders the fence differently from the run is a dry of a different program — and it would have gone on
# passing while every real episode REFUSED.
python3 "$HERE/render_settings_verus.py" --bench "$BENCH" --cfg "$CFG" --out "$CFG/settings.json" >/dev/null || exit 2
TASK=$(ls "$ROOT/views/views" | head -1 | tr -d '/')

run(){ # run <mode> -> the landed class
  rm -rf "${CFG:?}/projects"/* "${EPROOT:?}"/*
  printf '%s\n' "$1" > "$CFG/stub_mode"
  printf 'a0\n' | env BENCH="$BENCH" H="$BENCH/harness" CFG="$CFG" EPROOT="$EPROOT" VIEWS="$ROOT/views" \
    VERUS_ROOT="$VERUS_ROOT" LYNETTE_BIN="$LYNETTE_BIN" \
    CLAUDE_BIN="$HERE/dry_exec_stub_s2rust.sh" CLAUDE_BIN_STUB=1 MAX_TURNS=3 WALL_S=600 \
    bash "$HERE/episode_s2rust.sh" "$TASK" 2>&1 | grep '^LANDED' | awk '{print $6}'
}

pass=0; fail=0
check(){ # check <mode> <expected>
  local got; got=$(run "$1")
  if [ "$got" = "$2" ]; then printf '  PASS %-8s %s\n' "$1" "$got"; pass=$((pass+1))
  else printf '  FAIL %-8s expected=%s got=%s\n' "$1" "$2" "${got:-<no landing>}"; fail=$((fail+1)); fi
}
echo "RUN-SHAPED DRY (task=$TASK, zero model tokens)"
check proof   VERIFY_FAIL
check clean   VERIFY_FAIL
check screen  SCREEN
check helper  VERIFY_FAIL
check badhelp SCREEN
check damage  SCAFFOLD_DAMAGED

# ── D0: the matrix must DISCRIMINATE. ────────────────────────────────────────────────────────────────────
# ⛔ THIS ARM EXISTS BECAUSE THE FIRST VERSION OF THIS DRY PASSED SIX MODES THROUGH ONE CODE PATH AND
# REPORTED SIX IDENTICAL VERIFY_FAILs. The cause was that it steered the stub with `STUB_MODE=…` on the
# driver's command line, and the driver launches the agent under `env -i` — the hermeticity the campaign
# rests on — so the knob was never connected. Six runs, one measurement, and nothing looked wrong.
#   ⇒ A TEST RIG THAT STEERS ITS SUBJECT THROUGH A CHANNEL THE SUBJECT FENCES OFF MEASURES THE DEFAULT PATH
#     N TIMES AND CALLS IT N CASES. Distinctness is now asserted, not assumed.
classes=$(for m in proof screen damage; do run "$m"; done | sort -u | wc -l | tr -d ' ')
if [ "$classes" -ge 3 ]; then printf '  PASS %-8s %s distinct classes — the rig actually steers the subject\n' "D0" "$classes"; pass=$((pass+1))
else printf '  FAIL %-8s only %s distinct class(es) across three modes — the mode channel is not connected\n' "D0" "$classes"; fail=$((fail+1)); fi

echo
echo "dry selftest: $((pass+fail)) arms, $fail failed"
[ "$fail" = 0 ] || exit 1
