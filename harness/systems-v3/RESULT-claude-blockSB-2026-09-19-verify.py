#!/usr/bin/env python3
"""Re-derive every headline figure of RESULT-claude-blockSB-2026-09-19.md from the table of record
and assert it against the BYTES of that document.  IDIOM LAW clause 1: no expectation is typed here.
Every value asserted is COMPUTED from the TSV and then searched for in the .md; a figure that drifts
in either file turns this red.

  usage:  python3 RESULT-claude-blockSB-2026-09-19-verify.py [--doc <md>] [--cells <tsv>]
  exit 0  every arm green        exit 1  any arm red        exit 2  could not read an input

⛔ WHAT THIS DOES NOT DO (limits ride with verdicts): it checks that the DOCUMENT agrees with the
TABLE. It does not re-score a cell, does not re-run a suite, and cannot tell you the table is right.
"""
import csv, sys, re, os

DOC = "RESULT-claude-blockSB-2026-09-19.md"
TSV = "RESULT-claude-blockSB-2026-09-19-cells.tsv"
a = sys.argv[1:]
if "--doc" in a:   DOC = a[a.index("--doc") + 1]
if "--cells" in a: TSV = a[a.index("--cells") + 1]

try:
    doc = open(DOC, encoding="utf-8").read()
    rows = list(csv.DictReader(open(TSV, encoding="utf-8"), delimiter="\t"))
except OSError as e:
    print("CANNOT READ INPUT: %s" % e); sys.exit(2)

N = [0, 0]
DATA_ARMS = [0]          # arms minted per-row rather than per-program: see the LIMITS block at the end
def arm(label, ok, shown="", data_dependent=False):
    if data_dependent: DATA_ARMS[0] += 1
    N[0] += 1; N[1] += 0 if ok else 1
    print("  %s  %s%s" % ("ok  " if ok else "RED ", label, ("   [%s]" % shown) if shown else ""))

def insrc(s):
    """the derived value must appear in the document, with thousands separators tolerated"""
    return s in doc or s.replace(",", "") in doc

F = lambda r, k: float(r[k])
P = [r for r in rows if r["arm"] == "plain"]
S = [r for r in rows if r["arm"] == "salt-diet"]

print("POPULATION")
arm("the table has rows", len(rows) > 0, str(len(rows)))
arm("the document states the cell count", insrc(str(len(rows))), "%d cells" % len(rows))
conds = sorted(set((r["problem"], r["arm"]) for r in rows))
arm("the document states the condition count", insrc(str(len(conds))), "%d conditions" % len(conds))
per = sorted(set(sum(1 for x in rows if (x["problem"], x["arm"]) == c) for c in conds))
arm("EVERY condition ran the same number of cells", len(per) == 1, "cells per condition %s" % per)
arm("the document states that number", insrc("%d of %d" % (per[0], per[0])), "%d of %d" % (per[0], per[0]))

print("\nCEILINGS (§1)")
npass = sum(1 for r in rows if r["suite"] == "PASS")
arm("suite PASS count is derived and appears", insrc("PASS %d/%d" % (npass, len(rows))), "PASS %d/%d" % (npass, len(rows)))
arm("⭐ the CEILING claim is TRUE of the table (no non-PASS row)", npass == len(rows))
v1 = {}
for r in rows: v1[r["V1_bugs_fixed"]] = v1.get(r["V1_bugs_fixed"], 0) + 1
arm("no V1 cell is UNMEASURED", "UNMEASURED" not in v1, str(sorted(v1.items())))
for k, c in sorted(v1.items()):
    arm("the V1 tally %s x%d appears" % (k, c), insrc("%s ×%d" % (k, c)) or insrc("%s x%d" % (k, c)))

print("\nRUN STATE (§3)")
rs = {}
for r in rows: rs[r["run_state"]] = rs.get(r["run_state"], 0) + 1
for k, c in sorted(rs.items()):
    arm("run_state %s = %d appears" % (k, c), insrc("%s %d" % (k.replace("ENDED: ", ""), c)))
landed = rs.get("ENDED: LANDED", 0)
arm("⭐ self-graded LANDED is BELOW verified PASS (the inversion §3 claims)", landed < npass,
    "LANDED %d < PASS %d" % (landed, npass))
