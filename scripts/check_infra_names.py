#!/usr/bin/env python3
"""No infrastructure name (a host, an account) may sit in the public tree.

WHY THIS EXISTS
---------------
The private-paths gate (check_private_paths.py) fires on PATHS into the private
record. The 2026-09-02 refuter pass on the v1 flip package found 41 occurrences of
a class no gate covered: the name of the machine the episodes ran on and the name
of the subscription account that ran them, in frozen documents, evidence READMEs
and harness defaults. They were replaced by role words ("the Studio", "the bench
account", the ssh alias `studio`) and the class is GATED here, so that it is held
by an instrument rather than remembered.

WHAT IT CHECKS
--------------
Every tracked, text file, case-insensitively, for the forbidden names. The names
are ASSEMBLED in this file rather than spelled, for the same reason the trailer
gate assembles its fixture: this gate scans itself.

FAILING CLOSED
--------------
A scan over zero files REDS. `--self-test` proves the empty scan is fatal, that a
planted name is caught in every case and prefix form, and that the role words pass,
before the tree scan is trusted.

WHAT IT DOES NOT DO
-------------------
It does not scan commit MESSAGES. History carried one such message at the time this
gate was written; whether that history is rewritten before the flip is the owner's
decision (PUBLISH-CHECKLIST.md), and a gate that reds on a decision not yet taken is
a gate that gets abandoned.
"""
from __future__ import annotations

import argparse
import os
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(subprocess.run(["git", "rev-parse", "--show-toplevel"],
                                   cwd=pathlib.Path(__file__).resolve().parent,
                                   capture_output=True, text=True, check=True).stdout.strip())

# Assembled, never spelled — this gate scans itself.
#
# ⛔⛔ WIDENED 2026-09-10, on `systems`'s measurement of a FALSE GREEN. This list held exactly ONE
#   stem, because when the gate was written the host and the account SHARED it. The fleet now runs
#   FOUR accounts across FOUR boxes, and a BOX NAME (2 files) and an ACCOUNT NAME (2 files) were sitting
#   on PUBLIC main with Scrub GREEN. The gate was never wrong; it was OUTGROWN, and nothing announced
#   that.  ⇒ 🔑 AN ARM THAT NAMES ONE MEMBER OF A SET GOES VACUOUS WHEN THE SET GROWS.
FORBIDDEN = [
    "kri" + "ter" + "ion",      # a box, and an account: the original single stem
    "yu" + "kon",               # the box the seats run on
    "ke" + "nai",               # a box
    "jao" + "quin",             # a box
    "ja" + "son" + "h",         # an account
    "jy" + "aletheia",          # an account
    "claude-account-" + "ja" + "son",   # see the note below: the bare stem is NOT gateable
]

# ⛔ THE ONE THAT CANNOT BE A BARE SUBSTRING, AND THE REASON IS NOT A TECHNICALITY.
#   One account's name is the Captain's own GIVEN NAME, which appears legitimately in this public
#   repo as AUTHORSHIP -- `CITATION.cff` and `paper/saltbench-v1.tex` (\author{...}, and twice in the
#   bibliography). A bare substring rule would RED the paper's author line, and a gate that reds on
#   correct content is a gate that gets deleted. So that account is gated in its CONFIG-DIR SHAPE
#   only, which no byline can produce.
#   ⇒ 🔑 A NAME THAT IS ALSO A PERSON'S NAME IS GATEABLE ONLY IN THE SHAPES INFRASTRUCTURE USES.
#   ⇒ Anything this shape cannot catch is carried by the CONVENTION instead: a public tree names
#     accounts by anonymised label (ACCOUNT A / ACCOUNT B), with the mapping in the private record.

# ⛔ WHAT THIS TRIPWIRE DOES AND -- MORE IMPORTANTLY -- WHAT IT DOES NOT.
#   It refuses to scan when the forbidden set has SHRUNK below the count declared here. That catches
#   a name being DELETED. It does NOT catch the failure that actually happened, which was the FLEET
#   GROWING while this list stood still: both lines below are edited by the same hand, so they move
#   together and neither can notice a new account or a new box existing.
#   ⇒ 🔑 A DECLARATION AND THE THING IT DESCRIBES, EDITED TOGETHER, CANNOT CHECK EACH OTHER.
#   ⇒ **Completeness is not checkable from inside this repo at all.** The roster lives outside it and
#     MOVES, and CI cannot read it. Only a FLEET-SIDE check that reads the roster can know this set is
#     incomplete; that check is the load-bearing one and this is a second lock, not the lock.
#     (Named by `systems` on the bus, 2026-09-10, correcting this seat's first claim for it.)
#   The count is printed on every run so a reader can compare it against the fleet map rather than
#   trusting a date. Reconciled against the fleet roster on the date below -- its box column and its
#   account column. Adding a box or an account means editing BOTH lines, deliberately.
DECLARED_NAMES = 7
DECLARED_RECONCILED = "2026-09-10"

