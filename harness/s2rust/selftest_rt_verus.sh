#!/bin/bash
# selftest_rt_verus.sh — drives rt.template's ARGUMENT FENCE and its pass-through.
# ⛔ The fence is the reason an arm cannot buy a verdict the checker will not reproduce: `rt` bakes in the
# pinned --rlimit and seed, so the in-episode referee IS the check-time referee. A fence that is never driven
# is a comment. Each arm below names the rc it requires.
set -u
HERE=$(cd "$(dirname "$0")" && pwd)
VERUS=${1:?usage: selftest_rt_verus.sh <verus-binary>}
WORK=$(mktemp -d) || exit 2
trap 'rm -rf "$WORK"' EXIT
mkdir -p "$WORK/repo"
sed -e "s#__EP__#$WORK#g" -e "s#__VERUS__#$VERUS#g" -e "s#__RLIMIT__#250#g" \
    -e "s#__SEED__#0#g" -e "s#__RT_TIMEOUT__#120#g" "$HERE/rt.template" > "$WORK/rt"
chmod +x "$WORK/rt"
cat > "$WORK/repo/task.rs" <<'RS'
use vstd::prelude::*;
fn main() {}
verus!{
pub proof fn triv(n: nat)
    ensures n >= 0
{
}
}
RS
pass=0; fail=0
arm() { # arm <name> <expected-rc> <args...>
  local name="$1" want="$2"; shift 2
  "$WORK/rt" "$@" >/dev/null 2>&1; local rc=$?
  if [ "$rc" = "$want" ]; then echo "ok   $name (rc=$rc)"; pass=$((pass+1));
  else echo "FAIL $name: want rc=$want got rc=$rc"; fail=$((fail+1)); fi
}
echo "--- RED ARMS: the fence must refuse every argument list but one ---"
arm "no arguments"                       64
arm "wrong verb"                         64 lake env lean task.lean
arm "right verb, wrong file"             64 verus other.rs
arm "extra argument"                     64 verus task.rs --rlimit 999999
arm "an arm smuggling --no-cheating"     64 verus task.rs --no-cheating
arm "an arm smuggling --no-verify"       64 verus task.rs --no-verify
arm "shell string form (Lean rt's idiom)" 64 "verus task.rs"
echo "--- GREEN ARM: the one accepted command actually runs the referee ---"
arm "verus task.rs on a valid file"       0 verus task.rs
echo "--- the log records both outcomes ---"
if grep -q REFUSED "$WORK/repo/.rt.log" && grep -q 'END.*rc=0' "$WORK/repo/.rt.log"; then
  echo "ok   .rt.log carries REFUSED and END rc=0"; pass=$((pass+1))
else echo "FAIL .rt.log: $(cat "$WORK/repo/.rt.log" 2>/dev/null | tr '\n' '|')"; fail=$((fail+1)); fi
echo
echo "selftest_rt_verus: $((pass+fail)) arms, $fail failed"
exit $([ "$fail" -eq 0 ] && echo 0 || echo 1)
