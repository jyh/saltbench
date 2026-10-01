#!/bin/bash
# Desk KS (bench, 2026-10-01): the token columns beside the dollar columns the two Claude-row x86 CRC-32 RESULTs quote, read from each
# cell's own ctl/post-end-1.tsv (the file both RESULTs name: at_end_COST = col 3, final_COST = col 5; at_end_T = col 2, final_T = col 4).
# Run ON THE RUN BOX:  bash gather.sh > tokens.tsv     It prints cell ids and numbers only; a cell it cannot find prints MISSING.
set -u
echo -e "cell\tat_end_T\tat_end_COST\tfinal_T\tfinal_COST"
for c in clbqcp01 clbqcs01 clbqcp02 clbqcs02 clbqcp03 clbqcs03 clbkcp01 clbkcs01 clbkcp02 clbkcs02 clbkcp03 clbkcs03; do
  f=$(ls -d "$HOME"/cells-clb-x86*/"$c" 2>/dev/null | head -1)
  if [ -n "$f" ] && [ -r "$f/ctl/post-end-1.tsv" ]; then awk -F'\t' -v c="$c" 'NR==2{print c"\t"$2"\t"$3"\t"$4"\t"$5}' "$f/ctl/post-end-1.tsv"
  else echo -e "$c\tMISSING\tMISSING\tMISSING\tMISSING"; fi
done
