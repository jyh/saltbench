#!/usr/bin/env python3
"""CENSUS-full-matrix-2026-09-14-verify.py [--doc D] [--selftest]

Re-derive the census's TRAJECTORY BOX from the `ADDENDUM n` HEADLINES of the same document and assert it
against the BYTES of that box. Idiom law clause 1: NO TYPED EXPECTATIONS — every expected figure is
COMPUTED from a headline and then required to be PRESENT in the box.

⛔⛔ WHY THIS FILE EXISTS, AND IT IS NOT A HYPOTHETICAL. The box carries a long, correct post-mortem of
  itself going stale (the ADDENDUM 9 row, added two days late by ADDENDUM 10) — and then went stale again
  for SEVEN CONSECUTIVE ADDENDA. On 2026-09-22 its `LIVE` row read `ADDENDUM 11 · DONE 109 · OWED 75`
  while the document's own live figure was `DONE 160 · OWED 24`: fifty-one conditions behind, in the one
  table that section declares to be the only current figure in the document, about the Captain's stated
  top priority.
  ⇒ 🔑 THE POST-MORTEM DIAGNOSED THE FAILURE PRECISELY AND PREVENTED NOTHING, BECAUSE A POST-MORTEM IS
    SOMETHING A READER READS WHILE THE LAPSE IS SOMETHING A WRITER COMMITS.
  ⇒ 🔑 AND THE REMEDY IT REACHED FOR WAS READER-SIDE — "the rows are DERIVABLE, so a reader who distrusts
    this box can rebuild it." That is TRUE, and it taxes every read while leaving every write free.
    A READER-SIDE REMEDY FOR A WRITER-SIDE DEFECT IS A PERMANENT TAX THAT NEVER FIXES ANYTHING.
  ⇒ ✅ So this does the rebuilding the box already proved was possible, and REFUSES. The box's own
    sentence — "that is the check this box should have had" — is what this file is.

⛔ WHAT IT DOES NOT DO. It does not check that the addenda's arithmetic is RIGHT; it checks that the BOX
  AGREES WITH THE HEADLINES. If an addendum's own headline is wrong, both agree and this stays green —
  a limit stated here, beside the verdict, because a limit printed anywhere else is one the reader of the
  verdict never sees. The per-block `RESULT-*-verify.py` files are what check a block's own figures.

rc 0 the box agrees with every headline · 1 a mismatch, named · 2 usage/missing document."""
import re, sys, os, argparse

HERE = os.path.dirname(os.path.abspath(__file__))
DOC = os.path.join(HERE, "CENSUS-full-matrix-2026-09-14.md")

HEAD = re.compile(r'^# .*ADDENDUM (\d+) — \*\*(.+?)\*\*', re.M)
ROW  = re.compile(r'^>\s+(?:LIVE \(ADDENDUM (\d+)\)|ADDENDUM (\d+))\s+DONE (\d+) · OWED\s+(\d+) ·', re.M)

def headlines(src):
    """{n: (done_after, owed_after)} for every addendum whose headline states a move OF THE TOTAL.

    ⛔⛔ A HEADLINE MAY MOVE A SUB-ROW AND THE TOTAL IN ONE SENTENCE, AND THE FIRST FIGURE IS THE SUB-ROW.
      ADDENDUM 5 reads "THE FLASH ROW MOVES: `DONE 0 → 7`, `OWED 46 → 39`. TOTAL `DONE 50 → 57`." — a
      naive first-match parser reads `DONE → 7` as the total and reports the box as wrong by fifty.
      ⇒ 🔑 THIS IS NOT HYPOTHETICAL: the first version of this file did exactly that and manufactured
        THREE confident findings against a CORRECT document. A needle defect gives you a finding where
        your own words are wrong, and it looks like news, which is precisely the shape one wants to
        publish. ✅ So: when a headline says TOTAL, the total is what follows TOTAL.
    ⛔ AND A HEADLINE SCOPED TO A SUB-ROW WITH NO TOTAL CLAUSE (ADDENDUM 2, "THE FLASH ROW WAS WRONG")
      MOVES NO TOTAL AND OWES NO ROW."""
    out = {}
    for m in HEAD.finditer(src):
        n, h = int(m.group(1)), m.group(2)
        tail = h[h.index("TOTAL"):] if "TOTAL" in h else h
        scoped_sub = ("TOTAL" not in h) and re.search(r'\b(FLASH|OPUS|SONNET|PRO)\s+ROW\b', h, re.I)
        if scoped_sub:
            continue
        d = re.search(r'DONE (\d+) → (\d+)', tail)
        o = re.search(r'OWED (\d+) → (\d+)', tail)
        if d or o:
            out[n] = (d.group(2) if d else None, o.group(2) if o else None)
    return out

