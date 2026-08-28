#!/usr/bin/env python3
"""
SaltBench wave 1 — task selection, METADATA ONLY.

⛔⛔ RE-FROZEN 2026-08-27 21:0x AFTER A 6/6 REPAIR-THEN-FIRE REFUTER PASS. The previous
   freeze was measurably unbuildable: run against the live 500-row split it returned
   measured=42, pilot=0 and RAISED NOTHING. Reproduced at this hand before repairing —
   that reproduction is the entry price for claiming a fix.

   THREE DEFECTS, all of them mine, all found by refuters running THIS FILE:

   (1) THE CAP STARVED THE DRAW. MAX_PER_REPO=4 over the 11 eligible repos ceilings the
       draw at sum(min(eligible_r,4)) = 42, against the 60 the loop asked for. The old
       code sliced chosen[:50] and chosen[50:60] and returned a short list in silence.
   (2) THE PREDICATE WAS A NO-OP ON THE REAL ENCODING. FAIL_TO_PASS / PASS_TO_PASS ship
       as JSON-encoded STRINGS in SWE-bench Verified, so `len(...)` counted CHARACTERS.
       len("[]") == 2, so the criterion that exists to guarantee a regression surface
       admitted the 11 instances that have none. Two of them (pylint-dev__pylint-4604,
       -4661) were in the frozen measured set.
   (3) MY SELF-TEST'S FIXTURES BRACKETED THE FAILURE AND NEVER TOUCHED IT. The "diverse"
       pool was `repo=f"r/{n%30}"` — THIRTY synthetic repos, so 30*4=120 >= 60 and the cap
       never bound; the other fixture was MONO-repo, where it always bound. The real
       substrate sits at ELEVEN, between the two fixtures, which is exactly the interval
       where the design breaks. Both arms were driven and green meant nothing.
       ⇒ ***A SELFTEST INHERITS THE SCOPE OF ITS FIXTURES.*** The fixtures below are now
       the REAL repo distribution and the REAL string encoding.

⛔ THIS SCRIPT READS METADATA ONLY. It never reads a task's solution patch content, never
   runs a task, and never calls a model. The one field it reads off a patch is its FILE
   LIST (criterion 3); the patch TEXT is not read.

Run `python3 select_tasks.py --self-test` to drive every arm both ways.
"""

import argparse
import hashlib
import json
import sys
from collections import Counter, defaultdict

# ── FROZEN 2026-08-27 21:0x, BEFORE ANY MODEL CALL (PRE-REGISTRATION.md §3) ──────────
SEED = "saltbench-wave1-2026-08-27"
N_MEASURED = 50
N_PILOT = 30             # raised from 10: at n=10 the band decision mis-routes a
                         # dead-centre model 34.4% of the time (exact binomial).
MIN_PROBLEM_CHARS = 500
PATCH_FILES_MIN = 1
PATCH_FILES_MAX = 3
STRATA_TOLERANCE = 0.08   # max per-repo share gap between measured and pilot
MAX_PER_REPO = 9         # ⛔ CHOSEN FROM MEASURED ARITHMETIC, NOT PREFERENCE.
                         # ceiling = sum(min(eligible_r, cap)) over the 11 eligible repos:
                         #   cap 4 -> 42   cap 5 -> 52   cap 6 -> 62
                         #   cap 8 -> 78   cap 9 -> 86   cap 10 -> 94
                         # We need N_MEASURED + N_PILOT = 80. cap 8 STARVES (78); cap 9
                         # clears it with 6 to spare. The diversity intent survives:
                         # django is 46% of the raw split and at most 9/80 = 11% here.