arm("the document states that pair", insrc("%d of %d" % (landed, len(rows))) and insrc("%d of %d" % (npass, len(rows))))
arm("every row is TERMINAL (run_state starts ENDED:)", all(r["run_state"].startswith("ENDED:") for r in rows))
arm("w1_fenced is COVERED on every row", all(r["w1_fenced"] == "COVERED" for r in rows))

print("\nRETENTION, SURVIVAL, GROWTH (§5)")
for nm, L in (("plain", P), ("salt-diet", S)):
    for col, fmt in (("retained", "%.3f"), ("surv", "%.3f")):
        lo, hi = min(F(r, col) for r in L), max(F(r, col) for r in L)
        arm("%s %s range appears" % (nm, col), insrc((fmt + " .. " + fmt) % (lo, hi)), (fmt + ".." + fmt) % (lo, hi))
    lo, hi = min(F(r, "growth") for r in L), max(F(r, "growth") for r in L)
    arm("%s growth range appears" % nm, insrc("%.2fx .. %5.2fx" % (lo, hi)) or insrc("%.2fx .. %.2fx" % (lo, hi)),
        "%.2fx..%.2fx" % (lo, hi))
dis_ret = [t for t in sorted(set(r["problem"] for r in rows))
           if min(F(r, "retained") for r in P if r["problem"] == t) > max(F(r, "retained") for r in S if r["problem"] == t)]
dis_sur = [t for t in sorted(set(r["problem"] for r in rows))
           if min(F(r, "surv") for r in P if r["problem"] == t) > max(F(r, "surv") for r in S if r["problem"] == t)]
nprob = len(set(r["problem"] for r in rows))
arm("retained disjointness count is derived and appears", insrc("DISJOINT %d of %d" % (len(dis_ret), nprob)),
    "retained DISJOINT %d of %d" % (len(dis_ret), nprob))
arm("survival disjointness count is derived and appears", insrc("DISJOINT %d of %d" % (len(dis_sur), nprob)),
    "surv DISJOINT %d of %d" % (len(dis_sur), nprob))
arm("⭐ the claim that survival separates LESS than retained is TRUE of the table", len(dis_sur) < len(dis_ret))
lzw_p = [r for r in P if r["problem"] == "LZW"]; lzw_s = [r for r in S if r["problem"] == "LZW"]
arm("⭐ §5's LZW REVERSAL is real: retained says plain>salt, surv says salt>plain",
    min(F(r, "retained") for r in lzw_p) > max(F(r, "retained") for r in lzw_s)
    and min(F(r, "surv") for r in lzw_s) > min(F(r, "surv") for r in lzw_p))
# §5's pair deliberately sets the block's highest-survival cell (a SALT cell) against the
# lowest-survival PLAIN cell — one from each arm. The block minimum (clbbps03, 0.419) is a salt
# cell and would make the pair same-arm, which proves nothing about the two arms.
hi = max(rows, key=lambda r: F(r, "surv"))
lo = min(P, key=lambda r: F(r, "surv"))
blockmin = min(rows, key=lambda r: F(r, "surv"))
arm("the HIGHEST-survival cell named in §5 is the table's", insrc(hi["cell"]), "%s surv %s" % (hi["cell"], hi["surv"]))
arm("the lowest-survival PLAIN cell named in §5 is the table's", insrc(lo["cell"]), "%s surv %s" % (lo["cell"], lo["surv"]))
arm("⭐ THE PAIR: the highest-survival cell scores WORSE on retained than the lowest-survival plain one",
    F(hi, "retained") < F(lo, "retained"), "%s %s < %s %s" % (hi["cell"], hi["retained"], lo["cell"], lo["retained"]))
arm("both their retained values appear", insrc(hi["retained"]) and insrc(lo["retained"]))
arm("⭐ §5's caveat is required AND present: the block minimum is a DIFFERENT cell, and it is named",
    blockmin["cell"] != lo["cell"] and insrc(blockmin["cell"]) and insrc(blockmin["surv"]),
    "block min %s %s vs plain min %s %s" % (blockmin["cell"], blockmin["surv"], lo["cell"], lo["surv"]))
