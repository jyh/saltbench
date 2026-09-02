#!/usr/bin/env python3
"""fetch_problem_statements.py: re-derive harness/data/problem_statements.json from the pinned
SWE-bench Verified revision, instead of redistributing the 30 issue texts from this repository.

WHY THIS FILE EXISTS. The 30 problem statements are GitHub issue text authored by the reporters of
nine source repositories. The SWE-bench Verified dataset card carries no licence field
(PROVENANCE.md section 1.3), so this repository does not redistribute the text. It redistributes
what identifies it exactly: the 30 ids (TASKLIST.json "pilot"), the dataset repo revision
(TASKLIST.json "dataset_repo_sha"), the sha256 over the 500 canonicalised rows the draw was made
from (TASKLIST.json "rows_sha256_canonical"), and the sha256 of the projection itself
(harness/HASHES.txt, key "problem_statements.json"). Those four values make the reconstruction
verifiable byte for byte: if your rebuilt file matches the pin, it is the file the episodes read.

WHAT IT IS NOT. This script is NOT part of the frozen measurement apparatus. It was written on
2026-09-02 for publication, after every episode had run, and it is deliberately absent from
harness/hashes.sh's pin list so that nothing here can be mistaken for run-time apparatus. The
episodes read data/problem_statements.json; they never ran this.

WHERE THE PROJECTION CHECK NOW LIVES. build_prompt.py's self-test carries an arm asserting that the
projection holds exactly the five fields, and that arm is guarded by `if os.path.exists(...)`: with
the file absent it does not run, and the self-test still prints OK with one fewer check. The
coverage is not lost, it moved here and got stronger. project() below refuses a row carrying a field
outside the five and refuses a pilot id the rows do not supply, so the assertion now runs when the
file is BUILT rather than only when a stale copy happens to be lying beside the harness. The
self-test drives both refusals. build_prompt.py is a pinned file and was deliberately not edited;
re-pinning it to add a printed "skipped" line would change bytes the frozen run manifests recorded.

  usage:
    fetch_problem_statements.py --self-test                 # no network: drives every arm
    fetch_problem_statements.py --rows verified.json        # from a local copy of the 500 rows
    fetch_problem_statements.py --download                  # fetch the pinned revision (needs `datasets`)

  Either mode writes <harness>/data/problem_statements.json and verifies it against the pin.
"""

import argparse
import hashlib
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)

DATASET = "princeton-nlp/SWE-bench_Verified"
DATASET_SPLIT = "test"
DATASET_ROWS = 500
# The five fields the Studio was allowed to hold during an episode. No patch, no test_patch, no
# hints_text, no FAIL_TO_PASS/PASS_TO_PASS -- project_data.py's projection, restated here so this
# script is readable without it.
KEEP = ("instance_id", "problem_statement", "base_commit", "repo", "version")


def dataset_rows_sha256(rows):
    """THE RECIPE, copied from select_tasks.py. Four defensible fold recipes give four digests over
    one set of bytes, so the recipe is published as an invocation and not as a number."""
    return hashlib.sha256(json.dumps(rows, sort_keys=True, separators=(",", ":")).encode("utf-8")).hexdigest()


def project(rows, pilot_ids):
    """The projection project_data.py performs, in the order project_data.py performs it: source
    order filtered by the pilot set, NOT sorted. The pin is over these exact bytes."""
    pilot = set(pilot_ids)
    out = [{k: r[k] for k in KEEP} for r in rows if r["instance_id"] in pilot]
    if len(out) != len(pilot):
        missing = sorted(pilot - {r["instance_id"] for r in out})
        raise RuntimeError("rows do not carry every pilot id; missing %d: %s" % (len(missing), missing[:5]))
    for r in out:
        if set(r) != set(KEEP):
            raise RuntimeError("projection carries a field outside the five: %s" % sorted(set(r) - set(KEEP)))
    return json.dumps(out, sort_keys=True, separators=(",", ":"))


def read_pin(name, hashes_path):
    """Return the sha256 pinned under `name` in HASHES.txt, or None."""
    if not os.path.exists(hashes_path):
        return None
    for line in open(hashes_path):
        f = line.split()
        if len(f) >= 2 and f[0] == name:
            return f[1]
    return None


def tasklist(path):
    d = json.load(open(path))
    for k in ("pilot", "dataset_repo_sha", "rows_sha256_canonical"):
        if k not in d:
            raise RuntimeError("TASKLIST.json has no %r" % k)
    return d


def download_rows(revision):
    """Fetch the 500 rows at the PINNED revision. A default-branch fetch is refused: the draw
    depends on byte-level fields, so a later reformatting upstream would give a different set."""
    try:
        from datasets import load_dataset
    except ImportError:
        raise RuntimeError("--download needs the `datasets` package (pip install datasets), or pass "
                           "--rows with a local JSON list of the 500 rows")
    ds = load_dataset(DATASET, split=DATASET_SPLIT, revision=revision)
    return [dict(r) for r in ds]


