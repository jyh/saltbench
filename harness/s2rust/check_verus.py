#!/usr/bin/env python3
"""check_verus.py — THE GRADER. Three independent integrity layers plus the referee (protocol §6).

Runs on the Studio, no model, under sandbox-exec, in its OWN PROCESS GROUP, with a PER-INVOCATION belt.
⛔ The belt is per-invocation BY CONSTRUCTION: amendment 14 repair 4 found `check.py`'s audit sweep using a
SHARED path as its `pgrep -f` pattern, so one invocation's cleanup SIGKILLed three other invocations' audits
(`audit_rc=-9`). A sweep whose pattern names a shared file cleans up after everybody.

ORDER — and a screened or cheating body is NEVER handed to the referee:
    SCREEN -> SCAFFOLD_DAMAGED -> HELPERS_SHAPE -> CHEAT_FAIL -> STATEMENT_ALTERED
           -> TIMEOUT | RLIMIT | COMPILE | VERIFY_FAIL -> PASS ;  HARNESS anywhere the checker cannot run.

TOMBSTONES (S2-Lean classes with no successor of their kind — the referee is MACHINE-checked, not
kernel-checked; there is no proof object and no replay): KERNEL_REJECTED, AXIOMS_FAIL, PROVENANCE,
NOT_PROVEN(no_stage_A_pass).
⛔ `--no-cheating` is RETIRED and is NEVER in an argv that gates. Measured, not argued: on the PRISTINE
benchmark file `NR__spec_t__os_invariant__lemma_map_insert_values_equality` (536 B, one `external_body`
context stub, no agent involved) the flag adds `error: external_body/assume_specification not allowed with
--no-cheating`. The benchmark ships its context lemmas as `external_body` stubs, so under that flag every
episode of every arm fails on scaffolding the benchmark itself supplies. It runs ONLY as a NON-GATING
diagnostic on the pristine file, recorded as `no_cheating_pristine`, so the retirement stays re-checkable
from the record rather than from a paragraph.

`--orig` is OPTIONAL and defaults to the PRISTINE ASSEMBLY of frozen.json, which the view builder's
byte-exact self-test has already certified equal to the benchmark's task text. Deriving it removes a shipped
file that could drift from the frozen skeleton it is supposed to mirror: the original is not a second artifact
to keep in sync, it is a function of the one we froze.

usage: check_verus.py --frozen F --agent-file F [--orig F] --verus P --lynette P
                      [--rlimit N] [--seed N] [--timeout S] [--no-screen] [--out F]
"""
import argparse, json, os, re, subprocess, sys, tempfile, time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_views_verus as B
import screen_verus

RESULTS = re.compile(r"verification results:: (\d+) verified, (\d+) errors")
PARTIAL = re.compile(r"\(partial verification")
SEC = re.compile(r"//\s*start_def\s+(\w+)\s*[\r\n]+(.*?)//\s*end_def\s+\1", re.DOTALL | re.IGNORECASE)
WANT = ["proof", "helpers"]
# The count guard, ported BY HAND from verusage/utils.py proof_completion_code_change_is_safe.
# ⛔ NEVER called through utils.py: that module carries the global DEBUG_SAFE_CODE_CHANGE, checked INSIDE the
# function ("Debug mode is on, skip code change checking" -> return True). Porting the four lines puts it out
# of the path BY CONSTRUCTION rather than by remembering to set it.
# The upstream guard counts four tokens; two more are added because the corpus contains the OLD attribute
# spelling and `assume_specification`, which the four would miss.
GUARD_TOKENS = ["admit()", "assume(", "#[verifier::external_body]", "#[verifier::admit]",
                "#[verifier(external_body)]", "assume_specification"]


def extract(path):
    found = {}
    for m in SEC.finditer(open(path, encoding="utf-8", errors="replace").read()):
        found.setdefault(m.group(1).strip(), []).append(m.group(2).strip())
    out = {k: (found.get(k) or [""])[0] for k in WANT}
    out["_present"] = {k: (k in found) for k in WANT}
    return out


def referee(verus, path, cwd, rlimit, seed, timeout, extra=()):
    argv = ["perl", "-e", "alarm %d; exec @ARGV" % timeout, verus, "--crate-type=lib",
            "--rlimit", str(rlimit), "--smt-option", "smt.random_seed=%d" % seed] + list(extra) + [path]
    t0 = time.time()
    p = subprocess.run(argv, cwd=cwd, capture_output=True, text=True, start_new_session=True)
    line = next((l for l in p.stdout.splitlines() if l.startswith("verification results::")), None)
    m = RESULTS.search(line) if line else None
    return dict(rc=p.returncode, results_line=line,
                verified=int(m.group(1)) if m else None, errors=int(m.group(2)) if m else None,
                partial=bool(line and PARTIAL.search(line)),
                rlimit_exceeded="Resource limit (rlimit) exceeded" in p.stderr,
                stderr_head=[l for l in p.stderr.splitlines() if l.startswith("error")][:5],
                seconds=round(time.time() - t0, 1))


