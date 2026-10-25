#!/usr/bin/env python3
"""o90_flaglog.py — the O90 truth axis's FLAG LOG: its schema, its validator, and the readings it exists for (desk AEY;
the design §3 truth row [F8c]; evidence's ask in the 10-23 schedule §4: every flag records its READER and its OUTCOME;
AMENDMENT-O90-stage1 ADDENDUM 3, A3.4a–A3.6, with systems' C1 of 2026-10-25).
One TSV row per (sentence, read). Columns, in order, all required:
  problem    CLEVER id (int)                     arm         a0 | a5
  b_episode  the scored stage-B episode whose artifact the sentence is in (its author)
  sentence   a stable id within the artifact      sentence_sha256  sha256 of the sentence's bytes as read
  reader     the read's id (a session id)         mechanism   gemini | claude      (the reader's model family)
  verdict    OK | FALSE | UNSCORED | HALTED       (FALSE = the reader says the sentence is false of its Lean; UNSCORED = the
             read did not parse; HALTED = only the halt writes it, for a sentence its set did not reach — ADDENDUM 4)
  confirmer  the third read's id, or -            confirmed   yes | no | UNSCORED | -   (- unless verdict is FALSE)
Rules (each a refusal): a reader or confirmer is never the author (never equals b_episode); the confirmer is never the
reader; a FALSE carries a confirmer and yes|no|UNSCORED; an OK, UNSCORED or HALTED carries - and -; one row per (b_episode,
sentence, reader); one sentence_sha256 per (b_episode, sentence).
THE POPULATION (A3.1, systems' C1) is REQUIRED: `--population sentences.tsv` is the frozen file `o90_sentences.py` wrote. Every
log row must be a frozen `given=no` row with the same problem, arm and sha (a GIVEN sentence is read by no one), and for each
mechanism in the log, every written sentence must have a row of that mechanism, never left out: a read that does not parse is
written UNSCORED, and a sentence a halted set did not reach is written HALTED (ADDENDUM 4), so a halted set is counted rather
than shrunk.
Readings: (1) PER ARTIFACT — a sentence is FALSE iff some read flagged it AND its confirmation is yes [F8c]; an artifact with
ANY unscored sentence (a read UNSCORED, or a confirmation UNSCORED) is UNSCORED on this rule, printed per arm (A3.4 M2).
(2) PER SENTENCE, the A3.4b decision — confirmed-FALSE against not over the written SCORED sentences, a5 against a0, one-sided
Fisher exact p, whole and doc-comment-only (A3.7 4's length-matched read), beside each arm's per-sentence FLAG rate per
mechanism. (3) evidence's leg (c) analogue — the share of FALSE flags NOT confirmed, per mechanism and per arm.
Nothing here scores a reader against a key: stage 1 has no planted key (schedule §4).
A set that stopped at an A3.5 halt is named with `--halted <mechanism>`: its rows are left out of the state and the report
declares it, so the figures read "by one reader mechanism" rather than unscoring every sentence it did not reach (systems' E1).
A `--halted` set must carry at least one HALTED verdict row, and a HALTED row of an undeclared mechanism refuses: a halt is a
fact recorded by the halt, not a choice made after the reads (systems' H1 and K1).
  usage: o90_flaglog.py <log.tsv> --population <sentences.tsv> [--halted gemini|claude]      ·      o90_flaglog.py --selftest"""
