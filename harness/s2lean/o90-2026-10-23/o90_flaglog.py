#!/usr/bin/env python3
"""o90_flaglog.py — the O90 truth axis's FLAG LOG: its schema, its validator, and the readings it exists for (desk AEY;
the design §3 truth row [F8c]; evidence's ask in the 10-23 schedule §4: every flag records its READER and its OUTCOME;
AMENDMENT-O90-stage1 ADDENDUM 3, A3.4a–A3.6, with systems' C1 of 2026-10-25).
One TSV row per (sentence, read). Columns, in order, all required:
  problem    CLEVER id (int)                     arm         a0 | a5
  b_episode  the scored stage-B episode whose artifact the sentence is in (its author)
  sentence   a stable id within the artifact      sentence_sha256  sha256 of the sentence's bytes as read
  reader     the read's id (a session id)         mechanism   gemini | claude      (the reader's model family)
  verdict    OK | FALSE | UNSCORED                (FALSE = the reader says the sentence is false of its Lean)
  confirmer  the third read's id, or -            confirmed   yes | no | UNSCORED | -   (- unless verdict is FALSE)
Rules (each a refusal): a reader or confirmer is never the author (never equals b_episode); the confirmer is never the
reader; a FALSE carries a confirmer and yes|no|UNSCORED; an OK or UNSCORED carries - and -; one row per (b_episode,
sentence, reader); one sentence_sha256 per (b_episode, sentence).
THE POPULATION (A3.1, systems' C1) is REQUIRED: `--population sentences.tsv` is the frozen file `o90_sentences.py` wrote. Every
log row must be a frozen `given=no` row with the same problem, arm and sha (a GIVEN sentence is read by no one), and for each
mechanism in the log, every written sentence must have a row of that mechanism (a sentence not read is written UNSCORED, never
left out, so a halted set is counted rather than shrunk).
Readings: (1) PER ARTIFACT — a sentence is FALSE iff some read flagged it AND its confirmation is yes [F8c]; an artifact with
ANY unscored sentence (a read UNSCORED, or a confirmation UNSCORED) is UNSCORED on this rule, printed per arm (A3.4 M2).
(2) PER SENTENCE, the A3.4b decision — confirmed-FALSE against not over the written SCORED sentences, a5 against a0, one-sided
Fisher exact p, whole and doc-comment-only (A3.7 4's length-matched read), beside each arm's per-sentence FLAG rate per
mechanism. (3) evidence's leg (c) analogue — the share of FALSE flags NOT confirmed, per mechanism and per arm.
Nothing here scores a reader against a key: stage 1 has no planted key (schedule §4).
  usage: o90_flaglog.py <log.tsv> --population <sentences.tsv>      ·      o90_flaglog.py --selftest"""
import csv, collections, io, math, sys
COLS = ["problem", "arm", "b_episode", "sentence", "sentence_sha256", "reader", "mechanism", "verdict", "confirmer", "confirmed"]
POP_COLS = ["problem", "arm", "b_episode", "sentence", "sentence_sha256", "given", "text"]
def load_population(f):
    rows = [r for r in csv.reader((l for l in f if not l.startswith("#")), delimiter="\t", quoting=csv.QUOTE_NONE)]
    if not rows or rows[0] != POP_COLS: raise SystemExit("REFUSE: population header must be exactly: " + "\t".join(POP_COLS))
    pop = {}
    for r in rows[1:]:
        d = dict(zip(POP_COLS, r)); pop[(d["b_episode"], d["sentence"])] = d
    return pop
