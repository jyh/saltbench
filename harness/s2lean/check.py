#!/usr/bin/env python3
"""check.py — the scout's checker for one stage of one problem (runs on the Studio, no model):
  1. assemble the canonical file (frozen statements + extracted bodies) with the axiom audit appended
  2. forbidden tokens in the BODIES: axiom, unsafe, implemented_by, extern, opaque, sorry, admit, set_option
  3. `lake env lean <file>` in the shared project (timeout); rc must be 0
  4. no "declaration uses 'sorry'" for THIS file in the output
  5. every `#print axioms` line lists only {propext, Classical.choice, Quot.sound}   (native_decide's
     Lean.ofReduceBool and any user axiom fail here)
usage: check.py <stage> <frozen.json> <bodies.json> <lean-project-dir> <workfile.lean> [--timeout 600] -> JSON"""
import json, os, re, subprocess, sys, time
stage, fzp, bdp, proj, work = sys.argv[1:6]
timeout = int(sys.argv[sys.argv.index("--timeout") + 1]) if "--timeout" in sys.argv else 600
ALLOW = {"propext", "Classical.choice", "Quot.sound"}
FORBID = re.compile(r"(^|[^A-Za-z0-9_.'])(axiom|unsafe|implemented_by|extern|opaque|sorry|admit|set_option)([^A-Za-z0-9_]|$)")
bd = json.load(open(bdp)); fz = json.load(open(fzp))
res = {"stage": stage, "problem_id": fz["problem_id"], "forbidden": [], "compiled": False, "sorry_lines": [], "axioms": {}, "axioms_ok": None, "passed": False, "rc": None, "wall_s": None, "log_tail": ""}
for k, v in bd.items():
    if k.startswith("_"): continue
    for m in FORBID.finditer(v or ""):
        res["forbidden"].append("%s: %s" % (k, m.group(2)))
src = subprocess.check_output([sys.executable, os.path.join(os.path.dirname(__file__), "assemble.py"), stage, fzp, bdp]).decode()
open(work, "w").write(src)
t0 = time.time()
try:
    p = subprocess.run(["lake", "env", "lean", work], cwd=proj, capture_output=True, text=True, timeout=timeout)
    out = p.stdout + p.stderr; res["rc"] = p.returncode
except subprocess.TimeoutExpired as e:
    out = (e.stdout or b"").decode(errors="replace") if isinstance(e.stdout, bytes) else (e.stdout or ""); res["rc"] = "TIMEOUT"
res["wall_s"] = round(time.time() - t0, 1); res["log_tail"] = out[-3000:]
res["compiled"] = (res["rc"] == 0)
res["sorry_lines"] = [l for l in out.splitlines() if "declaration uses 'sorry'" in l]
for m in re.finditer(r"'([A-Za-z0-9_.]+)' (?:depends on axioms: \[(.*?)\]|does not depend on any axioms)", out):
    ax = [a.strip() for a in (m.group(2) or "").split(",") if a.strip()]
    res["axioms"][m.group(1)] = ax
if res["compiled"]:
    res["axioms_ok"] = bool(res["axioms"]) and all(set(v) <= ALLOW for v in res["axioms"].values())
res["passed"] = bool(res["compiled"] and not res["sorry_lines"] and res["axioms_ok"] and not res["forbidden"])
print(json.dumps(res, indent=1))
