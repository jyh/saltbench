#!/usr/bin/env python3
"""controls_gate_verus.py — the CHECKER-CONTROLS gate for S2-Rust, read by CONTENT.

⛔ THE DEFECT IT EXISTS TO PREVENT IS NOT HYPOTHETICAL — it was measured live on 2026-09-01 on the S2-Lean
side. The driver gated every scored episode on ONE BOOLEAN (`controls_pass`), and the landed record certified
`screen.py = aa2c9376…` while the screen that would actually score the run was `cc591ca6…`. **The gate was
green against a checker that no longer existed.** ⇒ A GATE THAT READS A SUMMARY CANNOT TELL A RESULT FROM A
MEMORY OF ONE. The cure is to read the CONTENT, in the place the work will happen.

⚖️ THIS IS A PORT, NOT AN EDIT. `s2lean/controls_gate.py` is untouched: amendment 11 §13's stage-C dispatch is
still inside its 09/02 window and must run against the harness frozen at `15cfdc2`. Making that file
substrate-parametric would have been the tidier engineering and the wrong call — SPEND COMPARABILITY ONLY
WHEN A RUN NEEDS IT.

WHAT IT VERIFIES — every clause a refusal, and a refusal is a RESULT:
  1. `controls_pass` is true AND `n_ok == n` — the summary must agree with itself.
  2. EVERY file in `checker_sha256` matches the sha of the LIVE file of that name. This is the clause that
     catches a record certifying a checker that has since changed.
  3. The TOOLCHAIN pins in the record match the LIVE `HASHES.txt` — `verus-sha`, `z3-sha`, `vstd-sha`,
     `lynette-sha`, `verus-rlimit`, `verus-seed`. ⛔ NEW ON THIS SUBSTRATE AND NOT IN THE S2-LEAN GATE: on
     S2-Lean the referee is a toolchain the harness does not carry; here the referee IS a pinned binary and
     its rlimit and seed are part of the verdict. A controls record taken at a different rlimit certifies
     nothing about this run, and no sha of a .py file would notice.
  4. Every REQUIRED control name is present, `ok` is true, and its recorded `class` is in its `expect_class`.
  5. The record is inside a clock (`--max-age-h`, default off).
  6. The results block is non-empty and every row carries a class — `controls_pass: true` over ZERO rows is
     the failure mode a boolean cannot express.

usage: controls_gate_verus.py <controls.json> <harness s2rust dir> [--require n1,n2] [--max-age-h H] [--quiet]
       controls_gate_verus.py --selftest
exit 0 PASS · 3 REFUSE · 2 bad args
"""
import datetime, hashlib, json, os, sys, tempfile

PIN_KEYS = ["verus-sha", "z3-sha", "vstd-sha", "lynette-sha", "verus-rlimit", "verus-seed"]
DEFAULT_REQUIRE = ["P_clean", "P_pristine", "P_assume", "P_extbody", "P_axiomfn", "P_specfn", "P_nomarker"]


def sha_f(p):
    try:
        return hashlib.sha256(open(p, "rb").read()).hexdigest()
    except OSError:
        return None


def read_pins(hdir):
    """The toolchain pins, read from the ONE merged table.

    ⛔ `HASHES-S2RUST.txt` is RETIRED (amendment 16): its pins were merged into `HASHES.txt` at the VeruSAGE
    stage-0 regime boundary and the standalone file is gone. Keeping both would have been a checksum defined
    twice — the generator and the verifier must be the same CODE, not the same idea — and this gate is
    precisely the verifier, so it reads what `hashes.sh` now writes.
    📌 The keys read here (`verus-sha`, `z3-sha`, …) are toolchain pins and were NEVER namespaced, so the
    merge did not move them; only the S2-Rust FILE keys gained an `s2rust/` prefix, to avoid colliding with
    `base.md` and `rt.template`, which exist in both halves with different values.
    """
    p = os.path.join(hdir, "HASHES.txt")
    out = {}
    try:
        for line in open(p):
            parts = line.split()
            if len(parts) >= 2 and not line.startswith("#"):
                out[parts[0]] = parts[1]
    except OSError:
        return None
    return out


