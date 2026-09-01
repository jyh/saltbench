#!/usr/bin/env python3
"""controls_gate.py — the CHECKER-CONTROLS gate, read by CONTENT (amendment 12, 2026-09-01, desk row AS).

⛔ THE DEFECT IT REPLACES, MEASURED LIVE ON 2026-09-01 AND NOT HYPOTHETICAL. `run_s2_stage0.sh` gated on

    python3 -c "import json,sys;sys.exit(0 if json.load(open('$cj')).get('controls_pass') else 1)"

— one summary field, no clock, no comparison to the checker that is about to run, and no idea WHICH controls
produced it. On 2026-09-01 the landed `s2-controls.json` (dated 2026-08-29T10:33:38Z, 30/30) certified
`screen.py = aa2c9376…` while the screen that would actually score the run was `cc591ca6…` — amendment 9's
§9.5 widening, landed 08/31. **The gate was green against a checker that no longer existed.** Amendment 9
proved that particular widening a no-op over all 201 landed episodes, so nothing was harmed; the gate could
not have known that, and that is the whole point.

⇒ THIRD INSTANCE OF ONE SHAPE at this seat in three days: `ship BC` gated on a DONE line in a log; `c_dead`
gated on elaboration; this gated on a boolean. **A GATE THAT READS A SUMMARY CANNOT TELL A RESULT FROM A
MEMORY OF ONE.** The cure each time is the same: read the CONTENT, in the place the work will happen.

WHAT IT VERIFIES (every clause a refusal, and a refusal is a result):
  1. `controls_pass` is true AND `n_ok == n` — the summary must agree with itself.
  2. EVERY file in `checker_sha256` matches the sha of the LIVE file of that name in the harness dir. This is
     the clause that fires today.
  3. Every REQUIRED control name (`--require`, or `--stage C` for the C family) is present, `ok` is true, and
     its recorded `class` is in its own `expect_class`.
  4. The record is inside a clock (`--max-age-h`, default off — a stage run passes its own).
  5. The results block is non-empty and every row carries a class — an empty or half-written record is not a
     pass, and `controls_pass: true` over zero rows is the failure mode a boolean cannot express.

usage: controls_gate.py <s2-controls.json> <harness s2lean dir> [--stage A|B|C] [--require n1,n2]
                        [--max-age-h H] [--quiet]
       controls_gate.py --selftest
exit 0 PASS · 3 REFUSE · 2 bad args
"""
import datetime, hashlib, json, os, subprocess, sys, tempfile

C_FAMILY = ["C_pos", "C_neg", "C_ax", "C_decide", "C_badimpl", "C_notation", "C_notation_noscreen"]
A_FAMILY = ["A_pos", "A_neg"]
B_FAMILY = ["B_pos", "B_neg", "B_ax"]


def sha_f(p):
    try: return hashlib.sha256(open(p, "rb").read()).hexdigest()
    except OSError: return None


def gate(cj, hdir, require, max_age_h):
    """-> (ok, [refusals], [notes])"""
    ref, note = [], []
    try: d = json.load(open(cj))
    except Exception as e: return False, ["cannot read %s: %s" % (cj, e)], []

    if not d.get("controls_pass"): ref.append("controls_pass is not true (%r)" % d.get("controls_pass"))
    n, n_ok = d.get("n"), d.get("n_ok")
    if n is None or n_ok is None: ref.append("n / n_ok absent — the record does not say how many controls ran")
    elif n_ok != n: ref.append("n_ok %s != n %s" % (n_ok, n))

    res = d.get("results") or {}
    if not res: ref.append("results block is EMPTY — controls_pass over zero rows is not a pass")
    else:
        classless = sorted(k for k, v in res.items() if not isinstance(v, dict) or v.get("class") is None)
        if classless: ref.append("rows with no recorded class: %s" % classless[:8])

    cs = d.get("checker_sha256") or {}
    if not cs: ref.append("checker_sha256 absent — the record cannot be tied to a checker")
    for fname, want in sorted(cs.items()):
        got = sha_f(os.path.join(hdir, fname))
        if got is None: ref.append("checker file %s is not in %s" % (fname, hdir))
        elif got != want:
            ref.append("CHECKER DRIFT %s: controls certified %s… but the live file is %s…"
                       % (fname, want[:16], got[:16]))
        else: note.append("%s %s… matches" % (fname, want[:12]))

    for name in require:
        row = res.get(name)
        if row is None: ref.append("required control %s is ABSENT from the record" % name)
        elif not row.get("ok"): ref.append("required control %s did not pass (%s)" % (name, row.get("class")))
        elif row.get("expect_class") and row.get("class") not in row["expect_class"]:
            ref.append("required control %s: class %s not in %s" % (name, row.get("class"), row["expect_class"]))
        else: note.append("%s %s" % (name, row.get("class")))

    if max_age_h is not None:
        ds = d.get("date")
        if not ds: ref.append("no date in the record but --max-age-h was asked for")
        else:
            try:
                t = datetime.datetime.strptime(ds, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=datetime.timezone.utc)
                age = (datetime.datetime.now(datetime.timezone.utc) - t).total_seconds() / 3600.0
                if age > max_age_h: ref.append("record is %.1f h old, limit %.1f h" % (age, max_age_h))
                else: note.append("age %.1f h" % age)
            except ValueError: ref.append("date %r is not YYYY-MM-DDTHH:MM:SSZ" % ds)

    return (not ref), ref, note


