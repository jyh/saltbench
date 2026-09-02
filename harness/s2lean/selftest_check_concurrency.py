#!/usr/bin/env python3
"""selftest_check_concurrency.py — the driven gate for check.py's process-sweep BELT PATTERN
(amendment 14, 2026-09-01).

⛔ THE DEFECT IT CLOSES, measured not theorised. `run_fenced` sweeps `pgrep -f <belt>` and SIGKILLs every
match. The compile and pristine steps pass per-invocation source paths; the AUDIT step passed `a.audit` —
`<harness>/s2audit.lean`, **identical for every invocation**. Two `check.py` runs against the same harness
therefore kill each other's audits. Measured, three invocations staggered by 9 s under load:

    c1 class=HARNESS  audit_rc=-9  retry=-9  err=RuntimeError('audit did not run: no JSON on stdout (rc=-9)')

killed once, retried by FN-5, **killed again by the same sweep**. It fails LOUD — no episode can be
mis-scored — but it makes any concurrent checker run INTERMITTENT, and it is how this amendment's own new gate
first failed: green when published, red when re-run beside the controls.
⇒ ***A SWEEP WHOSE PATTERN NAMES A SHARED FILE DOES NOT CLEAN UP AFTER ITSELF, IT CLEANS UP AFTER EVERYBODY.***

⛔⛔ AND THE SECOND DEFECT, WHICH WAS IN THIS FILE'S FIRST CUT. That version reproduced the RACE: three
staggered invocations, asserting none is killed. It passed against the amended checker — and **it also passed
against the PRE-change checker**, because the collision needs one audit to be mid-flight when another sweeps,
which depends on machine load. **A gate whose red control only fires under load is a gate that reads green
for ever.** It is the same intermittency, one level up, in the instrument built to catch it.
⇒ The arm below does not race at all. It tests the defect ITSELF: a DECOY process whose command line contains
the shared audit path is started, one `check.py` runs to completion, and the decoy must SURVIVE. Under the
pre-change belt the decoy is SIGKILLed every time; under the amended belt it is never touched. **Deterministic
in both directions, single-invocation, no timing assumption.**

usage: python3 selftest_check_concurrency.py            env: LEANPROJ, VIEWS, EPISODE
"""
import argparse, json, os, shutil, signal, subprocess, sys, tempfile, time

HERE = os.path.dirname(os.path.abspath(__file__))


def refuse(msg):
    print("REFUSE: %s" % msg); sys.exit(2)


def alive(p):
    return p.poll() is None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", default=os.path.join(HERE, "check.py"))
    ap.add_argument("--leanproj", default=os.environ.get("LEANPROJ", os.path.expanduser("~/lean-shared/clever")))
    ap.add_argument("--views", default=os.environ.get("VIEWS", os.path.expanduser("~/bench-aw/s2views")))
    ap.add_argument("--problem", default="problem_112")
    ap.add_argument("--episode", default=os.environ.get("EPISODE", os.path.expanduser("~/bench-aw/state/ep-2714f8d2")))
    a = ap.parse_args()

    fzp = os.path.join(a.views, a.problem, "frozen.json")
    for p, what in ((a.check, "check.py"), (a.leanproj, "LEANPROJ"), (fzp, "frozen.json"), (a.episode, "the episode")):
        if not os.path.exists(p): refuse("%s does not exist: %s" % (what, p))
    audit_path = os.path.join(os.path.dirname(os.path.abspath(a.check)), "s2audit.lean")
    if not os.path.exists(audit_path): refuse("no s2audit.lean beside %s" % a.check)
    fz = json.load(open(fzp))
    can = open(os.path.join(a.episode, "canonical.lean"), encoding="utf-8").read()
    i = can.index(fz["generated_spec_header"]) + len(fz["generated_spec_header"])
    a_body = can[i:can.index("\ndef problem_spec")].strip()
    if not a_body: refuse("could not recover the stage-A generated_spec body")

    W = tempfile.mkdtemp(prefix="concurrency-selftest-")
    fails = []

    def check(name, cond, detail=""):
        print("  %-6s %s%s" % ("PASS" if cond else "FAIL", name, "" if cond else "   << " + str(detail)[:400]))
        if not cond: fails.append(name)

    # The DECOY: a harmless sleeper whose argv carries the SHARED audit path, so `pgrep -f <audit path>`
    # matches it and `pgrep -f <this invocation's olean>` does not. It stands in for another seat's, or
    # another run's, in-flight audit. It touches nothing and is killed by this test at the end.
    decoy = subprocess.Popen([sys.executable, "-c", "import time; time.sleep(240)", audit_path])
    try:
        if not alive(decoy): refuse("the decoy died before the test began — it proves nothing")
        d = os.path.join(W, "run"); os.makedirs(d)
        bp = os.path.join(d, "bodies.json")
        json.dump({"spec_isomorphism_proof": "by sorry", "iso_helper_lemmas": "",
                   "_present": {"spec_isomorphism_proof": True, "iso_helper_lemmas": True}}, open(bp, "w"))
        abp = os.path.join(d, "A.bodies.json"); json.dump({"generated_spec_body": a_body}, open(abp, "w"))
        p = subprocess.run([sys.executable, a.check, "B", fzp, bp, a.leanproj,
                            os.path.join(d, "canonical.lean"), "--a-bodies", abp, "--timeout", "600"],
                           cwd=a.leanproj, capture_output=True, text=True)
        try: j = json.loads(p.stdout)
        except ValueError: j = {"class": "NO-JSON", "harness_error": (p.stderr or p.stdout)[-300:]}
        time.sleep(1)
        survived = alive(decoy)

        print("     verdict=%s audit_rc=%s retry=%s   decoy=%s" % (
            j.get("class"), j.get("audit_rc"), j.get("audit_retry"), "ALIVE" if survived else "KILLED"))
        check("the audit's sweep does NOT kill a process it does not own",
              survived, "the decoy carrying %s was SIGKILLed by check.py's audit sweep" % audit_path)
        check("and the check itself still reaches its real verdict",
              j.get("class") == "AXIOMS_FAIL", j.get("class"))
        check("its own audit is never SIGKILLed and FN-5's retry is unused",
              j.get("audit_retry") is None and not (isinstance(j.get("audit_rc"), int) and j["audit_rc"] < 0),
              (j.get("audit_rc"), j.get("audit_retry")))
    finally:
        try:
            decoy.kill(); decoy.wait(timeout=10)
        except Exception:
            pass
        shutil.rmtree(W, ignore_errors=True)

    print("SELF-TEST %s — 1 arm driven (a decoy carrying the shared audit path, one real check.py invocation), "
          "deterministic in both directions" % ("PASS" if not fails else "FAIL: " + ", ".join(fails)))
    return 0 if not fails else 1


if __name__ == "__main__":
    sys.exit(main())
