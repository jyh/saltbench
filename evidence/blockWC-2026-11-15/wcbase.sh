#!/bin/bash
# wcbase.sh <work-dir> <copies-dir> <export-root> — block WC §WC3 item 2 / §WC2 (NC ADDENDUM 1's instrument): the P1 baseline = the EXPORT's
#   G/run_tests.sh on a CLONE of each block-W source's landed-1. Zero model tokens. Run on the lead's box over COPIES of block W's 24 cells of
#   record (taken after each end marker, repo/target excluded), so the withheld trees never reach the run box. Each copy's tree hash and HEAD
#   are recorded before and after (the copy is never written; the clone is).
#   ELIGIBLE iff rc 0 and passed == total > 0. CONTROL: B/run_tests.sh on one source's landed-1 must exit 3 with no REGRESSIONS line.
set -u
B=${1:?work dir}; C=${2:?copies dir}; R=${3:?export root (harness + tasks of the export)}
set -a; . "${TOOLCHAIN_ENV:?the suite runner toolchain env}"; set +a
mkdir -p "$B/work" "$B/logs" "$B/tmp"; export TMPDIR=$B/tmp
cat "$R/EXPORTED-FROM.sha"
OUT=$B/baselines.tsv
printf 'model\tproblem\tarm\tcell\tlanded1\trc\tTESTS\teligible\tsolution_sha256_16\tsrc_tree_before\tsrc_tree_after\n' > "$OUT"
treeh() { ( cd "$1" && find . -path ./.git -prune -o -type f -print0 | sort -z | xargs -0 shasum -a 256 | shasum -a 256 | cut -c1-16; git -C "$1" rev-parse HEAD 2>/dev/null | cut -c1-12 ) | tr '\n' ':'; }
for c in $(ls -d "$C"/clb[di][wt][ps]0[123] | sort); do
  id=$(basename "$c"); case ${id:3:1} in d) M=Opus;; i) M=Sonnet;; esac; case ${id:4:1} in w) T=WHT;; t) T=NTT;; esac; case ${id:5:1} in p) A=plain;; s) A=salt-diet;; esac
  before=$(treeh "$c/repo")
  if git -C "$c/repo" rev-parse -q --verify refs/tags/landed-1 >/dev/null; then
    [ -e "$B/work/$id" ] && { echo "WORK EXISTS $id — refusing to reuse"; exit 6; }
    git clone -q --no-local "$c/repo" "$B/work/$id" && git -C "$B/work/$id" checkout -q landed-1
    sh "$R/tasks/systems-v3/$T/G/run_tests.sh" "$B/work/$id" > "$B/logs/$id.G.log" 2>&1; rc=$?
    tl=$(grep -E '^TESTS [0-9]+/[0-9]+' "$B/logs/$id.G.log" | tail -1 | cut -d' ' -f2); [ -n "$tl" ] || tl=NONE
    p=${tl%/*}; t=${tl#*/}; el=NO; [ "$rc" = 0 ] && [ "$tl" != NONE ] && [ "$p" = "$t" ] && [ "$t" -gt 0 ] && el=YES
    sh_=$(shasum -a 256 "$B/work/$id/solution.rs" | cut -c1-16); l1=yes
  else rc=-; tl=-; el=NO; sh_=-; l1=no; fi
  after=$(treeh "$c/repo")
  printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' $M $T $A $id $l1 $rc $tl $el $sh_ $before $after >> "$OUT"
  echo "$M $T $A $id landed1=$l1 rc=$rc TESTS=$tl eligible=$el $([ "$before" = "$after" ] && echo SRC-UNCHANGED || echo SRC-CHANGED)"
done
# CONTROL (NC ADDENDUM 1): B/run_tests.sh on ONE source's landed-1 must exit 3 with no REGRESSIONS line.
sh "$R/tasks/systems-v3/NTT/B/run_tests.sh" "$B/work/clbdtp01" > "$B/logs/CONTROL-clbdtp01.B.log" 2>&1; crc=$?
echo "CONTROL B on clbdtp01 (NTT): rc=$crc REGRESSIONS-lines=$(grep -c '^REGRESSIONS' "$B/logs/CONTROL-clbdtp01.B.log") last=$(tail -1 "$B/logs/CONTROL-clbdtp01.B.log" | cut -c1-120)"
echo BASELINES-END