import csv, collections, hashlib, io, math, sys
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
    out, seen, shas, conf = [], set(), {}, {}
    for n, r in enumerate(rows[1:], 2):
        if len(r) != len(COLS): raise SystemExit("REFUSE line %d: %d fields, want %d" % (n, len(r), len(COLS)))
        d = dict(zip(COLS, r))
        if d["arm"] not in ("a0", "a5"): raise SystemExit("REFUSE line %d: arm %r" % (n, d["arm"]))
        if d["mechanism"] not in ("gemini", "claude"): raise SystemExit("REFUSE line %d: mechanism %r" % (n, d["mechanism"]))
        if d["verdict"] not in ("OK", "FALSE", "UNSCORED", "HALTED"): raise SystemExit("REFUSE line %d: verdict %r" % (n, d["verdict"]))
        if d["reader"] == d["b_episode"] or d["confirmer"] == d["b_episode"]: raise SystemExit("REFUSE line %d: a read by the author" % n)
        if d["verdict"] == "FALSE":
            if d["confirmer"] in ("-", "") or d["confirmed"] not in ("yes", "no", "UNSCORED"):
                raise SystemExit("REFUSE line %d: a FALSE needs a confirmer and yes|no|UNSCORED" % n)
            if d["confirmer"] == d["reader"]: raise SystemExit("REFUSE line %d: the confirmer is the reader" % n)
            c = conf.setdefault((d["b_episode"], d["sentence"], d["confirmer"]), d["confirmed"])
            if c != d["confirmed"]: raise SystemExit("REFUSE line %d: confirmer %r answered %s and %s for one sentence (L3)" % (n, d["confirmer"], c, d["confirmed"]))
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
def readings(rows, pop, halted=()):
    """halted: mechanisms whose set stopped at an A3.5 halt; their rows are left out of the state and declared in the report."""
    by_s = collections.defaultdict(list)
    for r in rows:
        if r["mechanism"] not in halted: by_s[(r["b_episode"], r["sentence"])].append(r)
    state = {}
    for k, p in pop.items():
        if p["given"] != "no": continue
        rs = by_s.get(k, [])
        # E1 (systems): a confirmed FALSE is a fact about the Lean, so it is decided FIRST, whatever another read failed to answer
        if any(r["verdict"] == "FALSE" and r["confirmed"] == "yes" for r in rs): state[k] = "FALSE"
        elif not rs or any(r["verdict"] in ("UNSCORED", "HALTED") or r["confirmed"] == "UNSCORED" for r in rs): state[k] = "UNSCORED"
        else: state[k] = "OK"
    axis = []
    for p_, a, e in sorted({(p["problem"], p["arm"], k[0]) for k, p in pop.items()}):
        ss = [v for k, v in state.items() if k[0] == e]
        axis.append((p_, a, e, "no written prose" if not ss else "UNSCORED" if "UNSCORED" in ss else ss.count("FALSE")))
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
        if r["verdict"] not in ("UNSCORED", "HALTED"):
            flag[(r["mechanism"], r["arm"])][0] += r["verdict"] == "FALSE"; flag[(r["mechanism"], r["arm"])][1] += 1
        if r["verdict"] == "FALSE":
            for key in ((r["mechanism"], r["arm"]), (r["mechanism"], "*"), ("*", r["arm"])):
                fa[key][0] += 1; fa[key][1] += (r["confirmed"] == "no")
    return axis, per, dict(flag), dict(fa)
