#!/bin/bash
# hashes.sh — regenerate HASHES.txt: every harness file, the settings, and the RENDERED arm files
# for a canonical episode path so an episode can assert its CLAUDE.md is a registered rendering.
# ⛔ The rendered CLAUDE.md contains the episode path, so its sha varies per episode; what is pinned is
# the sha of the rendering with the path replaced by the literal __EP__ — episode.sh checks the
# UN-substituted form by re-rendering.
set -u
cd "$(dirname "$0")" || exit 1
OUT=HASHES.txt.tmp; trap 'rm -f HASHES.txt.tmp' EXIT   # atomic: a fail-loud exit (e.g. CLEVER_SRC unset) must NOT clobber HASHES.txt (FN2-01)
{
  echo "# HASHES — regenerate with harness/hashes.sh; sha256; generated $(date -u +%Y-%m-%dT%H:%M:%SZ)"
  for f in base.md prompt.md rt.template episode.sh check2b.sh check2b.selftest.sh hook-deny-network.sh meter.py build_prompt.py preflight_gold.sh bridge_assert.sh score.sh run_stage0.sh predictions.py project_data.py morning_line.py pull_pilot.sh sync_studio.sh studio_phase.sh dry_exec_stub.sh smoke.sh settings.bench.json arms/*.md; do
    printf '%s %s\n' "$f" "$(shasum -a 256 "$f" | cut -d' ' -f1)"
  done
  printf 'settings.json %s\n' "$(shasum -a 256 settings.bench.json | cut -d' ' -f1)"
  printf 'claude-version %s\n' "2.1.251"
  # S2-Lean: the harness files, the arm renderings with the Lean base block, and every shipped view
  for f in s2lean/*.py s2lean/*.sh s2lean/*.md s2lean/rt.template s2lean/*.lean s2lean/*.sb; do [ -f "$f" ] && printf '%s %s\n' "$f" "$(shasum -a 256 "$f" | cut -d' ' -f1)"; done
  for a in arms/*.md; do id=$(basename "$a" .md); src="$a"; [ "$id" = a1 ] && [ -f s2lean/placebo.md ] && src=s2lean/placebo.md; printf 'rendered-s2-%s(__EP__) %s bytes=%s\n' "$id" "$(cat s2lean/base.md "$src" | shasum -a 256 | cut -d' ' -f1)" "$(cat s2lean/base.md "$src" | wc -c | tr -d ' ')"; done
  # S2 pins added 2026-08-28 after refuter pass 1 (F10/FN-10/FN-9): settings.s2.json, every shipped file incl. frozenA, flagged/view_status, the draw, the shared project's three files
  [ -f settings.s2.json ] && printf 'settings.s2.json %s\n' "$(shasum -a 256 settings.s2.json | cut -d' ' -f1)"
  for f in s2lean/flagged.json s2lean/view_status.json s2lean/c_dead_unsat.json; do [ -f "$f" ] && printf '%s %s\n' "$f" "$(shasum -a 256 "$f" | cut -d' ' -f1)"; done   # s2audit.lean/sandbox_check.sb come from the *.lean/*.sb glob above — do NOT re-emit (a duplicate line breaks sync_studio.sh's receipt: P2C2-01)
  if [ -d s2lean/views ]; then for d in s2lean/views/problem_*; do t=$(basename "$d"); printf 'view-A %s %s\n' "$t" "$(shasum -a 256 "$d/A.lean" | cut -d' ' -f1)"; printf 'view-C %s %s\n' "$t" "$(shasum -a 256 "$d/C.lean" | cut -d' ' -f1)"; printf 'frozen %s %s\n' "$t" "$(shasum -a 256 "$d/frozen.json" | cut -d' ' -f1)"; printf 'frozenA %s %s\n' "$t" "$(shasum -a 256 "$d/frozenA.json" | cut -d' ' -f1)"; done; fi
  [ -f s2lean/draw.py ] && printf 'draw-30 %s\n' "$(python3 s2lean/draw.py 30 | shasum -a 256 | cut -d' ' -f1)"
  if [ -n "${CLEVER_SRC:-}" ] && [ -d "$CLEVER_SRC" ]; then for pair in lakefile:lakefile.lean manifest:lake-manifest.json toolchain:lean-toolchain; do printf 'leanproj-%s %s\n' "${pair%%:*}" "$(shasum -a 256 "$CLEVER_SRC/${pair#*:}" | cut -d' ' -f1)"; done
  else echo "FATAL: CLEVER_SRC unset or not a dir — the three leanproj-* pins cannot be emitted; a HASHES.txt without them makes episode_s2.sh refuse EVERY episode (FN2-01). Set CLEVER_SRC=<clever clone>/src/lean4 and re-run." >&2; exit 2; fi
  printf 'clever-commit %s\n' "8348039a7ff7730a126d761e71d0439735eeb3e2"
  printf 'lean-toolchain %s\n' "leanprover/lean4:v4.27.0"
  printf 'mathlib-rev %s\n' "a3a10db0e9d66acbebf76c5e6a135066525ac900"
  for a in arms/*.md; do
    id=$(basename "$a" .md)
    printf 'rendered-%s(__EP__) %s bytes=%s\n' "$id" "$(cat base.md "$a" | shasum -a 256 | cut -d' ' -f1)" "$(cat base.md "$a" | wc -c | tr -d ' ')"
  done
  # ── S2-RUST (amendment 16, the VeruSAGE stage-0 regime boundary) ────────────────────────────────────
  # ⛔ EMITTED BY s2rust/hashes_s2rust.sh --emit, NEVER re-implemented here. A checksum defined twice is two
  # checksums (amendment 15): the generator and the verifier must be the same CODE, not the same idea.
  # ⛔ Its file keys are namespaced `s2rust/…` because `base.md`, `rt.template` and `arms/a2.md` exist in BOTH
  # tables and the first two mean DIFFERENT files with DIFFERENT shas. Every consumer resolves a key with
  # `grep … | head -1`, so an un-namespaced merge would have made one of two `base.md` lines silently
  # authoritative — P2C2-01, re-created by the merge meant to be bookkeeping. The duplicate-key gate below
  # is what keeps that fixed rather than merely fixed-today.
  if [ -n "${VERUS_ROOT:-}" ] && [ -n "${LYNETTE_BIN:-}" ] && [ -n "${BENCH_REPO:-}" ]; then
    s2rust/hashes_s2rust.sh --emit || { echo "FATAL: the S2-Rust pin emitter failed" >&2; exit 2; }
  else
    echo "FATAL: VERUS_ROOT / LYNETTE_BIN / BENCH_REPO unset — the S2-Rust pins cannot be emitted, and a" >&2
    echo "  HASHES.txt silently missing them reports green to every gate that reads it (FN2-01's shape)." >&2
    exit 2
  fi
} > "$OUT"
# per-task CANONICAL prompt shas (prompt with the episode path replaced by __EP__), so a pair's prompts are
# provably identical up to the path (refuter F3); requires data/problem_statements.json beside the harness
if [ -f data/problem_statements.json ]; then
  python3 - >> "$OUT" <<'PY'
import json,hashlib
t=open("prompt.md").read()
for r in sorted(json.load(open("data/problem_statements.json")),key=lambda r:r["instance_id"]):
    p=t.replace("__PROBLEM_STATEMENT__",r["problem_statement"])
    print("prompt-canonical", r["instance_id"], hashlib.sha256(p.encode()).hexdigest())
PY
  printf 'problem_statements.json %s\n' "$(shasum -a 256 data/problem_statements.json | cut -d' ' -f1)" >> "$OUT"
fi
# ⛔ THE DUPLICATE-KEY GATE. Every consumer of this table resolves a key with `grep "^<key> " | head -1`, so a
# table with the same key twice does not fail — it silently elects one of the two values. sync_studio.sh's
# `head -1` was added for exactly that reason (P2C2-01) and treats the symptom; this treats the cause, and it
# is what makes the S2-Rust merge safe rather than merely careful.
#
# ⛔⛔ THE RESOLUTION KEY IS NOT ALWAYS FIELD 1, AND MY FIRST CUT OF THIS GATE GOT IT WRONG. The table carries
# TWO line shapes — `<key> <value>` and `<kind> <subject> <value>` (`frozen <task> <sha>`, `view-A <task> <sha>`,
# `prompt-canonical <instance_id> <sha>`) — which is exactly why episode_s2.sh has BOTH `pin2` and `pin3`.
# Keying on $1 alone reported `frozen`, `frozenA` and `prompt-canonical` as duplicates on a table that was
# perfectly well-formed: 3 false positives out of 4 hits, and it would have blocked every regeneration.
#   ⇒ A UNIQUENESS GATE MUST KEY ON WHAT THE CONSUMER RESOLVES ON. Mine keyed on what the line STARTS with,
#     which is the same mistake in miniature as the whole family this campaign keeps finding: an instrument
#     that names a proxy for the thing it means.
dups=$(awk '!/^#/ && NF>=2 { if (NF>=3) print $1, $2; else print $1 }' "$OUT" | sort | uniq -d)
if [ -n "$dups" ]; then
  echo "FATAL: duplicate key(s) in HASHES.txt — a consumer would silently elect one value:" >&2
  echo "$dups" | sed 's/^/  /' >&2
  exit 2
fi
mv "$OUT" HASHES.txt; cat HASHES.txt
