#!/bin/bash
# Desk KS part 3 (bench, 2026-10-01): each HC1 Crc32/Paxos cell's own ctl/post-end-1.tsv, the cell watcher's meter at END
# (at_end_T, at_end_COST, final_T, final_COST). Run ON THE RUN BOX: bash gather_hc1.sh > hc1_post_end.tsv. Cell ids and numbers only.
set -u
echo -e "root_arm\tcell\tat_end_T\tat_end_COST\tfinal_T\tfinal_COST"
for r in "$HOME"/cells-hc1-crc32-* "$HOME"/cells-hc1-paxos-*; do
  # only a cell OF RECORD's id (hc1 + 2 letters + 2 digits); a set-aside directory (`<id>.<reason>`) is counted, never named,
  # because its name can carry a host or account word (the infra-names gate refused the first gather on exactly that)
  aside=$(ls -d "$r"/hc1*.* 2>/dev/null | wc -l | tr -d ' '); [ "$aside" = 0 ] || echo -e "# ${r##*/cells-hc1-}: $aside set-aside dir(s) skipped"
  for c in "$r"/hc1*; do
    case "${c##*/}" in hc1[a-z][a-z][0-9][0-9]) : ;; *) continue ;; esac
    [ -r "$c/ctl/post-end-1.tsv" ] || { echo -e "${r##*/cells-hc1-}\t${c##*/}\tMISSING\tMISSING\tMISSING\tMISSING"; continue; }
    awk -F'\t' -v a="${r##*/cells-hc1-}" -v c="${c##*/}" 'NR==1{for(i=1;i<=NF;i++)h[$i]=i} NR==2{print a"\t"c"\t"$h["at_end_T"]"\t"$h["at_end_COST"]"\t"$h["final_T"]"\t"$h["final_COST"]}' "$c/ctl/post-end-1.tsv"
  done
done
