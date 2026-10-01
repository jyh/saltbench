#!/bin/bash
# o37-derive.sh <out-dir> <local tasks/systems-v3 root>   — the O37 Aeneas pilot (AMENDMENT-O37-aeneas-pilot-2026-09-30): derive the
#   RESULT's cell table FROM THE OBJECTS, never typed. Read-only on the run box. The hidden suite runs HERE (the withheld tests never reach
#   the run box) over a COPY of each cell's solution.rs; the Lean half runs ON the run box through the export's own o37_score.sh, in
#   scoring mode (confined, the three use-time controls), which copies the end tree and writes nothing into the cell.
#   cells.tsv  one row per block-A cell: end-1 kind · dirty · suite · tests · O37-LEAN · axioms · O37-STMT · PASS (§A3: suite FULL PASS ∧ LEAN
#              GREEN ∧ STMT UNCHANGED) · proof lines · meter (post-end-1) · served head/sidechain · client versions · export · head · runner sha16
#   A cell with no ctl/end-1 is written with kind NO-END-1 and NO score (never scored mid-run).
set -u
OUT=${1:?out dir}; TASKS=${2:?local tasks root}
H=${RUN_HOST:?the run box ssh name}; EXP=${RUN_EXPORT:?the export dir under the run box home}; POOL_CFG=${POOL_CFG:?the pool config dir on the run box}
RH=${RUN_HOME:?the run box home}; AROOT=${O37_ROOT_ON_BOX:?the Aeneas root on the run box}
mkdir -p "$OUT/sol"
set -a; . "$HOME/cells/toolchain.env"; set +a   # the suite runner's toolchain contract (run_tests.sh -> _common_v3.sh)
CELLS='clbeca01 opus cells-clb-ao-crc32-lean-aeneas
clbwca01 sonnet cells-clb-as-crc32-lean-aeneas
clbeca02 opus cells-clb-ao-crc32-lean-aeneas
clbwca02 sonnet cells-clb-as-crc32-lean-aeneas
clbeca03 opus cells-clb-ao-crc32-lean-aeneas
clbwca03 sonnet cells-clb-as-crc32-lean-aeneas'
printf 'cell\tcondition\tend1_kind\tdirty\tsuite\ttests\to37_lean\to37_axioms\to37_stmt\tPASS\tproof_lines\tfinal_T\tfinal_COST\tat_end_COST\tcap\tserved_head\tserved_sidechain\tserved_verdict\tclient_versions\texport12\thead12\tG_runner_sha16\n' > "$OUT/cells.tsv"
while read -r ID COND R; do
  [ -n "$ID" ] || continue
  C=$RH/$R/$ID
  e1=$(ssh "$H" "head -1 $C/ctl/end-1 2>/dev/null" < /dev/null)
  kind=$(printf '%s' "$e1" | awk '{print $2}'); [ -n "$kind" ] || kind=NO-END-1
  head=$(ssh "$H" "git -C $C/repo rev-parse --short=12 HEAD" < /dev/null)
  dirty=$(ssh "$H" "git -C $C/repo status --porcelain | wc -l | tr -d ' '" < /dev/null)
  exp12=$(ssh "$H" "awk -F'\\t' '\$1==\"export_sha\"{print substr(\$2,1,12)}' $C/ctl/built-from.tsv" < /dev/null)
  pe=$(ssh "$H" "tail -1 $C/ctl/post-end-1.tsv 2>/dev/null" < /dev/null)
  fT=$(printf '%s' "$pe" | cut -f4); fC=$(printf '%s' "$pe" | cut -f5); aC=$(printf '%s' "$pe" | cut -f3); cap=$(printf '%s' "$pe" | cut -f9)
  slug="$POOL_CFG/projects/${RH//\//-}-$R-$ID-repo"
  sv=$(ssh "$H" "python3 ~/$EXP/harness/systems-v3/served_models_v3.py check-cell --condition $COND --slug $slug --cell $C 2>&1" < /dev/null)
  sh_=$(printf '%s\n' "$sv" | sed -n 's/^ *served head *//p'); ss_=$(printf '%s\n' "$sv" | sed -n 's/^ *served sidechain *//p')
  svv=$(printf '%s\n' "$sv" | sed -n 's/.*set_verdict \([a-z]*\).*/\1/p' | head -1)
  vers=$(ssh "$H" "cat $slug/*.jsonl 2>/dev/null | python3 -c 'import sys,json
v=set()
for l in sys.stdin:
  try: v.add(json.loads(l).get(\"version\") or \"\")
  except Exception: pass
print(\",\".join(sorted(x for x in v if x)))'" < /dev/null)
  suite=-; tests=-; lean=-; ax=-; stmt=-; pass=-; plines=-
  if [ "$kind" != NO-END-1 ]; then
    mkdir -p "$OUT/sol/$ID"
    # the WORKING TREE is the registered end state (the scorer's rule); a dirty count other than 0 is printed beside the verdict
    ssh "$H" "cat $C/repo/solution.rs" > "$OUT/sol/$ID/solution.rs" < /dev/null
    ssh "$H" "cat $C/repo/proof/Proof.lean" > "$OUT/sol/$ID/Proof.lean" < /dev/null
    plines=$(wc -l < "$OUT/sol/$ID/Proof.lean" | tr -d ' ')
    sh "$TASKS/Crc32/G/run_tests.sh" "$OUT/sol/$ID" > "$OUT/sol/$ID/g.out" 2>&1; grc=$?
    case $grc in 0) suite=PASS;; 4) suite=REFUSE;;
      3) if grep -q 'did not finish inside' "$OUT/sol/$ID/g.out"; then suite=TIMEOUT; elif grep -q 'did not build with the harness' "$OUT/sol/$ID/g.out"; then suite=BUILD-FAIL; else suite=ABORT; fi;;
      *) suite=FAIL;; esac
    tests=$(sed -n 's/^TESTS //p' "$OUT/sol/$ID/g.out" | tail -1)
    ssh "$H" "O37_ROOT=$AROOT bash ~/$EXP/harness/systems-v3/o37/o37_score.sh ~/$EXP/harness/systems-v3 $C" > "$OUT/sol/$ID/o37.out" 2>&1 < /dev/null
    lean=$(sed -n 's/^O37-LEAN [^ ]* \([A-Z]*\) .*/\1/p' "$OUT/sol/$ID/o37.out")
    ax=$(sed -n 's/^O37-AXIOMS [^ ]* O37AX-AXIOMS \[\([^]]*\)\].*/\1/p' "$OUT/sol/$ID/o37.out" | tr -d ' ')
    stmt=$(sed -n 's/^O37-STMT [^ ]* \([A-Z]*\).*/\1/p' "$OUT/sol/$ID/o37.out")
    if [ "$suite" = PASS ] && [ "$lean" = GREEN ] && [ "$stmt" = UNCHANGED ]; then pass=PASS; else pass=NO; fi
  fi
  rsha=$(shasum -a 256 "$TASKS/Crc32/G/run_tests.sh" | cut -c1-16)
  printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' "$ID" "$COND" "$kind" "$dirty" "$suite" "${tests:--}" \
    "${lean:--}" "${ax:--}" "${stmt:--}" "$pass" "$plines" "${fT:--}" "${fC:--}" "${aC:--}" "${cap:--}" "${sh_:--}" "${ss_:--}" "${svv:--}" "${vers:--}" \
    "${exp12:--}" "$head" "$rsha" >> "$OUT/cells.tsv"
done <<EOF_C
$CELLS
EOF_C
echo "o37-derive: $(($(wc -l < "$OUT/cells.tsv")-1)) cell rows"
