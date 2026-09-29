#!/bin/bash
# YP step f input (run on the run box): cell_meter --json over EVERY CLAUDE-shape cell of record, one row per (cell, config dir), with
# the cell's own cost caps read from its ctl/budgets.env. The config-dir column is dropped before the file is tracked.
M=${CELL_METER:?set CELL_METER to the cell_meter.py of the harness export (export 9d873183acab)}
printf 'cell\troot\tcfg\tT\tCOST\tvoid\tC1_USD\tC2_USD\n'
while IFS=$'\t' read c r; do
  R=~/$r/$c/ctl/run-cfg.tsv; B=~/$r/$c/ctl/budgets.env
  S=$(printf '%s' "$HOME/$r/$c/repo" | sed 's#[/.]#-#g')
  if [ -s "$R" ]; then cfgs=$(awk -F'\t' '$1=="cfg"{print $2}' "$R" | sort -u)
  else found=$(ls -d ~/.claude*/projects/"$S" 2>/dev/null); k=$(printf '%s' "$found" | grep -c .)
       if [ "$k" != 1 ]; then printf '%s\t%s\tNOCFG-FOUND-%s\n' "$c" "$r" "$k"; continue; fi; cfgs=${found%/projects/*}; fi
  c1=$(grep -E '^(export )?C1_USD=' "$B" 2>/dev/null | tail -1 | cut -d= -f2); c2=$(grep -E '^(export )?C2_USD=' "$B" 2>/dev/null | tail -1 | cut -d= -f2)
  for cfg in $cfgs; do
    python3 "$M" "$cfg/projects/$S" --json 2>/dev/null | python3 -c '
import json,sys
c,r,cfg,c1,c2=sys.argv[1:6]
try: d=json.load(sys.stdin)
except Exception: print("\t".join([c,r,cfg,"METER-FAILED"])); sys.exit()
print("\t".join(map(str,[c,r,cfg,d["T"],d.get("COST"),";".join(sorted({v.split(" ")[0] for v in d["void"]})) or "-",c1 or "-",c2 or "-"])))
' "$c" "$r" "$cfg" "$c1" "$c2"
  done
done < ~/bench-dry/v3-claude-cells.tsv
