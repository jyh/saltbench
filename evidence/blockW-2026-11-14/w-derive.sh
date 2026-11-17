#!/bin/bash
# w-derive.sh <out-dir> — block W's per-cell table FROM THE OBJECTS (block NO's cells.tsv columns), never typed.
#   Read-only on the run box. The withheld suite runs HERE over a COPY of each cell (score_claude_v3.py, the scorer of record for this
#   block per wnext.sh), from a local root extracted from export 0916ef9a (harness + tasks), which W's cells ran.
#   A cell with no ctl/end-1 is written NO-END-1 with no score (never scored mid-run).
set -u
OUT=${1:?out dir}; H=${RUN_HOST:?the run box ssh name}; RH=${RUN_HOME:?the run box home}; SYS=${SYSTEMS_CLONE:?a local saltbench-systems clone holding 0916ef9a}
R=$OUT/root; mkdir -p "$OUT/cells" "$R"
if [ ! -d "$R/harness/systems-v3" ]; then
  ( cd "$SYS" && git archive 0916ef9a harness/systems-v3 tasks/systems-v3/WHT tasks/systems-v3/NTT | tar -x -C "$R" )
  git -C "$SYS" rev-parse 0916ef9a > "$R/EXPORTED-FROM.sha"
fi
set -a; . "${TOOLCHAIN_ENV:?the suite runner toolchain env}"; set +a
printf 'cell\tproblem\tarm\tmodel_block\tend1_kind\tend_from\tsuite\ttests\tfinal_T\tfinal_COST\tcap_unit\tcap\tcapped\tserved_verdict\tserved_head\texport12\n' > "$OUT/cells.tsv"
for B in WO WS; do b=$([ $B = WO ] && echo d || echo i)
 for P in WHT NTT; do p=$([ $P = WHT ] && echo w || echo t); pl=$(echo $P | tr A-Z a-z)
  for A in plain salt-diet; do a=$([ $A = plain ] && echo p || echo s); ad=$([ $A = plain ] && echo plain || echo saltdiet)
   for n in 1 2 3; do ID=clb$b$p${a}0$n; RT=cells-clb-$(echo $B | tr A-Z a-z)-$pl-$ad; C=$RH/$RT/$ID
    ex=$(ssh "$H" "test -d $C && echo Y" < /dev/null)
    if [ "$ex" != Y ]; then printf '%s\t%s\t%s\t%s\tNOT-STAGED\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\n' $ID $P $A $B >> "$OUT/cells.tsv"; continue; fi
    kind=$(ssh "$H" "head -1 $C/ctl/end-1 2>/dev/null | awk '{print \$2}'" < /dev/null); [ -n "$kind" ] || kind=NO-END-1
    exp12=$(ssh "$H" "awk -F'\\t' '\$1==\"export_sha\"{print substr(\$2,1,12)}' $C/ctl/built-from.tsv" < /dev/null)
    pe=$(ssh "$H" "tail -1 $C/ctl/post-end-1.tsv 2>/dev/null" < /dev/null)
    fT=$(printf '%s' "$pe" | cut -f4); fC=$(printf '%s' "$pe" | cut -f5); cu=$(printf '%s' "$pe" | cut -f8); cap=$(printf '%s' "$pe" | cut -f9)
    capped=$( [ "$kind" = CAP-COST ] && echo yes || echo no )
    cfg=$(ssh "$H" "awk -F'\\t' '\$1==\"cfg\"{print \$2}' $C/ctl/run-cfg.tsv" < /dev/null)
    cond=$([ $B = WO ] && echo opus || echo sonnet)
    sv=$(ssh "$H" "python3 ~/${RUN_EXPORT:?the export dir under the run box home}/harness/systems-v3/served_models_v3.py check-cell --condition $cond --slug $cfg/projects/${RH//\//-}-$RT-$ID-repo --cell $C 2>&1" < /dev/null)
    svv=$(printf '%s\n' "$sv" | sed -n 's/.*set_verdict \([a-z]*\).*/\1/p' | head -1); svh=$(printf '%s\n' "$sv" | sed -n 's/^ *served head *//p' | head -1)
    suite=-; tests=-; ef=-
    if [ "$kind" != NO-END-1 ]; then
      rsync -a --exclude repo/target "$H:$C" "$OUT/cells/" && echo "$OUT/cells/$ID" > "$OUT/decl-$ID"
      sc=$(python3 "$R/harness/systems-v3/score_claude_v3.py" --tasks "$R/tasks/systems-v3" --declared "$OUT/decl-$ID" --toolchain-env "$TOOLCHAIN_ENV" 2>"$OUT/score-$ID.err" | awk -F'\t' -v id=$ID '$1==id{print $8"\t"$9"\t"$NF}')
      suite=$(printf '%s' "$sc" | cut -f1); tests=$(printf '%s' "$sc" | cut -f2); ef=$(printf '%s' "$sc" | cut -f3 | sed -n 's/.*end read from \([A-Za-z -]*\).*/\1/p')
      [ -n "$suite" ] || suite=UNSCORED; [ -n "$ef" ] || ef=-
    fi
    printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' $ID $P $A $B "$kind" "$ef" "$suite" "$tests" "${fT:--}" "${fC:--}" "${cu:--}" "${cap:--}" $capped "${svv:--}" "${svh:--}" "${exp12:--}" >> "$OUT/cells.tsv"
   done; done; done; done
echo "rows $(($(wc -l < "$OUT/cells.tsv")-1))"