def load(f, pop):
    rows = list(csv.reader(f, delimiter="\t"))
    if not rows or rows[0] != COLS: raise SystemExit("REFUSE: header must be exactly: " + "\t".join(COLS))
    out, seen, shas = [], set(), {}
    for n, r in enumerate(rows[1:], 2):
        if len(r) != len(COLS): raise SystemExit("REFUSE line %d: %d fields, want %d" % (n, len(r), len(COLS)))
        d = dict(zip(COLS, r))
        if d["arm"] not in ("a0", "a5"): raise SystemExit("REFUSE line %d: arm %r" % (n, d["arm"]))
        if d["mechanism"] not in ("gemini", "claude"): raise SystemExit("REFUSE line %d: mechanism %r" % (n, d["mechanism"]))
        if d["verdict"] not in ("OK", "FALSE", "UNSCORED"): raise SystemExit("REFUSE line %d: verdict %r" % (n, d["verdict"]))
        if d["reader"] == d["b_episode"] or d["confirmer"] == d["b_episode"]: raise SystemExit("REFUSE line %d: a read by the author" % n)
        if d["verdict"] == "FALSE":
            if d["confirmer"] in ("-", "") or d["confirmed"] not in ("yes", "no", "UNSCORED"):
                raise SystemExit("REFUSE line %d: a FALSE needs a confirmer and yes|no|UNSCORED" % n)
            if d["confirmer"] == d["reader"]: raise SystemExit("REFUSE line %d: the confirmer is the reader" % n)
        elif (d["confirmer"], d["confirmed"]) != ("-", "-"): raise SystemExit("REFUSE line %d: an %s carries - and -" % (n, d["verdict"]))
        k = (d["b_episode"], d["sentence"], d["reader"])
        if k in seen: raise SystemExit("REFUSE line %d: duplicate read %r" % (n, k))
        seen.add(k)
        s = shas.setdefault((d["b_episode"], d["sentence"]), d["sentence_sha256"])
        if s != d["sentence_sha256"]: raise SystemExit("REFUSE line %d: sentence %r read as two different texts" % (n, d["sentence"]))
        p = pop.get((d["b_episode"], d["sentence"]))
        if p is None: raise SystemExit("REFUSE line %d: %r is not a sentence of the frozen population" % (n, (d["b_episode"], d["sentence"])))
        if p["given"] != "no": raise SystemExit("REFUSE line %d: %r is GIVEN text, read by no one (A3.1)" % (n, d["sentence"]))
        if (p["problem"], p["arm"], p["sentence_sha256"]) != (d["problem"], d["arm"], d["sentence_sha256"]):
            raise SystemExit("REFUSE line %d: problem, arm or sha differs from the frozen row" % n)
        out.append(d)
    written = {k for k, p in pop.items() if p["given"] == "no"}
    for mech in sorted({d["mechanism"] for d in out}):
        missing = written - {(d["b_episode"], d["sentence"]) for d in out if d["mechanism"] == mech}
        if missing: raise SystemExit("REFUSE: %d written sentence(s) have no %s row (write UNSCORED, never omit), e.g. %r"
                                     % (len(missing), mech, sorted(missing)[0]))
    return out
def fisher_greater(f5, n5, f0, n0):
    """One-sided Fisher exact p that a5's rate exceeds a0's: P(X >= f5), X hypergeometric over the pooled table."""
    N, K = n5 + n0, f5 + f0
    if N == 0 or n5 == 0: return float("nan")
    tot = math.comb(N, n5)
    return sum(math.comb(K, x) * math.comb(N - K, n5 - x) for x in range(f5, min(K, n5) + 1)) / tot