# The draw depends on byte-level fields (patch file list, statement length), so the
# snapshot is pinned. Anyone re-deriving must use this revision.
DATASET = "princeton-nlp/SWE-bench_Verified"
DATASET_SPLIT = "test"
DATASET_ROWS = 500
DATASET_REPO_SHA = "c104f840cc67f8b6eec6f759ebc8b2693d585d4a"   # HF repo revision
DATASET_ROWS_SHA256 = "4f74c5cff0d5838cd8026295d7ed61ed8171147207ead7d795ff18c977712ae2"
# ⛔ A ROW COUNT IS NOT A CONTENT PIN. The draw depends on byte-level fields — the gold
#   patch's file list and the statement length — so any upstream reformatting changes the
#   eligible set and therefore the sorted draw. `data/` is gitignored, so without these two
#   values the bytes the frozen list came from are not recoverable and
#   "anyone may re-derive the exact task list" is false.
# ─────────────────────────────────────────────────────────────────────────────────────


def parse_ids(value):
    """FAIL_TO_PASS / PASS_TO_PASS are JSON-encoded STRINGS in the published dataset.

    ⛔ THE OLD CODE CALLED len() ON THE RAW VALUE, so it counted characters and len("[]")
    was 2 — the criterion passed on an EMPTY list. Decode first, always.
    """
    if isinstance(value, str):
        try:
            value = json.loads(value)
        except (ValueError, TypeError):
            return []
    return value or []


def patch_file_count(patch_text):
    """Count files a unified diff touches. Reads the FILE LIST, never the content."""
    return sum(1 for line in (patch_text or "").splitlines() if line.startswith("diff --git "))


def meets_predicate(inst):
    """Criteria 1-4 of PRE-REGISTRATION.md §3. Returns (bool, reason_if_false).

    Criterion 5 (repo-diversity cap) is NOT here: it is a property of the SET, not of an
    instance, so it is applied during the draw.
    """
    if len(parse_ids(inst.get("FAIL_TO_PASS"))) < 1:
        return False, "no FAIL_TO_PASS: no solvable signal"
    if len(parse_ids(inst.get("PASS_TO_PASS"))) < 1:
        return False, "no PASS_TO_PASS: a false green would be undetectable"
    n = patch_file_count(inst.get("patch"))
    if not (PATCH_FILES_MIN <= n <= PATCH_FILES_MAX):
        return False, f"scope band: touches {n} files, want {PATCH_FILES_MIN}-{PATCH_FILES_MAX}"
    if len(inst.get("problem_statement") or "") < MIN_PROBLEM_CHARS:
        return False, "problem statement under the length floor: underspecified"
    return True, ""


def draw_key(instance_id, seed=SEED):
    """Deterministic order. Seed is a PARAMETER — the frozen constant is never mutated.

    ⛔ The old self-test did `global SEED` with no try/finally, so any exception inside
    select() left the frozen seed permanently changed for every later in-process caller,
    in the one file whose whole thesis is that the seed is frozen.
    """
    return hashlib.sha256((instance_id + seed).encode("utf-8")).hexdigest()


class DrawStarved(Exception):
    """The cap cannot serve the pre-registered n. Raised LOUDLY, never truncated."""