def report(rows, pop, pop_sha, halted=()):
    axis, per, flag, fa = readings(rows, pop, halted)
    print("POPULATION sha256/16 %s · %d written sentences" % (pop_sha, sum(1 for p in pop.values() if p["given"] == "no")))
    for m in sorted(halted):
        mr = [r for r in rows if r["mechanism"] == m]
        print("HALTED %s: %d rows left out of the state (A3.5), confirmed FALSE %d among them; the per-artifact and per-sentence"
              " figures are by the other mechanism alone, and the flag tables report the halted set at the n it reached"
              % (m, len(mr), sum(1 for r in mr if r["verdict"] == "FALSE" and r["confirmed"] == "yes")))
    print("PER ARTIFACT (a sentence is FALSE iff flagged AND confirmed yes; any unscored sentence makes it UNSCORED):")
    for p, a, e, n in axis: print("  %s %s %s %s%s" % (p, a, e, n, "  <- carries a FALSE sentence" if isinstance(n, int) and n else ""))
    for a in ("a0", "a5"): print("  UNSCORED artifacts %s: %d · no written prose %d" % (a, sum(1 for x in axis if x[1] == a and x[3] == "UNSCORED"),
                                                                                  sum(1 for x in axis if x[1] == a and x[3] == "no written prose")))
    for scope, (c, p) in per.items():
        print("PER SENTENCE (%s): a5 %d / %d · a0 %d / %d confirmed FALSE of scored written sentences · one-sided Fisher p = %.4f%s"
              % (scope, c["a5"][0], c["a5"][1], c["a0"][0], c["a0"][1], p, "".join(" · halted: %s" % m for m in sorted(halted))))
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
    # E1 (systems, shape D): a second read UNSCORED on a sentence read 1 confirmed FALSE does not erase the confirmed FALSE
    r3 = [list(x) for x in base] + [["31", "a5", "ep-b5", "doc:1", "aa", "k1", "claude", "UNSCORED", "-", "-"],
                                    ["31", "a5", "ep-b5", "explain:1", "bb", "k1", "claude", "OK", "-", "-"],
                                    ["31", "a0", "ep-b0", "doc:1", "cc", "k2", "claude", "OK", "-", "-"],
                                    ["32", "a5", "ep-c5", "explain:1", "ff", "k3", "claude", "OK", "-", "-"]]
    a3, p3, _, _ = readings(load(io.StringIO(H + "".join("\t".join(x) + "\n" for x in r3)), pop), pop)
    assert a3[1][3] == 1 and p3["whole"][0]["a5"][0] == 1, ("E1: a confirmed FALSE was erased", a3, p3)
    # E1 (shape C): a HALTED mechanism, declared, is left out of the state rather than unscoring every sentence it did not reach
    r4 = [list(x) for x in base] + [["31", "a5", "ep-b5", "doc:1", "aa", "k1", "claude", "UNSCORED", "-", "-"],
                                    ["31", "a5", "ep-b5", "explain:1", "bb", "k1", "claude", "UNSCORED", "-", "-"],
                                    ["31", "a0", "ep-b0", "doc:1", "cc", "k2", "claude", "UNSCORED", "-", "-"],
                                    ["32", "a5", "ep-c5", "explain:1", "ff", "k3", "claude", "UNSCORED", "-", "-"]]
    l4 = load(io.StringIO(H + "".join("\t".join(x) + "\n" for x in r4)), pop)
    a4, p4, _, _ = readings(l4, pop, halted={"claude"})
    assert [x[3] for x in a4] == [0, 1, "UNSCORED"] and p4["whole"][0] == {"a0": [0, 1], "a5": [1, 2]}, ("C: halted", a4, p4)
    # L1: an artifact with no written sentence is listed as such, so the per-problem pairing need not infer it
    P1 = P.replace("# TOTAL\n", "") + "\t".join(["33", "a0", "ep-d0", "doc:1", "gg", "yes", "given"]) + "\n"
    pop1 = load_population(io.StringIO(P1)); a5_ = readings(load(io.StringIO(good), pop1), pop1)[0]
    assert ("33", "a0", "ep-d0", "no written prose") in a5_, a5_
    bad = {"author reads": ["31", "a5", "ep-b5", "doc:1", "aa", "ep-b5", "claude", "OK", "-", "-"],
           "FALSE w/o confirmer": ["31", "a5", "ep-b5", "doc:1", "aa", "k2", "claude", "FALSE", "-", "-"],
           "confirmer is reader": ["31", "a5", "ep-b5", "doc:1", "aa", "k2", "claude", "FALSE", "k2", "yes"],
           "OK with confirmer": ["31", "a5", "ep-b5", "doc:1", "aa", "k2", "claude", "OK", "c1", "yes"],
           "UNSCORED with confirmer": ["31", "a5", "ep-b5", "doc:1", "aa", "k2", "claude", "UNSCORED", "c1", "yes"],
           "HALTED with confirmer": ["31", "a5", "ep-b5", "doc:1", "aa", "k2", "claude", "HALTED", "c1", "yes"],
           "two texts": ["31", "a5", "ep-b5", "doc:1", "zz", "g9", "gemini", "OK", "-", "-"],
           "duplicate read": ["31", "a5", "ep-b5", "doc:1", "aa", "g1", "gemini", "OK", "-", "-"],
           "bad mechanism": ["31", "a5", "ep-b5", "doc:1", "aa", "g2", "gpt", "OK", "-", "-"],
           "not in population": ["31", "a5", "ep-b5", "doc:9", "aa", "g9", "gemini", "OK", "-", "-"],
           "a GIVEN sentence read": ["31", "a0", "ep-b0", "doc:2", "ee", "g9", "gemini", "OK", "-", "-"],
           "sha differs from frozen": ["31", "a5", "ep-b5", "doc:1", "aa", "g9", "gemini", "OK", "-", "-"][:4] + ["xx", "g9", "gemini", "OK", "-", "-"],
           "a mechanism that misses a written sentence": ["31", "a5", "ep-b5", "doc:1", "aa", "k1", "claude", "OK", "-", "-"],
           "one confirmer, two answers (L3)": ["31", "a5", "ep-b5", "doc:1", "aa", "g5", "gemini", "FALSE", "c1", "no"]}
    for name, row in bad.items():
        try: load(io.StringIO(good + "\t".join(row) + "\n"), pop); raise AssertionError("ACCEPTED: " + name)
        except SystemExit as e: assert str(e).startswith("REFUSE"), (name, e)
    # H1 (systems) + the main-driving arm: a --halted set must carry A3.5's mark (an UNSCORED verdict row), and main's own
    # checks (the value check, both-halted, the POPULATION sha line, the halted count) are driven through a subprocess.
    import os, subprocess, tempfile
    with tempfile.TemporaryDirectory() as t:
        pp, lg = os.path.join(t, "pop.tsv"), os.path.join(t, "log.tsv")
        open(pp, "w").write(P); r5 = [list(x) for x in base] + [["31", "a5", "ep-b5", "doc:1", "aa", "k1", "claude", "OK", "-", "-"],
                                    ["31", "a5", "ep-b5", "explain:1", "bb", "k1", "claude", "OK", "-", "-"],
                                    ["31", "a0", "ep-b0", "doc:1", "cc", "k2", "claude", "OK", "-", "-"],
                                    ["32", "a5", "ep-c5", "explain:1", "ff", "k3", "claude", "OK", "-", "-"]]
        open(lg, "w").write(H + "".join("\t".join(x) + "\n" for x in r5))
        def run(*extra):
            r = subprocess.run([sys.executable, os.path.abspath(__file__), lg, "--population", pp] + list(extra), capture_output=True, text=True)
            return r.returncode, r.stdout + r.stderr
        rc, out = run("--halted", "claude")
        assert rc == 1 and "has no HALTED row" in out, ("H1: a complete set accepted as halted", rc, out)
        # K1 (systems): gemini's set carries an UNSCORED (a PARSE failure, ep-c5), which is not a halt, so it must refuse
        rc, out = run("--halted", "gemini")
        assert rc == 1 and "has no HALTED row" in out, ("K1: a parse failure passed as a halt", rc, out)
        lg_h = os.path.join(t, "log-halted.tsv"); rh = [list(x) for x in r5]; rh[3][7] = "HALTED"
        open(lg_h, "w").write(H + "".join("\t".join(x) + "\n" for x in rh))
        r = subprocess.run([sys.executable, os.path.abspath(__file__), lg_h, "--population", pp, "--halted", "gemini"], capture_output=True, text=True)
        assert r.returncode == 0 and "HALTED gemini" in r.stdout and "confirmed FALSE 1" in r.stdout, ("a marked halt", r.stdout, r.stderr)
        r = subprocess.run([sys.executable, os.path.abspath(__file__), lg_h, "--population", pp], capture_output=True, text=True)
        assert r.returncode == 1 and "undeclared" in r.stdout + r.stderr, ("a HALTED row of an undeclared mechanism", r.stdout, r.stderr)
        # N1 (systems): a HALTED row is not a scored read, so the halted set's flag rate counts only the sentences it reached
        r = subprocess.run([sys.executable, os.path.abspath(__file__), lg_h, "--population", pp, "--halted", "gemini"], capture_output=True, text=True)
        fr = r.stdout.split("FLAG RATE")[1].split("FALSE FLAGS")[0]
        assert "gemini   a5  2 / 2" in fr and "gemini   a0  0 / 1" in fr, ("N1: HALTED counted as a scored read", fr)
        # N2: a declared mechanism with no rows is refused by its own text, not by the HALTED check's
        lg_g = os.path.join(t, "log-gemini-only.tsv"); open(lg_g, "w").write(good)
        r = subprocess.run([sys.executable, os.path.abspath(__file__), lg_g, "--population", pp, "--halted", "claude"], capture_output=True, text=True)
        assert r.returncode == 1 and "claude has no rows" in r.stdout + r.stderr, ("N2", r.stdout, r.stderr)
        rc, out = run()
        assert rc == 0 and ("POPULATION sha256/16 %s" % hashlib.sha256(P.encode()).hexdigest()[:16]) in out, ("L2 via main", out)
        # each refusal by its OWN text: the H1 refusal also exits 1, so an rc-only arm would pass with either check removed
        rv, ov = run("--halted", "gpt"); rb, ob = run("--halted", "claude", "--halted", "gemini")
        assert rv == 1 and "outside gemini | claude" in ov and rb == 1 and "BOTH mechanisms halted" in ob, ("main's refusals", ov, ob)
    print("SELFTEST PASS: 1 good log (per artifact 0 / 1 / UNSCORED; per sentence whole a5 1/2 a0 0/1, doc a5 1/1 a0 0/1;"
          " Fisher 5/10 vs 0/10 = 252/15504), an UNSCORED confirmation makes its artifact UNSCORED, %d refusals each fired" % len(bad))
