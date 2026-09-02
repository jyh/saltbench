#!/usr/bin/env python3
r"""c_oracle_preflight.py — the stage-C ORACLE pre-flight (amendment 11).

WHY IT EXISTS. `view_status.json`'s `c_dead` is an ELABORATION check: it measures whether the stage-C task
can be STATED, never whether it can be DONE. On 2026-09-01 the Step-0 triage proved `problem_18`'s stage C
UNSATISFIABLE — its `problem_spec` forces `implementation "aaaa" "aa" = 0` while the frozen `#test` line
demands 3 — and `c_dead` had it marked `C: ok`. An episode on such a cell cannot pass by any route and would
be scored as the ARM's failure. This tool is the gate `c_dead` is not.

WHAT IT CHECKS, and it never claims more than it proved:

  CHECK 1 — SLICE-EQ (mechanical, reaches every problem). Elaborate the frozen `problem_spec` and inspect the
    ELABORATED term for a `String.Slice` coercion sitting inside an equality. This is `problem_18`'s exact
    root cause and it is invisible in the source text: `(string.drop i).take n = substring` typechecks only
    because Lean silently inserts `String.toSlice`, and `Slice` equality is STRUCTURAL -- it forces the base
    strings equal, so the occurrence test is FALSE at a genuine occurrence. THE SOURCE READS AS CONTENT
    EQUALITY AND MEANS SOMETHING ELSE. Verdict SLICE_EQ_RISK.

  CHECK 2 — GT-TEST (reaches only problems whose CLEVER reference `implementation` is not `sorry`). Run the
    frozen `#test` lines against the reference implementation. If the benchmark's own implementation fails
    the benchmark's own tests, the cell is incoherent before any arm touches it. Verdict GT_TEST_FAIL.

  It does NOT prove satisfiability, and it does not pretend to. A GT-based satisfiability check was the first
  design and it is IMPOSSIBLE on this substrate: measured at the artifact, only 4 of 161 CLEVER problems carry
  a complete reference `correctness` proof, and of the commission's 13 exactly ONE does (problem_0). A problem
  this tool does not refute is UNREFUTED, never "clean" -- and the report says so in that word.

usage: c_oracle_preflight.py <ids...>            ids as bare ints or problem_<n>
       c_oracle_preflight.py --selftest          red-first: drives the real argv as a subprocess
env:   VIEWS      frozen views dir      (default: <this dir>/views)
       LEANPROJ   lean project to run `lake env lean` in   (default: ~/lean-shared/clever)
       CLEVER_GT  CLEVER checkout for CHECK 2 (default: ~/clever-gt); absent => CHECK 2 reports UNREACHED
       SSH_HOST   run lean over ssh on this host instead of locally (e.g. the Studio host)
exit:  0 = no problem refuted · 3 = at least one problem REFUTED · 2 = harness error. A REFUSAL IS A RESULT.
"""
import json, os, re, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
VIEWS = os.environ.get("VIEWS") or os.path.join(HERE, "views")
LEANPROJ = os.environ.get("LEANPROJ") or "~/lean-shared/clever"
CLEVER_GT = os.environ.get("CLEVER_GT") or "~/clever-gt"
SSH_HOST = os.environ.get("SSH_HOST") or ""


def die(msg, code=2):
    print("⛔ %s" % msg, file=sys.stderr)
    sys.exit(code)


def norm(tok):
    t = str(tok).strip()
    if t.startswith("problem_"):
        t = t[len("problem_"):]
    if not re.fullmatch(r"[0-9]+", t):
        die("not a problem id: %r" % tok)
    return "problem_%d" % int(t)


