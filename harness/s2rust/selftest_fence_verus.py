#!/usr/bin/env python3
"""selftest_fence_verus.py — THE FENCE'S OWN ARMS (amendment 16). Zero model tokens.

Every arm here is driven RED FIRST, and amendment 14's law binds the whole file: **a gate must fail on the
broken version EVERY time — reproducing a defect is not gating it.**

WHAT THIS FILE EXISTS TO STOP BEING TRUE. `check_verus.py`'s docstring claimed "under sandbox-exec, in its
OWN PROCESS GROUP, with a PER-INVOCATION belt" from the day it was written, and the code had none of it:
the paragraph was inherited verbatim from `s2lean/check.py`, where every clause is true. Nothing caught it
because nothing ever ASKED THE RUNNING PROGRAM whether it was fenced.
  => A DOCSTRING COPIED FROM A FILE WHERE IT WAS TRUE IS AN ASSERTION ABOUT THE FILE IT CAME FROM.

THE ARMS:
  A1-A4  THE EXEC LADDER — each of the four binaries proven NECESSARY by its own red arm, in which the error
         text names the next binary in the chain. This is what establishes the set, and it is why the set is
         a whitelist proven by measurement rather than a list someone wrote down.
  A5     FORK IS REQUIRED — `(deny process-fork)`, which S2-Lean uses, BREAKS Verus. The widening is forced
         by the tool, and this arm is what keeps that a measured claim instead of a remembered one.
  A6-A9  THE FOUR LEGS, each by positive control on the production profile text with ONE declared difference
         (/bin/sh + /bin/bash added so a probe can exercise legs Verus itself never touches).
  A10    NOT BLANKET — a non-denied path stays readable, so A6 is proven to bite without over-denying.
  A11    ROW CO — the deny-read set DERIVES from $BENCH: a sibling state root must be denied when $BENCH
         names it, and an UNSET $BENCH must contribute no root rather than a guessed one.
  A12    THE DIFFERENTIAL — a real reference file scores the same verdict fenced and unfenced.
  A13    THE FENCE IS ON BY DEFAULT — `check_verus.referee`'s default is fenced=True. An opt-in fence that
         nobody opts into is the docstring defect again, one layer down.

usage: selftest_fence_verus.py [--verus P]   (default: the seat's pinned release)
"""
import json, os, re, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import check_verus as C

DEFAULT_VERUS = os.path.expanduser("~/bench-src/verus-release-pin/verus-arm64-macos/verus")
GT_FIXTURE = """// a 1.3 kB proof-only shape is NOT representative: see arm A12's note.
use vstd::prelude::*;
verus!{
proof fn add_zero(x: int)
    ensures x + 0 == x
{
}
}
fn main() {}
"""

PASS, FAIL = [], []


def arm(name, ok, detail=""):
    (PASS if ok else FAIL).append(name)
    print("  %s %-34s %s" % ("PASS" if ok else "FAIL", name, detail))


def sandbox_run(profile, argv, cwd):
    p = subprocess.run(["/usr/bin/sandbox-exec", "-p", profile] + argv, cwd=cwd,
                       capture_output=True, text=True, env=dict(os.environ, TMPDIR=cwd))
    return p.returncode, p.stdout + p.stderr


def ladder_profile(verus, work, n):
    """The production profile with the exec allow-list TRUNCATED to the first n of the four binaries."""
    tmpl = open(C.PROFILE_TEMPLATE, encoding="utf-8").read()
    ex = " ".join('(literal "%s")' % b for b in C.verus_exec_set(verus)[:n])
    dr = " ".join('(subpath "%s")' % p for p in C.deny_read_paths(None))
    return (tmpl.replace("__EXEC_ALLOW__", ex).replace("__DENY_READ__", "(deny file-read* %s)" % dr)
                .replace("__WRITE_PATHS__", '(subpath "%s")' % os.path.realpath(work)))


