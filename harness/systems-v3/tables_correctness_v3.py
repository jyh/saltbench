#!/usr/bin/env python3
"""tables_correctness_v3.py --map CELLMAP.tsv [--out RESULT.md] [--selftest]

The instrument registered by REGISTRATION-correctness-tables-v3-2026-10-01.md (§P1–§P6, ADDENDA 1–3): four correctness tables over the
complete pilot matrix (P1 greenfield, P2 brownfield, P3 spec-change, P4 signs), DECLARED POST HOC. The cell map is v2's
(CELLMAP-descriptive-tables-v2-2026-09-27.tsv) with two more columns: `verdict_source`, which POINTS at the tracked line of the
condition's result of record that prints the cell's suite verdict (as amended by any addendum to that result), and `verdict_why`.
Nothing is typed: the instrument opens each cited line and reads the verdict there. A cell whose line cannot be read, or whose
bytes do not classify, prints `unmeasured`, its condition prints `unmeasured`, and the 200 check fails (rc 1).

verdict_source grammar (each entry yields up to three strings: V the verdict word, K the count `k/n`, E the end kind; `-` = absent):
  tsv|<path>|<k=v,..>|<V col>|<K col>|<E col>        filters select exactly one data row ('#' lines are not data)
  md|<path>|<line>|<V hdr>|<K hdr>|<E hdr>            a markdown pipe-table row; its header row is found above it
  fix|<path>|<line>|<V #>|<K #>|<E #>                 a whitespace-split line (1-based fields); the cell id must be on it
  json|<path>|<id>|<phase or ->|<V key>|<K key>|<E key>
  re|<path>|<line>|<regex>                            named groups V, K, E (any subset), exactly one match; cell id on the line
  re@<anchor>|<path>|<line>|<regex>                   the same, the cell id on an ANCHOR line at most 5 lines above (v2's form)
  pool|<path>|<line>|<regex>|<bind>|<roots tsv>|<root>  a verdict printed ONCE for a whole wave: the regex carries groups L (the
                                                      wave's label) and N (its size) beside V/K; line <bind> of the same file names
                                                      L and <root>; the roots table puts the cell in <root>, which holds exactly N
Rows whose `cell` is `COUNT` carry the SECOND METHOD (§P5): `verdict_source` is an `re` entry with groups k and n pointing at a count a
result of record already prints for that condition; the cell-id rule does not apply. Each disagreement with the instrument's k is printed.

Classes (§P2, four and only four):
  PASS        V is PASS, or (no V) K is k/n with k == n > 0. A halted cell whose end state passed is PASS.
  CENSORED    not PASS, and E names a registered budget halt (HALTS below)                        - a halt is never a failure
  FAIL        not PASS, not halted, and V is FAIL or BUILD-FAIL (or, no V, K is k/n with k < n)
  UNSCORABLE  not PASS, not halted, and V is TIMEOUT / ABORT / VOID / NOT-SCORED / INCOMPLETE
Anything else (an unknown token, a V that contradicts its own K, two verdict tokens) is `unmeasured`, named, and fails the run.
Sign (§P4, ADDENDUM 1 STRICT): per arm the interval [k/(n+c+u), (k+c+u)/(n+c+u)]; `+` iff salt-diet's lower end > plain's upper end,
`−` the mirror, `=` iff both are the same single point, else `?`. Touching intervals do not separate.
Two more forms (ADDENDUM 3): `bycond[|<entry yielding E>]` marks a cell whose record prints only its condition's count; that condition
carries one row whose `cell` is `CONDITION` and whose source is an `re` entry with groups k and n, optionally ` ; ` an `re` entry with
groups A and B ("A cells . B LANDED") standing for every cell's end. The condition reads k / n only if n is its cells of record and every
cell is shown LANDED; its table entry carries `†`.
rc 0 the 200 check holds and no cell is unmeasured · 1 otherwise · 2 usage. Second-method disagreements are printed and counted and do
not gate the run (ADDENDUM 3)."""
import argparse, csv, json, os, re, subprocess, sys
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import tables_v2 as v2   # MODELS, PROBLEMS, REPO, _tsv, _mdcells: v2's population and readers, unchanged

REPO = v2.REPO
RC3 = "evidence/rc3-census-2026-09-30/census.tsv"
HALTS = ["CAP-COST", "CAP-TOKENS", "CAP-WALL", "DEADLINE", "MEM-CAP", "TURN-TIMEOUT"]   # TURN-TIMEOUT: the per-turn deadline (ADD. 3a)
FAILS = ["FAIL", "BUILD-FAIL"]
UNSCORABLE = ["TIMEOUT", "ABORT", "VOID", "NOT-SCORED", "INCOMPLETE"]
FLAGS = ["TRUNCATED", "SELF-NOT"]          # level 7's `verdicts` flags: not suite verdicts, ignored when they ride beside one
LANDING = ["NOT-LANDED"]                   # a landing word in a verdict column: the scorer did not score the cell (ADDENDUM 3a)
FOUR = [("bare-plain", "plain", "none"), ("bare-salt-diet", "salt-diet", "none"),
        ("statement-plain", "plain", "statement"), ("statement-salt-diet", "salt-diet", "statement")]


def blob(path):
    return subprocess.run(["git", "hash-object", path], capture_output=True, text=True).stdout.strip()[:12] or "UNHASHED"


def _lines(path, cache):
    if ("lines", path) not in cache:
        full = os.path.join(REPO, path)
        cache[("lines", path)] = open(full, encoding="utf-8").read().splitlines() if os.path.exists(full) else None
    return cache[("lines", path)]


