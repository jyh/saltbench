#!/usr/bin/env python3
"""For every landed episode's canonical.olean: does problem_spec's VALUE use a match-auxiliary
constant that problem_spec does not own? That is the exact trip condition of the
STATEMENT_ALTERED false positive. Zero model tokens; reads oleans only."""
import glob, json, os, subprocess, sys, shutil
H = os.path.expanduser("~/bench-aw/harness/s2lean"); sys.path.insert(0, H)
import check as C
LEANPROJ = os.path.expanduser("~/lean-shared/clever")
W = os.path.expanduser("~/probe-sweep"); shutil.rmtree(W, ignore_errors=True); os.makedirs(W)
env, lean = C.lake_env(LEANPROJ)
probe = os.path.join(W, "sweep.lean")
open(probe, "w").write('''
import Lean
open Lean
def main (args : List String) : IO Unit := do
  for p in args do
    try
      let (md, _) ← readModuleData p
      let mut found : Array Name := #[]
      let mut stage := "?"
      for ci in md.constants do
        if ci.name == `problem_spec then
          stage := "has_problem_spec"
          let v := match ci with | .defnInfo d => d.value | .thmInfo d => d.value | _ => default
          for c in v.getUsedConstants do
            let s := c.toString
            if (s.splitOn ".match_").length > 1 then
              if !(s.startsWith "problem_spec.match_") then found := found.push c
      IO.println s!"{p}\t{stage}\t{found}"
    catch e => IO.println s!"{p}\tERR\t{e}"
''')
oleans = []
for r in sorted(glob.glob(os.path.expanduser("~/bench*"))):
    oleans += sorted(glob.glob(os.path.join(r, "state", "ep-*", "canonical.olean")))
print("canonical.olean files: %d" % len(oleans))
# chunk to keep argv sane
hits, seen = [], 0
for i in range(0, len(oleans), 60):
    chunk = oleans[i:i+60]
    rc, out, wall, _, _ = C.run_fenced([lean, "--root=" + W, "--run", probe] + chunk, W, env,
                                       C.render_profile(template=open(os.path.join(H, "sandbox_check.sb")).read(),
                                                        lean_bin=lean, write_paths=[W]), 900, probe)
    if rc != 0:
        print("chunk rc=%s" % rc); print(out[-1500:]); sys.exit(1)
    for line in out.splitlines():
        if "\t" not in line: continue
        p, stage, found = line.split("\t", 2)
        seen += 1
        if stage == "has_problem_spec" and found.strip() not in ("#[]", ""):
            hits.append((p, found))
print("modules read: %d" % seen)
print("TRIP CONDITION (problem_spec's value uses a matcher it does not own): %d" % len(hits))
for p, f in hits: print("   %s  %s" % (p, f))