def run(rows, tl, out_path, hashes_path):
    ok = True

    def check(cond, msg):
        nonlocal ok
        ok = ok and bool(cond)
        print(("  ok   " if cond else "  FAIL "), msg)

    print("rows: %d" % len(rows))
    check(len(rows) == DATASET_ROWS, "row count is the pinned %d" % DATASET_ROWS)
    got = dataset_rows_sha256(rows)
    want = tl["rows_sha256_canonical"]
    check(got == want, "rows_sha256_canonical matches TASKLIST.json (%s)" % want)
    if got != want:
        print("       got %s" % got)
        print("       these are not the bytes the draw was made from; check the revision "
              "(%s) before going on" % tl["dataset_repo_sha"])

    text = project(rows, tl["pilot"])
    got_p = hashlib.sha256(text.encode("utf-8")).hexdigest()
    pin = read_pin("problem_statements.json", hashes_path)
    if pin is None:
        print("  note  no problem_statements.json pin in %s; wrote without comparing" % hashes_path)
    else:
        check(got_p == pin, "projection sha256 matches harness/HASHES.txt (%s)" % pin)
        if got_p != pin:
            print("       got %s" % got_p)

    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    open(out_path, "w").write(text)
    print("wrote %s  rows=%d sha256=%s" % (out_path, len(json.loads(text)), got_p))
    print("FETCH", "OK" if ok else "FAILED")
    return 0 if ok else 1


def self_test():
    """Drives the projection, the two hashes and every refusal, with no network and no dataset."""
    ok = True

    def check(cond, msg):
        nonlocal ok
        ok = ok and bool(cond)
        print(("  ok   " if cond else "  FAIL "), msg)

    rows = [
        {"instance_id": "a__a-1", "problem_statement": "s1", "base_commit": "c1", "repo": "a/a",
         "version": "1.0", "patch": "diff --git x", "hints_text": "leak", "FAIL_TO_PASS": "[\"t\"]"},
        {"instance_id": "b__b-2", "problem_statement": "s2", "base_commit": "c2", "repo": "b/b",
         "version": "2.0", "patch": "diff --git y", "hints_text": "leak", "PASS_TO_PASS": "[\"u\"]"},
        {"instance_id": "c__c-3", "problem_statement": "s3", "base_commit": "c3", "repo": "c/c",
         "version": "3.0"},
    ]
    text = project(rows, ["a__a-1", "c__c-3"])
    out = json.loads(text)
    check(len(out) == 2, "projects exactly the pilot ids (2 of 3)")
    check(all(set(r) == set(KEEP) for r in out), "every projected row is exactly the five fields")
    check("hints_text" not in text and "diff --git" not in text and "FAIL_TO_PASS" not in text,
          "no held-out field survives the projection")
    check([r["instance_id"] for r in out] == ["a__a-1", "c__c-3"], "source order is preserved, not re-sorted")
    check(text == json.dumps(out, sort_keys=True, separators=(",", ":")),
          "the emitted bytes are compact and sort_keys, as project_data.py writes them")

    # FAILING INPUTS: a pilot id the rows do not carry must raise, never write a short file
    try:
        project(rows, ["a__a-1", "zz__zz-9"])
        check(False, "a missing pilot id is refused")
    except RuntimeError:
        check(True, "a missing pilot id is refused")
    # a row missing one of the five must raise rather than emit a four-field row
    try:
        project([{"instance_id": "d__d-4", "problem_statement": "s", "base_commit": "c", "repo": "d/d"}], ["d__d-4"])
        check(False, "a row missing a projected field is refused")
    except KeyError:
        check(True, "a row missing a projected field is refused")

    # THE RECIPE must be the compact one; the indent=2 fold is a different digest and must not match
    r2 = [{"z": 1, "a": 2}]
    check(dataset_rows_sha256(r2) !=
          hashlib.sha256(json.dumps(r2, sort_keys=True, indent=2).encode("utf-8")).hexdigest(),
          "the compact recipe and the indent=2 fold differ (the recipe decides the digest)")

    # the pin reader finds a real key and rejects a prefix match
    import tempfile
    with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False) as fh:
        fh.write("other.json ab\nproblem_statements.json cd\nproblem_statements.json.bak ef\n")
        p = fh.name
    check(read_pin("problem_statements.json", p) == "cd", "the pin reader matches the whole key")
    check(read_pin("nothing.json", p) is None, "the pin reader returns None for an absent key")
    os.unlink(p)

    # the real TASKLIST.json carries the three values this script needs
    tp = os.path.join(REPO, "TASKLIST.json")
    if os.path.exists(tp):
        tl = tasklist(tp)
        check(len(tl["pilot"]) == 30, "TASKLIST.json carries the 30 pilot ids")
        check(len(tl["dataset_repo_sha"]) == 40, "TASKLIST.json carries the 40-char revision")
        check(read_pin("problem_statements.json", os.path.join(HERE, "HASHES.txt")) is not None,
              "HASHES.txt still carries the projection pin (the reconstruction's handle)")

    print("SELF-TEST", "OK" if ok else "FAILED")
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser(description="re-derive the 30 projected problem statements from the pinned revision")
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--rows", metavar="VERIFIED_JSON", help="local JSON list of the 500 dataset rows")
    ap.add_argument("--download", action="store_true", help="fetch the pinned revision with `datasets`")
    ap.add_argument("--tasklist", default=os.path.join(REPO, "TASKLIST.json"))
    ap.add_argument("--hashes", default=os.path.join(HERE, "HASHES.txt"))
    ap.add_argument("--out", default=os.path.join(HERE, "data", "problem_statements.json"))
    a = ap.parse_args()

    if a.self_test:
        return self_test()
    if bool(a.rows) == bool(a.download):
        ap.error("give exactly one of --rows <verified.json> or --download")

    tl = tasklist(a.tasklist)
    rows = json.load(open(a.rows)) if a.rows else download_rows(tl["dataset_repo_sha"])
    return run(rows, tl, a.out, a.hashes)


if __name__ == "__main__":
    sys.exit(main())
