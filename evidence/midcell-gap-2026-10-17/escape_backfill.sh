#!/bin/bash
# escape_backfill.sh < uncov.tsv (cell<TAB>root) — item 7 (c), relight 149. Runs ON THE RUN BOX, zero spend, reads only.
# The chain's own escape_scan.py, run after the fact on cells of record that never had one. The transcript dir is SEARCHED across every
# ~/.claude* config dir (pools moved); a cell with no transcript dir found is printed NO-TRANSCRIPT, never clean.
cd "$(dirname "$0")" || exit 2
while IFS=$(printf '\t') read -r cell root; do
  slug=$(printf '%s' "$HOME/$root/$cell/repo" | tr '/.' '--')
  set -- $HOME/.claude*/projects/$slug; d=$1
  if [ ! -d "$d" ]; then printf '%s\t%s\tNO-TRANSCRIPT\n' "$cell" "$root"; continue; fi
  out=$(python3 - "$d" "$root" < escape_scan.py 2>&1); printf '%s\t%s\t%s\t%s\n' "$cell" "$root" "$(basename "$(dirname "$(dirname "$d")")")" "$out"
done
