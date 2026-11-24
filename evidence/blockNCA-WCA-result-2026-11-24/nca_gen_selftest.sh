#!/bin/bash
# nca_gen_selftest.sh — the generator's refusals driven RED on a scratch receipts root (NCA_RUNS); the real root is read, never written.
# Each arm builds its fixture from the REAL receipts (copied), plants one defect, and requires the named refusal and rc 1.
set -u
HERE=$(cd "$(dirname "$0")" && pwd); REAL=${REAL_RUNS:-$HOME/.fleet/executors/gemini.runs}; pass=0; fail=0
T=$(mktemp -d "${TMPDIR:-/tmp}/nca-gen-st.XXXXXX") || exit 2
fresh(){ find "$T" -mindepth 1 -delete; for d in "$REAL"/nca-*-score*/ "$REAL"/wca-*-score*/; do [ -d "$d" ] || continue; mkdir -p "$T/$(basename "$d")"; cp "$d"*.p2.score.txt "$T/$(basename "$d")/" 2>/dev/null; done; }
arm(){ local name=$1 want=$2 rcw=$3; out=$(NCA_RUNS=$T python3 -I "$HERE/nca_cells_gen.py" --summary 2>&1); rc=$?
  if [ "$rc" = "$rcw" ] && printf '%s\n' "$out" | grep -q -F -- "$want"; then pass=$((pass+1)); echo "ok   $name (rc $rc)"; else fail=$((fail+1)); echo "FAIL $name (rc $rc): $(printf '%s' "$out" | tail -1)"; fi; }
fresh; arm control-real-receipts 'rows 96 · scored' 0
fresh; f=$(ls "$T"/nca-flash-liveness-*-score/*ncacp2.p2.score.txt | head -1); mkdir -p "$T/nca-zz-score"; sed 's/REGRESSIONS 0\//REGRESSIONS 9\//' "$f" > "$T/nca-zz-score/$(basename "$f")"
arm disagreeing-duplicate 'two receipts that DISAGREE' 1
fresh; f=$(ls "$T"/nca-flash-luby-*-score/*.p2.score.txt | head -1); mkdir -p "$T/nca-zz-score"; cp "$f" "$T/nca-zz-score/"
arm agreeing-duplicate-admitted 'rows 96 · scored' 0
fresh; mkdir -p "$T/nca-zz-score"; cp "$f" "$T/nca-zz-score/cells-na-nosuch-root.p2.score.txt"
arm stray-root 'outside the 96' 1
fresh; f=$(ls "$T"/nca-flash-luby-*-score/*ncacp1.p2.score.txt | grep -v salt | head -1); sed -i '' 's/^nalbfq01 /nalbfq99 /' "$f"
arm cell-mismatch 'receipt names cell nalbfq99' 1
fresh; f=$(ls "$T"/nca-flash-luby-*-score/*ncacp1.p2.score.txt | grep -v salt | head -1); sed -i '' '/^nalbfq01 /d' "$f"
arm no-row-reads-unread 'rows 96 · scored 11' 0
find "$T" -delete
echo "nca_gen_selftest: $pass of $((pass+fail)) arms"; [ "$fail" = 0 ]
