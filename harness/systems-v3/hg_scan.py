#!/usr/bin/env python3
"""hg_scan.py — the HG A + B reading, executed against its registration.

The authority is AMENDMENT-HG-AB-registration-2026-09-26.md (beside this file). This program
parses that file's TABLE 1 and TABLE 2 out of their fenced blocks, so the population is the
registered one by construction, never a retyped list.

  fetch     --host-file F --out D     per cell, `cat` repo/LANDING.md (unless NF) and repo/BUS.md
                                      over ssh; write D/texts/<key>.txt = LANDING.md + BUS.md
                                      (byte concatenation, exactly what `cat A B` writes) and
                                      D/texts/MANIFEST.tsv. The host is LINE 1 of F; no host
                                      name is written by this program.
  scan      --export E --out D        run E/harness/systems-v3/ambiguity_scan.py per text; one
                                      JSON per cell into D/json/<key>.json
  read      --out D [--repo R --ref origin/main]
                                      derive every number from D/json (A) and from TABLE 2's
                                      recorded locations at R:ref (B); print READING markdown
  --selftest --export E              red-first fixtures for the classes + mutants that must red

<key> = condition_key with '|' -> '_' + '__' + cell_id, because several cell ids appear under two
conditions (a phase-1 root and a phase-2 root).

DECLARED CHOICES (where the registration is silent) are printed verbatim in the reading; the
list is CHOICES below, so the program and its report cannot disagree.
"""
import argparse, collections, hashlib, json, os, re, statistics, subprocess, sys, tempfile
from concurrent.futures import ThreadPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
REG = os.path.join(HERE, "AMENDMENT-HG-AB-registration-2026-09-26.md")
ARMS = ("plain", "salt-diet", "placebo")
MODELS = {"O": "claude-opus-5", "S": "claude-sonnet-5", "P": "gemini-3.1-pro-high", "F": "gemini-3.8-flash-high"}

CHOICES = [
    "C1  CLASS PRECEDENCE: WRONG > SILENT > DOCUMENTED > NOTICED. §HG1's rows overlap in two places "
    "(a wrong hit on an undetected id; a resolution hit on an undetected id). Any wrong hit is WRONG (its row says 'any'); "
    "otherwise an undetected id is SILENT even if a resolution pattern hit (DOCUMENTED requires 'detected').",
    "C2  ASKED is a flag beside the class, not a fifth class: detected AND no resolution hit AND >= 1 detect-hit line ending "
    "in '?' (after trailing whitespace is stripped). It is independent of WRONG. A cell is ASKED if any of its planted ids is.",
    "C3  ASKED is read from the JSON alone (§HG6: 'the RESULT is derived from those JSONs alone'). The scanner stores each "
    "hit line as strip()[:120], so a hit line longer than 120 characters that ends in '?' is invisible to that reading. "
    "The full-line reading (from the kept text) is printed beside it as a sensitivity, and the count of truncated hit lines "
    "is printed.",
    "C4  A1-A4 are read over the GRID population (lanes claude + agy: the 535 cells of the 181 DONE conditions). HC1's 45 cells "
    "enter A5 only (§HG3: HC1 counts +0 to the grid and is added because A5 needs it). A1-A4 with HC1's plain and salt-diet "
    "cells added are printed as a sensitivity.",
    "C5  A5 compares placebo with HC1's OWN plain and salt-diet cells (same stage, same model, same problems), not with the grid.",
    "C6  Shares: A1, A2, A3 are shares of PLANTED ITEMS, i.e. (cell, planted id) pairs, 3 per cell; A4 is a share of CELLS "
    "(its wording). Pooled = one ratio over all items of the arm, not a mean of per-condition ratios.",
    "C7  The missingness readings (i)/(ii) of §HG3 are printed for EVERY prediction A1-A5, not only A1 and A2, and a verdict is "
    "given under each reading separately.",
    "C8  The scanner's 'scored_at: landed-1' field (LRU get_miss_effect only) is NOT applied: §HG6 fixes one text per cell and "
    "the scanner's output over it. A sensitivity dropping LRU get_miss_effect in spec-change (phase-2 text) cells is printed.",
    "C9  An NF cell's directory is the root of the other cells of its condition (grouped by lane AND condition key, because HC1 "
    "reuses the grid's condition keys). Where every cell of a condition is NF, the root "
    "is the opposite-arm condition's root (same model, problem, field, extras, result file) with '-plain' replaced by "
    "'-saltdiet'. Each derived path is proven by a successful `cat` of its BUS.md, and the LANDING.md `cat` is recorded as failing.",
    "C10 B, the REGRESSIONS column: every recorded value is 'f/t' with f = FAILED of t (AMENDMENT-specchange-taskshape-2026-09-09 "
    ":67, 'REGRESSIONS 3/9  3 FAILED of 9  <- a HIGH number is BAD'). The registration writes 'p/t'; the pass share used here is "
    "(t - f)/t, pooled as sum(t - f)/sum(t). The share of cells with f = 0 is printed beside it.",
    "C11 B, missing: ABSENT (a BUILD-FAIL cell), UNREAD, NOT RECORDED and NOT IN REPO are all MISSING and counted; nothing is "
    "substituted (the two l8cpss phase-2 meters named as 'on the box' are not read).",
    "C12 B1 pools problems within a model (its wording: 'within model'), the median over that model's spec-change cells per arm. "
    "'A majority of models with both arms' = strictly more than half. Sonnet's salt-diet arm covers only Crc32 and LRU while its "
    "plain arm covers five problems, so a problem-matched median table is printed as a descriptive check.",
    "C13 B1 cost: Opus phase 1 = the `cost` column of the matrix1 tokens table (USD); Opus phase 2 = `cost_usd` of the named "
    "spec-change file (USD); Sonnet = p1_COST (col 12) and p2_COST (col 24), USD; agy = `T` of the phase_facts record "
    "(tokens). A CAP-COST (censored) phase 2 enters with its recorded cost, which is a floor, and is flagged.",
    "C15 Sonnet's p1_COST and p2_COST (blockSC-cells.tsv cols 12, 24) include the harness's own sandbox probe, per that file's "
    "header line 7; they are used as recorded and not corrected.",
    "C14 TABLE 2's short file names are resolved to repository paths by the fixed map FILEMAP in this program, and every cited "
    "line is checked to carry the cell's id before its value is used; a line that does not is a failure, not a lookup.",
]