# THE RECONCILIATION ITSELF, WRITTEN OUT, so a reader can check COMPLETENESS without re-deriving it.
# The roster carries 5 ACCOUNTS and 4 BOXES -- 9 entities, covered by the 7 stems above because two
# stems each cover a box and an account that share a word. Entity -> the stem that catches it:
#
#     account  jy-aletheia      -> its own stem
#     account  ja-son           -> the CONFIG-DIR shape only (see the note above: it is also a byline)
#     account  jy-<the box word>-> the box stem, as a substring
#     account  ja-son-h         -> its own stem
#     account  <box4>-local     -> the box-4 stem, as a substring
#     box      yu-kon           -> its own stem       box  ke-nai   -> its own stem
#     box      <the box word>   -> its own stem       box  jao-quin -> its own stem
#
# ⛔ THIS TABLE IS A SNAPSHOT OF A FILE THAT LIVES ELSEWHERE AND MOVES, exactly like the roots list
#   in the private-paths gate. It is written down not because it stays true but because a reader who
#   suspects it has stopped being true can check it in one pass instead of rebuilding the derivation.


def tracked_files() -> list[tuple[str, str]]:
    out = subprocess.run(["git", "ls-files", "-z"], cwd=ROOT, capture_output=True, check=True).stdout
    rows = []
    for rel in out.decode("utf-8").split("\0"):
        if not rel:
            continue
        p = ROOT / rel
        if not p.is_file():
            continue
        data = p.read_bytes()
        if b"\0" in data:
            continue  # binary
        rows.append((rel, data.decode("utf-8", errors="replace")))
    return rows


def scan(rows: list[tuple[str, str]]) -> list[tuple[str, int, str]]:
    found = []
    for rel, text in rows:
        for i, line in enumerate(text.splitlines(), 1):
            low = line.lower()
            if any(n in low for n in FORBIDDEN):
                found.append((rel, i, line.strip()[:160]))
    return found


def self_test() -> int:
    failures = []
    # 1. The empty set is FATAL, first.
    if scan([]) != []:
        failures.append("scan([]) must find nothing")
    if not _is_empty_scan_fatal([]):
        failures.append("an empty file set must be FATAL, not green")
    # 2. EVERY name is planted, in every case and prefix form -- not just FORBIDDEN[0]. A per-name
    #    loop is the arm that a widened list cannot silently outgrow.
    for stem in FORBIDDEN:
        for form in (stem, stem.capitalize(), "x" + stem, "ssh " + stem + "-lan 'x'", stem.upper()):
            if len(scan([("f.md", f"a line\n{form} here\n")])) != 1:
                failures.append(f"planted form {form!r} must be caught exactly once")
    # 2b. THE TRIPWIRE ITSELF, driven: a set smaller than the declaration must be FATAL. Without this
    #     arm the declaration is a comment, and a comment cannot fail.
    if _declared_ok(FORBIDDEN[:-1]):
        failures.append("a set smaller than DECLARED_NAMES must be FATAL")
    if not _declared_ok(FORBIDDEN):
        failures.append("the live set must satisfy its own declaration")
    # 2c. The author's given name, standing alone as a byline, must PASS -- it is authorship, not
    #     infrastructure, and it is in this repo's own CITATION.cff and paper.
    if scan([("CITATION.cff", "  given-names: Ja" + "son\n\\author{Ja" + "son Hickey}\n")]):
        failures.append("an author byline must not be caught")
    # 3. The role words pass.
    clean = [("g.md", "on the Studio, on the bench account, STUDIO=\"${STUDIO:-studio}\", ssh studio 'x'\n")]
    if scan(clean):
        failures.append("role words must pass")
    # 4. The gate scans itself and is clean (it assembles, never spells).
    me = pathlib.Path(__file__).read_text(encoding="utf-8")
    if scan([("scripts/check_infra_names.py", me)]):
        failures.append("this file must not spell the name it forbids")
    for f in failures:
        print(f"SELF-TEST FAIL: {f}")
    if failures:
        return 1
    print(f"check_infra_names SELF-TEST: OK (empty scan fatal proven FIRST, "
          f"{len(FORBIDDEN) * 5} planted forms caught across {len(FORBIDDEN)} name(s), "
          f"the shrunk-set tripwire fires, an author byline passes, role words pass, self clean)")
    return 0