def run_lean(src, tag):
    """Elaborate `src` in the pinned project. Returns (rc, stdout+stderr)."""
    with tempfile.NamedTemporaryFile("w", suffix="_%s.lean" % tag, delete=False) as f:
        f.write(src)
        local = f.name
    try:
        if SSH_HOST:
            remote = "/tmp/%s" % os.path.basename(local)
            r = subprocess.run(["scp", "-q", local, "%s:%s" % (SSH_HOST, remote)],
                               capture_output=True, text=True)
            if r.returncode != 0:
                return 2, "scp failed: %s" % r.stderr
            cmd = ["ssh", SSH_HOST, "bash -lc 'cd %s && lake env lean %s 2>&1; echo __RC=$?'"
                   % (LEANPROJ, remote)]
        else:
            cmd = ["bash", "-lc", "cd %s && lake env lean %s 2>&1; echo __RC=$?"
                   % (os.path.expanduser(LEANPROJ), local)]
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=1800)
        out = r.stdout + r.stderr
        m = re.search(r"__RC=(\d+)\s*$", out)
        rc = int(m.group(1)) if m else 2
        return rc, re.sub(r"__RC=\d+\s*$", "", out)
    finally:
        try:
            os.unlink(local)
        except OSError:
            pass


# ---------- CHECK 1: the elaborated spec, and coercions hiding inside an equality
def check_slice_eq(ids):
    """Elaborate every frozen problem_spec in its own namespace and #print it."""
    parts = ["import Imports.AllImports", "set_option pp.coercions true", ""]
    for p in ids:
        fz = json.load(open(os.path.join(VIEWS, p, "frozen.json")))
        parts += ["namespace %s" % p, fz["problem_spec"], "end %s" % p, ""]
    for p in ids:
        parts.append("#print %s.problem_spec" % p)
    rc, out = run_lean("\n".join(parts), "sliceeq")
    if rc not in (0, 1):
        return None, out
    # split the #print blocks: each begins `def <ns>.problem_spec :`
    blocks, cur, name = {}, [], None
    for line in out.splitlines():
        m = re.match(r"def (problem_\d+)\.problem_spec\s*:", line)
        if m:
            if name:
                blocks[name] = "\n".join(cur)
            name, cur = m.group(1), [line]
        elif name:
            cur.append(line)
    if name:
        blocks[name] = "\n".join(cur)
    res = {}
    for p in ids:
        body = blocks.get(p)
        if body is None:
            res[p] = dict(verdict="UNREACHED", detail="no #print block (elaboration failed?)", term=None)
            continue
        hits = [l.strip() for l in body.splitlines()
                if re.search(r"\.toSlice\b", l) or re.search(r"String\.Slice", l)]
        res[p] = dict(verdict="SLICE_EQ_RISK" if hits else "no-slice-coercion",
                      detail=hits, term=body)
    return res, out


# ---------- CHECK 2: the reference implementation against the frozen #test lines
GT_SEC = r"-- start_def %s\n(.*?)-- end_def %s"


def gt_section(txt, name):
    m = re.search(GT_SEC % (name, name), txt, re.S)
    return m.group(1) if m else None


def strip_comments(s):
    if s is None:
        return None
    s = re.sub(r"/-.*?-/", "", s, flags=re.S)
    return re.sub(r"--[^\n]*", "", s)