def main(argv):
    if argv[:1] == ["--selftest"]: return selftest()
    if len(argv) < 2 or argv[0].startswith("-"): print(__doc__); return 2
    cj, hdir = argv[0], argv[1]
    require, max_age_h, quiet = [], None, False
    rest = argv[2:]
    while rest:
        a = rest.pop(0)
        if a == "--stage":
            st = rest.pop(0)
            if st == "A": require += A_FAMILY
            elif st == "B": require += B_FAMILY
            elif st == "C": require += C_FAMILY
            else: print("REFUSE: --stage must be A, B or C"); return 2
        elif a == "--require": require += [x for x in rest.pop(0).split(",") if x]
        elif a == "--max-age-h": 
            try: max_age_h = float(rest.pop(0))
            except ValueError: print("REFUSE: --max-age-h must be a number"); return 2
        elif a == "--quiet": quiet = True
        else: print("REFUSE: unknown arg %r" % a); return 2
    ok, ref, note = gate(cj, hdir, require, max_age_h)
    if not quiet:
        for x in note: print("  ok   %s" % x)
    for x in ref: print("REFUSE: %s" % x)
    print("CONTROLS GATE %s (%s, %d checked, %d required)" % ("PASS" if ok else "REFUSE", cj, len(note), len(require)))
    return 0 if ok else 3


