#!/usr/bin/env python3
"""Land the arXiv identifier in the three sites PUBLISH-CHECKLIST section (n) names.

Written BEFORE the identifier existed, so the identifier is a PARAMETER and nothing
about it is encoded here. A drop-in that hardcodes its target stops being a drop-in.

The three sites, measured at the object 2026-09-10 (NOT the three the original order
named -- README.md and PROVENANCE.md had no arXiv line at all, so those are ADDITIONS):

  1. CITATION.cff      replace preferred-citation.notes, add preferred-citation.url
  2. README.md         a citation line beside the paper reference
  3. PROVENANCE.md     this repository's own paper, beside the third-party ones

The tex is deliberately NOT a site: an arXiv paper does not print its own identifier,
arXiv stamps it, and a copy here would be a second hand-maintained record of a number
the service owns.

ALL OR NOTHING. Every anchor is located before anything is written; a missing anchor
refuses the whole run rather than leaving the three sites disagreeing.

  usage:  python3 scripts/apply_arxiv_id.py --id 2609.01234 [--apply]
          python3 scripts/apply_arxiv_id.py --check
"""
import argparse, io, os, re, sys

ID_RE = re.compile(r'^\d{4}\.\d{4,5}(v\d+)?$')
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CFF_ANCHOR = '  notes: "arXiv identifier to be added at submission"'
README_ANCHOR = ("The paper is `paper/saltbench-v1.tex` (build: `cd paper && tectonic "
                 "saltbench-v1.tex`; the PDF is\ncommitted beside it). Every number in the paper "
                 "carries a comment naming the file in this\nrepository it was copied from.\n")
PROV_ANCHOR = "## 1. Task populations\n"


def path(name):
    return os.path.join(ROOT, name)


def read(name):
    with io.open(path(name), encoding='utf-8') as fh:
        return fh.read()


def plan(arxiv_id):
    """Locate every anchor and build the replacement text. Raises on any miss."""
    edits = []

    cff = read('CITATION.cff')
    if cff.count(CFF_ANCHOR) != 1:
        raise SystemExit("REFUSED: CITATION.cff anchor found %d times, expected 1.\n"
                         "  looked for: %s" % (cff.count(CFF_ANCHOR), CFF_ANCHOR))
    cff_new = ('  notes: "arXiv:%s"\n  url: "https://arxiv.org/abs/%s"' % (arxiv_id, arxiv_id))
    edits.append(('CITATION.cff', cff, CFF_ANCHOR, cff_new))

    rd = read('README.md')
    if rd.count(README_ANCHOR) != 1:
        raise SystemExit("REFUSED: README.md anchor found %d times, expected 1."
                         % rd.count(README_ANCHOR))
    rd_new = README_ANCHOR + (
        "\nThe paper is on arXiv as [arXiv:%s](https://arxiv.org/abs/%s). The version there is built\n"
        "by arXiv from that same `.tex`; the PDF committed here is built with `tectonic` and differs\n"
        "from it in line breaking and in the typewriter face, not in content.\n" % (arxiv_id, arxiv_id))
    edits.append(('README.md', rd, README_ANCHOR, rd_new))

    pv = read('PROVENANCE.md')
    if pv.count(PROV_ANCHOR) != 1:
        raise SystemExit("REFUSED: PROVENANCE.md anchor found %d times, expected 1."
                         % pv.count(PROV_ANCHOR))
    pv_new = (
        "## 0. This repository's own paper\n\n"
        "| field | value |\n|---|---|\n"
        "| paper | Hickey, \"SaltBench: A Referee-Gated Protocol for Measuring Method Effects in "
        "Machine-Checked Software Work\", arXiv:%s, https://arxiv.org/abs/%s |\n"
        "| source | `paper/saltbench-v1.tex` in this repository. arXiv builds its own PDF from that "
        "file; `paper/saltbench-v1.pdf` is the `tectonic` build committed beside it |\n"
        "| licence | CC-BY-4.0, as `LICENSE-DATA` (the owner's choice of 2026-09-02, recorded in "
        "`CITATION.cff`) |\n"
        "| relation | every number in the paper names the file in this repository it was copied "
        "from, checked by `scripts/check_paper_sources.py` |\n\n"
        % (arxiv_id, arxiv_id) + PROV_ANCHOR)
    edits.append(('PROVENANCE.md', pv, PROV_ANCHOR, pv_new))
    return edits


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--id', help='the arXiv identifier, e.g. 2609.01234 (no "arXiv:" prefix)')
    ap.add_argument('--apply', action='store_true', help='write the files (default: dry run)')
    ap.add_argument('--check', action='store_true', help='report site state and exit')
    a = ap.parse_args()

    if a.check:
        cff = read('CITATION.cff')
        landed = 'arXiv identifier to be added at submission' not in cff
        print('apply_arxiv_id --check: identifier %s' % ('LANDED' if landed else 'NOT YET LANDED'))
        # NOT labelled "self-citations": this counts EVERY arXiv identifier in the
        # file, and PROVENANCE.md legitimately cites four third-party papers. A count
        # that calls them ours would read as four self-citations before we had one.
        for n in ('CITATION.cff', 'README.md', 'PROVENANCE.md'):
            hits = sorted(set(re.findall(r'arXiv:\d{4}\.\d{4,5}', read(n))))
            print('  %-16s %d arXiv id(s), all citations: %s'
                  % (n, len(hits), ', '.join(hits) if hits else '(none)'))
        return 0

    if not a.id:
        raise SystemExit('REFUSED: --id is required. This drop-in was written before the '
                         'identifier existed and does not carry one.')
    arxiv_id = a.id.strip()
    for pre in ('arXiv:', 'arxiv:', 'https://arxiv.org/abs/'):
        if arxiv_id.startswith(pre):
            arxiv_id = arxiv_id[len(pre):]
    if not ID_RE.match(arxiv_id):
        raise SystemExit('REFUSED: %r is not an arXiv identifier of the form YYMM.NNNNN' % a.id)

    edits = plan(arxiv_id)
    print('arXiv identifier: %s' % arxiv_id)
    print('mode: %s' % ('APPLY' if a.apply else 'DRY RUN (pass --apply to write)'))
    for name, whole, old, new in edits:
        print('  %-16s anchor found, %+d chars' % (name, len(new) - len(old)))
    if not a.apply:
        print('nothing written.')
        return 0
    for name, whole, old, new in edits:
        with io.open(path(name), 'w', encoding='utf-8') as fh:
            fh.write(whole.replace(old, new))
        print('  wrote %s' % name)

    # POST-WRITE VERIFICATION. The bug this exists for: the PROVENANCE template was
    # missing its % operator, so it wrote a literal "%s" -- and the run still printed
    # "all three sites written", which was true about the write and false about the
    # content. A drop-in that does not read back what it wrote reports its own success.
    bad = []
    for name, _w, _o, _n in edits:
        after = read(name)
        if arxiv_id not in after:
            bad.append('%s: the identifier is not in the file after writing' % name)
        if '%s' in after.split('## 1.')[0] and name == 'PROVENANCE.md':
            bad.append('%s: an unsubstituted format placeholder was written' % name)
    if bad:
        print('\nVERIFICATION FAILED:')
        for b in bad:
            print('  ' + b)
        raise SystemExit('REFUSED after writing: the sites are now inconsistent, fix by hand.')
    print('verified: the identifier reads back from all three sites.')
    print('all three sites written. The tex is deliberately untouched.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
