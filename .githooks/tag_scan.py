#!/usr/bin/env python3
"""tag_scan.py -- what a push of a TAG adds, scanned with the gates' own patterns.

An annotated tag on a commit origin already has adds no commit, so every range arm
of .githooks/pre-push lists zero commits and refuses ("an empty scan is not a clean
scan"). What such a push adds is the TAG OBJECT: its raw text and its message.
This script scans exactly that, loading the patterns FROM THE GATE SCRIPTS the
caller names (nothing is typed here, so a hook cannot drift from its gate), and
refuses -- exit 2 -- when a gate cannot be loaded or the object is not a tag chain
ending at a commit.

Ported from jyh/saltworks .githooks/gate_scan.py (its tag mode); this repository
has no gate_scan.py, so only the tag half lives here.

USAGE (the hook is the caller; the repo root is the working directory)
    tag_scan.py tag --trailers-gate T --paths-gate P --subject-gate S [--infra-gate I] TAGSHA
exit 0 clean, 1 finding (named on stderr), 2 could not look (refuse).

This file is 100644 on purpose: the hook invokes it as "$PY" tag_scan.py after
choosing an interpreter by execution.
"""
import argparse
import re
import subprocess
import sys
import types


def load_gate(path: str, needs: tuple):
    """Exec a gate's source as a module. Its main() sits behind __main__, so
    nothing runs. Returns None when the file is unreadable or lacks a name the
    caller needs -- the caller refuses, it never falls back to a local copy."""
    try:
        with open(path, encoding="utf-8") as fh:
            src = fh.read()
    except OSError:
        return None
    mod = types.ModuleType("_gate_" + str(abs(hash(path))))
    mod.__file__ = path
    try:
        exec(compile(src, path, "exec"), mod.__dict__)
    except Exception as e:  # a gate that cannot load is a gate that cannot look
        print(f"gate_scan: {path} failed to load: {type(e).__name__}: {e}", file=sys.stderr)
        return None
    missing = [n for n in needs if not hasattr(mod, n)]
    if missing:
        print(f"gate_scan: {path} lacks {', '.join(missing)}", file=sys.stderr)
        return None
    return mod


def git(*args: str) -> str:
    return subprocess.run(["git", *args], capture_output=True, text=True,
                          encoding="utf-8", check=True).stdout


def show(rows, verb: str) -> None:
    for ident, what, line in rows:
        print(f"    {ident}  {verb} {what}", file=sys.stderr)
        # The trailer gate returns a LINE NUMBER in place of the text (desk PX);
        # the paths gate returns the line, and this output is local.
        if isinstance(line, int):
            print(f"        at line {line}", file=sys.stderr)
        elif line:
            print(f"        {line[:110]}", file=sys.stderr)


def _identity(header_line: str) -> str:
    """`tagger Name <e@x> 1700000000 -0700` -> `Name <e@x>` (the date is not identity)."""
    rest = header_line.split(None, 1)[1] if " " in header_line else ""
    return re.sub(r"\s+\d+\s+[+-]\d{4}\s*$", "", rest).strip()


