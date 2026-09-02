#!/usr/bin/env python3
"""fencediff.py — the fence differential: every reference file run UNFENCED and FENCED, verdicts compared.

The green arm on a single fixture proves nothing about the population: my first fixture was a proof-only
file that never reached Verus's lifetime/borrow driver, and the lifetime driver execs a binary the fixture
never provoked. A whitelist is complete only over the shapes it was measured on.
"""
import json, os, re, subprocess, sys, tempfile, time

RESULTS = re.compile(r"verification results:: (\d+) verified, (\d+) errors")
V = os.path.expanduser("~/bench-src/verus-release-pin/verus-arm64-macos")
RUSTUP = subprocess.check_output(["bash", "-lc", "command -v rustup"], text=True).strip()


def profile(work, extra_execs=()):
    execs = [os.path.join(V, "verus"), RUSTUP, os.path.join(V, "rust_verify"), os.path.join(V, "z3")]
    execs += list(extra_execs)
    allow = " ".join('(literal "%s")' % e for e in execs)
    deny_read = " ".join('(subpath "%s")' % os.path.expanduser(p)
                         for p in ["~/.ssh", "~/.aws", "~/.gnupg", "~/.claude", "~/Library/Keychains"])
    return ("(version 1)\n(allow default)\n(deny network*)\n(deny process-exec*)\n"
            "(deny file-read* %s)\n(allow process-exec %s)\n"
            "(deny file-write*)\n(allow file-write* (subpath \"%s\") (literal \"/dev/null\"))\n"
            % (deny_read, allow, work))


def run(src, fenced, extra=()):
    work = tempfile.mkdtemp(prefix="fdiff.")
    open(os.path.join(work, "task.rs"), "w", encoding="utf-8").write(src)
    argv = [os.path.join(V, "verus"), "--crate-type=lib", "--rlimit", "250",
            "--smt-option", "smt.random_seed=0", "task.rs"]
    if fenced:
        argv = ["/usr/bin/sandbox-exec", "-p", profile(work, extra)] + argv
    env = dict(os.environ, TMPDIR=work)
    t0 = time.time()
    p = subprocess.run(["perl", "-e", "alarm 900; exec @ARGV"] + argv, cwd=work,
                       capture_output=True, text=True, env=env)
    line = next((l for l in p.stdout.splitlines() if l.startswith("verification results::")), None)
    m = RESULTS.search(line) if line else None
    if p.returncode == 0 and m and int(m.group(2)) == 0 and int(m.group(1)) >= 1:
        cls = "PASS"
    elif "Resource limit (rlimit) exceeded" in p.stderr:
        cls = "RLIMIT"
    elif line is None:
        cls = "COMPILE"
    else:
        cls = "VERIFY_FAIL"
    err = [l for l in (p.stderr + p.stdout).splitlines() if "error" in l.lower()][:2]
    return cls, err, round(time.time() - t0, 1)


def main():
    jsonl = os.path.expanduser("~/bench-src/verus-proof-synthesis/benchmarks/VeruSAGE-Bench/tasks.jsonl")
    limit = int(sys.argv[1]) if len(sys.argv) > 1 else 40
    recs = {json.loads(l)["task_id"]: json.loads(l) for l in open(jsonl) if l.strip()}
    ids = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "sample.json")))
    sample = [recs[i] for i in ids]
    print("SEEDED SAMPLE over AC+NR: n=%d (seed 20260902, plus the 4 exec-only records forced in)" % len(sample))
    rows, diffs = [], []
    for i, r in enumerate(sample):
        u, ue, ut = run(r["ground_truth"], False)
        f, fe, ft = run(r["ground_truth"], True)
        same = (u == f)
        rows.append(dict(task_id=r["task_id"], unfenced=u, fenced=f, same=same,
                         fenced_err=fe if not same else [], secs=[ut, ft]))
        if not same:
            diffs.append(rows[-1])
        print("%3d/%d %-8s %-8s %s %s" % (i + 1, len(sample), u, f, "OK " if same else "DIFF",
                                          r["task_id"][:60]), flush=True)
    out = dict(n=len(sample), diffs=len(diffs), rows=rows)
    json.dump(out, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "fencediff.json"), "w"), indent=1)
    print("\nFENCE DIFFERENTIAL: n=%d  agree=%d  DIFFER=%d" % (len(sample), len(sample) - len(diffs), len(diffs)))
    for d in diffs:
        print("  DIFF %s unfenced=%s fenced=%s %s" % (d["task_id"], d["unfenced"], d["fenced"], d["fenced_err"]))


if __name__ == "__main__":
    main()
