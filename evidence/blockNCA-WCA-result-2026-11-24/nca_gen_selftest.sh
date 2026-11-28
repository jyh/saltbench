#!/bin/bash
# nca_gen_selftest.sh — the generator's refusals driven RED on a scratch receipts root (NCA_RUNS); the real root is read, never written.
# Each arm builds its fixture from the REAL receipts (copied), plants one defect, and requires the named refusal and rc 1.
set -u
HERE=$(cd "$(dirname "$0")" && pwd); REAL=${REAL_RUNS:-$HOME/.fleet/executors/gemini.runs}; pass=0; fail=0
export NCA_WEB_JOIN="${NCA_WEB_JOIN:-$HERE/../o37-agy-web-served-2026-11-20/join.tsv}"   # the arms below run COPIES of this dir, which have no sibling
T=$(mktemp -d "${TMPDIR:-/tmp}/nca-gen-st.XXXXXX") || exit 2
fresh(){ find "$T" -mindepth 1 -delete; for d in "$REAL"/nca-*-score*/ "$REAL"/wca-*-score*/ "$REAL"/nca-*-harvest*/ "$REAL"/wca-*-harvest*/; do [ -d "$d" ] || continue; mkdir -p "$T/$(basename "$d")"; cp "$d"*.p2.score.txt "$T/$(basename "$d")/" 2>/dev/null; done
  mkdir -p "$T/nca-manifests-2026-11-24"; cp "$REAL"/nca-manifests-2026-11-24/harvest-*.out "$T/nca-manifests-2026-11-24/" 2>/dev/null; }   # the G receipts (2026-11-28)
arm(){ local name=$1 want=$2 rcw=$3; out=$(NCA_RUNS=$T python3 -I "$HERE/nca_cells_gen.py" --summary 2>&1); rc=$?
  if [ "$rc" = "$rcw" ] && printf '%s\n' "$out" | grep -q -F -- "$want"; then pass=$((pass+1)); echo "ok   $name (rc $rc)"; else fail=$((fail+1)); echo "FAIL $name (rc $rc): $(printf '%s' "$out" | tail -1)"; fi; }