def main():
    verus = DEFAULT_VERUS
    for i, a in enumerate(sys.argv):
        if a == "--verus" and i + 1 < len(sys.argv): verus = sys.argv[i + 1]
    if not os.path.exists(verus):
        sys.exit("selftest_fence_verus: no verus at %s — REFUSE, never skip: a fixture that cannot be built "
                 "proves nothing (amendment 12's law)." % verus)

    work = tempfile.mkdtemp(prefix="fencetest.")
    src = os.path.join(work, "task.rs")
    open(src, "w").write(GT_FIXTURE)
    names = ["verus", "rustup", "rust_verify", "z3"]
    print("EXEC SET (derived, not typed): %s" % " ".join(os.path.basename(b) for b in C.verus_exec_set(verus)))

    # ---- A1-A4: the ladder. Each truncated arm must FAIL, and its error must NAME the next binary.
    expect = {1: "rust_verify", 2: "rust_verify", 3: "z3"}
    for n in (1, 2, 3):
        rc, out = sandbox_run(ladder_profile(verus, work, n), [verus, "--crate-type=lib", "task.rs"], work)
        named = expect[n] in out
        denied = "not permitted" in out.lower()
        arm("A%d exec-ladder allow=%d" % (n, n), rc != 0 and named and denied,
            "rc=%d names=%r denied=%s" % (rc, expect[n], denied))
    rc, out = sandbox_run(ladder_profile(verus, work, 4), [verus, "--crate-type=lib", "task.rs"], work)
    arm("A4 exec-ladder allow=4 GREEN", rc == 0 and "0 errors" in out, "rc=%d" % rc)

    # ---- A5: fork is REQUIRED (the widening over s2lean's profile is forced, not chosen)
    nofork = ladder_profile(verus, work, 4).replace("(deny process-exec*)",
                                                    "(deny process-fork)\n(deny process-exec*)")
    rc, out = sandbox_run(nofork, [verus, "--crate-type=lib", "task.rs"], work)
    arm("A5 deny-process-fork BREAKS verus", rc != 0, "rc=%d" % rc)

    # ---- A6-A10: the legs, by positive control. ONE declared difference: a shell is admitted so the probe
    # can reach legs Verus itself never touches. Nothing else about the profile text changes.
    ctl = C.render_profile(verus, work, None).replace(
        "(allow process-exec ", '(allow process-exec (literal "/bin/sh") (literal "/bin/bash") ')
    escape = os.path.expanduser("~/FENCE_ESCAPE_PROBE_SELFTEST")
    def probe(script):
        return sandbox_run(ctl, ["/bin/bash", "-c", script], work)
    _, o = probe('read -r _ < ~/.ssh/known_hosts 2>/dev/null && echo READ_OK || echo READ_DENIED')
    arm("A6 deny-read credential tree", "READ_DENIED" in o)
    # ⛔ THE PROBE FILE IS REMOVED FIRST, AND AGAIN AFTER. Found by driving mutation M2 (remove
    # `(deny file-write*)`): that arm correctly went red, the probe file was really created — and it then
    # SURVIVED into every later run, so A7 stayed red on an unmutated tree with the fence working.
    #   ⇒ AN ARM THAT LEAVES ITS OWN EVIDENCE ON DISK STOPS MEASURING THE FENCE AND STARTS MEASURING ITS
    #     OWN HISTORY — a false red that outlives its cause is as useless as a false green, and worse to
    #     debug, because the tree it accuses is clean.
    if os.path.exists(escape): os.remove(escape)
    _, o = probe(': > %s 2>/dev/null && echo WROTE || echo WRITE_DENIED' % escape)
    leaked = os.path.exists(escape)
    if leaked: os.remove(escape)
    arm("A7 deny-write outside workdir", "WRITE_DENIED" in o and not leaked,
        "no file on disk=%s" % (not leaked))
    _, o = probe(': > %s/inside 2>/dev/null && echo INSIDE_OK || echo INSIDE_DENIED' % work)
    arm("A8 workdir IS writable", "INSIDE_OK" in o)
    _, o = probe('exec 3<>/dev/tcp/1.1.1.1/443 2>/dev/null && echo NET_OK || echo NET_DENIED')
    arm("A9 deny-network", "NET_DENIED" in o)
    _, o = probe('/usr/bin/whoami >/dev/null 2>&1 && echo EXEC_OK || echo EXEC_DENIED')
    arm("A10a unlisted exec denied", "EXEC_DENIED" in o)
    _, o = probe('read -r _ < %s 2>/dev/null && echo OK || echo DENIED' % src)
    arm("A10b fence is NOT blanket", "OK" in o, "an allowed path stays readable")

    # ---- A11: ROW CO — the deny set DERIVES from $BENCH
    sib = "/Users/jyh/bench-a8"
    got = C.deny_read_paths(sib)
    arm("A11a $BENCH root is denied", os.path.realpath(sib) in got, sib)
    arm("A11b sibling root NOT covered by ~/bench",
        not os.path.realpath(sib).startswith(os.path.realpath(os.path.expanduser("~/bench")) + os.sep),
        "this is the defect row CO names")
    env_clean = {k: v for k, v in os.environ.items() if k != "BENCH"}
    old = os.environ.pop("BENCH", None)
    try:
        unset = C.deny_read_paths(None)
    finally:
        if old is not None: os.environ["BENCH"] = old
    arm("A11c unset BENCH guesses NO root", len(unset) == len(C.DENY_READ),
        "an unset root must not silently become ~/bench")

    # ---- A11d/A11e: ROW CO's OWN REFUSAL ARM, as the desk row words it — "a GT file planted in a sibling
    # root => RED". Not a property of the path list: a real file, planted in a real sibling root, read
    # through the real rendered profile. The two arms are a PAIR and only the pair means anything: the same
    # file must be DENIED when $BENCH names its root and READABLE when it does not, because a fence that
    # denies everything would pass the first arm on its own.
    sib_root = os.path.join(work, "bench-sibling")
    os.makedirs(os.path.join(sib_root, "state"), exist_ok=True)
    planted = os.path.join(sib_root, "state", "gt.json")
    open(planted, "w").write('{"ground_truth": "proof { assert(false); }"}\n')
    def read_under(bench):
        prof = C.render_profile(verus, work, bench).replace(
            "(allow process-exec ", '(allow process-exec (literal "/bin/sh") (literal "/bin/bash") ')
        _, o = sandbox_run(prof, ["/bin/bash", "-c",
                                  'read -r _ < %s 2>/dev/null && echo GT_READ || echo GT_DENIED' % planted], work)
        return o
    arm("A11d CO: GT in sibling root DENIED", "GT_DENIED" in read_under(sib_root),
        "$BENCH=%s" % sib_root)
    arm("A11e CO: same file readable when $BENCH elsewhere", "GT_READ" in read_under(os.path.join(work, "other")),
        "proves A11d is the DERIVATION, not a blanket deny")

    # ---- A12: THE DIFFERENTIAL. ⛔ This fixture is proof-only and therefore NOT representative on its own —
    # the population differential (61 seeded reference files from AC u NR, 61/61 agree) is the real evidence
    # and lives in the evidence directory. This arm is the permanent, cheap sentinel over the same property.
    f = C.referee(verus, "task.rs", work, 250, 0, 300, fenced=True)
    u = C.referee(verus, "task.rs", work, 250, 0, 300, fenced=False)
    arm("A12 fenced verdict == unfenced",
        C.classify(f, f["timed_out"]) == C.classify(u, u["timed_out"]) == "PASS",
        "%s vs %s" % (C.classify(f, f["timed_out"]), C.classify(u, u["timed_out"])))

    # ---- A13: the fence is ON BY DEFAULT
    import inspect
    d = inspect.signature(C.referee).parameters["fenced"].default
    arm("A13 referee defaults to fenced", d is True, "default=%r" % d)

    print("\nFENCE SELFTEST: %d passed, %d FAILED" % (len(PASS), len(FAIL)))
    if FAIL:
        print("  failed: %s" % ", ".join(FAIL))
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