# ---------------------------------------------------------------- registration tables
def fenced_after(text, marker):
    i = text.index(marker)
    a = text.index("```", i) + 3
    a = text.index("\n", a) + 1
    b = text.index("```", a)
    return text[a:b].rstrip("\n").split("\n")

def table1(reg=REG):
    lines = fenced_after(open(reg, encoding="utf-8").read(), "**TABLE 1")
    hdr = lines[0].split("\t")
    rows = []
    for l in lines[1:]:
        f = l.split("\t")
        f += [""] * (len(hdr) - len(f))
        r = dict(zip(hdr, f))
        m, prob, field, arm, extra = r["condition_key"].split("|")
        r.update(model=m, problem=prob, field=field, arm=arm, extras=extra)
        r["key"] = r["condition_key"].replace("|", "_") + "__" + r["cell_id"]
        r["grid"] = r["lane"] != "claude-hc1"
        rows.append(r)
    return rows

def expand_ids(tok):
    parts = tok.split("/")
    first = parts[0]
    out = [first]
    for p in parts[1:]:
        out.append(first[: len(first) - len(p)] + p)
    return out

def table2(reg=REG):
    lines = fenced_after(open(reg, encoding="utf-8").read(), "**TABLE 2")
    out = []
    for l in lines[1:]:
        ck, ids, p1, p2, rg = l.split("\t")
        out.append(dict(condition_key=ck, ids=expand_ids(ids), p1=p1, p2=p2, rg=rg))
    return out

def hg5(reg=REG):
    t = open(reg, encoding="utf-8").read()
    a = t.index("## §HG5"); b = t.index("## §HG6")
    return t[a:b].strip()

# ---------------------------------------------------------------- roots (C9)
def cell_dirs(rows):
    by_cond = collections.defaultdict(list)
    for r in rows:
        by_cond[(r["lane"], r["condition_key"])].append(r)  # HC1 reuses grid condition keys: group by lane too
    out = {}
    for r in rows:
        if r["landing_path"] != "NF":
            out[r["key"]] = (r["landing_path"], "registered")
            continue
        sib = [s for s in by_cond[(r["lane"], r["condition_key"])] if s["landing_path"] != "NF"]
        roots = {os.path.dirname(s["landing_path"]) for s in sib}
        if len(roots) == 1:
            out[r["key"]] = (roots.pop() + "/" + r["cell_id"], "sibling root")
            continue
        if len(roots) > 1:
            out[r["key"]] = (None, "AMBIGUOUS sibling roots " + ",".join(sorted(roots)))
            continue
        opp = "plain" if r["arm"] == "salt-diet" else None
        cand = {os.path.dirname(s["landing_path"]) for s in rows
                if opp and s["model"] == r["model"] and s["problem"] == r["problem"] and s["field"] == r["field"]
                and s["extras"] == r["extras"] and s["arm"] == opp and s["result_file"] == r["result_file"] and s["lane"] == r["lane"]
                and s["landing_path"] != "NF"}
        if len(cand) == 1:
            root = cand.pop()
            if root.endswith("-plain"):
                out[r["key"]] = (root[: -len("-plain")] + "-saltdiet/" + r["cell_id"], "opposite-arm root, -plain -> -saltdiet")
                continue
        out[r["key"]] = (None, "UNDERIVABLE")
    return out

# ---------------------------------------------------------------- fetch
def fetch(args):
    host = open(os.path.expanduser(args.host_file), encoding="utf-8").readline().strip()
    if not host:
        sys.exit("host file line 1 is empty")
    rows = table1()
    dirs = cell_dirs(rows)
    tdir = os.path.join(args.out, "texts"); os.makedirs(tdir, exist_ok=True)
    cm = os.path.expanduser("~/.ssh/hgcm-%C")  # a short path: a Unix socket name is length-limited
    base = ["ssh", "-o", "BatchMode=yes", "-o", "ControlMaster=auto", "-o", "ControlPath=" + cm,
            "-o", "ControlPersist=300", host]

    def cat(path):
        for attempt in range(5):
            try:
                p = subprocess.run(base + ["cat", path], capture_output=True)
                return p.returncode, p.stdout
            except OSError:  # a transient fork failure on this box; retried, never read as an absent file
                import time; time.sleep(2 * (attempt + 1))
        raise RuntimeError("could not spawn ssh for " + path)

    def one(r):
        d, how = dirs[r["key"]]
        rec = dict(key=r["key"], cell_dir=d or "-", dir_from=how)
        if d is None:
            rec.update(landing_rc="-", landing_bytes="-", bus_rc="-", bus_bytes="-", text_bytes="-", sha256="-", status="NO-DIR")
            return rec
        lrc, lb = cat(d + "/repo/LANDING.md")
        brc, bb = cat(d + "/repo/BUS.md")
        rec.update(landing_rc=lrc, landing_bytes=len(lb) if lrc == 0 else "-", bus_rc=brc, bus_bytes=len(bb) if brc == 0 else "-")
        nf = r["landing_path"] == "NF"
        text = (b"" if nf or lrc != 0 else lb) + (bb if brc == 0 else b"")
        status = []
        if brc != 0: status.append("BUS-MISSING")
        if not nf and lrc != 0: status.append("LANDING-MISSING")
        if nf and lrc == 0: status.append("NF-BUT-LANDING-EXISTS(omitted per registration)")
        if not nf and lrc == 0 and str(len(lb)) != r["landing_bytes"]:
            status.append(f"LANDING-BYTES {len(lb)}!=registered {r['landing_bytes']}")
        if brc == 0:
            open(os.path.join(tdir, r["key"] + ".txt"), "wb").write(text)
        rec.update(text_bytes=len(text) if brc == 0 else "-", sha256=hashlib.sha256(text).hexdigest()[:16] if brc == 0 else "-",
                   status=";".join(status) or "OK")
        return rec

    recs = [one(rows[0])]  # the first call opens the shared connection alone
    with ThreadPoolExecutor(3) as ex:
        recs += list(ex.map(one, rows[1:]))
    cols = ["key", "cell_dir", "dir_from", "landing_rc", "landing_bytes", "bus_rc", "bus_bytes", "text_bytes", "sha256", "status"]
    with open(os.path.join(tdir, "MANIFEST.tsv"), "w") as f:
        f.write("\t".join(cols) + "\n")
        for rec in recs:
            f.write("\t".join(str(rec[c]) for c in cols) + "\n")
    bad = [r for r in recs if r["status"] != "OK"]
    print(f"fetched {sum(1 for r in recs if r['bus_rc'] == 0)} of {len(recs)} texts; {len(bad)} rows with a status other than OK")
    for r in bad:
        print("  ", r["key"], r["status"])

