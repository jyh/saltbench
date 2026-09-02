#!/bin/bash
# hashes_s2rust.sh — THE S2-RUST PIN EMITTER. One implementation, two callers.
#
# ⭐ MERGED INTO `hashes.sh` at the VeruSAGE stage-0 regime boundary (amendment 16), as the helm ruled: one
# regime change, not three. Until then this wrote its own `HASHES-S2RUST.txt`, because rewriting `HASHES.txt`
# would have moved the harness the still-pending stage-C dispatch was frozen against.
#
# ⛔⛔ THE MERGE WAS NOT THE ONE-LINE CHORE IT LOOKED LIKE: THE TWO TABLES SHARE KEYS WITH DIFFERENT VALUES.
# Measured before merging — `base.md` (9ada9241… vs 7e543ff6…) and `rt.template` (c46e59af… vs 5db37bbe…)
# exist in BOTH tables and mean different files; `arms/a2.md` collides too but is byte-identical by design.
# A naive concatenation would have put two `base.md` lines in `HASHES.txt`, and every consumer resolves a key
# with `grep … | head -1`, so ONE OF THEM WOULD HAVE SILENTLY BECOME AUTHORITATIVE — the exact P2C2-01 defect
# `sync_studio.sh`'s own comment warns about, re-created by the merge that was supposed to be bookkeeping.
# ⇒ THE FILE KEYS ARE THEREFORE NAMESPACED `s2rust/<file>`, exactly as S2-Lean's are `s2lean/<file>`, and
#   `hashes.sh` now REFUSES a table containing any duplicate key at all (a gate, so this cannot recur).
# ⇒ 🔑 TWO TABLES THAT WERE NEVER COMPARED CAN EACH BE CORRECT AND STILL COLLIDE — a merge is a measurement,
#   not an append.
#
# ⛔ AND IT IS STILL ONE IMPLEMENTATION: `--emit` prints the pin block to stdout and the default writes the
# standalone file from THAT SAME BLOCK. Amendment 15's law — a checksum defined twice is two checksums; the
# generator and the verifier must be the same CODE, not the same idea.
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

# ⛔ THIS SCRIPT NOW ONLY EMITS. Its standalone-file mode is GONE with `HASHES-S2RUST.txt` itself: leaving a
# mode that writes a second pin table would let anyone re-create, in one command, exactly the duplicate this
# amendment merged away — and the second table would then drift silently, because nothing reads it.
#   ⇒ A RETIRED ARTIFACT WHOSE GENERATOR SURVIVES IS NOT RETIRED.
# `--emit` is still accepted so the caller's intent stays readable at the call site in hashes.sh.
OUT=$(mktemp /tmp/s2rustpins.XXXXXX); trap 'rm -f "$OUT"' EXIT
sha() { shasum -a 256 "$1" | cut -d' ' -f1; }
{
  # ⛔ ENUMERATED, NOT HAND-LISTED. The first cut carried an explicit file list, and within one commit it was
  # already stale: six new tools (the episode driver, its dry stub, the settings renderer and template, the
  # smoke gate, the provisioning script) were on disk and absent from the table.
  #   ⇒ 🔑 A HAND-MAINTAINED FILE LIST IS AN ABSENCE-LIST, AND AN ABSENCE-LIST CARRIES THE SAME STALENESS AS
  #     THE PRESENCE-LIST IT COMPLEMENTS — while reading, to anyone reviewing it, exactly like an audit.
  # It fails LOUD rather than silently omitting: episode_s2rust.sh refuses any s2rust/ file that is on the
  # host and not in the table, so an unpinned tool stops the run instead of riding along unmeasured. The
  # exclusions are by KIND (build artefacts, state, the table itself), never by name.
  # ⛔ AND THE GLOB IS EVERY FILE, NOT A LIST OF EXTENSIONS — my first enumerating cut still missed
  # `settings.s2rust.template.json`, because `*.py *.sh *.sb *.md rt.template` is a hand-list wearing a
  # glob's clothes. Same defect, one layer down, caught the same way: by counting the keys against the dir.
  for f in *; do
    [ -f "$f" ] || continue
    case "$f" in *.pyc|HASHES*|FREEZE-COMMIT) continue ;; esac
    need "$f"; printf 's2rust/%s %s\n' "$f" "$(sha "$f")"
  done
  # the toolchain, pinned as BINARIES — no cargo and no rustup at episode time
  printf 'verus-release %s\n'  "$("$VERUS_ROOT/verus" --version 2>/dev/null | awk '/Version:/{print $2}')"
  printf 'verus-sha %s\n'      "$(sha "$VERUS_ROOT/verus")"
  printf 'rust_verify-sha %s\n' "$(sha "$VERUS_ROOT/rust_verify")"
  printf 'z3-sha %s\n'         "$(sha "$VERUS_ROOT/z3")"
  printf 'z3-version %s\n'     "$("$VERUS_ROOT/z3" --version 2>/dev/null | head -1 | tr ' ' '_')"
  printf 'vstd-sha %s\n'       "$(sha "$VERUS_ROOT/libvstd.rlib")"
  printf 'lynette-sha %s\n'    "$(sha "$LYNETTE_BIN")"
  # ⛔ rustup IS PINNED BECAUSE THE FENCE ADMITS IT. `verus` is a shim that resolves its toolchain by RUNNING
  # rustup, so `sandbox_verus.sb` must allow rustup to exec — and rustup is the one member of that trusted set
  # that is NOT part of the pinned release: it lives on the user's PATH and is user-writable. A binary admitted
  # to a fence must be pinned by the same instrument that pins the ones it stands next to.
  RUSTUP_BIN=$(command -v rustup); need "$RUSTUP_BIN"
  printf 'rustup-sha %s\n'     "$(sha "$RUSTUP_BIN")"
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
  # ⛔ `arms/a2.md` is NOT emitted here any more: hashes.sh's own `arms/*.md` loop already pins it, and after
  # the merge a second line would be a duplicate key. It happens to carry the SAME sha (a2.md is byte-identical
  # across substrates by design) — which is precisely what makes it dangerous to leave: a duplicate whose two
  # values agree today is a duplicate that stops agreeing silently.
  # THE VIEWS ARE NOT SHIPPED — they are REBUILT from the pinned jsonl and verified by SET-HASH. 207 views of
  # multi-hundred-KB Rust do not belong in git when they are a pure function of two pinned inputs
  # (bench-jsonl-sha + build_views_verus.py). Measured: a clean rebuild reproduces the set-hash byte-identically.
  if [ -n "${VIEWS_DIR:-}" ] && [ -d "$VIEWS_DIR/views" ]; then
    printf 'views-set-sha256 %s\n' "$(python3 views_sethash.py "$VIEWS_DIR")"
  fi
} > "$OUT"
cat "$OUT"
