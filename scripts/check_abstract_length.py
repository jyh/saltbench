#!/usr/bin/env python3
r"""THE ABSTRACT MUST FIT arXiv's SUBMISSION FIELD, WHICH NO OTHER GATE HERE CAN SEE.

WHY THIS EXISTS
---------------
arXiv's submission form refuses an abstract over 1,920 characters. Verified at the object
2026-09-09 at https://info.arxiv.org/help/prep.html: "Keep it short - abstracts longer than
1920 characters will not be accepted; abridge your abstract if necessary."

NOT TRUNCATED. REFUSED, at the form, by the person clicking submit.

WHAT ACTUALLY HAPPENED ON 2026-09-09, stated precisely because the first account of it was
wrong. Applying the registered statement-arm null took the abstract to 1,887 characters -- 33
UNDER the cap. A second edit in the same sitting, replacing "the verification arms cost more"
with "the arm instructed to specify and verify cost more on all five components", took it to
1,929: NINE OVER. Both figures are reproducible from the recorded shas (seat 2bf4bfe1 applied
to saltbench 0ca3b27). It was first reported as the null's doing, which it was not.

⇒ THE EDIT THAT CROSSED THE LIMIT WAS NOT THE ONE THAT LOOKED LIKE IT ADDED CONTENT. The null
added a whole clause and stayed inside. A wording change that added seven words went over. Nobody
measures a wording change against a length cap, which is exactly why this has to be mechanical.

Nothing in this repository measured either. Every check here reads tree bytes, commit messages,
source markers, or the rendered PDF; a limit that lives in a web form is invisible to all of
them, and its failure mode is a person discovering it at the moment of submission.

WHAT IT MEASURES, AND WHY THAT IS NOT THE SOURCE LENGTH
-------------------------------------------------------
arXiv receives PLAIN TEXT in that field, not LaTeX. So the count that matters is the abstract
after the transformations a person makes when pasting it: math delimiters dropped, `\times`
written as `x`, TeX quotes and dashes as their plain characters, whitespace collapsed. Counting
the tex source instead OVERSTATES the length and would red a submittable abstract, which is the
safe direction but a false one. This gate does the transformation and counts what is left.

⛔ BLIND SPOTS, DECLARED
  * It assumes the paper's own abstract IS the metadata abstract. If a separate, shorter
    abstract is pasted at the form instead, this gate measures the wrong string -- and the
    two would then drift apart, which is a worse defect than the one this prevents.
    PUBLISH-CHECKLIST section (n) records which one is submitted; keep them one string.
  * The plain-text transformation is an approximation of what a person types. It handles the
    constructs this abstract actually uses. A new construct (a `\cite`, an accent, an entity)
    is not modelled and would be counted as its source characters.
  * It says nothing about whether the abstract is GOOD, only that it fits.
"""
import argparse, re, sys

CAP = 1920            # info.arxiv.org/help/prep.html, verified at the object 2026-09-09
DEFAULT = "paper/saltbench-v1.tex"

def plain(abstract: str) -> str:
    t = abstract.strip()
    t = t.replace("\\times", "x").replace("\\%", "%").replace("\\,", " ")
    t = t.replace("``", '"').replace("''", '"').replace("---", "--")
    t = t.replace("$", "")
    return re.sub(r"\s+", " ", t).strip()

def extract(tex: str):
    m = re.search(r"\\begin\{abstract\}(.*?)\\end\{abstract\}", tex, re.S)
    return m.group(1) if m else None

def check(path: str) -> int:
    try:
        tex = open(path, encoding="utf-8").read()
    except OSError as e:
        print(f"FAIL: cannot read {path}: {e}")
        return 1
    a = extract(tex)
    if a is None:
        # An absent abstract is FATAL, never a pass. A gate that scans nothing and exits 0 is
        # the failure this house drives red first.
        print(f"FAIL: no abstract environment in {path}; this gate scanned nothing")
        return 1
    n = len(plain(a))
    if n > CAP:
        print(f"FAIL: abstract is {n} plain-text characters, {n - CAP} over arXiv's {CAP} cap.")
        print("      arXiv REFUSES a longer abstract at the submission form; it does not truncate.")
        print("      Shorten the abstract. Do not raise the constant: it is arXiv's, not ours.")
        return 1
    print(f"check_abstract_length: OK ({n} plain-text characters, {CAP - n} under arXiv's {CAP} cap)")
    return 0

def self_test() -> int:
    # (0) SCANNING NOTHING IS FATAL, proven before any arm that can pass.
    import tempfile, os
    with tempfile.TemporaryDirectory() as d:
        empty = os.path.join(d, "no-abstract.tex")
        open(empty, "w").write("\\documentclass{article}\\begin{document}hi\\end{document}\n")
        if check(empty) == 0:
            print("SELF-TEST FAIL: a tex with no abstract must be fatal"); return 1
        print("  self-test 0/3: a tex with no abstract is fatal ...................... ok")

        # (1) RED on an abstract one character over the cap.
        over = "x" * (CAP + 1)
        red = os.path.join(d, "over.tex")
        open(red, "w").write("\\begin{abstract}\n" + over + "\n\\end{abstract}\n")
        if check(red) == 0:
            print("SELF-TEST FAIL: an abstract over the cap must be refused"); return 1
        print(f"  self-test 1/3: {CAP + 1} characters is refused ....................... ok")

        # (2) GREEN at exactly the cap -- the boundary is inclusive, and an off-by-one here
        #     would red a submittable abstract.
        at = os.path.join(d, "at.tex")
        open(at, "w").write("\\begin{abstract}\n" + "x" * CAP + "\n\\end{abstract}\n")
        if check(at) != 0:
            print("SELF-TEST FAIL: exactly the cap must pass"); return 1
        print(f"  self-test 2/3: exactly {CAP} characters passes ...................... ok")

        # (3) The transformation must SHORTEN: a source that is over the cap only because of
        #     markup must pass, or the gate reds a submittable abstract.
        markup = "$2.8879\\times$ " * 130 + "x" * 400
        if len(markup) <= CAP:
            print("SELF-TEST FAIL: fixture is not over the cap in source form"); return 1
        mk = os.path.join(d, "markup.tex")
        open(mk, "w").write("\\begin{abstract}\n" + markup + "\n\\end{abstract}\n")
        if check(mk) != 0:
            print("SELF-TEST FAIL: markup must be stripped before counting"); return 1
        print(f"  self-test 3/3: {len(markup)} source chars counted as plain text ...... ok")
    return 0

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--self-test", action="store_true")
    p.add_argument("--tex", default=DEFAULT)
    a = p.parse_args()
    if a.self_test:
        sys.exit(self_test())
    sys.exit(check(a.tex))