# ---------------------------------------------------------------- scan
def scan(args):
    scanner = os.path.join(args.export, "harness", "systems-v3", "ambiguity_scan.py")
    packet = os.path.join(args.export, "harness", "systems-v3", "packet")
    tasks = os.path.join(args.export, "tasks", "systems-v3")
    rows = table1()
    tdir = os.path.join(args.out, "texts"); jdir = os.path.join(args.out, "json"); os.makedirs(jdir, exist_ok=True)
    fails = []

    def one(r):
        t = os.path.join(tdir, r["key"] + ".txt")
        if not os.path.exists(t):
            return (r["key"], "NO-TEXT")
        p = subprocess.run([sys.executable, scanner, os.path.join(tasks, r["problem"]), t, "--packet", packet],
                           capture_output=True, text=True)
        if p.returncode != 0:
            return (r["key"], f"rc {p.returncode}: {p.stderr.strip()[-200:]}")
        try:
            json.loads(p.stdout)
        except Exception as e:
            return (r["key"], f"bad JSON: {e}")
        open(os.path.join(jdir, r["key"] + ".json"), "w").write(p.stdout)
        return (r["key"], "OK")

    with ThreadPoolExecutor(8) as ex:
        res = list(ex.map(one, rows))
    fails = [x for x in res if x[1] != "OK"]
    with open(os.path.join(jdir, "SCAN-STATUS.tsv"), "w") as f:
        for k, s in res: f.write(f"{k}\t{s}\n")
    print(f"scanned {len(res) - len(fails)} of {len(res)}; {len(fails)} not scanned")
    for k, s in fails: print("  ", k, s)

# ---------------------------------------------------------------- classes (§HG1)
MUTANT = os.environ.get("HG_MUTANT", "")

def classify(v):
    if MUTANT == "documented-before-wrong":
        if v["detected"] and v["resolutions"]:
            return "DOCUMENTED"
    if v["wrong"]:
        return "WRONG"
    if not v["detected"]:
        return "SILENT"
    if v["resolutions"]:
        return "DOCUMENTED"
    return "NOTICED"

def asked(v, text_lines=None):
    if not v["detected"] or v["resolutions"]:
        return False
    for h in v["detect_hits"]:
        line = h[2] if text_lines is None else text_lines[h[0] - 1]
        if MUTANT == "asked-no-qmark":
            return True
        if line.rstrip().endswith("?"):
            return True
    return False

# ---------------------------------------------------------------- A
def load_a(out, rows):
    jdir = os.path.join(out, "json"); tdir = os.path.join(out, "texts")
    man = {}
    mp = os.path.join(tdir, "MANIFEST.tsv")
    if os.path.exists(mp):
        ls = open(mp).read().rstrip("\n").split("\n")
        h = ls[0].split("\t")
        for l in ls[1:]:
            d = dict(zip(h, l.split("\t"))); man[d["key"]] = d
    cells = []
    for r in rows:
        jp = os.path.join(jdir, r["key"] + ".json")
        c = dict(r, scanned=os.path.exists(jp), has_landing=r["landing_path"] != "NF", items=[])
        if c["scanned"]:
            j = json.load(open(jp))
            tl = open(os.path.join(tdir, r["key"] + ".txt"), encoding="utf-8", errors="replace").read().split("\n")
            for pid, v in j["planted"].items():
                trunc = sum(1 for h in v["detect_hits"] if len(h[2]) >= 120)
                c["items"].append(dict(id=pid, cls=classify(v), asked=asked(v), asked_full=asked(v, tl), trunc=trunc))
        cells.append(c)
    return cells, man

def agg(cells):
    n_items = sum(len(c["items"]) for c in cells)
    cnt = collections.Counter(i["cls"] for c in cells for i in c["items"])
    a_cells = sum(1 for c in cells if any(i["asked"] for i in c["items"]))
    a_full = sum(1 for c in cells if any(i["asked_full"] for i in c["items"]))
    a_items = sum(1 for c in cells for i in c["items"] if i["asked"])
    return dict(cells=len(cells), items=n_items, cnt=cnt, asked_cells=a_cells, asked_full_cells=a_full, asked_items=a_items)

def sh(n, d):
    return None if d == 0 else n / d

def fmt(x):
    return "n/a" if x is None else f"{100 * x:.1f} %"

def reading_filter(cells, rd):
    cs = [c for c in cells if c["scanned"]]
    return [c for c in cs if c["has_landing"]] if rd == "i" else cs

def verdicts(A, placeboA=None):
    """A: {arm: agg}; returns list of (id, verdict, numbers)."""
    out = []
    def share(arm, cls):
        a = A.get(arm); return None if a is None else sh(a["cnt"][cls], a["items"])
    p, s = share("plain", "DOCUMENTED"), share("salt-diet", "DOCUMENTED")
    out.append(("A1", "UNREADABLE" if None in (p, s) else ("HOLDS" if s > p else "FALSIFIED"),
                f"DOCUMENTED plain {fmt(p)} · salt-diet {fmt(s)}"))
    p, s = share("plain", "SILENT"), share("salt-diet", "SILENT")
    out.append(("A2", "UNREADABLE" if None in (p, s) else ("HOLDS" if s < p else "FALSIFIED"),
                f"SILENT plain {fmt(p)} · salt-diet {fmt(s)}"))
    p, s = share("plain", "WRONG"), share("salt-diet", "WRONG")
    out.append(("A3", "UNREADABLE" if None in (p, s) else ("HOLDS" if p < 0.10 and s < 0.10 else "FALSIFIED"),
                f"WRONG plain {fmt(p)} · salt-diet {fmt(s)} (threshold 10 %)"))
    def ask(arm):
        a = A.get(arm); return None if a is None else sh(a["asked_cells"], a["cells"])
    p, s = ask("plain"), ask("salt-diet")
    out.append(("A4", "UNREADABLE" if None in (p, s) else ("HOLDS" if p < 0.05 and s < 0.05 else "FALSIFIED"),
                f"ASKED cells plain {fmt(p)} · salt-diet {fmt(s)} (threshold 5 %)"))
    if placeboA is not None:
        def ps(arm):
            a = placeboA.get(arm); return None if a is None else sh(a["cnt"]["DOCUMENTED"], a["items"])
        p, s, b = ps("plain"), ps("salt-diet"), ps("placebo")
        v = "UNREADABLE" if None in (p, s, b) else ("FALSIFIED" if (b >= s or b <= p) else "HOLDS")
        out.append(("A5", v, f"HC1 DOCUMENTED plain {fmt(p)} · placebo {fmt(b)} · salt-diet {fmt(s)}"))
    return out