def select(instances, seed=SEED, n_measured=N_MEASURED, n_pilot=N_PILOT,
           max_per_repo=MAX_PER_REPO):
    """Return (measured, pilot, rejected).

    THE ALGORITHM, stated because the prose version was unimplementable (criterion 5 has
    no per-item form, and the old text gave no tie-break for which N of a repo survive):
      1. filter by criteria 1-4;
      2. sort by sha256(instance_id + SEED);
      3. walk in that order, admitting while that repo's count < max_per_repo;
      4. RAISE if fewer than n_measured + n_pilot were admitted;
      5. partition into measured/pilot by STRATIFIED assignment within each repo, so the
         pilot mirrors the measured set's repo mix.

    ⛔ STEP 5 REPLACES A TAIL-TAKE. The old code took chosen[50:60] — and because the cap
    is spent in hash order, the big repos fill their quota early, so the tail was composed
    ENTIRELY of the smallest codebases. The pilot's job is to estimate the baseline of the
    MEASURED set; drawn from the tail it shared near-zero composition with it, and that
    bias survives n -> infinity.
    """
    eligible, rejected = [], []
    for inst in instances:
        ok, why = meets_predicate(inst)
        if ok:
            eligible.append(inst)
        else:
            rejected.append({"instance_id": inst.get("instance_id"), "reason": why})

    eligible.sort(key=lambda i: draw_key(i["instance_id"], seed))

    want = n_measured + n_pilot
    chosen, per_repo = [], Counter()
    for inst in eligible:
        repo = inst.get("repo", "?")
        if per_repo[repo] >= max_per_repo:
            continue
        per_repo[repo] += 1
        chosen.append(inst)
        if len(chosen) >= want:
            break

    if len(chosen) < want:
        ceiling = sum(min(v, max_per_repo) for v in Counter(i.get("repo", "?") for i in eligible).values())
        raise DrawStarved(
            f"cap starves the draw: admitted {len(chosen)} of {want} "
            f"(max_per_repo={max_per_repo}, eligible={len(eligible)}, ceiling={ceiling}). "
            f"Per-repo admitted: {dict(per_repo)}. "
            f"Raise max_per_repo or lower n — do NOT truncate."
        )

    # ── step 5: stratified partition by LARGEST-REMAINDER APPORTIONMENT ──
    # ⛔ THE FIRST REPAIR OF THIS STEP WAS ALSO WRONG, AND THE REAL DATA CAUGHT IT WHEN
    #    MY FIXTURE DID NOT. I rounded each repo's share and then fixed the total with a
    #    blind `measured.pop()` from the tail — which dumped the ENTIRE rounding surplus
    #    into whichever repo happened to sit last in draw order. Measured on the live
    #    split: pytest came out 6.0% of measured against 20.0% of the pilot, a 14-point
    #    gap, while the shape-matched synthetic fixture passed at 10.0%.
    #    ⇒ A FIXTURE THAT MATCHES THE POPULATION'S SHAPE STILL DOES NOT MATCH ITS ORDER.
    #    Largest-remainder removes the fix-up entirely: every repo lands on floor or ceil
    #    of its exact share, so no repo can absorb the surplus.
    by_repo = defaultdict(list)
    for inst in chosen:
        by_repo[inst.get("repo", "?")].append(inst)

    exact = {r: len(v) * n_measured / want for r, v in by_repo.items()}
    quota = {r: int(e) for r, e in exact.items()}
    short = n_measured - sum(quota.values())
    # hand out the remaining seats to the largest fractional remainders; ties broken by
    # repo name so the result is deterministic and re-derivable.
    for r in sorted(exact, key=lambda r: (-(exact[r] - quota[r]), r))[:short]:
        quota[r] += 1

    order = {id(x): n for n, x in enumerate(chosen)}
    measured, pilot = [], []
    for repo, items in by_repo.items():
        k = min(quota[repo], len(items))
        measured.extend(items[:k])
        pilot.extend(items[k:])
    measured.sort(key=lambda x: order[id(x)])
    pilot.sort(key=lambda x: order[id(x)])
    pilot = pilot[:n_pilot]

    # ⭐ THE GUARANTEE LIVES HERE, NOT IN THE SELF-TEST, so no caller can skip it.
    if measured and pilot:
        mm = Counter(x.get("repo", "?") for x in measured)
        pp = Counter(x.get("repo", "?") for x in pilot)
        worst = max(abs(mm[r] / len(measured) - pp[r] / len(pilot))
                    for r in set(mm) | set(pp))
        if worst > STRATA_TOLERANCE:
            raise DrawStarved(
                f"stratification failed: worst per-repo share gap {worst:.1%} > "
                f"{STRATA_TOLERANCE:.0%}. measured={dict(mm)} pilot={dict(pp)}")

    assert len(measured) == n_measured, f"measured {len(measured)} != {n_measured}"
    assert len(pilot) == n_pilot, f"pilot {len(pilot)} != {n_pilot}"
    return measured, pilot, rejected


# ── SELF-TEST: fixtures now match the REAL substrate ─────────────────────────────────

# The eligible-pool distribution MEASURED at this hand against the live 500-row split.
REAL_ELIGIBLE = [
    ("django/django", 172), ("sympy/sympy", 54), ("sphinx-doc/sphinx", 40),
    ("matplotlib/matplotlib", 33), ("scikit-learn/scikit-learn", 31),
    ("pydata/xarray", 22), ("astropy/astropy", 20), ("pytest-dev/pytest", 16),
    ("psf/requests", 6), ("pylint-dev/pylint", 6), ("mwaskom/seaborn", 2),
]


