#!/usr/bin/env python3
"""transcript_use_census.py --projects <config dir>/projects --dir-match <substring> --needle N [--needle N ...]

EXPOSURE IS NOT USE. For every project dir whose name contains --dir-match (one per cell), counts the transcript files
(heads and sidechains, recursively) that contain each needle literally, beside a CONTROL needle that every cell's
transcript should contain (REQUIREMENTS.md). Then a second method on the same files: every `<home>/cells*/<cell>` path
a transcript names, compared with the transcript's own most-named cell, and prints how many FOREIGN cells are named.
Prints counts only, never transcript content or the config dir's name.
LIMIT: a read whose path string appears in neither the call nor its result (e.g. inside a substitution) is not seen.
"""
import argparse, collections, glob, os, re


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--projects", required=True)
    ap.add_argument("--dir-match", required=True)
    ap.add_argument("--needle", action="append", required=True)
    ap.add_argument("--control", default="REQUIREMENTS.md")
    a = ap.parse_args()
    home = os.path.expanduser("~")
    dirs = sorted(d for d in glob.glob(os.path.join(a.projects, "*")) if a.dir_match in os.path.basename(d))
    files = [f for d in dirs for f in glob.glob(os.path.join(d, "**", "*.jsonl"), recursive=True)]
    hits = collections.Counter()
    rx = re.compile(re.escape(home) + r"/(cells(?:-[A-Za-z0-9._-]+)?)/([A-Za-z0-9._-]+)")
    named_own, foreign = 0, collections.Counter()
    for f in files:
        b = open(f, "rb").read()
        for n in a.needle + [a.control]:
            if n.encode() in b:
                hits[n] += 1
        seen = collections.Counter((m.group(1), m.group(2)) for m in rx.finditer(b.decode("utf-8", "replace")))
        if seen:
            named_own += 1
            own = seen.most_common(1)[0][0]
            for k in seen:
                if k != own and not k[1].startswith("_"):
                    foreign[k] += 1
    print("# project dirs matching %r: %d · transcript files (heads + sidechains): %d" % (a.dir_match, len(dirs), len(files)))
    print("needle\tfiles")
    for n in a.needle:
        print("%s\t%d" % (n, hits[n]))
    print("CONTROL %s\t%d" % (a.control, hits[a.control]))
    print("CONTROL files naming their own cell path\t%d" % named_own)
    print("FOREIGN cell paths named (distinct cells)\t%d" % len(foreign))


if __name__ == "__main__":
    main()
