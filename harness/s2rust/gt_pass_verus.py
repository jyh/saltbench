#!/usr/bin/env python3
"""gt_pass_verus.py — THE GROUND-TRUTH PASS (protocol §4 (b'), §8.4). Runs on the SEAT (it needs ground
truth) and produces `task_dead.json` in the `c_dead` shape, pre-registered before any scored episode.

⛔ THE VERDICT IS A THREE-WAY DIFFERENTIAL, NOT A PASS/FAIL. Amendment 15 §4 registered a two-way
(standalone vs scaffold); the first real run showed two DISTINCT causes hiding behind one FAIL, so the
DIRECT-SPLICE control is the third leg and it is what exonerates or indicts our own assembler:

  standalone  splice  scaffold   verdict
  ----------  ------  --------   --------------------------------------------------------------
     PASS      PASS    PASS      LIVE — the task is drawable
     PASS      FAIL    FAIL      TASK_CONTEXT_INCOMPLETE — the record's `task` omits context its own
                                 `ground_truth` supplies; unsolvable by ANY agent; REMOVED from the draw
     PASS      PASS    FAIL      SCAFFOLD_DEFECT — ours. LOUD, BLOCKING, never a task property.
     FAIL       -       -        COMPILE => PIN DEFECT (blocking, §5) ; otherwise TASK_DEAD

  standalone = the benchmark's own `ground_truth` file, verbatim
  splice     = the reference body spliced into the benchmark's own `task` file, no markers, no scaffold
  scaffold   = assemble(frozen, {proof: reference body}) — ours

A front-end error on a REFERENCE file indicts the toolchain, never the task (§5): `COMPILE` is counted
separately and a non-zero count blocks.

usage: gt_pass_verus.py <tasks.jsonl> <viewsdir> <verus> [--rlimit N] [--seed N] [--limit N] [--out F]
"""
import json, os, re, subprocess, shutil, sys, tempfile, time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_views_verus as B
import rustspan

RESULTS = re.compile(r"verification results:: (\d+) verified, (\d+) errors")


def referee(verus, src, work, rlimit, seed, timeout=900):
    open(os.path.join(work, "task.rs"), "w", encoding="utf-8").write(src)
    p = subprocess.run(["perl", "-e", "alarm %d; exec @ARGV" % timeout, verus, "--crate-type=lib",
                        "--rlimit", str(rlimit), "--smt-option", "smt.random_seed=%d" % seed, "task.rs"],
                       cwd=work, capture_output=True, text=True)
    line = next((l for l in p.stdout.splitlines() if l.startswith("verification results::")), None)
    m = RESULTS.search(line) if line else None
    if p.returncode == 0 and m and int(m.group(2)) == 0 and int(m.group(1)) >= 1:
        cls = "PASS"
    elif "Resource limit (rlimit) exceeded" in p.stderr:
        cls = "RLIMIT"
    elif line is None:
        cls = "COMPILE"          # no results line at all => the front end refused it
    else:
        cls = "VERIFY_FAIL"
    errs = [l for l in p.stderr.splitlines() if l.startswith("error")][:3]
    return dict(cls=cls, rc=p.returncode, results_line=line, errors=errs)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if len(args) != 3:
        sys.exit(__doc__)
    jsonl, viewsdir, verus = args
    def opt(name, dflt, cast=int):
        for a in sys.argv[1:]:
            if a.startswith("--%s=" % name):
                return cast(a.split("=", 1)[1])
        return dflt
    rlimit, seed = opt("rlimit", 250), opt("seed", 0)
    limit, out = opt("limit", 0), opt("out", os.path.join(viewsdir, "task_dead.json"), str)

    have = {d for d in os.listdir(os.path.join(viewsdir, "views"))}
    work = tempfile.mkdtemp(prefix="gtpass.")
    rows, tally = [], {}
    t_all = time.time()
    n = 0
    for line in open(jsonl, encoding="utf-8"):
        rec = json.loads(line)
        tid = rec["task_id"]
        if tid not in have:
            continue
        n += 1
        if limit and n > limit:
            break
        fz = json.load(open(os.path.join(viewsdir, "views", tid, "frozen.json")))
        gt = json.load(open(os.path.join(viewsdir, "gt", tid + ".json")))
        t0 = time.time()
        standalone = referee(verus, rec["ground_truth"], work, rlimit, seed)
        if standalone["cls"] != "PASS":
            verdict = "PIN_DEFECT" if standalone["cls"] == "COMPILE" else "TASK_DEAD"
            row = dict(task_id=tid, verdict=verdict, standalone=standalone, splice=None, scaffold=None)
        else:
            scaffold = referee(verus, B.assemble(fz, gt), work, rlimit, seed)
            if scaffold["cls"] == "PASS":
                row = dict(task_id=tid, verdict="LIVE", standalone=standalone, splice=None, scaffold=scaffold)
            else:
                src = rec["task"]
                _, incode = rustspan.code_map(src)
                it = [x for x in B.find_targets(src, rec["target_function"], incode)
                      if "unimplemented!()" not in x["body"]][0]
                direct = src[:it["body_open"] + 1] + gt["proof"] + src[it["body_close"]:]
                splice = referee(verus, direct, work, rlimit, seed)
                verdict = "TASK_CONTEXT_INCOMPLETE" if splice["cls"] != "PASS" else "SCAFFOLD_DEFECT"
                row = dict(task_id=tid, verdict=verdict, standalone=standalone, splice=splice, scaffold=scaffold)
        row["seconds"] = round(time.time() - t0, 1)
        rows.append(row)
        tally[row["verdict"]] = tally.get(row["verdict"], 0) + 1
        print("%4d %-24s %6.1fs %s" % (len(rows), row["verdict"], row["seconds"], tid[:58]), flush=True)
    shutil.rmtree(work, ignore_errors=True)
    report = dict(rlimit=rlimit, seed=seed, verus=verus, n=len(rows), tally=tally,
                  wall_s=round(time.time() - t_all, 1), rows=rows)
    json.dump(report, open(out, "w"), indent=1)
    print("\nTALLY", json.dumps(tally))
    print("dead-list written to", out)
    if tally.get("SCAFFOLD_DEFECT"):
        print("⛔ SCAFFOLD_DEFECT present — BLOCKING, this is ours")
    if tally.get("PIN_DEFECT"):
        print("⛔ PIN_DEFECT present — BLOCKING, a front-end error on a reference file indicts the toolchain")


if __name__ == "__main__":
    main()
