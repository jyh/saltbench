#!/usr/bin/env python3
"""reread.py — amendment 14 comparability re-read (08/31 law: publish the flips BY NAME).
For every landed stage-B/C episode across ALL state roots: rebuild the pristine from that root's own
frozen.json (cached per problem+stage), then run BOTH the pre-change and the amended s2audit.lean over
(canonical.olean, pristine.olean) and report every verdict that moves. Stage A never compares a value
(frozen "A" = generated_spec with cmpVal=false), so it cannot move and is not re-run. Zero model tokens."""
import glob, json, os, shutil, sys, tempfile
H = os.path.expanduser("~/bench-aw/harness/s2lean"); sys.path.insert(0, H)
import check as C
from assemble import assemble
PRE = os.path.expanduser("~/bench-aw/harness/s2lean/s2audit.lean")
NEW = os.path.expanduser("~/s2audit.NEW.lean")
LEANPROJ = os.path.expanduser("~/lean-shared/clever")
W = os.path.expanduser("~/reread-work"); shutil.rmtree(W, ignore_errors=True); os.makedirs(W)
env, lean = C.lake_env(LEANPROJ)
tmpl = open(os.path.join(H, "sandbox_check.sb")).read()
prof = C.render_profile(tmpl, lean, [W])
shutil.copy(PRE, os.path.join(W, "pre.lean")); shutil.copy(NEW, os.path.join(W, "new.lean"))

def audit(af, canon, pris, stage):
    rc, out, wall, _, _ = C.run_fenced([lean, "--run", os.path.join(W, af), canon, pris, stage, "-"],
                                       W, env, prof, 900, af)
    js = [l for l in out.splitlines() if l.strip().startswith("{")]
    return json.loads(js[-1]) if js else {"error": "no json rc=%s" % rc}

pcache = {}
def pristine(root, prob, stage):
    key = (root, prob, stage)
    if key in pcache: return pcache[key]
    fzp = os.path.join(root, "s2views", prob, "frozen.json")
    if not os.path.exists(fzp): pcache[key] = None; return None
    fz = json.load(open(fzp))
    tag = "pris_%s_%s_%s" % (os.path.basename(root), prob, stage)
    src = os.path.join(W, tag + ".lean"); ol = os.path.join(W, tag + ".olean")
    open(src, "w", encoding="utf-8").write(assemble(stage, fz, {}, pristine=True))
    rc, out, wall, _, _ = C.run_fenced([lean, "--root=" + W, "-o", ol, src], W, env, prof, 900, src)
    pcache[key] = ol if rc == 0 else None
    if rc != 0: print("   PRISTINE FAILED %s %s %s rc=%s" % (root, prob, stage, rc), flush=True)
    return pcache[key]

rows, n, flips, errs = [], 0, [], []
eps = []
for root in sorted(glob.glob(os.path.expanduser("~/bench*"))):
    for m in sorted(glob.glob(os.path.join(root, "state", "ep-*", "manifest.json"))):
        d = os.path.dirname(m)
        try: mf = json.load(open(m))
        except Exception: continue
        if mf.get("stage") not in ("B", "C"): continue
        if not os.path.exists(os.path.join(d, "canonical.olean")): continue
        eps.append((root, d, mf))
print("stage-B/C episodes with a canonical.olean: %d" % len(eps), flush=True)
for root, d, mf in eps:
    prob = mf["instance_id"]; stage = mf["stage"]
    p = pristine(root, prob, stage)
    if not p:
        errs.append((d, "no pristine")); continue
    canon = os.path.join(d, "canonical.olean")
    a1 = audit("pre.lean", canon, p, stage); a2 = audit("new.lean", canon, p, stage)
    n += 1
    k1 = (a1.get("statements_identical"), tuple(a1.get("statement_diffs") or []))
    k2 = (a2.get("statements_identical"), tuple(a2.get("statement_diffs") or []))
    if "error" in a1 or "error" in a2: errs.append((d, a1.get("error") or a2.get("error")))
    elif k1 != k2:
        flips.append((root, os.path.basename(d), prob, stage, mf.get("arm"), k1, k2))
        print("   FLIP %s %s %s %s  %s -> %s" % (os.path.basename(d), prob, stage, mf.get("arm"), k1, k2), flush=True)
    if n % 20 == 0: print("   ... %d/%d re-audited" % (n, len(eps)), flush=True)
print("\nRE-READ COMPLETE: %d stage-B/C episodes re-audited under BOTH checkers" % n)
print("FLIPS: %d" % len(flips))
for f in flips: print("   %s" % (f,))
print("ERRORS: %d" % len(errs))
for e in errs[:10]: print("   %s" % (e,))