def read_vke(e, cache, cell=None):
    """One verdict-source entry -> ({'V','K','E'}, provenance) or (None, reason)."""
    parts = e.strip().split("|")
    kind = parts[0]
    pick = lambda vals: {k: (v.strip() if v not in (None, "") else None) for k, v in zip("VKE", vals)}
    if kind == "tsv" and len(parts) == 6:
        _, path, filt, *cols = parts
        header, rows = v2._tsv(path, cache)
        if header is None:
            return None, "no such source %s" % path
        conds = [kv.split("=", 1) for kv in filt.split(",") if kv]
        if any(k not in header for k, _ in conds) or any(c != "-" and c not in header for c in cols):
            return None, "column missing in %s" % path
        hits = [r for r in rows if all(len(r) > header.index(k) and r[header.index(k)] == v for k, v in conds)]
        if len(hits) != 1:
            return None, "%d rows for %s in %s" % (len(hits), filt, path)
        r = hits[0]
        return pick([r[header.index(c)] if c != "-" and len(r) > header.index(c) else None for c in cols]), "%s [%s]" % (path, filt)
    if kind == "json" and len(parts) == 7:
        _, path, cid, phase, *keys = parts
        full = os.path.join(REPO, path)
        if not os.path.exists(full):
            return None, "no such source %s" % path
        if ("json", path) not in cache:
            cache[("json", path)] = json.load(open(full, encoding="utf-8"))
        hits = [x for x in cache[("json", path)] if isinstance(x, dict) and str(x.get("id")) == cid and (phase == "-" or str(x.get("phase")) == phase)]
        if len(hits) != 1:
            return None, "%d records for id=%s phase=%s in %s" % (len(hits), cid, phase, path)
        return pick([None if k == "-" or hits[0].get(k) is None else str(hits[0].get(k)) for k in keys]), "%s [id=%s,phase=%s]" % (path, cid, phase)
    if kind == "pool" and len(parts) == 7:
        # a verdict printed once for a whole wave; bound to this cell by bytes, never by eye: the verdict line names the wave (group L)
        # and its size (group N); <bind> in the SAME file names the wave and its root; the roots table puts this cell in that root;
        # and the root holds exactly N cells there.
        _, path, lineno, rx, bind, roots, root = parts
        lines = _lines(path, cache)
        if lines is None or not (0 < int(lineno) <= len(lines)) or not (0 < int(bind) <= len(lines)):
            return None, "no such source line %s:%s/%s" % (path, lineno, bind)
        ms = list(re.finditer(rx, lines[int(lineno) - 1]))
        if len(ms) != 1 or not {"L", "N"} <= set(ms[0].groupdict()):
            return None, "pool regex matched %d times at %s:%s (or lacks groups L, N)" % (len(ms), path, lineno)
        g = ms[0].groupdict()
        if root not in lines[int(bind) - 1] or g["L"] not in lines[int(bind) - 1]:
            return None, "%s:%s does not bind %r to %r" % (path, bind, g["L"], root)
        header, rows = v2._tsv(roots, cache)
        if header is None or "cell" not in header or "root" not in header:
            return None, "no roots table %s" % roots
        ci, ri = header.index("cell"), header.index("root")
        members = [r[ci] for r in rows if len(r) > ri and r[ri] == root]
        if cell not in members or len(members) != int(g["N"]):
            return None, "pool %s: cell %s %s, %d members against N %s" % (root, cell, "in" if cell in members else "NOT in", len(members), g["N"])
        return {k: (g.get(k) or None) for k in ("V", "K", "E")}, "%s:%s (pool %r = %s, bound at :%s; %s)" % (path, lineno, g["L"], root, bind, roots)
    anchor = None
    if kind.startswith("re@"):
        kind, anchor = "re", int(kind[3:])
    if kind in ("md", "fix", "re") and len(parts) >= 4:
        path, lineno = parts[1], parts[2]
        lines = _lines(path, cache)
        if lines is None:
            return None, "no such source %s" % path
        i = int(lineno) - 1
        if not (0 <= i < len(lines)):
            return None, "no line %s in %s" % (lineno, path)
        ln = lines[i]
        ids = lambda s: re.split(r"[\s|`,;()]+", s)
        if anchor is not None:
            if not (i - 5 <= anchor - 1 <= i) or not cell or cell not in ids(lines[anchor - 1]):
                return None, "cell %s not on anchor line %s of %s (within 5 above %s)" % (cell, anchor, path, lineno)
        elif cell and cell not in ids(ln):
            return None, "cell %s not on %s:%s" % (cell, path, lineno)
        prov = "%s:%s" % (path, lineno) + (" (anchor :%d)" % anchor if anchor else "")
        if kind == "md" and len(parts) == 6:
            if not ln.lstrip().startswith("|"):
                return None, "line %s of %s is not a table row" % (lineno, path)
            j = i
            while j > 0 and lines[j - 1].lstrip().startswith("|"):
                j -= 1
            header, row = v2._mdcells(lines[j]), v2._mdcells(ln)
            if any(h != "-" and h not in header for h in parts[3:]):
                return None, "a header of %s not in the table at %s:%d" % (parts[3:], path, j + 1)
            return pick([row[header.index(h)] if h != "-" and len(row) > header.index(h) else None for h in parts[3:]]), prov
        if kind == "fix" and len(parts) == 6:
            f = ln.split()
            vals = []
            for x in parts[3:]:
                if x == "-":
                    vals.append(None)
                elif 1 <= int(x) <= len(f):
                    vals.append(f[int(x) - 1])
                else:
                    return None, "no field %s at %s" % (x, prov)
            return pick(vals), prov
        if kind == "re":
            ms = list(re.finditer("|".join(parts[3:]), ln))
            if len(ms) != 1:
                return None, "regex matched %d times at %s" % (len(ms), prov)
            g = ms[0].groupdict()
            return dict({k: None for k in "VKE"}, **{k: (v or None) for k, v in g.items()}), prov
    return None, "unparsed verdict source %r" % e


def _count(k):
    m = re.fullmatch(r"\s*(\d+)\s*/\s*(\d+)\s*", k or "")
    return (int(m.group(1)), int(m.group(2))) if m else None