def _inst(iid, repo="r/a", ftp=1, ptp=1, files=2, chars=600, as_string=True):
    """Fixture in the DATASET'S NATIVE ENCODING by default (JSON strings, not lists)."""
    f2p = ["t"] * ftp
    p2p = ["t"] * ptp
    return {
        "instance_id": iid,
        "repo": repo,
        "FAIL_TO_PASS": json.dumps(f2p) if as_string else f2p,
        "PASS_TO_PASS": json.dumps(p2p) if as_string else p2p,
        "patch": "".join(f"diff --git a/f{i} b/f{i}\n+x\n" for i in range(files)),
        "problem_statement": "x" * chars,
    }


def _real_pool():
    pool = []
    for repo, n in REAL_ELIGIBLE:
        pool += [_inst(f"{repo.split('/')[-1]}-{i}", repo=repo) for i in range(n)]
    return pool


def self_test():
    ok = True

    def check(cond, msg):
        nonlocal ok
        print(("  ✅ " if cond else "  ⛔ FAIL ") + msg)
        ok = ok and cond

    print("(1) THE PREDICATE, ON THE DATASET'S NATIVE STRING ENCODING")
    check(meets_predicate(_inst("a"))[0], "a conforming instance (JSON strings) is ACCEPTED")
    check(not meets_predicate(_inst("b", ftp=0))[0], 'FAIL_TO_PASS "[]" is REFUSED')
    check(not meets_predicate(_inst("c", ptp=0))[0], 'PASS_TO_PASS "[]" is REFUSED — THE OLD CODE ADMITTED IT')
    check(not meets_predicate(_inst("d", files=9))[0], "a sprawling patch is REFUSED")
    check(not meets_predicate(_inst("e", files=0))[0], "a zero-file patch is REFUSED")
    check(not meets_predicate(_inst("f", chars=10))[0], "a short problem statement is REFUSED")
    check(meets_predicate(_inst("g", as_string=False))[0], "a native-LIST instance still works (both encodings)")

    print("(2) THE REGRESSION TEST FOR THE ENCODING BUG, DRIVEN EXPLICITLY")
    raw = {"instance_id": "z", "repo": "r/z", "FAIL_TO_PASS": "[]", "PASS_TO_PASS": "[]",
           "patch": "diff --git a/f b/f\n+x\n", "problem_statement": "x" * 600}
    check(len("[]") == 2 and not meets_predicate(raw)[0],
          'len("[]")==2 would have PASSED the old test; the new predicate REFUSES it')

    print("(3) THE CAP MUST BE ABLE TO STARVE — AND SAY SO, NOT TRUNCATE")
    starved = False
    try:
        select(_real_pool(), max_per_repo=4)
    except DrawStarved as e:
        starved = True
        print(f"      raised: {str(e)[:96]}…")
    check(starved, "the REAL 11-repo pool at the OLD cap=4 RAISES DrawStarved (it silently returned 42)")

    print("(4) AT THE RE-FROZEN CAP THE DRAW IS SERVED, ON THE REAL DISTRIBUTION")
    m, p, _ = select(_real_pool())
    check(len(m) == N_MEASURED, f"measured is exactly {N_MEASURED}")
    check(len(p) == N_PILOT, f"pilot is exactly {N_PILOT}")

    print("(5) THE PILOT MIRRORS THE MEASURED REPO MIX (it used to be the tail)")
    mm = Counter(x["repo"] for x in m)
    pp = Counter(x["repo"] for x in p)
    shared = set(mm) & set(pp)
    check(len(shared) >= max(1, len(mm) - 2),
          f"pilot shares {len(shared)} of {len(mm)} measured repos")
    worst = max((abs(mm[r] / len(m) - pp[r] / len(p)) for r in set(mm) | set(pp)), default=1.0)
    # ⛔ WAS `<= 0.12` WHILE select() RAISES ABOVE STRATA_TOLERANCE=0.08 — a branch that
    #   could never fail, in the file that had just learned "green meant nothing".
    check(worst <= STRATA_TOLERANCE, f"largest per-repo share gap {worst:.1%} <= {STRATA_TOLERANCE:.0%}")
    check(not (set(x['instance_id'] for x in m) & set(x['instance_id'] for x in p)),
          "measured ∩ pilot = ∅")

    print("(6) DETERMINISM, AND THE SEED IS LOAD-BEARING AND NEVER MUTATED")
    before = SEED
    m2, _, _ = select(list(reversed(_real_pool())))
    check([x["instance_id"] for x in m2] == [x["instance_id"] for x in m],
          "input ORDER does not change the selection")
    m3, _, _ = select(_real_pool(), seed="some-other-seed")
    check([x["instance_id"] for x in m3] != [x["instance_id"] for x in m],
          "a different seed draws a different set")
    check(SEED == before, "the frozen SEED constant was NOT mutated (old code used `global SEED`)")

    print("\n" + ("⇒ ✅ SELECTION SELF-TEST PASSED — fixtures match the real substrate."
                  if ok else "⇒ ⛔ SELF-TEST FAILED"))
    return 0 if ok else 1


