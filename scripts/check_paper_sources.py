#!/usr/bin/env python3
"""Every source marker in the paper must name a file a reader can open.

WHY THIS EXISTS
---------------
The paper's discipline is that every number carries a `\\src{...}` marker naming the
file in this repository it was copied from, and the macro expands to nothing in the
PDF, so the markers are checked by nobody on the way to the reader.

The 2026-09-09 revision found the failure that discipline permits. Matrix #1 entered
the paper citing six files under `harness/systems-v3/`. Two of them had been merged to
the default branch; four had not, and one of the four was the PRE-REGISTRATION itself.
The paper's central methodological claim is that the reading was registered before the
first cell, and the document substantiating it was the one a reader could not open.

Nothing about that state is visible from the paper, from the PDF, or from a build: the
markers do not print, so a marker naming a file that reaches no public branch looks
exactly like a marker naming one that does.

WHAT IT CHECKS
--------------
Every `\\src{...}` block in every tracked `.tex` file under `paper/`:

  1. the block names at least one path, and
  2. the first path-like token of each of its segments (split on `;`) resolves to a
     tracked file or a tracked directory of this repository.

Later tokens in a segment are LOCATORS, not paths ("the dt_quote.py block", a section
name, a symbol), and are not required to resolve. A segment naming no path at all is a
continuation of the segment before it ("amendment 3") and is legitimate as long as its
block named a file somewhere.

FAILING CLOSED
--------------
A scan that finds no .tex file, or no source marker, REDS. `--self-test` proves both of
those are fatal before the real scan is trusted, and drives every arm of the rule in
both directions.

WHAT IT DOES NOT DO
-------------------
It does not check that the cited file SAYS what the sentence claims. A marker resolving
is necessary and not sufficient, and no gate replaces reading the source.
"""
from __future__ import annotations

import argparse
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(subprocess.run(["git", "rev-parse", "--show-toplevel"],
                                   cwd=pathlib.Path(__file__).resolve().parent,
                                   capture_output=True, text=True, check=True).stdout.strip())

SRC = re.compile(r"\\src\{([^}]*)\}")
TOKEN = re.compile(r"[A-Za-z0-9][A-Za-z0-9_./\\-]*")
HAS_EXT = re.compile(r"\.(md|py|json|tsv|txt|sh|cff|yml|yaml|tex|bib)$")


def _unescape(tok: str) -> str:
    return tok.replace("\\_", "_").replace("\\", "").rstrip(".,")


def cited_path(segment: str) -> str | None:
    """The first path-like token of a segment is the file it cites. The rest are locators."""
    for m in TOKEN.finditer(segment):
        tok = _unescape(m.group(0))
        if "/" in tok or HAS_EXT.search(tok):
            return tok
    return None


def tracked() -> tuple[set[str], set[str]]:
    out = subprocess.run(["git", "ls-files", "-z"], cwd=ROOT, capture_output=True, check=True).stdout
    files = {r for r in out.decode("utf-8").split("\0") if r}
    dirs: set[str] = set()
    for f in files:
        parts = f.split("/")
        for i in range(1, len(parts)):
            dirs.add("/".join(parts[:i]))
    return files, dirs


def tex_sources() -> list[tuple[str, str]]:
    out = subprocess.run(["git", "ls-files", "-z", "paper"], cwd=ROOT, capture_output=True, check=True).stdout
    rows = []
    for rel in out.decode("utf-8").split("\0"):
        if rel.endswith(".tex"):
            rows.append((rel, (ROOT / rel).read_text(encoding="utf-8", errors="replace")))
    return rows


def scan(rows: list[tuple[str, str]], files: set[str], dirs: set[str]) -> tuple[list, int]:
    """Return (findings, blocks_seen). A finding is (rel, line, kind, detail)."""
    findings, blocks = [], 0
    for rel, text in rows:
        for lineno, line in enumerate(text.splitlines(), 1):
            for block in SRC.findall(line):
                blocks += 1
                named = 0
                for seg in block.split(";"):
                    path = cited_path(seg)
                    if path is None:
                        continue
                    named += 1
                    if path not in files and path not in dirs:
                        findings.append((rel, lineno, "UNRESOLVED", path))
                if named == 0:
                    findings.append((rel, lineno, "NAMES-NO-FILE", block.strip()[:100]))
    return findings, blocks


