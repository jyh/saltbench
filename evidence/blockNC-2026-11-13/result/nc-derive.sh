#!/bin/bash
# nc-derive.sh <out-dir> — block NC's per-cell table FROM THE OBJECTS, never typed (block WC's wc-derive.sh, re-cut for NC's 72).
#   The POPULATION is NC_SOURCES in the export's clb_stage.sh (72 rows: model, problem, arm, n, source), read by git show, never listed here.
#   The phase-2 cell is FOUND, not named: the cell under cells-clb-nc{o|s}-<problem>-<arm> whose ctl/copied-from.tsv copied_from_id is
#   the source's id. No phase-2 cell: REACH-LOSS when the source did not land; REACH-LOSS-G when it landed and its G baseline (gbase.sh's
#   log under ~/bench-dry/nc-fresh-baselines-*/logs) did not pass in full; NO-PHASE-2 otherwise (not fired yet: a result is not cut then).
#   Read-only on the run box. The withheld B suite runs HERE over a COPY of solution.rs, from a local root extracted from the export
#   (harness + the two task trees). The scored object is the WORKING TREE when solution.rs is dirty, else HEAD (score_claude_v3's rule,
#   the one the lane's drivers applied at each harvest).
set -u
# RUN_HOST=local runs the box-side reads here (the derive runs ON the run box when the scoring host is under a disk hold)
rh(){ if [ "$H" = local ]; then bash -c "$1"; else ssh "$H" "$1"; fi; }
OUT=$(mkdir -p "${1:?out dir}" && cd "$1" && pwd) || exit 2; H=${RUN_HOST:?the run box ssh name}; RH=${RUN_HOME:?the run box home}
SYS=${SYSTEMS_CLONE:?a local saltbench-systems clone holding the export}; EXP=${EXPORT_SHA:?the block export sha}
RUNEXP=${RUN_EXPORT:?the export dir under the run box home}; TC=${TOOLCHAIN_ENV:?the suite runner toolchain env}
R=$OUT/root; mkdir -p "$OUT/sol" "$R"
if [ ! -d "$R/harness/systems-v3" ]; then
  ( cd "$SYS" && git archive "$EXP" harness/systems-v3 tasks/systems-v3 | tar -x -C "$R" )
  git -C "$SYS" rev-parse "$EXP" > "$R/EXPORTED-FROM.sha"