def _is_empty_scan_fatal(rows) -> bool:
    return len(rows) == 0


def _declared_ok(names) -> bool:
    """The forbidden set must not be SMALLER than what was reconciled against the roster."""
    return len(names) >= DECLARED_NAMES



# ---------------------------------------------------------------------------
# ⛔⛔ THE HISTORY AND RANGE ARMS, ADDED 2026-09-11.
# Measured that night, on the helm's ruling about the SIBLING gate: this file
# had `[-h] [--self-test]` and nothing else. No range arm, no history arm, no
# message arm. It scanned the tracked TREE and had never read a single commit —
# and it is the gate on HOST AND ACCOUNT NAMES, the class the fleet has an
# explicit law about and the one that actually leaked.
#   ⇒ Measured over saltbench's 360 commits the first time this ran:
#       current tree   0 occurrences        ✅
#       history      107 occurrences in 36 commits, NONE of them still in the tree
#   ⇒ 🔑 A GATE WITH ONE ARM IS CLEAN ABOUT THE ONLY POPULATION IT CAN SEE, and
#     the tree is the population that MOVES. Everything it ever caught and
#     everything anyone ever tidied away is still in a public clone.
#
# ⛔ THE RATCHET IS NOT A REPAIR AND MUST NOT READ AS ONE. A pushed commit's
# content cannot be changed without a force-push, ruled out 08/30 and in any
# case a Captain-level call on a public repo an arXiv paper now cites. This
# freezes the population and COUNTS it. It stops tomorrow's commit and says
# nothing whatever about yesterday's.
# ---------------------------------------------------------------------------
HIST_BASELINE = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             "infra_names_history_baseline.tsv")
EMPTY_TREE = "4b825dc642cb6eb9a060e54bf8d69288fbee4904"


def _git(args: list) -> str:
    return subprocess.run(["git"] + args, capture_output=True, text=True,
                          encoding="utf-8", errors="replace").stdout


def load_hist_baseline() -> set:
    """Accepted (sha, file) pairs. An absent file is an EMPTY set, never a pass."""
    out = set()
    if not os.path.exists(HIST_BASELINE):
        return out
    with open(HIST_BASELINE, encoding="utf-8") as fh:
        for line in fh:
            line = line.rstrip("\n")
            if not line.strip() or line.startswith("#"):
                continue
            parts = line.split("\t")
            if len(parts) >= 2:
                out.add((parts[0], parts[1]))
    return out


def added_rows(base: str, sha: str) -> list:
    """(path, added text) for what this commit ADDS. A deletion is never a finding."""
    out = _git(["diff", "--unified=0", "--no-color", base, sha])
    rows, path = [], "?"
    for line in out.splitlines():
        if line.startswith("+++ b/"):
            path = line[6:]
        elif line.startswith("+") and not line.startswith("+++"):
            rows.append((path, line[1:]))
    return rows


def _is_shallow() -> bool:
    return _git(["rev-parse", "--is-shallow-repository"]).strip() == "true"


