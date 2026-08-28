#!/usr/bin/env python3
"""build_prompt.py — build an episode's prompt and arm file from the pinned dataset.

    ARM_FOR_BUILD=<a0|a1|...> build_prompt.py --instance <id> --ep <EPROOT/ep-xxxx> --out <STATE/ep-xxxx>
    (the arm arrives in the ENVIRONMENT, never argv, and is written to NO file here — refuter F1)
    build_prompt.py --self-test

THE ONLY DATASET FIELD THAT LEAVES THIS PROCESS IS `problem_statement` (DESIGN §4 CHECK 1, applied
to the prompt builder). During episodes the Studio holds only the PROJECTION data/problem_statements.json
(no patch/test_patch/hints/F2P/P2P bytes exist on the host at all); the builder still refuses a leak if
handed a full row. A self-test drives
the failing input: a prompt that contains any byte of `patch`, `test_patch`, `hints_text`,
FAIL_TO_PASS or PASS_TO_PASS raises.
"""
import argparse, hashlib, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
FORBIDDEN = ("patch", "test_patch", "hints_text", "FAIL_TO_PASS", "PASS_TO_PASS")


def sha(b):
    return hashlib.sha256(b).hexdigest()


def load_row(instance_id, data_path):
    rows = json.load(open(data_path))
    hits = [r for r in rows if r["instance_id"] == instance_id]
    if len(hits) != 1:
        raise SystemExit("instance %s: %d rows" % (instance_id, len(hits)))
    return hits[0]


def render(problem_statement, arm, ep, row_for_check=None, arms_dir=None):
    arms_dir = arms_dir or os.path.join(HERE, "arms")
    tmpl = open(os.path.join(HERE, "prompt.md")).read()
    base = open(os.path.join(HERE, "base.md")).read()
    arm_block = open(os.path.join(arms_dir, arm + ".md")).read()
    prompt = tmpl.replace("__EP__", ep).replace("__PROBLEM_STATEMENT__", problem_statement)
    claude_md = base.replace("__EP__", ep) + arm_block
    if row_for_check is not None:
        # the failing input this builder exists to refuse: held-out material in the prompt or arm
        for f in FORBIDDEN:
            v = row_for_check.get(f)
            if isinstance(v, str) and len(v.strip()) >= 20 and (v.strip() in prompt or v.strip() in claude_md):
                raise RuntimeError("LEAK: dataset field %r appears in the rendered prompt/arm" % f)
        # ids inside the JSON-encoded lists, individually
        for f in ("FAIL_TO_PASS", "PASS_TO_PASS"):
            v = row_for_check.get(f)
            ids = json.loads(v) if isinstance(v, str) else (v or [])
            for i in ids:
                if len(i) >= 12 and (i in prompt or i in claude_md):
                    raise RuntimeError("LEAK: test id %r appears in the rendered prompt/arm" % i)
    return prompt, claude_md


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--instance"); ap.add_argument("--ep"); ap.add_argument("--out")
    ap.add_argument("--data", default=os.path.join(HERE, "data", "problem_statements.json"))
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args()
    if a.self_test:
        return self_test()
    arm = os.environ.get("ARM_FOR_BUILD")
    if not arm:
        raise SystemExit("ARM_FOR_BUILD must be set in the environment")
    row = load_row(a.instance, a.data)
    ps = row["problem_statement"]
    prompt, claude_md = render(ps, arm, a.ep, row_for_check=row)
    canonical = open(os.path.join(HERE, "prompt.md")).read().replace("__PROBLEM_STATEMENT__", ps)
    os.makedirs(a.out, exist_ok=True)
    open(os.path.join(a.out, "prompt.md"), "w").write(prompt)
    open(os.path.join(a.ep, "CLAUDE.md"), "w").write(claude_md)
    # NO arm-identifying field is written here; finish() in episode.sh adds them after the agent has exited
    meta = {
        "instance_id": a.instance, "ep": a.ep,
        "prompt_sha256": sha(prompt.encode()), "prompt_sha256_canonical": sha(canonical.encode()), "prompt_bytes": len(prompt.encode()),
        "problem_statement_sha256": sha(ps.encode()),
        "base_commit": row["base_commit"], "repo": row["repo"], "version": row.get("version"),
    }
    json.dump(meta, open(os.path.join(a.out, "prompt_meta.json"), "w"), indent=1, sort_keys=True)
    print(json.dumps(meta, sort_keys=True))
    return 0


