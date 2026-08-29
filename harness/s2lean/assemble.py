#!/usr/bin/env python3
"""assemble.py — the CANONICAL scored file (frozen statements + the agent's extracted bodies) and the PRISTINE
file (frozen statements only, `sorry` bodies, NO agent text). Repair round 1: NO `#print axioms` lines are
appended — the axiom audit is done by s2audit.lean over the compiled olean, outside the agent's elaboration.

Layout (D4/§1): `import Imports.AllImports` NL preamble NL `/-- nl -/` then per stage:
  A: generated_spec header + body
  B: generated_spec header + body(stage-A body, merged by check.py) · problem_spec · iso_helper_lemmas · theorem + proof
  C: problem_spec · implementation signature + body · test_cases (IN the canonical file) · helpers · theorem + proof
The pristine file has `sorry` bodies, empty helper sections and, for C, NO test lines (a `#test` on a sorry
implementation cannot evaluate). A missing `preamble` key means an empty preamble.

usage: assemble.py <stage> <frozen.json> <bodies.json|-> [--pristine]      -> Lean source on stdout
importable: assemble(stage, frozen_dict, bodies_dict, pristine=False) -> str
"""
import json, sys


def _hdr(fz):
    pre = (fz.get("preamble") or "").strip("\n")
    return "import Imports.AllImports\n" + (pre + "\n" if pre.strip() else "") + "\n/--\n%s\n-/\n" % fz["nl"]


def assemble(stage, fz, bd, pristine=False):
    bd = {} if pristine else (bd or {})
    g = lambda k, dflt: (dflt if pristine else ((bd.get(k) or "").strip() or dflt))
    h = lambda k: ("" if pristine else (bd.get(k) or "").strip())
    hdr = _hdr(fz)
    if stage == "A":
        return hdr + "\n%s\n%s\n" % (fz["generated_spec_header"], g("generated_spec_body", "sorry"))
    if stage == "B":
        return hdr + "\n%s\n%s\n\n%s\n\n%s\n\n%s\n%s\n" % (
            fz["generated_spec_header"], g("generated_spec_body", "sorry"), fz["problem_spec"],
            h("iso_helper_lemmas"), fz["isomorphism_theorem"], g("spec_isomorphism_proof", "by sorry"))
    if stage == "C":
        tests = "" if pristine else (fz.get("test_cases") or "")
        return hdr + "\n%s\n\n%s\n%s\n\n%s\n\n%s\n\n%s\n%s\n" % (
            fz["problem_spec"], fz["implementation_signature"], g("implementation", "sorry"), tests,
            h("correctness_helper_lemmas"), fz["correctness_theorem"], g("correctness_proof", "by sorry"))
    raise ValueError("stage must be A|B|C, got %r" % stage)


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if len(args) != 3:
        sys.exit(__doc__)
    stage, fzp, bdp = args
    pristine = "--pristine" in sys.argv
    fz = json.load(open(fzp))
    bd = {} if (pristine or bdp == "-") else json.load(open(bdp))
    sys.stdout.write(assemble(stage, fz, bd, pristine=pristine))