def classify(V, K, E):
    """-> (class, None) or (None, why). §P2's four classes; anything that does not fit is named, never guessed."""
    toks = [t for t in re.split(r"[\s|,;:]+", (V or "").upper()) if t and t not in FLAGS + LANDING]
    known = [t for t in toks if t in ["PASS"] + FAILS + UNSCORABLE]
    if toks and len(known) != len(toks):
        return None, "unknown verdict token(s) %s" % [t for t in toks if t not in known]
    if len(set(known)) > 1:
        return None, "two verdict tokens %s" % known
    v = known[0] if known else None
    kn = _count(K)
    if K and K.strip() not in ("-", "") and kn is None:
        return None, "count %r is not k/n" % K
    halted = any(re.search(r"(?<![A-Z-])%s(?![A-Z-])" % re.escape(h), (E or "").upper()) for h in HALTS)
    if v is None and kn is None:
        if halted and any(t in LANDING for t in re.split(r"[\s|,;:]+", (V or "").upper())):
            return "CENSORED", None            # ADDENDUM 3a: halted, and the record shows no pass
        return None, "neither a verdict nor a count"
    full = kn is not None and kn[1] > 0 and kn[0] == kn[1]
    if v == "PASS" and kn is not None and not full:
        return None, "PASS beside a count that is not full (%s)" % K
    if v in FAILS and full:
        return None, "%s beside a full count (%s)" % (v, K)
    if v == "PASS" or (v is None and full):
        return "PASS", None
    if v in UNSCORABLE:
        return "UNSCORABLE", None              # ADDENDUM 3b: before the halt test
    if halted:
        return "CENSORED", None
    if v in FAILS or (v is None and kn is not None and kn[0] < kn[1]):
        return "FAIL", None
    return None, "no class for V=%r K=%r E=%r" % (V, K, E)


def load_rc3():
    p = os.path.join(REPO, RC3)
    out = {}
    if os.path.exists(p):
        for r in csv.DictReader([l for l in open(p, encoding="utf-8") if not l.startswith("#")], delimiter="\t"):
            out.setdefault(r.get("cell"), []).append(r)
    return out


def build(map_path):
    cache, conds, prov, counts, meta = {}, {}, [], [], {}
    rc3 = load_rc3()
    for r in csv.DictReader(open(map_path, encoding="utf-8"), delimiter="\t"):
        if r["model"].startswith("#"):
            continue
        k = (r["model"], r["problem"], r["field"], r["arm"], r["extras"])
        if r["cell"] == "COUNT":
            got, p = read_vke(r["verdict_source"], cache)
            counts.append((k, got, p, r.get("verdict_why", ""), r.get("count_cause", "") or ""))
            continue
        if r["cell"] == "CONDITION":              # ADDENDUM 3d: a per-condition count, and optionally an all-landed line
            ents = [read_vke(e, cache) for e in r["verdict_source"].split(" ; ")]
            if k in meta:
                meta[k] = {"err": "two CONDITION rows"}
            else:
                meta[k] = {"ents": ents, "why": r.get("verdict_why", "")}
            continue
        c = conds.setdefault(k, {"status": r["status"], "cells": []})
        if c["status"] != r["status"]:
            c["status"] = "CONFLICT"
        if r["status"] != "DONE":
            continue
        f = {"cell": r["cell"], "src": r.get("verdict_source", ""), "why": r.get("verdict_why", "")}
        if f["src"].startswith("bycond"):
            f["bycond"], f["cls"], f["reason"], f["E"] = True, None, "ADDENDUM 3d: pending its condition", None
            sub = f["src"][len("bycond"):].lstrip("|")
            if sub:
                got, p = read_vke(sub, cache, r["cell"])
                if got is None:
                    f["reason"] = p
                else:
                    f["E"], f["prov"] = got["E"], p
        elif f["src"].strip() in ("", "-", "NONE"):
            f["cls"], f["reason"] = None, "no tracked verdict line (%s)" % (f["why"] or "none named")
        else:
            got, p = read_vke(f["src"], cache, r["cell"])
            if got is None:
                f["cls"], f["reason"] = None, p
            else:
                f.update(V=got["V"], K=got["K"], E=got["E"], prov=p)
                f["cls"], f["reason"] = classify(got["V"], got["K"], got["E"])
        if r["cell"] in rc3:
            f["rc3"] = " · ".join("%s %s %s" % (x.get("variant", ""), x.get("class", ""), x.get("tests", "")) for x in rc3[r["cell"]])
        c["cells"].append(f)
        prov.append((k, f))
    for k, c in conds.items():
        if any(f.get("bycond") for f in c["cells"]):
            err = bycond(c, meta.get(k))
            for f in c["cells"]:
                f["cls"], f["reason"] = (None, err) if err else ("by condition", None)
    return conds, prov, counts


def bycond(c, m):
    """ADDENDUM 3d's three conditions -> None (and c['bycond'] = (k, n)) or the reason every cell is unmeasured."""
    if not all(f.get("bycond") for f in c["cells"]):
        return "ADDENDUM 3d: a cell of this condition has its own verdict line"
    if not m or m.get("err") or not m["ents"] or m["ents"][0][0] is None:
        return "ADDENDUM 3d: no readable CONDITION row (%s)" % ((m or {}).get("err") or (m and m["ents"] and m["ents"][0][1]) or "none")
    cnt = m["ents"][0][0]
    if cnt.get("k") is None or cnt.get("n") is None:
        return "ADDENDUM 3d: the CONDITION count has no k and n"
    kk, nn = int(cnt["k"]), int(cnt["n"])
    if nn != len(c["cells"]) or not 0 <= kk <= nn:
        return "ADDENDUM 3d: printed n %d against %d cells of record" % (nn, len(c["cells"]))
    allland = None
    if len(m["ents"]) > 1:
        a = m["ents"][1][0]
        if a is None or a.get("A") is None or a.get("A") != a.get("B"):
            return "ADDENDUM 3d: the all-landed line does not read A cells, A LANDED (%s)" % m["ents"][1][1]
        allland = m["ents"][1][1]
    for f in c["cells"]:
        e = (f.get("E") or "").upper().split()
        if f.get("reason", "").startswith("ADDENDUM 3d: pending") is False:
            return "ADDENDUM 3d: cell %s: %s" % (f["cell"], f["reason"])
        if e != ["LANDED"] and not (not e and allland):
            return "ADDENDUM 3d: cell %s is not shown LANDED (end %r)" % (f["cell"], f.get("E"))
        if not e:
            f["prov"] = "landed by %s" % allland
    c["bycond"] = (kk, nn, m["ents"][0][1])
    return None


