#!/bin/bash
# t-box.sh <cell-path> <opus|sonnet> — block T's per-cell facts, READ ON THE RUN BOX, read-only. One key<TAB>value per line.
#   Called by t-derive.sh over ssh (copied to the run box's ~/bench-dry/ first). Writes nothing.
#   born-during = $HOME entries whose BIRTH time (stat %B, never find -newermt: it read a false NONE, block T ADDENDUM 3 correction)
#   lies between launch.log's birth and end-1's mtime, each searched for in every transcript of the cell (control: the cell's own id).
set -u
PC=${1:?cell path}; COND=${2:?opus or sonnet}; ID=$(basename "$PC")
kv(){ printf '%s\t%s\n' "$1" "$2"; }
kv id "$ID"
kv end1 "$(head -1 "$PC/ctl/end-1" 2>/dev/null || echo NO-END-1)"
kv post "$(tail -1 "$PC/ctl/post-end-1.tsv" 2>/dev/null | tr '\t' '|')"
kv export "$(awk -F'\t' '$1=="export_sha"{print $2}' "$PC/ctl/built-from.tsv")"
kv arm_ctl "$(awk -F'\t' '$1=="arm"{print $2}' "$PC/ctl/built-from.tsv")"
kv problem_ctl "$(awk -F'\t' '$1=="problem"{print $2}' "$PC/ctl/built-from.tsv")"
cfg=$(awk -F'\t' '$1=="cfg"{v=$2} END{print v}' "$PC/ctl/run-cfg.tsv"); kv cfg "$cfg"
kv extras "$(cat "$PC/ctl/card_extras" 2>/dev/null | head -1)"
t0=$(stat -f %B "$PC/ctl/launch.log"); t1=$(stat -f %m "$PC/ctl/end-1" 2>/dev/null || echo 0)
kv launch_birth "$(date -r "$t0" -u +%Y-%m-%dT%H:%M:%SZ)"
slug=$(echo "$PC/repo" | sed 's|/|-|g')
HV=$(awk -F'\t' '$1=="harness"{print $2}' "$PC/ctl/built-from.tsv")   # the export harness the cell was BUILT from (its own row)
sv=$(python3 "$HV/served_models_v3.py" check-cell --condition "$COND" --slug "$cfg/projects/$slug" --cell "$PC" 2>&1)
kv served_verdict "$(printf '%s\n' "$sv" | sed -n 's/.*set_verdict \([a-z]*\).*/\1/p' | head -1)"
kv served_head "$(printf '%s\n' "$sv" | sed -n 's/^ *served head *//p' | head -1)"
kv sol_dirty "$(git -C "$PC/repo" status --porcelain -- solution.rs | wc -l | tr -d ' ')"
kv head "$(git -C "$PC/repo" rev-parse --short=12 HEAD)"
kv sol_mtime "$(date -r "$(stat -f %m "$PC/repo/solution.rs")" -u +%Y-%m-%dT%H:%M:%SZ)"
D=$(ls -d "$HOME"/.claude-account-*/projects/"$slug" 2>/dev/null | head -1)
J=$(find "$D" -name '*.jsonl' 2>/dev/null)
kv transcripts "$(printf '%s\n' "$J" | grep -c .)"
ch=0; [ -n "$J" ] && ch=$(cat $J | grep -c "$ID"); kv control_own_id_hits "$ch"   # grep -c prints 0 AND exits 1: never `|| echo 0`
nb=0; hb=0; names=""
if [ "$t1" != 0 ]; then
  for e in "$HOME"/* "$HOME"/.[!.]*; do
    [ -e "$e" ] || continue; b=$(stat -f %B "$e")
    if [ "$b" -ge "$t0" ] && [ "$b" -le "$t1" ]; then
      n=$(basename "$e"); h=0; [ -n "$J" ] && h=$(cat $J | grep -cF "$n")
      nb=$((nb+1)); hb=$((hb+h)); names="$names$n:$h,"
    fi
  done
fi
kv born_n "$nb"; kv born_hits "$hb"; kv born_names "${names%,}"
# the subject's own Verus runs, by record TIMESTAMP (vtime.py's rule; vcheck.sh took find order as time and is superseded)
python3 - "$D" <<'PY'
import json, sys, glob, os, re
D = sys.argv[1]; out = []
for f in glob.glob(D + '/**/*.jsonl', recursive=True):
    for line in open(f, errors='replace'):
        try: r = json.loads(line)
        except Exception: continue
        ts = r.get('timestamp', '')
        for m in re.finditer(r'verification results:: (\d+) verified, (\d+) errors', line):
            out.append((ts, m.group(1), m.group(2)))
out = sorted(set(out))
print('verus_runs\t%d' % len(out))
print('verus_last\t%s' % ('|'.join(out[-1]) if out else '-'))
print('verus_last_clean\t%s' % (next(('|'.join(o) for o in reversed(out) if o[2] == '0'), '-')))
PY
