#!/bin/bash
# stepg-derive.sh <out-dir> <local tasks/systems-v3 root>   — step g (AMENDMENT-stepg-opus-specchange-2026-09-29): derive the RESULT's two
#   tables FROM THE OBJECTS, never typed. Read-only on the run box; the B rung runs HERE over a COPY of each cell's solution.rs at its HEAD.
#   cells.tsv  one row per block-G cell: end-2 kind · suite · tests · regressions/clause FAILED · meter (post-end-2) · served head/sidechain ·
#              client version · source + root · export · head sha · runner sha16
#   reach.tsv  per condition, the PHASE-1 REACH across the three source roots (cells-matrix1 · cells-n3-topup · cells-gf-topup-1): Opus ·
#              greenfield · none · card_extras none, landed / with an end-1. The helm's ruling makes this column MANDATORY in every row.
#   A cell with no ctl/end-2 is written as its row with kind NO-END-2 and NO score (never scored mid-run).
set -u
OUT=${1:?out dir}; TASKS=${2:?local tasks root}
H=${RUN_HOST:?the run box ssh name}; EXP=${RUN_EXPORT:?the harness export (9a3e6bf) path under the run box home, to its harness/systems-v3}
mkdir -p "$OUT/sol"
set -a; . "$HOME/cells/toolchain.env"; set +a
CELLS='clbkzp01 LZW plain cells-clb-g-lzw-plain
clbklp01 LRU plain cells-clb-g-lru-plain
clbkfp01 FreeList plain cells-clb-g-freelist-plain
clbkpp01 Paxos plain cells-clb-g-paxos-plain
clbkps01 Paxos salt-diet cells-clb-g-paxos-saltdiet
clbkfs01 FreeList salt-diet cells-clb-g-freelist-saltdiet
clbkfs02 FreeList salt-diet cells-clb-g-freelist-saltdiet'
printf 'cell\ttask\tarm\tend2_kind\tsuite\ttests\tregressions_failed\tclause_failed\tfinal_T\tfinal_COST\tat_end_COST\tcap\tserved_head\tserved_sidechain\tserved_verdict\tclient_versions\tsource\tsource_end12\texport12\thead12\tB_runner_sha16\n' > "$OUT/cells.tsv"
while read -r ID T A R; do
  [ -n "$ID" ] || continue
  C=${RUN_HOME:?the run box home}/$R/$ID
  e2=$(ssh "$H" "head -1 $C/ctl/end-2 2>/dev/null" < /dev/null)
  kind=$(printf '%s' "$e2" | awk '{print $2}'); [ -n "$kind" ] || kind=NO-END-2
  src=$(ssh "$H" "awk -F'\\t' '\$1==\"copied_from\"{print \$2}' $C/ctl/copied-from.tsv" < /dev/null | awk -F/ '{print $(NF-1)"/"$NF}')
  psha=$(ssh "$H" "awk -F'\\t' '\$1==\"parent_end_sha\"{print substr(\$2,1,12)}' $C/ctl/parent" < /dev/null)
  head=$(ssh "$H" "git -C $C/repo rev-parse --short=12 HEAD" < /dev/null)
  pe=$(ssh "$H" "tail -1 $C/ctl/post-end-2.tsv 2>/dev/null" < /dev/null)
  fT=$(printf '%s' "$pe" | cut -f4); fC=$(printf '%s' "$pe" | cut -f5); aC=$(printf '%s' "$pe" | cut -f3); cap=$(printf '%s' "$pe" | cut -f9)
  sv=$(ssh "$H" "python3 ~/$EXP/served_models_v3.py check-cell --condition opus --slug ${POOL_CFG:?the pool config dir on the run box}/projects/${RUN_HOME//\//-}-$R-$ID-repo --cell $C 2>&1" < /dev/null)
  sh_=$(printf '%s\n' "$sv" | sed -n 's/^ *served head *//p'); ss_=$(printf '%s\n' "$sv" | sed -n 's/^ *served sidechain *//p')
  svv=$(printf '%s\n' "$sv" | sed -n 's/.*set_verdict \([a-z]*\).*/\1/p' | head -1)
  vers=$(ssh "$H" "cat ${POOL_CFG:?the pool config dir on the run box}/projects/${RUN_HOME//\//-}-$R-$ID-repo/*.jsonl 2>/dev/null | python3 -c 'import sys,json
v=set()
for l in sys.stdin:
  try: v.add(json.loads(l).get(\"version\") or \"\")
  except Exception: pass
print(\",\".join(sorted(x for x in v if x)))'" < /dev/null)
  suite=-; tests=-; rg=-; cl=-
  if [ "$kind" != NO-END-2 ]; then
    mkdir -p "$OUT/sol/$ID"
    ssh "$H" "git -C $C/repo show HEAD:solution.rs" > "$OUT/sol/$ID/solution.rs" < /dev/null
    sh "$TASKS/$T/B/run_tests.sh" "$OUT/sol/$ID" > "$OUT/sol/$ID/b.out" 2>&1; brc=$?
    case $brc in 0) suite=PASS;; 4) suite=REFUSE;;
      3) if grep -q 'did not finish inside' "$OUT/sol/$ID/b.out"; then suite=TIMEOUT; else suite=BUILD-FAIL; fi;;   # rc 3 is three causes; the runner names which
      *) suite=FAIL;; esac
    tests=$(sed -n 's/^TESTS //p' "$OUT/sol/$ID/b.out" | tail -1); rg=$(sed -n 's/^REGRESSIONS //p' "$OUT/sol/$ID/b.out" | tail -1); cl=$(sed -n 's/^CLAUSE_TESTS //p' "$OUT/sol/$ID/b.out" | tail -1)
  fi
  rsha=$(shasum -a 256 "$TASKS/$T/B/run_tests.sh" | cut -c1-16)
  printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' "$ID" "$T" "$A" "$kind" "$suite" "${tests:--}" "${rg:--}" "${cl:--}" \
    "${fT:--}" "${fC:--}" "${aC:--}" "${cap:--}" "${sh_:--}" "${ss_:--}" "${svv:--}" "${vers:--}" "${src:--}" "${psha:--}" "9a3e6bf3450d" "$head" "$rsha" >> "$OUT/cells.tsv"