def arm_table(cells):
    A = {}
    for arm in ARMS:
        cs = [c for c in cells if c["arm"] == arm]
        if cs: A[arm] = agg(cs)
    return A

def table_md(A, title):
    L = [f"| {title} | cells | items | DOCUMENTED | NOTICED | WRONG | SILENT | ASKED items | ASKED cells | ASKED cells (full-line) |",
         "|---|---|---|---|---|---|---|---|---|---|"]
    for k, a in A.items():
        n = a["items"]
        L.append(f"| {k} | {a['cells']} | {n} | " + " | ".join(f"{a['cnt'][c]} ({fmt(sh(a['cnt'][c], n))})" for c in
                 ("DOCUMENTED", "NOTICED", "WRONG", "SILENT")) +
                 f" | {a['asked_items']} | {a['asked_cells']} ({fmt(sh(a['asked_cells'], a['cells']))}) | "
                 f"{a['asked_full_cells']} ({fmt(sh(a['asked_full_cells'], a['cells']))}) |")
    return "\n".join(L)

# ---------------------------------------------------------------- B
FILEMAP = {
    "matrix1-tokens.tsv": "harness/systems-v3-analysis/RESULT-tokens-table-matrix1-2026-09-10.tsv",
    "PS.tsv": "harness/systems-v3/RESULT-p1-specchange-2026-09-10.tsv",
    "S1-verdicts.tsv": "harness/systems-v3/RESULT-specchange-1-verdicts-2026-09-10.tsv",
    "blockSC-cells.tsv": "evidence/claude-lane-blocks-2026-09-21/blockSC-cells.tsv",
    "chainD phase_facts.json": "evidence/l8-chainD-2026-09-24/phase_facts.json",
    "chainF phase_facts.json": "evidence/l8-chainF-2026-09-24/phase_facts.json",
    "chainD-cells.tsv": "harness/systems-v3/RESULT-gemini-level8-chainD-2026-09-24-cells.tsv",
    "chainF-cells.tsv": "harness/systems-v3/RESULT-gemini-level8-chainF-2026-09-24-cells.tsv",
    "chainD md": "harness/systems-v3/RESULT-gemini-level8-chainD-2026-09-24.md",
}

class Repo:
    def __init__(self, repo, ref):
        self.repo, self.ref = repo, ref
        self.sha = subprocess.run(["git", "-C", repo, "rev-parse", ref], capture_output=True, text=True, check=True).stdout.strip()
        self.cache = {}
    def lines(self, short):
        path = FILEMAP[short]
        if path not in self.cache:
            t = subprocess.run(["git", "-C", self.repo, "show", f"{self.sha}:{path}"], capture_output=True, text=True, check=True).stdout
            self.cache[path] = t.split("\n")
        return self.cache[path]
    def line(self, short, n, cell):
        l = self.lines(short)[n - 1]
        if cell not in l:
            raise ValueError(f"{FILEMAP[short]}:{n} does not carry {cell}")
        return l
    def tsv_field(self, short, n, cell, col):
        hdr = None
        for l in self.lines(short):
            if not l.startswith("#"):
                hdr = l.split("\t"); break
        f = self.line(short, n, cell).split("\t")
        return f[hdr.index(col)] if isinstance(col, str) else f[col - 1]
    def facts(self, which):
        short = f"chain{which} phase_facts.json"
        return json.loads("\n".join(self.lines(short))), self.lines(short)

def b_records(repo):
    """One record per (condition, cell): model, arm, problem, unit, p1, p2, reg (f, t) or None, notes."""
    recs = []
    fD, lD = repo.facts("D"); fF, _ = repo.facts("F")
    idlines = [i + 1 for i, l in enumerate(lD) if l.strip().startswith('"id":')]
    D_by_line = {idlines[k]: rec for k, rec in enumerate(fD)}
    F_by = {(r["id"], r["phase"]): r for r in fF}
    for row in table2():
        m, prob, field, arm, extra = row["condition_key"].split("|")
        n = len(row["ids"])
        def nums(s):
            mm = re.search(r":([\d/]+)", s)
            ns = [int(x) for x in mm.group(1).split("/")] if mm else []
            return ns if len(ns) == n else ns * n if len(ns) == 1 else ns
        for k, cell in enumerate(row["ids"]):
            r = dict(condition_key=row["condition_key"], cell=cell, model=m, problem=prob, arm=arm, p1=None, p2=None,
                     reg=None, notes=[], unit="USD" if m in "OS" else "T")
            try:
                if m == "O":
                    n1 = nums(row["p1"])[k]
                    r["p1"] = float(repo.tsv_field("matrix1-tokens.tsv", n1, cell, "cost"))
                    if repo.tsv_field("matrix1-tokens.tsv", n1, cell, "status") == "FLOOR":
                        r["notes"].append("phase-1 FLOOR (a lower bound, so the ratio is an upper bound)")
                    short = "PS.tsv" if row["p2"].startswith("PS.tsv") else "S1-verdicts.tsv"
                    n2 = nums(row["p2"])[k]
                    r["p2"] = float(repo.tsv_field(short, n2, cell, "cost_usd"))
                    if repo.tsv_field(short, n2, cell, "censored") == "yes":
                        r["notes"].append("phase-2 CAP-COST (censored; cost is a floor)")
                    r["notes"].append("REGRESSIONS NOT RECORDED")
                elif m == "S":
                    ln = nums(row["p1"])[k]
                    r["p1"] = float(repo.tsv_field("blockSC-cells.tsv", ln, cell, 12))
                    r["p2"] = float(repo.tsv_field("blockSC-cells.tsv", ln, cell, 24))
                    if repo.tsv_field("blockSC-cells.tsv", ln, cell, "p2_capped") == "yes":
                        r["notes"].append("phase-2 capped (cost is a floor)")
                    rg = repo.tsv_field("blockSC-cells.tsv", ln, cell, 19)
                    r["reg_src"] = f"blockSC-cells.tsv:{ln} col19"
                    r["reg"] = rg
                else:
                    if "chainF" in row["p1"]:
                        r["p1"] = float(F_by[(cell, 1)]["T"]); r["p2"] = float(F_by[(cell, 2)]["T"])
                        for ph in (1, 2):
                            if F_by[(cell, ph)]["id"] != cell: raise ValueError("chainF id mismatch")
                    elif row["p1"].startswith("chainD md:"):
                        ln = int(re.search(r"md:(\d+)", row["p1"]).group(1))
                        l = repo.line("chainD md", ln, "phase 1")
                        mm = re.findall(r"phase (\d): T ([\d,]+)", l)
                        d = {int(a): float(b.replace(",", "")) for a, b in mm}
                        if cell not in "\n".join(repo.lines("chainD md")[ln - 4: ln]):
                            raise ValueError("chainD md block does not name " + cell)
                        r["p1"], r["p2"] = d[1], d[2]
                    else:
                        n1 = nums(row["p1"])[k]
                        rec1 = D_by_line[n1]
                        if rec1["id"] != cell or rec1["phase"] != 1: raise ValueError(f"phase_facts:{n1} is {rec1['id']} p{rec1['phase']}")
                        r["p1"] = float(rec1["T"])
                        if "NOT IN REPO" in row["p2"]:
                            r["notes"].append("phase-2 cost NOT IN REPO (missing)")
                        else:
                            n2 = nums(row["p2"])[k]
                            rec2 = D_by_line[n2]
                            if rec2["id"] != cell or rec2["phase"] != 2: raise ValueError(f"phase_facts:{n2} is {rec2['id']} p{rec2['phase']}")
                            r["p2"] = float(rec2["T"])
                    # regressions
                    if row["rg"].startswith("chainD md:"):
                        ln = int(re.search(r"md:(\d+)", row["rg"]).group(1))
                        l = repo.line("chainD md", ln, cell if cell in repo.lines("chainD md")[ln - 1] else "REGRESSIONS")
                        r["reg"] = re.search(r"REGRESSIONS (\S+)", l).group(1); r["reg_src"] = f"chainD md:{ln}"
                    elif "chainD md" in row["rg"]:
                        ln = int(re.search(r"md:(\d+)", row["rg"]).group(1))
                        l = repo.line("chainD md", ln, cell)
                        r["reg"] = re.search(r"REGRESSIONS (\S+)", l).group(1); r["reg_src"] = f"chainD md:{ln}"
                    else:
                        which = "chainD-cells.tsv" if "chainD" in row["rg"] else "chainF-cells.tsv"
                        ln = nums(row["rg"])[k]
                        r["reg"] = repo.tsv_field(which, ln, cell, "REGRESSIONS"); r["reg_src"] = f"{which}:{ln}"
            except Exception as e:
                r["notes"].append(f"FAILURE: {e}")
            recs.append(r)
    for r in recs:
        g = r["reg"]
        if g is not None and re.fullmatch(r"\d+/\d+", g):
            f, t = map(int, g.split("/")); r["reg_ft"] = (f, t)
        else:
            r["reg_ft"] = None
            if g is not None: r["notes"].append(f"REGRESSIONS {g} (missing)")
        r["ratio"] = r["p2"] / r["p1"] if r["p1"] and r["p2"] is not None else None
    return recs

