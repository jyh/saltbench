#!/bin/bash
# s2_controls.sh — drive every D14 control through the REAL check.py (s2_controls_kit.py built the kit on the seat),
# print PASS/FAIL per control and CONTROLS PASS iff every expectation holds, record $OUT (classes, walls, no bodies),
# then DELETE the kit (it carries ground truth) and assert its absence.
#   usage: s2_controls.sh <LEANPROJ> <KIT dir (absolute)> <out s2-controls.json>      env: KEEP_KIT=1 keeps the kit
set -u; export PATH="$HOME/.elan/bin:$PATH"
P="${1:?LEANPROJ}"; KIT="${2:?kit dir}"; OUT="${3:?out json}"; H="$(cd "$(dirname "$0")" && pwd)"
case "$KIT" in /*) ;; *) echo "REFUSE: kit dir must be absolute"; exit 2 ;; esac
[ -s "$KIT/controls.json" ] && [ -f "$KIT/.s2_controls_kit" ] || { echo "REFUSE: $KIT is not a controls kit"; exit 2; }
[ -d "$P/.lake/build/lib/lean/Imports" ] || { echo "REFUSE: $P has no built Imports"; exit 2; }
python3 "$H/screen.py" --selftest >/dev/null || { echo "REFUSE: screen.py selftest fails"; exit 2; }
WORK="$KIT/work"; rm -rf "$WORK"; mkdir -p "$WORK"
python3 - "$P" "$KIT" "$OUT" "$H" <<'PY'
import json, os, subprocess, sys, time, hashlib
P, KIT, OUT, H = sys.argv[1:5]
kit = json.load(open(os.path.join(KIT, "controls.json")))
home = os.environ["HOME"]; marker = kit["marker"].replace("__HOME__", home)
WORK = os.path.join(KIT, "work"); results = {}; allok = True
def render(o): return json.loads(json.dumps(o).replace("__HOME__", home))
for c in kit["controls"]:
    name = c["name"]; d = os.path.join(WORK, name); os.makedirs(d, exist_ok=True)
    bodies = os.path.join(d, "bodies.json"); json.dump(render(c["bodies"]), open(bodies, "w"))
    fz = os.path.join(KIT, "problem_%d" % c["problem"], "frozenA.json" if c["stage"] == "A" else "frozen.json")
    cmd = [sys.executable, os.path.join(H, "check.py"), c["stage"], fz, bodies, P, os.path.join(d, "canonical.lean"), "--timeout", str(c["timeout"])]
    if c["a_bodies"]:
        ab = os.path.join(d, "A.bodies.json"); json.dump(render(c["a_bodies"]), open(ab, "w")); cmd += ["--a-bodies", ab]
    if c["a_olean_from"]: cmd += ["--a-olean", os.path.join(WORK, c["a_olean_from"], "canonical.olean")]
    if c["no_screen"]: cmd += ["--no-screen"]
    if os.path.exists(marker): os.remove(marker)
    t0 = time.time(); p = subprocess.run(cmd, cwd=P, capture_output=True, text=True); wall = round(time.time() - t0, 1)
    try: r = json.loads(p.stdout)
    except ValueError: r = {"class": "NO_JSON", "passed": False, "harness_error": p.stderr[-800:]}
    open(os.path.join(d, "check.json"), "w").write(p.stdout)
    fails = []
    if r.get("class") not in c["expect_class"]: fails.append("class %s not in %s" % (r.get("class"), c["expect_class"]))
    if r.get("passed") != (c["expect_class"] == ["PASS"]): fails.append("passed=%s" % r.get("passed"))
    ax = set(sum((v for v in (r.get("axioms") or {}).values()), []))
    lean_left = []
    for a in c["asserts"]:
        k, _, v = a.partition(":")
        if k == "axiom" and v not in ax: fails.append("axiom %s not reported (%s)" % (v, sorted(ax)))
        elif k == "diff" and v not in (r.get("statement_diffs") or []): fails.append("no statement diff on %s" % v)
        elif k == "a_body_value_identical" and str(r.get("a_body_value_identical")).lower() != v: fails.append("a_body_value_identical=%s" % r.get("a_body_value_identical"))
        elif k == "tests_in_file" and str(r.get("tests_in_file")).lower() != v: fails.append("tests_in_file=%s" % r.get("tests_in_file"))
        elif k == "replay_error" and v not in (r.get("replay_error") or ""): fails.append("replay_error lacks %r" % v)
        elif k == "log" and v not in (r.get("log_tail") or ""): fails.append("log_tail lacks %r" % v)
        elif k == "log_absent" and v in (r.get("log_tail") or ""): fails.append("log_tail carries %r" % v)
        elif k == "marker_absent" and os.path.exists(marker): fails.append("MARKER WRITTEN: %s" % marker); os.remove(marker)
        elif k == "no_lean_left":
            time.sleep(1); pg = subprocess.run(["pgrep", "-fl", os.path.join(d, "canonical.lean")], capture_output=True, text=True)
            lean_left = [l for l in pg.stdout.splitlines() if "lean" in l]
            if lean_left: fails.append("lean still running: %s" % lean_left)
    ok = not fails; allok &= ok
    results[name] = {"ok": ok, "class": r.get("class"), "passed": r.get("passed"), "expect_class": c["expect_class"], "fails": fails,
                     "compile_wall_s": r.get("compile_wall_s"), "audit_wall_s": r.get("audit_wall_s"), "pristine_wall_s": r.get("pristine_wall_s"),
                     "check_wall_s": wall, "rc": r.get("rc"), "screen": r.get("screen"), "statement_diffs": r.get("statement_diffs"),
                     "axioms": r.get("axioms"), "replay_error": (r.get("replay_error") or "")[:160], "orphans_killed": r.get("orphans_killed"),
                     "a_body_value_identical": r.get("a_body_value_identical"), "tests_in_file": r.get("tests_in_file"),
                     "harness_error": (r.get("harness_error") or "")[:300], "note": c["note"]}
    print("%-4s %-26s class=%-18s expect=%-30s passed=%-5s compile=%-6s audit=%-5s total=%-6s %s" % (
        "PASS" if ok else "FAIL", name, r.get("class"), "|".join(c["expect_class"]), r.get("passed"), r.get("compile_wall_s"), r.get("audit_wall_s"), wall, "; ".join(fails)), flush=True)
pg = subprocess.run(["pgrep", "-fl", "lean"], capture_output=True, text=True).stdout
mine = [l for l in pg.splitlines() if WORK in l]
print("pgrep -fl lean (this kit's work dir): %s" % (mine or "none"))
print("pgrep -fl lean (all, other seats' processes included): %d line(s)" % len(pg.splitlines()))
summary = {"controls_pass": allok and not mine, "n": len(results), "n_ok": sum(1 for v in results.values() if v["ok"]),
           "leanproj": P, "checker_sha256": {f: hashlib.sha256(open(os.path.join(H, f), "rb").read()).hexdigest() for f in ("check.py", "s2audit.lean", "screen.py", "assemble.py", "sandbox_check.sb")},
           "date": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "results": results}
json.dump(summary, open(OUT, "w"), indent=1)
print("CONTROLS %s (%d/%d)" % ("PASS" if summary["controls_pass"] else "FAIL", summary["n_ok"], summary["n"]))
sys.exit(0 if summary["controls_pass"] else 1)
PY
rc=$?
if [ -z "${KEEP_KIT:-}" ]; then rm -rf "$KIT"; [ -e "$KIT" ] && { echo "KIT STILL PRESENT: $KIT"; exit 2; }; echo "kit deleted: $KIT"; fi
exit $rc