def gate(cj, hdir, require, max_age_h):
    ref, note = [], []
    try:
        d = json.load(open(cj))
    except Exception as e:
        return False, ["cannot read %s: %s" % (cj, e)], []

    # 1 — the summary must agree with itself
    if not d.get("controls_pass"):
        ref.append("controls_pass is not true (%r)" % d.get("controls_pass"))
    n, n_ok = d.get("n"), d.get("n_ok")
    if n is None or n_ok is None:
        ref.append("n / n_ok absent — the record does not say how many controls ran")
    elif n_ok != n:
        ref.append("n_ok %s != n %s" % (n_ok, n))

    # 6 — a record over zero rows is not a pass
    rows = d.get("results") or []
    if not rows:
        ref.append("the results block is EMPTY — controls_pass over zero rows is not a result")
    for r in rows:
        if not r.get("class"):
            ref.append("control %r carries no class" % r.get("name"))

    # 2 — the checker files, by content, in the place the run will happen
    cs = d.get("checker_sha256") or {}
    if not cs:
        ref.append("checker_sha256 absent — the record does not say WHICH checker produced it")
    for fn, want in sorted(cs.items()):
        got = sha_f(os.path.join(hdir, fn))
        if got is None:
            ref.append("checker file %s named in the record is MISSING from %s" % (fn, hdir))
        elif got != want:
            ref.append("checker DRIFT %s: record %s… live %s…" % (fn, want[:12], got[:12]))
        else:
            note.append("checker %s matches (%s…)" % (fn, got[:12]))

    # 3 — the toolchain pins, which on this substrate are part of the verdict
    live = read_pins(hdir)
    rec = d.get("toolchain") or {}
    if live is None:
        ref.append("HASHES.txt not found in %s — cannot verify the toolchain pins" % hdir)
    elif not rec:
        ref.append("the record carries no `toolchain` block — a controls record taken at a different "
                   "rlimit/seed/binary certifies nothing about this run")
    else:
        for k in PIN_KEYS:
            if k not in rec:
                ref.append("toolchain pin %s absent from the record" % k)
            elif k not in live:
                ref.append("toolchain pin %s absent from HASHES.txt" % k)
            elif str(rec[k]) != str(live[k]):
                ref.append("toolchain DRIFT %s: record %r live %r" % (k, rec[k], live[k]))
            else:
                note.append("pin %s matches (%s)" % (k, str(live[k])[:12]))

    # 4 — the required controls, by name, with their own expected class
    by = {r.get("name"): r for r in rows}
    for name in (require or []):
        r = by.get(name)
        if r is None:
            ref.append("required control %s is ABSENT" % name)
            continue
        if not r.get("ok"):
            ref.append("required control %s is not ok" % name)
        exp = r.get("expect_class")
        if exp and r.get("class") not in ([exp] if isinstance(exp, str) else exp):
            ref.append("control %s class %r not in expect_class %r" % (name, r.get("class"), exp))

    # 5 — the clock
    if max_age_h:
        ts = d.get("generated") or d.get("timestamp")
        if not ts:
            ref.append("no timestamp — cannot apply --max-age-h")
        else:
            try:
                t = datetime.datetime.fromisoformat(ts.replace("Z", "+00:00"))
                age = (datetime.datetime.now(datetime.timezone.utc) - t).total_seconds() / 3600
                if age > max_age_h:
                    ref.append("record is %.1f h old, limit %s h" % (age, max_age_h))
                else:
                    note.append("age %.1f h within %s h" % (age, max_age_h))
            except Exception as e:
                ref.append("unparsable timestamp %r (%s)" % (ts, e))
    return (not ref), ref, note


