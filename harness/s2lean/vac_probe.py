#!/usr/bin/env python3
"""vac_probe.py — AMENDMENT 11 §8, the PERMISSIVE-ORACLE DIAGNOSTIC. Zero model tokens.

WHAT IT ANSWERS, and what it deliberately does not. Four of the twelve registered stage-C reference specs
are VACUOUS on a region their own `#test` lines never visit, so a certified implementation may be WRONG
there and still be scored PASS by a checker doing exactly its job. This tool evaluates each PASS'd
implementation at a probe point INSIDE its vacuous region and reports `f_vac`.

  ⛔ IT DOES NOT CHANGE `P0`, THE RECORD, OR THE GATE. §8: reported BESIDE the number, never against it.
  The probe points are FIXED in amendment 11 §8, frozen 2026-09-01 BEFORE any stage-C call, and are
  transcribed here verbatim. Nothing here is chosen after seeing a result.

WHY IT PROBES THE FULL CERTIFIED FILE. The episode's own `canonical.lean` IS the artifact the checker
certified; the probes are APPENDED to it and the whole file is re-elaborated. Probing a trimmed copy
would measure a file the checker never saw — this seat's own law (`a self-test that never makes the call
its caller makes is a self-test of a different program`), applied to an artifact instead of a call.

usage: vac_probe.py <STATE_ROOT> <LEANPROJ> [--ids 0,4,96,127] [--arm a0] [--stage C]
                    [--timeout S] [--out FILE] [--json FILE]
       vac_probe.py --selftest <LEANPROJ>
exit 0 report written · 2 REFUSE (bad args / nothing to probe) · 3 a probe failed to elaborate
"""
import json, os, re, subprocess, sys

# ── THE FROZEN PROBE POINTS (amendment 11 §8, verbatim) ────────────────────────────────────────────
# Each entry: the Lean expressions to evaluate, and the VERDICT RULE applied to their printed values.
# The rule is in PYTHON, not in Lean, so it is auditable in the report rather than hidden in a proof.
PROBES = {
    0: {   # spec guarded by `numbers.length > 1` ⇒ silent for length <= 1
        "why": "problem_spec is guarded by `numbers.length > 1`; the #test lines visit only length 3 and 6",
        "evals": [("empty",  'implementation ([] : List Rat) (1/2)'),
                  ("single", 'implementation ([1] : List Rat) (1/2)')],
        # docstring: "are any two numbers closer to each other than threshold" — with <2 numbers there is
        # no such pair, so the only defensible answer is false. Anything else is wrong at the probe point.
        "rule": lambda v: (v["empty"] == "false" and v["single"] == "false"),
        "expect": "false on both (no two distinct elements exist)",
    },
    4: {   # spec guarded by `0 < numbers.length` ⇒ silent on []
        "why": "problem_spec is guarded by `0 < numbers.length`; the only #test visits a length-4 list",
        "evals": [("empty", '(implementation ([] : List Rat) == 0)'),
                  ("empty_value", 'implementation ([] : List Rat)')],
        # ⚠ WEAKER THAN THE OTHER THREE, AND SAID SO RATHER THAN FORCED: the mean absolute deviation of an
        # empty list is genuinely UNDEFINED in the docstring's own terms, so `0` is the defensible total
        # extension and not a theorem. Counted in f_vac, and flagged in the report as the soft cell.
        "rule": lambda v: v["empty"] == "true",
        "expect": "0 (the only defensible total extension; see the SOFT-CELL note)",
        "soft": True,
    },
    96: {  # spec constrains membership only — never order, never multiplicity
        "why": "the spec fixes only `every element is prime and < n` and `every prime < n is in the result`; "
               "it says NOTHING about order or duplicates, and 7 is not among the #test inputs (5,11,0,20,1,18)",
        "evals": [("at7", 'implementation 7')],
        "rule": lambda v: _strict_inc(v["at7"]),
        "expect": "[2, 3, 5] — strictly increasing and duplicate-free",
    },
    127: { # spec guarded by `s1 <= e1 -> s2 <= e2` ⇒ vacuous on an ill-formed interval
        "why": "problem_spec is guarded by `s1 ≤ e1 → s2 ≤ e2`; (5,0) is ill-formed so every clause is "
               "vacuously true, including `result = \"YES\" ∨ result = \"NO\"`",
        "evals": [("illformed", 'implementation (5,0) (0,10)')],
        # ⛔ THE QUOTES ARE NOT THERE, AND THE RED-FIRST SELFTEST IS THE ONLY REASON I KNOW IT. This rule
        # first read `in ('"YES"', '"NO"')` — the form `#eval` prints a bare String in. But the probe does not
        # print the String bare: `s!"…{impl …}"` interpolates its CONTENT, so the value arrives unquoted.
        # The vacuous-wrong arm passed anyway ("MAYBE" is outside the set under EITHER spelling); only the
        # CORRECT arm failed. ⇒ a one-sided fixture would have shown 8/8 with a rule that calls every
        # honest implementation a violation — the false-positive direction, invisible by construction.
        "rule": lambda v: v["illformed"] in ("YES", "NO"),
        "expect": '"YES" or "NO" (the spec\'s own totality clause, which the guard switches off)',
    },
}