def med(xs):
    return statistics.median(xs) if xs else None

def b_read(recs):
    L = []
    L.append("### B1 — cost-to-change = phase-2 ÷ phase-1 per cell; median per arm within model\n")
    L.append("| model | unit | plain n | plain median | salt-diet n | salt-diet median | salt-diet < plain? |")
    L.append("|---|---|---|---|---|---|---|")
    both, ge = 0, 0
    for m in "OSPF":
        rs = [r for r in recs if r["model"] == m]
        p = [r["ratio"] for r in rs if r["arm"] == "plain" and r["ratio"] is not None]
        s = [r["ratio"] for r in rs if r["arm"] == "salt-diet" and r["ratio"] is not None]
        mp, ms = med(p), med(s)
        cmp = "-"
        if p and s:
            both += 1
            cmp = "yes" if ms < mp else "NO"
            if ms >= mp: ge += 1
        L.append(f"| {m} {MODELS[m]} | {rs[0]['unit']} | {len(p)} | {mp and f'{mp:.3f}'} | {len(s)} | {ms and f'{ms:.3f}'} | {cmp} |")
    v = "UNREADABLE" if both == 0 else ("FALSIFIED" if ge > both / 2 else "HOLDS")
    L.append(f"\n**B1: {v}** — salt-diet median ≥ plain median in {ge} of {both} models with both arms "
             f"(falsified if in a strict majority).\n")
    flag = lambda r: any(("FLOOR" in n or "floor" in n) for n in r["notes"])
    L.append("Sensitivity (declared, not the registered reading) — dropping every cell whose phase-1 or phase-2 cost is flagged "
             "as a floor (FLOOR, CAP-COST, capped):\n")
    for m in "OSPF":
        rs = [r for r in recs if r["model"] == m and r["ratio"] is not None and not flag(r)]
        p = [r["ratio"] for r in rs if r["arm"] == "plain"]; s = [r["ratio"] for r in rs if r["arm"] == "salt-diet"]
        L.append(f"- {m}: plain n {len(p)} median {med(p) and f'{med(p):.3f}'} · salt-diet n {len(s)} median {med(s) and f'{med(s):.3f}'} "
                 f"· dropped {sum(1 for r in recs if r['model'] == m and flag(r))}")
    L.append("")
    L.append("Descriptive — the ratio's two terms, median per arm within model (same unit as the row); a ratio falls when "
             "phase 1 rises, so read B1 beside these:\n")
    L.append("| model | unit | plain p1 | plain p2 | salt-diet p1 | salt-diet p2 |"); L.append("|---|---|---|---|---|---|")
    for m in "OSPF":
        rs = [r for r in recs if r["model"] == m and r["ratio"] is not None]
        g = lambda arm, k: med([r[k] for r in rs if r["arm"] == arm])
        f2 = lambda x: "-" if x is None else (f"{x:.2f}" if rs[0]["unit"] == "USD" else f"{x:,.0f}")
        L.append(f"| {m} | {rs[0]['unit']} | {f2(g('plain','p1'))} | {f2(g('plain','p2'))} | {f2(g('salt-diet','p1'))} | {f2(g('salt-diet','p2'))} |")
    L.append("")
    miss = [r for r in recs if r["ratio"] is None]
    L.append(f"B1 missing ratios: {len(miss)} — " + "; ".join(f"{r['cell']} ({', '.join(r['notes'])})" for r in miss))
    L.append("\nDescriptive (C12) — problem-matched medians, only problems where the model has both arms:\n")
    L.append("| model | problem | plain n / median | salt-diet n / median |")
    L.append("|---|---|---|---|")
    for m in "OSPF":
        for prob in sorted({r["problem"] for r in recs if r["model"] == m}):
            rs = [r for r in recs if r["model"] == m and r["problem"] == prob and r["ratio"] is not None]
            p = [r["ratio"] for r in rs if r["arm"] == "plain"]; s = [r["ratio"] for r in rs if r["arm"] == "salt-diet"]
            if p and s:
                L.append(f"| {m} | {prob} | {len(p)} / {med(p):.3f} | {len(s)} / {med(s):.3f} |")
    L.append("\n### B2 — pooled REGRESSIONS pass share per arm, Sonnet + agy (C10: recorded f/t is FAILED of t)\n")
    res = {}
    L.append("| scope | arm | cells with a value | missing | Σ(t−f)/Σt | cells with f = 0 |")
    L.append("|---|---|---|---|---|---|")
    for scope, ms in (("POOLED S+P+F", "SPF"), ("S", "S"), ("P", "P"), ("F", "F")):
        for arm in ("plain", "salt-diet"):
            rs = [r for r in recs if r["model"] in ms and r["arm"] == arm]
            have = [r for r in rs if r["reg_ft"]]
            ft = [r["reg_ft"] for r in have]
            num = sum(t - f for f, t in ft); den = sum(t for f, t in ft)
            z = sum(1 for f, t in ft if f == 0)
            share = sh(num, den)
            if scope.startswith("POOLED"): res[arm] = share
            L.append(f"| {scope} | {arm} | {len(have)} | {len(rs) - len(have)} | {num}/{den} = {fmt(share)} | {z}/{len(have)} |")
    L.append("\nDescriptive (C12) — B2 on problem-matched cells only (model × problem with both arms valued):\n")
    L.append("| arm | cells | Σ(t−f)/Σt |"); L.append("|---|---|---|")
    pairs = {(r["model"], r["problem"]) for r in recs if r["model"] in "SPF" and r["reg_ft"]}
    matched = {mp for mp in pairs if all(any(r["reg_ft"] and (r["model"], r["problem"]) == mp and r["arm"] == a for r in recs)
                                         for a in ("plain", "salt-diet"))}
    for arm in ("plain", "salt-diet"):
        ft = [r["reg_ft"] for r in recs if r["reg_ft"] and r["arm"] == arm and (r["model"], r["problem"]) in matched]
        num = sum(t - f for f, t in ft); den = sum(t for f, t in ft)
        L.append(f"| {arm} | {len(ft)} | {num}/{den} = {fmt(sh(num, den))} |")
    p, s = res.get("plain"), res.get("salt-diet")
    v = "UNREADABLE" if None in (p, s) else ("HOLDS" if s >= p else "FALSIFIED")
    L.append(f"\n**B2: {v}** — pooled pass share salt-diet {fmt(s)} vs plain {fmt(p)} (falsified if salt-diet is below).\n")
    om = [r for r in recs if r["model"] == "O"]
    L.append(f"Opus gap (§HG2): {len(om)} Opus spec-change cells carry NO REGRESSIONS record "
             f"(plain {sum(1 for r in om if r['arm']=='plain')}, salt-diet {sum(1 for r in om if r['arm']=='salt-diet')}); "
             "B2 does not cover them.")
    missing = [r for r in recs if r["model"] in "SPF" and not r["reg_ft"]]
    L.append(f"B2 missing (Sonnet + agy): {len(missing)} — " + "; ".join(f"{r['cell']} [{r['reg']}]" for r in missing))
    fails = [r for r in recs if any(n.startswith("FAILURE") for n in r["notes"])]
    L.append(f"\nB lookup failures: {len(fails)}" + ("" if not fails else " — " + "; ".join(f"{r['cell']}: {r['notes']}" for r in fails)))
    return L, (v, res)

