#!/usr/bin/env python3
"""recut.py — the re-cut of every comparison that holds a WEB-SERVED cell of record, old line beside new (O37, 2026-11-20).

The WEB-SERVED cells are READ from ../join.tsv (state column), never typed. For each instrument of record, it runs the
instrument twice, on its input of record (OLD) and on the same input with the WEB-SERVED cells taken out (NEW), and prints the
rows that differ with recut_diff.py. It changes no instrument. A cell is taken out the way each instrument already provides:
  tables_v2.py, tables_v3.py, tables_correctness_v3.py   the cell-map row's model is prefixed '#EXCLUDED-BY-RECORD '
  RESULT-gemini-blockNA-2026-09-28-prose-verify.py        the cell's row is dropped from a scratch copy of the cells TSV
  zf_result.py                                            the cell's row is dropped from a copy passed as --cells

  python3 recut.py OUTDIR          write OUTDIR/<label>-{old,new}.* and <label>-moved.txt, print each trailer
  python3 recut.py OUTDIR --check  as above, then exit 1 unless every <label>-moved.txt equals the tracked one beside this file

The CONTROL, run every time: each OLD output must reproduce its RESULT of record's table rows exactly (the RESULT files below);
a control that fails stops the run, so a NEW is never compared with an OLD that is not the record.
"""
import csv, os, shutil, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
V3 = os.path.join(REPO, "harness", "systems-v3")
PY = sys.executable

served = sorted(r[1] for r in csv.reader(open(os.path.join(HERE, "..", "join.tsv"), encoding="utf-8"), delimiter="\t")
                if len(r) > 10 and r[10] == "WEB-SERVED")
if not served:
    sys.exit("REFUSE: no WEB-SERVED cell in ../join.tsv")
out = os.path.abspath(sys.argv[1])
os.makedirs(out, exist_ok=True)
print(f"WEB-SERVED cells read from join.tsv: {len(served)}: {' '.join(served)}")


def run(args, log):
    with open(log, "w") as fh:
        return subprocess.run(args, cwd=V3, stdout=fh, stderr=subprocess.STDOUT).returncode


def table_rows(p):
    return [l for l in open(p, encoding="utf-8") if l.startswith("|")]


def mark(map_path, dst):
    n = 0
    with open(map_path, encoding="utf-8") as fh, open(dst, "w", encoding="utf-8") as w:
        hdr = None
        for l in fh:
            f = l.rstrip("\n").split("\t")
            if hdr is None:
                hdr = f
            elif "cell" in hdr and len(f) == len(hdr) and f[hdr.index("cell")] in served and not f[0].startswith("#"):
                f[0] = "#EXCLUDED-BY-RECORD " + f[0]
                l = "\t".join(f) + "\n"
                n += 1
            w.write(l)
    return n


def drop(tsv, dst, col):
    n = 0
    with open(tsv, encoding="utf-8") as fh, open(dst, "w", encoding="utf-8") as w:
        hdr = None
        for l in fh:
            if l.startswith("#") or not l.strip():
                w.write(l); continue
            f = l.rstrip("\n").split("\t")
            if hdr is None:
                hdr = f; w.write(l); continue
            if f[hdr.index(col)] in served:
                n += 1; continue
            w.write(l)
    return n


diffs = []
M = os.path.join(V3, "CELLMAP-descriptive-tables-v2-2026-09-27.tsv")
MC = os.path.join(V3, "CELLMAP-correctness-tables-v3-2026-10-01.tsv")
xM, xMC = os.path.join(out, "x-descriptive-map.tsv"), os.path.join(out, "x-correctness-map.tsv")
print(f"map rows marked: descriptive {mark(M, xM)} · correctness {mark(MC, xMC)}")
ADDT = ["--add-T", os.path.join(REPO, "evidence", "o57-agy-subagent-unmetered-2026-10-13", "addT.tsv")]
EVC = ["--ev", os.path.join(REPO, "evidence", "v3-cost-tables-2026-09-28")]
TABLES = [
    ("descriptive-v2", "tables_v2.py", [], M, xM, "RESULT-descriptive-tables-v2-2026-09-27.md"),
    ("descriptive-v2-O57", "tables_v2.py", ADDT, M, xM, "RESULT-descriptive-tables-v2-O57-remeter-2026-10-13.md"),
    ("cost-v3", "tables_v3.py", EVC, M, xM, "RESULT-cost-tables-v3-2026-09-29.md"),
    ("correctness-v3", "tables_correctness_v3.py", [], MC, xMC, "RESULT-correctness-tables-v3-2026-10-01.md"),
]
for label, tool, extra, old_map, new_map, record in TABLES:
    rcs = []
    for side, mp in (("old", old_map), ("new", new_map)):
        o = os.path.join(out, f"{label}-{side}.md")
        rcs.append(run([PY, tool, "--map", mp] + extra + ["--out", o], os.path.join(out, f"{label}-{side}.log")))
    if table_rows(os.path.join(out, f"{label}-old.md")) != table_rows(os.path.join(V3, record)):
        sys.exit(f"CONTROL FAILED {label}: the OLD run does not reproduce {record}'s table rows")
    print(f"{label}: control OK ({len(table_rows(os.path.join(V3, record)))} table rows = {record}); tool rc old {rcs[0]} new {rcs[1]}")
    diffs.append((label, f"{label}-old.md", f"{label}-new.md"))

