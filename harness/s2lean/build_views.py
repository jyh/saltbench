#!/usr/bin/env python3
"""build_views.py — the ONLY code that reads a raw CLEVER problem file and emits what the agent may see. Per problem k
it writes, under <out>/problem_k/:
  A.lean         stage A view: preamble + NL spec + `generated_spec` header with body `sorry` (ground-truth spec,
                 implementation, proofs ABSENT — the agent writes the spec blind to the hidden human spec)
  C.lean         stage C view: preamble + NL spec + ground-truth `problem_spec` + `implementation` signature with body
                 `sorry` + test cases (uncommented, as CLEVER's reference view does) + `correctness` theorem with proof
                 `sorry` (no generated spec, no isomorphism, no proofs, no helper lemmas)
  frozen.json    every STATEMENT the agent may not change, verbatim: generated_spec header, isomorphism theorem,
                 problem_spec (GT), implementation signature, correctness theorem, test cases — plus the NL spec and the
                 PREAMBLE (repair D7): every non-blank, non-comment line of the raw file that lies OUTSIDE the marked
                 sections, except `import Imports.AllImports` (re-emitted by every file) — verbatim, in order, as one
                 string; the key is PRESENT ONLY WHEN NON-EMPTY (consumers read frozen.get("preamble", "")), so the
                 158 residue-free problems' frozen files are byte-identical to the pre-repair ones. At the pinned
                 commit: problem_62 `noncomputable def check_derivative …`,
                 problem_99 / problem_110 `import Std`. Every view and every canonical/pristine file emits it right
                 after the import line (assemble.py reads frozen["preamble"]); frozenA.json carries it too (stage A
                 checks against frozenA.json).
  frozenA.json   the ground-truth-free frozen file for stage A (problem_id, nl, generated_spec_header, preamble)
B.lean is assembled later by assemble.py / assemble_B from frozen.json + the agent's stage-A `generated_spec` body.
The docstring block (problem_details) is kept verbatim, CLEVER's view. Tests stay uncommented, as CLEVER ships them.
Self-test: --self-test parses the clone, asserts the preamble-bearing set is exactly {62, 99, 110}, that every raw
out-of-section code line is in the preamble, that the preamble reaches A, C and B, and the leak checks.
usage: build_views.py <clever-clone>/src/lean4 <out-dir> [--self-test]
"""
import json, os, re, sys

SEC = re.compile(r"--\s*start_def\s+(\w+)\s*[\r\n]+(.*?)--\s*end_def\s+\1", re.DOTALL | re.IGNORECASE)
START = re.compile(r"--\s*start_def\s+(\w+)\s*$", re.IGNORECASE)
END = re.compile(r"--\s*end_def\s+(\w+)\s*$", re.IGNORECASE)
IMPORT_LINE = "import Imports.AllImports"
EXPECTED_PREAMBLE_IDS = {62, 99, 110}

def sections(text):
    out = {}
    for m in SEC.finditer(text):
        out.setdefault(m.group(1).strip(), []).append(m.group(2).strip())
    return out

def first(s, k):
    v = s.get(k); return v[0] if v else None

def preamble(text):
    """the out-of-section residue, LINE-WISE (a marker line such as `--- start_def x` is a marker, not residue):
    lines outside every start_def..end_def span that are non-blank, not `--` comments, not inside a `/- -/` block
    and not the AllImports import — verbatim, in order, joined by newlines"""
    out, inside, block, names = [], None, False, []
    for line in text.splitlines():
        if inside is None:
            m = START.search(line)
            if m:
                inside = m.group(1).lower(); names.append(inside); continue
            s = line.strip()
            if block:
                if "-/" in s: block = False
                continue
            if not s or s == IMPORT_LINE: continue
            if s.startswith("--"): continue
            if s.startswith("/-"):
                if "-/" not in s: block = True
                continue
            out.append(line.rstrip("\r"))
        else:
            m = END.search(line)
            if m and m.group(1).lower() == inside: inside = None
    assert inside is None, "unterminated section %s" % inside
    return "\n".join(out), names

def nl_spec(details):
    # CLEVER's reference view builds `function_signature\n"""docstring"""` from the YAML; we keep the WHOLE docstring
    # block verbatim (signature, docstring, test cases in YAML) so the agent sees exactly what the reference view carries
    m = re.search(r"/--(.*?)-/", details, re.DOTALL)
    return m.group(1).strip() if m else details.strip()

def uncomment_tests(t):
    if not t: return None
    lines = [l.strip() for l in t.splitlines() if l.strip()]
    return "\n".join(l[2:].strip() if l.startswith("--") else l for l in lines)

def header(fz):
    """`import Imports.AllImports` NL preamble NL `/-- nl -/` — the layout every view and canonical file shares"""
    pre = fz.get("preamble") or ""
    return IMPORT_LINE + "\n" + (pre + "\n" if pre else "") + "\n/--\n%s\n-/\n" % fz["nl"]

