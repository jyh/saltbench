#!/bin/bash
# supervisor_gate_drive.sh <harness-repo> <sha> <level-8-template-dir>
# Zero spend, no ssh. (1) Runs the supervisor gemini_canary_wave_v1.sh --selftest from `git archive <sha>`. (2) Extracts
# its manifest reader and gate VERBATIM (manifest_rows .. phases_verdict) and drives them over every l8u-*.tsv template
# at AGY_PHASES unset · 1 · 1,2. (3) CONTROL: the same templates with the extra column emptied, at 1,2. Only template
# basenames and sha256/16 are printed. It REFUSES on a directory holding no l8u-*.tsv.
set -u
R=${1:?repo}; X=${2:?sha}; T=${3:?template dir}
ls "$T"/l8u-*.tsv >/dev/null 2>&1 || { echo "REFUSE: no l8u-*.tsv in the template dir"; exit 2; }
W=$(mktemp -d "${TMPDIR:-/tmp}/l8sup.XXXXXX")
git -C "$R" archive "$X" harness/systems-v3 | tar -x -C "$W"
SUP=$W/harness/systems-v3/gemini_canary_wave_v1.sh
echo "supervisor at $(git -C "$R" rev-parse "$X")  sha256/16 $(shasum -a 256 "$SUP" | cut -c1-16)"
echo "== 1 · --selftest"
bash "$SUP" --selftest > "$W/selftest.out" 2>&1; rc=$?
printf '  rc=%s  %s  FAIL lines %s\n' "$rc" "$(tail -1 "$W/selftest.out")" "$(command grep -c -F '  FAIL ' "$W/selftest.out")"
a=$(command grep -n -F 'manifest_rows() {' "$SUP" | head -1 | cut -d: -f1)
b=$(command grep -n -F 'phases_verdict() { local rows rc' "$SUP" | cut -d: -f1)
sed -n "${a},${b}p" "$SUP" > "$W/lib.sh"
printf '  gate extracted: lines %s..%s\n' "$a" "$b"
. "$W/lib.sh"
v() { phases_verdict "$1" "$2" | sed -e 's/^REFUSE:\([0-9]*\) .*\[\([A-Za-z0-9.]*\)\]$/REFUSE:\1[\2]/'; }
echo "== 2 · the level-8 templates as drafted   (unset | 1 | 1,2)"
mkdir -p "$W/emptied"
for f in "$T"/l8u-*.tsv; do
  n=$(basename "$f")
  printf '  %-24s %s  rows=%s  %s | %s | %s\n' "$n" "$(shasum -a 256 "$f" | cut -c1-16)" "$(manifest_rows "$f" | wc -l | tr -d ' ')" "$(v "$f" '')" "$(v "$f" 1)" "$(v "$f" 1,2)"
  awk 'BEGIN{FS=OFS="\t"} /^[ \t]*(#|$)/ {print; next} {NF=5; print $0 "\t"}' "$f" > "$W/emptied/$n"
done
echo "== 3 · CONTROL: the same templates with the extra column emptied (every other byte unchanged), at 1,2"
for f in "$W"/emptied/l8u-*.tsv; do
  n=$(basename "$f")
  printf '  %-24s extras-left=%s  bytes-changed-only-in-extra=%s  %s\n' "$n" \
    "$(manifest_rows "$f" | awk -F'\t' '$6!=""' | wc -l | tr -d ' ')" \
    "$(diff <(cut -f1-5 "$T/$n") <(cut -f1-5 "$f") > /dev/null && echo yes || echo NO)" "$(v "$f" 1,2)"
done
[ -d "${W:?}" ] && rm -rf -- "${W:?}"
