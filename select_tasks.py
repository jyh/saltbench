#!/usr/bin/env python3
"""
SaltBench wave 1 — task selection, METADATA ONLY.

The predicate and seed are frozen in PRE-REGISTRATION.md §3 and duplicated here as
executable code. A selection that can be RE-DERIVED cannot be quietly re-drawn, so this
file is the auditable form of that section.

⛔ THIS SCRIPT READS METADATA ONLY. It never reads a task's solution patch content, never
   runs a task, and never calls a model. It is safe to run before either arm exists —
   which is the point: the list is frozen before anything can fit it to a result.

⛔ THE ONE FIELD IT READS OFF A PATCH IS ITS FILE LIST (criterion 3, scope band). The
   patch TEXT is not read. That distinction is load-bearing: file count is metadata about
   scope; patch content is the answer.

Run `python3 select_tasks.py --self-test` to drive the predicate and the draw BOTH WAYS
on synthetic metadata. Every gate here ships with a failing input on record.
"""

import argparse
import hashlib
import json
import sys

# ── FROZEN 2026-08-27, BEFORE ANY MODEL CALL (PRE-REGISTRATION.md §3) ────────────────
SEED = "saltbench-wave1-2026-08-27"
N_MEASURED = 50          # the paired set
N_PILOT = 10             # offsets 50..59 — the pilot must NOT contaminate the measured set
MIN_PROBLEM_CHARS = 500
PATCH_FILES_MIN = 1
PATCH_FILES_MAX = 3
MAX_PER_REPO = 4
# ─────────────────────────────────────────────────────────────────────────────────────


def patch_file_count(patch_text):
    """Count files a unified diff touches. Reads the FILE LIST, never the content."""
    return sum(1 for line in patch_text.splitlines() if line.startswith("diff --git "))


def meets_predicate(inst):
    """Criteria 1-4 of PRE-REGISTRATION.md §3. Returns (bool, reason_if_false).

    Criterion 5 (repo-diversity cap) is NOT here: it is a property of the SET, not of an
    instance, so it is applied during the draw. Mixing the two is how a per-item filter
    silently becomes a quota.
    """
    if len(inst.get("FAIL_TO_PASS") or []) < 1:
        return False, "no FAIL_TO_PASS: no solvable signal"
    if len(inst.get("PASS_TO_PASS") or []) < 1:
        return False, "no PASS_TO_PASS: a false green would be undetectable"
    n = patch_file_count(inst.get("patch") or "")
    if not (PATCH_FILES_MIN <= n <= PATCH_FILES_MAX):
        return False, f"scope band: touches {n} files, want {PATCH_FILES_MIN}-{PATCH_FILES_MAX}"
    if len(inst.get("problem_statement") or "") < MIN_PROBLEM_CHARS:
        return False, "problem statement under the length floor: underspecified"
    return True, ""


def draw_key(instance_id):
    """Deterministic order. Anyone with this file and the public dataset re-derives it."""
    return hashlib.sha256((instance_id + SEED).encode("utf-8")).hexdigest()


def select(instances):
    """Return (measured, pilot, rejected). Pure function of the input + the frozen seed."""
    eligible, rejected = [], []
    for inst in instances:
        ok, why = meets_predicate(inst)
        (eligible if ok else rejected).append(inst if ok else {"instance_id": inst.get("instance_id"), "reason": why})

    eligible.sort(key=lambda i: draw_key(i["instance_id"]))

    chosen, per_repo = [], {}
    for inst in eligible:
        repo = inst.get("repo", "?")
        if per_repo.get(repo, 0) >= MAX_PER_REPO:
            continue
        per_repo[repo] = per_repo.get(repo, 0) + 1
        chosen.append(inst)
        if len(chosen) >= N_MEASURED + N_PILOT:
            break

    return chosen[:N_MEASURED], chosen[N_MEASURED:N_MEASURED + N_PILOT], rejected


# ── SELF-TEST: every arm driven BOTH ways ────────────────────────────────────────────

