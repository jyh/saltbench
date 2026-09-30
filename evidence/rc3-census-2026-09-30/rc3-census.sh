#!/bin/bash
# rc3-census.sh — the helm's rc-3 census (bus 2026-09-29 16:42:28): re-score every cell of record whose published verdict is BUILD-FAIL 0/0,
# with the runner its phase uses, over a COPY of solution.rs at HEAD (and at the working tree when it differs), and classify by the runner's
# PRINTED reason (rc 3 = did not build | aborted | timed out). Output: $OUT/census.tsv. Per-test logs stay local.
set -u
T=${TASKS:?the private tasks/systems-v3 root}; O=${OUT:?a scratch output dir}; mkdir -p "$O"
set -a; . "$HOME/cells/toolchain.env"; set +a
printf 'cell\tpublished_in\trunner\tvariant\tsol_sha16\trc\tclass\ttests\tpassed_lines\treason\n' > "$O/census.tsv"
# cell | root | task | rung | published in
LIST='b22d1000 cells-specchange-2 Paxos B RESULT-p1-specchange-2026-09-10
clbczs01 cells-clb-sc-lzw-saltdiet LZW B RESULT-claude-blockSC-2026-09-21
clbczs02 cells-clb-sc-lzw-saltdiet LZW B RESULT-claude-blockSC-2026-09-21
clbgfs02 cells-clb-sg-freelist-saltdiet FreeList G RESULT-claude-blockSG-2026-09-21
clbszs02 cells-clb-ss-lzw-saltdiet LZW G RESULT-claude-blockSS-2026-09-21
clbufs02 cells-clb-sbs-freelist-saltdiet FreeList G RESULT-claude-blockSBS-2026-09-21
l8fpsr03 cells-l8-freelist-pro-salt-sc-rerun FreeList B RESULT-gemini-level8-chainF-2026-09-24
av02lzw cells-agy-pilot2 LZW G RESULT-agy-lzw-scored-2026-09-10'
while read -r c root task rung pub; do
  [ -n "$c" ] || continue
  mkdir -p "$O/$c/head" "$O/$c/wt"
  ssh "${RUN_HOST:?the run box}" "git -C ~/$root/$c/repo show HEAD:solution.rs" > "$O/$c/head/solution.rs" 2>/dev/null < /dev/null
  scp -q "${RUN_HOST:?the run box}:$root/$c/repo/solution.rs" "$O/$c/wt/solution.rs" 2>/dev/null < /dev/null
  vars="head"; cmp -s "$O/$c/head/solution.rs" "$O/$c/wt/solution.rs" || vars="head wt"
  for v in $vars; do
    D="$O/$c/$v"; sha=$(shasum -a 256 "$D/solution.rs" | cut -c1-16)
    sh "$T/$task/$rung/run_tests.sh" "$D" > "$D/run.out" 2>&1; rc=$?
    reason=-
    case $rc in 0) cls=PASS;; 4) cls=REFUSE;;
      3) if grep -q 'did not finish inside' "$D/run.out"; then cls=TIMEOUT; reason=$(grep -m1 'did not finish inside' "$D/run.out" | sed 's/^ *//');
         elif grep -q -E '^error(\[E[0-9]+\])?:' "$D/run.out"; then cls=BUILD-FAIL; reason="$(grep -c -E '^error(\[E[0-9]+\])?:' "$D/run.out") compile error(s)";
         else cls=ABORT; reason=$(tail -1 "$D/run.out" | cut -c1-80); fi;;
      *) cls=FAIL;; esac
    tests=$(sed -n 's/^TESTS //p' "$D/run.out" | tail -1); pl=$(grep -c '^PASS ' "$D/run.out")
    printf '%s\t%s\t%s/%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' "$c" "$pub" "$task" "$rung" "$v" "$sha" "$rc" "$cls" "${tests:--}" "$pl" "$reason" >> "$O/census.tsv"
  done
done <<EOF_L
$LIST
EOF_L
echo CENSUS-DONE >> "$O/census.tsv.done"
