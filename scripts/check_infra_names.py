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

# Assembled, never spelled: the host and the account share this stem.
FORBIDDEN = ["kri" + "ter" + "ion"]


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
    # 2. Planted forms are caught: bare, capitalised, account-prefixed, inside an ssh alias.
    stem = FORBIDDEN[0]
    for form in (stem, stem.capitalize(), "jy" + stem, "ssh " + stem + "-lan 'x'", stem.upper()):
        if len(scan([("f.md", f"a line\n{form} here\n")])) != 1:
            failures.append(f"planted form {form!r} must be caught exactly once")
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
    print("check_infra_names SELF-TEST: OK (empty scan fatal proven FIRST, 5 planted forms caught, role words pass, self clean)")
    return 0


def _is_empty_scan_fatal(rows) -> bool:
    return len(rows) == 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args()
    if a.self_test:
        return self_test()
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
    print(f"check_infra_names: OK ({len(rows)} tracked text files, 0 occurrences)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
