#!/usr/bin/env python3
"""selftest_scaffold.py — the driven gate for check.py's SCAFFOLD_DAMAGED class (amendment 14, 2026-09-01).

Every arm runs the REAL `check.py` as a SUBPROCESS on its REAL argv, against a real frozen view and a real
`lake` toolchain — never an in-process call to the classifier. BOTH ARMS DIFFER: one arm must produce the new
class and three must NOT, because a change that emitted SCAFFOLD_DAMAGED unconditionally would pass a
one-armed test and destroy the taxonomy it was added to sharpen.

⛔ THE DISTINCTIONS UNDER TEST, each its own arm:
   damaged   — the marker PAIR is absent            ⇒ SCAFFOLD_DAMAGED   (pre-empts AXIOMS_FAIL)
   empty     — markers present, section empty       ⇒ unchanged          (an empty section is legitimate)
   unknown   — bodies.json has no `_present` at all ⇒ unchanged          (never convict on an unwritten field)
   control   — an ordinary honest `sorry`           ⇒ AXIOMS_FAIL        (the class it must not swallow)

usage: python3 selftest_scaffold.py            env: LEANPROJ, VIEWS, EPISODE
"""
import argparse, json, os, shutil, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)


def refuse(msg):
    print("REFUSE: %s" % msg); sys.exit(2)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", default=os.path.join(HERE, "check.py"))
    ap.add_argument("--leanproj", default=os.environ.get("LEANPROJ", os.path.expanduser("~/lean-shared/clever")))
    ap.add_argument("--views", default=os.environ.get("VIEWS", os.path.expanduser("~/bench-aw/s2views")))
    ap.add_argument("--problem", default="problem_112")
    ap.add_argument("--episode", default=os.environ.get("EPISODE", os.path.expanduser("~/bench-aw/state/ep-2714f8d2")))
    a = ap.parse_args()

    for p, what in ((a.check, "check.py"), (a.leanproj, "LEANPROJ"), (a.views, "VIEWS"), (a.episode, "the specimen episode")):
        if not os.path.exists(p): refuse("%s does not exist: %s" % (what, p))
    fzp = os.path.join(a.views, a.problem, "frozen.json")
    if not os.path.exists(fzp): refuse("no frozen.json at %s" % fzp)
    fz = json.load(open(fzp))
    can = open(os.path.join(a.episode, "canonical.lean"), encoding="utf-8").read()
    i = can.index(fz["generated_spec_header"]) + len(fz["generated_spec_header"])
    a_body = can[i:can.index("\ndef problem_spec")].strip()
    if not a_body: refuse("could not recover the stage-A generated_spec body from the specimen")

    W = tempfile.mkdtemp(prefix="scaffold-selftest-")
    fails, arms = [], 0

    def run(name, bodies):
        d = os.path.join(W, name); os.makedirs(d, exist_ok=True)
        bp = os.path.join(d, "bodies.json"); json.dump(bodies, open(bp, "w"))
        ab = os.path.join(d, "A.bodies.json"); json.dump({"generated_spec_body": a_body}, open(ab, "w"))
        cmd = [sys.executable, a.check, "B", fzp, bp, a.leanproj, os.path.join(d, "canonical.lean"),
               "--a-bodies", ab, "--timeout", "600"]
        p = subprocess.run(cmd, cwd=a.leanproj, capture_output=True, text=True)
        try:
            return json.loads(p.stdout)
        except ValueError:
            refuse("check.py produced no JSON for arm %s (rc=%s)\n%s" % (name, p.returncode, (p.stderr or p.stdout)[-800:]))

    def check(name, cond, detail=""):
        print("  %-6s %s%s" % ("PASS" if cond else "FAIL", name, "" if cond else "   << " + str(detail)[:400]))
        if not cond: fails.append(name)

    try:
        # ---------- ARM 1 (CONTROL): an honest sorry with intact markers. The class the new one must not swallow.
        arms += 1
        j = run("control", {"spec_isomorphism_proof": "by sorry", "iso_helper_lemmas": "",
                            "_present": {"spec_isomorphism_proof": True, "iso_helper_lemmas": True}})
        check("arm1 an honest sorry with intact markers is AXIOMS_FAIL, unchanged",
              j.get("class") == "AXIOMS_FAIL", j.get("class"))
        check("arm1 and it is not flagged as damaged",
              j.get("scaffold_damaged") is False and j.get("scaffold_missing") == [], j)

        # ---------- ARM 2: the marker pairs are GONE. Bodies empty, assemble substitutes the frozen defaults.
        arms += 1
        j = run("damaged", {"spec_isomorphism_proof": "", "iso_helper_lemmas": "",
                            "_present": {"spec_isomorphism_proof": False, "iso_helper_lemmas": False}})
        check("arm2 a damaged scaffold is SCAFFOLD_DAMAGED, not AXIOMS_FAIL",
              j.get("class") == "SCAFFOLD_DAMAGED", j.get("class"))
        check("arm2 it names WHICH sections were lost",
              j.get("scaffold_missing") == ["iso_helper_lemmas", "spec_isomorphism_proof"], j.get("scaffold_missing"))
        check("arm2 it still FAILS (both classes fail; only one accuses the agent)",
              j.get("passed") is False, j)
        check("arm2 the sorryAx is still visible in the record, not hidden by the new class",
              "sorryAx" in json.dumps(j.get("axioms") or {}), j.get("axioms"))

        # ---------- ARM 3: markers present, one section legitimately EMPTY. Must be unchanged.
        arms += 1
        j = run("empty", {"spec_isomorphism_proof": "by sorry", "iso_helper_lemmas": "",
                          "_present": {"spec_isomorphism_proof": True, "iso_helper_lemmas": True}})
        check("arm3 an EMPTY section with intact markers is NOT damage",
              j.get("class") == "AXIOMS_FAIL" and j.get("scaffold_damaged") is False, j.get("class"))

        # ---------- ARM 4: no `_present` key at all. UNKNOWN, never damaged.
        arms += 1
        j = run("unknown", {"spec_isomorphism_proof": "by sorry", "iso_helper_lemmas": ""})
        check("arm4 a bodies.json with no _present is UNKNOWN, and the class is unchanged",
              j.get("scaffold_unknown") is True and j.get("scaffold_damaged") is False
              and j.get("class") == "AXIOMS_FAIL", j)
    finally:
        shutil.rmtree(W, ignore_errors=True)

    print("SELF-TEST %s — %d arms driven (1 control, 1 damaged, 1 empty-section, 1 unknown-field), every arm a "
          "SUBPROCESS running the real check.py on the real argv"
          % ("PASS" if not fails else "FAIL: " + ", ".join(fails), arms))
    return 0 if not fails else 1


if __name__ == "__main__":
    sys.exit(main())
