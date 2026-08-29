#!/usr/bin/env python3
"""check.py — the S2-Lean checker for one stage of one problem (repair round 1, D4/D5): THE KERNEL, OUTSIDE THE
AGENT'S ELABORATION. Runs on the Studio, no model. Steps:
  1. SCREEN   token screen over the comment/string-stripped bodies (screen.py). Stage B first merges the SAME
              ARM's scored stage-A body from --a-bodies (D5) — never from the agent's stage-B file.
  2. COMPILE  the CANONICAL file (assemble.py: frozen statements + bodies, NO `#print axioms`) with
              `lean --root=<work> -o canonical.olean` in the environment `lake env` gives, under
              /usr/bin/sandbox-exec (sandbox_check.sb: no network, no fork/exec, writes only in the work dir),
              in its own process group; the timeout kills the GROUP and the group is swept afterwards.
              Stage C's `#test` lines are IN the canonical file: a failing test = rc 1 = COMPILE.
  3. PRISTINE the frozen statements with `sorry` bodies and NO agent text, compiled the same way AFTER the
              canonical (so no agent code can have touched it), optionally cached per problem+stage
              (--pristine-cache DIR; the cache is trusted only when the canonical compile could not write there).
  4. AUDIT    s2audit.lean (`lean --run`, same sandbox): kernel REPLAY of the canonical module into a fresh
              Imports.AllImports environment, Expr comparison of every frozen statement's type (and
              problem_spec's value) against the pristine olean, axiom collection over the replayed environment.
passed = screen ok ∧ compiled ∧ replay ok ∧ statements identical ∧ axioms ok.
class  = the first failing gate: SCREEN | TIMEOUT | COMPILE | KERNEL_REJECTED | STATEMENT_ALTERED | AXIOMS_FAIL
         | HARNESS (the checker itself could not run: bad args, no sandbox-exec, pristine does not compile,
         audit unreadable) | PASS.
A screened body is NOT compiled (its meta-code never runs); --no-screen (test flag, controls only) records the
violations but does not gate on them, so the structural gates can be driven on exploit bodies.

usage: check.py <A|B|C> <frozen.json> <bodies.json> <LEANPROJ> <work>/canonical.lean
         [--a-bodies A.bodies.json] [--a-olean <A canonical.olean>] [--pristine-cache DIR]
         [--timeout 600] [--audit-timeout 600] [--no-screen]                 -> check.json on stdout
exit 0 (verdict in JSON), 2 on class HARNESS.
"""
import argparse, hashlib, json, os, shutil, signal, subprocess, sys, tempfile, time, traceback
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import screen as scr
from assemble import assemble
ALLOW = {"propext", "Classical.choice", "Quot.sound"}
SANDBOX = "/usr/bin/sandbox-exec"


def sha_s(s): return hashlib.sha256(s.encode("utf-8")).hexdigest()
def sha_f(p): return hashlib.sha256(open(p, "rb").read()).hexdigest()


def lake_env(proj):
    """LEAN_PATH/PATH etc. from `lake env env` (harness-side, unsandboxed, no agent text involved) + the toolchain lean."""
    out = subprocess.check_output(["lake", "env", "env"], cwd=proj, text=True, timeout=120)
    env = dict(os.environ)
    for line in out.splitlines():
        if "=" in line:
            k, v = line.split("=", 1)
            if k.startswith("LEAN") or k == "PATH": env[k] = v
    lean = shutil.which("lean", path=env.get("PATH", ""))
    if not lean: raise RuntimeError("no lean on lake's PATH")
    return env, os.path.realpath(lean)


# credential/config trees the fenced compile must not READ (AP-2: `include_str`/#eval reading a secret into log_tail)
DENY_READ = ["~/.claude-bench", "~/.claude", "~/.ssh", "~/.aws", "~/.gnupg", "~/.config", "~/.gitconfig",
             "~/Library/Keychains", "~/Library/Application Support"]
