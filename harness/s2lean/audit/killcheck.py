#!/usr/bin/env python3
"""killcheck.py — run CLEVER's OWN reference checker (clever_bench.task.ProblemViewTask.submit_async,
the entry point its README documents for submissions) over SaltBench's 15 stage-B a0 artifacts.

Nothing of ours decides anything here: their Benchmark parses their human_eval files, their get_view
builds the SPEC_ISOMORPHISM view, and we inject ONLY the three fields a solver is supposed to fill
(generated spec, isomorphism proof, isomorphism helper lemmas). Their code assembles, compiles and
scores. We record isomorphism_ok beside our own checker's class.

usage: killcheck.py <episodes.json> <out.json>
"""
import asyncio, json, os, sys, time

CLEVER = "/Users/jyh/s2kill/clever"
sys.path.insert(0, os.path.join(CLEVER, "src"))
from clever_bench.benchmark import Benchmark                      # noqa: E402
from clever_bench.task import ProblemViewTask, TaskComponent      # noqa: E402
from clever_bench.lean_problem import Lemma                       # noqa: E402

BENCH = "/Users/jyh/bench"
LEAN4 = os.path.join(CLEVER, "src", "lean4")


def load(p):
    with open(p) as f:
        return json.load(f)


def main():
    eps = load(sys.argv[1])
    outp = sys.argv[2]

    benchmark = Benchmark(is_sample=False)
    benchmark.load_all()
    print("their benchmark loaded: %d problems" % len(benchmark.problems), flush=True)
    task = ProblemViewTask(benchmark, TaskComponent.SPEC_ISOMORPHISM,
                           lean_folder=LEAN4, report_dir="/Users/jyh/s2kill/reports")

    rows = []
    for e in eps:
        pid, ep = e["pid"], e["ep"]
        frozen = load(f"{BENCH}/s2views/problem_{pid}/frozen.json")
        abodies = load(f"{BENCH}/state/s2/problem_{pid}/a0/A.bodies.json")
        bbodies = load(f"{BENCH}/state/{ep}/bodies.json")

        gen_body = (abodies.get("generated_spec_body") or "").strip() or "sorry"
        gen_full = frozen["generated_spec_header"] + "\n" + gen_body
        iso_proof = (bbodies.get("spec_isomorphism_proof") or "").strip() or None
        iso_help = (bbodies.get("iso_helper_lemmas") or "").strip()

        view = task.get_view(pid)
        # statement fidelity between their view builder and ours, recorded not assumed
        same_thm = (view.isomorphism_theorem or "").strip() == frozen["isomorphism_theorem"].strip()
        same_gt = (view.problem_spec_formal_ground_truth or "").strip() == frozen["problem_spec"].strip()

        view.problem_spec_formal_generated = gen_full
        view.isomorphism_proof = iso_proof
        view.isomorphism_helper_lemmas = [Lemma(statement=iso_help, proof="")] if iso_help else []

        t0 = time.time()
        r = asyncio.run(task.submit_async(view, timeout_in_ms=600000))
        wall = round(time.time() - t0, 1)

        os.makedirs("/Users/jyh/s2kill/submitted", exist_ok=True)
        with open(f"/Users/jyh/s2kill/submitted/problem_{pid}.lean", "w") as f:
            f.write(r.lean_code or "")

        row = dict(pid=pid, ep=ep, our_class=e["our_class"], our_passed=e["our_passed"],
                   their_isomorphism_ok=r.isomorphism_ok, their_compilation_ok=r.compilation_ok,
                   their_error=(r.error_message or "")[-400:], wall_s=wall,
                   their_thm_matches_ours=same_thm, their_gt_matches_ours=same_gt,
                   iso_proof_submitted=iso_proof, iso_helper_bytes=len(iso_help))
        rows.append(row)
        print("problem_%-4s %-12s ours=%-12s theirs: iso_ok=%-5s compile_ok=%-5s (%ss)"
              % (pid, ep, e["our_class"], r.isomorphism_ok, r.compilation_ok, wall), flush=True)

    with open(outp, "w") as f:
        json.dump(rows, f, indent=1)

    agree = sum(1 for r in rows if r["their_isomorphism_ok"] == r["our_passed"])
    print("\n=== THEIR CHECKER: %d/%d isomorphism_ok" % (sum(1 for r in rows if r["their_isomorphism_ok"]), len(rows)))
    print("=== OUR CHECKER:   %d/%d passed" % (sum(1 for r in rows if r["our_passed"]), len(rows)))
    print("=== AGREEMENT:     %d/%d" % (agree, len(rows)))


if __name__ == "__main__":
    main()
