#!/bin/bash
# t-derive.sh <out-dir> — block T's per-cell table FROM THE OBJECTS, never typed (block NC's nc-derive.sh, re-cut for T's 72).
#   THE POPULATION is the registration's §T1 product (6 problems × {to,ts} × {plain,saltdiet}), each condition's directory
#   cells-clb-t{o|s}-<problem>-<arm> on the run box, whose clb* cells are LISTED there; the script refuses unless each condition
#   holds exactly 3 cells and the total is 72 unique ids.
#   The box-side facts come from t-box.sh (read-only, beside this file). The withheld G suite runs HERE over a COPY of each cell
#   (rsync, repo/target excluded), from a local root extracted by git archive from the release export; score_claude_v3.py decides
#   the scored object (the WORKING TREE when solution.rs is dirty, HEAD beside it non-scoring), as the lane's drivers did at harvest.
#   The statement line (salt-diet and plain alike, both arms carry the statement): stmtuse.py + specdefs.py against the section
#   extracted from the export; tnames (v2 needle) over tests/ and solution.rs.
set -u
OUT=$(mkdir -p "${1:?out dir}" && cd "$1" && pwd) || exit 2
H=${RUN_HOST:?run box ssh name}; RH=${RUN_HOME:?run box home}
SYS=${SYSTEMS_CLONE:?local saltbench-systems clone holding the export}; EXP=${EXPORT_SHA:?block export sha}
TC=${TOOLCHAIN_ENV:?suite runner toolchain env}
HERE=$(cd "$(dirname "$0")" && pwd)
# the sections come from the export's own cards (t-sections.py), unless SECTIONS_DIR names a prepared dir
R=$OUT/root; mkdir -p "$OUT/cells" "$OUT/box" "$OUT/score" "$R"
if [ ! -d "$R/harness/systems-v3" ]; then
  ( cd "$SYS" && git archive "$EXP" harness/systems-v3 tasks/systems-v3 | tar -x -C "$R" ) || exit 2
  git -C "$SYS" rev-parse "$EXP" > "$R/EXPORTED-FROM.sha"
fi
SEC=${SECTIONS_DIR:-$OUT/sections}; [ -d "$SEC" ] || python3 "$HERE/t-sections.py" "$R/tasks/systems-v3" "$SEC" || exit 2
PROBS="Luby AES Liveness MaxFlow BinomialHeap LinearScan"
for P in $PROBS; do
  [ -f "$R/tasks/systems-v3/$P/G/run_tests.sh" ] || [ -d "$R/tasks/systems-v3/$P/G" ] || { echo "REFUSE: no $P G suite under $R"; exit 2; }
  [ -s "$SEC/$(echo $P | tr A-Z a-z)-section.rs" ] || { echo "REFUSE: no $P section in $SEC"; exit 2; }