def self_test():
    ok = True
    def check(cond, msg):
        nonlocal ok
        print(("PASS " if cond else "FAIL ") + msg); ok = ok and cond
    row = {"instance_id": "x__y-1", "problem_statement": "The frobnicator returns None when given [].",
           "patch": "diff --git a/f.py b/f.py\n-return None\n+return []\n", "test_patch": "diff --git a/t.py b/t.py\n+def test_frob_empty(): pass\n",
           "hints_text": "The maintainer suggests routing the kwarg through frob_impl instead.",
           "FAIL_TO_PASS": json.dumps(["t.py::test_frob_empty_list_case"]), "PASS_TO_PASS": json.dumps(["t.py::test_frob_other_case"])}
    p, c = render(row["problem_statement"], "a0", "/E", row_for_check=row)
    check(row["problem_statement"] in p and "/E/rt" in c, "clean row renders; base block carries the wrapper path")
    check("hints" not in p.lower() and "patch" not in p.lower(), "prompt carries only the problem statement")
    p1, c1 = render(row["problem_statement"], "a1", "/E", row_for_check=row)
    check(c1.startswith(c) and len(c1) > len(c), "a1 = a0 base + a non-empty arm block (byte-identical prefix)")
    # FAILING INPUTS: each forbidden field, smuggled into the statement, must raise
    for f in FORBIDDEN:
        v = row[f]
        try:
            render(row["problem_statement"] + "\n" + (v if f not in ("FAIL_TO_PASS", "PASS_TO_PASS") else json.loads(v)[0]), "a0", "/E", row_for_check=row)
            check(False, "leak of %s NOT refused" % f)
        except RuntimeError:
            check(True, "leak of %s refused" % f)
    # the arm dir must contain no arm named by its meaning (arm-blindness on disk)
    names = sorted(os.listdir(os.path.join(HERE, "arms")))
    check(all(n[0] in "as" and n[1:-3].isdigit() and n.endswith(".md") for n in names), "arm files are opaquely named: %s" % names)
    # the projection carries no held-out field
    pp = os.path.join(HERE, "data", "problem_statements.json")
    if os.path.exists(pp):
        rows = json.load(open(pp))
        check(all(set(r) == {"instance_id", "problem_statement", "base_commit", "repo", "version"} for r in rows), "problem_statements.json holds exactly the five projected fields (%d rows)" % len(rows))
    # every __EP__/<name> the prompt and base block mention must be an entry episode.sh asserts (CLAUDE.md repo rt)
    import re as _re
    names = {n.rstrip(".") for n in _re.findall(r"__EP__/([A-Za-z0-9_.-]+)", open(os.path.join(HERE, "prompt.md")).read() + open(os.path.join(HERE, "base.md")).read())}
    check(names <= {"CLAUDE.md", "repo", "rt"}, "prompt/base name only episode-dir entries: %s" % sorted(names))
    # a1 (placebo) carries no verification vocabulary
    a1 = open(os.path.join(HERE, "arms", "a1.md")).read().lower()
    bad = [w for w in ("test", "reproduce", "verify", "verif", "spec", "propert", "checker", "proof", "prove", "statement", "assert", "expected") if w in a1]
    check(not bad, "a1 placebo carries none of the verification vocabulary: %s" % bad)
    print("SELF-TEST", "OK" if ok else "FAILED")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