def check_gt_tests(ids):
    gtdir = os.path.expanduser(CLEVER_GT)
    if SSH_HOST:
        r = subprocess.run(["ssh", SSH_HOST, "bash -lc 'ls %s/src/lean4/human_eval >/dev/null 2>&1; echo $?'"
                            % CLEVER_GT], capture_output=True, text=True)
        if r.stdout.strip() != "0":
            return {p: dict(verdict="UNREACHED", detail="CLEVER_GT not present on %s" % SSH_HOST) for p in ids}, ""
    elif not os.path.isdir(os.path.join(gtdir, "src/lean4/human_eval")):
        return {p: dict(verdict="UNREACHED", detail="CLEVER_GT not present at %s" % gtdir) for p in ids}, ""

    res, runnable, parts = {}, [], ["import Imports.AllImports", ""]
    for p in ids:
        if SSH_HOST:
            r = subprocess.run(["ssh", SSH_HOST, "bash -lc 'cat %s/src/lean4/human_eval/%s.lean'"
                                % (CLEVER_GT, p)], capture_output=True, text=True)
            txt = r.stdout if r.returncode == 0 else ""
        else:
            fp = os.path.join(gtdir, "src/lean4/human_eval", "%s.lean" % p)
            txt = open(fp).read() if os.path.exists(fp) else ""
        impl = strip_comments(gt_section(txt, "implementation"))
        sig = gt_section(txt, "implementation_signature")
        if not txt:
            res[p] = dict(verdict="UNREACHED", detail="no GT file")
            continue
        if impl is None or not impl.strip() or re.search(r"\bsorry\b", impl):
            res[p] = dict(verdict="UNREACHED", detail="GT implementation is sorry/absent")
            continue
        fz = json.load(open(os.path.join(VIEWS, p, "frozen.json")))
        tests = [l for l in fz["test_cases"].splitlines() if l.strip().startswith("#test")]
        if not tests:
            res[p] = dict(verdict="UNREACHED", detail="no #test lines")
            continue
        ns = p
        parts += ["namespace %s" % ns, sig.strip(), impl.strip()]
        parts += [t.replace("implementation", "implementation") for t in tests]
        parts += ["end %s" % ns, ""]
        runnable.append(p)
    if not runnable:
        return res, ""
    rc, out = run_lean("\n".join(parts), "gttest")
    # a failing #test is an ERROR; attribute errors to the namespace they fall in
    failed = set()
    for line in out.splitlines():
        m = re.search(r"error", line)
        if m:
            failed.add(line)
    # re-run per problem so attribution is exact rather than inferred
    for p in runnable:
        one = ["import Imports.AllImports", ""]
        if SSH_HOST:
            r = subprocess.run(["ssh", SSH_HOST, "bash -lc 'cat %s/src/lean4/human_eval/%s.lean'"
                                % (CLEVER_GT, p)], capture_output=True, text=True)
            txt = r.stdout
        else:
            txt = open(os.path.join(gtdir, "src/lean4/human_eval", "%s.lean" % p)).read()
        one += [strip_comments(gt_section(txt, "implementation_signature")).strip(),
                strip_comments(gt_section(txt, "implementation")).strip()]
        fz = json.load(open(os.path.join(VIEWS, p, "frozen.json")))
        one += [l for l in fz["test_cases"].splitlines() if l.strip().startswith("#test")]
        rc1, out1 = run_lean("\n".join(one), "gttest_%s" % p)
        res[p] = dict(verdict="GT_TEST_FAIL" if rc1 != 0 else "gt-passes-its-tests",
                      detail=[l for l in out1.splitlines() if l.strip()][:12], rc=rc1)
    return res, out


def report(ids):
    slic, raw1 = check_slice_eq(ids)
    if slic is None:
        die("CHECK 1 could not elaborate:\n%s" % raw1[:2000])
    gt, _ = check_gt_tests(ids)
    refused, rows = [], []
    for p in ids:
        s, g = slic[p], gt.get(p, dict(verdict="UNREACHED", detail=""))
        bad = (s["verdict"] == "SLICE_EQ_RISK") or (g["verdict"] == "GT_TEST_FAIL")
        v = "REFUSED" if bad else ("UNREFUTED" if s["verdict"] != "UNREACHED" else "UNREACHED")
        if bad:
            refused.append(p)
        rows.append((p, v, s["verdict"], g["verdict"]))
    w = max(len(p) for p in ids)
    print("%-*s  %-10s  %-22s  %s" % (w, "problem", "VERDICT", "CHECK1 slice-eq", "CHECK2 gt-vs-#test"))
    for p, v, a, b in rows:
        print("%-*s  %-10s  %-22s  %s" % (w, p, v, a, b))
    print()
    for p in ids:
        if slic[p]["verdict"] == "SLICE_EQ_RISK":
            print("⛔ %s CHECK 1: a String.Slice coercion sits inside an equality in the ELABORATED spec:" % p)
            for h in slic[p]["detail"]:
                print("     %s" % h)
        if gt.get(p, {}).get("verdict") == "GT_TEST_FAIL":
            print("⛔ %s CHECK 2: the reference implementation FAILS the frozen #test lines:" % p)
            for h in gt[p]["detail"]:
                print("     %s" % h)
    print()
    print("REFUSED: %s" % (", ".join(refused) if refused else "(none)"))
    print("⚠ UNREFUTED IS NOT CLEAN. This tool refutes; it does not certify. A GT-based satisfiability check")
    print("  is impossible here: only 4 of 161 CLEVER problems carry a complete reference correctness proof.")
    return 3 if refused else 0


