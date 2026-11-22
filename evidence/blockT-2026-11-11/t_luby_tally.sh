#!/bin/bash
# t_luby_tally.sh — block T's Luby cells of record, read from each cell's own ctl/ on the run box (no figure typed).
# One row per cell: cell, model (TO = opus, TS = sonnet), arm, final_T, final_COST, cap, pool NUMBER (1 = the config dir the tripwire
# T-T-O clbvys01 ran under, which ADDENDUM 2 registers as the first pool; 2 = any other; no account or path is printed), the withheld-G score line is
# NOT read here (it is computed on the lead's box by tscore.sh); the result cites both.
set -u
P1=$(awk -F'\t' '$1=="cfg"{print $2}' "$HOME/cells-clb-to-luby-saltdiet/clbvys01/ctl/run-cfg.tsv")
[ -n "$P1" ] || { echo 'REFUSE: no first-pool reference (clbvys01 run-cfg)'; exit 3; }
printf 'cell\tblock\tarm\tfinal_T\tfinal_COST\tcap\tcapped\tpool\n'
for spec in TO:luby-saltdiet:clbvys TO:luby-plain:clbvyp TS:luby-saltdiet:clbrys TS:luby-plain:clbryp; do
  blk=${spec%%:*}; rest=${spec#*:}; root=${rest%%:*}; pre=${rest#*:}
  arm=salt-diet; [ "${root#luby-}" = plain ] && arm=plain
  for n in 01 02 03; do
    c=$HOME/cells-clb-$(echo $blk | tr A-Z a-z)-$root/$pre$n
    [ -f "$c/ctl/end-1" ] || { printf '%s\t%s\t%s\tNOT-ENDED\n' "$pre$n" "$blk" "$arm"; continue; }
    awk -F'\t' -v id="$pre$n" -v b="$blk" -v a="$arm" -v pool="$( [ "$(awk -F'\t' '$1=="cfg"{print $2}' "$c/ctl/run-cfg.tsv")" = "$P1" ] && echo 1 || echo 2)" \
      'NR==2{capped=($5+0>$9+0)?"yes":"no"; printf "%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n", id,b,a,$4,$5,$9,capped,pool}' "$c/ctl/post-end-1.tsv"
  done
done
