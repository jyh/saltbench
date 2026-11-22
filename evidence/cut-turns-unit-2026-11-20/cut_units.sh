#!/bin/bash
# read-only: per cell (stdin: root id ...), timeout EVENTS (^AGY_ERROR lines containing 'timeout', and all ^AGY_ERROR) and
# 'print timeout' LINES, for agy-stderr-1.txt and agy-turnloop-stderr-1.txt separately
cd "$HOME" || exit 2
while read -r root id rest; do
  c="$root/$id/ctl"
  out="$id"
  for f in agy-stderr-1.txt agy-turnloop-stderr-1.txt; do
    p="$c/$f"
    if [ -f "$p" ]; then
      ae=$(/usr/bin/grep -c '^AGY_ERROR' "$p"); aet=$(/usr/bin/grep '^AGY_ERROR' "$p" | /usr/bin/grep -c 'timeout'); pl=$(/usr/bin/grep -c 'print timeout' "$p")
      out="$out	$f:agy_err=$ae,agy_err_timeout=$aet,pt_lines=$pl"
    else out="$out	$f:NOFILE"; fi
  done
  printf '%s\n' "$out"
done