def selftest():
    """RED-FIRST, and the arms are real subprocesses on the real argv."""
    py, me = sys.executable, os.path.abspath(__file__)
    arms, fails = [], 0

    def arm(name, argv, want_rc=None, want_in=(), want_not_in=()):
        nonlocal fails
        r = subprocess.run([py, me] + argv, capture_output=True, text=True)
        out = r.stdout + r.stderr
        ok = True
        if want_rc is not None and r.returncode != want_rc:
            ok = False
        for s in want_in:
            if s not in out:
                ok = False
        for s in want_not_in:
            if s in out:
                ok = False
        arms.append((name, ok, r.returncode))
        if not ok:
            fails += 1
            print("  ⛔ ARM FAILED %s (rc=%d)\n%s" % (name, r.returncode, out[:1500]))
        return out

    # --- REFUSE arms (argument handling): a bad id must be refused, never coerced
    arm("refuse/empty", [], want_rc=2, want_in=("usage",))
    arm("refuse/nonnumeric", ["problem_x"], want_rc=2, want_in=("not a problem id",))
    arm("refuse/negative", ["-4"], want_rc=2, want_in=("not a problem id",))
    arm("refuse/float", ["18.5"], want_rc=2, want_in=("not a problem id",))
    arm("accept/normalises", ["problem_18", "18"], want_rc=3)  # same id twice, still refuses

    # --- THE RED CONTROL: the tool MUST refuse problem_18 (Step 0 proved it unsatisfiable) ...
    arm("red/18-is-refused", ["18"], want_rc=3,
        want_in=("REFUSED: problem_18", "SLICE_EQ_RISK", "toSlice"))
    # --- ... AND THE GREEN CONTROL, without which the red arm proves only that it refuses everything.
    arm("green/0-is-not-refused", ["0"], want_rc=0,
        want_in=("UNREFUTED",), want_not_in=("REFUSED: problem_0",))
    # --- a mixed call must refuse the one and clear the other IN THE SAME RUN
    out = arm("mixed/18-and-0", ["18", "0"], want_rc=3, want_in=("REFUSED: problem_18",))
    for line in out.splitlines():
        if line.startswith("problem_0 "):
            if "REFUSED" in line:
                print("  ⛔ ARM FAILED mixed/0-row-must-not-be-refused")
                fails += 1
    # --- the honesty arm: the report must never call an unrefuted problem "clean"
    arm("honesty/no-clean-claim", ["0"], want_rc=0, want_in=("UNREFUTED IS NOT CLEAN",))

    print("\nSELFTEST: %d arms, %d failed" % (len(arms), fails))
    for n, ok, rc in arms:
        print("  %-28s %-5s rc=%d" % (n, "PASS" if ok else "FAIL", rc))
    return 1 if fails else 0


def main():
    argv = sys.argv[1:]
    if not argv:
        die(__doc__.split("usage:")[1].split("exit:")[0].strip().join(("usage: ", "")))
    if argv[0] == "--selftest":
        sys.exit(selftest())
    ids, seen = [], set()
    for a in argv:
        p = norm(a)
        if p not in seen:
            seen.add(p)
            ids.append(p)
    for p in ids:
        if not os.path.exists(os.path.join(VIEWS, p, "frozen.json")):
            die("no frozen view for %s under %s" % (p, VIEWS))
    sys.exit(report(ids))


if __name__ == "__main__":
    main()
