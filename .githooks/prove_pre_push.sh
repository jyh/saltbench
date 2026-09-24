#!/bin/sh
# prove_pre_push.sh -- RED PROVEN BEFORE GREEN IS BELIEVED, for .githooks/pre-push.
#
# A guard that has only ever been seen to pass is indistinguishable from a guard
# that cannot fail. This prover drives BOTH arms of .githooks/pre-push against a
# real `git push` into a real (scratch, bare) remote:
#
#   GREEN arms  -- a clean push must SUCCEED **and print its receipt**. A silent
#                  success is not evidence: a hook that never ran passes too.
#   RED arms    -- a private-record path in a commit MESSAGE, the same path in a
#                  FILE the commit ADDS, and a session trailer in a message must
#                  each be REFUSED, and the remote ref must NOT have moved.
#   DELETE arm  -- deleting a ref pushes no objects and must be ALLOWED.
#   MUTATION    -- the same refused push must SUCCEED with `--no-verify`. Without
#     CONTROL      this arm, every red above is equally consistent with "the push
#                  would have failed anyway", and the prover would prove nothing.
#
# ⛔ THE FIXTURES ARE NOT RETYPED. The forbidden shapes are read OUT OF THE GATE
#    SCRIPTS THEMSELVES (check_private_paths._EMPLOYER and
#    check_commit_trailers._SESSION_KEY), assembled at run time. Two reasons, and
#    the second is not style: a retyped fixture drifts silently when the gate's
#    list changes, AND this prover is a TRACKED FILE that the gate's own tree
#    ratchet scans -- spelling a private path here would make the prover trip the
#    gate it exists to drive.
#
# ⛔ THE SANDBOX IS REACHED BY ABSOLUTE PATH AND `git -C`, NEVER BY `cd`. A
#    fixture that reaches its sandbox by changing directory can, on any early
#    failure, run its git commands against THE REPOSITORY UNDER TEST.
#
# usage:  sh .githooks/prove_pre_push.sh
set -u

HERE=$(cd "$(dirname "$0")" && pwd)
REPO=$(cd "$HERE/.." && pwd)
# PROVE_HOOK: drive a DIFFERENT hook file through the same arms -- the red-first form:
#   PROVE_HOOK=<old hook> sh .githooks/prove_pre_push.sh  must FAIL on the arm a change adds.
HOOK=${PROVE_HOOK:-$HERE/pre-push}
PATHS_GATE="$REPO/scripts/check_private_paths.py"
TRAILER_GATE="$REPO/scripts/check_commit_trailers.py"
SUBJECT_GATE="$REPO/scripts/check_pr_descriptions.py"
SUBJECT_BASELINE="$REPO/scripts/subject_debt_baseline.tsv"
INFRA_GATE="$REPO/scripts/check_infra_names.py"

fail=0
note() { printf '%s\n' "$*"; }
bad()  { printf 'FAIL %s\n' "$*"; fail=$((fail + 1)); }

[ -f "$HOOK" ]         || { note "FAIL: no $HOOK"; exit 2; }
[ -x "$HOOK" ]         || { note "FAIL: $HOOK is not executable -- it would be INERT on this platform"; exit 2; }
[ -f "$PATHS_GATE" ]   || { note "FAIL: no $PATHS_GATE"; exit 2; }
[ -f "$TRAILER_GATE" ] || { note "FAIL: no $TRAILER_GATE"; exit 2; }

PY=
for c in python3 python py; do
  if "$c" -c "" >/dev/null 2>&1; then PY="$c"; break; fi
done
[ -n "$PY" ] || { note "FAIL: no working python interpreter"; exit 2; }

# ---- fixtures, read out of the gates ---------------------------------------
# Loading a gate as a module runs no main(): both guard it behind __main__.
read_const() {
  "$PY" - "$1" "$2" <<'PYEOF'
import sys, types
src_path, expr = sys.argv[1], sys.argv[2]
mod = types.ModuleType("_gate_under_proof")
mod.__file__ = src_path
with open(src_path, encoding="utf-8") as fh:
    exec(compile(fh.read(), src_path, "exec"), mod.__dict__)
print(eval(expr, mod.__dict__))
PYEOF
}

PRIVATE_PATH=$(read_const "$PATHS_GATE" '_EMPLOYER[0] + "/notes/x.md"') || PRIVATE_PATH=
TRAILER_KEY=$(read_const "$TRAILER_GATE" '_SESSION_KEY') || TRAILER_KEY=
[ -n "$PRIVATE_PATH" ] || { note "FAIL: could not read the private-path fixture out of the gate"; exit 2; }
[ -n "$TRAILER_KEY" ]  || { note "FAIL: could not read the trailer key out of the gate"; exit 2; }