def _strict_inc(s):
    """The printed value of a `List Nat`, e.g. `[2, 3, 5]` -> strictly increasing and duplicate-free."""
    m = re.fullmatch(r"\[\s*(.*?)\s*\]", s.strip())
    if not m: return False
    body = m.group(1)
    if body == "": return True
    try: xs = [int(x.strip()) for x in body.split(",")]
    except ValueError: return False
    return all(a < b for a, b in zip(xs, xs[1:]))

MARK = "VACPROBE"

def probe_lines(pid):
    out = []
    for name, expr in PROBES[pid]["evals"]:
        out.append('#eval s!"%s|%d|%s|{%s}"' % (MARK, pid, name, expr))
    return out

def lake_env(proj):
    """LEAN_PATH/PATH from `lake env env`, exactly as check.py:42 gets them. READ-ONLY against the shared
    project: this tool NEVER writes inside $LEANPROJ. The episodes' own `leanproj_sha` covers only the
    lakefile/manifest/toolchain, so a stray file there would not have been caught by any gate — which is
    precisely why it must not be written in the first place, and why the probe file lives in a temp dir."""
    out = subprocess.check_output(["lake", "env", "env"], cwd=proj, text=True, timeout=120)
    env = dict(os.environ)
    env["PATH"] = os.path.expanduser("~/.elan/bin") + ":" + env.get("PATH", "")
    for line in out.splitlines():
        if "=" in line:
            k, v = line.split("=", 1)
            if k.startswith("LEAN") or k == "PATH": env[k] = v
    return env

def run_probe(canon, pid, leanproj, timeout, env=None):
    """Append the frozen probes to the CERTIFIED file and elaborate it, from a temp dir OUTSIDE the shared
    Lean project (check.py's own idiom: cwd=leanproj, file elsewhere). Returns (values, rc, tail)."""
    import tempfile
    if env is None: env = lake_env(leanproj)
    src = open(canon, encoding="utf-8").read()
    d = tempfile.mkdtemp(prefix="vacprobe_")
    tmp = os.path.join(d, "probe_%d.lean" % pid)
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(src.rstrip("\n") + "\n\n-- amendment 11 \u00a78 probes, appended to the certified file\n")
        f.write("\n".join(probe_lines(pid)) + "\n")
    try:
        p = subprocess.run(["lean", tmp], cwd=leanproj, capture_output=True, text=True,
                           timeout=timeout, env=env)
        out, rc = p.stdout + p.stderr, p.returncode
    except subprocess.TimeoutExpired:
        out, rc = "TIMEOUT after %ss" % timeout, 124
    finally:
        try: os.unlink(tmp); os.rmdir(d)
        except OSError: pass
    vals = {}
    for line in out.splitlines():
        # #eval of a String prints it quoted; the marker is inside the quotes.
        if MARK not in line: continue
        body = line[line.index(MARK):].rstrip()
        if body.endswith('"'): body = body[:-1]
        parts = body.split("|")
        if len(parts) >= 4: vals[parts[2]] = "|".join(parts[3:])
    return vals, rc, out[-1200:]

