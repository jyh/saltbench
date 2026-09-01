#!/usr/bin/env python3
"""screen_widening_proof.py — the RED-FIRST gate for amendment 9 §9.5 (the `linter.` clause of the screen).

This repo's standing law: *a self-test that never makes the call its caller makes is a self-test of a different
program.* So this proof does three things, in this order:

  1. drives `screen_text` over a case list against BOTH the PRE-CHANGE screen.py (read out of git, by revision)
     and the working-tree one, and asserts:
       - every case matches WANT under the NEW file;
       - every case marked `must_stay_refused` is IDENTICAL under both files (the widening removed no refusal
         it was not meant to remove);
       - at least one case FLIPS (red under OLD, green under NEW) — otherwise the change is not proven at all.
  2. drives `screen_bodies` — THE CALL check.py ACTUALLY MAKES (`check.py` line: `scr.screen_bodies(bodies)`) —
     over the REAL landed artifact of the campaign's one screened episode, under both files.
  3. prints the flip count so the caller can see the change is neither empty nor larger than declared.

usage: screen_widening_proof.py [--rev <git rev of the pre-change screen.py>] [--bodies <a real bodies.json>]
exit 0 iff every assertion holds.
"""
import argparse, importlib.util, json, os, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
RELPATH = "harness/s2lean/screen.py"

# (body, want-under-NEW, must_stay_refused)
#   must_stay_refused=True  -> the OLD and NEW verdicts must be IDENTICAL (a guard the widening must not touch)
#   must_stay_refused=False -> the case is allowed to flip; at least one such case MUST flip, or nothing is proven
CASES = [
    # ---- the widening itself: the two forms of a linter suppression ----
    ("set_option linter.deprecated false\n\ntheorem t : True := trivial", [], False),
    ("set_option linter.deprecated false in\ntheorem t : True := trivial", [], False),
    ("set_option linter.unusedVariables true in\nexact foo", [], False),
    ("set_option linter.style.longLine false\nexact foo", [], False),
    # ---- the production instance, verbatim from problem_112/a2 (ep-6b5540c0) ----
    ("set_option linter.deprecated false\n\n/-- `String.data` is the deprecated spelling of `String.toList`. -/\n"
     "theorem iso_data_eq_toList (s : String) : s.data = s.toList := rfl", [], False),
    # ---- the guards the widening MUST NOT touch: identical under both files ----
    ("set_option debug.skipKernelTC true in\ntheorem x : True := trivial", ["set_option@1"], True),
    ("set_option debug.skipKernelTC true\ntheorem x : True := trivial", ["set_option@1"], True),
    ("set_option pp.all true\nexact foo", ["set_option@1"], True),
    ("set_option maxHeartbeats 400000\nby simp", ["set_option@1"], True),
    ("set_option linterFoo.bar false\nexact foo", ["set_option@1"], True),        # not the linter NAMESPACE
    ("set_option linter false\nexact foo", ["set_option@1"], True),               # bare `linter`, no dotted leaf
    ("set_option linter.deprecated 5\nexact foo", ["set_option@1"], True),        # value is not a boolean
    ("axiom cheat (P : Prop) : P\nexact cheat _", ["axiom@1"], True),
    ("run_cmd liftTermElabM do pure ()", ["run_cmd@1"], True),
    # ---- the smuggling arm: a permitted linter pragma must not carry a forbidden one through with it ----
    ("set_option linter.deprecated false in\nset_option debug.skipKernelTC true in\nexact foo", ["set_option@2"], False),
]


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--rev", default="HEAD", help="git rev holding the PRE-CHANGE screen.py")
    ap.add_argument("--bodies", default=os.path.join(REPO, "evidence", "amend9-refused-cell-2026-08-31",
                                                     "04-the-refused-bodies-AS-LANDED.json"))
    a = ap.parse_args()

    blob = subprocess.check_output(["git", "-C", REPO, "show", "%s:%s" % (a.rev, RELPATH)])
    tmp = tempfile.mkdtemp(prefix="screenproof-")
    oldp = os.path.join(tmp, "screen_old.py"); open(oldp, "wb").write(blob)
    old = load(oldp, "screen_old"); new = load(os.path.join(HERE, "screen.py"), "screen_new")
    print("PRE-CHANGE screen.py from %s (%d B); WORKING-TREE screen.py (%d B)"
          % (a.rev, len(blob), os.path.getsize(os.path.join(HERE, "screen.py"))))

    bad = flips = 0
    print("\n%-6s %-6s %-6s  %s" % ("OLD", "NEW", "WANT", "case"))
    for body, want, guard in CASES:
        o, n = old.screen_text(body), new.screen_text(body)
        okn = (n == want)
        okg = (o == n) if guard else True
        flip = (o != n)
        flips += flip and not guard
        bad += (not okn) or (not okg)
        print("%-6s %-6s %-6s  %s%s%s  %r"
              % ("RED" if o else "green", "RED" if n else "green", "RED" if want else "green",
                 "" if okn else "[WANT-MISMATCH] ", "" if okg else "[GUARD MOVED] ",
                 "FLIP" if flip else "    ", body.split("\n")[0][:64]))

    # ---- 2. THE CALL check.py ACTUALLY MAKES, on the real landed artifact ----
    print("\n-- screen_bodies() on the real landed artifact (the call check.py makes) --")
    if os.path.exists(a.bodies):
        b = json.load(open(a.bodies))
        ob, nb = old.screen_bodies(b), new.screen_bodies(b)
        print("   %s\n   OLD -> %r\n   NEW -> %r" % (os.path.relpath(a.bodies, REPO), ob, nb))
        if ob == []: print("   [FAIL] the OLD screen did not refuse the landed artifact — this is not the red case"); bad += 1
        if nb != []: print("   [FAIL] the NEW screen still refuses the landed artifact"); bad += 1
    else:
        print("   [FAIL] no bodies artifact at %s" % a.bodies); bad += 1

    print("\nflips (red->green, non-guard cases): %d" % flips)
    if flips == 0: print("[FAIL] nothing flipped: the change is unproven"); bad += 1
    print("screen widening proof: %s" % ("PASS" if bad == 0 else "FAIL (%d)" % bad))
    return 0 if bad == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