# ---------------------------------------------------------------- selftest
def selftest():
    """DIFFERENTIAL, red-first. The old one-line predicate must EXIT 0 on the very records this gate REFUSES —
    otherwise the gate is not demonstrably stronger than what it replaces, only longer."""
    root = tempfile.mkdtemp(prefix="cgv.")
    hdir = os.path.join(root, "h"); os.makedirs(hdir)
    open(os.path.join(hdir, "check_verus.py"), "w").write("# live checker\n")
    open(os.path.join(hdir, "screen_verus.py"), "w").write("# live screen\n")
    open(os.path.join(hdir, "HASHES.txt"), "w").write(
        "verus-sha AAA\nz3-sha BBB\nvstd-sha CCC\nlynette-sha DDD\nverus-rlimit 250\nverus-seed 0\n")
    good_cs = {f: sha_f(os.path.join(hdir, f)) for f in ("check_verus.py", "screen_verus.py")}
    good_tc = {"verus-sha": "AAA", "z3-sha": "BBB", "vstd-sha": "CCC", "lynette-sha": "DDD",
               "verus-rlimit": "250", "verus-seed": "0"}
    base = dict(controls_pass=True, n=2, n_ok=2, checker_sha256=good_cs, toolchain=good_tc,
                results=[dict(name="P_clean", ok=True, **{"class": "PASS", "expect_class": "PASS"}),
                         dict(name="P_assume", ok=True, **{"class": "SCREEN", "expect_class": "SCREEN"})])

    def write(d):
        p = os.path.join(root, "c%d.json" % len(os.listdir(root)))
        json.dump(d, open(p, "w"))
        return p

    def old_predicate(p):          # the one-line gate this replaces
        try:
            return 0 if json.load(open(p)).get("controls_pass") else 1
        except Exception:
            return 1

    cases = []
    cases.append(("a fresh, honest record", base, True))
    d = json.loads(json.dumps(base)); d["checker_sha256"]["check_verus.py"] = "0" * 64
    cases.append(("CHECKER DRIFT (the live 09/01 defect)", d, False))
    d = json.loads(json.dumps(base)); d["toolchain"]["verus-rlimit"] = "10"
    cases.append(("controls taken at a DIFFERENT RLIMIT", d, False))
    d = json.loads(json.dumps(base)); d["toolchain"]["verus-sha"] = "ZZZ"
    cases.append(("controls taken against a DIFFERENT VERUS BINARY", d, False))
    d = json.loads(json.dumps(base)); d.pop("toolchain")
    cases.append(("no toolchain block at all", d, False))
    d = json.loads(json.dumps(base)); d["results"] = []; d["n"] = d["n_ok"] = 0
    cases.append(("controls_pass TRUE over ZERO rows", d, False))
    d = json.loads(json.dumps(base)); d["n_ok"] = 1
    cases.append(("the summary disagrees with itself", d, False))
    d = json.loads(json.dumps(base)); d["results"][1]["class"] = "PASS"
    cases.append(("a control returned the WRONG class", d, False))
    d = json.loads(json.dumps(base)); d["results"] = [d["results"][0]]
    cases.append(("a required control is ABSENT", d, False))
    d = json.loads(json.dumps(base)); d.pop("checker_sha256")
    cases.append(("the record never says WHICH checker ran", d, False))

    bad = 0
    differential = 0
    print("--- %-52s %-6s %-6s %s" % ("case", "want", "gate", "old one-line predicate"))
    for name, doc, expect in cases:
        p = write(doc)
        # the require-list must name the controls THIS fixture record actually carries;
        # naming a control the base record lacks tests the fixture, not the gate.
        ok, ref, _ = gate(p, hdir, ["P_clean", "P_assume"], None)
        old = old_predicate(p)
        agree = ok == expect
        bad += not agree
        if (not expect) and old == 0:
            differential += 1
        print("%-4s %-52s %-6s %-6s exit %d%s" % ("ok" if agree else "FAIL", name, expect, ok, old,
              "   <- old gate would have PASSED this" if (not expect and old == 0) else ""))
        if not agree:
            print("        refusals: %s" % ref[:2])
    print("\ncontrols_gate_verus selftest: %d arms, %d failed" % (len(cases), bad))
    print("DIFFERENTIAL: %d of the %d refused records EXIT 0 under the one-line predicate this replaces."
          % (differential, sum(1 for _, _, e in cases if not e)))
    import shutil; shutil.rmtree(root, ignore_errors=True)
    return 1 if bad else 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(selftest())
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if len(args) != 2:
        sys.exit(__doc__)
    req = DEFAULT_REQUIRE
    age = None
    for a in sys.argv[1:]:
        if a.startswith("--require="):
            req = a.split("=", 1)[1].split(",")
        if a.startswith("--max-age-h="):
            age = float(a.split("=", 1)[1])
    ok, ref, note = gate(args[0], args[1], req, age)
    if "--quiet" not in sys.argv:
        for n in note:
            print("   ok  " + n)
    for r in ref:
        print("REFUSE: " + r)
    print("CONTROLS GATE: %s" % ("PASS" if ok else "REFUSE"))
    sys.exit(0 if ok else 3)
