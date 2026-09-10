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


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args()
    if a.self_test:
        return self_test()
    if not _declared_ok(FORBIDDEN):
        print(f"FAIL: {len(FORBIDDEN)} forbidden name(s) against DECLARED_NAMES={DECLARED_NAMES} "
              f"(reconciled {DECLARED_RECONCILED}) -- a set that has shrunk is a gate that has been "
              f"quietly narrowed; refusing to scan.")
        return 1
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
