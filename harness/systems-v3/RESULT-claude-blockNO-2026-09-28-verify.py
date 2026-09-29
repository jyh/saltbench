#!/usr/bin/env python3
"""RESULT-claude-blockNO-2026-09-28-verify.py [--print] — re-derive every figure in the block N Opus result
FROM ITS TWO TABLES, and assert each derived line against the BYTES of the result document.

  tables    evidence/claude-lane-blockN-2026-09-28/blockNO-cells.tsv       (join_cells_table.py, greenfield shape)
            evidence/claude-lane-blockN-2026-09-28/blockNO-cellfacts.tsv   (pool, export, concurrency, fault window, beat)
  document  harness/systems-v3/RESULT-claude-blockNO-2026-09-28.md

--print   print the derived lines (the document quotes them verbatim) and exit 0.
default   rc 0 iff every derived line occurs in the document; rc 1 names each one that does not.
--selftest  two mutants, each must go RED: one PASS turned FAIL in memory, and a capped cell's cost taken at the
          METER instead of at the cap (lane B §Q6 rule 6); then require the
          unmutated check GREEN. A verifier that cannot fail is decoration.

No expected value is typed here. Every line below is computed from the tables; the only literals are the
registered problem ORDER (the freeze's §N3) and the registered cap arithmetic's rule (lane B §Q6 rule 3).
"""
import csv, os, statistics, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
CELLS = os.path.join(ROOT, "evidence/claude-lane-blockN-2026-09-28/blockNO-cells.tsv")
FACTS = os.path.join(ROOT, "evidence/claude-lane-blockN-2026-09-28/blockNO-cellfacts.tsv")
SERVED = os.path.join(ROOT, "evidence/claude-lane-blockN-2026-09-28/blockNO-served.tsv")
DOC = os.path.join(HERE, "RESULT-claude-blockNO-2026-09-28.md")

ORDER = ["Luby", "AES", "Liveness", "MaxFlow", "BinomialHeap", "LinearScan"]   # §N3, ascending reference size
ARMS = ["plain", "salt-diet"]


def read_tsv(path):
    return list(csv.DictReader((l for l in open(path, encoding="utf-8") if not l.startswith("#")), delimiter="\t"))


def med(xs):
    return statistics.median(xs)


def cost(c):
    # lane B §Q6 rule 6: "a capped cell's pass result is a floor and its cost ENTERS AT THE CAP" — the registered
    # convention. The METERED figure of a capped cell overshoots the cap by up to one turn; it is printed on its own line.
    return float(c["cap"]) if c["capped"] == "yes" else float(c["final_COST"])


