#!/usr/bin/env python3
r"""check_paper_render.py — THE TRACKED PDF MUST RENDER THE TRACKED TEX.

WHY THIS EXISTS, AND IT IS A METHOD RATHER THAN A FIX. On 2026-09-09 a correction landed in
`paper/saltbench-v1.tex` and the tracked `paper/saltbench-v1.pdf` was not rebuilt, so the
repository held a corrected source beside a rendering of the sentence the correction removed.
Every gate was green, because no gate rendered anything: the source-marker gate reads the tex,
the scrub gates read tree bytes and commit messages, and nothing compared the two artifacts.
The PDF is what an arXiv cut would take, so the artifact anyone would have shipped was the stale
one. THE FAILURE DIRECTION IS THE DANGEROUS ONE: after the correction the repository looked MORE
correct than before, and a stale build fails toward looking fixed.

⭐ THE METHOD THAT CAUGHT IT, WHICH IS THE REASON THIS JOB EXISTS: the fix was verified by
reading both strings back OUT of the rendered PDF rather than by trusting that the build
succeeded. A build that exits 0 tells you a PDF was written. It does not tell you what is in it.
This gate is that read, performed mechanically on every push.

WHAT IT DOES. For every `<name>.tex` in `paper/` that has a tracked `<name>.pdf` beside it, it
rebuilds the tex in a scratch directory with the pinned engine, extracts the text layer of the
fresh PDF and of the tracked PDF, normalizes whitespace, and refuses if they differ.

⛔ DECLARED BLIND SPOTS, because a gate that does not state its limits gets read as stronger than
it is:
  1. ENGINE AND FONT DRIFT. The comparison assumes the tracked PDF was produced by the same
     engine and font set this runs. A tectonic upgrade, or a different font resolution on
     another box, can move the text layer with the source unchanged and red this gate on a
     correct pair. That is a false red, which is the safe direction, and the remedy is a rebuild
     rather than a suppression. The engine is pinned in the workflow for exactly this reason.
  2. IT COMPARES STRINGS, NOT LAYOUT. Two PDFs with the same extracted text can differ in
     pagination, figure placement, table rules, kerning and every other visual property. This
     gate cannot see a layout regression, and nothing here should be read as a claim that the
     tracked PDF LOOKS right.
  3. IT DOES NOT READ NON-TEXT CONTENT. Images, vector figures and anything without a text layer
     are invisible to it.
  4. `\src{}` markers expand to nothing, so a marker change moves the tex and not the text
     layer. That is the source-marker gate's job, not this one's.

FAIL-CLOSED. An empty scan is fatal: if no tex/pdf pair is found, the gate refuses rather than
passing, because a silent zero is how a scan that stopped matching looks exactly like a clean one.
"""
import argparse, os, re, shutil, subprocess, sys, tempfile

PAPER_DIR = "paper"


def die(msg):
    print("check_paper_render: FAIL — " + msg)
    sys.exit(1)


def have(tool):
    return shutil.which(tool) is not None


def text_of(pdf):
    """The PDF's text layer, whitespace-normalized. This is the 'read it back out' step."""
    out = subprocess.run(["pdftotext", "-layout", pdf, "-"],
                         capture_output=True, text=True)
    if out.returncode != 0:
        die("pdftotext failed on %s: %s" % (pdf, out.stderr.strip()[:400]))
    return re.sub(r"\s+", " ", out.stdout).strip()


def build(tex_path, outdir):
    """Render tex_path into outdir. Returns the produced PDF path."""
    r = subprocess.run(["tectonic", "--outdir", outdir, tex_path],
                       capture_output=True, text=True)
    if r.returncode != 0:
        die("tectonic failed on %s:\n%s" % (tex_path, r.stderr.strip()[:2000]))
    pdf = os.path.join(outdir, os.path.splitext(os.path.basename(tex_path))[0] + ".pdf")
    if not os.path.exists(pdf):
        die("tectonic exited 0 but wrote no PDF for %s" % tex_path)
    return pdf


def first_difference(a, b):
    """A human-readable window on where two normalized texts diverge."""
    n = min(len(a), len(b))
    i = 0
    while i < n and a[i] == b[i]:
        i += 1
    lo = max(0, i - 90)
    return ("  tracked : ...%s...\n  rebuilt : ...%s...\n  (diverges at character %d; "
            "tracked is %d chars, rebuilt is %d)"
            % (a[lo:i + 90], b[lo:i + 90], i, len(a), len(b)))