def main(argv):
    if argv and argv[0] == "--selftest":
        return selftest(argv[1] if len(argv) > 1 else os.path.expanduser("~/bench/lean/clever/src/lean4"))
    if len(argv) < 2:
        print(__doc__); return 2
    root, leanproj = argv[0], argv[1]
    ids = [0, 4, 96, 127]; arm = "a0"; stage = "C"; timeout = 1800; outf = None; jsonf = None
    a = argv[2:]
    while a:
        if a[0] == "--ids": ids = [int(x) for x in a[1].split(",")]; a = a[2:]
        elif a[0] == "--arm": arm = a[1]; a = a[2:]
        elif a[0] == "--stage": stage = a[1]; a = a[2:]
        elif a[0] == "--timeout": timeout = int(a[1]); a = a[2:]
        elif a[0] == "--out": outf = a[1]; a = a[2:]
        elif a[0] == "--json": jsonf = a[1]; a = a[2:]
        else: print("REFUSE: unknown arg %s" % a[0]); return 2
    if not os.path.isdir(root): print("REFUSE: no state root %s" % root); return 2
    if not os.path.isdir(leanproj): print("REFUSE: no lean project %s" % leanproj); return 2

    # ── find the PASS'd stage-C episodes for the four permissive ids, BY CONTENT ──
    cands = []
    for d in sorted(os.listdir(root)):
        ep = os.path.join(root, d)
        cj, mj = os.path.join(ep, "check.json"), os.path.join(ep, "manifest.json")
        if not (os.path.isfile(cj) and os.path.isfile(mj)): continue
        try: c, m = json.load(open(cj)), json.load(open(mj))
        except Exception: continue
        if m.get("stage") != stage or m.get("arm") != arm: continue
        pid = c.get("problem_id")
        try: pid = int(str(pid).replace("problem_", ""))
        except Exception: continue
        if pid not in ids or pid not in PROBES: continue
        cands.append((pid, d, ep, c.get("class")))
    cands.sort()

    lines, rows, rc_worst = [], [], 0
    lines.append("AMENDMENT 11 §8 — PERMISSIVE-ORACLE DIAGNOSTIC (probe points frozen before the run)")
    lines.append("state root %s   arm %s   stage %s   n_permissive_ids %d" % (root, arm, stage, len(ids)))
    lines.append("")
    passes = [c for c in cands if c[3] == "PASS"]
    for pid, d, ep, cls in cands:
        if cls != "PASS":
            lines.append("  %-12s %s  class=%-16s NOT PROBED (only a PASS can exploit permissiveness)"
                         % ("problem_%d" % pid, d, cls))
            rows.append({"problem": pid, "episode": d, "class": cls, "probed": False})
            continue
        canon = os.path.join(ep, "canonical.lean")
        if not os.path.isfile(canon):
            lines.append("  problem_%-5d %s  PASS but no canonical.lean — PROBE FAILED" % (pid, d))
            rows.append({"problem": pid, "episode": d, "class": cls, "probed": False, "error": "no canonical.lean"})
            rc_worst = max(rc_worst, 3); continue
        vals, rc, tail = run_probe(canon, pid, leanproj, timeout)
        want = [n for n, _ in PROBES[pid]["evals"]]
        if rc != 0 or any(w not in vals for w in want):
            lines.append("  problem_%-5d %s  PASS but the probe did not elaborate (rc=%s, got %s)"
                         % (pid, d, rc, sorted(vals)))
            lines.append("      tail: %s" % tail.replace("\n", " | ")[:400])
            rows.append({"problem": pid, "episode": d, "class": cls, "probed": False,
                         "error": "probe rc=%s" % rc, "values": vals})
            rc_worst = max(rc_worst, 3); continue
        ok = bool(PROBES[pid]["rule"](vals))
        soft = PROBES[pid].get("soft", False)
        lines.append("  problem_%-5d %s  PASS   probe %s%s" %
                     (pid, d, "CORRECT" if ok else "WRONG AT THE PROBE POINT",
                      "   [SOFT CELL]" if soft else ""))
        lines.append("      vacuous because: %s" % PROBES[pid]["why"])
        lines.append("      expected: %s" % PROBES[pid]["expect"])
        for n in want:
            lines.append("      %-12s = %s" % (n, vals[n]))
        rows.append({"problem": pid, "episode": d, "class": cls, "probed": True,
                     "correct_at_probe": ok, "soft": soft, "values": vals})
    probed = [r for r in rows if r.get("probed")]
    wrong = [r for r in probed if not r["correct_at_probe"]]
    lines.append("")
    if probed:
        lines.append("f_vac = %d/%d = %.3f  (fraction of PASSes on the four permissive specs that are WRONG "
                     "at their frozen probe point)" % (len(wrong), len(probed), len(wrong) / len(probed)))
        hard = [r for r in probed if not r["soft"]]
        hardw = [r for r in hard if not r["correct_at_probe"]]
        if hard:
            lines.append("f_vac(hard cells only, problem_4 excluded as undefined-in-the-docstring) = %d/%d = %.3f"
                         % (len(hardw), len(hard), len(hardw) / len(hard)))
    else:
        lines.append("f_vac = UNDEFINED — no PASS on any of the four permissive specs (nothing to exploit)")
    lines.append("")
    lines.append("⛔ THIS IS REPORTED BESIDE P0, NEVER AGAINST IT (§8). It does not change the record, the "
                 "class of any episode, or the gate.")
    rep = "\n".join(lines)
    print(rep)
    if outf: open(outf, "w", encoding="utf-8").write(rep + "\n")
    if jsonf: json.dump({"rows": rows, "f_vac_num": len(wrong), "f_vac_den": len(probed)},
                        open(jsonf, "w"), indent=1, sort_keys=True)
    return rc_worst