fresh; arm control-real-receipts 'rows 96 · scored' 0
fresh; arm web-source-leaves-comparisons 'NCA-flash LinearScan plain: PASS 3 of 3 scored, of 3 registered [T14/14 R0/9 C0/5 T14/14 R0/9 C0/5 T14/14 R0/9 C0/5] · G reach-loss 0 · cut turns 0 · truncated 0 of 3 scored · CTL-READ 0 of 3 scored · in comparisons 0 of 3 scored' 0   # its 3 sources are WEB-SERVED (census ADDENDUM 47)
# ⛔ WCA's receipts sit in wca-*-harvest* dirs (2026-11-28): a reader keyed on -score* read all 24 WCA rows UNSCORED, and so did this
#   fixture, which copied the same glob. The arm reads the table row of T-WCA-F's root, whose only receipts are in harvest dirs.
fresh; out=$(NCA_RUNS=$T python3 -I "$HERE/nca_cells_gen.py" 2>&1 | awk -F'\t' '$2=="cells-wa-ntt-flash-salt-r1-wcacp1"{print $22, $23}')
if [ "$out" = "PASS 15/15" ]; then pass=$((pass+1)); echo "ok   wca-harvest-receipt-read"; else fail=$((fail+1)); echo "FAIL wca-harvest-receipt-read: got [$out] want [PASS 15/15]"; fi
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
ctlarm ctl-line-unread-not-zero 'NCA-flash AES plain: PASS 3 of 3 scored, of 3 registered [T14/14 R0/8 C0/6 T14/14 R0/8 C0/6 T14/14 R0/8 C0/6] · G reach-loss 0 · cut turns 0 · truncated 0 of 3 scored · CTL-READ UNREAD of 3 scored' 0 'cells-na-aes-flash-plain-ncacp1\t0\t-\n'
ctlarm ctl-unread-comparisons-unread 'CTL-READ UNREAD of 3 scored · in comparisons UNREAD of 3 scored' 0 'cells-na-aes-flash-plain-ncacp1\t0\t-\n'
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
# attempt arms (L8 A2.2; 2026-11-28): a receipt root is a manifest root or <root>-a<k>, k >= 2; the run box names the standing attempt
fresh; mkdir -p "$T/nca-zz-score"; f=$(ls "$T"/nca-*-score*/cells-nca-linearscan-argon-plain-r2-a2.p2.score.txt | head -1)
cp "$f" "$T/nca-zz-score/cells-na-nosuch-root-a2.p2.score.txt"
arm attempt-stray-root 'outside the 96: cells-na-nosuch-root-a2' 1
fresh; mkdir -p "$T/nca-zz-score"; cp "$f" "$T/nca-zz-score/cells-nca-linearscan-argon-plain-r2.p2.score.txt"
arm two-attempts-scored 'row cells-nca-linearscan-argon-plain-r2 has receipts for two attempts' 1
fresh; G=$(mktemp -d "${TMPDIR:-/tmp}/nca-gen-att.XXXXXX") || exit 2; cp -R "$HERE"/. "$G"/
python3 -c 'import json,sys; p=sys.argv[1]; j=json.load(open(p)); [r.update(attempt=1) for r in j if r["root"]=="cells-nca-linearscan-argon-plain-r2"]; json.dump(j,open(p,"w"))' "$G/cell_facts.json"
out=$(NCA_RUNS=$T python3 -I "$G/nca_cells_gen.py" --summary 2>&1); rc=$?
if [ "$rc" = 1 ] && printf '%s\n' "$out" | grep -q -F 'receipt scores attempt 2, the run box reads attempt 1 as standing'; then pass=$((pass+1)); echo "ok   attempt-disagrees (rc $rc)"; else fail=$((fail+1)); echo "FAIL attempt-disagrees (rc $rc): $(printf '%s' "$out" | tail -1)"; fi
find "$G" -delete
F=$(mktemp -d "${TMPDIR:-/tmp}/nca-gen-st2.XXXXXX") || exit 2
attarm(){ local name=$1 want=$2; shift 2; find "$F" -mindepth 1 -delete; for d in "$@"; do mkdir -p "$F/$d"; done
  out=$(printf 'r\tpq\t-\n' | HOME=$F python3 -I "$HERE/nca_facts.py" | python3 -c 'import json,sys; r=json.load(sys.stdin)[0]; print("%s %s %s %s" % (r["id"], r["attempt"], r["discarded"], r["standing_root"]))' 2>&1)
  if [ "$out" = "$want" ]; then pass=$((pass+1)); echo "ok   $name"; else fail=$((fail+1)); echo "FAIL $name: got [$out] want [$want]"; fi; }
attarm attempt-standing-a2 'pqa201 2 1 r-a2' r-a2/pqa201/ctl r.DISCARDED-503-2026-11-27T11:15:13Z/pq01/ctl
attarm attempt-two-roots 'TWO-ATTEMPTS TWO-ATTEMPTS 0 TWO-ATTEMPTS' r/pq01/ctl r-a2/pqa201/ctl
attarm attempt-no-root 'NO-ROOT NO-ROOT 1 NO-ROOT' r.DISCARDED-503-x/pq01/ctl
attarm attempt-one-plain 'pq01 1 0 r' r/pq01/ctl rx-a2/pqa201/ctl
# ⛔ the bare prefix `pq` is a prefix of `pqa201`, so the arms above pass whether or not a<k> is appended (mutant M5 survived them,
#   2026-11-28; equivalent on the real population, where each -a<k> root holds one cell). Only an attempt root that ALSO holds a
#   `pq`-named dir separates the two: with a<k> appended the cell is pqa201, without it TWO-CELLS.
attarm attempt-prefix-carries-ak 'pqa201 2 0 r-a2' r-a2/pq01/ctl r-a2/pqa201/ctl
find "$F" -delete
# G arms (NC rule 4; 2026-11-28): a fresh cell counts only on an ELIGIBLE baseline; the box's verdict and the hand's ROW line must agree
fresh; arm g-reach-loss-not-counted 'NCA-flash BinomialHeap salt-diet: PASS 2 of 2 scored, of 3 registered [T18/18 R0/13 C0/5 T18/18 R0/13 C0/5] · G reach-loss 1 [ncabhfs01 G 7/13, phase 2 FAIL T7/18]' 0
fresh; G=$(mktemp -d "${TMPDIR:-/tmp}/nca-gen-g.XXXXXX") || exit 2; cp -R "$HERE"/. "$G"/
python3 -c 'import json,sys; p=sys.argv[1]; j=json.load(open(p)); [r.update(g_verdict="NOT-ELIGIBLE") for r in j if r["root"]=="cells-nca-aes-argon-plain-r1"]; json.dump(j,open(p,"w"))' "$G/cell_facts.json"
out=$(NCA_RUNS=$T python3 -I "$G/nca_cells_gen.py" --summary 2>&1); rc=$?
if [ "$rc" = 1 ] && printf '%s\n' "$out" | grep -q -F 'cells-nca-aes-argon-plain-r1 G baseline: the box reads NOT-ELIGIBLE'; then pass=$((pass+1)); echo "ok   g-box-vs-receipt (rc $rc)"; else fail=$((fail+1)); echo "FAIL g-box-vs-receipt (rc $rc): $(printf '%s' "$out" | tail -1)"; fi
find "$G" -delete
F=$(mktemp -d "${TMPDIR:-/tmp}/nca-gen-g2.XXXXXX") || exit 2
garm(){ local name=$1 want=$2 setup=$3; find "$F" -mindepth 1 -delete; B="$F/bench-dry/nca-fresh-gbase-2026-11-25"; mkdir -p "$F/r/pq01/ctl" "$B"; eval "$setup"
  out=$(printf 'r\tpq\t-\n' | HOME=$F python3 -I "$HERE/nca_facts.py" | python3 -c 'import json,sys; r=json.load(sys.stdin)[0]; print("%s %s %s %s" % (r["g_tests"], r["g_verdict"], r["g_sha12"], r["g_aborted"]))' 2>&1)
  if [ "$out" = "$want" ]; then pass=$((pass+1)); echo "ok   $name"; else fail=$((fail+1)); echo "FAIL $name: got [$out] want [$want]"; fi; }
