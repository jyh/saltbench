#!/bin/bash
# smoke_toolchain_verus.sh — THE TOOLCHAIN GATE. No model, no agent, no episode. Run on the machine that will
# run the referee, BEFORE the first episode; the driver refuses to start without its PASS line.
#
# ⛔ WHY THIS GATE EXISTS AT ALL, and it is a measured history rather than a precaution. Amendment 15 §3.5
# chose the Verus release by reading release notes. Run on real reference proofs, that binary failed **5 of 15
# at the RUSTC FRONT END** while the benchmark's own pin passed **15/15** — and a front-end error on a
# reference file indicts the TOOLCHAIN, never the task. Worse, the failure is silent in the shape that
# matters: a Verus release zip DOES NOT STAND ALONE. It refuses to run until a MATCHING rustup toolchain is
# on the host, and the two candidate releases want DIFFERENT ones (1.88.0 vs 1.97.1). A host with the wrong
# channel produces a dead-task list that is not a small error in a number — IT IS A DIFFERENT LIST.
#
# ⭐ AND THE PIN CHECK ALONE IS NOT ENOUGH, WHICH IS WHY T3 EXISTS. Every sha can match while the toolchain
# cannot execute (a missing rust channel, an unsigned binary, a half-copied tree). A gate that checks only
# identity certifies a museum piece. T3 runs the referee on a real proof and requires `0 errors`.
#   ⇒ IDENTITY AND CAPABILITY ARE TWO CLAIMS; A TOOLCHAIN GATE MUST MAKE BOTH.
#
#   T1  every pinned binary is present and its sha256 EQUALS the pin in HASHES.txt
#   T2  the rust channel `verus --version` demands is the pinned one AND is installed on this host
#   T3  the referee actually verifies a real proof under the fence (capability, not identity)
#   T4  the Seatbelt profile's sha EQUALS its pin (the fence text is part of the toolchain)
#   T5  the referee's own flags (rlimit, seed) are pinned, so the in-episode rt and the checker cannot diverge
#
# usage: smoke_toolchain_verus.sh [--selftest]
#   env: HASHES (default <harness>/HASHES.txt) · VERUS_ROOT · LYNETTE_BIN
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
HASHES="${HASHES:-$HERE/../HASHES.txt}"
VERUS_ROOT="${VERUS_ROOT:-$HOME/verus-pin/verus-arm64-macos}"
LYNETTE_BIN="${LYNETTE_BIN:-$HOME/verus-pin/lynette}"

sha(){ shasum -a 256 "$1" 2>/dev/null | cut -d' ' -f1; }
pin(){ grep -E "^$1 " "$HASHES" 2>/dev/null | head -1 | cut -d' ' -f2; }
rc=0
fail(){ printf 'SMOKE FAIL %-22s %s\n' "$1" "$2"; rc=2; }
ok(){   printf 'SMOKE OK   %-22s %s\n' "$1" "$2"; }

[ -r "$HASHES" ] || { echo "SMOKE REFUSED: no pin table at $HASHES"; exit 3; }

# ── T1: identity ────────────────────────────────────────────────────────────────────────────────────────
# ⛔ An ABSENT pin is a FAILURE, never a skip. A gate that quietly passes the keys it cannot find reports
# green on a table that forgot the binary — the FN2-01 shape, and the reason hashes_s2rust.sh fails loud too.
check(){ # check <label> <pin-key> <path>
  local want have; want=$(pin "$2"); have=$(sha "$3")
  if   [ -z "$want" ]; then fail "$1" "no pin '$2' in $(basename "$HASHES") — cannot certify it"
  elif [ -z "$have" ]; then fail "$1" "not present on this host: $3"
  elif [ "$want" != "$have" ]; then fail "$1" "DRIFT host=${have:0:16} pinned=${want:0:16}"
  else ok "$1" "${have:0:16}"; fi
}
check verus       verus-sha        "$VERUS_ROOT/verus"
check rust_verify rust_verify-sha  "$VERUS_ROOT/rust_verify"
check z3          z3-sha           "$VERUS_ROOT/z3"
check vstd        vstd-sha         "$VERUS_ROOT/libvstd.rlib"
check lynette     lynette-sha      "$LYNETTE_BIN"
# rustup is in the fence's exec allow-list, so it is part of the toolchain whether or not it feels like it
RUSTUP_BIN="$(command -v rustup || true)"
if [ -n "$RUSTUP_BIN" ]; then check rustup rustup-sha "$RUSTUP_BIN"
else fail rustup "no rustup on PATH — the verus shim resolves its toolchain by running it"; fi

# ── T2: the rust channel, demanded AND installed ─────────────────────────────────────────────────────────
want_ch=$(pin rust-channel)
have_ch=$("$VERUS_ROOT/verus" --version 2>/dev/null | awk '/Toolchain:/{print $2}')
if [ -z "$want_ch" ]; then fail rust-channel "no 'rust-channel' pin in $(basename "$HASHES")"
elif [ "$want_ch" != "$have_ch" ]; then fail rust-channel "binary wants '$have_ch', pin says '$want_ch'"
elif ! rustup toolchain list 2>/dev/null | grep -q -- "$want_ch"; then
  fail rust-channel "'$want_ch' is NOT installed on this host — the release zip does not stand alone"
else ok rust-channel "$want_ch installed"; fi

# ── T4: the fence text is part of the toolchain ──────────────────────────────────────────────────────────
check profile s2rust/sandbox_verus.sb "$HERE/sandbox_verus.sb"

# ── T5: the referee's flags ──────────────────────────────────────────────────────────────────────────────
RL=$(pin verus-rlimit); SD=$(pin verus-seed)
{ [ -n "$RL" ] && [ -n "$SD" ]; } && ok referee-flags "rlimit=$RL seed=$SD" \
  || fail referee-flags "verus-rlimit/verus-seed missing — the rt and the checker could diverge"

# ── T3: capability. A real proof, through check_verus's own fenced referee. ───────────────────────────────
W=$(mktemp -d /tmp/verussmoke.XXXXXX)
printf 'use vstd::prelude::*;\nverus!{\nproof fn smoke_add_zero(x: int)\n    ensures x + 0 == x\n{\n}\n}\nfn main() {}\n' > "$W/task.rs"
export HERE
out=$(cd "$W" && PATH="$HOME/.cargo/bin:$PATH" python3 - "$VERUS_ROOT/verus" "$W" <<'PY' 2>&1
import sys, os
sys.path.insert(0, os.environ["HERE"])
import check_verus as C
r = C.referee(sys.argv[1], "task.rs", sys.argv[2], 250, 0, 300, fenced=True)
print("%s|%s" % (C.classify(r, r["timed_out"]), r["results_line"]))
PY
)
case "$out" in
  PASS\|*) ok referee "fenced run verifies: ${out#*|}" ;;
  *)       fail referee "the toolchain is pinned but cannot verify a reference proof: $out" ;;
esac
rm -rf "$W"

[ "$rc" = 0 ] && echo "SMOKE PASS toolchain (T1-T5)" || echo "SMOKE FAILED toolchain"
exit $rc