# ---------------------------------------------------------------- read
def read(args):
    rows = table1()
    cells, man = load_a(args.out, rows)
    grid = [c for c in cells if c["grid"]]; hc1 = [c for c in cells if not c["grid"]]
    L = []
    P = L.append
    reg_sha = subprocess.run(["git", "-C", HERE, "log", "-1", "--format=%H %cI", "--", os.path.basename(REG)],
                             capture_output=True, text=True).stdout.strip()
    P("# HG A + B — READING against the registration\n")
    P(f"Registration: `{os.path.basename(REG)}`, last commit touching it `{reg_sha}`. Every number below is printed by "
      "`hg_scan.py read` from the per-cell scanner JSONs (A) and from TABLE 2's recorded locations (B).\n")
    js = [os.path.getmtime(os.path.join(args.out, "json", f)) for f in os.listdir(os.path.join(args.out, "json")) if f.endswith(".json")]
    if js:
        import datetime
        P(f"Scan output written {datetime.datetime.fromtimestamp(min(js), datetime.timezone.utc):%Y-%m-%dT%H:%M:%SZ} → "
          f"{datetime.datetime.fromtimestamp(max(js), datetime.timezone.utc):%Y-%m-%dT%H:%M:%SZ} (the registration commit must precede it).\n")
    # population
    conds = {c["condition_key"] for c in grid}
    P("## POPULATION — registered vs scanned\n")
    P(f"- TABLE 1 rows: {len(rows)} (grid {len(grid)} cells in {len(conds)} conditions; HC1 {len(hc1)} cells). "
      "Registered: 535 grid cells in 181 conditions + 45 HC1.")
    nf = [c for c in cells if not c["has_landing"]]
    P(f"- NF (no LANDING.md) per TABLE 1: grid {sum(1 for c in nf if c['grid'])} · HC1 {sum(1 for c in nf if not c['grid'])}. Registered: 22 · 2.")
    sc = [c for c in cells if c["scanned"]]
    P(f"- Texts fetched: {sum(1 for k in man if man[k]['bus_rc'] == '0')} of {len(rows)}; scanned: {len(sc)} of {len(rows)}; "
      f"not scanned: {len(rows) - len(sc)}.")
    st = [(k, d["status"], d["dir_from"]) for k, d in man.items() if d["status"] != "OK"]
    P(f"- Manifest rows with a status other than OK: {len(st)}" + ("" if not st else ""))
    for k, s, f in st: P(f"  - `{k}`: {s} (dir from: {f})")
    der = [(k, d["dir_from"], d["cell_dir"]) for k, d in man.items() if d["dir_from"] != "registered"]
    P(f"- NF cell directories derived under C9: {len(der)}")
    for k, f, d in der: P(f"  - `{k}` → `{d}` ({f}; LANDING.md cat rc {man[k]['landing_rc']}, BUS.md cat rc {man[k]['bus_rc']}, "
                          f"BUS.md {man[k]['bus_bytes']} B)")
    sp = os.path.join(args.out, "json", "SCAN-STATUS.tsv")
    if os.path.exists(sp):
        bad = [l for l in open(sp).read().split("\n") if l and not l.endswith("\tOK")]
        P(f"- Scanner failures: {len(bad)}" + "".join(f"\n  - `{b}`" for b in bad))
    tr = sum(i["trunc"] for c in sc for i in c["items"])
    P(f"- Detect-hit lines stored at the scanner's 120-character truncation (C3): {tr}")
    diff = sum(1 for c in sc for i in c["items"] if i["asked"] != i["asked_full"])
    P(f"- (cell, id) pairs where JSON-alone ASKED and full-line ASKED differ: {diff}\n")

    P("## §HG5 — printed beside every reading (verbatim from the registration)\n")
    P(hg5() + "\n")

    P("## A — the two missingness readings side by side\n")
    summ = {}
    for rd, name in (("i", "(i) cells WITH a LANDING.md"), ("ii", "(ii) ALL cells, BUS.md alone where LANDING.md is absent")):
        g = reading_filter(grid, rd); h = reading_filter(hc1, rd)
        A = arm_table(g); H = arm_table(h)
        P(f"### Reading {name}\n")
        P(table_md(A, "grid arm")); P("")
        P(table_md(H, "HC1 arm")); P("")
        vs = verdicts(A, H)
        summ[rd] = vs
        for vid, v, nums in vs:
            P(f"- **{vid}: {v}** — {nums}")
        P("")
    P("### A verdicts, the two readings side by side\n")
    P("| prediction | reading (i) | reading (ii) |")
    P("|---|---|---|")
    for k in range(5):
        a, b = summ["i"][k], summ["ii"][k]
        P(f"| {a[0]} | {a[1]} — {a[2]} | {b[1]} — {b[2]} |")
    P("")
    P("### A sensitivities (declared, not predictions)\n")
    for rd in ("i", "ii"):
        g = reading_filter(grid, rd) + [c for c in reading_filter(hc1, rd) if c["arm"] != "placebo"]
        vs = verdicts(arm_table(g))
        P(f"- C4, grid + HC1 plain/salt-diet, reading ({rd}): " + " · ".join(f"{a} {b} ({c})" for a, b, c in vs))
    for rd in ("i", "ii"):
        g = reading_filter(grid, rd)
        A = {}
        for arm in ("plain", "salt-diet"):
            cs = [c for c in g if c["arm"] == arm]
            A[arm] = dict(cells=len(cs), asked_cells=sum(1 for c in cs if any(i["asked_full"] for i in c["items"])))
        P(f"- C3, A4 with full-line ASKED, reading ({rd}): plain {A['plain']['asked_cells']}/{A['plain']['cells']} = "
          f"{fmt(sh(A['plain']['asked_cells'], A['plain']['cells']))} · salt-diet {A['salt-diet']['asked_cells']}/{A['salt-diet']['cells']} = "
          f"{fmt(sh(A['salt-diet']['asked_cells'], A['salt-diet']['cells']))}")
    for rd in ("i", "ii"):
        g = []
        for c in reading_filter(grid, rd):
            c2 = dict(c)
            if c["extras"] == "sc" and c["problem"] == "LRU":
                c2["items"] = [i for i in c["items"] if i["id"] != "get_miss_effect"]
            g.append(c2)
        vs = verdicts(arm_table(g))[:3]
        P(f"- C8, dropping LRU get_miss_effect from spec-change cells, reading ({rd}): " + " · ".join(f"{a} {b} ({c})" for a, b, c in vs))
    P("")
    P("### Descriptive only — per lane and per model (no predictions; reading (ii), all cells)\n")
    allc = reading_filter(cells, "ii")
    for lane in ("claude", "agy", "claude-hc1"):
        P(table_md(arm_table([c for c in allc if c["lane"] == lane]), f"lane {lane}")); P("")
    for m in "OSPF":
        P(table_md(arm_table([c for c in allc if c["model"] == m and c["grid"]]), f"grid model {m}")); P("")
    P("Per planted id (grid, reading (ii)), counts of DOCUMENTED / NOTICED / WRONG / SILENT per arm:\n")
    P("| problem | id | plain D/N/W/S | salt-diet D/N/W/S |"); P("|---|---|---|---|")
    ids = sorted({(c["problem"], i["id"]) for c in allc for i in c["items"]})
    for prob, pid in ids:
        cc = {}
        for arm in ("plain", "salt-diet"):
            k = collections.Counter(i["cls"] for c in allc if c["grid"] and c["arm"] == arm and c["problem"] == prob
                                    for i in c["items"] if i["id"] == pid)
            cc[arm] = "/".join(str(k[x]) for x in ("DOCUMENTED", "NOTICED", "WRONG", "SILENT"))
        P(f"| {prob} | {pid} | {cc['plain']} | {cc['salt-diet']} |")
    P("")
    P("## B — change (analysis commitments, NOT blind: §HG2)\n")
    repo = Repo(args.repo, args.ref)
    P(f"Inputs read with `git show {repo.sha}:<path>` ({args.ref}). Units: Opus and Sonnet in USD, agy (P, F) in tokens T; "
      "B1 never compares across units.\n")
    recs = b_records(repo)
    P(f"TABLE 2 expands to {len(recs)} (condition, cell) records in {len({r['condition_key'] for r in recs})} distinct condition keys "
      "(registered in §HG3: 104 cells, 47 conditions). TABLE 1 carries "
      f"{len({r['condition_key'] for r in rows if r['extras'] == 'sc'})} distinct spec-change condition keys.")
    t1sc = {(r["condition_key"], r["cell_id"]) for r in rows if r["extras"] == "sc"}
    t2 = {(r["condition_key"], r["cell"]) for r in recs}
    P(f"TABLE 1 spec-change cells not in TABLE 2: {sorted(t1sc - t2)} · TABLE 2 cells not in TABLE 1: {sorted(t2 - t1sc)}\n")
    bl, _ = b_read(recs)
    L.extend(bl)
    P("\n### B per-cell record\n")
    P("| condition | cell | unit | phase 1 | phase 2 | ratio | REGRESSIONS (f/t, src) | notes |"); P("|---|---|---|---|---|---|---|---|")
    for r in recs:
        ratio = "" if r["ratio"] is None else "%.3f" % r["ratio"]
        P(f"| {r['condition_key']} | {r['cell']} | {r['unit']} | {r['p1']} | {r['p2']} | "
          f"{ratio} | {r['reg']} {r.get('reg_src','')} | {'; '.join(r['notes'])} |")
    P("\n## DECLARED CHOICES (the registration is silent on each)\n")
    for c in CHOICES: P(f"- {c}")
    out = "\n".join(L) + "\n"
    if args.write:
        open(args.write, "w").write(out)
    print(out)