def readings(rows, pop):
    by_s = collections.defaultdict(list)
    for r in rows: by_s[(r["b_episode"], r["sentence"])].append(r)
    state = {}
    for k, rs in by_s.items():
        if any(r["verdict"] == "UNSCORED" or r["confirmed"] == "UNSCORED" for r in rs): state[k] = "UNSCORED"
        else: state[k] = "FALSE" if any(r["verdict"] == "FALSE" and r["confirmed"] == "yes" for r in rs) else "OK"
    arts = sorted({(pop[k]["problem"], pop[k]["arm"], k[0]) for k in by_s})
    axis = []
    for p, a, e in arts:
        ss = [v for k, v in state.items() if k[0] == e]
        axis.append((p, a, e, "UNSCORED" if "UNSCORED" in ss else ss.count("FALSE")))
    per = {}
    for scope in ("whole", "doc"):
        c = {a: [0, 0] for a in ("a0", "a5")}
        for k, v in state.items():
            if v == "UNSCORED" or (scope == "doc" and not k[1].startswith("doc:")): continue
            c[pop[k]["arm"]][0] += v == "FALSE"; c[pop[k]["arm"]][1] += 1
        per[scope] = (c, fisher_greater(c["a5"][0], c["a5"][1], c["a0"][0], c["a0"][1]))
    flag = collections.defaultdict(lambda: [0, 0])
    fa = collections.defaultdict(lambda: [0, 0])
    for r in rows:
        if r["verdict"] != "UNSCORED":
            flag[(r["mechanism"], r["arm"])][0] += r["verdict"] == "FALSE"; flag[(r["mechanism"], r["arm"])][1] += 1
        if r["verdict"] == "FALSE":
            for key in ((r["mechanism"], r["arm"]), (r["mechanism"], "*"), ("*", r["arm"])):
                fa[key][0] += 1; fa[key][1] += (r["confirmed"] == "no")
    return axis, per, dict(flag), dict(fa)
def report(rows, pop):
    axis, per, flag, fa = readings(rows, pop)
    print("PER ARTIFACT (a sentence is FALSE iff flagged AND confirmed yes; any unscored sentence makes it UNSCORED):")
    for p, a, e, n in axis: print("  %s %s %s %s%s" % (p, a, e, n, "  <- carries a FALSE sentence" if n not in (0, "UNSCORED") else ""))
    for a in ("a0", "a5"): print("  UNSCORED artifacts %s: %d" % (a, sum(1 for x in axis if x[1] == a and x[3] == "UNSCORED")))
    for scope, (c, p) in per.items():
        print("PER SENTENCE (%s): a5 %d / %d · a0 %d / %d confirmed FALSE of scored written sentences · one-sided Fisher p = %.4f"
              % (scope, c["a5"][0], c["a5"][1], c["a0"][0], c["a0"][1], p))
    print("FLAG RATE per sentence (mechanism, arm): FALSE flags / scored reads")
    for k in sorted(flag): print("  %-8s %-3s %d / %d" % (k[0], k[1], flag[k][0], flag[k][1]))
    print("FALSE FLAGS NOT CONFIRMED (mechanism, arm): not_confirmed / flags")
    for k in sorted(fa): print("  %-8s %-3s %d / %d" % (k[0], k[1], fa[k][1], fa[k][0]))