rep = {a_: sum(1 for r in rows if r["arm"] == a_ and r["class"] == "REPLACED") for a_ in ("plain", "salt-diet")}
for a_ in ("plain", "salt-diet"):
    arm("REPLACED %d of %d for %s appears" % (rep[a_], len(P if a_ == "plain" else S), a_),
        insrc("%d of %d" % (rep[a_], len(P if a_ == "plain" else S))))
replaced_surv = [F(r, "surv") for r in rows if r["class"] == "REPLACED"]
if replaced_surv:
    arm("§5's 'REPLACED cells retained X..Y of the given' band is derived and appears",
        insrc("%.1f–%.1f %%" % (min(replaced_surv) * 100, max(replaced_surv) * 100))
        or insrc("%.1f-%.1f %%" % (min(replaced_surv) * 100, max(replaced_surv) * 100)),
        "%.1f-%.1f%%" % (min(replaced_surv) * 100, max(replaced_surv) * 100))

print("\nTHE CAP (§6)")
cap_by = {a_: sum(1 for r in rows if r["arm"] == a_ and r["capped"] == "YES") for a_ in ("plain", "salt-diet")}
arm("the cap counts appear, per arm",
    insrc("salt-diet %d of %d" % (cap_by["salt-diet"], len(S))) and insrc("plain %d of %d" % (cap_by["plain"], len(P))),
    str(cap_by))
arm("⭐ the cap binds ONE arm only, which is what makes §6 a treatment claim",
    cap_by["plain"] == 0 and cap_by["salt-diet"] > 0)
caps = set(r["cap"] for r in rows)
arm("one cap value across the block, and it appears", len(caps) == 1 and insrc(list(caps)[0]), str(caps))
for r in [x for x in rows if x["capped"] == "YES"]:
    arm("capped cell %s and its cost appear" % r["cell"], insrc(r["cell"]) and insrc(r["final_COST"]),
        data_dependent=True)

print("\nTOKENS AND COST (§7)")
for col, fmt, xf in (("final_T", "{:,.0f}", "%.2fx"), ("final_COST", "{:.4f}", "%.2fx")):
    for t in sorted(set(r["problem"] for r in rows)) + ["TOTAL"]:
        sel = (lambda L: L if t == "TOTAL" else [r for r in L if r["problem"] == t])
        p = sum(F(r, col) for r in sel(P)); s = sum(F(r, col) for r in sel(S))
        arm("%s %s plain appears" % (t, col), insrc(fmt.format(p)), fmt.format(p))
        arm("%s %s salt appears" % (t, col), insrc(fmt.format(s)), fmt.format(s))
        arm("%s %s ratio appears" % (t, col), insrc(xf % (s / p)), xf % (s / p))

print("\nTHE CENSUS (ADDENDUM 11) — the move must equal the table's condition count, and both views must close")
CEN = "CENSUS-full-matrix-2026-09-14.md"
if "--census" in a: CEN = a[a.index("--census") + 1]
try:
    cen = open(CEN, encoding="utf-8").read()
except OSError as e:
    arm("census readable", False, str(e)); cen = ""
if cen:
    # ⛔ take the LAST match, never the first: this is an APPEND-ONLY document and re.search would
    #    hand back ADDENDUM 10's line forever (the defect that reddened level 7's verifier).
    mv = re.findall(r"DONE (\d+) · OWED (\d+) · BLOCKED (\d+) · INEXPR (\d+)\s+= 200", cen)
    arm("the census states a 200-view total at all", bool(mv), str(mv[-1:]))
    if mv:
        d, o, b, i = (int(x) for x in mv[-1])
        arm("200-view closes: DONE+OWED+BLOCKED+INEXPR == 200", d + o + b + i == 200, "%d+%d+%d+%d" % (d, o, b, i))
        prev = re.findall(r">\s+ADDENDUM 10\s+DONE (\d+) · OWED\s+(\d+)", cen)
        arm("the trajectory box carries the PREVIOUS addendum's row", bool(prev), str(prev[-1:]))
        if prev:
            pd, po = int(prev[-1][0]), int(prev[-1][1])
            arm("⭐ THE MOVE EQUALS THE TABLE'S CONDITION COUNT", d - pd == len(conds),
                "DONE %d -> %d = +%d, conditions in the table %d" % (pd, d, d - pd, len(conds)))
            arm("⭐ OWED FALLS BY THE SAME AMOUNT (no condition invented or lost)", po - o == d - pd,
                "OWED %d -> %d = -%d" % (po, o, po - o))
        live = re.findall(r">\s+LIVE \(ADDENDUM \d+\) DONE (\d+) · OWED (\d+)", cen)
        arm("the trajectory box's LIVE row exists and matches the §R1 total", bool(live) and (int(live[-1][0]), int(live[-1][1])) == (d, o),
            str(live[-1:]))
        arm("the 240-view is stated and closes", ("DONE %d · OWED %d · BLOCKED 0 · INEXPR %d" % (d, o, i + 40)) in cen,
            "240-view INEXPR %d, total %d" % (i + 40, d + o + i + 40))
        arm("no condition is BLOCKED", b == 0)
        arm("the result document and the census agree on the condition count", insrc(str(len(conds))))