# THE SUBJECT GATE'S WORDS (desk QA), read out of it: the longest lane word
# and the first family word. Each must be exactly one finding in a subject, or
# its arm is vacuous. Neither word is ever spelled in this file.
[ -f "$SUBJECT_GATE" ] || { note "FAIL: no $SUBJECT_GATE"; exit 2; }
[ -f "$SUBJECT_BASELINE" ] || { note "FAIL: no $SUBJECT_BASELINE"; exit 2; }
[ -f "$INFRA_GATE" ] || { note "FAIL: no $INFRA_GATE"; exit 2; }
# The infra fixture is READ OUT OF THE GATE (it assembles its names and never spells them; so does this
# prover), and its own scan must find exactly ONE occurrence on the planted line or the arm proves nothing.
INFRA_NAME=$(read_const "$INFRA_GATE" 'sorted(FORBIDDEN, key=len)[0]') || INFRA_NAME=
[ -n "$INFRA_NAME" ] || { note "FAIL: could not read an infrastructure name out of the infra gate"; exit 2; }
n=$(read_const "$INFRA_GATE" 'len(scan([("f", "the run box for tonight is " + sorted(FORBIDDEN, key=len)[0] + ", per the roster")]))') || n=
[ "$n" = "1" ] || { note "FAIL: the infra-gate fixture is not exactly one finding (got '${n}') -- its arm would prove nothing"; exit 2; }
LANE_WORD=$(read_const "$SUBJECT_GATE" 'sorted(lane_words(), key=len)[-1]') || LANE_WORD=
KIN_WORD=$(read_const "$SUBJECT_GATE" '_KIN[0]') || KIN_WORD=
[ -n "$LANE_WORD" ] || { note "FAIL: could not read a lane word out of the subject gate"; exit 2; }
[ -n "$KIN_WORD" ]  || { note "FAIL: could not read a family word out of the subject gate"; exit 2; }
for w in "$LANE_WORD" "$KIN_WORD"; do
  n=$(MSG="tidy the $w notes" read_const "$SUBJECT_GATE" 'len(subject_scan([("s", __import__("os").environ["MSG"], "subject")]))') || n=
  [ "$n" = "1" ] || { note "FAIL: a subject-gate fixture is not exactly one finding (got '${n}') -- its arm would prove nothing"; exit 2; }
done

# The fixture must actually be forbidden, or every RED arm below is vacuous.
if "$PY" "$PATHS_GATE" --self-test >/dev/null 2>&1; then :; else
  note "FAIL: the private-paths gate's own self-test does not pass; nothing here is readable"
  exit 2
fi