S40=aaaaaaaaaaaa0000000000000000000000000000
garm g-root-id-eligible "8/8 ELIGIBLE aaaaaaaaaaaa 0" 'mkdir -p $B/r/pq01/logs $B/r/pq01/work/pq01/.git; printf "x\nTESTS 8/8\n" > $B/r/pq01/logs/pq01.G.log; echo $S40 > $B/r/pq01/work/pq01/.git/HEAD'
garm g-short-not-eligible "7/13 NOT-ELIGIBLE aaaaaaaaaaaa 0" 'mkdir -p $B/r/pq01/logs $B/r/pq01/work/pq01/.git; printf "TESTS 7/13\n" > $B/r/pq01/logs/pq01.G.log; echo $S40 > $B/r/pq01/work/pq01/.git/HEAD'
garm g-legacy-own-root "12/12 ELIGIBLE aaaaaaaaaaaa 1" 'mkdir -p $B/pq01/logs $B/pq01/work/pq01/.git $B/r.ABORTED-SIGPIPE-x; echo r > $B/pq01/CELL-ROOT.txt; printf "TESTS 12/12\n" > $B/pq01/logs/pq01.G.log; echo $S40 > $B/pq01/work/pq01/.git/HEAD'
garm g-legacy-other-root "NO-RECORD NO-RECORD NO-RECORD 0" 'mkdir -p $B/pq01/logs; echo rr > $B/pq01/CELL-ROOT.txt; printf "TESTS 12/12\n" > $B/pq01/logs/pq01.G.log'
garm g-no-log "NO-LOG NO-LOG NO-LOG 0" 'mkdir -p $B/r/pq01'
find "$F" -delete
# rep, web and phase-1 arms (2026-11-28, bench relight 229)
reparm(){ local name=$1 want=$2 root=$3; out=$(cd "$HERE" && python3 -I -c 'import sys; sys.path.insert(0, "."); import nca_cells_gen as g; print(g.rep_of(sys.argv[1]))' "$root" 2>&1)
  if [ "$out" = "$want" ]; then pass=$((pass+1)); echo "ok   $name"; else fail=$((fail+1)); echo "FAIL $name: got [$out] want [$want]"; fi; }
