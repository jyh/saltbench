#!/bin/bash
# hashes_s2rust.sh — regenerate HASHES-S2RUST.txt: the S2-Rust harness files, the toolchain pins, the
# benchmark pins and the rendered arm files.
#
# ⛔ THIS IS A SEPARATE FILE FROM THE SHARED `harness/HASHES.txt` **ON PURPOSE**, AND THE REASON IS A DATE.
# Amendment 11 §13's stage-C dispatch is still pending its 09/02 objection window and must run against the
# harness `sync_studio.sh` froze at saltbench `15cfdc2`. Adding S2-Rust keys to `hashes.sh` would rewrite
# `HASHES.txt`, move the harness sha `sync_studio.sh` receipts, and put the Studio out of step with its own
# freeze commit — for a wave that has not yet crossed its regime boundary.
# ⇒ SPEND COMPARABILITY ONLY WHEN A RUN NEEDS IT (amendment 11's law). These pins merge into `hashes.sh` at
# the VeruSAGE stage-0 regime boundary, together with the z3 fence widening and rows AV + CO — the helm's
# ruling that they land as ONE regime change, not three.
#
# Every path below is REQUIRED and the script FAILS LOUD if one is missing: a HASHES file that silently omits
# a pin is worse than none, because the gate that reads it reports green (amendment 12's law).
set -u
cd "$(dirname "$0")" || exit 1
: "${VERUS_ROOT:?set VERUS_ROOT=<unpacked verus release dir> (the one holding verus, z3, libvstd.rlib)}"
: "${LYNETTE_BIN:?set LYNETTE_BIN=<lynette binary built on the SEAT from the pinned benchmark repo>}"
: "${BENCH_REPO:?set BENCH_REPO=<verus-proof-synthesis clone at the pinned commit>}"
RLIMIT=${VERUS_RLIMIT:-250}
SEED=${VERUS_SEED:-0}

need() { [ -e "$1" ] || { echo "FATAL: missing $1 — cannot emit its pin" >&2; exit 2; }; }
need "$VERUS_ROOT/verus"; need "$VERUS_ROOT/z3"; need "$VERUS_ROOT/libvstd.rlib"; need "$LYNETTE_BIN"
JSONL="$BENCH_REPO/benchmarks/VeruSAGE-Bench/tasks.jsonl"; need "$JSONL"

OUT=HASHES-S2RUST.txt.tmp; trap 'rm -f HASHES-S2RUST.txt.tmp' EXIT   # atomic: a fail-loud exit must not clobber
sha() { shasum -a 256 "$1" | cut -d' ' -f1; }
{
  echo "# HASHES-S2RUST — regenerate with harness/s2rust/hashes_s2rust.sh; sha256; generated $(date -u +%Y-%m-%dT%H:%M:%SZ)"
  for f in rustspan.py build_views_verus.py extract_verus.py screen_verus.py check_verus.py gt_pass_verus.py \
           rlimit_curve_verus.py gt_leak_check.py controls_gate_verus.py views_sethash.py \
           selftest_check_verus.py selftest_rt_verus.sh hashes_s2rust.sh rt.template base.md prompt_P.md; do
    need "$f"; printf '%s %s\n' "$f" "$(sha "$f")"
  done
  # the toolchain, pinned as BINARIES — no cargo and no rustup at episode time
  printf 'verus-release %s\n'  "$("$VERUS_ROOT/verus" --version 2>/dev/null | awk '/Version:/{print $2}')"
  printf 'verus-sha %s\n'      "$(sha "$VERUS_ROOT/verus")"
  printf 'rust_verify-sha %s\n' "$(sha "$VERUS_ROOT/rust_verify")"
  printf 'z3-sha %s\n'         "$(sha "$VERUS_ROOT/z3")"
  printf 'z3-version %s\n'     "$("$VERUS_ROOT/z3" --version 2>/dev/null | head -1 | tr ' ' '_')"
  printf 'vstd-sha %s\n'       "$(sha "$VERUS_ROOT/libvstd.rlib")"
  printf 'lynette-sha %s\n'    "$(sha "$LYNETTE_BIN")"
  # ⛔ NOT a documentation pin: a Verus release zip does NOT stand alone — it refuses to run until a MATCHING
  # rustup toolchain is installed on the host, and the two candidate releases want different ones
  # (1.97.1 for 0.2026.08.30, 1.88.0 for the benchmark's pin). This is a Studio PREREQUISITE.
  printf 'rust-channel %s\n'   "$("$VERUS_ROOT/verus" --version 2>/dev/null | awk '/Toolchain:/{print $2}')"
  # the benchmark
  printf 'bench-repo-commit %s\n' "$(git -C "$BENCH_REPO" rev-parse HEAD)"
  printf 'bench-jsonl-sha %s\n'   "$(sha "$JSONL")"
  # the referee's flags, pinned so the in-episode rt and the check-time referee cannot diverge
  printf 'verus-rlimit %s\n' "$RLIMIT"
  printf 'verus-seed %s\n'   "$SEED"
  # the rendered arms: the Verus base block + each arm text. a2.md is BYTE-IDENTICAL to S2-Lean's by design.
  for a in ../arms/*.md; do
    id=$(basename "$a" .md); src="$a"
    [ "$id" = a1 ] && [ -f ../s2lean/placebo.md ] && src=../s2lean/placebo.md
    printf 'rendered-s2rust-%s(__EP__) %s bytes=%s\n' "$id" \
      "$(cat base.md "$src" | shasum -a 256 | cut -d' ' -f1)" "$(cat base.md "$src" | wc -c | tr -d ' ')"
  done
  printf 'arms/a2.md %s\n' "$(sha ../arms/a2.md)"
  # THE VIEWS ARE NOT SHIPPED — they are REBUILT from the pinned jsonl and verified by SET-HASH. 207 views of
  # multi-hundred-KB Rust do not belong in git when they are a pure function of two pinned inputs
  # (bench-jsonl-sha + build_views_verus.py). Measured: a clean rebuild reproduces the set-hash byte-identically.
  if [ -n "${VIEWS_DIR:-}" ] && [ -d "$VIEWS_DIR/views" ]; then
    printf 'views-set-sha256 %s\n' "$(python3 views_sethash.py "$VIEWS_DIR")"
  fi
} > "$OUT"
mv "$OUT" HASHES-S2RUST.txt
trap - EXIT
echo "wrote $(pwd)/HASHES-S2RUST.txt ($(wc -l < HASHES-S2RUST.txt | tr -d ' ') lines)"