def tag_mode(trailers, paths, subject, infra, tag_sha: str) -> int:
    """A TAG whose commit origin already has adds no commit to scan; what it adds
    is the TAG OBJECT, and that carries a message and a tagger line nobody has
    scanned. Walk the chain (a tag may point at a tag), scan each object's raw
    text with the trailer, private-paths and infra-names patterns and its message
    with the subject gate, and name every object scanned. Anything that is not an
    annotated tag, or a chain that does not end at a commit, is 'could not look'.

    THE TAGGER HEADER IS MEASURED BY WHAT IT ADDS. A tagger identity byte-equal to
    the author or committer of the tagged commit adds nothing: that commit is
    already public. It is the identity of every public commit in the repository,
    and the infra-name list matches it, so scanning it refused EVERY tag the owner
    makes (found at the first real push, 2026-10-15 18:13). Such a header is left
    out of the scan and the receipt says so; any OTHER header and the message are
    scanned as before, and a tagger that the commit does not carry is scanned."""
    seen, obj = [], tag_sha
    for _ in range(8):
        try:
            typ = git("cat-file", "-t", obj).strip()
        except subprocess.CalledProcessError as e:
            print(f"gate_scan: cannot read object {obj[:10]}: {e.stderr.strip()}", file=sys.stderr)
            return 2
        if typ == "commit":
            break
        if typ != "tag":
            print(f"gate_scan: {obj[:10]} is a {typ}, not an annotated tag chain ending at a commit -- refusing.",
                  file=sys.stderr)
            return 2
        raw = git("cat-file", "tag", obj)
        if not raw.strip():
            print(f"gate_scan: tag object {obj[:10]} read EMPTY -- refusing to call that clean.", file=sys.stderr)
            return 2
        seen.append((obj, raw))
        nxt = [l.split(None, 1)[1].strip() for l in raw.splitlines() if l.startswith("object ")]
        if len(nxt) != 1:
            print(f"gate_scan: tag object {obj[:10]} has no single 'object' header -- refusing.", file=sys.stderr)
            return 2
        obj = nxt[0]
    else:
        print("gate_scan: tag chain deeper than 8 -- refusing.", file=sys.stderr)
        return 2
    if not seen:
        print(f"gate_scan: {tag_sha[:10]} is a commit, not a tag object -- nothing for the tag arm to read.",
              file=sys.stderr)
        return 2
    try:
        commit_head = git("cat-file", "commit", obj).split("\n\n", 1)[0]
    except subprocess.CalledProcessError as e:
        print(f"gate_scan: cannot read the tagged commit {obj[:10]}: {e.stderr.strip()}", file=sys.stderr)
        return 2
    public_ids = {_identity(l) for l in commit_head.splitlines() if l.startswith(("author ", "committer "))}
    public_ids.discard("")
    skipped = 0

    bad = []
    for sha, raw in seen:
        short = "tag " + sha[:10]
        head, sep, body = raw.partition("\n\n")
        kept = []
        for l in head.splitlines():
            if l.startswith("tagger ") and _identity(l) in public_ids:
                skipped += 1
                continue
            kept.append(l)
        raw = "\n".join(kept) + sep + body
        bad += [(short, what, ln) for _, what, ln in trailers.scan([(short, raw)])]
        bad += [(short, what, ln) for _, what, ln in paths.scan([(short, raw)])]
        if infra is not None:
            bad += [(short, "an infrastructure name", f"line {ln}") for _, ln, _ in infra.scan([(short, raw)])]
        message = raw.split("\n\n", 1)[1] if "\n\n" in raw else ""
        for where, what in subject.subject_scan(subject.message_rows(message, short + " message")):
            bad.append((where, what, ""))
    if bad:
        print(f"REFUSED: {len(bad)} finding(s) in the tag object(s) this push adds:", file=sys.stderr)
        show(bad, "carries")
        return 1
    print(f"gate_scan OK: {len(seen)} tag object(s) -- raw text vs {len(trailers.FORBIDDEN)} trailer shape(s), "
          f"{len(paths.FORBIDDEN)} path shape(s), "
          + ("the infra-name list" if infra is not None else "NO infra-name gate in this repository")
          + "; message vs the subject gate"
          + (f"; {skipped} tagger header(s) equal to the tagged commit's author/committer NOT scanned (already public)"
             if skipped else "")
          + ".")
    return 0


def main(argv) -> int:
    ap = argparse.ArgumentParser(description="the hook's view of a tag push")
    sub = ap.add_subparsers(dest="mode", required=True)
    t = sub.add_parser("tag")
    t.add_argument("--trailers-gate", required=True)
    t.add_argument("--paths-gate", required=True)
    t.add_argument("--subject-gate", required=True)
    t.add_argument("--infra-gate", default=None)
    t.add_argument("tagsha")
    args = ap.parse_args(argv)

    trailers = load_gate(args.trailers_gate, ("FORBIDDEN", "scan"))
    paths = load_gate(args.paths_gate, ("FORBIDDEN", "scan"))
    subject = load_gate(args.subject_gate, ("subject_scan", "message_rows"))
    infra = load_gate(args.infra_gate, ("scan", "FORBIDDEN")) if args.infra_gate else None
    if trailers is None or paths is None or subject is None or (args.infra_gate and infra is None):
        print("tag_scan: a gate could not be loaded.", file=sys.stderr)
        return 2
    return tag_mode(trailers, paths, subject, infra, args.tagsha)


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv[1:]))
    except subprocess.CalledProcessError as e:
        print(f"tag_scan: git failed mid-scan: {e.cmd}: {(e.stderr or '').strip()}", file=sys.stderr)
        sys.exit(2)