def build(problem_path):
    txt = open(problem_path, encoding="utf-8").read()
    s = sections(txt)
    pre, names = preamble(txt)
    assert len(names) == sum(len(v) for v in s.values()), "section count mismatch (regex vs line scan) in %s" % problem_path
    gen = first(s, "generated_spec")            # header ending in ':=' — the body section is separate
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
    if pre: fz["preamble"] = pre
    for k in ("problem_spec", "generated_spec_header", "isomorphism_theorem", "implementation_signature", "correctness_theorem"):
        assert fz[k], "problem %s lacks %s" % (fz["problem_id"], k)
    hdr = header(fz)
    A = hdr + ("\n-- start_def generated_spec\n%s\n-- end_def generated_spec\n-- start_def generated_spec_body\nsorry\n-- end_def generated_spec_body\n" % gen)
    C = hdr + ("\n-- start_def problem_spec\n%s\n-- end_def problem_spec\n\n-- start_def implementation_signature\n%s\n-- end_def implementation_signature\n-- start_def implementation\nsorry\n-- end_def implementation\n\n-- start_def test_cases\n%s\n-- end_def test_cases\n\n-- start_def correctness_helper_lemmas\n-- end_def correctness_helper_lemmas\n\n-- start_def correctness_definition\n%s\n-- end_def correctness_definition\n-- start_def correctness_proof\nby sorry\n-- end_def correctness_proof\n"
               % (fz["problem_spec"], fz["implementation_signature"], fz["test_cases"] or "", fz["correctness_theorem"]))
    return fz, A, C

def assemble_B(fz, generated_spec_body):
    return header(fz) + ("\n-- start_def generated_spec\n%s\n-- end_def generated_spec\n-- start_def generated_spec_body\n%s\n-- end_def generated_spec_body\n\n-- start_def problem_spec\n%s\n-- end_def problem_spec\n\n-- start_def iso_helper_lemmas\n-- end_def iso_helper_lemmas\n\n-- start_def spec_isomorphism\n%s\n-- end_def spec_isomorphism\n-- start_def spec_isomorphism_proof\nby sorry\n-- end_def spec_isomorphism_proof\n"
                         % (fz["generated_spec_header"], generated_spec_body.strip(), fz["problem_spec"], fz["isomorphism_theorem"]))

FROZEN_A_KEYS = ("problem_id", "nl", "generated_spec_header", "preamble")

def raw_code_lines_outside_sections(txt):
    """independent check for the self-test: every raw line outside the SEC regex spans that is code"""
    spans = []
    for m in SEC.finditer(txt):
        a = txt.rfind("\n", 0, m.start()) + 1; b = m.end()
        spans.append((a, b))
    pos, out = 0, []
    for line in txt.splitlines(keepends=True):
        a, b = pos, pos + len(line); pos = b
        if any(x <= a and b <= y for x, y in spans): continue
        s = line.strip()
        if not s or s == IMPORT_LINE or s.startswith("--") or s.startswith("/-") or s.startswith("-/"): continue
        out.append(line.rstrip("\r\n"))
    return out

def main():
    if "--self-test" in sys.argv:
        root = sys.argv[1]; ok = True
        files = sorted(os.listdir(os.path.join(root, "human_eval")))
        n, with_pre = 0, set()
        for f in files:
            path = os.path.join(root, "human_eval", f); txt = open(path, encoding="utf-8").read(); s = sections(txt)
            fz, A, C = build(path); n += 1
            for leak in (first(s, "implementation"), first(s, "correctness_proof")):
                if leak and len(leak) > 40 and (leak in A or leak in C):
                    print("FAIL leak in views of", f); ok = False
            if fz["problem_spec"] in A:
                print("FAIL ground-truth spec present in stage-A view of", f); ok = False
            if "sorry" not in A or "sorry" not in C:
                print("FAIL a view lacks its sorry:", f); ok = False
            raw = raw_code_lines_outside_sections(txt)
            if [l for l in raw if l.strip()] and any(l not in fz.get("preamble", "") for l in raw):
                print("FAIL raw out-of-section code line missing from preamble:", f, raw); ok = False
            if fz.get("preamble"):
                with_pre.add(fz["problem_id"]); B = assemble_B(fz, "True")
                for name, v in (("A", A), ("C", C), ("B", B)):
                    if not v.startswith(IMPORT_LINE + "\n" + fz["preamble"] + "\n\n/--"):
                        print("FAIL preamble not right after the import in %s of %s" % (name, f)); ok = False
                if fz["preamble"] in fz["nl"]:
                    print("FAIL preamble text duplicated in nl of", f); ok = False
        if with_pre != EXPECTED_PREAMBLE_IDS:
            print("FAIL preamble-bearing set %s != expected %s" % (sorted(with_pre), sorted(EXPECTED_PREAMBLE_IDS))); ok = False
        print("PASS %d problems parsed; no implementation/proof/GT-spec leak into A; C carries GT spec by design; preamble ids %s" % (n, sorted(with_pre)) if ok else "FAILED")
        B = assemble_B(build(os.path.join(root, "human_eval", "problem_0.lean"))[0], "True")
        print("PASS B assembles" if "spec_isomorphism" in B and "problem_spec" in B else "FAIL B")
        return 0 if ok else 1
    root, out = sys.argv[1], sys.argv[2]
    for f in sorted(os.listdir(os.path.join(root, "human_eval"))):
        fz, A, C = build(os.path.join(root, "human_eval", f))
        d = os.path.join(out, "problem_%d" % fz["problem_id"]); os.makedirs(d, exist_ok=True)
        open(os.path.join(d, "A.lean"), "w").write(A); open(os.path.join(d, "C.lean"), "w").write(C)
        json.dump(fz, open(os.path.join(d, "frozen.json"), "w"), indent=1, sort_keys=True)
        # the GROUND-TRUTH-FREE frozen file for stage A (the only frozen file on the Studio while stage A runs)
        json.dump({k: fz[k] for k in FROZEN_A_KEYS if k in fz}, open(os.path.join(d, "frozenA.json"), "w"), indent=1, sort_keys=True)
    print("views written to", out)
    return 0

if __name__ == "__main__":
    sys.exit(main())