def dataset_rows_sha256(rows):
    """THE RECIPE for DATASET_ROWS_SHA256 -- published as an invocation, not a number (silicon's
    handoff defect, 08/28: four defensible fold recipes give four digests over one set of bytes,
    and the only sort_keys in this file emits with indent=2, which is a DIFFERENT digest).
        sha256(json.dumps(rows, sort_keys=True, separators=(",", ":")).encode("utf-8"))
    """
    return hashlib.sha256(json.dumps(rows, sort_keys=True, separators=(",", ":")).encode("utf-8")).hexdigest()


def verify_dataset(path):
    rows = json.load(open(path))
    got = dataset_rows_sha256(rows)
    print(f"rows={len(rows)} expected_rows={DATASET_ROWS}")
    print(f"sha256(compact,sort_keys)  = {got}")
    print(f"DATASET_ROWS_SHA256 (pinned) = {DATASET_ROWS_SHA256}")
    alt = hashlib.sha256(json.dumps(rows, sort_keys=True, indent=2).encode("utf-8")).hexdigest()
    print(f"sha256(indent=2,sort_keys) = {alt}   <- NOT the pin; shown so the recipe is seen to matter")
    ok = got == DATASET_ROWS_SHA256 and len(rows) == DATASET_ROWS
    print("DATASET", "MATCHES the pin" if ok else "DOES NOT MATCH the pin")
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser(description="SaltBench wave 1 task selection (metadata only)")
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--verify-dataset", metavar="ROWS_JSON",
                    help="recompute DATASET_ROWS_SHA256 over ROWS_JSON with THE RECIPE and compare")
    ap.add_argument("--instances", help="JSON list of SWE-bench Verified instance metadata")
    ap.add_argument("--emit", help="write the frozen task list here")
    a = ap.parse_args()

    if a.self_test:
        return self_test()
    if a.verify_dataset:
        return verify_dataset(a.verify_dataset)
    if not a.instances:
        ap.error("give --instances <file.json> or --self-test")

    pool = json.load(open(a.instances))
    measured, pilot, rejected = select(pool)
    out = {
        "dataset": DATASET, "split": DATASET_SPLIT, "rows": DATASET_ROWS,
        "seed": SEED, "max_per_repo": MAX_PER_REPO,
        "n_measured": len(measured), "n_pilot": len(pilot), "n_rejected": len(rejected),
        "measured": [i["instance_id"] for i in measured],
        "pilot": [i["instance_id"] for i in pilot],
    }
    text = json.dumps(out, indent=2, sort_keys=True)
    if a.emit:
        open(a.emit, "w").write(text + "\n")
        print(f"wrote {a.emit}  sha256={hashlib.sha256((text + chr(10)).encode()).hexdigest()[:32]}")
    else:
        print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
