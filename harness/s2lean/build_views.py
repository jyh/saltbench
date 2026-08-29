#!/usr/bin/env python3
"""build_views.py — the ONLY code that reads a raw CLEVER problem file (a full solution) and emits what the agent
may see. Per problem k it writes, under <out>/problem_k/:
  A.lean         stage A view: NL spec + `generated_spec` header with body `sorry` (ground-truth spec, implementation,
                 proofs ABSENT — the agent writes the spec blind to the hidden human spec)
  C.lean         stage C view: NL spec + ground-truth `problem_spec` + `implementation` signature with body `sorry` +
                 test cases (uncommented, as the reference view does) + `correctness` theorem with proof `sorry`
                 (no generated spec, no isomorphism, no proofs, no helper lemmas)
  frozen.json    every STATEMENT the agent may not change, verbatim: generated_spec header, isomorphism theorem,
                 problem_spec (GT), implementation signature, correctness theorem, test cases — plus the NL spec
B.lean is assembled later by assemble.py from frozen.json + the agent's stage-A `generated_spec` body.
The ground-truth spec is in frozen.json and C.lean; those files are shipped to the Studio ONLY after all stage-A
episodes have landed (SCOUT-S2LEAN-STAGE0 §2). Self-test: --self-test parses the clone and round-trips problem 0.
usage: build_views.py <clever-clone>/src/lean4 <out-dir> [--self-test]
"""
import json, os, re, sys

SEC = re.compile(r"--\s*start_def\s+(\w+)\s*[\r\n]+(.*?)--\s*end_def\s+\1", re.DOTALL | re.IGNORECASE)

def sections(text):
    out = {}
    for m in SEC.finditer(text):
        out.setdefault(m.group(1).strip(), []).append(m.group(2).strip())
    return out

def first(s, k):
    v = s.get(k); return v[0] if v else None

def nl_spec(details):
    # the reference builds `function_signature\n"""docstring"""` from the YAML; we keep the WHOLE docstring block
    # verbatim (signature, docstring, test cases in YAML) so the agent sees exactly what the reference view carries
    m = re.search(r"/--(.*?)-/", details, re.DOTALL)
    return m.group(1).strip() if m else details.strip()

def uncomment_tests(t):
    if not t: return None
    lines = [l.strip() for l in t.splitlines() if l.strip()]
    return "\n".join(l[2:].strip() if l.startswith("--") else l for l in lines)

def build(problem_path):
    txt = open(problem_path, encoding="utf-8").read()
    s = sections(txt)
    gen = first(s, "generated_spec")            # header ending in ':= ' — the body section is separate
    gen_body = first(s, "generated_spec_body")  # 'sorry' in the shipped files
    fz = {
        "problem_id": int(os.path.basename(problem_path).split("_")[1].split(".")[0]),
        "nl": nl_spec(first(s, "problem_details") or ""),
        "problem_spec": first(s, "problem_spec"),
        "generated_spec_header": gen,
        "isomorphism_theorem": first(s, "spec_isomorphism"),
        "implementation_signature": first(s, "implementation_signature"),
        "test_cases": uncomment_tests(first(s, "test_cases")),
        "correctness_theorem": first(s, "correctness_definition"),
        "shipped_generated_spec_body": gen_body,
    }
    for k in ("problem_spec", "generated_spec_header", "isomorphism_theorem", "implementation_signature", "correctness_theorem"):
        assert fz[k], "problem %s lacks %s" % (fz["problem_id"], k)
    hdr = "import Imports.AllImports\n\n/--\n%s\n-/\n" % fz["nl"]
    A = hdr + ("\n-- start_def generated_spec\n%s\n-- end_def generated_spec\n-- start_def generated_spec_body\nsorry\n-- end_def generated_spec_body\n" % gen)
    C = hdr + ("\n-- start_def problem_spec\n%s\n-- end_def problem_spec\n\n-- start_def implementation_signature\n%s\n-- end_def implementation_signature\n-- start_def implementation\nsorry\n-- end_def implementation\n\n-- start_def test_cases\n%s\n-- end_def test_cases\n\n-- start_def correctness_helper_lemmas\n-- end_def correctness_helper_lemmas\n\n-- start_def correctness_definition\n%s\n-- end_def correctness_definition\n-- start_def correctness_proof\nby sorry\n-- end_def correctness_proof\n"
               % (fz["problem_spec"], fz["implementation_signature"], fz["test_cases"] or "", fz["correctness_theorem"]))
    return fz, A, C

def assemble_B(fz, generated_spec_body):
    hdr = "import Imports.AllImports\n\n/--\n%s\n-/\n" % fz["nl"]
    return hdr + ("\n-- start_def generated_spec\n%s\n-- end_def generated_spec\n-- start_def generated_spec_body\n%s\n-- end_def generated_spec_body\n\n-- start_def problem_spec\n%s\n-- end_def problem_spec\n\n-- start_def iso_helper_lemmas\n-- end_def iso_helper_lemmas\n\n-- start_def spec_isomorphism\n%s\n-- end_def spec_isomorphism\n-- start_def spec_isomorphism_proof\nby sorry\n-- end_def spec_isomorphism_proof\n"
                  % (fz["generated_spec_header"], generated_spec_body.strip(), fz["problem_spec"], fz["isomorphism_theorem"]))

def main():
    if "--self-test" in sys.argv:
        root = sys.argv[1]; ok = True
        files = sorted(os.listdir(os.path.join(root, "human_eval")))
        n = 0
        for f in files:
            fz, A, C = build(os.path.join(root, "human_eval", f)); n += 1
            for leak in (first(sections(open(os.path.join(root, "human_eval", f)).read()), "implementation"), first(sections(open(os.path.join(root, "human_eval", f)).read()), "correctness_proof")):
                if leak and len(leak) > 40 and (leak in A or leak in C):
                    print("FAIL leak in views of", f); ok = False
            if fz["problem_spec"] in A:
                print("FAIL ground-truth spec present in stage-A view of", f); ok = False
            if "sorry" not in A or "sorry" not in C:
                print("FAIL a view lacks its sorry:", f); ok = False
        print("PASS %d problems parsed; no implementation/proof/GT-spec leak into A; C carries GT spec by design" % n if ok else "FAILED")
        B = assemble_B(*build(os.path.join(root, "human_eval", "problem_0.lean"))[:1], "True")
        print("PASS B assembles" if "spec_isomorphism" in B and "problem_spec" in B else "FAIL B")
        return 0 if ok else 1
    root, out = sys.argv[1], sys.argv[2]
    for f in sorted(os.listdir(os.path.join(root, "human_eval"))):
        fz, A, C = build(os.path.join(root, "human_eval", f))
        d = os.path.join(out, "problem_%d" % fz["problem_id"]); os.makedirs(d, exist_ok=True)
        open(os.path.join(d, "A.lean"), "w").write(A); open(os.path.join(d, "C.lean"), "w").write(C)
        json.dump(fz, open(os.path.join(d, "frozen.json"), "w"), indent=1, sort_keys=True)
        # the GROUND-TRUTH-FREE frozen file for stage A (the only frozen file on the Studio while stage A runs)
        json.dump({k: fz[k] for k in ("problem_id", "nl", "generated_spec_header")}, open(os.path.join(d, "frozenA.json"), "w"), indent=1, sort_keys=True)
    print("views written to", out)
    return 0

if __name__ == "__main__":
    sys.exit(main())
