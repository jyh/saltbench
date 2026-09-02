#!/usr/bin/env python3
"""selftest_s2audit.py — the driven gate for s2audit.lean's statement-value comparison (amendment 14, 2026-09-01).

⛔ THE LAW THIS FILE OBEYS (paid for by meter.py on 08/30): A SELF-TEST THAT NEVER MAKES THE CALL ITS CALLER
MAKES IS A SELF-TEST OF A DIFFERENT PROGRAM. Every arm compiles a REAL canonical/pristine pair with the real
`lean`, under the harness's own `sandbox_check.sb` fence, and runs `s2audit.lean` on the real argv as a
subprocess — never an in-process reimplementation of the comparison.

BOTH ARMS DIFFER. Arm 1 is the real specimen and must PASS the amended comparison; arms 2 and 3 are real
alterations of the same specimen and must be REFUSED by it. Without 2 and 3, a repair that simply returned
`value_identical = true` for everything would pass arm 1 and destroy the gate.

Runs on the Studio (needs lean + the shared CLEVER build). Refuses, loudly, if its inputs are absent —
a self-test that silently tests nothing is the failure it exists to prevent.

usage: python3 selftest_s2audit.py [--audit <s2audit.lean>]
"""
import argparse, json, os, shutil, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)


def refuse(msg):
    print("REFUSE: %s" % msg); sys.exit(2)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--audit", default=os.path.join(HERE, "s2audit.lean"))
    ap.add_argument("--leanproj", default=os.environ.get("LEANPROJ", os.path.expanduser("~/lean-shared/clever")))
    ap.add_argument("--views", default=os.environ.get("VIEWS", os.path.expanduser("~/bench-aw/s2views")))
    ap.add_argument("--problem", default="problem_112")
    ap.add_argument("--a-body", default=os.environ.get("A_BODY", ""),
                    help="the scored stage-A generated_spec body; default: read from the specimen episode")
    ap.add_argument("--episode", default=os.environ.get("EPISODE", os.path.expanduser("~/bench-aw/state/ep-2714f8d2")))
    a = ap.parse_args()

    import check as C
    from assemble import assemble

    for p, what in ((a.audit, "the audit"), (a.leanproj, "LEANPROJ"), (a.views, "VIEWS"), (a.episode, "the specimen episode")):
        if not os.path.exists(p): refuse("%s does not exist: %s" % (what, p))
    fzp = os.path.join(a.views, a.problem, "frozen.json")
    if not os.path.exists(fzp): refuse("no frozen.json at %s" % fzp)
    fz = json.load(open(fzp))
    bd = json.load(open(os.path.join(a.episode, "bodies.json")))
    # stage B merges the SAME arm's scored stage-A body (D5) — take it from the episode's own record.
    ab = a.a_body
    if not ab:
        abp = os.path.join(a.episode, "a_bodies.json")
        if os.path.exists(abp): ab = (json.load(open(abp)) or {}).get("generated_spec_body") or ""
    if not ab:
        # recover it from the episode's own canonical: everything between the header and problem_spec
        can = open(os.path.join(a.episode, "canonical.lean"), encoding="utf-8").read()
        i = can.index(fz["generated_spec_header"]) + len(fz["generated_spec_header"])
        ab = can[i:can.index("\ndef problem_spec")].strip()
    if not ab: refuse("could not recover the stage-A generated_spec body")
    bd = dict(bd); bd["generated_spec_body"] = ab

    W = tempfile.mkdtemp(prefix="s2audit-selftest-")
    env, lean = C.lake_env(a.leanproj)
    tmpl = open(os.path.join(HERE, "sandbox_check.sb")).read()
    fails, arms = [], 0

    def build(name, src):
        f = os.path.join(W, name + ".lean"); open(f, "w", encoding="utf-8").write(src)
        ol = os.path.join(W, name + ".olean")
        rc, out, wall, _, _ = C.run_fenced([lean, "--root=" + W, "-o", ol, f], W, env,
                                           C.render_profile(tmpl, lean, [W]), 900, f)
        return (rc, ol if rc == 0 else None, out)

    def audit(canon, pris):
        af = os.path.join(W, "audit.lean"); shutil.copy(a.audit, af)
        rc, out, wall, _, _ = C.run_fenced([lean, "--run", af, canon, pris, "B", "-"], W, env,
                                           C.render_profile(tmpl, lean, [W]), 900, af)
        js = [l for l in out.splitlines() if l.strip().startswith("{")]
        return json.loads(js[-1]) if js else {"error": out[-500:]}

    def check(name, cond, detail=""):
        print("  %-6s %s%s" % ("PASS" if cond else "FAIL", name, "" if cond else "   << " + str(detail)[:400]))
        if not cond: fails.append(name)

    try:
        canon_src = assemble("B", fz, bd)
        pris_src = assemble("B", fz, {}, pristine=True)
        rc, canon, out = build("canonical", canon_src)
        if not canon: refuse("the specimen canonical does not compile (rc=%s)\n%s" % (rc, out[-800:]))
        rc, pris, out = build("pristine", pris_src)
        if not pris: refuse("the pristine does not compile (rc=%s)\n%s" % (rc, out[-800:]))

        # ---------- ARM 1: the real specimen. The matcher is shared, the spec is untouched.
        arms += 1
        j = audit(canon, pris)
        ps = (j.get("statements") or {}).get("problem_spec") or {}
        check("arm1 the specimen's statements are IDENTICAL under the amended comparison",
              j.get("statements_identical") is True and j.get("statement_diffs") == [], j)
        check("arm1 the PRE-amendment verdict is preserved and is FALSE (the flip is on the record)",
              ps.get("value_identical_raw") is False and ps.get("value_identical") is True, ps)
        check("arm1 the flip is attributed to aux-matcher renaming, not asserted",
              ps.get("aux_matcher_renaming") is True, ps)
        check("arm1 the shared matcher really is owner-named (the mechanism, not a coincidence)",
              "generated_spec.match_1" in (j.get("constants") or []), j.get("constants"))

        # ---------- ARM 2: the SAME shared matcher, but problem_spec's MEANING altered — the empty-`c` clause
        # now constrains the result to `c` instead of `s`. The pattern-`let` (and therefore the shared matcher)
        # is untouched, so this arm asks the amended comparison the only question that matters: does normalising
        # the matcher's NAME also normalise away a real change in the SPEC? It must not.
        # 📌 My first cut of this arm swapped the two destructured components — which does not compile at all
        #    (`result_bool` would be a String). A fixture that cannot be built proves nothing, and the selftest
        #    REFUSED rather than skipping it, which is why it was noticed instead of silently passing three arms.
        arms += 1
        fz2 = dict(fz)
        assert "c.data.length = 0 → result_str = s" in fz2["problem_spec"], "fixture drift: clause not found"
        fz2["problem_spec"] = fz2["problem_spec"].replace(
            "c.data.length = 0 → result_str = s", "c.data.length = 0 → result_str = c")
        rc, c2, out = build("canonical_altered", assemble("B", fz2, bd))
        if not c2: refuse("the altered fixture does not compile (rc=%s)\n%s" % (rc, out[-800:]))
        j2 = audit(c2, pris)            # altered canonical vs the ORIGINAL frozen pristine
        ps2 = (j2.get("statements") or {}).get("problem_spec") or {}
        check("arm2 an ALTERED problem_spec is still REFUSED by the amended comparison",
              ps2.get("value_identical") is False and j2.get("statements_identical") is False, ps2)
        check("arm2 it is refused for the RIGHT declaration",
              j2.get("statement_diffs") == ["problem_spec"], j2.get("statement_diffs"))

        # ---------- ARM 3: a value change that leaves the matcher untouched (a constant in the body).
        arms += 1
        fz3 = dict(fz)
        assert "c.data.length = 0" in fz3["problem_spec"], "fixture drift: constant not found"
        fz3["problem_spec"] = fz3["problem_spec"].replace("c.data.length = 0", "c.data.length = 1")
        rc, c3, out = build("canonical_const", assemble("B", fz3, bd))
        if not c3: refuse("the constant-change fixture does not compile (rc=%s)\n%s" % (rc, out[-600:]))
        j3 = audit(c3, pris)
        ps3 = (j3.get("statements") or {}).get("problem_spec") or {}
        check("arm3 a changed CONSTANT inside problem_spec is still REFUSED",
              ps3.get("value_identical") is False, ps3)
        check("arm3 and its raw verdict agrees (this arm was never a false positive)",
              ps3.get("value_identical_raw") is False, ps3)

        # ---------- ARM 4: the NO-OP control. pristine vs pristine — nothing shared, nothing to normalise.
        arms += 1
        j4 = audit(pris, pris)
        ps4 = (j4.get("statements") or {}).get("problem_spec") or {}
        check("arm4 an unshared pair passes and is NOT attributed to renaming",
              ps4.get("value_identical") is True and ps4.get("value_identical_raw") is True
              and ps4.get("aux_matcher_renaming") is False, ps4)
        check("arm4 the pristine mints its OWN matcher (the other half of the mechanism)",
              "problem_spec.match_1" in (j4.get("constants") or []), j4.get("constants"))
    finally:
        shutil.rmtree(W, ignore_errors=True)

    print("SELF-TEST %s — %d arms driven (1 specimen, 2 alteration, 1 no-op control), every arm a real "
          "lean compile under the fence and a subprocess audit on the real argv"
          % ("PASS" if not fails else "FAIL: " + ", ".join(fails), arms))
    return 0 if not fails else 1


if __name__ == "__main__":
    sys.exit(main())
