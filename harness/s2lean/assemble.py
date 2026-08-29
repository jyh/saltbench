#!/usr/bin/env python3
"""assemble.py — the CANONICAL scored file: frozen statements + the agent's extracted bodies. Emits the Lean source
and appends the axiom audit commands. usage: assemble.py <stage> <frozen.json> <bodies.json> [--no-audit]"""
import json, sys
stage, fz, bd = sys.argv[1], json.load(open(sys.argv[2])), json.load(open(sys.argv[3]))
audit = "--no-audit" not in sys.argv
hdr = "import Imports.AllImports\n\n/--\n%s\n-/\n" % fz["nl"]
if stage == "A":
    src = hdr + "\n%s\n%s\n" % (fz["generated_spec_header"], bd["generated_spec_body"].strip() or "sorry")
    decls = ["generated_spec"]
elif stage == "B":
    src = hdr + "\n%s\n%s\n\n%s\n\n%s\n\n%s\n%s\n" % (fz["generated_spec_header"], bd["generated_spec_body"].strip(), fz["problem_spec"], bd.get("iso_helper_lemmas", ""), fz["isomorphism_theorem"], bd["spec_isomorphism_proof"].strip() or "by sorry")
    decls = ["generated_spec", "spec_isomorphism"]
else:
    src = hdr + "\n%s\n\n%s\n%s\n\n%s\n\n%s\n\n%s\n%s\n" % (fz["problem_spec"], fz["implementation_signature"], bd["implementation"].strip() or "sorry", fz["test_cases"] or "", bd.get("correctness_helper_lemmas", ""), fz["correctness_theorem"], bd["correctness_proof"].strip() or "by sorry")
    decls = ["implementation", "correctness"]
if audit:
    src += "\n" + "\n".join("#print axioms %s" % d for d in decls) + "\n"
sys.stdout.write(src)