def derive(cells, facts):
    L = []
    fx = {f["cell"]: f for f in facts}
    assert set(fx) == {c["cell"] for c in cells}, "the two tables name different cells"
    n = len(cells)
    L.append("cells %d · conditions %d · models %s · cap %s %s" % (
        n, len({(c["problem"], c["arm"]) for c in cells}), ",".join(sorted({c["model_served"] for c in cells})),
        ",".join(sorted({c["cap_unit"] for c in cells})), ",".join(sorted({c["cap"] for c in cells}))))
    states = {}
    for c in cells: states[c["run_state"]] = states.get(c["run_state"], 0) + 1
    L.append("run_state " + " · ".join("%s %d" % (k, states[k]) for k in sorted(states)))
    ex = {}
    for c in cells: ex.setdefault((c["problem"] == "LinearScan", fx[c["cell"]]["export"]), 0); ex[(c["problem"] == "LinearScan", fx[c["cell"]]["export"])] += 1
    L.append("export " + " · ".join("%s %s %d" % ("LinearScan" if k[0] else "other-five", k[1], ex[k]) for k in sorted(ex)))
    ef = {}
    for f in facts: ef[f["end_from"]] = ef.get(f["end_from"], 0) + 1
    L.append("end_from " + " · ".join("%s %d" % (k, ef[k]) for k in sorted(ef)))
    # §2 correctness, per condition, verified first (lane B §Q6 rule 1)
    for p in ORDER:
        parts = []
        for a in ARMS:
            rs = [c for c in cells if c["problem"] == p and c["arm"] == a]
            parts.append("%s %d/%d [%s]" % (a, sum(c["suite"] == "PASS" for c in rs), len(rs),
                                            " ".join(c["tests"] for c in sorted(rs, key=lambda c: c["cell"]))))
        L.append("%-12s %s" % (p, " · ".join(parts)))
    for a in ARMS:
        rs = [c for c in cells if c["arm"] == a]
        L.append("FULL PASS %s %d of %d" % (a, sum(c["suite"] == "PASS" for c in rs), len(rs)))
    # §3 cost and the premium, with its verdict kind (lane B §Q6 rule 3: CENSORED -> UNDERPOWERED)
    for p in ORDER:
        m, capped = {}, {}
        for a in ARMS:
            rs = [c for c in cells if c["problem"] == p and c["arm"] == a]
            m[a] = med([cost(c) for c in rs])
            capped[a] = sum(c["capped"] == "yes" for c in rs)
        k = len([c for c in cells if c["problem"] == p and c["arm"] == "salt-diet"])
        # the median of n cells sits AT the cap when more than half are capped: the cap's arithmetic forbids a clearing median
        kind = "UNRESOLVED-CENSORED" if capped["salt-diet"] * 2 > k else "UNRESOLVED-UNDERPOWERED"
        # the ratio carries its own limit (kent's read of #277): a median is a floor when a capped cell sits at or below its
        # position; a floored numerator makes the ratio >=, a floored denominator makes it <=
        def floored(a):
            rs = sorted((cost(c), c["capped"] == "yes") for c in cells if c["problem"] == p and c["arm"] == a)
            return any(cp for _, cp in rs[:len(rs) // 2 + 1])
        nb, db = floored("salt-diet"), floored("plain")
        mark = "bounds only " if nb and db else ("≥ " if nb else ("≤ " if db else ""))
        L.append("%-12s median COST plain $%.2f · salt-diet $%.2f · ratio %s%.1fx · CAP-COST plain %d salt-diet %d · %s" % (
            p, m["plain"], m["salt-diet"], mark, m["salt-diet"] / m["plain"], capped["plain"], capped["salt-diet"], kind))
    for a in ARMS:
        rs = [c for c in cells if c["arm"] == a]
        L.append("total COST (capped at the cap) %s $%.2f · total T %s" % (a, sum(cost(c) for c in rs),
                                                      format(sum(int(c["final_T"]) for c in rs), ",")))
    capd = sorted((c for c in cells if c["capped"] == "yes"), key=lambda c: c["cell"])
    L.append("capped cells METERED (not used above): %d, $%.2f .. $%.2f against cap $%s · metered salt-diet total $%.2f" % (
        len(capd), min(float(c["final_COST"]) for c in capd), max(float(c["final_COST"]) for c in capd), capd[0]["cap"],
        sum(float(c["final_COST"]) for c in cells if c["arm"] == "salt-diet")))
    over = [c for c in cells if c["capped"] == "no" and float(c["final_COST"]) > float(c["cap"])]
    L.append("uncapped cells ending above the cap: %d%s" % (len(over), "".join(
        " (%s $%.2f %s)" % (c["cell"], float(c["final_COST"]), c["run_state"]) for c in over)))
    # §4 the three registered predictions, per arm
    inc = {p: {a: sum(c["capped"] == "yes" for c in cells if c["problem"] == p and c["arm"] == a) for a in ARMS} for p in ORDER}
    held = sum(inc[p]["salt-diet"] >= inc[p]["plain"] for p in ORDER)
    strict = sum(inc[p]["salt-diet"] > inc[p]["plain"] for p in ORDER)
    L.append("(i) salt-diet CAP-COST >= plain in %d of %d problems (%d strictly, %d ties)" % (held, len(ORDER), strict, held - strict))
    for a in ARMS:
        seq = [inc[p][a] for p in ORDER]
        mono = all(x <= y for x, y in zip(seq, seq[1:]))
        rise = all(x < y for x, y in zip(seq, seq[1:]))
        # §N4 registers "rises with reference size across the six" and states no test, so BOTH readings print and neither is
        # called the registration's (kent's read of #277)
        L.append("(ii) %s CAP-COST in reference-size order %s · non-decreasing (weakest reading) %s · strictly rising %s" % (
            a, " ".join(map(str, seq)), "yes" if mono else "NO", "yes" if rise else "NO"))
    wall = sum("CAP-WALL" in c["run_state"] for c in cells)
    L.append("(iii) CAP-WALL cells %d" % wall)
    # §5 the declared columns (ADDENDA 6, 8, 9)
    pools = {}
    for c in cells:
        k = (fx[c["cell"]]["pool"], c["arm"]); pools[k] = pools.get(k, 0) + 1
    L.append("pool x arm " + " · ".join("%s %s %d" % (k[0], k[1], pools[k]) for k in sorted(pools)))
    live = sum(f["claude_live_at_fire"] != "0" for f in facts)
    L.append("claude_live_at_fire >0 in %d of %d cells" % (live, len(facts)))
    fw = sorted(f["cell"] for f in facts if f["fault_window"] == "yes")
    L.append("fault window cells %s" % (" ".join(fw) if fw else "none"))
    sampled = [f for f in facts if f["beat_max_s"] != "-"]
    if sampled:
        top = max(sampled, key=lambda f: int(f["beat_max_s"]))
        L.append("beat sampler: %d cells sampled · max %s s (%s)" % (len(sampled), top["beat_max_s"], top["cell"]))
    else:
        L.append("beat sampler: 0 cells sampled")
    # the served models per cell (served_models_v3.py), so the sidechain count in §3 is a derived line
    if os.path.exists(SERVED):
        sv = read_tsv(SERVED)
        L.append("served: %d of %d cells clean · head claude-opus-5 only in %d · sidechains served claude-sonnet-5 in %d of %d cells" % (
            sum(r["verdict"] == "clean" for r in sv), len(sv), sum(set(x.split("=")[0] for x in r["head"].split()) == {"claude-opus-5"} for r in sv),
            sum("claude-sonnet-5" in r["sidechain"] for r in sv), len(sv)))
    return L


def check(lines, doc):
    return [l for l in lines if l not in doc]


def main():
    cells, facts = read_tsv(CELLS), read_tsv(FACTS)
    if "--print" in sys.argv:
        print("\n".join(derive(cells, facts))); return 0
    doc = open(DOC, encoding="utf-8").read()
    if "--selftest" in sys.argv:
        mut = [dict(c) for c in cells]
        i = next(i for i, c in enumerate(mut) if c["suite"] == "PASS")
        mut[i]["suite"] = "FAIL"
        red = check(derive(mut, facts), doc)
        green = check(derive(cells, facts), doc)
        # arm 2 — the convention kent's read found: a capped cell's cost at the METER instead of at the cap (rule 6)
        global cost
        keep = cost
        cost = lambda c: float(c["final_COST"])
        red2 = check(derive(cells, facts), doc)
        cost = keep
        ok = bool(red) and bool(red2) and not green
        print("selftest: mutant (one PASS -> FAIL in %s) %s with %d missing line(s); unmutated %s" % (
            mut[i]["cell"], "RED" if red else "GREEN (DEFECT)", len(red), "GREEN" if not green else "RED"))
        print("selftest: mutant (capped cost at the METER, not the cap) %s with %d missing line(s)" % (
            "RED" if red2 else "GREEN (DEFECT)", len(red2)))
        return 0 if ok else 1
    miss = check(derive(cells, facts), doc)
    for m in miss: print("MISSING from the document: " + m)
    print("verify: %d derived line(s), %d missing" % (len(derive(cells, facts)), len(miss)))
    return 1 if miss else 0


if __name__ == "__main__":
    sys.exit(main())
