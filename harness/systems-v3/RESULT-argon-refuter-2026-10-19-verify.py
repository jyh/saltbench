#!/usr/bin/env python3
"""RESULT-argon-refuter-2026-10-19-verify.py [--doc D] [--selftest]

Re-derive every figure in RESULT-argon-refuter-2026-10-19.md from the evidence files (the key, both answers, the
manifest, gemini's served-model evidence) and the block tables in evidence/claude-lane-blocks-2026-09-21/, and
assert each against the BYTES of that document. No typed expectations: each expected string is COMPUTED.
rc 0 all figures re-derived and found · 1 a mismatch, named · 2 usage."""
import argparse, csv, hashlib, os, re, statistics, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..", "..")
DOC = os.path.join(HERE, "RESULT-argon-refuter-2026-10-19.md")
EV = os.path.join(ROOT, "evidence", "argon-refuter-2026-10-19")
BL = os.path.join(ROOT, "evidence", "claude-lane-blocks-2026-09-21")

def rows(name):
    p = os.path.join(BL, name)
    return [r for r in csv.DictReader((l for l in open(p, encoding="utf-8") if not l.startswith("#")), delimiter="\t")]

def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()

def ratios(block):
    R = rows("block%s-cells.tsv" % block)
    c = {a: [float(r["final_COST"]) for r in R if r["arm"] == a] for a in ("plain", "salt-diet")}
    T = {a: sum(int(r["final_T"]) for r in R if r["arm"] == a) for a in ("plain", "salt-diet")}
    mp, ms = statistics.median(c["plain"]), statistics.median(c["salt-diet"])
    return dict(med="%.2fx" % (ms / mp), med_rounded="%.2fx" % (round(ms, 2) / round(mp, 2)),
                tot="%.2fx" % (sum(c["salt-diet"]) / sum(c["plain"])),
                tot_rounded="%.2fx" % (round(sum(c["salt-diet"]), 2) / round(sum(c["plain"]), 2)),
                T="%.2fx" % (T["salt-diet"] / T["plain"]))

