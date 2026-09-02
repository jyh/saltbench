#!/usr/bin/env python3
"""selftest_settings_verus.py — the AGENT fence's arms (amendment 16). Row CO, on the agent side.

The checker's fence is gated by selftest_fence_verus.py. This file gates the OTHER fence — the one the
AGENT runs under — because they are two independent instruments and only one of them was ever measured.

  C1  the rendered fence DENIES the run's own state root, derived from $BENCH
  C2  a SIBLING root is covered when $BENCH names it — the exact case the static fence missed
  C3  a DIFFERENT root is NOT denied — so C1/C2 prove derivation, not a blanket deny
  C4  an UNSET/empty $BENCH REFUSES rather than defaulting to ~/bench
  C5  the hook path is DERIVED from the same root, not hardcoded to ~/bench/harness
  C6  the rendering is valid JSON and its sandbox block is intact (enabled, failIfUnavailable, no network)
  C7  --check ACCEPTS a faithful rendering
  C8  --check REFUSES a tampered one (a deny-read entry deleted) — the red arm that makes C7 mean something
  C9  --check REFUSES a rendering made for a DIFFERENT root — a fence can be well-formed and still be the
      wrong run's fence, which is precisely how the static one kept passing while protecting nothing

usage: selftest_settings_verus.py
"""
import json, os, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import render_settings_verus as R

# ⛔ Every arm below must now pass a CONFIG DIR: since 09/02 the fence derives TWO roots (the state
# root from $BENCH and the agent config dir from $CFG) and the renderer REFUSES an unset cfg rather
# than defaulting — a default is how the config dir came to be another run's for a whole P0 read.
CFG_FIXTURE = "/Users/jyh/.claude-bench-rust"

PASS, FAIL = [], []


def arm(name, ok, detail=""):
    (PASS if ok else FAIL).append(name)
    print("  %s %-40s %s" % ("PASS" if ok else "FAIL", name, detail))


def deny_of(txt):
    return json.loads(txt)["sandbox"]["filesystem"]["denyRead"]


def main():
    root = "/Users/jyh/bench-a8"          # a real sibling root from the campaign's own history
    other = "/Users/jyh/bench-c"
    txt = R.render(root, None, CFG_FIXTURE)
    deny = deny_of(txt)

    arm("C1 run's own root is denied", os.path.realpath(root) in deny, root)
    arm("C2 sibling root covered when named",
        os.path.realpath(root) in deny and not os.path.realpath(root).startswith(
            os.path.realpath(os.path.expanduser("~/bench")) + os.sep),
        "a subpath deny on ~/bench would NOT have reached it")
    arm("C3 a different root is NOT denied", os.path.realpath(other) not in deny,
        "proves derivation, not a blanket deny")

    try:
        R.render("", None, CFG_FIXTURE)
        ok4 = False
    except SystemExit:
        ok4 = True
    arm("C4 empty $BENCH REFUSES", ok4, "no silent fallback to ~/bench")

    hook = json.loads(txt)["hooks"]["PreToolUse"][0]["hooks"][0]["command"]
    arm("C5 hook path derived from the root", hook.startswith(os.path.realpath(root) + os.sep), hook)

    sb = json.loads(txt)["sandbox"]
    arm("C6 sandbox block intact",
        sb["enabled"] and sb["failIfUnavailable"] and not sb["allowUnsandboxedCommands"]
        and sb["network"]["strictAllowlist"] and sb["network"]["allowedDomains"] == [],
        "enabled+failIfUnavailable+no network")

    work = tempfile.mkdtemp(prefix="setverus.")
    good = os.path.join(work, "settings.json")
    open(good, "w").write(txt)
    def check(path, bench):
        p = subprocess.run([sys.executable, os.path.join(HERE, "render_settings_verus.py"),
                            "--check", path, "--bench", bench, "--cfg", CFG_FIXTURE],
                           capture_output=True, text=True)
        return p.returncode, (p.stdout + p.stderr).strip()

    rc, out = check(good, root)
    arm("C7 --check accepts a faithful rendering", rc == 0, out[:60])

    # C8 — the RED arm. Remove one deny-read entry, exactly the tamper this gate exists to catch.
    d = json.loads(txt); d["sandbox"]["filesystem"]["denyRead"] = deny[1:]
    bad = os.path.join(work, "tampered.json"); open(bad, "w").write(json.dumps(d, indent=2))
    rc, out = check(bad, root)
    arm("C8 --check REFUSES a tampered fence", rc != 0, out[:60])

    # C9 — well-formed, but rendered for the WRONG root.
    rc, out = check(good, other)
    arm("C9 --check REFUSES another root's fence", rc != 0, out[:60])

    # C10/C11 — THE SELF-BLOCK ARM. Two episodes PASSED before this existed, both of them blind: the fence
    # derived from $BENCH denied the agent its own episode dir, because the workspace had been placed inside
    # the root the fence protects. The agent tried `../rt` three times and failed silently every time.
    #   ⇒ A FENCE DERIVED FROM THE RUN ROOT MUST NOT CONTAIN THE AGENT'S OWN WORKSPACE.
    def blocked(ep, bench):
        d = deny_of(R.render(bench, None, CFG_FIXTURE))
        return [x for x in d if ep == x or ep.startswith(os.path.realpath(os.path.expanduser(x)) + os.sep)]
    inside = os.path.join(root, "work", "ep-deadbeef")
    outside = os.path.join(os.path.expanduser("~"), "work", "ep-deadbeef")
    arm("C10 workspace INSIDE the root is caught", bool(blocked(inside, root)),
        "this is the defect that let two blind episodes score")
    arm("C11 workspace OUTSIDE the root is fine", not blocked(outside, root),
        "so C10 is the containment test, not a blanket refusal")

    print("\nsettings-fence selftest: %d arms, %d failed" % (len(PASS) + len(FAIL), len(FAIL)))
    if FAIL:
        print("  failed: %s" % ", ".join(FAIL))
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