def history_mode(write: bool) -> int:
    # ⛔⛔ A SHALLOW CLONE FAILS, AND THIS GUARD WAS MISSING FOR ONE CI RUN.
    #   Driven, and caught only by reading the COUNT in a PASSING line rather than the
    #   colour beside it: this arm's first CI run printed
    #       check_infra_names --history: OK (1 commits scanned; 40 accepted, 0 new)
    #   while the sibling in the same workflow printed 358. The job checks out at the
    #   default depth, and without this guard a one-commit history scans the truncation
    #   and reports success -- a green that means nothing, in a gate whose whole job is
    #   to report a negative.
    #   ⇒ 🔑 THE WORKFLOW WAS ALSO FIXED (fetch-depth: 0), AND THAT IS NOT THE REPAIR.
    #     A script that depends on its caller being configured correctly has moved the
    #     guard to the one place a reader of the script cannot see it.
    if _is_shallow():
        print("FAIL: this is a SHALLOW clone. A full-history ratchet on a truncated "
              "history scans the truncation, not the history.\n"
              "      CI must check out with `fetch-depth: 0` for this job.")
        return 1
    shas = _git(["rev-list", "HEAD"]).split()
    if not shas:
        print("FAIL: scanned ZERO commits from HEAD. An empty scan is not a clean scan.")
        return 1
    per = {}
    total = 0
    for sha in shas:
        parents = _git(["rev-list", "--parents", "-n", "1", sha]).split()
        # ⛔ first parent, so a merge is charged for what it BRINGS, not for the
        #   whole branch; and a root commit against the empty tree, because the
        #   first commit is exactly where a pre-gate name sits.
        base = parents[1] if len(parents) > 1 else EMPTY_TREE
        rows = added_rows(base, sha)
        if not rows:
            continue
        for rel, _i, _line in scan(rows):
            per.setdefault((sha[:12], rel), 0)
            per[(sha[:12], rel)] += 1
            total += 1
    if write:
        with open(HIST_BASELINE, "w", encoding="utf-8", newline="") as fh:
            fh.write("# infra_names_history_baseline.tsv -- ACCEPTED historical commits whose ADDED "
                     "LINES carry an infrastructure name (check_infra_names.py --history).\n"
                     "# sha<TAB>file<TAB>count. NEVER the line and NEVER the name: an excerpt would "
                     "put the name into the tree, where the tree arm correctly reds on it.\n"
                     "# This list does not shrink without a force-push, which is a Captain-level call "
                     "on a public repo. A GROWTH is a reviewed diff.\n")
            for k in sorted(per):
                fh.write(f"{k[0]}\t{k[1]}\t{per[k]}\n")
        print(f"check_infra_names --history --write-baseline: {len(per)} accepted (commit, file) "
              f"pair(s), {total} occurrence(s), written to {os.path.basename(HIST_BASELINE)}")
        return 0
    base_set = load_hist_baseline()
    new = [k for k in sorted(per) if k not in base_set]
    if new:
        print(f"FAIL: {len(new)} NEW infrastructure-name finding(s) in history, not in "
              f"{os.path.basename(HIST_BASELINE)} ({len(shas)} commits scanned):")
        for sha, rel in new[:20]:
            print(f"  {sha}  {rel}")
        return 1
    print(f"check_infra_names --history: OK ({len(shas)} commits scanned; "
          f"{len(base_set)} accepted historical (commit, file) pair(s), 0 new)")
    return 0


def range_mode(rev_range: str) -> int:
    """The arm CI runs on a push: what THIS delta adds, against nothing."""
    rows = added_rows(*rev_range.split("..", 1)) if ".." in rev_range else added_rows(EMPTY_TREE, rev_range)
    found = scan(rows)
    for rel, i, line in found:
        print(f"  {rel}:{i}: {line}")
    if found:
        print(f"FAIL: {len(found)} infrastructure-name occurrence(s) added by {rev_range}")
        return 1
    print(f"check_infra_names --range {rev_range}: OK ({len(rows)} added lines, 0 occurrences)")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--history", action="store_true",
                    help="ratchet: added lines of EVERY commit in history vs the committed baseline")
    ap.add_argument("--range", default=None,
                    help="scan the added lines of a git revision range (the push arm)")
    ap.add_argument("--write-baseline", action="store_true",
                    help="with --history: write the accepted-history baseline")
    a = ap.parse_args()
    if a.self_test:
        return self_test()
    if a.history and a.range:
        print("FAIL: --history and --range are separate arms; run them separately so a red names its arm.")
        return 1
    if not _declared_ok(FORBIDDEN):
        print(f"FAIL: {len(FORBIDDEN)} forbidden name(s) against DECLARED_NAMES={DECLARED_NAMES} "
              f"(reconciled {DECLARED_RECONCILED}) -- a set that has shrunk is a gate that has been "
              f"quietly narrowed; refusing to scan.")
        return 1
    if a.history:
        return history_mode(a.write_baseline)
    if a.range:
        return range_mode(a.range)
    rows = tracked_files()
    if _is_empty_scan_fatal(rows):
        print("FAIL: zero tracked text files -- refusing to call an empty scan clean")
        return 1
    found = scan(rows)
    for rel, i, line in found:
        print(f"  {rel}:{i}: {line}")
    if found:
        print(f"FAIL: {len(found)} infrastructure-name occurrence(s) in {len({r for r, _, _ in found})} file(s)")
        return 1
    print(f"check_infra_names: OK ({len(rows)} tracked text files, 0 occurrences; "
          f"{len(FORBIDDEN)} names WATCHED BY NAME, reconciled against the fleet roster {DECLARED_RECONCILED} -- \n"
          f"  the count is printed so a reader can compare it against the fleet map instead of trusting the date.)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
