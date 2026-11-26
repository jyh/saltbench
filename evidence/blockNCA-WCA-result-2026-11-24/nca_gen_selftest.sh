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
fresh
n0=$(NCA_RUNS=$T python3 -I "$HERE/nca_cells_gen.py" --summary 2>/dev/null | sed -n 's/^rows 96 · scored \([0-9]*\) .*/\1/p')   # derived, never typed (was 11 at 12 receipts)
fresh; f=$(ls "$T"/nca-flash-luby-*-score/*ncacp1.p2.score.txt | grep -v salt | head -1); sed -i '' '/^nalbfq01 /d' "$f"
arm no-row-reads-unread "rows 96 · scored $((n0-1)) " 0
# ctl census arms: the census file lives beside the generator, so each arm runs on a COPY of this dir (the real file is never written)
G=$(mktemp -d "${TMPDIR:-/tmp}/nca-gen-ctl.XXXXXX") || exit 2
ctlarm(){ local name=$1 want=$2 rcw=$3 body=$4; cp -R "$HERE"/. "$G"/; printf '%b' "$body" > "$G/ctl_census.tsv"
  out=$(NCA_RUNS=$T python3 -I "$G/nca_cells_gen.py" --summary 2>&1); rc=$?
  if [ "$rc" = "$rcw" ] && printf '%s\n' "$out" | grep -q -F -- "$want"; then pass=$((pass+1)); echo "ok   $name (rc $rc)"; else fail=$((fail+1)); echo "FAIL $name (rc $rc): $(printf '%s' "$out" | grep -F 'CTL-READ' | head -2 | tail -1)"; fi; }
fresh
ctlarm ctl-flagged 'CTL-READ 1 [cells-na-aes-flash-salt-ncacp1]' 0 'cells-na-aes-flash-salt-ncacp1\t8\tctl/briefing-claim,ctl/launch.log\ncells-na-aes-flash-plain-ncacp1\t0\t-\n'
ctlarm ctl-line-unread-not-zero 'NCA-flash AES plain: PASS 3 of 3 scored, of 3 registered [T14/14 R0/8 C0/6 T14/14 R0/8 C0/6 T14/14 R0/8 C0/6] · cut turns 0 · truncated 0 of 3 scored · CTL-READ UNREAD of 3 scored' 0 'cells-na-aes-flash-plain-ncacp1\t0\t-\n'
ctlarm ctl-malformed 'not root TAB reads TAB paths' 1 'cells-na-aes-flash-salt-ncacp1\t3\t-\n'
ctlarm ctl-stray-root 'outside the 96' 1 'cells-na-nosuch\t0\t-\n'
ctlarm ctl-duplicate 'twice' 1 'cells-na-aes-flash-plain-ncacp1\t0\t-\ncells-na-aes-flash-plain-ncacp1\t0\t-\n'
find "$G" -delete
# p2_gate arms: nca_facts.py run against a FAKE HOME (two roots holding the SAME id, distinct receipts; the gate log written by hand)
F=$(mktemp -d "${TMPDIR:-/tmp}/nca-gen-gate.XXXXXX") || exit 2
gatearm(){ local name=$1 want=$2 log=$3; find "$F" -mindepth 1 -delete
  for r in ra rb; do mkdir -p "$F/$r/ncax01/ctl" "$F/$r/ncax01/repo/.seat"; done
  printf 'aaaaaaaaaaaa%028d\n' 0 > "$F/ra/ncax01/repo/.seat/landing-1"; printf 'bbbbbbbbbbbb%028d\n' 0 > "$F/rb/ncax01/repo/.seat/landing-1"
  [ -n "$log" ] && printf '%b' "$log" > "$F/agy-widen-X.log"
  out=$(printf 'ra\tncax\t-\nrb\tncax\t-\n' | HOME=$F python3 -I "$HERE/nca_facts.py" | python3 -c 'import json,sys; print(" ".join(r["root"]+"="+r["p2_gate"] for r in json.load(sys.stdin)))' 2>&1)
  if [ "$out" = "$want" ]; then pass=$((pass+1)); echo "ok   $name"; else fail=$((fail+1)); echo "FAIL $name: got [$out] want [$want]"; fi; }
gatearm gate-keyed-by-receipt 'ra=rc=0 LANDED rb=NONE' 'phase2-landed-gate ncax01 rc=0 LANDED end-1=LANDED record=True tag=aaaaaaaaaaaa receipt=aaaaaaaaaaaa | limit\n'
gatearm gate-refusal-named 'ra=rc=0 LANDED rb=rc=1 NOT-LANDED tag=ABSENT receipt=bbbbbbbbbbbb' 'phase2-landed-gate ncax01 rc=0 LANDED tag=aaaaaaaaaaaa receipt=aaaaaaaaaaaa | x\nphase2-landed-gate ncax01 rc=1 NOT-LANDED end-1=LANDED record=True tag=ABSENT receipt=bbbbbbbbbbbb \xe2\x80\x94 fails: tag=ABSENT | x\n'
gatearm gate-no-log-unread 'ra=UNREAD rb=UNREAD' ''
find "$F" -delete
find "$T" -delete
echo "nca_gen_selftest: $pass of $((pass+fail)) arms"; [ "$fail" = 0 ]