def compare_pair(tex, tracked_pdf, scratch):
    """True when the tracked PDF renders the tex. False, with a report, when it does not."""
    fresh = build(tex, scratch)
    t_tracked, t_fresh = text_of(tracked_pdf), text_of(fresh)
    if t_tracked == t_fresh:
        return True, "%s renders %s (%d chars of text layer, identical)" % (
            os.path.basename(tracked_pdf), os.path.basename(tex), len(t_fresh))
    return False, ("%s DOES NOT RENDER %s — the tracked PDF is stale against its source.\n%s"
                   % (os.path.basename(tracked_pdf), os.path.basename(tex),
                      first_difference(t_tracked, t_fresh)))


def scan(paper_dir):
    if not have("tectonic"):
        die("tectonic is not on PATH; this gate cannot run without the pinned engine")
    if not have("pdftotext"):
        die("pdftotext (poppler) is not on PATH; this gate cannot read a PDF back")
    if not os.path.isdir(paper_dir):
        die("no %s/ directory — EMPTY SCAN IS FATAL (a silent zero looks like a clean run)"
            % paper_dir)
    pairs = []
    for f in sorted(os.listdir(paper_dir)):
        if f.endswith(".tex"):
            pdf = os.path.join(paper_dir, f[:-4] + ".pdf")
            if os.path.exists(pdf):
                pairs.append((os.path.join(paper_dir, f), pdf))
    if not pairs:
        die("no tex/pdf pair found under %s/ — EMPTY SCAN IS FATAL" % paper_dir)
    bad = []
    for tex, pdf in pairs:
        with tempfile.TemporaryDirectory() as scratch:
            ok, report = compare_pair(tex, pdf, scratch)
        print(("  OK   " if ok else "  RED  ") + report)
        if not ok:
            bad.append(pdf)
    if bad:
        die("%d tracked PDF(s) stale against source: %s\n"
            "       A commit that edits the tex owns the rebuild: cd paper && tectonic <name>.tex"
            % (len(bad), ", ".join(bad)))
    print("check_paper_render: OK (%d tex/pdf pair(s), every tracked PDF renders its source)"
          % len(pairs))


FIXTURE_STALE = r"""\documentclass{article}
\begin{document}
\textbf{Every magnitude is unresolved.} This fixture reconstructs the state of this repository
on 2026-09-09: a bold lead-in that was corrected in the source after the PDF was built.
\end{document}
"""
FIXTURE_FIXED = FIXTURE_STALE.replace(
    "Every magnitude is unresolved.", "No magnitude is resolvable for the population.")


def self_test():
    """Drive the gate RED before it is allowed to pass, on a fixture that reconstructs the
    real defect: a corrected tex beside the PDF built from the text before the correction."""
    if not have("tectonic") or not have("pdftotext"):
        die("self-test needs tectonic and pdftotext on PATH")
    arms = []
    with tempfile.TemporaryDirectory() as d:
        paper = os.path.join(d, "paper")
        os.makedirs(paper)
        tex = os.path.join(paper, "fixture.tex")

        # ARM 0 — the empty scan must be fatal, and it is proven FIRST, before any arm that
        # can pass. A gate whose scan silently matches nothing prints the same thing as a
        # clean repository.
        rc = subprocess.run([sys.executable, __file__, "--paper-dir", paper],
                            capture_output=True, text=True).returncode
        if rc == 0:
            die("SELF-TEST: empty scan PASSED; it must be fatal")
        arms.append("empty scan fatal proven FIRST")

        # Build the STALE pdf from the pre-correction text, then correct the tex under it.
        open(tex, "w").write(FIXTURE_STALE)
        stale_pdf = build(tex, paper)
        assert stale_pdf == os.path.join(paper, "fixture.pdf")
        open(tex, "w").write(FIXTURE_FIXED)

        # ARM 1 — RED on the stale pair. This is today's defect, reconstructed.
        with tempfile.TemporaryDirectory() as s:
            ok, report = compare_pair(tex, stale_pdf, s)
        if ok:
            die("SELF-TEST: the stale pair PASSED; the gate cannot see the defect it exists for")
        if "Every magnitude" not in report and "No magnitude" not in report:
            die("SELF-TEST: the stale pair was caught but the report names neither sentence")
        arms.append("RED on a corrected tex beside its pre-correction PDF (today's state)")

        # ARM 2 — GREEN once rebuilt, and nothing else changed between the arms.
        build(tex, paper)
        with tempfile.TemporaryDirectory() as s:
            ok, _ = compare_pair(tex, stale_pdf, s)
        if not ok:
            die("SELF-TEST: the REBUILT pair was refused; the gate reds on a correct pair")
        arms.append("GREEN on the same pair after the rebuild, nothing else changed")

    print("check_paper_render SELF-TEST: OK (%s)" % "; ".join(arms))


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--self-test", action="store_true")
    p.add_argument("--paper-dir", default=PAPER_DIR)
    a = p.parse_args()
    if a.self_test:
        self_test()
    else:
        scan(a.paper_dir)