# ---------------------------------------------------------------- selftest
FIX = {
    # name: (task, text, {id: expected class}, {id: expected asked}, cell_asked)
    "documented": ("LRU", "## DECISIONS\n- capacity 0: a precondition — the caller must pass at least 1; new(0) is undefined.\n",
                   {"capacity_zero": "DOCUMENTED", "get_miss_effect": "SILENT"}, {"capacity_zero": False}, False),
    "noticed": ("LRU", "key_at with an index past the end is something this landing did not settle.\n",
                {"observer_out_of_range": "NOTICED"}, {"observer_out_of_range": False}, False),
    "wrong": ("LRU", "On a miss the get will evict the oldest entry.\n", {"get_miss_effect": "WRONG"}, {}, False),
    "wrong-beats-resolution": ("LRU", "A get miss leaves the order unchanged.\nOn a miss the get will evict the oldest entry.\n",
                               {"get_miss_effect": "WRONG"}, {}, False),
    "silent": ("LRU", "Everything built and every test passes.\n",
               {"get_miss_effect": "SILENT", "capacity_zero": "SILENT", "observer_out_of_range": "SILENT"}, {}, False),
    "asked": ("LRU", "What should key_at give for an index past the end?\n",
              {"observer_out_of_range": "NOTICED"}, {"observer_out_of_range": True}, True),
    "qmark-off-hit-line": ("LRU", "Is this all right?\nkey_at with an index past the end is left open by me.\n",
                           {"observer_out_of_range": "NOTICED"}, {"observer_out_of_range": False}, False),
    "resolved-question-not-asked": ("LRU", "capacity 0 is a precondition: the caller must pass at least 1, is that right?\n",
                                    {"capacity_zero": "DOCUMENTED"}, {"capacity_zero": False}, False),
}