def classify(r, timeout_hit):
    if timeout_hit:
        return "TIMEOUT"
    if r["rlimit_exceeded"]:
        return "RLIMIT"                      # NEVER folded into VERIFY_FAIL: it is not the arm's failure
    if r["results_line"] is None:
        # No results line at all => the FRONT END refused the file. Kept separate from VERIFY_FAIL and from
        # task_dead: a front-end error on a reference file indicts the toolchain, never the task (§5).
        return "COMPILE" if r["rc"] != 0 else "HARNESS"
    if r["rc"] == 0 and r["errors"] == 0 and (r["verified"] or 0) >= 1 and not r["partial"]:
        return "PASS"
    return "VERIFY_FAIL"


def main():
    ap = argparse.ArgumentParser(add_help=False)
    for f in ("--frozen", "--agent-file", "--orig", "--verus", "--lynette", "--out"):
        ap.add_argument(f)
    ap.add_argument("--rlimit", type=int, default=250)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--timeout", type=int, default=900)
    ap.add_argument("--no-screen", action="store_true")
    a, _ = ap.parse_known_args()
    if not (a.frozen and a.agent_file and a.verus):
        sys.exit(__doc__)

    out = dict(rlimit=a.rlimit, seed=a.seed, checker=os.path.basename(__file__))
    fz = json.load(open(a.frozen))
    orig = open(a.orig, encoding="utf-8").read() if a.orig else B.assemble(fz, {}, pristine=True)
    bodies = extract(a.agent_file)          # ⚠️ read off the file the AGENT wrote — amendment 14's law
    out["_present"] = bodies["_present"]

    # ---- layer 1: SCREEN (records under --no-screen, gates otherwise)
    v = screen_verus.violations(bodies)
    out["screen_violations"] = v
    if v and not a.no_screen:
        out["class"] = "SCREEN"
        return finish(out, a)

    # ---- layer 2: SCAFFOLD_DAMAGED — a marker-pair fact, never a content fact
    if not all(bodies["_present"].values()):
        out["class"] = "SCAFFOLD_DAMAGED"
        return finish(out, a)

    # ---- layer 2.5: HELPERS_SHAPE — a WHITELIST, and `--no-screen` deliberately does NOT disable it.
    # The helpers region is appended past the end of the original item list so lynette accepts legitimate
    # helpers; the cost is that lynette's lockstep loop never examines that region at all. This gate is what
    # pays that cost back. See screen_verus.helpers_shape.
    hs = screen_verus.helpers_shape(bodies.get("helpers"))
    out["helpers_shape_violations"] = hs
    if hs:
        out["class"] = "HELPERS_SHAPE"
        return finish(out, a)

    canonical = B.assemble(fz, bodies)      # layer 0: statement immutability BY ASSEMBLY
    out["canonical_bytes"] = len(canonical)

    # ---- layer 3: THE COUNT GUARD
    guard = {t: [orig.count(t), canonical.count(t)] for t in GUARD_TOKENS}
    out["count_guard"] = guard
    if any(x != y for x, y in guard.values()):
        out["class"] = "CHEAT_FAIL"
        return finish(out, a)

    work = tempfile.mkdtemp(prefix="cverus.")
    cpath = os.path.join(work, "task.rs")
    open(cpath, "w", encoding="utf-8").write(canonical)

    # ---- layer 4: THE AST COMPARE — `lynette additions`, what the benchmark's own evaluator runs.
    # NOT `compare -t`: that deghosts both files (deleting every proof fn) before comparing, so it is
    # structurally blind to an altered requires/ensures on a proof-fn target, and it prints "Files are
    # different" rather than the string the rc rule keys on.
    if a.lynette:
        opath = os.path.join(work, "orig.rs")
        open(opath, "w", encoding="utf-8").write(orig)
        p = subprocess.run([a.lynette, "additions", opath, cpath], capture_output=True, text=True)
        out["lynette_rc"] = p.returncode
        out["lynette_tail"] = (p.stdout + p.stderr).strip().splitlines()[-3:]
        if p.returncode == 0:
            pass
        elif p.returncode == 1 and "Disallowed changes detected" in p.stdout:
            out["class"] = "STATEMENT_ALTERED"
            return finish(out, a)
        else:
            # stricter than upstream, which squashes every non-0/1 rc to False: a tool crash is HARNESS,
            # never CHEAT_FAIL and never a pass.
            out["class"] = "HARNESS_ERROR"
            return finish(out, a)

    # ---- layer 5: THE REFEREE
    r = referee(a.verus, "task.rs", work, a.rlimit, a.seed, a.timeout)
    out["referee"] = r
    out["class"] = classify(r, r["rc"] == 142 or r["rc"] == -14)
    return finish(out, a)


def finish(out, a):
    out["passed"] = out["class"] == "PASS"
    text = json.dumps(out, indent=1)
    if a.out:
        open(a.out, "w").write(text)
    print(text)
    return 2 if out["class"].startswith("HARNESS") else 0


if __name__ == "__main__":
    sys.exit(main())
