#!/usr/bin/env python3
"""o90_flaglog.py — the O90 truth axis's FLAG LOG: its schema, its validator, and the two readings it exists for (desk AEY;
the design §3 truth row [F8c]; evidence's ask in the 10-23 schedule §4: every flag records its READER and its OUTCOME).
One TSV row per (sentence, read). Columns, in order, all required:
  problem    CLEVER id (int)                     arm         a0 | a5
  b_episode  the scored stage-B episode whose artifact the sentence is in (its author)
  sentence   a stable id within the artifact      sentence_sha256  sha256 of the sentence's bytes as read
  reader     the read's id (a session id)         mechanism   gemini | claude      (the reader's model family)
  verdict    OK | FALSE                           (FALSE = the reader says the sentence is false of its Lean)
  confirmer  the third read's id, or -            confirmed   yes | no | -         (- only when verdict is OK)
Rules (each a refusal): a reader or confirmer is never the author (never equals b_episode); the confirmer is never the
reader; a FALSE carries a confirmer and yes|no; an OK carries - and -; one row per (b_episode, sentence, reader); one
sentence_sha256 per (b_episode, sentence).
Readings: (1) the AXIS — a sentence is FALSE iff some read flagged it AND its confirmation is yes [F8c]; per problem and arm,
does the artifact carry >= 1 FALSE sentence. (2) evidence's leg (c) analogue — the share of FALSE flags NOT confirmed,
per mechanism and per arm. Nothing here scores a reader against a key: stage 1 has no planted key (schedule §4).
  usage: o90_flaglog.py <log.tsv>      ·      o90_flaglog.py --selftest"""
import csv, collections, io, sys
COLS = ["problem", "arm", "b_episode", "sentence", "sentence_sha256", "reader", "mechanism", "verdict", "confirmer", "confirmed"]
def load(f):
    rows = list(csv.reader(f, delimiter="\t"))
    if not rows or rows[0] != COLS: raise SystemExit("REFUSE: header must be exactly: " + "\t".join(COLS))
    out, seen, shas = [], set(), {}
    for n, r in enumerate(rows[1:], 2):
        if len(r) != len(COLS): raise SystemExit("REFUSE line %d: %d fields, want %d" % (n, len(r), len(COLS)))
        d = dict(zip(COLS, r))
        if d["arm"] not in ("a0", "a5"): raise SystemExit("REFUSE line %d: arm %r" % (n, d["arm"]))
        if d["mechanism"] not in ("gemini", "claude"): raise SystemExit("REFUSE line %d: mechanism %r" % (n, d["mechanism"]))
        if d["verdict"] not in ("OK", "FALSE"): raise SystemExit("REFUSE line %d: verdict %r" % (n, d["verdict"]))
        if d["reader"] == d["b_episode"] or d["confirmer"] == d["b_episode"]: raise SystemExit("REFUSE line %d: a read by the author" % n)
        if d["verdict"] == "FALSE":
            if d["confirmer"] in ("-", "") or d["confirmed"] not in ("yes", "no"): raise SystemExit("REFUSE line %d: a FALSE needs a confirmer and yes|no" % n)
            if d["confirmer"] == d["reader"]: raise SystemExit("REFUSE line %d: the confirmer is the reader" % n)
        elif (d["confirmer"], d["confirmed"]) != ("-", "-"): raise SystemExit("REFUSE line %d: an OK carries - and -" % n)
        k = (d["b_episode"], d["sentence"], d["reader"])
        if k in seen: raise SystemExit("REFUSE line %d: duplicate read %r" % (n, k))
        seen.add(k)
        s = shas.setdefault((d["b_episode"], d["sentence"]), d["sentence_sha256"])
        if s != d["sentence_sha256"]: raise SystemExit("REFUSE line %d: sentence %r read as two different texts" % (n, d["sentence"]))
        out.append(d)
    return out
def readings(rows):
    false_s = {(r["problem"], r["arm"], r["b_episode"], r["sentence"]) for r in rows if r["verdict"] == "FALSE" and r["confirmed"] == "yes"}
    arts = sorted({(r["problem"], r["arm"], r["b_episode"]) for r in rows})
    axis = [(p, a, e, sum(1 for s in false_s if s[:3] == (p, a, e))) for p, a, e in arts]
    fa = collections.defaultdict(lambda: [0, 0])
    for r in rows:
        if r["verdict"] == "FALSE":
            for key in ((r["mechanism"], r["arm"]), (r["mechanism"], "*"), ("*", r["arm"])):
                fa[key][0] += 1; fa[key][1] += (r["confirmed"] == "no")
    return axis, dict(fa)
def report(rows):
    axis, fa = readings(rows)
    print("AXIS (a sentence is FALSE iff flagged AND confirmed yes): problem arm b_episode false_sentences")
    for p, a, e, n in axis: print("  %s %s %s %d%s" % (p, a, e, n, "  <- carries a FALSE sentence" if n else ""))
    print("FALSE FLAGS NOT CONFIRMED (mechanism, arm): not_confirmed / flags")
    for k in sorted(fa): print("  %-8s %-3s %d / %d" % (k[0], k[1], fa[k][1], fa[k][0]))
def selftest():
    H = "\t".join(COLS) + "\n"
    good = H + "".join("\t".join(x) + "\n" for x in [
        ["31", "a5", "ep-b5", "s1", "aa", "g1", "gemini", "FALSE", "c1", "yes"],
        ["31", "a5", "ep-b5", "s1", "aa", "k1", "claude", "OK", "-", "-"],
        ["31", "a5", "ep-b5", "s2", "bb", "g1", "gemini", "FALSE", "c1", "no"],
        ["31", "a0", "ep-b0", "s1", "cc", "g1", "gemini", "OK", "-", "-"]])
    rows = load(io.StringIO(good)); axis, fa = readings(rows)
    assert axis == [("31", "a0", "ep-b0", 0), ("31", "a5", "ep-b5", 1)], axis
    assert fa[("gemini", "a5")] == [2, 1] and ("claude", "a5") not in fa, fa
    bad = {"author reads": ["31", "a5", "ep-b5", "s3", "dd", "ep-b5", "gemini", "OK", "-", "-"],
           "FALSE w/o confirmer": ["31", "a5", "ep-b5", "s3", "dd", "g2", "gemini", "FALSE", "-", "-"],
           "confirmer is reader": ["31", "a5", "ep-b5", "s3", "dd", "g2", "gemini", "FALSE", "g2", "yes"],
           "OK with confirmer": ["31", "a5", "ep-b5", "s3", "dd", "g2", "gemini", "OK", "c1", "yes"],
           "two texts": ["31", "a5", "ep-b5", "s1", "zz", "g9", "gemini", "OK", "-", "-"],
           "duplicate read": ["31", "a5", "ep-b5", "s1", "aa", "g1", "gemini", "OK", "-", "-"],
           "bad mechanism": ["31", "a5", "ep-b5", "s3", "dd", "g2", "gpt", "OK", "-", "-"]}
    for name, row in bad.items():
        try: load(io.StringIO(good + "\t".join(row) + "\n")); raise AssertionError("ACCEPTED: " + name)
        except SystemExit as e: assert str(e).startswith("REFUSE"), (name, e)
    # mutant: an axis that counts a FALSE flag without its confirmation would report 2 for ep-b5 — the arm above pins 1
    print("SELFTEST PASS: 1 good log (axis 0 / 1, gemini a5 1 of 2 not confirmed), %d refusals each fired" % len(bad))
if __name__ == "__main__":
    if sys.argv[1:] == ["--selftest"]: selftest()
    else: report(load(open(sys.argv[1], newline="")))