print("\nCLOSURE ARMS — `systems`' finding of 2026-09-19 against its own signature of this tool")
# ⛔⛔ `insrc()` IS PURE CONTAINMENT, so an edit to ONE occurrence of a figure the document states
#    MORE THAN ONCE is invisible: `systems` drove three (M7/M8/M9) that each left the document
#    SELF-CONTRADICTING — two different total-token premiums, two different suite ceilings — with
#    this program printing 90 arms, 0 RED. It is the containment defect bench had found in the
#    SIBLING verifier NINE MINUTES EARLIER and did not carry across. ⇒ A DEFECT REPAIRED IN ONE
#    TOOL IS NOT REPAIRED IN ITS CLASS.
# ✅ THE FORM HERE IS DELIBERATELY *NOT* LABEL-ANCHORED, because `systems`' own remedy missed M9 on
#    a SINGLE EXTRA SPACE in `suite··PASS`: an anchored arm only moves the question to "does my label
#    select every line that makes this claim?". These arms take EVERY token OF THE RIGHT SHAPE in the
#    whole document and require each to be a value DERIVED from the table. No label, no population
#    judgement, nothing for a space to defeat.
derived_ratios = set()
for col, in (("final_T",), ("final_COST",)):
    for t in sorted(set(r["problem"] for r in rows)) + ["TOTAL"]:
        sel = (lambda L: L if t == "TOTAL" else [r for r in L if r["problem"] == t])
        p_ = sum(F(r, col) for r in sel(P)); s_ = sum(F(r, col) for r in sel(S))
        derived_ratios.add("%.2fx" % (s_ / p_))
for L in (P, S):
    for fn in (min, max):
        derived_ratios.add("%.2fx" % fn(F(r, "growth") for r in L))
seen_ratios = set(re.findall(r"\d+\.\d\dx", doc))
stray = sorted(seen_ratios - derived_ratios)
arm("⭐ EVERY `N.NNx` IN THE DOCUMENT IS A RATIO DERIVED FROM THE TABLE", not stray,
    "%d distinct in doc, %d derived, stray %s" % (len(seen_ratios), len(derived_ratios), stray or "none"))
derived_pass = {"PASS %d/%d" % (npass, len(rows))}
seen_pass = set(re.findall(r"PASS\s+\d+/\d+", doc))
seen_pass = {" ".join(x.split()) for x in seen_pass}
arm("⭐ EVERY `PASS n/m` IN THE DOCUMENT IS THE DERIVED SUITE VERDICT", seen_pass <= derived_pass,
    "in doc %s, derived %s" % (sorted(seen_pass), sorted(derived_pass)))
cell_vals = set()
for r in rows:
    for c in ("retained", "surv"): cell_vals.add("%.3f" % F(r, c))
for L in (P, S):
    for c in ("retained", "surv"):
        cell_vals.add("%.3f" % min(F(r, c) for r in L)); cell_vals.add("%.3f" % max(F(r, c) for r in L))
