#!/bin/bash
# export_delta.sh <harness-repo> <base-sha> <export-sha>
# Read-only. Prints (1) the ancestry checks §M0 row 4 and ADDENDA 2-3 require of the export, (2) the harness delta from
# the base, and (3) which changed files the agy lane's entry points NAME at the export, so "on the agy path" is derived
# from the tree and not asserted. It REFUSES if either sha does not resolve.
set -u
R=${1:?repo}; B=${2:?base}; X=${3:?export}
g() { git -C "$R" "$@"; }
g rev-parse -q --verify "$B^{commit}" >/dev/null || { echo "REFUSE: base $B does not resolve"; exit 2; }
g rev-parse -q --verify "$X^{commit}" >/dev/null || { echo "REFUSE: export $X does not resolve"; exit 2; }
echo "export $(g rev-parse "$X")  tree $(g rev-parse "$X^{tree}")"
echo "base   $(g rev-parse "$B")"
echo "== 1 · ancestry (rc 0 = the commit is in the export)"
for c in "$B:base, the phase-2 wiring (§M0 row 4)" "9e45404:§M3 the phase-1 fault gate" "5c2bb95:A2.1 AGY_PHASES binds" \
         "6edf70b:A3.3 one reader, wide needle" "205d7db:R1-R3 + ROOT" "2884f75:R4-R6 + FIELDS"; do
  s=${c%%:*}; g merge-base --is-ancestor "$s" "$X"; printf '  rc=%s  %s  %s\n' "$?" "$s" "${c#*:}"
done
echo "== 1b · CONTROL: a commit that is NOT in the export must read rc=1"
g merge-base --is-ancestor "$X" "$B"; printf '  rc=%s  export-in-base (must be 1)\n' "$?"
echo "== 2 · delta $B..$X"
printf '  commits %s · files %s\n' "$(g rev-list --count "$B..$X")" "$(g diff --name-only "$B" "$X" | wc -l | tr -d ' ')"
g diff --numstat "$B" "$X" | awk '{printf "  +%-5s -%-4s %s\n", $1, $2, $3}'
echo "== 3 · the delta GROUPED BY PATH PATTERN — a reading aid, NOT a call graph"
echo "   ⚠️ a first draft grouped by which entry points NAME each basename; it was withdrawn before commit because a generic"
echo "      basename (solution.rs) and a mention in a comment both count as a call. What runs on the agy path at this sha is"
echo "      shown by §M0 row 8's dry drive AT the export, not by this grouping."
P_CLB='^harness/systems-v3/(clb_[^/]*|cell-claude\.sh|score_claude_v3\.py|served_models_v3\.py|models-sonnet\.tsv)$'
P_CTL='^tasks/systems-v3/[^/]+/B/withheld/controls/'
P_AGY='^harness/systems-v3/(agy_[^/]*|fire_agy[^/]*|gemini_[^/]*|dry_phase2[^/]*)$'
printf '   patterns  claude-lane-prefixed %s\n             withheld control      %s\n             agy-prefixed          %s\n' "$P_CLB" "$P_CTL" "$P_AGY"
n1=0; n2=0; n3=0; n4=0
while IFS= read -r f; do
  if   printf '%s' "$f" | command grep -q -E "$P_CLB"; then k=CLAUDE-LANE-PREFIXED; n1=$((n1+1))
  elif printf '%s' "$f" | command grep -q -E "$P_CTL"; then k=WITHHELD-CONTROL; n2=$((n2+1))
  elif printf '%s' "$f" | command grep -q -E "$P_AGY"; then k=AGY-PREFIXED; n3=$((n3+1))
  else k=SHARED-OR-OTHER; n4=$((n4+1)); fi
  printf '  %-21s %s\n' "$k" "$f"
done < <(g diff --name-only "$B" "$X")
echo "  SUMMARY  CLAUDE-LANE-PREFIXED $n1 · WITHHELD-CONTROL $n2 · AGY-PREFIXED $n3 · SHARED-OR-OTHER $n4 · total $((n1+n2+n3+n4))"
echo "== 4 · CONTROL on the withheld-control group: no changed file lies under a withheld/mutants/ directory (the scoring population)"
printf '  files under withheld/mutants/: %s\n' "$(g diff --name-only "$B" "$X" | command grep -c -F '/withheld/mutants/')"
printf '  files under withheld/ at all (the control must find the fixture): %s\n' "$(g diff --name-only "$B" "$X" | command grep -c -F '/withheld/')"
