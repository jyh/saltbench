#!/bin/bash
# O60 §R4: `.claude/` in each cell's JUDGED tree, read from the archived cell repo at the harness pin (HARVEST.tsv col 10).
# usage: r4_judged_claude_census.sh <root> <HARVEST.tsv>   — prints cell, pin, resolved commit, .claude entries
root=$1; h=$2
printf 'cell\tpin\tcommit\tclaude_entries\n'
tail -n +2 "$h" | cut -f1,10 | while IFS=$'\t' read -r cell pin; do
  arm=plain; case $cell in clbps*) arm=saltdiet;; esac
  g="$root/cells-clb-x86p-o60-$arm/$cell/repo/.git"
  sha=${pin#*@}
  c=$(git --git-dir="$g" rev-parse --verify -q "$sha^{commit}") || { printf '%s\t%s\tUNRESOLVED\t-\n' "$cell" "$pin"; continue; }
  n=$(git --git-dir="$g" ls-tree -r --name-only "$c" | awk '$0 ~ /(^|\/)\.claude(\/|$)/' | wc -l | tr -d ' ')
  printf '%s\t%s\t%s\t%s\n' "$cell" "$pin" "$c" "$n"
done
