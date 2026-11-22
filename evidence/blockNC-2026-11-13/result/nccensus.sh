#!/bin/bash
# nccensus.sh <sources-file> — RUN ON THE RUN BOX. For each NC_SOURCES row: the phase-2 cell found by copied_from_id and its end-2 kind,
# else the source's end-1 kind. Prints one line per row and a tally. Read-only.
while read -r M P A N SRC; do
  B=$([ "$M" = Opus ] && echo nco || echo ncs); pl=$(echo "$P" | tr A-Z a-z); ad=$([ "$A" = plain ] && echo plain || echo saltdiet)
  RT=$HOME/cells-clb-$B-$pl-$ad; SID=$(basename "$SRC"); ID=
  for c in "$RT"/clb*; do
    [ -f "$c/ctl/copied-from.tsv" ] && awk -F'\t' -v s="$SID" '$1=="copied_from_id" && $2==s{f=1} END{exit !f}' "$c/ctl/copied-from.tsv" && { ID=$(basename "$c"); break; }
  done
  if [ -n "$ID" ] && [ -f "$RT/$ID/ctl/end-2" ]; then k="P2:$(head -1 "$RT/$ID/ctl/end-2" | awk '{print $2}')"
  elif [ -n "$ID" ]; then k="P2:RUNNING-OR-NO-END"
  else k="NOP2:src-$(head -1 "$HOME/$SRC/ctl/end-1" 2>/dev/null | awk '{print $2}')"; fi
  echo "$M $P $A $N $SID ${ID:--} $k"
done < "$1"
