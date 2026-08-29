#!/bin/bash
# lean_shared_build.sh — THE STUDIO PREP of the shared Lean project (repair D2). Runs ON THE STUDIO, once, before the
# controls and the driver (it needs the network: git clone + `lake exe cache get`; never run it on the seat).
# What it builds: $HOME/lean-shared/clever = a `git archive` EXPORT of src/lean4 at the pinned CLEVER commit, taken from
# a clone that lives ONLY at a temp path outside $HOME and is deleted afterwards; human_eval/ and sample_examples/ are
# removed from the export; then `lake exe cache get` + `lake build Imports.AllImports`. Then it ASSERTS: no .git anywhere
# under $HOME/lean-shared except the packages' own clones (.lake/packages/<pkg>/.git — Lake re-checks `git rev-parse HEAD`
# against the manifest on every load, lake/Lake/Load/Materialize.lean:233 at v4.27.0, so they must stay; none may be
# CLEVER), no human_eval/sample_examples dirs, no human_eval/sample_examples oleans, Imports/AllImports.olean present;
# and it prints the shas of lakefile.lean, lake-manifest.json, lean-toolchain as `leanproj-*` lines (hashes.sh emits the
# same lines from CLEVER_SRC on the seat; episode_s2.sh refuses on any difference).
#   usage: lean_shared_build.sh [--skip-build]     env: H (~/bench/harness: clever-commit from HASHES.txt)
#          LEAN_SHARED ($HOME/lean-shared) · CLEVER_SOURCE (git url or a local clone path; default the public repo)
#   --skip-build: export + strip + assert only (seat self-test of the export logic; the build assertions then report MISSING)
set -u
H="${H:-$HOME/bench/harness}"; LS="${LEAN_SHARED:-$HOME/lean-shared}"; DST="$LS/clever"; SKIP=""; [ "${1:-}" = "--skip-build" ] && SKIP=1
SRC="${CLEVER_SOURCE:-https://github.com/trishullab/clever.git}"
COMMIT=$(grep '^clever-commit ' "$H/HASHES.txt" | cut -d' ' -f2); [ -n "$COMMIT" ] || { echo "REFUSE: no clever-commit line in $H/HASHES.txt"; exit 3; }
TOOLCHAIN=$(grep '^lean-toolchain ' "$H/HASHES.txt" | cut -d' ' -f2)
case "$LS" in "$HOME"/*|/private/tmp/*|/tmp/*) ;; *) echo "REFUSE: LEAN_SHARED must be under \$HOME (or a temp path for the seat test)"; exit 3 ;; esac
TMP=$(mktemp -d /private/tmp/clever-clone.XXXXXX) || exit 1
trap 'rm -rf "$TMP"' EXIT
say() { printf '%s\n' "$*"; }
say "LEAN-SHARED-BUILD start commit=$COMMIT src=$SRC dst=$DST tmp=$TMP"
git clone -q "$SRC" "$TMP/clone" || { say "FAIL clone"; exit 1; }
git -C "$TMP/clone" checkout -q "$COMMIT" || { say "FAIL checkout $COMMIT"; exit 1; }
[ "$(git -C "$TMP/clone" rev-parse HEAD)" = "$COMMIT" ] || { say "FAIL HEAD != $COMMIT"; exit 1; }
rm -rf "$DST"; mkdir -p "$DST"
git -C "$TMP/clone" archive --format=tar "$COMMIT:src/lean4" | tar -x -C "$DST" || { say "FAIL archive"; exit 1; }
rm -rf "$TMP"   # the clone (and its .git) is gone before anything else happens; the trap repeats it on any exit
rm -rf "$DST/human_eval" "$DST/sample_examples"
say "exported: $(ls -A "$DST" | tr '\n' ' ')"
[ "$(cat "$DST/lean-toolchain")" = "$TOOLCHAIN" ] || { say "FAIL lean-toolchain $(cat "$DST/lean-toolchain") != pinned $TOOLCHAIN"; exit 1; }
if [ -z "$SKIP" ]; then
  ( cd "$DST" && export PATH="$HOME/.elan/bin:$PATH" && lake exe cache get 2>&1 | tr '\r' '\n' | grep -Ev '^Downloaded: [0-9]+ file' | tail -20 && lake build Imports.AllImports ) || { say "FAIL lake (cache get / build Imports.AllImports)"; exit 1; }
fi
# ── assertions (the same ones episode_s2.sh makes at every episode) ──
fail=0
g=$(find "$LS" -name .git -not -path '*/.lake/packages/*/.git' 2>/dev/null | head -3 | tr '\n' ' '); [ -z "$g" ] && say "ASSERT PASS no .git under $LS (outside .lake/packages)" || { say "ASSERT FAIL .git present: $g"; fail=1; }
git -C "$DST" rev-parse --git-dir >/dev/null 2>&1 && { say "ASSERT FAIL $DST is inside a git repository"; fail=1; } || say "ASSERT PASS $DST is not inside any git repository"
for pg in "$DST"/.lake/packages/*/.git; do [ -e "$pg" ] || continue; u=$(git --git-dir="$pg" config --get remote.origin.url 2>/dev/null); case "$u" in *clever*|*CLEVER*) say "ASSERT FAIL package clone is CLEVER: $pg ($u)"; fail=1 ;; esac; done
say "package clones (allowed, Lake needs them): $(ls -d "$DST"/.lake/packages/*/.git 2>/dev/null | wc -l | tr -d ' ')"
[ -e "$DST/human_eval" ] || [ -e "$DST/sample_examples" ] && { say "ASSERT FAIL human_eval/ or sample_examples/ present"; fail=1; } || say "ASSERT PASS no human_eval/ sample_examples/"
p=$(find "$LS" -name 'problem_*.lean' -not -path '*/.lake/packages/*' 2>/dev/null | head -1); [ -z "$p" ] && say "ASSERT PASS no problem_*.lean under $LS" || { say "ASSERT FAIL $p"; fail=1; }
[ -f "$DST/.lake/build/lib/lean/Imports/AllImports.olean" ] && say "ASSERT PASS Imports/AllImports.olean present" || { say "ASSERT ${SKIP:+MISSING(skip-build)}${SKIP:-FAIL} Imports/AllImports.olean absent"; [ -z "$SKIP" ] && fail=1; }
[ -z "$(ls "$DST/.lake/build/lib/lean/human_eval" "$DST/.lake/build/lib/lean/sample_examples" 2>/dev/null)" ] && say "ASSERT PASS no human_eval/sample_examples oleans" || { say "ASSERT FAIL human_eval/sample_examples oleans present"; fail=1; }
for pair in lakefile:lakefile.lean manifest:lake-manifest.json toolchain:lean-toolchain; do printf 'leanproj-%s %s\n' "${pair%%:*}" "$(shasum -a 256 "$DST/${pair#*:}" | cut -d' ' -f1)"; done
[ "$fail" = 0 ] && say "LEAN-SHARED-BUILD-DONE $DST" || { say "LEAN-SHARED-BUILD FAILED"; exit 1; }