def summarise(c):
    """-> dict(k, n, c, u, mark). mark '' when the condition has a count."""
    if c is None:
        return {"mark": "missing"}
    if c["status"] == "INEXPR":
        return {"mark": "—"}
    if c["status"] == "DECLARED":
        return {"mark": "declared"}
    if c["status"] != "DONE":
        return {"mark": c["status"]}
    if not c["cells"] or any(f["cls"] is None for f in c["cells"]):
        return {"mark": "unmeasured"}
    if c.get("bycond"):
        return {"k": c["bycond"][0], "n": c["bycond"][1], "c": 0, "u": 0, "mark": "", "bycond": True}
    cl = [f["cls"] for f in c["cells"]]
    k = cl.count("PASS")
    return {"k": k, "n": k + cl.count("FAIL"), "c": cl.count("CENSORED"), "u": cl.count("UNSCORABLE"), "mark": ""}


def show(s):
    if s["mark"]:
        return s["mark"]
    t = ("%d / %d" % (s["k"], s["n"])) if s["n"] else "n = 0"          # ADDENDUM 2: never 0/0
    extra = [x for x in (("+%d censored" % s["c"]) if s["c"] else "", ("+%d unscorable" % s["u"]) if s["u"] else "") if x]
    return t + (" (%s)" % ", ".join(extra) if extra else "") + (" †" if s.get("bycond") else "")


def interval(s):
    if s["mark"]:
        return None
    N = s["n"] + s["c"] + s["u"]
    if N == 0:
        return None
    return Fraction(s["k"], N), Fraction(s["k"] + s["c"] + s["u"], N)


def sign(sd, pl):
    """§P4 with ADDENDUM 1 (STRICT). -> '+', '−', '=', '?', or '—' when either side has no interval."""
    a, b = interval(sd), interval(pl)
    if a is None or b is None:
        return "—"
    if a[0] > b[1]:
        return "+"
    if a[1] < b[0]:
        return "−"
    if a[0] == a[1] == b[0] == b[1]:
        return "="
    return "?"


def render(conds):
    out, tally, fails = [], {"num": 0, "—": 0, "declared": 0, "unmeasured": 0, "other": 0}, []
    def cell(k, tag):
        s = summarise(conds.get(k))
        key = "num" if s["mark"] == "" else (s["mark"] if s["mark"] in tally else "other")
        tally[key] += 1
        if key == "other":
            fails.append("%s %s -> %s" % (tag, "/".join(k), s["mark"]))
        return s
    def table(tag, title, field, cols):
        out.append("\n## %s · %s\n" % (tag, title))
        out.append("| model | problem | " + " | ".join(c[0] for c in cols) + " |")
        out.append("|---|---|" + "---|" * len(cols))
        g = {}
        for m in v2.MODELS:
            for p in v2.PROBLEMS:
                vals = []
                for name, arm, extras in cols:
                    g[(m, p, name)] = s = cell((m, p, field, arm, extras), tag)
                    vals.append(show(s))
                out.append("| %s | %s | %s |" % (m, p, " | ".join(vals)))
        return g
    g1 = table("P1", "greenfield — full passes k / n per condition (n = PASS + FAIL; censored and unscorable beside)", "greenfield", FOUR)
    g2 = table("P2", "brownfield — full passes k / n per condition", "brownfield", FOUR)
    g3 = table("P3", "spec-change (greenfield only) — phase-2 full passes k / n per condition", "greenfield",
               [("plain", "plain", "spec-change"), ("salt-diet", "salt-diet", "spec-change")])
    total = sum(tally.values())
    check = "CHECK conditions with a k/n %d + — %d + declared %d + unmeasured %d = %d (other %d) against 181 + 16 + 3 = 200" % (
        tally["num"], tally["—"], tally["declared"], tally["unmeasured"], total, tally["other"])
    if total != 200 or tally["other"] or tally["unmeasured"] or tally["—"] != 16 or tally["declared"] != 3 or tally["num"] != 181:
        fails.insert(0, check)
    pairs = lambda g, m, p: [("bare", g[(m, p, "bare-salt-diet")], g[(m, p, "bare-plain")]),
                             ("statement", g[(m, p, "statement-salt-diet")], g[(m, p, "statement-plain")])]
    out.append("\n## P4 · signs, greenfield: salt-diet's pass-rate interval against plain's (ADDENDUM 1: STRICT)\n")
    out.append("| model | problem | bare | statement | spec-change |")
    out.append("|---|---|---|---|---|")
    sg, qsrc = {}, {}
    for m in v2.MODELS:
        for p in v2.PROBLEMS:
            row = pairs(g1, m, p) + [("spec-change", g3[(m, p, "salt-diet")], g3[(m, p, "plain")])]
            vals = []
            for name, sd, pl in row:
                s = sign(sd, pl)
                sg.setdefault((m, name), []).append((p, s))
                if s == "?":
                    q = qsrc.setdefault(name, {"salt-diet": 0, "plain": 0, "both": 0})
                    cs, cp = sd["c"] + sd["u"] > 0, pl["c"] + pl["u"] > 0
                    q["both" if cs and cp else ("salt-diet" if cs else "plain")] += 1
                vals.append(s)
            out.append("| %s | %s | %s |" % (m, p, " | ".join(vals)))
    out.append("\n### P4 counts, per model per treatment (no test, no p-value)\n")
    out.append("| model | treatment | + | = | − | ? | no sign (—) |")
    out.append("|---|---|---|---|---|---|---|")
    for m in v2.MODELS:
        for name in ("bare", "statement", "spec-change"):
            ss = [s for _, s in sg[(m, name)]]
            out.append("| %s | %s | %d | %d | %d | %d | %d |" % (m, name, ss.count("+"), ss.count("="), ss.count("−"), ss.count("?"), ss.count("—")))
    out.append("\n### Where each `?` comes from (§P6): every `?` has a censored or unscorable cell on at least one side\n")
    out.append("| treatment | censoring on salt-diet only | on plain only | on both |")
    out.append("|---|---|---|---|")
    for name in ("bare", "statement", "spec-change"):
        q = qsrc.get(name, {"salt-diet": 0, "plain": 0, "both": 0})
        out.append("| %s | %d | %d | %d |" % (name, q["salt-diet"], q["plain"], q["both"]))
    out.append("\n### Brownfield signs, by the same rule (in the file, not in P4)\n")
    out.append("| model | problem | bare | statement |")
    out.append("|---|---|---|---|")
    for m in v2.MODELS:
        for p in v2.PROBLEMS:
            out.append("| %s | %s | %s |" % (m, p, " | ".join(sign(sd, pl) for _, sd, pl in pairs(g2, m, p))))
    return out, check, fails