def rows(src):
    """[(n, done, owed, is_live)] in document order, from the trajectory box."""
    out = []
    for m in ROW.finditer(src):
        live = m.group(1) is not None
        out.append((int(m.group(1) or m.group(2)), m.group(3), m.group(4), live))
    return out

def run(doc):
    if not os.path.exists(doc):
        print("⛔ REFUSE — no such document: %s" % doc); return 2
    src = open(doc, encoding="utf-8").read()
    H, R = headlines(src), rows(src)
    if not H or not R:
        print("⛔ REFUSE — parsed %d headline(s) and %d box row(s); one of the two shapes has changed "
              "and this verifier would otherwise pass vacuously." % (len(H), len(R))); return 1
    fails = []
    by_n = {n: (d, o) for n, d, o, _ in R}

    # (1) every addendum that MOVED a figure owes a row, and the row must carry the headline's AFTER value
    # ⚖️ SCOPED TO THE REGION THE BOX COVERS, because a coverage claim is only as wide as its population.
    #   The box's per-addendum rows begin at the FIRST addendum it carries; earlier corrections are folded
    #   into its `12:1x (§F1)` row by construction and owe no row of their own. Measuring "every addendum"
    #   against a box that never claimed to hold them all is an accurate measurement of the wrong thing.
    first_row = min(by_n) if by_n else 0
    for n in sorted(H):
        if n < first_row:
            continue
        want_d, want_o = H[n]
        if n not in by_n:
            fails.append("ADDENDUM %d moves the count in its own headline (DONE→%s OWED→%s) and has NO ROW "
                         "in the trajectory box" % (n, want_d, want_o)); continue
        got_d, got_o = by_n[n]
        if want_d and got_d != want_d:
            fails.append("ADDENDUM %d: headline says DONE → %s, box row says DONE %s" % (n, want_d, got_d))
        if want_o and got_o != want_o:
            fails.append("ADDENDUM %d: headline says OWED → %s, box row says OWED %s" % (n, want_o, got_o))

    # (2) the LIVE row is the LAST addendum in the document, and there is exactly one
    lives = [n for n, _, _, live in R if live]
    last = max(max(H), max(by_n))
    if len(lives) != 1:
        fails.append("the box carries %d rows marked LIVE; there must be exactly one" % len(lives))
    elif lives[0] != last:
        fails.append("the LIVE row is ADDENDUM %d but the document's last addendum is %d — the box is "
                     "%d addend(a) STALE, which is the defect this file exists for"
                     % (lives[0], last, last - lives[0]))

    # (3) the chain is continuous: each row starts where the previous one ended, unless its headline moved it
    seq = [(n, d, o) for n, d, o, _ in R]
    for (pn, pd, po), (n, d, o) in zip(seq, seq[1:]):
        if n not in H and (d, o) != (pd, po):
            fails.append("ADDENDUM %d's row moves the count (DONE %s→%s, OWED %s→%s) while its headline "
                         "states no move" % (n, pd, d, po, o))

    for f in fails:
        print("⛔ %s" % f)
    if fails:
        print("\n⛔ CENSUS BOX REFUSED — %d finding(s). The box is derived from the ADDENDUM headlines; fix\n"
              "   whichever of the two is wrong, in the same edit as the addendum that moved the count." % len(fails))
        return 1
    print("✅ the trajectory box agrees with all %d addendum headline(s) that state a move; LIVE is "
          "ADDENDUM %d, the last in the document; the chain is continuous." % (len(H), last))
    print("⚠️  LIMIT, beside the verdict: this asserts the BOX AGREES WITH THE HEADLINES. It cannot see an\n"
          "   addendum whose own headline is wrong — both would agree. The per-block RESULT verifiers do that.")
    print("⚠️  COVERAGE, derived not assumed: checked from ADDENDUM %d (the first the box carries) to %d.\n"
          "   Earlier addenda are folded into the box's `12:1x` row and owe no row; sub-row-only headlines\n"
          "   (e.g. \"THE FLASH ROW WAS WRONG\") move no total and are excluded BY NAME, not silently."
          % (first_row, last))
    return 0

