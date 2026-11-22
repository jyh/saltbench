#!/bin/bash
# block NC §C3 item 2 / §C2 step 1 as ADDENDUM 1 registers it: the P1 baseline = the EXPORT's G/run_tests.sh on each source's landed-1,
# run on a CLONE (never in the cell). Zero model tokens. Sources are read-only: tree hash of each cell's repo before and after.
set -u
B=$HOME/bench-dry/nc-baselines-2026-11-13; R=$HOME/bench-dry/nc-copydry-2026-11-13/root   # the 36ca596b archive
set -a; . "$HOME/cells/toolchain.env"; set +a
mkdir -p $B/work $B/logs $B/tmp; export TMPDIR=$B/tmp
cat $R/EXPORTED-FROM.sha 2>/dev/null
OUT=$B/baselines.tsv
printf 'model\tproblem\tarm\tcell\tlanded1\trc\tTESTS\tsolution_sha256_16\tsrc_tree_before\tsrc_tree_after\n' > $OUT
treeh() { ( cd "$1" && find . -path ./.git -prune -o -type f -print0 | sort -z | xargs -0 shasum -a 256 | shasum -a 256 | cut -c1-16; git -C "$1" rev-parse HEAD 2>/dev/null | cut -c1-12 ) | tr '\n' ':'; }
for root in $HOME/cells-clb-n[os]-*; do
  base=$(basename $root); m=${base#cells-clb-n}; m=${m%%-*}; rest=${base#cells-clb-n?-}; prob=${rest%-*}; arm=${rest##*-}
  case $prob in aes) T=AES;; binomialheap) T=BinomialHeap;; linearscan) T=LinearScan;; liveness) T=Liveness;; luby) T=Luby;; maxflow) T=MaxFlow;; *) echo "UNKNOWN $prob"; exit 5;; esac
  [ $m = o ] && M=Opus || M=Sonnet
  for c in $root/clb*; do
    [ -d "$c/repo" ] || continue; id=$(basename $c)
    before=$(treeh $c/repo)
    if git -C $c/repo rev-parse -q --verify refs/tags/landed-1 >/dev/null; then
      [ -e "$B/work/$id" ] && { echo "WORK EXISTS $id — refusing to reuse"; exit 6; }
      git clone -q --no-local $c/repo $B/work/$id && git -C $B/work/$id checkout -q landed-1
      sh $R/tasks/systems-v3/$T/G/run_tests.sh $B/work/$id > $B/logs/$id.G.log 2>&1; rc=$?
      tl=$(grep -E '^TESTS [0-9]+/[0-9]+' $B/logs/$id.G.log | tail -1 | cut -d' ' -f2); [ -n "$tl" ] || tl=NONE
      sh=$(shasum -a 256 $B/work/$id/solution.rs | cut -c1-16); l1=yes
    else rc=-; tl=-; sh=-; l1=no; fi
    after=$(treeh $c/repo)
    printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' $M $T $arm $id $l1 $rc $tl $sh $before $after >> $OUT
    echo "$M $T $arm $id landed1=$l1 rc=$rc TESTS=$tl $([ "$before" = "$after" ] && echo SRC-UNCHANGED || echo SRC-CHANGED)"
  done
done
# CONTROL (ADDENDUM 1): B/run_tests.sh on ONE source's landed-1 must exit 3 with no REGRESSIONS line.
sh $R/tasks/systems-v3/AES/B/run_tests.sh $B/work/clbmap01 > $B/logs/CONTROL-clbmap01.B.log 2>&1; crc=$?
echo "CONTROL B on clbmap01: rc=$crc REGRESSIONS-lines=$(grep -c '^REGRESSIONS' $B/logs/CONTROL-clbmap01.B.log) last=$(tail -1 $B/logs/CONTROL-clbmap01.B.log)"
echo BASELINES-END