def cause_of(spec, got, c, cache):
    """A disagreement's cause, VERIFIED or None (with why). Two forms:
      repro|<tsv>|<filter>|<cell col>|<V col or ->|<K col, or a/b for two columns>  the printed k/n is re-derived from the per-cell table
          that count was built on, over its own population (k = rows that classify PASS, n = rows); then that population is set against
          this condition's cells of record, and every cell the two read differently is named
      superseded|<path>|<line>|<regex>   a later dated line of the same record replaces the printed figure (one match on that line)"""
    parts = spec.split("|")
    if parts[0] == "superseded" and len(parts) >= 4:
        lines = _lines(parts[1], cache)
        if lines is None or not (0 < int(parts[2]) <= len(lines)):
            return None, "no line %s:%s" % (parts[1], parts[2])
        if len(list(re.finditer("|".join(parts[3:]), lines[int(parts[2]) - 1]))) != 1:
            return None, "superseding line %s:%s does not match" % (parts[1], parts[2])
        return "SUPERSEDED by %s:%s" % (parts[1], parts[2]), None
    if parts[0] == "repro" and len(parts) == 6:
        _, path, filt, ccol, vcol, kcol = parts
        header, rows = v2._tsv(path, cache)
        need = [x for x in [ccol, vcol] + kcol.split("/") + [kv.split("=", 1)[0] for kv in filt.split(",")] if x != "-"]
        if header is None or any(x not in header for x in need):
            return None, "repro: column missing in %s" % path
        conds = [kv.split("=", 1) for kv in filt.split(",") if kv]
        hit = [r for r in rows if all(len(r) > header.index(a) and r[header.index(a)] == b for a, b in conds)]
        col = lambda r, x: r[header.index(x)] if len(r) > header.index(x) else ""
        cls = {}
        for r in hit:
            K = "/".join(col(r, x) for x in kcol.split("/")) if "/" in kcol else col(r, kcol)
            cls[col(r, ccol)] = classify(None if vcol == "-" else col(r, vcol), K, None)[0]
        kk, nn = sum(1 for v in cls.values() if v == "PASS"), len(cls)
        if got.get("n") is None or (kk, nn) != (int(got["k"]), int(got["n"])):
            return None, "repro over %s [%s] gives %d/%d, not the printed %s/%s" % (path, filt, kk, nn, got["k"], got.get("n"))
        mine = {f["cell"]: f["cls"] for f in (c or {}).get("cells", [])}
        only_p = sorted(set(cls) - set(mine))
        only_r = sorted(set(mine) - set(cls))
        diff = sorted(x for x in set(cls) & set(mine) if (cls[x] == "PASS") != (mine[x] == "PASS") or mine[x] in ("CENSORED", "UNSCORABLE"))
        parts_ = ["printed %d/%d REPRODUCED from %s [%s]" % (kk, nn, path, filt)]
        parts_.append("in that count, not a cell of record: %s" % (", ".join(only_p) or "none"))
        parts_.append("cells of record outside it: %s" % (", ".join("%s (%s)" % (x, mine[x]) for x in only_r) or "none"))
        parts_.append("read differently: %s" % (", ".join("%s (%s there, %s here)" % (x, cls[x] or "no class", mine[x]) for x in diff) or "none"))
        if not (only_p or only_r or diff):
            return None, "repro reproduces the count over the SAME cells read the same way: the disagreement is unexplained"
        return "; ".join(parts_), None
    return None, "no cause given"


def second_method(conds, counts, cache=None):
    cache = {} if cache is None else cache
    rows, dis, nocause, kinds = [], 0, [], {}
    for k, got, p, why, spec in counts:
        s = summarise(conds.get(k))
        if got is None or got.get("k") is None:
            rows.append((k, "unread: %s" % p, "-", "UNREAD", why))
            dis += 1
            nocause.append((k, p))
            continue
        mine = s.get("k")
        ok = mine is not None and int(got["k"]) == mine
        verdict = "agrees"
        if not ok:
            dis += 1
            cz, err = cause_of(spec, got, conds.get(k), cache)
            if cz is None:
                nocause.append((k, err))
                verdict = "DISAGREES — NO CAUSE: %s" % err
            else:
                kd = "REPRODUCED over another population" if "REPRODUCED" in cz.split(";")[0] else cz.split(" ")[0]
                kinds[kd] = kinds.get(kd, 0) + 1
                verdict = "DISAGREES — cause: %s" % cz
        rows.append((k, "%s%s" % (got["k"], "/" + got["n"] if got.get("n") else ""), show(s), verdict, "%s %s" % (p, why)))
    return rows, dis, nocause, kinds


