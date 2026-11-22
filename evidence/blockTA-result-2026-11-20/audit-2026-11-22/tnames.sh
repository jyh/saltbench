# tnames.sh <section.rs> <cell>... — statement-derived needle (gemini's form): per cell, how many of the section's spec fn NAMES
# the tests DEFINE as `fn NAME` or `fn <prefix>_NAME`, across every tests/*.rs; plus the same over solution.rs.
# v2 (11-19, gemini's needle v2): a name beginning s_ also matches with s_ REPLACED: `fn REST` or `fn <prefix>_REST`.
S=$1; shift
names=$(grep -oE 'spec fn [a-z_0-9]+' "$S" | awk '{print $3}' | sort -u); tot=$(echo "$names" | grep -c .)
for C in "$@"; do
  t=0; s=0
  for n in $names; do
    pat="$n"; case "$n" in s_*) pat="(s_)?${n#s_}";; esac
    cat "$C"/repo/tests/*.rs 2>/dev/null | grep -qE "fn ([a-z0-9]+_)?$pat[^a-z0-9_]" && t=$((t+1))
    grep -qE "fn ([a-z0-9]+_)?$pat[^a-z0-9_]" "$C/repo/solution.rs" 2>/dev/null && s=$((s+1))
  done
  echo "$(basename $C) tests-define $t/$tot · solution-defines $s/$tot · test files $(ls "$C"/repo/tests/*.rs 2>/dev/null | wc -l | tr -d ' ')"
done
