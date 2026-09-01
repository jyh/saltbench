#!/usr/bin/env python3
"""bc_gate.py — the CONTENT gate for `stage_views.sh ship BC` (amendment 10, 2026-08-31). Runs ON THE MACHINE
THAT HOLDS THE STATE ROOT (stage_views.sh pipes it to the Studio over ssh as `python3 - <args>`).

WHY IT EXISTS. The predicate it replaces was one line:

    ssh STUDIO 'grep -q "S2 STAGE A DRIVER DONE" ~/bench/logs/run_s2_stage0.log'

and on 2026-08-31 it was measured GREEN while pointing at nothing (`FINDING-ship-bc-gate-2026-08-31.md`). Three
independent defects, and the repair answers each by name:

  1. WRONG ROOT — the path was hardwired `~/bench` while the run that mattered wrote `~/bench-a8`. ⇒ the root is
     a REQUIRED argument with NO DEFAULT. A default here protects only the caller who forgot, and forgetting is
     the bug (this repo's own law, minted by helm_append.sh's SEAT parameter).
  2. NO CLOCK — `grep -q` over an APPEND-ONLY log cannot tell today's DONE from one written a week ago; the line
     it matched was in fact 97 minutes stale AND from a different run. ⇒ every provenance episode must have
     finished within --max-age-h hours (default 24), measured against `end_utc` in its own manifest.
  3. NO SUBSTANCE — a driver's DONE line is the DRIVER'S CLAIM, not the STATE'S FACT; the line that made the gate
     green was printed by a run that executed ZERO episodes. ⇒ nothing here reads a log at all. The gate walks
     the drawn ids × the arms and, for each cell, verifies the stage-A artifact BY CONTENT: the file exists and
     is non-empty, it carries the D5 provenance keys, `a_passed` is true, the episode it names EXISTS IN THIS
     ROOT, that episode's manifest agrees on stage/instance/arm, it finished inside the age window, and
     ***its recorded `a_bodies_sha256` equals the sha256 of that episode's own bodies.json*** — the receipt is
     the content, never the tool that moved it.

usage: bc_gate.py --root <state root> --arms a0,a2 --ids "73 0 146 ..." [--max-age-h 24] [--now <epoch>]
exit 0 iff EVERY cell is green; 3 on a refusal; 2 on bad arguments.
"""
import argparse, hashlib, json, os, sys, time

D5_KEYS = ("generated_spec_body", "a_episode", "a_bodies_sha256", "a_termination", "a_passed")


def main():
    ap = argparse.ArgumentParser(add_help=True)
    ap.add_argument("--root", required=True, help="the ACTIVE state root, e.g. /Users/jyh/bench-a8 (no default)")
    ap.add_argument("--arms", required=True, help="comma-separated arms that ran stage A, e.g. a0,a2")
    ap.add_argument("--ids", required=True, help="space- or comma-separated problem ids (the drawn population)")
    ap.add_argument("--max-age-h", type=float, default=24.0)
    ap.add_argument("--now", type=float, default=None, help="epoch override, for the self-test's clock arm")
    try:
        a = ap.parse_args()
    except SystemExit:
        return 2

    root = os.path.abspath(os.path.expanduser(a.root))
    arms = [x for x in a.arms.replace(",", " ").split() if x]
    ids = [x for x in a.ids.replace(",", " ").split() if x]
    now = a.now if a.now is not None else time.time()
    if not arms or not ids:
        print("REFUSE: --arms and --ids must each name at least one value"); return 2
    if not os.path.isdir(root):
        print("REFUSE: root does not exist: %s" % root); return 3
    for x in ids:
        if not x.isdigit():
            print("REFUSE: %r is not a problem id" % x); return 2

    print("BC CONTENT GATE  root=%s  arms=%s  ids=%d  max_age_h=%g" % (root, ",".join(arms), len(ids), a.max_age_h))
    bad = 0
    for pid in ids:
        for arm in arms:
            cell = "problem_%s/%s" % (pid, arm)
            ab = os.path.join(root, "state", "s2", "problem_%s" % pid, arm, "A.bodies.json")
            def red(why):
                print("  RED   %-18s %s" % (cell, why)); return 1
            if not os.path.exists(ab):
                bad += red("no A.bodies.json (%s)" % ab); continue
            if os.path.getsize(ab) == 0:
                bad += red("A.bodies.json is EMPTY"); continue
            try:
                obj = json.load(open(ab))
            except Exception as e:
                bad += red("A.bodies.json does not parse: %s" % e); continue
            missing = [k for k in D5_KEYS if k not in obj]
            if missing:
                bad += red("A.bodies.json lacks D5 provenance %s" % missing); continue
            if obj.get("a_passed") is not True:
                bad += red("a_passed is %r — stage A did not score a pass here" % obj.get("a_passed")); continue
            if not str(obj.get("generated_spec_body") or "").strip():
                bad += red("generated_spec_body is empty"); continue
            ep = obj.get("a_episode") or ""
            man = os.path.join(root, "state", ep, "manifest.json")
            if not ep or not os.path.exists(man):
                bad += red("provenance episode %r is NOT IN THIS ROOT (%s)" % (ep, man)); continue
            try:
                m = json.load(open(man))
            except Exception as e:
                bad += red("episode manifest does not parse: %s" % e); continue
            if m.get("stage") != "A":
                bad += red("provenance episode %s is stage %r, not A" % (ep, m.get("stage"))); continue
            if m.get("instance_id") != "problem_%s" % pid or m.get("arm") != arm:
                bad += red("provenance episode %s is %s/%s, not this cell" % (ep, m.get("instance_id"), m.get("arm"))); continue
            end = m.get("end_utc")
            if not isinstance(end, (int, float)):
                bad += red("episode %s has no numeric end_utc — the gate has no clock without it" % ep); continue
            age_h = (now - float(end)) / 3600.0
            if age_h > a.max_age_h:
                bad += red("episode %s finished %.1f h ago (> %g) — STALE" % (ep, age_h, a.max_age_h)); continue
            epb = os.path.join(root, "state", ep, "bodies.json")
            if not os.path.exists(epb):
                bad += red("episode %s has no bodies.json to verify the receipt against" % ep); continue
            got = hashlib.sha256(open(epb, "rb").read()).hexdigest()
            if got != obj.get("a_bodies_sha256"):
                bad += red("RECEIPT MISMATCH: a_bodies_sha256 %s != sha256(%s/bodies.json) %s"
                           % (str(obj.get("a_bodies_sha256"))[:16], ep, got[:16])); continue
            print("  green %-18s %s  end_utc=%s (%.1f h ago)  sha=%s" % (cell, ep, int(end), age_h, got[:16]))

    n = len(ids) * len(arms)
    if bad:
        print("REFUSE: %d of %d cells failed the content gate — stage A has NOT completed in this root." % (bad, n))
        print("        (FORCE_BC=1 overrides, loudly. A DONE line is not evidence; this gate reads the state.)")
        return 3
    print("PASS: %d/%d cells carry a content-verified, in-root, fresh stage-A pass." % (n, n))
    return 0


if __name__ == "__main__":
    sys.exit(main())
