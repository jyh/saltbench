#!/bin/bash
# score-topups.sh — the step g score receipt for the four stage-3 agy top-ups, with three controls
# re-scored IN THE SAME ACT. gemini, 2026-09-29. Zero model spend: no cell is fired or written to.
#
# Method (bench's ask, bus 2026-09-29 11:02): for each cell, fetch ctl/ + repo/{solution.rs,LANDING.md}
# READ-ONLY from the run box into a local COPY, drive the referee's own run_tests.sh over the copy, and
# read the meter columns exactly as stage 3's generator (s3-result-tsv.sh, 8c3adb406d2eff44) reads them,
# plus three columns stage 3 did not carry: the served model (agy_meter's census), the export sha the
# cell was built from (ctl/built-from.tsv) and the client binary sha (ctl/launch.log's LAUNCHING line).
# The referee's run_tests.sh is hashed BEFORE and AFTER the drive and must equal stage 3's header.
# ⛔ No defaults for the box or the referee root: which box a cell is read from, and which referee
#   scores it, are part of what the receipt claims.
set -u
HOST=${WAVE_HOST:?REFUSE - WAVE_HOST names the box the cells live on; no default}
TASKS=${REFEREE_TASKS:?REFUSE - REFEREE_TASKS names the referee tasks/systems-v3 root; no default}
OUT=${OUT:?REFUSE - OUT names the directory the receipt is written to}
set -a; . "$HOME/cells/toolchain.env"; set +a
# role · cell · task · arm · root (relative to the box's $HOME)
CELLS='CONTROL s3fp01 FreeList plain cells-s3-freelist-plain
CONTROL s3fq01 FreeList plain+stmt cells-s3-freelist-plain-stmt
CONTROL s3ct02 Crc32 salt-diet+stmt cells-s3-crc32-saltdiet-stmt
TARGET s3fpk01 FreeList plain cells-s3-freelist-plain-topup-s2k
TARGET s3fpk02 FreeList plain cells-s3-freelist-plain-topup-s2k
TARGET s3fqk01 FreeList plain+stmt cells-s3-freelist-plain-stmt-topup-s2k
TARGET s3ctk01 Crc32 salt-diet+stmt cells-s3-crc32-saltdiet-stmt-topup-s2k'
declare_sha() { case $1 in FreeList) echo cc555a74d71f2689;; Crc32) echo 3f1d7e4497d86c0e;; esac; }
W=$(mktemp -d "${TMPDIR:-/tmp}/stepg-score.XXXXXX")
mkdir -p "$OUT"
printf 'role\tcell\ttask\tarm\trc\tverdict\ttests\tN\ttrunc\tturns_sent\tresults\twall_s\tmax_turns\tmax_wall\tdone_reason\tlanded\tcred_fault\tfalse_done\tT\tcache_read\toutput_tok\tend_marker\tserved_model\trequested_model\texport_sha\tclient_sha\treferee_sha_before\treferee_sha_after\n' > "$OUT/score.tsv"
printf '%s\n' "$CELLS" | while read -r role id task arm root; do
  C="$W/$id"; mkdir -p "$C"
  if ! scp -q -r "$HOST:$root/$id/ctl" "$C/ctl" 2>"$C.scperr" || ! scp -q "$HOST:$root/$id/repo/solution.rs" "$C/solution.rs" 2>>"$C.scperr"; then
    printf '%s\t%s\t%s\t%s\t-\tFETCH-FAIL\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\n' "$role" "$id" "$task" "$arm" >> "$OUT/score.tsv"; continue
  fi
  scp -q "$HOST:$root/$id/repo/LANDING.md" "$C/LANDING.md" 2>/dev/null || true
  R="$TASKS/$task/G/run_tests.sh"
  s0=$(shasum -a 256 "$R" | cut -c1-16)
  sh "$R" "$C" > "$OUT/$id.run_tests.log" 2>&1; rc=$?
  s1=$(shasum -a 256 "$R" | cut -c1-16)
  line=$(grep -oE 'TESTS [0-9]+/[0-9]+' "$OUT/$id.run_tests.log" | tail -1 | awk '{print $2}')
  k=${line%%/*}; N=${line##*/}
  case $rc in 0) v=PASS;; 3) v=BUILD-FAIL;; *) v=FAIL;; esac
  [ "$s0" = "$(declare_sha "$task")" ] && [ "$s0" = "$s1" ] || v="REFEREE-MISMATCH($v)"
  trunc=$(grep -c 'print timeout' "$C/ctl/agy-stderr-1.txt" 2>/dev/null | tr -d ' \n'); trunc=${trunc:-0}
  cred=$(grep -c 'oauth2.googleapis.com/token": Forbidden' "$C/ctl/agy-stderr-1.txt" 2>/dev/null | tr -d ' \n'); cred=${cred:-0}
  mt=$(awk -F'\t' '$1=="max_turns"{print $2}' "$C/ctl/caps.tsv"); mw=$(awk -F'\t' '$1=="max_wall"{print $2}' "$C/ctl/caps.tsv")
  endm=$(head -1 "$C/ctl/end-1" 2>/dev/null | cut -c22- | awk '{print $1}')
  exp=$(awk -F'\t' '$1=="export_sha"{print $2}' "$C/ctl/built-from.tsv")
  cli=$(grep -oE 'LAUNCHING phase 1 model [^ ]+ client [0-9a-f]{16}' "$C/ctl/launch.log" | head -1 | awk '{print $NF}')
  python3 - "$C/ctl/agy-turnloop-1.json" "$C/ctl/agy-meter-1.json" "$role" "$id" "$task" "$arm" "$rc" "$v" "${k:--}" "${N:--}" "$trunc" "$mt" "$mw" "$cred" "${endm:-NO-END}" "${exp:--}" "${cli:--}" "$s0" "$s1" >> "$OUT/score.tsv" <<'PY'
import json,sys
a=sys.argv
t=json.load(open(a[1])); m=json.load(open(a[2])); pk=m.get("per_key",{})
print("\t".join(str(x) for x in [a[3],a[4],a[5],a[6],a[7],a[8],a[9],a[10],a[11],
  t.get("turns_sent"),t.get("results"),round(t.get("wall_seconds",0)),a[12],a[13],
  t.get("done_reason"),t.get("landed"),a[14],t.get("false_done_claims"),
  m.get("T"),pk.get("cache_read_tokens"),pk.get("output_tokens"),a[15],
  ",".join(m.get("served_models") or ["-"]),m.get("requested_model","-"),a[16],a[17],a[18],a[19]]))
PY
done
rm -rf -- "${W:?}"
