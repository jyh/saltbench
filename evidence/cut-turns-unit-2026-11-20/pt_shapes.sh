#!/bin/bash
# read-only: every agy-stderr-*.txt under ~/cells-* carrying 'print timeout': its three line shapes, the client stamp, mtime
cd "$HOME" || exit 2
for f in cells-*/*/ctl/agy-stderr-*.txt cells-*/*/ctl/agy-turnloop-stderr-*.txt; do
  [ -f "$f" ] || continue
  pl=$(/usr/bin/grep -c 'print timeout' "$f")
  [ "$pl" -gt 0 ] || continue
  a=$(/usr/bin/grep -c '^\[agy\] print timeout' "$f")
  e=$(/usr/bin/grep -c '^error: print timeout' "$f")
  j=$(/usr/bin/grep '^AGY_ERROR' "$f" | /usr/bin/grep -c 'print_timeout')
  cl=$(head -c 40 "$(dirname "$f")/client" 2>/dev/null | tr -d '\n\t' )
  m=$(stat -f %Sm -t %Y-%m-%d "$f")
  printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\n' "$m" "$f" "$pl" "$a" "$e" "$j" "${cl:-NOCLIENT}"
done