# block NA: the lead's prose verifier, in two scratch copies (it reads its cells TSV beside itself)
NA = "RESULT-gemini-blockNA-2026-09-28"
for side in ("old", "new"):
    d = os.path.join(out, f"na-{side}")
    os.makedirs(d, exist_ok=True)
    for f in (f"{NA}-prose-verify.py", f"{NA}.md"):
        shutil.copy(os.path.join(V3, f), d)
    if side == "old":
        shutil.copy(os.path.join(V3, f"{NA}-cells.tsv"), d)
    else:
        print(f"blockNA: cells dropped {drop(os.path.join(V3, f'{NA}-cells.tsv'), os.path.join(d, f'{NA}-cells.tsv'), 'id')}")
    rc = run([PY, "-I", os.path.join(d, f"{NA}-prose-verify.py"), "--print"], os.path.join(out, f"blockNA-{side}.txt"))
    print(f"blockNA {side}: rc {rc}")
diffs.append(("blockNA", "blockNA-old.txt", "blockNA-new.txt"))

# ZF: zf_result.py --print, its own --cells
ZC = os.path.join(REPO, "evidence", "zf-result", "zf-cells.tsv")
xZC = os.path.join(out, "x-zf-cells.tsv")
print(f"ZF: cells dropped {drop(ZC, xZC, 'cid')}")
for side, c in (("old", ZC), ("new", xZC)):
    rc = run([PY, "zf_result.py", "--cells", c, "--print"], os.path.join(out, f"zf-{side}.txt"))
    print(f"ZF {side}: rc {rc}")
chk = subprocess.run([PY, "zf_result.py", "--check", "RESULT-ZF-gemini4-argon-2026-10-25.md"], cwd=V3, capture_output=True, text=True)
if chk.returncode != 0:
    sys.exit("CONTROL FAILED ZF: zf_result.py --check on the RESULT of record is not green")
print("ZF: control OK (zf_result.py --check RESULT-ZF-gemini4-argon-2026-10-25.md green)")
diffs.append(("ZF", "zf-old.txt", "zf-new.txt"))

bad = 0
for label, a, b in diffs:
    mv = os.path.join(out, f"{label}-moved.txt")
    if a.endswith(".md"):
        with open(mv, "w") as fh:
            subprocess.run([PY, "-I", os.path.join(HERE, "recut_diff.py"), os.path.join(out, a), os.path.join(out, b), label],
                           stdout=fh, check=True)
    else:
        with open(mv, "w") as fh:  # line outputs: a unified diff, no context, is the old line beside the new
            r = subprocess.run(["diff", "-U0", os.path.join(out, a), os.path.join(out, b)], capture_output=True, text=True)
            body = [l for l in r.stdout.splitlines(True) if not l.startswith(("---", "+++"))]
            fh.write("".join(body))
            fh.write(f"\n#RECUT {label}: {sum(l.startswith('-') for l in body)} old line(s), {sum(l.startswith('+') for l in body)} new line(s)\n")
    print(open(mv).read().rstrip("\n").splitlines()[-1])
    if "--check" in sys.argv:
        tracked = os.path.join(HERE, f"{label}-moved.txt")
        same = os.path.exists(tracked) and open(tracked).read() == open(mv).read()
        print(f"  --check {label}: {'SAME' if same else 'DIFFERS'} as the tracked {label}-moved.txt")
        bad += 0 if same else 1
sys.exit(1 if bad else 0)