done
set -a; . "$TC"; set +a
printf 'cell\tproblem\tarm\tmodel_block\tn\tend1_kind\tend1_at\tscored\tsuite\ttests\tfailing\tat_end_COST\tfinal_T\tfinal_COST\tcap\tcapped\tserved_verdict\tserved_head\texport12\thead12\tsol_sha16\tsol_mtime\tverus_runs\tverus_last\tverus_last_clean\tstmt_named\tstmt_verbatim\tspecdefs\ttnames_tests\ttnames_sol\ttest_files\tborn_n\tborn_hits\tborn_names\tcontrol_own_id_hits\ttranscripts\tlaunch_birth\n' > "$OUT/cells.tsv"
for MB in to ts; do
  cond=$([ $MB = to ] && echo opus || echo sonnet)
  for P in $PROBS; do
    pl=$(echo $P | tr A-Z a-z); S=$SEC/$pl-section.rs
    for A in plain saltdiet; do
      D=$RH/cells-clb-$MB-$pl-$A
      ids=$(ssh "$H" "cd $D && ls -d clb*" < /dev/null 2>/dev/null | grep -E '^clb[a-z0-9]+$')
      [ "$(printf '%s\n' "$ids" | grep -c .)" = 3 ] || { echo "REFUSE: $D holds $(printf '%s\n' "$ids" | grep -c .) cells, not 3"; exit 3; }
      for ID in $ids; do
        C=$D/$ID; ssh "$H" "bash ~/bench-dry/t-box.sh $C $cond" < /dev/null 2>/dev/null > "$OUT/box/$ID.kv"
        g(){ awk -F'\t' -v k="$1" '$1==k{sub(/^[^\t]*\t/,""); print; exit}' "$OUT/box/$ID.kv"; }
        e1=$(g end1); kind=$(echo "$e1" | awk '{print $2}'); at=$(echo "$e1" | awk '{print $1}')
        post=$(g post); aec=$(echo "$post" | cut -d'|' -f3); fT=$(echo "$post" | cut -d'|' -f4); fC=$(echo "$post" | cut -d'|' -f5); cap=$(echo "$post" | cut -d'|' -f9)
        [ "$(g arm_ctl | tr -d -)" = "$A" ] && [ "$(g problem_ctl)" = "$P" ] || { echo "REFUSE: $ID ctl says $(g arm_ctl)/$(g problem_ctl), dir says $A/$P"; exit 3; }
        rsync -a --delete --exclude repo/target "$H:$C" "$OUT/cells/" 2>&1 | grep -v -iE 'quantum|decrypt|upgraded'
        echo "$OUT/cells/$ID" > "$OUT/score/decl-$ID"
        python3 "$R/harness/systems-v3/score_claude_v3.py" --tasks "$R/tasks/systems-v3" --declared "$OUT/score/decl-$ID" --toolchain-env "$TC" > "$OUT/score/$ID.out" 2> "$OUT/score/$ID.err"
        row=$(awk -F'\t' -v i=$ID '$1==i' "$OUT/score/$ID.out")
        [ -n "$row" ] || { echo "REFUSE: no score row for $ID (see $OUT/score/$ID.err)"; exit 4; }
        suite=$(echo "$row" | cut -f8); tests=$(echo "$row" | cut -f9); fail=$(echo "$row" | cut -f10); note=$(echo "$row" | cut -f16)
        case "$note" in "end read from working tree"*) sc=WORKING-TREE; cp "$OUT/cells/$ID/repo/solution.rs" "$OUT/score/$ID.sol.rs";;
                        "end read from HEAD"*) sc=HEAD; git -C "$OUT/cells/$ID/repo" show HEAD:solution.rs > "$OUT/score/$ID.sol.rs";;
                        *) echo "REFUSE: $ID score note unread: $note"; exit 4;; esac
        sh16=$(shasum -a 256 "$OUT/score/$ID.sol.rs" | cut -c1-16)
        su=$(python3 "$HERE/stmtuse.py" "$S" "$OUT/score/$ID.sol.rs" "$R/tasks/systems-v3/$P/G/interface.rs")
        named=$(echo "$su" | sed -n 's/^spec fns named //p'); verb=$(echo "$su" | sed -n 's/^section lines verbatim //p')
        sdo=$(python3 "$HERE/specdefs.py" "$S" "$OUT/score/$ID.sol.rs"); sd="$(echo "$sdo" | head -1 | sed -n 's/.*defined in solution \([0-9]*\) · identical (whitespace-normalised) \([0-9]*\) · DIFFERENT \([0-9]*\).*/defined=\1 same=\2 diff=\3/p') $(echo "$sdo" | awk '$1=="DIFF"{printf "%s%s", (n++?",":"DIFF:"), $2}')"
        tn=$(bash "$HERE/tnames.sh" "$S" "$OUT/cells/$ID"); tt=$(echo "$tn" | sed -n 's/.*tests-define \([0-9/]*\).*/\1/p'); ts=$(echo "$tn" | sed -n 's/.*solution-defines \([0-9/]*\).*/\1/p'); tf=$(echo "$tn" | sed -n 's/.*test files \([0-9]*\).*/\1/p')
        n=$(echo $ID | sed 's/.*\([0-9]\)$/\1/')
        printf '%s\t' $ID $P "$( [ $A = plain ] && echo plain || echo salt-diet)" $(echo $MB | tr a-z A-Z) $n "$kind" "$at" $sc "$suite" "$tests" "$fail" "${aec:--}" "${fT:--}" "${fC:--}" "${cap:--}" "$( [ "$kind" = CAP-COST ] && echo yes || echo no)" \
          "$(g served_verdict)" "$(g served_head)" "$(g export | cut -c1-12)" "$(g head)" $sh16 "$(g sol_mtime)" "$(g verus_runs)" "$(g verus_last)" "$(g verus_last_clean)" "$named" "$verb" "$sd" "$tt" "$ts" "$tf" \
          "$(g born_n)" "$(g born_hits)" "$(g born_names)" "$(g control_own_id_hits)" "$(g transcripts)" >> "$OUT/cells.tsv"
        printf '%s\n' "$(g launch_birth)" >> "$OUT/cells.tsv"
        echo "$ID $P $A $MB $kind $suite $tests" >&2
      done
    done
  done
done
n=$(($(wc -l < "$OUT/cells.tsv")-1)); u=$(tail -n +2 "$OUT/cells.tsv" | cut -f1 | sort -u | wc -l | tr -d ' '); echo "rows $n unique $u"
[ "$n" = 72 ] && [ "$u" = 72 ] || { echo "REFUSE: $n rows, $u unique ids; the population is 72"; exit 3; }
