#!/usr/bin/env python3
"""verify_arm_render.py — assert every cell's arm file IS the accepted template, rendered.

⛔⛔ WHY A SHA COMPARISON CANNOT DO THIS, AND WHY THE ATTEMPT LOOKS LIKE A FINDING.
  An acceptance ruling pins the arm artefact by sha and says, correctly, that the sha is the artefact
  and the path is not.  But the file a cell carries is the template RENDERED: the builder substitutes
  the task name for a placeholder.  So the ruled sha can NEVER equal a fired cell's sha, for any
  cell, ever.
  ⇒ 🔑 A RULING THAT PINS A TEMPLATE BY SHA CANNOT BE CHECKED AGAINST A RENDERED CELL BY SHA, AND A
    HEAD WHO TRIES GETS A MISMATCH THAT READS AS "THE CELLS RAN ON AN UNRULED ARTEFACT".
  That is a false alarm in the expensive direction: it impugns an entire arm's cells over a
  difference the design put there deliberately.

✅ WHAT IS CHECKED: rendering the template with the DECLARED substitution must reproduce the cell's
  file EXACTLY.  Not "the diff looks like a substitution" — the rendered bytes are compared.
⛔ THE SUBSTITUTION IS A PARAMETER, NEVER A GUESS ABOUT WORDING.  An earlier cut of this file
  classified a diff line as "a substitution" if it contained the placeholder OR a phrase from the
  template's title.  That is a filter that names one member of a set: it passes whatever it was
  written against and goes vacuous the moment the template's wording changes.

usage: verify_arm_render.py TEMPLATE CELLS_ROOT --placeholder '<Task>' [--arm ARM] [--value-from ctl/task]
       the substituted VALUE defaults to the cell's own ctl/task field 1, which is where the builder
       takes it from; pass --value X to force one.
"""
import os, sys

def opt(name, default=None):
    return sys.argv[sys.argv.index(name) + 1] if name in sys.argv else default

def main():
    if len(sys.argv) < 3 or "--placeholder" not in sys.argv:
        print(__doc__); return 2
    tmpl, root = sys.argv[1], os.path.expanduser(sys.argv[2])
    ph, want_arm, forced = opt("--placeholder"), opt("--arm"), opt("--value")
    T = open(tmpl, encoding="utf-8").read()
    if ph not in T:
        print("REFUSE — the placeholder %r does not occur in the template. A checker whose "
              "substitution never fires passes every cell." % ph)
        return 2
    ok = bad = 0
    for cid in sorted(os.listdir(root)):
        d = os.path.join(root, cid)
        if cid.startswith("_") or not os.path.isdir(d): continue
        armf = os.path.join(d, "ctl", "arm")
        if not os.path.isfile(armf): continue
        arm = open(armf).read().strip()
        if want_arm and arm != want_arm: continue
        cf = next((p for p in (os.path.join(d, "repo", n) for n in ("CLAUDE.md", "AGENTS.md"))
                   if os.path.isfile(p)), None)
        if cf is None:
            print("  %-10s %-10s ⛔ REFUSE — no arm file in repo/" % (cid, arm)); bad += 1; continue
        val = forced
        if val is None:
            tf = os.path.join(d, "ctl", "task")
            val = open(tf).readline().split("\t")[0].strip() if os.path.isfile(tf) else None
        if not val:
            print("  %-10s %-10s ⛔ REFUSE — no value to substitute (ctl/task unreadable)" % (cid, arm))
            bad += 1; continue
        rendered = T.replace(ph, val)
        actual = open(cf, encoding="utf-8").read()
        if rendered == actual:
            ok += 1
            print("  %-10s %-10s ✅ template rendered with %s=%s reproduces the cell EXACTLY"
                  % (cid, arm, ph, val))
        else:
            bad += 1
            n = min(len(rendered), len(actual))
            i = next((k for k in range(n) if rendered[k] != actual[k]), n)
            print("  %-10s %-10s ⛔ DIFFERS from the rendered template at byte %d (len %d vs %d)"
                  % (cid, arm, i, len(rendered), len(actual)))
    print("\n  %d cell(s) carry the accepted template, rendered · %d REFUSED · template %s"
          % (ok, bad, os.path.basename(tmpl)))
    return 1 if bad else 0

sys.exit(main())