fi
# fail closed: a root without both B runners scores every row rc 127 with no TESTS line (the first run of this script did exactly that)
SRCS=$([ -n "${SOURCES_FILE:-}" ] && cat "$SOURCES_FILE" || git -C "$SYS" show "$EXP:harness/systems-v3/clb_stage.sh" | awk '/^NC_SOURCES=/{f=1; sub(/^NC_SOURCES=./,"")} f{l=$0; gsub(/\x27/,"",l); print l} f&&/\x27$/{exit}')
[ "$(printf '%s\n' "$SRCS" | grep -c .)" = 72 ] || { echo "REFUSE: NC_SOURCES did not read as 72 rows"; exit 2; }
for P in $(printf '%s\n' "$SRCS" | awk '{print $2}' | sort -u); do [ -f "$R/tasks/systems-v3/$P/B/run_tests.sh" ] || { echo "REFUSE: no $P B runner under $R"; exit 2; }; done
set -a; . "$TC"; set +a
printf 'cell\tproblem\tarm\tmodel_block\tn\tsource\tsource_end1\tend2_kind\tscored\ttests\tregressions_failed\tclause_failed\tbrc\tfinal_T\tfinal_COST\tcap_unit\tcap\tcapped\tserved_verdict\tserved_head\texport12\tsol_sha16\n' > "$OUT/cells.tsv"
printf '%s\n' "$SRCS" | while read -r M P A N SRC; do
  B=$([ "$M" = Opus ] && echo NCO || echo NCS); cond=$([ "$M" = Opus ] && echo opus || echo sonnet)
  pl=$(echo "$P" | tr A-Z a-z); ad=$([ "$A" = plain ] && echo plain || echo saltdiet); SID=$(basename "$SRC")
  RT=cells-clb-$(echo $B | tr A-Z a-z)-$pl-$ad; S=$RH/$SRC
  ID=$(rh "for c in $RH/$RT/clb*; do [ -f \$c/ctl/copied-from.tsv ] && awk -F'\\t' -v s=$SID '\$1==\"copied_from_id\" && \$2==s{f=1} END{exit !f}' \$c/ctl/copied-from.tsv && basename \$c; done" < /dev/null | head -1)
  C=$RH/$RT/${ID:-none}
  se1=$(rh "head -1 $S/ctl/end-1 2>/dev/null | awk '{print \$2}'" < /dev/null); [ -n "$se1" ] || se1=NO-END-1
  ex=$(rh "test -f $C/ctl/end-2 && echo Y" < /dev/null)
  if [ "$ex" != Y ]; then
    pe=$(rh "tail -1 $S/ctl/post-end-1.tsv 2>/dev/null" < /dev/null)
    k=REACH-LOSS
    if [ "$se1" = LANDED ]; then
      gl=$(rh "grep -h '^TESTS ' ~/bench-dry/nc-fresh-baselines-*/logs/$SID.G.log 2>/dev/null | tail -1" < /dev/null)
      if [ -n "$gl" ]; then gp=${gl#TESTS }; [ "${gp%%/*}" = "${gp##*/}" ] && [ "${gp##*/}" != 0 ] && k=NO-PHASE-2 || k=REACH-LOSS-G; else k=NO-PHASE-2; fi
      [ -z "$ID" ] && ex=N
    fi
    printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t-\t-\t-\t-\t-\t%s\t%s\t%s\t%s\t-\t-\t-\t-\t-\n' "$(basename $SRC)" $P $A $B $N "$SRC" "$se1" $k \
      "$(printf '%s' "$pe" | cut -f4)" "$(printf '%s' "$pe" | cut -f5)" "$(printf '%s' "$pe" | cut -f8)" "$(printf '%s' "$pe" | cut -f9)" >> "$OUT/cells.tsv"
    continue
  fi
  kind=$(rh "head -1 $C/ctl/end-2 | awk '{print \$2}'" < /dev/null)
  pe=$(rh "tail -1 $C/ctl/post-end-2.tsv 2>/dev/null" < /dev/null)
  fT=$(printf '%s' "$pe" | cut -f4); fC=$(printf '%s' "$pe" | cut -f5); cu=$(printf '%s' "$pe" | cut -f8); cap=$(printf '%s' "$pe" | cut -f9)
  capped=$([ "$kind" = CAP-COST ] && echo yes || echo no)
  exp12=$(rh "for f in \$(ls -t ~/bench-dry/clb/stage-$ID-*.log); do head -1 \$f | grep -q 'dry=0' && { head -1 \$f | sed -n 's/.* export=\([0-9a-f]*\).*/\1/p'; break; }; done" < /dev/null)
  cfg=$(rh "awk -F'\\t' '\$1==\"cfg\"{v=\$2} END{print v}' $C/ctl/run-cfg.tsv" < /dev/null)
  sv=$(rh "python3 ~/$RUNEXP/harness/systems-v3/served_models_v3.py check-cell --condition $cond --slug $cfg/projects/$(echo $C/repo | tr / -) --cell $C 2>&1" < /dev/null)
  svv=$(printf '%s\n' "$sv" | sed -n 's/.*set_verdict \([a-z]*\).*/\1/p' | head -1); svh=$(printf '%s\n' "$sv" | sed -n 's/^ *served head *//p' | head -1)
  dirty=$(rh "git -C $C/repo status --porcelain -- solution.rs | wc -l | tr -d ' '" < /dev/null)
  mkdir -p "$OUT/sol/$ID"
  if [ "$dirty" != 0 ]; then rh "cat $C/repo/solution.rs" > "$OUT/sol/$ID/solution.rs" < /dev/null; sc=WORKING-TREE
  else rh "git -C $C/repo show HEAD:solution.rs" > "$OUT/sol/$ID/solution.rs" < /dev/null; sc=HEAD; fi
  sh "$R/tasks/systems-v3/$P/B/run_tests.sh" "$OUT/sol/$ID" > "$OUT/sol/$ID/b.out" 2>&1; brc=$?
  t=$(grep '^TESTS ' "$OUT/sol/$ID/b.out" | tail -1 | cut -d' ' -f2); rg=$(grep '^REGRESSIONS ' "$OUT/sol/$ID/b.out" | tail -1 | cut -d' ' -f2)
  cl=$(grep '^CLAUSE_TESTS ' "$OUT/sol/$ID/b.out" | tail -1 | cut -d' ' -f2); sh16=$(shasum -a 256 "$OUT/sol/$ID/solution.rs" | cut -c1-16)
  printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' $ID $P $A $B $N "$SRC" "$se1" "$kind" $sc \
    "${t:--}" "${rg:--}" "${cl:--}" $brc "${fT:--}" "${fC:--}" "${cu:--}" "${cap:--}" $capped "${svv:--}" "${svh:--}" "${exp12:--}" $sh16 >> "$OUT/cells.tsv"
done
n=$(($(wc -l < "$OUT/cells.tsv")-1)); u=$(tail -n +2 "$OUT/cells.tsv" | cut -f1 | sort -u | wc -l | tr -d ' '); echo "rows $n unique $u"
# the population asserts itself: two writers into one file read as 32 rows on 2026-11-17 (a killed run's loop subshell survived)
[ "$n" = 72 ] && [ "$u" = 72 ] || { echo "REFUSE: $n rows, $u unique ids; the population is 72"; exit 3; }