# ───────────────────────────── selftest: every arm a subprocess on the real argv ─────────────────────────────
def selftest():
    ME = os.path.abspath(__file__); arms = 0; fails = []

    def run(args): return subprocess.run([sys.executable, ME] + args, capture_output=True, text=True)

    def arm(name, cond, detail=""):
        nonlocal arms; arms += 1
        print("  %-6s %s%s" % ("PASS" if cond else "FAIL", name, "" if cond else "   << " + str(detail)[:300]))
        if not cond: fails.append(name)

    with tempfile.TemporaryDirectory() as d:
        hdir = os.path.join(d, "h"); os.makedirs(hdir)
        open(os.path.join(hdir, "check.py"), "w").write("CHECKER v1\n")
        open(os.path.join(hdir, "screen.py"), "w").write("SCREEN v1\n")
        s_check = sha_f(os.path.join(hdir, "check.py")); s_screen = sha_f(os.path.join(hdir, "screen.py"))

        def rows(names, ok=True):
            return {n: {"class": "PASS", "ok": ok, "expect_class": ["PASS"], "fails": []} for n in names}

        def write(name, obj):
            p = os.path.join(d, name); json.dump(obj, open(p, "w"), indent=1); return p

        good = {"controls_pass": True, "n": 7, "n_ok": 7, "date": "2026-09-01T00:00:00Z",
                "checker_sha256": {"check.py": s_check, "screen.py": s_screen}, "results": rows(C_FAMILY)}

        # 1 GREEN — everything agrees
        r = run([write("good.json", good), hdir, "--stage", "C"])
        arm("green/all-agree", r.returncode == 0, r.stdout[-300:])

        # 2 ⭐ THE ARM THAT IS THE WHOLE POINT: the checker drifted under a green summary. This is the live
        #   2026-09-01 state (screen.py aa2c9376… certified, cc591ca6… on disk) and the OLD gate passed it.
        open(os.path.join(hdir, "screen.py"), "w").write("SCREEN v2 — the amendment-9 widening\n")
        r = run([write("drift.json", good), hdir, "--stage", "C"])
        arm("red/CHECKER DRIFT caught", r.returncode == 3 and "CHECKER DRIFT screen.py" in r.stdout, r.stdout[-300:])
        arm("red/drift names both shas", s_screen[:16] in r.stdout and sha_f(os.path.join(hdir, "screen.py"))[:16] in r.stdout, r.stdout[-300:])
        # …and the OLD gate's predicate, run verbatim on the SAME file, says PASS — both arms, one fixture.
        old = subprocess.run([sys.executable, "-c",
                              "import json,sys;sys.exit(0 if json.load(open(%r)).get('controls_pass') else 1)"
                              % os.path.join(d, "drift.json")])
        arm("red/the OLD predicate passes the same file", old.returncode == 0, "old rc=%s" % old.returncode)
        open(os.path.join(hdir, "screen.py"), "w").write("SCREEN v1\n")   # restore

        # 3 REFUSE: controls_pass false
        r = run([write("cp.json", dict(good, controls_pass=False)), hdir, "--stage", "C"])
        arm("red/controls_pass false", r.returncode == 3, r.stdout[-200:])

        # 4 REFUSE: n_ok != n — a summary that disagrees with itself
        r = run([write("nok.json", dict(good, n_ok=6)), hdir, "--stage", "C"])
        arm("red/n_ok != n", r.returncode == 3 and "n_ok 6 != n 7" in r.stdout, r.stdout[-200:])

        # 5 REFUSE: an empty results block under a true boolean — what a boolean cannot express
        r = run([write("empty.json", dict(good, results={})), hdir, "--stage", "C"])
        arm("red/empty results under a green boolean", r.returncode == 3 and "EMPTY" in r.stdout, r.stdout[-200:])

        # 6 REFUSE: a required control missing — the 30-row record against a 31-row requirement, i.e. exactly
        #   what a stage-C run gets if it inherits a controls file written before C_decide existed.
        r = run([write("noC.json", dict(good, results=rows([x for x in C_FAMILY if x != "C_decide"]))), hdir, "--stage", "C"])
        arm("red/required control absent", r.returncode == 3 and "C_decide is ABSENT" in r.stdout, r.stdout[-250:])

        # 7 REFUSE: a required control present but not ok
        r = run([write("badC.json", dict(good, results=rows(C_FAMILY, ok=False))), hdir, "--stage", "C"])
        arm("red/required control not ok", r.returncode == 3, r.stdout[-200:])

        # 8 REFUSE: a row whose class contradicts its own expectation
        bad = json.loads(json.dumps(good)); bad["results"]["C_pos"]["class"] = "AXIOMS_FAIL"
        r = run([write("cls.json", bad), hdir, "--stage", "C"])
        arm("red/class not in expect_class", r.returncode == 3 and "not in" in r.stdout, r.stdout[-250:])

        # 9 REFUSE: checker_sha256 names a file that is not in the harness dir
        r = run([write("miss.json", dict(good, checker_sha256=dict(good["checker_sha256"], gone_py="0" * 64))), hdir, "--stage", "C"])
        arm("red/checker file absent", r.returncode == 3 and "gone_py is not in" in r.stdout, r.stdout[-250:])

        # 10 REFUSE: no checker_sha256 at all
        g2 = {k: v for k, v in good.items() if k != "checker_sha256"}
        r = run([write("nocs.json", g2), hdir, "--stage", "C"])
        arm("red/no checker_sha256", r.returncode == 3 and "checker_sha256 absent" in r.stdout, r.stdout[-200:])

        # 11 the CLOCK, both ways
        r = run([write("old.json", dict(good, date="2020-01-01T00:00:00Z")), hdir, "--stage", "C", "--max-age-h", "24"])
        arm("red/too old", r.returncode == 3 and "old, limit" in r.stdout, r.stdout[-200:])
        r = run([write("old2.json", dict(good, date="2020-01-01T00:00:00Z")), hdir, "--stage", "C"])
        arm("green/no clock asked, no clock applied", r.returncode == 0, r.stdout[-200:])

        # 12 bad args
        arm("red/bad stage", run([os.path.join(d, "good.json"), hdir, "--stage", "Z"]).returncode == 2)
        arm("red/unknown arg", run([os.path.join(d, "good.json"), hdir, "--nope"]).returncode == 2)
        arm("red/no args", run([]).returncode == 2)

    print("controls_gate selftest: %d arms, %d failed" % (arms, len(fails)))
    for f in fails: print("  FAIL " + f)
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