def selftest():
    P = "\t".join(POP_COLS) + "\n" + "".join("\t".join(x) + "\n" for x in [
        ["31", "a5", "ep-b5", "doc:1", "aa", "no", "t"], ["31", "a5", "ep-b5", "explain:1", "bb", "no", "t"],
        ["31", "a0", "ep-b0", "doc:1", "cc", "no", "t"], ["31", "a0", "ep-b0", "doc:2", "ee", "yes", "given"],
        ["32", "a5", "ep-c5", "explain:1", "ff", "no", "t"]]) + "# TOTAL\n"
    pop = load_population(io.StringIO(P))
    H = "\t".join(COLS) + "\n"
    base = [["31", "a5", "ep-b5", "doc:1", "aa", "g1", "gemini", "FALSE", "c1", "yes"],
            ["31", "a5", "ep-b5", "explain:1", "bb", "g1", "gemini", "FALSE", "c1", "no"],
            ["31", "a0", "ep-b0", "doc:1", "cc", "g2", "gemini", "OK", "-", "-"],
            ["32", "a5", "ep-c5", "explain:1", "ff", "g3", "gemini", "UNSCORED", "-", "-"]]
    good = H + "".join("\t".join(x) + "\n" for x in base)
    rows = load(io.StringIO(good), pop); axis, per, flag, fa = readings(rows, pop)
    assert axis == [("31", "a0", "ep-b0", 0), ("31", "a5", "ep-b5", 1), ("32", "a5", "ep-c5", "UNSCORED")], axis
    assert per["whole"][0] == {"a0": [0, 1], "a5": [1, 2]} and per["doc"][0] == {"a0": [0, 1], "a5": [1, 1]}, per
    assert flag[("gemini", "a5")] == [2, 2] and flag[("gemini", "a0")] == [0, 1], flag
    assert fa[("gemini", "a5")] == [2, 1], fa
    assert abs(fisher_greater(5, 10, 0, 10) - 252 / 15504) < 1e-12, fisher_greater(5, 10, 0, 10)
    assert abs(fisher_greater(0, 10, 5, 10) - 1.0) < 1e-12
    r2 = [list(x) for x in base]; r2[1][9] = "UNSCORED"
    assert readings(load(io.StringIO(H + "".join("\t".join(x) + "\n" for x in r2)), pop), pop)[0][1][3] == "UNSCORED"
    bad = {"author reads": ["31", "a5", "ep-b5", "doc:1", "aa", "ep-b5", "claude", "OK", "-", "-"],
           "FALSE w/o confirmer": ["31", "a5", "ep-b5", "doc:1", "aa", "k2", "claude", "FALSE", "-", "-"],
           "confirmer is reader": ["31", "a5", "ep-b5", "doc:1", "aa", "k2", "claude", "FALSE", "k2", "yes"],
           "OK with confirmer": ["31", "a5", "ep-b5", "doc:1", "aa", "k2", "claude", "OK", "c1", "yes"],
           "UNSCORED with confirmer": ["31", "a5", "ep-b5", "doc:1", "aa", "k2", "claude", "UNSCORED", "c1", "yes"],
           "two texts": ["31", "a5", "ep-b5", "doc:1", "zz", "g9", "gemini", "OK", "-", "-"],
           "duplicate read": ["31", "a5", "ep-b5", "doc:1", "aa", "g1", "gemini", "OK", "-", "-"],
           "bad mechanism": ["31", "a5", "ep-b5", "doc:1", "aa", "g2", "gpt", "OK", "-", "-"],
           "not in population": ["31", "a5", "ep-b5", "doc:9", "aa", "g9", "gemini", "OK", "-", "-"],
           "a GIVEN sentence read": ["31", "a0", "ep-b0", "doc:2", "ee", "g9", "gemini", "OK", "-", "-"],
           "sha differs from frozen": ["31", "a5", "ep-b5", "doc:1", "aa", "g9", "gemini", "OK", "-", "-"][:4] + ["xx", "g9", "gemini", "OK", "-", "-"],
           "a mechanism that misses a written sentence": ["31", "a5", "ep-b5", "doc:1", "aa", "k1", "claude", "OK", "-", "-"]}
    for name, row in bad.items():
        try: load(io.StringIO(good + "\t".join(row) + "\n"), pop); raise AssertionError("ACCEPTED: " + name)
        except SystemExit as e: assert str(e).startswith("REFUSE"), (name, e)
    print("SELFTEST PASS: 1 good log (per artifact 0 / 1 / UNSCORED; per sentence whole a5 1/2 a0 0/1, doc a5 1/1 a0 0/1;"
          " Fisher 5/10 vs 0/10 = 252/15504), an UNSCORED confirmation makes its artifact UNSCORED, %d refusals each fired" % len(bad))
if __name__ == "__main__":
    if sys.argv[1:] == ["--selftest"]: selftest(); sys.exit(0)
    if len(sys.argv) != 4 or sys.argv[2] != "--population": raise SystemExit(__doc__)
    pop = load_population(open(sys.argv[3], newline=""))
    report(load(open(sys.argv[1], newline=""), pop), pop)
