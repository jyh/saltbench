#!/usr/bin/env python3
"""gt_leak_check.py — THE GROUND-TRUTH FENCE (protocol §8.8), stated as an ARM rather than a design fact.

The commission's tombstone law: `bc_gate.py`'s successor is NOT a refusal fence, it is the DESIGN FACT that
no ground truth is shipped to the Studio at all — the split happens on the seat and the sync excludes the
jsonl. ⛔ A design fact that nothing checks is a hope. This is the check, and it REFUSES:

  · any file named `tasks.jsonl` / `tasks-no-lemma.jsonl`, or a `tasks/` directory of the benchmark's shape
  · any JSON object anywhere under the root carrying a `ground_truth` key (at any nesting depth)
  · any file under a `gt/` directory (the seat-side reference bodies)
  · the benchmark clone itself appearing under the root

It is deliberately CONTENT-BASED as well as name-based: a leak renamed is still a leak, and the fixture that
plants a `ground_truth` key under a harmless filename is the arm that proves the difference.

exit 0 = clean · exit 3 = LEAK (never 1, so a crash and a leak are not the same signal) · exit 2 = harness

usage: gt_leak_check.py <root> [--quiet]
       gt_leak_check.py --selftest
"""
import json, os, sys, tempfile, shutil

BAD_NAMES = {"tasks.jsonl", "tasks-no-lemma.jsonl", "tasks-sampled-100.jsonl"}
BAD_DIRS = {"gt", "verus-proof-synthesis"}
SKIP_DIRS = {".git", "__pycache__", "node_modules"}


def _has_gt_key(obj, depth=0):
    if depth > 12:
        return False
    if isinstance(obj, dict):
        if "ground_truth" in obj:
            return True
        return any(_has_gt_key(v, depth + 1) for v in obj.values())
    if isinstance(obj, list):
        return any(_has_gt_key(v, depth + 1) for v in obj)
    return False


def scan(root):
    leaks = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for d in list(dirnames):
            if d in BAD_DIRS:
                leaks.append("%s: a %r directory is on the Studio" % (os.path.join(dirpath, d), d))
        for fn in filenames:
            p = os.path.join(dirpath, fn)
            if fn in BAD_NAMES:
                leaks.append("%s: the benchmark's task file itself" % p)
                continue
            if not fn.endswith((".json", ".jsonl")):
                continue
            try:
                with open(p, encoding="utf-8", errors="replace") as fh:
                    head = fh.read(4_000_000)
            except OSError:
                continue
            if "ground_truth" not in head:
                continue                      # cheap reject before the parse
            hit = False
            try:
                hit = _has_gt_key(json.loads(head))
            except Exception:
                for line in head.splitlines():          # jsonl
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        if _has_gt_key(json.loads(line)):
                            hit = True
                            break
                    except Exception:
                        continue
            # a file naming the key but not parsing as data carrying it is still reported: the fence errs
            # toward refusing, because a false RED costs a look and a false GREEN costs the wave.
            leaks.append("%s: carries a `ground_truth` key%s" % (p, "" if hit else " (unparsed — refusing anyway)"))
    return leaks


def selftest():
    root = tempfile.mkdtemp(prefix="gtfence.")
    bad = 0

    def arm(name, setup, expect_leak):
        nonlocal bad
        d = tempfile.mkdtemp(dir=root)
        setup(d)
        got = bool(scan(d))
        ok = got == expect_leak
        bad += not ok
        print("%-4s %-52s expect_leak=%-5s got=%s" % ("ok" if ok else "FAIL", name, expect_leak, got))

    def w(d, rel, text):
        p = os.path.join(d, rel)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        open(p, "w").write(text)

    arm("a clean shipped root", lambda d: (
        w(d, "views/t1/frozen.json", json.dumps({"task_id": "t1", "prefix": "use vstd::prelude::*;"})),
        w(d, "views/t1/task.rs", "verus!{}")), False)
    # ⛔ THE FIXTURE THE PROTOCOL NAMES: a ground_truth key planted on the Studio must turn the fence RED
    arm("a planted ground_truth key", lambda d:
        w(d, "views/t1/frozen.json", json.dumps({"task_id": "t1", "ground_truth": "proof { }"})), True)
    arm("the key NESTED two levels down", lambda d:
        w(d, "state/run.json", json.dumps({"episodes": [{"rec": {"ground_truth": "x"}}]})), True)
    arm("a LEAK UNDER A HARMLESS FILENAME", lambda d:
        w(d, "state/harmless_notes.json", json.dumps({"ground_truth": "x"})), True)
    arm("the benchmark's task file by name", lambda d: w(d, "data/tasks.jsonl", '{"a":1}\n'), True)
    arm("a seat-side gt/ directory", lambda d: w(d, "gt/t1.json", '{"proof":"x"}'), True)
    arm("a .rs file MENTIONING ground_truth in a comment", lambda d:
        w(d, "views/t1/task.rs", "// ground_truth lives host-side\nverus!{}"), False)
    print("\ngt_leak_check selftest: 7 arms, %d failed" % bad)
    shutil.rmtree(root, ignore_errors=True)
    return 1 if bad else 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(selftest())
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if len(args) != 1:
        sys.exit(__doc__)
    found = scan(args[0])
    if found:
        print("⛔ GROUND-TRUTH FENCE: RED — %d finding(s)" % len(found))
        for f in found:
            print("   " + f)
        sys.exit(3)
    if "--quiet" not in sys.argv:
        print("ground-truth fence: clean (%s)" % args[0])
    sys.exit(0)