done <<EOF_C
$CELLS
EOF_C
# reach: every Opus greenfield none (extras none) phase-1 cell with an end-1 in the three roots, by task x arm
ssh "$H" 'for r in cells-matrix1 cells-n3-topup cells-gf-topup-1; do for c in ~/$r/*/; do c=${c%/}; [ -f $c/ctl/end-1 ] || continue; x=$(tr -d "\n" < $c/ctl/card_extras 2>/dev/null); [ "${x:-none}" = none ] || continue; m=$(awk -v i=$(basename $c) "\$1==i{print \$10}" ~/$r/CELLS.tsv); printf "%s\t%s\t%s\t%s\t%s\t%s\n" "$r" "$(basename $c)" "$(cut -f1 $c/ctl/task)" "$(head -1 $c/ctl/arm)" "$m" "$(head -1 $c/ctl/end-1 | awk "{print \$2}")"; done; done' < /dev/null > "$OUT/phase1-population.tsv"
printf 'task\tarm\tlanded\twith_end1\tnot_landed_kinds\n' > "$OUT/reach.tsv"
for ta in "LZW plain" "LRU plain" "FreeList plain" "Paxos plain" "Paxos salt-diet" "FreeList salt-diet"; do
  set -- $ta
  awk -F'\t' -v t="$1" -v a="$2" '$3==t && $4==a && $5=="claude-opus-5" { n++; if ($6=="LANDED") l++; else k[$6]++ }
    END { s=""; for (x in k) s=s x "=" k[x] " "; printf "%s\t%s\t%d\t%d\t%s\n", t, a, l, n, (s==""?"-":s) }' "$OUT/phase1-population.tsv" >> "$OUT/reach.tsv"
done
echo "stepg-derive: $(($(wc -l < "$OUT/cells.tsv")-1)) cell rows, $(($(wc -l < "$OUT/reach.tsv")-1)) reach rows, population $(wc -l < "$OUT/phase1-population.tsv") phase-1 cells"
