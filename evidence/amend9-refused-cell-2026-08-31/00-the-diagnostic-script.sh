#!/bin/bash
# amend9_diag.sh — the DIAGNOSTIC of amendment 9 §9.2/§9.3. ZERO model tokens: it re-runs the CHECKER over a
# frozen, sha-pinned agent artifact. Two arms: PRESENT (bodies byte-identical to what landed) and DELETED (the
# one `set_option linter.deprecated false` line removed). Nothing under ~/bench or ~/bench-a8/state is written.
set -u
D=/Users/jyh/bench-a8/diag-amend9
EP=/Users/jyh/bench-a8/state/ep-6b5540c0
V=/Users/jyh/bench-a8/s2views/problem_112
AB=/Users/jyh/bench-a8/state/s2/problem_112/a2/A.bodies.json
S2=/Users/jyh/bench/harness/s2lean
LEANPROJ=/Users/jyh/lean-shared/clever
rm -rf "$D"; mkdir -p "$D/present" "$D/deleted" "$D/pristine"

cp "$EP/bodies.json" "$D/present/bodies.json"
python3 - "$EP/bodies.json" "$D/deleted/bodies.json" <<'PY'
import json,sys,re
b=json.load(open(sys.argv[1]))
src=b["iso_helper_lemmas"]
lines=src.split("\n")
assert re.match(r'^set_option\s+linter\.deprecated\s+false\s*$', lines[0]), repr(lines[0])
b["iso_helper_lemmas"]="\n".join(lines[1:])
json.dump(b,open(sys.argv[2],"w"))
print("DELETED-ARM: removed line 1 %r; %d -> %d lines" % (lines[0], len(lines), len(lines)-1))
PY

echo "== screen verdicts (frozen screen.py, unchanged) =="
for a in present deleted; do
  printf '%-8s ' "$a"; python3 "$S2/screen.py" "$D/$a/bodies.json"
done

for a in present deleted; do
  echo "== ARM $a : full gate, --no-screen (screen recorded, not gating) =="
  s=$(date +%s)
  ( cd "$LEANPROJ" && PATH="$HOME/.elan/bin:$PATH" python3 "$S2/check.py" B "$V/frozen.json" \
      "$D/$a/bodies.json" "$LEANPROJ" "$D/$a/canonical.lean" \
      --timeout 900 --audit-timeout 900 --pristine-cache "$D/pristine" \
      --a-bodies "$AB" --no-screen ) > "$D/$a/check.json" 2> "$D/$a/check.err"
  echo "rc=$? wall=$(( $(date +%s) - s ))s"
  cat "$D/$a/check.json"; echo
  [ -s "$D/$a/check.err" ] && { echo "-- stderr --"; tail -20 "$D/$a/check.err"; }
done
echo "AMEND9-DIAG-DONE"