def checks():
    out = []
    key = open(os.path.join(EV, "KEY.txt"), encoding="utf-8").read()
    A = open(os.path.join(EV, "argon-ANSWER.md"), encoding="utf-8").read()
    K = open(os.path.join(EV, "kent-ANSWER.md"), encoding="utf-8").read()
    # hashes, as the doc abbreviates them: first 8 hex … last 4 (answers: last 4, as the posts gave them)
    ab = lambda h, n=4: "%s…%s" % (h[:8], h[-n:])
    out.append(("key sha", ab(sha(os.path.join(EV, "KEY.txt")))))
    out.append(("manifest sha", "%s…" % sha(os.path.join(EV, "BUNDLE-MANIFEST.sha256"))[:8]))
    out.append(("planted sha", ab(sha(os.path.join(EV, "planted-copy.md")))))
    out.append(("planted sha = key", re.search(r"planted\s+sha256 (\w+)", key).group(1)[:8]))
    out.append(("original sha (key)", ab(re.search(r"original\s+sha256 (\w+)", key).group(1))))
    out.append(("argon answer sha", ab(sha(os.path.join(EV, "argon-ANSWER.md")))))
    out.append(("kent answer sha", ab(sha(os.path.join(EV, "kent-ANSWER.md")), 2)))
    out.append(("argon bytes", "{:,} B".format(os.path.getsize(os.path.join(EV, "argon-ANSWER.md")))))
    out.append(("kent bytes", "{:,} B".format(os.path.getsize(os.path.join(EV, "kent-ANSWER.md")))))
    # S1: the planted and true values from the key; each reader's WRONG row on that figure
    planted = re.search(r"planted\s+[\d.]+ \.\. ([\d.]+)", key).group(1)
    truth = re.search(r"truth\s+.*= ([\d.]+) ", key).group(1)
    out.append(("plant planted", "reads `%s`" % planted)); out.append(("plant original", "read `%s`" % truth))
    for nm, T in (("Argon", A), ("kent", K)):
        w = [l for l in T.splitlines() if "WRONG" in l and "salt-diet retained max" in l and "SUMMARY" not in l]
        assert len(w) == 1, (nm, w)
        cells = [c.strip(" `") for c in w[0].split("|")]
        assert cells[2] == planted and cells[3] == truth and cells[4] == "WRONG", (nm, cells)
        n_wrong = sum(1 for l in T.splitlines() if "| WRONG |" in l.replace("`", "") and "SUMMARY" not in l)
        assert n_wrong == 1, (nm, n_wrong)
        out.append((nm + " S1 row", "`salt-diet retained max | … | %s | %s | WRONG`" % (planted, truth)))
        s = re.search(r"SUMMARY: (\d+) figures checked · (\d+) CONFIRMED · (\d+) WRONG · (\d+) NOT DERIVABLE", T).groups()
        out.append((nm + " figures", ("Argon declares %s" if nm == "Argon" else "kent %s.") % s[0]))
        out.append((nm + " notder", s[3]))
    # verdict table rows (S2 counts are bench's scoring, stated in the doc; S3 / NOT DERIVABLE derived)
    sa = re.search(r"SUMMARY: .*· (\d+) NOT DERIVABLE", A).group(1); sk = re.search(r"SUMMARY: .*· (\d+) NOT DERIVABLE", K).group(1)
    # S2 F1: block SBS figures
    R = rows("blockSBS-cells.tsv")
    arm = lambda a: [r for r in R if r["arm"] == a]
    sv = {a: [float(r["surv"]) for r in arm(a)] for a in ("plain", "salt-diet")}
    kept = {a: sum(int(r["kept"]) for r in arm(a)) for a in ("plain", "salt-diet")}
    seed = {a: sum(int(r["seed_lines"]) for r in arm(a)) for a in ("plain", "salt-diet")}
    assert seed["plain"] == seed["salt-diet"]
    out.append(("median surv", "Median `surv` is %.3f for salt-diet against %.3f for plain" % (statistics.median(sv["salt-diet"]), statistics.median(sv["plain"]))))
    out.append(("kept", "Total `kept` is %d against %d of %d seed lines each" % (kept["salt-diet"], kept["plain"], seed["plain"])))
    out.append(("floors", "worst `surv` %.3f is above plain's worst %.3f" % (min(sv["salt-diet"]), min(sv["plain"]))))
    out.append(("plain kept again", "table sums to %d" % kept["plain"]))
    # F2: capped cells rank and the median's two middle values
    sd = sorted(arm("salt-diet"), key=lambda r: float(r["final_COST"]))
    capped_ranks = [i + 1 for i, r in enumerate(sd) if r["capped"] not in ("0", "", "-", "no")]
    out.append(("capped ranks", "(ranks %d–%d of %d)" % (capped_ranks[0], capped_ranks[-1], len(sd))))
    c = [float(r["final_COST"]) for r in sd]
    out.append(("median $", "the median of $%.2f (the mean of the 6th\nand 7th values, $%.2f and $%.2f)" % (statistics.median(c), c[5], c[6])))
    # F4: ratios, exact vs printed, for SBS, SG, SS, O, OS
    r = ratios("SBS")
    out.append(("SBS exact", "**%s** (median) and **%s** (total)" % (r["med"], r["tot"])))
    out.append(("SBS printed", "The file prints %s and %s" % (r["med_rounded"], r["tot_rounded"])))
    out.append(("SBS T", "%s (T) is right" % r["T"]))
    for b in ("SG", "SS"):
        r = ratios(b); assert r["med"] != r["med_rounded"]
        out.append((b, "block %s prints %s where the unrounded\n  median ratio is **%s**" % (b, r["med_rounded"], r["med"])
                    if b == "SG" else "block %s prints %s where it is **%s**" % (b, r["med_rounded"], r["med"])))
    ro, ros = ratios("O"), ratios("OS")
    assert ro["med"] == ro["med_rounded"] and ros["med"] == ros["med_rounded"]
    out.append(("O OS", "Blocks O and OS print %s and %s, both right" % (ro["med"], ros["med"])))
    # S3: the shipped SBS verifier's checks, as token presence in each answer
    sys.path.insert(0, HERE)
    import importlib.util
    spec = importlib.util.spec_from_file_location("sbsv", os.path.join(HERE, "RESULT-claude-blockSBS-2026-09-21-verify.py"))
    v = importlib.util.module_from_spec(spec); spec.loader.exec_module(v)
    C = v.checks(R); norm = lambda s: s.replace(",", "")
    for nm, T in (("Argon", A), ("kent", K)):
        hit = sum(all(norm(t) in norm(T) for t in (re.findall(r"\d[\d.,]*", val) or [val])) for _, val in C)
        out.append((nm + " coverage", "%d of %d" % (hit, len(C))))
    out.append(("verdict Argon", "Argon         FOUND           1            3              %d of %d      %s" % (len(C), len(C), sa)))
    out.append(("verdict kent", "kent          FOUND           0            1              %d of %d      %s" % (len(C), len(C), sk)))
    # run receipts from gemini's served-model evidence
    se = open(os.path.join(EV, "argon-SERVED-MODEL-EVIDENCE.txt"), encoding="utf-8").read()
    gen = [l for l in se.splitlines() if re.match(r"\d+\t", l)]
    out.append(("gen rows", "%d of %d generation rows read `%s`" % (sum(1 for l in gen if l.split("\t")[1] == "gemini-4-argon"), len(gen), "gemini-4-argon")))
    fence = re.search(r"hook\.log =\s+(\d+) ALLOW view_file; (\d+) ALLOW write_to_file; (\d+) DENY", se).groups()
    out.append(("fence", "%s file reads and %s write, all allowed, and %s denials" % fence))
    out.append(("agy", "agy %s" % re.search(r"agy ([\d.]+)", se).group(1)))
    return out

def run(doc):
    text = open(doc, encoding="utf-8").read()
    miss = [(l, s) for l, s in checks() if s not in text]
    for l, s in miss: print("MISSING  %-20s expected %r" % (l, s))
    n = len(checks())
    print("%s: %d figures re-derived, %d found" % ("OK" if not miss else "FAIL", n, n - len(miss)))
    return 0 if not miss else 1

def selftest():
    import tempfile
    text = open(DOC, encoding="utf-8").read()
    bad = 0
    for old, new in (("**4.70x**", "**4.71x**"), ("8.29x", "8.27x"), ("1228 of 1332", "1128 of 1332")):
        assert old in text, old
        with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8") as f: f.write(text.replace(old, new, 1))
        rc = run(f.name); os.unlink(f.name); print("  mutant %r -> rc %d" % (old, rc)); bad += rc != 1
    rc = run(DOC); print("  original -> rc %d" % rc)
    return 0 if bad == 0 and rc == 0 else 1

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--doc", default=DOC); ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    sys.exit(selftest() if a.selftest else run(a.doc))