if __name__ == "__main__":
    if sys.argv[1:] == ["--selftest"]: selftest(); sys.exit(0)
    a = sys.argv[1:]
    if len(a) < 3 or a[1] != "--population" or (len(a) - 3) % 2 or any(x != "--halted" for x in a[3::2]): raise SystemExit(__doc__)
    halted = set(a[4::2])
    if halted - {"gemini", "claude"}: raise SystemExit("REFUSE: --halted names a mechanism outside gemini | claude")
    if halted == {"gemini", "claude"}: raise SystemExit("REFUSE: BOTH mechanisms halted: there is no deciding figure (evidence's F1)")
    raw = open(a[2], "rb").read()
    pop = load_population(io.StringIO(raw.decode("utf-8")))
    rows = load(open(a[0], newline=""), pop)
    for m in sorted(halted):   # H1/K1 (systems): a halt is a fact recorded by the halt itself, never a choice made after the reads
        if not any(r["mechanism"] == m for r in rows): raise SystemExit("REFUSE: --halted %s, but %s has no rows" % (m, m))
        if not any(r["mechanism"] == m and r["verdict"] == "HALTED" for r in rows):
            raise SystemExit("REFUSE: --halted %s, but its set has no HALTED row, so it did not halt (UNSCORED marks a parse failure, not a halt)" % m)
    und = sorted({r["mechanism"] for r in rows if r["verdict"] == "HALTED"} - halted)
    if und: raise SystemExit("REFUSE: HALTED rows of an undeclared mechanism (%s): name it with --halted" % ", ".join(und))
    report(rows, pop, hashlib.sha256(raw).hexdigest()[:16], halted)