def selftest(export):
    scanner = os.path.join(export, "harness", "systems-v3", "ambiguity_scan.py")
    packet = os.path.join(export, "harness", "systems-v3", "packet")
    tasks = os.path.join(export, "tasks", "systems-v3")
    results = {}
    for name, (task, text, exp_cls, exp_ask, exp_cell) in FIX.items():
        with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False) as f:
            f.write(text); p = f.name
        j = json.loads(subprocess.run([sys.executable, scanner, os.path.join(tasks, task), p, "--packet", packet],
                                      capture_output=True, text=True, check=True).stdout)
        os.unlink(p)
        ok = all(classify(j["planted"][k]) == v for k, v in exp_cls.items())
        ok = ok and all(asked(j["planted"][k]) == v for k, v in exp_ask.items())
        ok = ok and (any(asked(v) for v in j["planted"].values()) == exp_cell)
        if not ok:
            got = {k: (classify(v), asked(v)) for k, v in j["planted"].items()}
            print(f"  RED  {name}: got {got}")
        results[name] = ok
    # the precedence table itself, on synthetic records (no scanner): every row of §HG1
    syn = [({"detected": True, "resolutions": ["x"], "wrong": False, "detect_hits": []}, "DOCUMENTED"),
           ({"detected": True, "resolutions": [], "wrong": False, "detect_hits": []}, "NOTICED"),
           ({"detected": True, "resolutions": ["x"], "wrong": True, "detect_hits": []}, "WRONG"),
           ({"detected": False, "resolutions": [], "wrong": True, "detect_hits": []}, "WRONG"),
           ({"detected": False, "resolutions": ["x"], "wrong": False, "detect_hits": []}, "SILENT"),
           ({"detected": False, "resolutions": [], "wrong": False, "detect_hits": []}, "SILENT")]
    results["precedence-table"] = all(classify(r) == e for r, e in syn)
    # the truncation divergence C3 declares: a 150-char hit line ending in '?' is ASKED full-line, not JSON-alone
    longq = ("key_at with an index past the end " + "x" * 100 + " what then?")
    v = {"detected": True, "resolutions": [], "wrong": False, "detect_hits": [[1, "p", longq.strip()[:120]]]}
    results["C3-truncation-declared"] = (asked(v) is False and asked(v, [longq]) is True)
    n_ok = sum(results.values())
    for k, ok in results.items():
        print(f"  {'GREEN' if ok else 'RED  '} {k}")
    print(f"hg_scan selftest{(' [mutant ' + MUTANT + ']') if MUTANT else ''}: {n_ok}/{len(results)} arms green")
    return results

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", nargs="?", choices=["fetch", "scan", "read"])
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--host-file"); ap.add_argument("--export"); ap.add_argument("--out")
    ap.add_argument("--repo", default=HERE); ap.add_argument("--ref", default="origin/main"); ap.add_argument("--write")
    a = ap.parse_args()
    if a.out: a.out = os.path.expanduser(a.out)
    if a.selftest:
        if MUTANT:
            r = selftest(a.export); sys.exit(0 if all(r.values()) else 1)
        r = selftest(a.export)
        ok = all(r.values())
        # the mutants: each must turn its NAMED arm red, run in a child so the switch is the environment's
        want = {"asked-no-qmark": {"noticed", "qmark-off-hit-line"},
                "documented-before-wrong": {"wrong-beats-resolution", "precedence-table"}}
        for mname, arms in want.items():
            p = subprocess.run([sys.executable, __file__, "--selftest", "--export", a.export], capture_output=True, text=True,
                               env=dict(os.environ, HG_MUTANT=mname))
            reds = {l.split()[1] for l in p.stdout.split("\n") if l.strip().startswith("RED") and len(l.split()) > 1}
            reds = {x.rstrip(":") for x in reds}
            hit = arms & reds
            print(f"  mutant {mname}: rc {p.returncode}, red arms {sorted(reds)} — named arm(s) {sorted(arms)} "
                  f"{'REDDENED' if hit else 'DID NOT REDDEN'}")
            ok = ok and p.returncode != 0 and bool(hit)
        print("hg_scan selftest", "GREEN" if ok else "RED")
        sys.exit(0 if ok else 1)
    {"fetch": fetch, "scan": scan, "read": read}[a.cmd](a)

if __name__ == "__main__":
    main()
