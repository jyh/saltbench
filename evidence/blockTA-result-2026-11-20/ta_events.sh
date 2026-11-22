#!/bin/bash
# read-only: per TA cell of record, timeout EVENTS (^AGY_ERROR) and the scorer's LINE count ("print timeout"), phase-1 stderr
cd "$HOME" || exit 2
for d in cells-ta-*-flash-* cells-ta-*-argon-*; do
  [ -d "$d" ] || continue
  for c in "$d"/ta*; do
    [ -d "$c/ctl" ] || continue
    f="$c/ctl/agy-stderr-1.txt"
    if [ -f "$f" ]; then e=$(/usr/bin/grep -c '^AGY_ERROR' "$f"); l=$(/usr/bin/grep -c 'print timeout' "$f"); else e=NOFILE; l=NOFILE; fi
    printf '%s\t%s\t%s\t%s\n' "$(basename "$c")" "$d" "$e" "$l"
  done
done
