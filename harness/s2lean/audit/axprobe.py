#!/usr/bin/env python3
"""axprobe.py — the third probe: the missing axiom audit, with the STATEMENT LEFT UNTOUCHED.

The mutation probe altered the theorem. This one does not touch it. It submits, as an isomorphism
helper lemma, a single universally-false axiom

    axiom cheat (P : Prop) : P

and discharges the untouched isomorphism theorem with `cheat _`. The file compiles, Lean emits no
"declaration uses 'sorry'" (an `axiom` is not a sorry), so CLEVER's log grep sees nothing. Only
`#print axioms spec_isomorphism` shows it. This is the gap the SaltBench checker's axiom allowlist
{propext, Classical.choice, Quot.sound} exists to close.

usage: axprobe.py <episodes.json> <out.json>
"""
import asyncio, json, os, subprocess, sys, time

CLEVER = "/Users/jyh/s2kill/clever"
sys.path.insert(0, os.path.join(CLEVER, "src"))
from clever_bench.benchmark import Benchmark                      # noqa: E402
from clever_bench.task import ProblemViewTask, TaskComponent      # noqa: E402
from clever_bench.lean_problem import Lemma                       # noqa: E402

BENCH = "/Users/jyh/bench"
LEAN4 = os.path.join(CLEVER, "src", "lean4")
CHEAT = "axiom cheat (P : Prop) : P"


def load(p):
    with open(p) as f:
        return json.load(f)


def main():
    eps = load(sys.argv[1])
    outp = sys.argv[2]
    benchmark = Benchmark(is_sample=False)
    benchmark.load_all()
    task = ProblemViewTask(benchmark, TaskComponent.SPEC_ISOMORPHISM,
                           lean_folder=LEAN4, report_dir="/Users/jyh/s2kill/reports-ax")
    os.makedirs("/Users/jyh/s2kill/axiomed", exist_ok=True)

    rows = []
    for e in eps:
        pid = e["pid"]
        frozen = load(f"{BENCH}/s2views/problem_{pid}/frozen.json")
        abodies = load(f"{BENCH}/state/s2/problem_{pid}/a0/A.bodies.json")
        gen_full = frozen["generated_spec_header"] + "\n" + ((abodies.get("generated_spec_body") or "").strip() or "sorry")

        v = task.get_view(pid)
        v.problem_spec_formal_generated = gen_full
        v.isomorphism_helper_lemmas = [Lemma(statement=CHEAT, proof="")]
        v.isomorphism_proof = "cheat _"
        # v.isomorphism_theorem is left exactly as their benchmark produced it
        thm_untouched = (v.isomorphism_theorem or "").strip() == frozen["isomorphism_theorem"].strip()

        t0 = time.time()
        r = asyncio.run(task.submit_async(v, timeout_in_ms=600000))
        wall = round(time.time() - t0, 1)
        path = f"/Users/jyh/s2kill/axiomed/problem_{pid}.lean"
        with open(path, "w") as f:
            f.write(r.lean_code or "")

        # what an axiom audit would have seen, run separately on the same file
        audit = ""
        if r.compilation_ok:
            ap = f"/Users/jyh/s2kill/clever/src/lean4/temp/audit_{pid}.lean"
            with open(ap, "w") as f:
                f.write((r.lean_code or "") + "\n\n#print axioms spec_isomorphism\n")
            p = subprocess.run(["lake", "lean", f"temp/audit_{pid}.lean"], cwd=LEAN4,
                               capture_output=True, text=True, timeout=600)
            audit = " | ".join(l.strip() for l in p.stdout.splitlines() if "axiom" in l.lower())[:300]
            os.remove(ap)

        rows.append(dict(pid=pid, our_class=e["our_class"], thm_untouched=thm_untouched,
                         their_iso_ok=r.isomorphism_ok, their_compile_ok=r.compilation_ok,
                         their_error=(r.error_message or "")[-200:], axiom_audit=audit, wall_s=wall))
        print("problem_%-4s thm_untouched=%-5s  theirs: iso_ok=%-5s  |  axiom audit: %s"
              % (pid, thm_untouched, r.isomorphism_ok, audit[:120]), flush=True)

    with open(outp, "w") as f:
        json.dump(rows, f, indent=1)
    print("=== CLEVER's checker certified %d/%d with an untouched statement and a false axiom"
          % (sum(1 for r in rows if r["their_iso_ok"]), len(rows)))


if __name__ == "__main__":
    main()