# ⛔ AND THE DERIVED SET HAS TO INCLUDE WHAT THE DOCUMENT LEGITIMATELY QUOTES FROM ELSEWHERE, or the
#    arm reddens on correct text. Three strays on the first run — 0.001, 0.107, 0.291 — were all real:
#    §5's "lower by 0.001" (a DIFFERENCE) and §8 item 6's level-7 band (ANOTHER DOCUMENT'S numbers).
#    They are DERIVED here too, from the objects they came from, rather than typed into an allow-list.
blockmin_surv = min(F(r, "surv") for r in rows); plainmin_surv = min(F(r, "surv") for r in P)
cell_vals.add("%.3f" % (plainmin_surv - blockmin_surv))          # §5's caveat, a difference
try:
    L7 = [r for r in csv.DictReader(open("RESULT-gemini-level7-2026-09-19-cells.tsv", encoding="utf-8"),
                                    delimiter="\t") if r["field"] == "brownfield" and r["retained"] not in ("-", "")]
    for a_ in ("plain", "salt-diet"):
        v = [float(r["retained"]) for r in L7 if r["arm"] == a_]
        cell_vals.add("%.3f" % min(v)); cell_vals.add("%.3f" % max(v))
    l7ok = True
except OSError:
    l7ok = False
arm("§8 item 6's level-7 band is derived FROM LEVEL 7's OWN TABLE, not typed", l7ok)
seen3 = set(re.findall(r"(?<![\d.])0\.\d{3}(?![\d])", doc))
stray3 = sorted(seen3 - cell_vals)
arm("⭐ EVERY THREE-DECIMAL 0.xyz IN THE DOCUMENT IS A VALUE THE TABLE CARRIES", not stray3,
    "%d distinct in doc, stray %s" % (len(seen3), stray3 or "none"))
arm("⛔ and these three arms are NOT label-anchored, which is the point",
    True, "shape-scoped: N.NNx / PASS n/m / 0.xyz — no section, no heading, no spacing assumption")

print("\nANTI-VACUITY — these arms must be able to go RED")
mut = doc.replace("18.59x", "18.60x")   # ALL occurrences: the ratio is quoted in three sections
saved, globals()["doc"] = doc, mut
p = sum(F(r, "final_T") for r in P); s = sum(F(r, "final_T") for r in S)
would_red = not insrc("%.2fx" % (s / p))
globals()["doc"] = saved
arm("⭐ MUTANT: changing the total-token ratio by 0.01 in the document reddens the arm that names it", would_red)
arm("⭐ a value NOT in the document is not found (insrc is not vacuously true)", not insrc("__NOT_IN_THIS_DOCUMENT__"))

# ⛔⛔ THE LIMITS RIDE WITH THE VERDICT, AND THEY DID NOT UNTIL 2026-09-19.
#    `systems` found it at its non-author signature: this file's docstring carries the header
#    "limits ride with verdicts" and named four limits, and ZERO of them appeared in the 5,784 B
#    this program printed. A reader ran it, saw "90 arms, 0 RED", and never met the sentence saying
#    this cannot tell you the table is right. ⇒ THE IDIOM LAW'S CLAUSE (b) FAILING INSIDE A TOOL
#    WHOSE DOCSTRING NAMES THE LAW. The fix is a print, in the same act as the count.
# ⛔ AND THE ARM COUNT IS DATA-DEPENDENT — `systems`' finding (C). The capped-cell loop mints one arm
#    per capped cell, so a table with one fewer capped cell prints 89 and still reads as success.
#    The count is therefore SPLIT below, so a reader can tell an instrument change from a data change.
print("\n%d arms, %d RED   (%d fixed + %d data-dependent: 1 per capped cell, %d capped here)"
      % (N[0], N[1], N[0] - DATA_ARMS[0], DATA_ARMS[0], DATA_ARMS[0]))
print("LIMITS, beside the verdict and not only in the source:")
print("  · this checks that the DOCUMENT agrees with the TABLE and that the CENSUS's move equals the")
print("    table's condition count. IT CANNOT TELL YOU THE TABLE IS RIGHT.")
print("  · it does not re-score a cell, does not re-run a suite, and does not reach the run box.")
print("  · the arm COUNT is partly a claim about the data (see the split above), so a changed count")
print("    is not by itself an instrument failure — read the split, never the total.")
print("  · a COMPENSATED forgery of the census (every surface moved consistently) is caught by exactly")
print("    ONE arm here, the cross-object MOVE arm. That class has no redundancy in this file.")
sys.exit(1 if N[1] else 0)