reparm rep-copy-trailing-not-source-group 1 cells-na-luby-flash-plain-r2-ncacp1
reparm rep-fresh-trailing 2 cells-nca-luby-argon-plain-r2
reparm rep-no-index-refuses 'REFUSE: no trailing rep index in root cells-x-plain-r2-ncacp' cells-x-plain-r2-ncacp
fresh; W=$(mktemp -d "${TMPDIR:-/tmp}/nca-gen-web.XXXXXX") || exit 2
WC=cells-wa-ntt-flash-salt-r1-wcacp1/wanfs101
webarm(){ local name=$1 col=$2 want=$3 root=$4 setup=$5; find "$W" -mindepth 1 -delete; cp -R "$HERE"/. "$W"/; cp "$NCA_WEB_JOIN" "$W/join.tsv"; eval "$setup"
  out=$(NCA_RUNS=$T NCA_WEB_JOIN="$W/join.tsv" python3 -I "$W/nca_cells_gen.py" 2>&1 | awk -F'\t' -v c="$col" -v r="$root" 'NR==1{for(i=1;i<=NF;i++) if($i==c) k=i} NR>1 && $2==r {print $k}')
  if [ "$out" = "$want" ]; then pass=$((pass+1)); echo "ok   $name"; else fail=$((fail+1)); echo "FAIL $name: got [$out] want [$want]"; fi; }
webarm web-control-clean p2_web_served CLEAN cells-wa-ntt-flash-salt-r1-wcacp1 ':'
webarm web-zero-transcripts-unmeasured p2_web_served UNMEASURED cells-wa-ntt-flash-salt-r1-wcacp1 "sed -i '' 's|^$WC	[0-9]*\$|$WC	0|' \$W/web_transcripts.tsv"
webarm web-served-counted p2_web_served 'WEB-SERVED(2)' cells-wa-ntt-flash-salt-r1-wcacp1 "printf '%s\tc0\tsearch_web\t2\t2\t0\t0\t0\tq\n' $WC >> \$W/web_census.tsv"
webarm web-absent-unread p2_web_served UNREAD cells-wa-ntt-flash-salt-r1-wcacp1 "sed -i '' '\|^$WC	|d' \$W/web_transcripts.tsv"
webarm source-web-served-carried source_web_served WEB-SERVED cells-na-linearscan-flash-plain-r2-ncacp1 ':'
webarm source-not-in-join source_web_served NOT-IN-JOIN cells-wa-ntt-flash-salt-r1-wcacp1 "sed -i '' '/	wanfs101	/d' \$W/join.tsv"
webarm fresh-source-is-own source_web_served OWN:CLEAN cells-nca-luby-argon-plain-r1 ':'
find "$W" -delete
F=$(mktemp -d "${TMPDIR:-/tmp}/nca-gen-p1.XXXXXX") || exit 2
p1arm(){ local name=$1 want=$2 setup=$3; find "$F" -mindepth 1 -delete; mkdir -p "$F/r/pq01/ctl" "$F/src/pq01/ctl" "$F/r/_aside/pq01/phase1/ctl"
  printf 'source\t%s\n' "$F/src/pq01" > "$F/r/pq01/ctl/copied-from.tsv"; eval "$setup"
  out=$(printf 'r\tpq\t%s\n' "$F/src/pq01" | HOME=$F python3 -I "$HERE/nca_facts.py" | python3 -c 'import json,sys; r=json.load(sys.stdin)[0]; print(r["p1_model"], r["p1_client16"])' 2>&1)
  if [ "$out" = "$want" ]; then pass=$((pass+1)); echo "ok   $name"; else fail=$((fail+1)); echo "FAIL $name: got [$out] want [$want]"; fi; }
L1='x LAUNCHING phase 1 model mA client aaaaaaaaaaaaaaaa'; L2='x LAUNCHING phase 1 model mA client bbbbbbbbbbbbbbbb'
p1arm p1-aside-agrees-with-source 'mA aaaaaaaaaaaaaaaa' "echo '$L1' > \$F/r/_aside/pq01/phase1/ctl/launch.log; echo '$L1' > \$F/src/pq01/ctl/launch.log"
p1arm p1-aside-disagrees 'DISAGREE DISAGREE' "echo '$L1' > \$F/r/_aside/pq01/phase1/ctl/launch.log; echo '$L2' > \$F/src/pq01/ctl/launch.log"
p1arm p1-aside-absent-source-read 'mA bbbbbbbbbbbbbbbb' "echo '$L2' > \$F/src/pq01/ctl/launch.log"
p1arm p1-no-log 'NO-LOG NO-LOG' ':'
p1arm p1-no-line 'NO-LINE NO-LINE' "echo 'LAUNCHING phase 2 model mA client aaaaaaaaaaaaaaaa' > \$F/r/_aside/pq01/phase1/ctl/launch.log"
find "$F" -delete
find "$T" -delete
echo "nca_gen_selftest: $pass of $((pass+fail)) arms"; [ "$fail" = 0 ]
