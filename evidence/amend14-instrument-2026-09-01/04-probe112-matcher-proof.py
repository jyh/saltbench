#!/usr/bin/env python3
"""probe112.py — DIAGNOSTIC ONLY, zero model tokens. Rebuilds problem_112 stage-B canonical + pristine
under the SAME fence check.py uses, then reports each module's constant names. Writes nothing under
any bench state root."""
import json, os, shutil, subprocess, sys
H = os.path.expanduser("~/bench-aw/harness/s2lean")
sys.path.insert(0, H)
import check as C
from assemble import assemble

LEANPROJ = os.path.expanduser("~/lean-shared/clever")
EP = os.path.expanduser("~/bench-aw/state/ep-2714f8d2")
FZ = json.load(open(os.path.expanduser("~/bench-aw/s2views/problem_112/frozen.json")))
W = os.path.expanduser("~/probe112"); shutil.rmtree(W, ignore_errors=True); os.makedirs(W)

env, lean = C.lake_env(LEANPROJ)
template = open(os.path.join(H, "sandbox_check.sb")).read()

# canonical = the EXACT scored file (byte-copied from the episode, sha-checked)
shutil.copy(os.path.join(EP, "canonical.lean"), os.path.join(W, "canonical.lean"))
assert C.sha_f(os.path.join(W, "canonical.lean")) == C.sha_f(os.path.join(EP, "canonical.lean"))
open(os.path.join(W, "pristine.lean"), "w").write(assemble("B", FZ, {}, pristine=True))

for name in ("canonical", "pristine"):
    src, ol = os.path.join(W, name + ".lean"), os.path.join(W, name + ".olean")
    rc, out, wall, _, _ = C.run_fenced([lean, "--root=" + W, "-o", ol, src], W, env,
                                       C.render_profile(template, lean, [W]), 600, src)
    print("%s: rc=%s wall=%ss olean=%s" % (name, rc, wall, os.path.exists(ol)))
    if rc != 0: print(out[-800:]); sys.exit(1)

probe = os.path.join(W, "probe.lean")
open(probe, "w").write('''
import Lean
open Lean
def consts (p : String) : IO (Array Name) := do
  let (md, _) ← readModuleData p
  return (md.constants.map (·.name)).qsort Name.lt
def valOf (p : String) (n : Name) : IO (Option Expr) := do
  let (md, _) ← readModuleData p
  for ci in md.constants do
    if ci.name == n then
      match ci with
      | .defnInfo v => return some v.value
      | .thmInfo v  => return some v.value
      | _ => return none
  return none
def main (args : List String) : IO Unit := do
  let c := args[0]!; let p := args[1]!
  IO.println s!"CANONICAL constants: {← consts c}"
  IO.println s!"PRISTINE  constants: {← consts p}"
  let vc ← valOf c `problem_spec
  let vp ← valOf p `problem_spec
  IO.println s!"problem_spec value EQUAL: {vc == vp}"
  match vc, vp with
  | some a, some b =>
    IO.println s!"CANONICAL problem_spec used constants: {(a.getUsedConstants).qsort Name.lt}"
    IO.println s!"PRISTINE  problem_spec used constants: {(b.getUsedConstants).qsort Name.lt}"
  | _, _ => IO.println "one side missing"
''')
rc, out, wall, _, _ = C.run_fenced([lean, "--root=" + W, "--run", probe,
                                    os.path.join(W, "canonical.olean"), os.path.join(W, "pristine.olean")],
                                   W, env, C.render_profile(template, lean, [W]), 600, probe)
print("probe rc=%s" % rc); print(out)