def _inst(iid, repo="r/a", ftp=1, ptp=1, files=2, chars=600):
    return {
        "instance_id": iid,
        "repo": repo,
        "FAIL_TO_PASS": ["t"] * ftp,
        "PASS_TO_PASS": ["t"] * ptp,
        "patch": "".join(f"diff --git a/f{i} b/f{i}\n+x\n" for i in range(files)),
        "problem_statement": "x" * chars,
    }


def self_test():
    ok = True

    def check(cond, msg):
        nonlocal ok
        print(("  ✅ " if cond else "  ⛔ FAIL ") + msg)
        ok = ok and cond

    print("(1) THE PREDICATE SAYS YES — and it must be able to")
    check(meets_predicate(_inst("a"))[0], "a fully conforming instance is ACCEPTED")

    print("(2) THE PREDICATE SAYS NO — each criterion driven to refusal")
    check(not meets_predicate(_inst("b", ftp=0))[0], "no FAIL_TO_PASS is REFUSED")
    check(not meets_predicate(_inst("c", ptp=0))[0], "no PASS_TO_PASS is REFUSED (false green undetectable)")
    check(not meets_predicate(_inst("d", files=9))[0], "a sprawling patch is REFUSED")
    check(not meets_predicate(_inst("e", files=0))[0], "a zero-file patch is REFUSED")
    check(not meets_predicate(_inst("f", chars=10))[0], "a short problem statement is REFUSED")

    print("(3) THE DRAW IS DETERMINISTIC")
    pool = [_inst(f"i{n}", repo=f"r/{n % 30}") for n in range(400)]
    m1, p1, _ = select(pool)
    m2, p2, _ = select(list(reversed(pool)))
    check([i["instance_id"] for i in m1] == [i["instance_id"] for i in m2],
          "input ORDER does not change the selection")
    check(len(m1) == N_MEASURED, f"measured set is exactly {N_MEASURED}")

    print("(4) THE PILOT DOES NOT CONTAMINATE THE MEASURED SET")
    overlap = {i["instance_id"] for i in m1} & {i["instance_id"] for i in p1}
    check(not overlap, f"measured ∩ pilot = ∅ (got {len(overlap)})")
    check(len(p1) == N_PILOT, f"pilot set is exactly {N_PILOT}")

    print("(5) THE REPO CAP BINDS — and can be shown to")
    mono = [_inst(f"m{n}", repo="r/only") for n in range(400)]
    mm, mp, _ = select(mono)
    check(len(mm) + len(mp) == MAX_PER_REPO,
          f"one repo yields at most {MAX_PER_REPO} (got {len(mm) + len(mp)})")
    check(len(m1) == N_MEASURED, "a DIVERSE pool still fills the set (the cap is not always binding)")

    print("(6) THE SEED MATTERS — a different seed draws a different set")
    global SEED
    keep, SEED = SEED, "some-other-seed"
    m3, _, _ = select(pool)
    SEED = keep
    check([i["instance_id"] for i in m3] != [i["instance_id"] for i in m1],
          "changing the seed changes the draw (so the seed is load-bearing, not decoration)")

    print("\n" + ("⇒ ✅ SELECTION SELF-TEST PASSED — every arm driven both ways."
                  if ok else "⇒ ⛔ SELF-TEST FAILED"))
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser(description="SaltBench wave 1 task selection (metadata only)")
    ap.add_argument("--self-test", action="store_true", help="drive the predicate and draw both ways")
    ap.add_argument("--instances", help="path to a JSON list of SWE-bench Verified instance metadata")
    a = ap.parse_args()

    if a.self_test:
        return self_test()
    if not a.instances:
        ap.error("give --instances <file.json> or --self-test")

    with open(a.instances) as f:
        pool = json.load(f)
    measured, pilot, rejected = select(pool)
    json.dump(
        {"seed": SEED, "measured": [i["instance_id"] for i in measured],
         "pilot": [i["instance_id"] for i in pilot], "n_rejected": len(rejected)},
        sys.stdout, indent=2)
    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
