#!/bin/bash
# YP step e raw (run on the run box): cell_meter --json over every CLAUDE-shape cell of record whose ctl/run-cfg.tsv names its cfg.
# A cell whose phases ran under two cfg dirs gets one row per cfg (spec-change cells). A cell without ctl/run-cfg.tsv is metered from the ONE config dir holding its slug; zero or several is printed NOCFG-FOUND-<k>.
M=${CELL_METER:?set CELL_METER to the cell_meter.py of the harness export (export 9d873183acab)}
printf 'cell\troot\tcfg\thead_models\tT_head\tT_exec\tT_wf\tT\tCOST_head\tCOST_exec\tCOST_wf\tCOST\tvoid\trates_source\n'
while IFS=$'\t' read c r; do
  R=~/$r/$c/ctl/run-cfg.tsv
  S=$(printf '%s' "$HOME/$r/$c/repo" | sed 's#[/.]#-#g')
  if [ -s "$R" ]; then cfgs=$(awk -F'\t' '$1=="cfg"{print $2}' "$R" | sort -u)
  else
    # no run-cfg.tsv (the 09-09/09-10 roots): the cfg is whichever config dir holds this cell's slug; exactly one, or refused by name
    found=$(ls -d ~/.claude*/projects/"$S" 2>/dev/null)
    k=$(printf '%s' "$found" | grep -c .)
    if [ "$k" != 1 ]; then printf '%s\t%s\tNOCFG-FOUND-%s\n' "$c" "$r" "$k"; continue; fi
    cfgs=${found%/projects/*}
  fi
  for cfg in $cfgs; do
  slug="$cfg/projects/$S"
  python3 "$M" "$slug" --json 2>/dev/null | python3 -c '
import json,sys
c,r,cfg=sys.argv[1:4]
try: d=json.load(sys.stdin)
except Exception as e: print("\t".join([c,r,cfg,"METER-FAILED"])); sys.exit()
j=lambda x: json.dumps(x,sort_keys=True,separators=(",",":"))
print("\t".join(map(str,[c,r,cfg,j(d.get("head_models")),d["T_head"],j(d["T_exec"]),d["T_wf"],d["T"],d.get("COST_head"),j(d.get("COST_exec")),d.get("COST_wf"),d.get("COST"),j(d["void"]),d.get("rates_source")])))
' "$c" "$r" "$cfg"
  done
done < ~/bench-dry/v3-claude-cells.tsv
