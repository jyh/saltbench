set -u
set -a; . ~/.fleet/saltbench/claude-lane.env; set +a
M="$CLB_EXPORT/harness/systems-v3/cell_meter.py"
echo "# cell_meter.py sha256/16 $(python3 -c 'import hashlib,sys;print(hashlib.sha256(open(sys.argv[1],"rb").read()).hexdigest()[:16])' "$M")  (from the release export tree)"
echo "# taken $(date -u +%Y-%m-%dT%H:%M:%SZ) on the run box, READ-ONLY: no cell, slug or config dir was written."
for C in ~/cells-hc1-lru-plain/hc1lp0*; do
  [ -d "$C" ] || continue
  id=$(basename "$C")
  R=$(python3 -c 'import os,sys;print(os.path.realpath(sys.argv[1]))' "$C/repo")
  LEAF=$(python3 -c 'import sys;print(sys.argv[1].replace(chr(47),chr(45)))' "$R")
  CFG=$(awk '$1=="cfg"{print $2}' "$C/ctl/run-cfg.tsv" | tail -1); CFG=${CFG/#\~/$HOME}
  echo ""
  echo "===== CELL $id  field=$(cat $C/ctl/field)  arm=$(cat $C/ctl/arm)  extras=$(cat $C/ctl/card_extras)"
  echo "----- terminal marker: $(head -1 $C/ctl/end-1)"
  echo "----- cfg rows recorded IN THE CELL (ctl/run-cfg.tsv, distinct): $(awk '$1=="cfg"{print $2}' $C/ctl/run-cfg.tsv | sort -u | tr '\n' ' ')"
  echo "----- ARM A: the slug as clb_harvest.py derives it from the lane env (CLB_CFG)"
  python3 "$M" "$CLB_CFG/projects/$LEAF" --launches 1 2>&1 | head -1
  echo "----- ARM B: the slug the CELL ITSELF records"
  python3 "$M" "$CFG/projects/$LEAF" --launches 1 2>&1
done
