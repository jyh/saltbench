#!/usr/bin/env python3
"""check_recut.py — reproduce the (b′) re-cut of record (census ADDENDUM 52) and compare it with the files tracked here.

  python3 -I check_recut.py            run recut_sets.py twice into scratch dirs, with ../o37-agy-ctl-read-census-2026-11-25/recut/
                                       set-content.txt (NEW) and with '-' (the RULED state, WEB-SERVED out only); exit 0 only if every
                                       tracked <label>-moved.txt (record vs NEW) and <label>-moved-vs-ruled.txt (RULED vs NEW, by
                                       ../o37-agy-web-served-2026-11-20/recut/recut_diff.py) equals the fresh one byte for byte, and
                                       the fresh trailers equal run.log's #RECUT and #TAKEN-OUT lines
  python3 -I check_recut.py --mutant   the same, with one tracked file altered in a scratch copy first; must exit 1 (the check can fail)
It changes no instrument: recut_sets.py runs each instrument of record on its input (OLD, whose control must reproduce the RESULT of
record) and with the 10 WEB-SERVED cells plus the set taken out (NEW).
"""
import os, shutil, subprocess, sys, tempfile
HERE = os.path.dirname(os.path.abspath(__file__))
RC = os.path.join(HERE, "..", "o37-agy-ctl-read-census-2026-11-25", "recut")
LABELS = ["ZF", "blockNA", "descriptive-v2", "descriptive-v2-O57", "cost-v3", "correctness-v3"]
MATRIX = ["descriptive-v2", "descriptive-v2-O57", "cost-v3", "correctness-v3"]
DIFF = os.path.join(HERE, "..", "o37-agy-web-served-2026-11-20", "recut", "recut_diff.py")
mutant = "--mutant" in sys.argv[1:]
def keep(text):
    return [l for l in text.splitlines() if l.startswith(("#RECUT", "#TAKEN-OUT"))]
with tempfile.TemporaryDirectory() as tmp:
    fresh = os.path.join(tmp, "fresh")
    p = subprocess.run([sys.executable, "-I", os.path.join(RC, "recut_sets.py"), fresh, os.path.join(RC, "set-content.txt")],
                       capture_output=True, text=True)
    if p.returncode != 0:
        print(p.stdout[-2000:] + p.stderr[-2000:]); sys.exit(f"FAIL: recut_sets.py rc {p.returncode}")
    ruled = os.path.join(tmp, "ruled")
    q = subprocess.run([sys.executable, "-I", os.path.join(RC, "recut_sets.py"), ruled, "-"], capture_output=True, text=True)
    if q.returncode != 0:
        print(q.stdout[-2000:] + q.stderr[-2000:]); sys.exit(f"FAIL: recut_sets.py (ruled) rc {q.returncode}")
    for lab in MATRIX:
        d = subprocess.run([sys.executable, "-I", DIFF, os.path.join(ruled, f"{lab}-new.md"), os.path.join(fresh, f"{lab}-new.md"), lab],
                           capture_output=True)
        if d.returncode != 0: sys.exit(f"FAIL: recut_diff.py {lab} rc {d.returncode}")
        open(os.path.join(fresh, f"{lab}-moved-vs-ruled.txt"), "wb").write(d.stdout)
    tracked = HERE
    if mutant:
        tracked = os.path.join(tmp, "tracked"); shutil.copytree(HERE, tracked)
        with open(os.path.join(tracked, "correctness-v3-moved-vs-ruled.txt"), "a", encoding="utf-8") as f:
            f.write("  MUTANT | a line the instrument never printed |\n")
    bad = []
    names = [f"{lab}-moved.txt" for lab in LABELS] + [f"{lab}-moved-vs-ruled.txt" for lab in MATRIX]
    for name in names:
        a = open(os.path.join(tracked, name), "rb").read()
        b = open(os.path.join(fresh, name), "rb").read()
        print(f"{name}: {'SAME' if a == b else 'DIFFERS'}")
        if a != b: bad.append(name)
    t_old = keep(open(os.path.join(tracked, "run.log"), encoding="utf-8").read()); t_new = keep(p.stdout + p.stderr)
    print(f"trailers: {'SAME' if t_old == t_new and t_old else 'DIFFER'} ({len(t_old)} lines)")
    if t_old != t_new or not t_old: bad.append("trailers")
    if bad:
        sys.exit(f"FAIL: {', '.join(bad)}")
    print(f"OK: {len(names)} files and the trailers reproduce")