def render_profile(template, lean_bin, write_paths):
    wp = " ".join('(subpath "%s")' % os.path.realpath(p) for p in write_paths)
    dr = " ".join('(subpath "%s")' % os.path.expanduser(p) for p in DENY_READ)
    return template.replace("__LEAN_BIN__", lean_bin).replace("__WRITE_PATHS__", wp).replace("__DENY_READ__", "(deny file-read* %s)" % dr)


def pgrep(args):
    p = subprocess.run(["pgrep"] + args, capture_output=True, text=True)
    return sorted(int(x) for x in p.stdout.split() if x.isdigit())


def run_fenced(argv, cwd, env, profile, timeout, belt_pattern):
    """argv under sandbox-exec in its OWN process group; on timeout kill the group; afterwards sweep the group
    (and, as a belt, anything whose argv carries this check's unique file path) so nothing of it remains."""
    cmd = [SANDBOX, "-p", profile] + argv
    t0 = time.time()
    p = subprocess.Popen(cmd, cwd=cwd, env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, start_new_session=True)
    pgid, timed_out = p.pid, False
    try:
        out, _ = p.communicate(timeout=timeout)
    except subprocess.TimeoutExpired:
        timed_out = True
        try: os.killpg(pgid, signal.SIGKILL)
        except ProcessLookupError: pass
        out, _ = p.communicate()
    wall = round(time.time() - t0, 1)
    killed, left = [], []
    for _ in range(25):
        left = [x for x in pgrep(["-g", str(pgid)]) + pgrep(["-f", belt_pattern]) if x != os.getpid()]
        if not left: break
        for pid in set(left):
            try: os.kill(pid, signal.SIGKILL); killed.append(pid)
            except ProcessLookupError: pass
        time.sleep(0.2)
    return ("TIMEOUT" if timed_out else p.returncode), out.decode("utf-8", "replace"), wall, sorted(set(killed)), left