def selftest():
    n = 0
    def ok(c, msg):
        nonlocal n
        n += 1
        if not c:
            raise AssertionError(msg)
    S = lambda k, nn, c=0, u=0: {"k": k, "n": nn, "c": c, "u": u, "mark": ""}
    # ADDENDUM 1, red first: paper's example. plain 2/3 none censored = [2/3, 2/3]; salt-diet k 2, n 2, c 1 = [2/3, 1]. Touching: `?`.
    ok(sign(S(2, 2, 1), S(2, 3)) == "?", "ADDENDUM 1: touching intervals do NOT separate (shared endpoint 2/3 is `?`, never `+`)")
    ok(sign(S(2, 3), S(2, 2, 1)) == "?", "ADDENDUM 1: the mirror of the touching case is `?`, never `−`")
    ok(sign(S(3, 3), S(1, 3)) == "+" and sign(S(1, 3), S(3, 3)) == "−", "points that differ separate")
    ok(sign(S(2, 3), S(2, 3)) == "=", "the same single point is `=`")
    ok(sign(S(3, 3, 0, 0), S(0, 2, 1)) == "+", "[1,1] against [0,1/3] separates")
    ok(sign(S(2, 2, 1), S(0, 3)) == "+", "a censored arm whose WHOLE interval is above still separates")
    ok(sign(S(0, 0, 3), S(3, 3)) == "?", "an all-censored arm is [0,1]: never a sign")
    ok(sign({"mark": "—"}, S(3, 3)) == "—", "no interval, no sign")
    # §P2's classes
    ok(classify("PASS", "6/6", "ENDED: LANDED")[0] == "PASS", "PASS")
    ok(classify("PASS", "24/24", "CAP-COST")[0] == "PASS", "a halted cell whose end state passed is PASS")
    ok(classify("FAIL", "3/7", "ENDED: CAP-COST")[0] == "CENSORED", "a halt is never a failure")
    ok(classify("BUILD-FAIL", "0/0", "ENDED: CAP-COST")[0] == "CENSORED", "a halted build failure is censored")
    ok(classify("BUILD-FAIL", "0/0", "LANDED")[0] == "FAIL", "a landed build failure is FAIL")
    ok(classify("TIMEOUT", "0/0", "LANDED")[0] == "UNSCORABLE", "the runner's own timeout is unscorable")
    ok(classify(None, "10/16", "LANDED")[0] == "FAIL" and classify(None, "7/7", None)[0] == "PASS", "a bare count classifies")
    ok(classify("TRUNCATED|PASS", "8/8", "LANDED")[0] == "PASS", "level 7's flags ride beside the verdict and are ignored")
    ok(classify("PASS", "6/7", "LANDED")[0] is None, "PASS beside a short count is unmeasured, never resolved")
    ok(classify("FAIL", "7/7", "LANDED")[0] is None, "FAIL beside a full count is unmeasured")
    ok(classify("MAYBE", "1/2", "LANDED")[0] is None, "an unknown token is unmeasured")
    ok(classify("PASS FAIL", None, None)[0] is None, "two verdict tokens are unmeasured")
    ok(classify(None, "0/0", "LANDED")[0] is None, "0/0 with no verdict word has no class")
    ok(classify("FAIL", None, "ENDED: CAP-COSTLY")[0] == "FAIL", "a halt token must be whole")
    ok(classify("NOT-SCORED", "-", "NO-FIRST-RESULT")[0] == "UNSCORABLE", "not scored, not halted: unscorable")
    # §P3 and ADDENDUM 2
    ok(show(S(0, 0, 3)) == "n = 0 (+3 censored)" and show(S(0, 0, 2, 1)) == "n = 0 (+2 censored, +1 unscorable)", "ADDENDUM 2: n = 0, never 0/0")
    ok(show(S(2, 3, 1)) == "2 / 3 (+1 censored)" and show(S(3, 3)) == "3 / 3", "k / n with the rest beside it")
    c = {"status": "DONE", "cells": [{"cls": "PASS"}, {"cls": "CENSORED"}, {"cls": "FAIL"}]}
    ok(summarise(c) == {"k": 1, "n": 2, "c": 1, "u": 0, "mark": ""}, "a censored cell enters neither k nor n")
    ok(summarise({"status": "DONE", "cells": [{"cls": "PASS"}, {"cls": None}]})["mark"] == "unmeasured", "any cell unmeasured -> condition unmeasured")
    # the readers, on a fixture
    import tempfile
    d = tempfile.mkdtemp(dir=REPO)
    try:
        rel = os.path.relpath(d, REPO)
        open(os.path.join(d, "t.tsv"), "w").write("# note\ncell\tsuite\ttests\trun_state\nc1\tPASS\t6/6\tENDED: LANDED\nc2\tFAIL\t3/7\tENDED: CAP-COST\n")
        open(os.path.join(d, "t.md"), "w").write("x\n  c3  C  plain  FAIL  10/16  LANDED\n| cell | v | t |\n|---|---|---|\n| c4 | PASS | 7/7 |\n  FULL PASS 3 of 3\n")
        cache = {}
        g, _ = read_vke("tsv|%s/t.tsv|cell=c2|suite|tests|run_state" % rel, cache, "c2")
        ok(g == {"V": "FAIL", "K": "3/7", "E": "ENDED: CAP-COST"}, "tsv reader")
        ok(read_vke("tsv|%s/t.tsv|cell=c9|suite|tests|-" % rel, cache, "c9")[0] is None, "a filter selecting no row is refused")
        g, _ = read_vke("fix|%s/t.md|2|4|5|6" % rel, cache, "c3")
        ok(g == {"V": "FAIL", "K": "10/16", "E": "LANDED"}, "fix reader")
        ok(read_vke("fix|%s/t.md|2|4|5|6" % rel, cache, "c9")[0] is None, "a line without the cell id is refused")
        g, _ = read_vke("md|%s/t.md|5|v|t|-" % rel, cache, "c4")
        ok(g["V"] == "PASS" and g["K"] == "7/7" and g["E"] is None, "md reader")
        g, _ = read_vke(r"re|%s/t.md|6|FULL PASS (?P<k>\d+) of (?P<n>\d+)" % rel, cache)
        ok(g["k"] == "3" and g["n"] == "3", "a count source (second method)")
        open(os.path.join(d, "l.md"), "w").write("  27 cells . 27 LANDED . 25 FULL PASS\n")
        g, _ = read_vke(r"re|%s/l.md|1|(?P<A>\d+) cells \. (?P<B>\d+) LANDED" % rel, cache)
        ok(g and g.get("A") == "27" and g.get("B") == "27", "3d: the reader returns an all-landed line's own groups (A, B)")
        # the 19-row causes (the helm, 11:05): a cause is VERIFIED or the row reads NO CAUSE
        open(os.path.join(d, "pc.tsv"), "w").write("cell\ttask\tkind\tclass\ttests\nx1\tT\tLANDED\tPASS\t7/7\nx2\tT\tLANDED\tPASS\t7/7\nx9\tT\tLANDED\tPASS\t7/7\n")
        cc = {"cells": [{"cell": "x1", "cls": "PASS"}, {"cell": "x2", "cls": "PASS"}, {"cell": "x3", "cls": "CENSORED"}]}
        cz, _ = cause_of("repro|%s/pc.tsv|task=T,kind=LANDED|cell|class|tests" % rel, {"k": "3", "n": "3"}, cc, cache)
        ok(cz and "x9" in cz.split("not a cell of record:")[1].split(";")[0] and "x3 (CENSORED)" in cz, "a reproduced count names both set differences")
        ok(cause_of("repro|%s/pc.tsv|task=T,kind=LANDED|cell|class|tests" % rel, {"k": "2", "n": "3"}, cc, cache)[0] is None,
           "a count the repro does not reproduce has NO cause")
        same = {"cells": [{"cell": x, "cls": "PASS"} for x in ("x1", "x2", "x9")]}
        ok(cause_of("repro|%s/pc.tsv|task=T,kind=LANDED|cell|class|tests" % rel, {"k": "3", "n": "3"}, same, cache)[0] is None,
           "the same cells read the same way explain nothing")
        ok(cause_of(r"superseded|%s/t.md|6|FULL PASS \d+ of \d+" % rel, {"k": "1", "n": "3"}, cc, cache)[0] is not None
           and cause_of(r"superseded|%s/t.md|6|NOT THERE" % rel, {"k": "1"}, cc, cache)[0] is None, "a superseding line must match")
        ok(cause_of("", {"k": "1"}, cc, cache)[0] is None, "no cause given is no cause")
        # ADDENDUM 3a/3b
        ok(classify("NOT-LANDED", "-", "TURN-TIMEOUT")[0] == "CENSORED", "3a: halted with no suite verdict is censored")
        ok(classify("NOT-LANDED", "-", "LANDED")[0] is None, "3a: a landing word without a halt has no class")
        ok(classify("NOT-SCORED", None, "TURN-TIMEOUT")[0] == "UNSCORABLE", "3b: a declared void comes before the halt test")
        # ADDENDUM 3c: the pool form
        open(os.path.join(d, "p.md"), "w").write("  wave 2 ( 2 cells): PASS  2   (TESTS 7/7 each)\n  ~/root-a (wave 2, x)\n")
        open(os.path.join(d, "roots.tsv"), "w").write("cell\troot\np1\troot-a\np2\troot-a\np3\troot-b\n")
        rx = r"(?P<L>wave 2) \( (?P<N>\d+) cells\): (?P<V>PASS)\s+\d+\s+\(TESTS (?P<K>\d+/\d+) each"
        g, _ = read_vke("pool|%s/p.md|1|%s|2|%s/roots.tsv|root-a" % (rel, rx, rel), cache, "p1")
        ok(g is not None and g["V"] == "PASS" and g["K"] == "7/7", "3c: a wave verdict reaches a member cell")
        ok(read_vke("pool|%s/p.md|1|%s|2|%s/roots.tsv|root-a" % (rel, rx, rel), cache, "p3")[0] is None, "3c: a non-member is refused")
        open(os.path.join(d, "roots2.tsv"), "w").write("cell\troot\np1\troot-a\np2\troot-a\np4\troot-a\n")
        ok(read_vke("pool|%s/p.md|1|%s|2|%s/roots2.tsv|root-a" % (rel, rx, rel), cache, "p1")[0] is None, "3c: a root holding more than N is refused")
        # re@ (v2's anchored form)
        open(os.path.join(d, "a.md"), "w").write("  cell a9 here\n  FULL PASS 1 of 1\n  TESTS 23/23\n")
        g, _ = read_vke(r"re@1|%s/a.md|3|TESTS (?P<K>\d+/\d+)" % rel, cache, "a9")
        ok(g and g["K"] == "23/23", "re@: the cell on an anchor line above")
        ok(read_vke(r"re@1|%s/a.md|3|TESTS (?P<K>\d+/\d+)" % rel, cache, "a8")[0] is None, "re@: a wrong anchor is refused")
        # ADDENDUM 3d: by condition
        cnt = ({"k": "2", "n": "3"}, "x:1")
        land = ({"A": "3", "B": "3"}, "x:2")
        mk = lambda es: {"status": "DONE", "cells": [{"cell": "b%d" % i, "bycond": True, "reason": "ADDENDUM 3d: pending its condition", "E": e}
                                                      for i, e in enumerate(es)]}
        c = mk(["LANDED"] * 3)
        ok(bycond(c, {"ents": [cnt]}) is None and c["bycond"][:2] == (2, 3), "3d: n = cells of record, all landed -> k / n")
        ok(bycond(mk(["LANDED", "LANDED"]), {"ents": [cnt]}) is not None, "3d: printed n against a different cell count is refused")
        ok(bycond(mk(["LANDED", "CAP-COST", "LANDED"]), {"ents": [cnt]}) is not None, "3d: a halted cell refuses the whole condition")
        ok(bycond(mk([None] * 3), {"ents": [cnt]}) is not None, "3d: no end shown and no all-landed line is refused")
        ok(bycond(mk([None] * 3), {"ents": [cnt, land]}) is None, "3d: the all-landed line stands for every end")
        ok(bycond(mk([None] * 3), {"ents": [cnt, ({"A": "27", "B": "26"}, "x:2")]}) is not None, "3d: an all-landed line that is not all is refused")
        c = mk(["LANDED"] * 3)
        c["cells"][0]["bycond"] = False
        ok(bycond(c, {"ents": [cnt]}) is not None, "3d: the whole condition or none of it")
        ok(show({"k": 2, "n": 3, "c": 0, "u": 0, "mark": "", "bycond": True}) == "2 / 3 †", "3d: marked in the table")
    finally:
        for f in os.listdir(d):
            os.remove(os.path.join(d, f))
        os.rmdir(d)
    print("selftest OK (%d arms)" % n)
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--map")
    ap.add_argument("--out")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    if not a.map:
        ap.error("--map is required")
    conds, prov, counts = build(a.map)
    body, check, fails = render(conds)
    sm, dis, nocause, kinds = second_method(conds, counts)
    agree = {k for k, _, _, v, _ in sm if v == "agrees"}
    only_dis = {k for k, _, _, v, _ in sm if v != "agrees"} - agree
    unm = [(k, f) for k, f in prov if f["cls"] is None]
    rc3 = [(k, f) for k, f in prov if f.get("rc3")]
    cls = {}
    for _, f in prov:
        cls[f["cls"] or "unmeasured"] = cls.get(f["cls"] or "unmeasured", 0) + 1
    head = subprocess.run(["git", "-C", REPO, "rev-parse", "--short=12", "HEAD"], capture_output=True, text=True).stdout.strip()
    hdr = ["# RESULT: CORRECTNESS OVER THE COMPLETE PILOT MATRIX (arXiv v3), DECLARED POST HOC",
           "## Printed by `harness/systems-v3/tables_correctness_v3.py` over the working tree at repo head `%s`, from `%s`. Registered in "
           "`REGISTRATION-correctness-tables-v3-2026-10-01.md` (§P1–§P6, ADDENDA 1–3; ADDENDA 1–2 merged and ADDENDUM 3 committed (`7da02bb`) "
           "before this ran, in the same PR as this file). The instrument and its map "
           "are named by CONTENT (git blob ids, checkable with `git hash-object <file>`): `%s` %s · `%s` %s." % (
               head, os.path.relpath(os.path.abspath(a.map), REPO), os.path.basename(__file__), blob(os.path.abspath(__file__)),
               os.path.basename(a.map), blob(os.path.abspath(a.map))), "",
           "**%s**" % check,
           "**Cells: %s.**" % " · ".join("%s %d" % (k, cls[k]) for k in ("PASS", "FAIL", "CENSORED", "UNSCORABLE", "by condition", "unmeasured") if k in cls),
           "**Second method (§P5): %d printed count(s) compared, %d disagreement(s); %d of the 181 DONE conditions have at least one printed "
           "count that agrees, %d have a printed count and none agrees, %d have no printed count.**" % (
               len(sm), dis, len(agree), len(only_dis), 181 - len(agree) - len(only_dis)),
           "**Every disagreement's cause, verified by the instrument: %s; with NO verified cause: %d.**" % (
               " · ".join("%s %d" % (a, b) for a, b in sorted(kinds.items())) or "none", len(nocause)), "",
           "⛔ **A descriptive reading, declared post hoc (§P6): no test, no p-value, no verdict on the arms; the registered tests remain §4's.** "
           "n = 3 per condition, so a rate moves in thirds. A PASS is the withheld suite's verdict and is bounded by that suite's strength "
           "(mutant scores are ceilings, not strengths). The agy and Claude lanes have different scorers of record; a row compares arms "
           "within one model and one problem.", "",
           "- **k / n** full passes over n = PASS + FAIL. **(+c censored)** cells that halted at a registered budget without a pass on the "
           "record; **(+u unscorable)** cells the suite gave no verdict on. Neither enters k or n. **`n = 0`** every cell censored or "
           "unscorable (ADDENDUM 2). **`†`** the record prints only the condition's count, read under ADDENDUM 3d. **`—`** inexpressible. "
           "**`declared`** unreached at the cap.",
           "- **Signs** (§P4, ADDENDUM 1): each arm's interval [k/(n+c+u), (k+c+u)/(n+c+u)]; `+` / `−` only when the intervals are strictly "
           "apart, `=` only when both are the same single point, otherwise `?`. Censoring cannot make a sign, and every `?` has a censored "
           "or unscorable cell on at least one side (counted below by arm).",
           "- **The map** is v2's cell map plus `verdict_source` and `verdict_why`, plus the twelve cells census ADDENDA 30–32 made cells of "
           "record after v2's map was cut (ADDENDUM 3e), plus one `CONDITION` row per ADDENDUM 3d condition and the `COUNT` rows of the "
           "second method. The pointers were authored by the lead, and by three extraction passes it commissioned, all read-only. The "
           "instrument re-reads every cited line on every run, so a pointer that does not hold prints `unmeasured`.",
           "- **The second method's disagreements are listed, never resolved** (ADDENDUM 3). Each row carries its source's own description "
           "of the population it counts: a landed-only reading, one wave's share of a condition, a figure an addendum superseded, the "
           "first-run cells a re-fire replaced.", ""]
    tail = ["\n## Second method: every count a result of record already prints, against the instrument's k\n",
            "| model | problem | field | arm | extras | printed | instrument | verdict | source |", "|---|---|---|---|---|---|---|---|---|"]
    tail += ["| %s | %s | %s | %s | %s |" % (" | ".join(k), pr, mine, v, src) for k, pr, mine, v, src in sm] or ["| none | | | | | | | | |"]
    tail += ["\n## The rc-3 census's cells (§P2): the record's class, and the census's beside it\n",
             "| model | problem | field | arm | extras | cell | class of record | census (variant class tests) |", "|---|---|---|---|---|---|---|---|"]
    tail += ["| %s | %s | %s | %s |" % (" | ".join(k), f["cell"], f["cls"] or "unmeasured", f["rc3"]) for k, f in rc3] or ["| none |"]
    tail += ["\n## Unmeasured cells\n", "| model | problem | field | arm | extras | cell | why |", "|---|---|---|---|---|---|---|"]
    tail += ["| %s | %s | %s |" % (" | ".join(k), f["cell"], f["reason"]) for k, f in unm] or ["| none | | | | | | |"]
    tail += ["\n## Per-cell verdicts and their sources (every table entry derives from these rows)\n",
             "| model | problem | field | arm | extras | cell | class | V | K | E | source |", "|---|---|---|---|---|---|---|---|---|---|---|"]
    tail += ["| %s | %s | %s | %s | %s | %s | %s |" % (" | ".join(k), f["cell"], f["cls"] or "unmeasured", f.get("V") or "-", f.get("K") or "-",
             f.get("E") or "-", f.get("prov") or f["reason"]) for k, f in prov]
    txt = "\n".join(hdr + body + tail) + "\n"
    if a.out:
        open(a.out, "w", encoding="utf-8").write(txt)
    else:
        sys.stdout.write(txt)
    print(check, file=sys.stderr)
    for f in fails[:40]:
        print("FAIL " + f, file=sys.stderr)
    for k, f in unm[:40]:
        print("UNMEASURED %s %s: %s" % ("/".join(k), f["cell"], f["reason"]), file=sys.stderr)
    print("second method: %d compared, %d disagreement(s), %d with no verified cause" % (len(sm), dis, len(nocause)), file=sys.stderr)
    for k, why in nocause:
        print("NO CAUSE %s: %s" % ("/".join(k), why), file=sys.stderr)
    return 0 if not (fails or unm) else 1


if __name__ == "__main__":
    sys.exit(main())
