#!/usr/bin/env python3
"""check_verus.py — THE GRADER. Three independent integrity layers plus the referee (protocol §6).

Runs on the Studio, no model, under sandbox-exec, in its OWN PROCESS GROUP, with a PER-INVOCATION belt.
⛔ The belt is per-invocation BY CONSTRUCTION: amendment 14 repair 4 found `check.py`'s audit sweep using a
SHARED path as its `pgrep -f` pattern, so one invocation's cleanup SIGKILLed three other invocations' audits
(`audit_rc=-9`). A sweep whose pattern names a shared file cleans up after everybody.

⛔⛔ THE SENTENCE ABOVE WAS FALSE OF THIS FILE FROM THE DAY IT WAS WRITTEN UNTIL AMENDMENT 16 (2026-09-02).
It was inherited verbatim from `s2lean/check.py`, where every clause of it is true. Here, a grep for
SANDBOX / sandbox-exec / killpg / belt over the code returned NOTHING but this comment: the referee ran
UNFENCED, in a bare `subprocess.run`, with no profile, no process-group kill and no belt at all. Of the three
properties the paragraph claims, exactly one (`start_new_session=True`) was implemented.
  ⇒ 🔑 A DOCSTRING COPIED FROM A FILE WHERE IT WAS TRUE IS AN ASSERTION ABOUT THE FILE IT CAME FROM. It reads
    as a receipt, it survives review because it is accurate prose about a real design, and it describes
    another program. The fence below is what makes it true here; it is not documentation of a fence, it is
    the fence.

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
import argparse, hashlib, json, os, re, shutil, signal, subprocess, sys, tempfile, time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build_views_verus as B
import screen_verus

SANDBOX = "/usr/bin/sandbox-exec"
PROFILE_TEMPLATE = os.path.join(HERE, "sandbox_verus.sb")

# Credential/config trees the fenced referee must not READ. The RUN'S OWN STATE ROOT is appended by
# `deny_read_paths` below, DERIVED from $BENCH — see row CO.
DENY_READ = ["~/.claude-bench", "~/.claude", "~/.ssh", "~/.aws", "~/.gnupg", "~/.config", "~/.gitconfig",
             "~/Library/Keychains", "~/Library/Application Support"]


def deny_read_paths(bench=None):
    """The deny-read set: the static credential trees PLUS the run's own state root, DERIVED.

    ⛔ ROW CO, AND IT IS THE REASON THIS IS A FUNCTION RATHER THAN A LIST. The S2-Lean fences name `~/bench`
    STATICALLY. Since 08/31 this campaign has deliberately run each new regime in its OWN state root
    (`~/bench-a8`, `~/bench-c`, `~/bench-aw`), and `/Users/jyh/bench-a8` is a SIBLING of `/Users/jyh/bench`,
    not a child of it — so a subpath deny on `~/bench` does not reach it. The state roots stayed protected
    only by an accident of how they were built (their `s2views` were symlinks resolving back into the denied
    subpath) and by the hook layer, whose escape pattern happens to match `bench-*`.
      ⇒ A FENCE THAT NAMES A PATH INSTEAD OF DERIVING ONE STOPS PROTECTING THE DAY THE WORK MOVES — and the
        move that broke it was a repair, adopted for good reasons, whose blast radius nobody re-measured.
    $BENCH is the root the driver already exports per run, so the fence now follows the root by construction.
    Falling back to `~/bench` when $BENCH is unset would silently reinstate the exact defect this repairs, so
    an unset $BENCH contributes NO root rather than a guessed one, and the caller records which it used.
    """
    paths = [os.path.expanduser(p) for p in DENY_READ]
    root = bench if bench is not None else os.environ.get("BENCH")
    if root:
        paths.append(os.path.realpath(os.path.expanduser(root)))
    return paths


def verus_exec_set(verus):
    """The FOUR binaries the fence admits, derived from the verus path the caller pinned.

    ⭐ MEASURED, NOT ASSUMED (and amendment 15 §8's open question (ii), 'Verus execs only z3', is FALSE):
    `verus` is a shim that resolves the pinned Rust toolchain by running `rustup`, which execs `rust_verify`,
    which execs `z3`. Each member is proven necessary by its own red arm — see sandbox_verus.sb's ladder.
    ⛔ `rustup` is the one member OUTSIDE the pinned release (it is on the user's PATH and user-writable), so
    it is pinned by sha in HASHES.txt (`rustup-sha`) like the other three. A missing rustup is a HARNESS error and
    never a silently narrower fence: the referee would fail on every task and look like a dead toolchain.
    """
    root = os.path.dirname(os.path.realpath(verus))
    rustup = shutil.which("rustup")
    if not rustup:
        raise RuntimeError("no rustup on PATH: the verus shim resolves its toolchain through it (fence needs it)")
    return [os.path.realpath(verus), os.path.realpath(rustup),
            os.path.join(root, "rust_verify"), os.path.join(root, "z3")]


def render_profile(verus, work, bench=None):
    tmpl = open(PROFILE_TEMPLATE, encoding="utf-8").read()
    ex = " ".join('(literal "%s")' % b for b in verus_exec_set(verus))
    dr = " ".join('(subpath "%s")' % p for p in deny_read_paths(bench))
    wp = '(subpath "%s")' % os.path.realpath(work)
    return (tmpl.replace("__EXEC_ALLOW__", ex)
                .replace("__DENY_READ__", "(deny file-read* %s)" % dr)
                .replace("__WRITE_PATHS__", wp))


def pgrep(args):
    p = subprocess.run(["pgrep"] + args, capture_output=True, text=True)
    return sorted(int(x) for x in p.stdout.split() if x.isdigit())

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


def referee(verus, path, cwd, rlimit, seed, timeout, extra=(), fenced=True, bench=None):
    """Run Verus on `path` under the Seatbelt profile, in its OWN process group, with a PER-INVOCATION belt.

    ⛔ The timeout is the PARENT'S, not `perl -e alarm`'s. The old shape wrapped the referee in perl so perl
    could raise SIGALRM; under the fence that would have required admitting `perl` to the exec allow-list —
    i.e. widening the fence to carry the timeout. `Popen.communicate(timeout=)` plus `killpg` does the same
    job from OUTSIDE the sandbox and keeps the admitted set at the four binaries the tool actually needs.
    ⛔ The belt pattern is THIS INVOCATION'S OWN work dir (amendment 14 repair 4): a sweep whose pattern names
    a shared file cleans up after everybody, and that one SIGKILLed three concurrent invocations' audits.
    """
    profile = render_profile(verus, cwd, bench) if fenced else None
    argv = [verus, "--crate-type=lib", "--rlimit", str(rlimit),
            "--smt-option", "smt.random_seed=%d" % seed] + list(extra) + [path]
    cmd = ([SANDBOX, "-p", profile] + argv) if fenced else argv
    t0 = time.time()
    p = subprocess.Popen(cmd, cwd=cwd, env=dict(os.environ, TMPDIR=cwd), stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE, text=True, start_new_session=True)
    pgid, timed_out = p.pid, False
    try:
        out, err = p.communicate(timeout=timeout)
    except subprocess.TimeoutExpired:
        timed_out = True
        try: os.killpg(pgid, signal.SIGKILL)
        except ProcessLookupError: pass
        out, err = p.communicate()
    killed, left = [], []
    for _ in range(25):
        left = [x for x in pgrep(["-g", str(pgid)]) + pgrep(["-f", os.path.realpath(cwd)]) if x != os.getpid()]
        if not left: break
        for pid in set(left):
            try: os.kill(pid, signal.SIGKILL); killed.append(pid)
            except ProcessLookupError: pass
        time.sleep(0.2)
    line = next((l for l in out.splitlines() if l.startswith("verification results::")), None)
    m = RESULTS.search(line) if line else None
    return dict(rc=p.returncode, results_line=line, timed_out=timed_out, fenced=fenced,
                verified=int(m.group(1)) if m else None, errors=int(m.group(2)) if m else None,
                partial=bool(line and PARTIAL.search(line)),
                rlimit_exceeded="Resource limit (rlimit) exceeded" in err,
                stderr_head=[l for l in err.splitlines() if l.startswith("error")][:5],
                belt_killed=sorted(set(killed)), belt_left=left,
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
    # ⛔ `--no-fence` exists ONLY for the fence differential (selftest_fence_verus.py), which must run the same
    # file both ways to prove the fence changes no verdict. It is never in a scored argv, and `check.json`
    # records `fenced` per run so a scored record can be read back and audited for it.
    ap.add_argument("--no-fence", action="store_true")
    a, _ = ap.parse_known_args()
    if not (a.frozen and a.agent_file and a.verus):
        sys.exit(__doc__)

    out = dict(rlimit=a.rlimit, seed=a.seed, checker=os.path.basename(__file__),
               profile_sha256=hashlib.sha256(open(PROFILE_TEMPLATE, "rb").read()).hexdigest())
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
    r = referee(a.verus, "task.rs", work, a.rlimit, a.seed, a.timeout, fenced=not a.no_fence)
    out["referee"] = r
    # ⛔ TIMEOUT is read off the PARENT'S own bookkeeping, never inferred from an rc. The old form tested
    # `rc == 142 or rc == -14`, which is `perl -e alarm`'s SIGALRM signature — a fact about the wrapper that
    # is no longer in the argv. An rc test for a wrapper you removed answers about a program you are not
    # running: it cannot fire, so every timeout would have been scored VERIFY_FAIL or COMPILE.
    out["class"] = classify(r, r["timed_out"])
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