def check(a, res):
    fz = json.load(open(a.frozen)); bd = json.load(open(a.bodies))
    res["problem_id"] = fz.get("problem_id")
    if a.stage not in ("A", "B", "C"): raise RuntimeError("stage must be A|B|C")
    if a.stage == "B":
        if not a.a_bodies: raise RuntimeError("stage B requires --a-bodies (the same arm's scored stage-A body, D5)")
        ab = json.load(open(a.a_bodies))
        body = (ab.get("generated_spec_body") or "").strip()
        if not body: raise RuntimeError("--a-bodies carries no generated_spec_body")
        bd["generated_spec_body"] = body
        res["a_bodies_file_sha256"] = sha_f(a.a_bodies)
        for k in ("a_episode", "a_bodies_sha256", "a_termination", "a_passed", "a_view_sha256"): res[k] = ab.get(k)
    # 1. screen
    res["screen"] = scr.screen_bodies(bd); res["screen_enforced"] = not a.no_screen
    # sources. `art` = the ARCHIVE dir (the harness writes here, unfenced); `cwork` = a FRESH isolated dir the
    # fenced compile is the ONLY thing that may write (AP-1: the fence's writable path must never be a file the
    # harness later reads/archives — $ST/bodies.json etc.). cwork lives under TMPDIR/private-tmp, outside $BENCH.
    art = os.path.dirname(os.path.abspath(a.canonical)); os.makedirs(art, exist_ok=True)
    src = assemble(a.stage, fz, bd); psrc = assemble(a.stage, fz, {}, pristine=True)
    open(a.canonical, "w").write(src)                       # the ARCHIVE copy (harness write, not the fenced process)
    res["canonical_sha256"] = sha_s(src); res["pristine_sha256"] = sha_s(psrc)
    res["tests_in_file"] = a.stage == "C" and "#test" in src
    if res["screen"] and res["screen_enforced"]:
        res["class"] = "SCREEN"; return
    if not os.path.exists(SANDBOX): raise RuntimeError("%s missing: cannot fence the compile" % SANDBOX)
    env, lean = lake_env(a.proj); res["lean_bin"] = lean
    template = open(a.profile).read()
    cwork = tempfile.mkdtemp(prefix="s2check-")           # the ONLY write-allowed path; removed in finally
    res["check_work"] = cwork
    env = dict(env); env["TMPDIR"] = cwork                # lean's own scratch stays inside the fence
    prof = render_profile(template, lean, [cwork])        # writes: cwork only (no broad /private/tmp — R1)
    ccanon = os.path.join(cwork, "canonical.lean"); open(ccanon, "w").write(src)
    # 2. compile the canonical file (agent text) — fenced, in cwork
    olean = os.path.join(cwork, "canonical.olean")
    rc, out, wall, killed, left = run_fenced([lean, "--root=" + cwork, "-o", olean, ccanon], cwork, env, prof, a.timeout, ccanon)
    res["rc"], res["compile_wall_s"], res["log_tail"] = rc, wall, out[-3000:]
    res["orphans_killed"], res["orphans_left"] = killed, left
    res["sorry_lines"] = [l for l in out.splitlines() if "declaration uses 'sorry'" in l]
    open(os.path.join(art, "compile.log"), "w").write(out)
    res["compiled"] = (rc == 0 and os.path.exists(olean))
    if rc == "TIMEOUT": res["class"] = "TIMEOUT"; return
    if not res["compiled"]: res["class"] = "COMPILE"; return
    res["canonical_olean_sha256"] = sha_f(olean)
    shutil.copy(olean, os.path.join(art, "canonical.olean"))   # archive the olean (cwork is deleted); stage B reads it as --a-olean (AP-1 fix must not break the a_olean chain)
    # 3. pristine (no agent text) — compiled in cwork/pristine; cached olean lives OUTSIDE cwork (never fence-writable)
    pdir = os.path.join(cwork, "pristine"); os.makedirs(pdir, exist_ok=True)
    pfile, polean = os.path.join(pdir, "canonical.lean"), os.path.join(pdir, "canonical.olean")
    cache_olean = None
    if a.pristine_cache:
        cache_olean = os.path.join(a.pristine_cache, "problem_%s" % fz.get("problem_id"), a.stage, res["pristine_sha256"][:16] + ".olean")
    res["pristine_cache_olean"] = cache_olean
    cached = bool(cache_olean and os.path.exists(cache_olean))
    res["pristine_cached"] = cached
    if cached:
        shutil.copy(cache_olean, polean)                 # harness copy into cwork; the fenced audit reads it there
    else:
        open(pfile, "w").write(psrc)
        prc, pout, pwall, _, _ = run_fenced([lean, "--root=" + pdir, "-o", polean, pfile], pdir, env, render_profile(template, lean, [cwork]), a.timeout, pfile)
        res["pristine_rc"], res["pristine_wall_s"] = prc, pwall
        open(os.path.join(art, "pristine.compile.log"), "w").write(pout)
        if prc != 0 or not os.path.exists(polean):
            res["pristine_log_tail"] = pout[-2000:]
            raise RuntimeError("pristine file does not compile (rc=%s): the view is dead, not the agent" % prc)
        if cache_olean:                                  # populate the cache (harness copy, outside the fence)
            os.makedirs(os.path.dirname(cache_olean), exist_ok=True); shutil.copy(polean, cache_olean)
    res["pristine_olean_sha256"] = sha_f(polean)
    # 4. audit — replay + statements + axioms, outside the agent's elaboration. The stage-A olean is copied INTO
    #    cwork so the audit reads nothing under $BENCH/state (the profile denies that read).
    aol = "-"
    if a.a_olean and os.path.exists(a.a_olean):
        aol = os.path.join(cwork, "a_canonical.olean"); shutil.copy(a.a_olean, aol)
    elif a.a_olean:
        res["a_olean_missing"] = a.a_olean
    arc, aout, awall, _, _ = run_fenced([lean, "--run", a.audit, olean, polean, a.stage, aol], cwork, env, render_profile(template, lean, [cwork]), a.audit_timeout, a.audit)
    # 4a. a transient SIGKILL of the audit (OOM/contention, rc negative and not a timeout) is retried ONCE (FN-5)
    if arc not in (0,) and arc != "TIMEOUT" and isinstance(arc, int) and arc < 0:
        res["audit_retry"] = arc
        arc, aout, awall, _, _ = run_fenced([lean, "--run", a.audit, olean, polean, a.stage, aol], cwork, env, render_profile(template, lean, [cwork]), a.audit_timeout, a.audit)
    res["audit_rc"], res["audit_wall_s"] = arc, awall
    open(os.path.join(art, "audit.log"), "w").write(aout)
    aj = None
    for line in reversed(aout.splitlines()):
        line = line.strip()
        if line.startswith("{"):
            try: aj = json.loads(line); break
            except ValueError: pass
    if aj is None or "error" in aj:
        res["audit_log_tail"] = aout[-2000:]
        raise RuntimeError("audit did not run: %s" % ((aj or {}).get("error") or "no JSON on stdout (rc=%s)" % arc))
    open(os.path.join(art, "audit.json"), "w").write(json.dumps(aj, indent=1))
    res["replay_ok"], res["replay_error"] = bool(aj.get("replay_ok")), aj.get("replay_error") or ""
    res["statements"], res["statements_identical"] = aj.get("statements"), bool(aj.get("statements_identical"))
    res["statement_diffs"], res["axioms"] = aj.get("statement_diffs") or [], aj.get("axioms") or {}
    res["axioms_ok"] = bool(aj.get("axioms_ok")) and bool(res["axioms"]) and all(set(v) <= ALLOW for v in res["axioms"].values())
    res["a_body_value_identical"] = aj.get("a_body_value_identical")
    res["module_constants"] = aj.get("constants")
    if not res["replay_ok"]: res["class"] = "KERNEL_REJECTED"
    elif not res["statements_identical"]: res["class"] = "STATEMENT_ALTERED"
    elif not res["axioms_ok"]: res["class"] = "AXIOMS_FAIL"
    elif res.get("a_body_value_identical") is False: res["class"] = "PROVENANCE"   # AP-4: stage-B generated_spec != the scored stage-A body
    else: res["class"] = "PASS"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("stage"); ap.add_argument("frozen"); ap.add_argument("bodies"); ap.add_argument("proj"); ap.add_argument("canonical")
    ap.add_argument("--a-bodies"); ap.add_argument("--a-olean"); ap.add_argument("--pristine-cache")
    ap.add_argument("--timeout", type=int, default=600); ap.add_argument("--audit-timeout", type=int, default=600)
    ap.add_argument("--no-screen", action="store_true")
    ap.add_argument("--audit", default=os.path.join(HERE, "s2audit.lean")); ap.add_argument("--profile", default=os.path.join(HERE, "sandbox_check.sb"))
    a = ap.parse_args()
    res = {"stage": a.stage, "problem_id": None, "screen": [], "screen_enforced": True, "compiled": False, "rc": None,
           "compile_wall_s": None, "log_tail": "", "replay_ok": None, "replay_error": None, "statements_identical": None,
           "statement_diffs": [], "axioms": {}, "axioms_ok": None, "passed": False, "class": "HARNESS",
           "tests_in_file": False, "a_body_value_identical": None, "audit_wall_s": None, "harness_error": None,
           "checker_sha256": {os.path.basename(p): sha_f(p) for p in (__file__, a.audit, a.profile, os.path.join(HERE, "screen.py"), os.path.join(HERE, "assemble.py")) if os.path.exists(p)}}
    try:
        check(a, res)
    except Exception as e:
        res["class"] = "HARNESS"; res["harness_error"] = "%s\n%s" % (repr(e), traceback.format_exc()[-1500:])
    finally:
        cw = res.get("check_work")
        if cw and os.path.isdir(cw): shutil.rmtree(cw, ignore_errors=True)
    res["passed"] = (res["class"] == "PASS")
    print(json.dumps(res, indent=1))
    sys.exit(2 if res["class"] == "HARNESS" else 0)


if __name__ == "__main__":
    main()