def selftest():
    src = open(DOC, encoding="utf-8").read()
    import tempfile
    fails, fired, total = [], 0, 0
    def drive(label, text, want_rc):
        nonlocal fired, total
        total += 1
        d = tempfile.mkdtemp(); p = os.path.join(d, "c.md")
        open(p, "w", encoding="utf-8").write(text)
        import io, contextlib
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            rc = run(p)
        ok = (rc == want_rc)
        if ok: fired += 1; print("  ok   %-26s rc %d" % (label, rc))
        else:  fails.append(label); print("  FAIL %-26s rc %d (wanted %d)" % (label, rc, want_rc))
        return buf.getvalue()

    drive("control-unmodified", src, 0)
    # ⭐ RED BACKWARDS: restore the pre-2026-09-22 box — LIVE at ADDENDUM 11 with rows 12-18 gone.
    stale = src
    for n in (12, 13, 14, 15, 16, 17):
        stale = re.sub(r'^>   ADDENDUM %d .*\n' % n, '', stale, flags=re.M)
    stale = re.sub(r'^>   LIVE \(ADDENDUM 18\).*\n' % (), '', stale, flags=re.M)
    stale = stale.replace(">   ADDENDUM 11       DONE 109 · OWED  75",
                          ">   LIVE (ADDENDUM 11) DONE 109 · OWED 75")
    out = drive("RED-the-actual-lapse", stale, 1)
    if "STALE" not in out:
        fails.append("RED-the-actual-lapse-names-staleness"); print("  FAIL the lapse arm did not name STALENESS")
    else:
        fired += 1; print("  ok   %-26s and it NAMES the staleness and its size" % "lapse-names-staleness")
    total += 1
    drive("RED-a-wrong-figure", src.replace("ADDENDUM 13       DONE 119", "ADDENDUM 13       DONE 118"), 1)
    drive("RED-two-LIVE-rows", src.replace(">   ADDENDUM 17       DONE 152", ">   LIVE (ADDENDUM 17) DONE 152"), 1)
    # ⛔ THE CONTROL FOR THE rc-2 ARM, NAMED FOR WHAT IT DRIVES: a PRESENT document must not give rc 2,
    #   or "absent refuses" would be indistinguishable from "this verifier refuses everything".
    drive("control-doc-present", src, 0)
    total += 1
    import io as _io, contextlib as _c
    _b = _io.StringIO()
    with _c.redirect_stdout(_b):
        rc = run(os.path.join(HERE, "no-such-census-file.md"))
    if rc == 2: fired += 1; print("  ok   %-26s rc 2, NOT 1 — absence is refused, never reported as a clean pass" % "REFUSE-absent-doc")
    else: fails.append("REFUSE-absent-doc"); print("  FAIL absent doc gave rc %d" % rc)
    # a shape change must not pass VACUOUSLY
    drive("REFUSE-shape-changed", re.sub(r'^# .*ADDENDUM .*$', '# gone', src, flags=re.M), 1)

    print()
    if fails:
        print("⛔ SELFTEST FAILED on arm(s) %s" % fails); return 1
    print("✅ SELFTEST %d/%d — control green; THE ACTUAL 2026-09-22 LAPSE reddens it and is named as\n"
          "   staleness WITH ITS SIZE (red-backwards: the mutant is the real pre-fix box, not an invented\n"
          "   one); a wrong figure, two LIVE rows, and a changed heading shape each redden it; and a\n"
          "   MISSING document refuses rc 2 rather than 1, so absence is never a clean pass." % (fired, total))
    return 0

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--doc", default=DOC)
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    sys.exit(selftest() if a.selftest else run(a.doc))
