#!/usr/bin/env python3
"""mutate.py — the second probe: does CLEVER's reference checker notice when the SOLVER alters the
statement it is supposed to prove?

task.py:122-129 builds `original_problem` from the benchmark (comment: "Only change the proofs and
helper lemmas") and then task.py:134 formats `problem` — the submitted view. `original_problem` is a
dead store. We test that reading directly: resubmit each of the 15 stage-B artifacts with the
isomorphism theorem replaced by a trivially true one.

  M1 = model's own generated spec + helper lemmas kept; ONLY the theorem+proof swapped.
  M2 = M1 with helper lemmas dropped (the minimal adversarial submission).

usage: mutate.py <episodes.json> <out.json>
"""
import asyncio, json, os, sys, time

CLEVER = "/Users/jyh/s2kill/clever"
sys.path.insert(0, os.path.join(CLEVER, "src"))
from clever_bench.benchmark import Benchmark                      # noqa: E402
from clever_bench.task import ProblemViewTask, TaskComponent      # noqa: E402
from clever_bench.lean_problem import Lemma                       # noqa: E402

BENCH = "/Users/jyh/bench"
LEAN4 = os.path.join(CLEVER, "src", "lean4")
TRIVIAL_THM = "theorem spec_isomorphism : True :="
TRIVIAL_PRF = "trivial"


def load(p):
    with open(p) as f:
        return json.load(f)


def main():
    eps = load(sys.argv[1])
    outp = sys.argv[2]
    benchmark = Benchmark(is_sample=False)
    benchmark.load_all()
    task = ProblemViewTask(benchmark, TaskComponent.SPEC_ISOMORPHISM,
                           lean_folder=LEAN4, report_dir="/Users/jyh/s2kill/reports-mut")

    rows = []
    for e in eps:
        pid, ep = e["pid"], e["ep"]
        frozen = load(f"{BENCH}/s2views/problem_{pid}/frozen.json")
        abodies = load(f"{BENCH}/state/s2/problem_{pid}/a0/A.bodies.json")
        bbodies = load(f"{BENCH}/state/{ep}/bodies.json")
        gen_full = frozen["generated_spec_header"] + "\n" + ((abodies.get("generated_spec_body") or "").strip() or "sorry")
        iso_help = (bbodies.get("iso_helper_lemmas") or "").strip()

        row = dict(pid=pid, ep=ep, our_class=e["our_class"])
        for tag, keep_helpers in (("M1", True), ("M2", False)):
            v = task.get_view(pid)
            v.problem_spec_formal_generated = gen_full
            v.isomorphism_theorem = TRIVIAL_THM
            v.isomorphism_proof = TRIVIAL_PRF
            v.isomorphism_helper_lemmas = ([Lemma(statement=iso_help, proof="")]
                                           if (keep_helpers and iso_help) else [])
            t0 = time.time()
            r = asyncio.run(task.submit_async(v, timeout_in_ms=600000))
            row[tag] = dict(iso_ok=r.isomorphism_ok, compile_ok=r.compilation_ok,
                            err=(r.error_message or "")[-200:], wall_s=round(time.time() - t0, 1))
            os.makedirs(f"/Users/jyh/s2kill/mutated/{tag}", exist_ok=True)
            with open(f"/Users/jyh/s2kill/mutated/{tag}/problem_{pid}.lean", "w") as f:
                f.write(r.lean_code or "")
        print("problem_%-4s ours=%-12s  M1 iso_ok=%-5s  M2 iso_ok=%-5s"
              % (pid, e["our_class"], row["M1"]["iso_ok"], row["M2"]["iso_ok"]), flush=True)
        rows.append(row)

    with open(outp, "w") as f:
        json.dump(rows, f, indent=1)
    for tag in ("M1", "M2"):
        print("=== %s: CLEVER's checker certified %d/%d" % (tag, sum(1 for r in rows if r[tag]["iso_ok"]), len(rows)))


if __name__ == "__main__":
    main()