# ---- sandbox ----------------------------------------------------------------
SBX=$(mktemp -d) || { note "FAIL: mktemp -d"; exit 2; }
cleanup() {
  case "${SBX:-}" in
    /*/*) [ -d "$SBX" ] && rm -rf -- "$SBX" ;;
    *) note "refusing to remove '${SBX:-<empty>}'" ;;
  esac
}
trap cleanup EXIT

REMOTE="$SBX/remote.git"
W="$SBX/work"
git init -q --bare "$REMOTE"
mkdir -p "$W/.githooks" "$W/scripts"
git init -q "$W"
git -C "$W" symbolic-ref HEAD refs/heads/main
git -C "$W" config user.email prover@example.invalid
git -C "$W" config user.name  "pre-push prover"
git -C "$W" config commit.gpgsign false
git -C "$W" config core.autocrlf false
git -C "$W" config advice.pushUpdateRejected false
git -C "$W" remote add origin "$REMOTE"

# ONLY pre-push is installed. Installing commit-msg too would make the RED arms
# unbuildable: that hook refuses the very trailer this prover must commit.
cp "$HOOK" "$W/.githooks/pre-push"
chmod +x "$W/.githooks/pre-push"
cp "$PATHS_GATE" "$W/scripts/check_private_paths.py"
cp "$TRAILER_GATE" "$W/scripts/check_commit_trailers.py"
cp "$SUBJECT_GATE" "$W/scripts/check_pr_descriptions.py"
cp "$SUBJECT_BASELINE" "$W/scripts/subject_debt_baseline.tsv"
cp "$INFRA_GATE" "$W/scripts/check_infra_names.py"
git -C "$W" config core.hooksPath .githooks

commit_file() { # <path> <content> <message>
  printf '%s\n' "$2" > "$W/$1"
  git -C "$W" add -- "$1"
  git -C "$W" commit -q --no-verify -F - <<EOF
$3
EOF
}

OUT="$SBX/out.txt"
run_push() { # <expected-exit> <label> <push args...>
  want=$1; label=$2; shift 2
  git -C "$W" push "$@" > "$OUT" 2>&1
  rc=$?
  if [ "$rc" -eq "$want" ]; then
    printf '  ok   %-22s exit=%s (expected %s)\n' "$label" "$rc" "$want"
    return 0
  fi
  printf '  FAIL %-22s exit=%s expected=%s\n' "$label" "$rc" "$want"
  sed 's/^/         | /' "$OUT"
  fail=$((fail + 1))
  return 1
}

expect_out() { # <label> <fixed string>
  if grep -qF -- "$2" "$OUT"; then
    printf '       +   %s: output carries "%s"\n' "$1" "$2"
  else
    bad "$1: output does NOT carry \"$2\""
    sed 's/^/         | /' "$OUT"
  fi
}

remote_tip() { git -C "$REMOTE" rev-parse --verify --quiet "refs/heads/$1" 2>/dev/null; }

note "prove_pre_push: every arm states its expected exit BEFORE it runs"
note "  sandbox: $SBX (never the repository under test)"
note ""

# ── ARM 1 ── first push of a new ref whose delta reaches the ROOT commit.
note "ARM 1  clean first push (new ref, root commit in the delta)   expect 0"
commit_file seed.txt "a role-worded line: the helm minuted it in its own brief" "seed: the clean base"
run_push 0 green-first-push origin main
expect_out green-first-push "pre-push OK"
expect_out green-first-push "MESSAGE ARM ONLY"
GOOD=$(git -C "$W" rev-parse HEAD)

# ── ARM 2 ── ordinary push onto an existing ref: a TWO-DOT range, so the gate's
# FILE arm runs. This is the positive control for ARM 5, which needs it.
note "ARM 2  clean push onto an existing ref (two-dot range)        expect 0"
commit_file clean2.txt "docs/QUEUE.md is a public path and stays" "clean: an added line the ruling permits"
run_push 0 green-two-dot origin main
expect_out green-two-dot "pre-push OK"
expect_out green-two-dot "delta against the remote tip"
expect_out green-two-dot "added lines scanned"
GOOD=$(git -C "$W" rev-parse HEAD)

# ── ARM 3 ── a NEW branch off an existing one: the merge-base arm.
note "ARM 3  clean push of a brand-new branch (merge-base arm)      expect 0"
git -C "$W" checkout -q -b feature
commit_file feat.txt "another seat's bank carries the superseded value" "feature: role-wording only"
run_push 0 green-new-branch origin feature
expect_out green-new-branch "merge-base with origin/"
git -C "$W" checkout -q main

# ── ARM 4 ── a private-record path in a COMMIT MESSAGE.
note "ARM 4  private path in a commit MESSAGE                       expect 1"
BEFORE_TIP=$(remote_tip main)
commit_file ok4.txt "nothing wrong with this line" "see $PRIVATE_PATH for the note"
BADSHA=$(git -C "$W" rev-parse HEAD)
run_push 1 red-message-path origin main
expect_out red-message-path "private-record path"
expect_out red-message-path "PUSH REFUSED by .githooks/pre-push"
if [ "$(remote_tip main)" = "$BEFORE_TIP" ]; then
  printf '       +   red-message-path: the remote ref did NOT move\n'
else
  bad "red-message-path: THE REMOTE REF MOVED -- the refusal did not stop the objects"
fi
git -C "$W" reset -q --hard "$GOOD"

# ── ARM 5 ── the same path in a FILE the commit ADDS (the arm a message-only
#             check is structurally blind to).
note "ARM 5  private path in an ADDED FILE LINE                     expect 1"
commit_file leak5.txt "the record is at $PRIVATE_PATH" "docs: a clean message over a dirty line"
run_push 1 red-file-path origin main
expect_out red-file-path "private-record path"
if [ "$(remote_tip main)" = "$BEFORE_TIP" ]; then
  printf '       +   red-file-path: the remote ref did NOT move\n'
else
  bad "red-file-path: THE REMOTE REF MOVED"
fi
git -C "$W" reset -q --hard "$GOOD"

# ── ARM 6 ── a session trailer in a commit message. Built from the gate's own
#             key so it cannot drift, and committed --no-verify because the
#             commit-msg hook is deliberately not installed in the sandbox.
note "ARM 6  session trailer in a commit message                    expect 1"
printf 'x\n' > "$W/t6.txt"
git -C "$W" add -- t6.txt
git -C "$W" commit -q --no-verify -F - <<EOF
docs: a commit whose message carries the forbidden trailer

Co-Authored-By: somebody <nobody@example.invalid>
${TRAILER_KEY}: 0123456789abcdef
EOF
TRAILER_SHA=$(git -C "$W" rev-parse --short HEAD)
run_push 1 red-session-trailer origin main
expect_out red-session-trailer "session trailer/URL in its message"
expect_out red-session-trailer "$TRAILER_SHA"
if [ "$(remote_tip main)" = "$BEFORE_TIP" ]; then
  printf '       +   red-session-trailer: the remote ref did NOT move\n'
else
  bad "red-session-trailer: THE REMOTE REF MOVED"
fi
git -C "$W" reset -q --hard "$GOOD"

# ── ARM 7 ── deleting a ref sends no objects and must be allowed.
note "ARM 7  deleting a remote ref (local sha all zeros)            expect 0"
run_push 0 delete-allowed origin --delete feature
expect_out delete-allowed "is being DELETED"

# ── ARM 8 ── THE MUTATION CONTROL. Every RED above is only evidence if the same
#             push SUCCEEDS once the hook is out of the way.
note "ARM 8  mutation control: the refused push, with --no-verify   expect 0"
git -C "$W" checkout -q -b mutation-control "$BADSHA"
run_push 0 mutation-control origin --no-verify mutation-control
if [ -n "$(remote_tip mutation-control)" ]; then
  printf '       +   mutation-control: the SAME commit lands once the hook is bypassed\n'
  printf '           => every refusal above was the hook'"'"'s, not an accident of the fixture\n'
else
  bad "mutation-control: the bypassed push did not land -- the RED arms prove nothing"
fi
git -C "$W" checkout -q main

# ── ARMS 9-11 ── the subject gate (desk QA). Each commit touches only a clean
#                file; each CONTROL shows the paths and trailer gates passing the
#                same range, so a refusal is the new arm's. The word must never
#                appear in the output, and no check below prints it.
older_arms_pass() { # <range>
  ( cd "$W" && "$PY" scripts/check_private_paths.py --range "$1" ) >/dev/null 2>&1 \
  && ( cd "$W" && "$PY" scripts/check_commit_trailers.py --range "$1" ) >/dev/null 2>&1
}
subject_arm() { # <arm-no> <label> <message> <class-line>
  note "ARM $1 $2   expect 1"
  BEFORE_TIP=$(remote_tip main)
  commit_file "s$1.txt" "nothing wrong with this line" "$3"
  SUBJ_SHA=$(git -C "$W" rev-parse HEAD | cut -c1-12)
  if older_arms_pass "$GOOD..HEAD"; then
    printf '       +   subject-arm-%s: CONTROL -- the paths and trailer gates pass this range\n' "$1"
  else
    bad "subject-arm-$1: an older gate already refuses this range, so the arm tests nothing new"
  fi
  run_push 1 "red-subject-arm-$1" origin main
  expect_out "red-subject-arm-$1" "the subject gate RED"
  expect_out "red-subject-arm-$1" "commit $SUBJ_SHA"
  expect_out "red-subject-arm-$1" "$4"
  if grep -qF -- "Traceback" "$OUT"; then bad "red-subject-arm-$1: a Traceback"; fi
  if grep -qF -- "$LANE_WORD" "$OUT"; then
    bad "red-subject-arm-$1: the output ECHOES the lane word (output withheld)"
  else
    printf '       +   red-subject-arm-%s: output does not echo the lane word\n' "$1"
  fi
  if [ "$(remote_tip main)" = "$BEFORE_TIP" ]; then
    printf '       +   red-subject-arm-%s: the remote ref did NOT move\n' "$1"
  else
    bad "red-subject-arm-$1: THE REMOTE REF MOVED"
    git -C "$REMOTE" update-ref refs/heads/main "$BEFORE_TIP"
  fi
  git -C "$W" reset -q --hard "$GOOD"
}
subject_arm 9 "a lane name in a SUBJECT only      " "tidy the $LANE_WORD notes

a clean body" "SUBJECT: an employer-lane or private project name"
subject_arm 10 "a family reference in a SUBJECT only" "ratified: the $KIN_WORD agreed

a clean body" "SUBJECT: a family reference"
subject_arm 11 "a lane name in a BODY only         " "docs: a clean subject

see the $LANE_WORD notes" "BODY: an employer-lane or private project name"

# ── ARM 12 ── a family word in the pushed BRANCH NAME, with clean commits (the
#              family word, never a lane word: the push output prints the name).
note "ARM 12 a family reference in the pushed BRANCH NAME          expect 1"
git -C "$W" checkout -q -b "tidy-$KIN_WORD"
commit_file s12.txt "nothing wrong with this line" "docs: a clean subject"
run_push 1 red-ref-name origin "tidy-$KIN_WORD"
expect_out red-ref-name "the pushed ref name carries a refused word"
expect_out red-ref-name "the ref name: a family reference"
if [ -z "$(remote_tip "tidy-$KIN_WORD")" ]; then
  printf '       +   red-ref-name: the branch did NOT reach the remote\n'
else
  bad "red-ref-name: THE BRANCH REACHED THE REMOTE"
fi
git -C "$W" checkout -q main
git -C "$W" branch -q -D "tidy-$KIN_WORD"

# ── ARM 13 ── FAIL CLOSED: with the subject gate absent, a clean push is
#              refused rather than waved through on two of three arms.
note "ARM 13 the subject gate is missing: a clean push is refused   expect 1"
mv "$W/scripts/check_pr_descriptions.py" "$SBX/check_pr_descriptions.py.hidden"
commit_file clean13.txt "nothing wrong with this line" "clean: nothing forbidden here"
run_push 1 fail-closed-no-subject-gate origin main
expect_out fail-closed-no-subject-gate "check_pr_descriptions.py is not in this working tree"
mv "$SBX/check_pr_descriptions.py.hidden" "$W/scripts/check_pr_descriptions.py"
git -C "$W" reset -q --hard "$GOOD"

note "ARM 14 an infrastructure name in an ADDED FILE LINE          expect 1"
BEFORE_TIP=$(remote_tip main)
commit_file infra14.txt "the run box for tonight is $INFRA_NAME, per the roster" "docs: a clean message over a line naming a host"
if older_arms_pass "$GOOD..HEAD" \
   && ( cd "$W" && "$PY" scripts/check_pr_descriptions.py --range "$GOOD..HEAD" ) >/dev/null 2>&1; then
  printf '       +   red-infra-name: CONTROL -- the paths, trailer and subject gates all pass this range\n'
else
  bad "red-infra-name: an older gate already refuses this range, so the arm tests nothing new"
fi
run_push 1 red-infra-name origin main
expect_out red-infra-name "the infra-names gate RED"
expect_out red-infra-name "an infrastructure name (account or host)"
if grep -qF -- "$INFRA_NAME" "$OUT"; then
  bad "red-infra-name: the output ECHOES the infrastructure name (the gate withholds matched text; the hook must too)"
else
  printf '       +   red-infra-name: output does not echo the infrastructure name\n'
fi
if [ "$(remote_tip main)" = "$BEFORE_TIP" ]; then
  printf '       +   red-infra-name: the remote ref did NOT move\n'
else
  bad "red-infra-name: THE REMOTE REF MOVED"
  git -C "$REMOTE" update-ref refs/heads/main "$BEFORE_TIP"
fi
git -C "$W" reset -q --hard "$GOOD"

note "ARM 15 the infra gate is missing: a clean push is refused     expect 1"
mv "$W/scripts/check_infra_names.py" "$SBX/check_infra_names.py.hidden"
commit_file clean15.txt "nothing wrong with this line" "clean: nothing forbidden here"
run_push 1 fail-closed-no-infra-gate origin main
expect_out fail-closed-no-infra-gate "check_infra_names.py is not in this working tree"
mv "$SBX/check_infra_names.py.hidden" "$W/scripts/check_infra_names.py"
git -C "$W" reset -q --hard "$GOOD"

note ""
if [ "$fail" -eq 0 ]; then
  note "prove_pre_push: PASS -- 3 clean pushes each SUCCEED and print a receipt"
  note "  naming the range; 3 distinct leak shapes (message path, added-line path,"
  note "  session trailer) and the subject gate's 3 (a lane name or family"
  note "  reference in a subject, a lane name in a body) are each REFUSED with the"
  note "  remote ref unmoved, and so is a branch whose name carries a refused word;"
  note "  an infrastructure name in an added line is REFUSED without being echoed;"
  note "  a missing subject gate or infra gate refuses a clean push; a delete is"
  note "  allowed; and the mutation control lands the same commit with the hook"
  note "  bypassed, so the refusals are attributable to the hook."
  exit 0
fi
note "prove_pre_push: FAILED ($fail arm(s))"
exit 1