# ── RED-FIRST SELFTEST: every arm drives run_probe() on a real Lean file, and each id gets BOTH a
#    correct-at-the-probe implementation and one that is wrong ONLY inside the vacuous region (so the
#    #test lines still pass and a checker would still certify it). A tool that only ever saw honest
#    artifacts would be a tool with no measured false-negative rate. ──────────────────────────────────
SELF = {
  0: ("def implementation (numbers : List Rat) (threshold : Rat) : Bool :=\n"
      "  numbers.any (fun x => numbers.any (fun y => x != y && (x - y < threshold && y - x < threshold)))",
      "def implementation (numbers : List Rat) (threshold : Rat) : Bool :=\n"
      "  if numbers.length ≤ 1 then true else\n"
      "  numbers.any (fun x => numbers.any (fun y => x != y && (x - y < threshold && y - x < threshold)))"),
  4: ("def implementation (numbers : List Rat) : Rat :=\n"
      "  if numbers.length = 0 then 0 else\n"
      "  (numbers.map (fun x => |x * numbers.length - numbers.sum|)).sum / (numbers.length * numbers.length)",
      "def implementation (numbers : List Rat) : Rat :=\n"
      "  if numbers.length = 0 then 42 else\n"
      "  (numbers.map (fun x => |x * numbers.length - numbers.sum|)).sum / (numbers.length * numbers.length)"),
  96: ("def implementation (n : Nat) : List Nat := (List.range n).filter Nat.Prime",
       "def implementation (n : Nat) : List Nat :=\n"
       "  if n = 7 then [5, 3, 2, 2] else (List.range n).filter Nat.Prime"),
  127:('def implementation (i1 : Int × Int) (i2 : Int × Int) : String :=\n'
       '  let s := max i1.1 i2.1; let e := min i1.2 i2.2;\n'
       '  if s ≤ e && Nat.Prime (e - s).toNat then "YES" else "NO"',
       'def implementation (i1 : Int × Int) (i2 : Int × Int) : String :=\n'
       '  if i1.1 > i1.2 then "MAYBE" else\n'
       '  let s := max i1.1 i2.1; let e := min i1.2 i2.2;\n'
       '  if s ≤ e && Nat.Prime (e - s).toNat then "YES" else "NO"'),
}

def selftest(leanproj):
    import tempfile
    if not os.path.isdir(leanproj):
        print("REFUSE: no lean project %s" % leanproj); return 2
    arms = failed = 0
    for pid in sorted(SELF):
        for label, body, want_ok in (("correct", SELF[pid][0], True), ("vacuous-wrong", SELF[pid][1], False)):
            arms += 1
            d = tempfile.mkdtemp()
            canon = os.path.join(d, "canonical.lean")
            open(canon, "w", encoding="utf-8").write("import Imports.AllImports\n\n" + body + "\n")
            vals, rc, tail = run_probe(canon, pid, leanproj, 900)
            want = [n for n, _ in PROBES[pid]["evals"]]
            if rc != 0 or any(w not in vals for w in want):
                print("  FAIL problem_%-4d %-14s probe did not elaborate rc=%s vals=%s" % (pid, label, rc, vals))
                print("       %s" % tail.replace("\n", " | ")[:300]); failed += 1; continue
            got = bool(PROBES[pid]["rule"](vals))
            if got == want_ok:
                print("  ok   problem_%-4d %-14s -> %-7s  %s" %
                      (pid, label, "CORRECT" if got else "WRONG", {k: vals[k] for k in want}))
            else:
                print("  FAIL problem_%-4d %-14s -> %-7s but the arm requires %s   %s" %
                      (pid, label, "CORRECT" if got else "WRONG", want_ok, {k: vals[k] for k in want}))
                failed += 1
    print("\nSELFTEST %d arms, %d failed" % (arms, failed))
    return 0 if failed == 0 else 1

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