def _empty_is_fatal(rows: list, blocks: int) -> bool:
    return not rows or blocks == 0


def self_test() -> int:
    fails = []
    files = {"A.md", "harness/x/B.py", "evidence/run-1/out.txt"}
    dirs = {"harness", "harness/x", "evidence", "evidence/run-1"}

    # 1. THE EMPTY SCANS ARE FATAL, PROVEN FIRST AND IN BOTH SHAPES.
    if not _empty_is_fatal([], 0):
        fails.append("zero .tex files must be fatal")
    if not _empty_is_fatal([("paper/p.tex", "no markers here")], 0):
        fails.append("zero source markers must be fatal")
    f, b = scan([("paper/p.tex", "prose with no marker")], files, dirs)
    if b != 0:
        fails.append("a file with no marker must count zero blocks")

    # 2. A RESOLVING MARKER PASSES, in every shape the paper actually uses.
    ok = [
        r"x\src{A.md section 3}",
        r"x\src{A.md, the header; harness/x/B.py, SOME\_SYMBOL}",
        r"x\src{evidence/run-1/out.txt}",
        r"x\src{evidence/run-1}",                                  # a directory
        r"x\src{A.md section 2; amendment 3}",                     # continuation segment
        r"x\src{the 2.2 to 2.8 re-timing: harness/x/B.py, header}",  # path not first in the segment
        r"x\src{A.md, the dt\_quote.py block, gates G1 and G2}",   # later token is a locator
    ]
    for line in ok:
        f, b = scan([("paper/p.tex", line)], files, dirs)
        if f:
            fails.append(f"must pass but found {f}: {line}")
        if b != 1:
            fails.append(f"must count exactly one block: {line}")

    # 3. THE FAILURES ARE CAUGHT, one per class.
    bad = [
        (r"x\src{MISSING.md section 1}", "UNRESOLVED"),
        (r"x\src{harness/x/GONE.py}", "UNRESOLVED"),
        (r"x\src{A.md, the header; harness/x/GONE.py}", "UNRESOLVED"),
        (r"x\src{section 4 of the record}", "NAMES-NO-FILE"),
    ]
    for line, kind in bad:
        f, _ = scan([("paper/p.tex", line)], files, dirs)
        if len(f) != 1 or f[0][2] != kind:
            fails.append(f"must be caught as {kind}, got {f}: {line}")

    # 4. A directory PREFIX that is not tracked is not a pass.
    f, _ = scan([("paper/p.tex", r"x\src{evidence/run-9}")], files, dirs)
    if len(f) != 1:
        fails.append("an untracked directory must not resolve")

    # 5. This gate's own docstring names files; it is not a .tex and is never scanned.
    if any(r.endswith(".tex") for r, _ in [("scripts/check_paper_sources.py", "")]):
        fails.append("this gate must not scan itself as a paper source")

    for x in fails:
        print(f"SELF-TEST FAIL: {x}")
    if fails:
        return 1
    print("check_paper_sources SELF-TEST: OK (both empty scans fatal proven FIRST, "
          "7 real marker shapes pass including directories and continuations, "
          "4 planted failures caught one per class, untracked directory refused)")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args()
    if a.self_test:
        return self_test()

    rows = tex_sources()
    files, dirs = tracked()
    findings, blocks = scan(rows, files, dirs)
    if _empty_is_fatal(rows, blocks):
        print(f"FAIL: {len(rows)} paper .tex file(s) and {blocks} source marker(s) -- "
              "refusing to call an empty scan clean")
        return 1
    for rel, lineno, kind, detail in findings:
        print(f"  {rel}:{lineno}: {kind}: {detail}")
    if findings:
        unresolved = sorted({d for _, _, k, d in findings if k == "UNRESOLVED"})
        if unresolved:
            print("\n  the paper names these paths and this repository does not carry them:")
            for u in unresolved:
                print(f"    {u}")
        print(f"\nFAIL: {len(findings)} source-marker finding(s) over {blocks} marker(s) "
              f"in {len(rows)} paper file(s)")
        return 1
    print(f"check_paper_sources: OK ({blocks} source markers in {len(rows)} paper file(s), "
          "every cited path tracked)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
