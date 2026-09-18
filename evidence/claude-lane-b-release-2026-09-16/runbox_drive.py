"""runbox_drive.py <export-dir> -- read-only, on the run box: the release export's marker, file count, withheld-shaped
paths and the five brownfield givens' git blob ids; then the EXPORT'S OWN served_models_v3.py check-cell over every HC1
cell under both conditions. Each cell's transcript dir is <its cfg from ctl/run-cfg.tsv>/projects/<key>."""
import glob, hashlib, json, os, re, subprocess, sys, collections
home = os.path.expanduser("~"); exp = sys.argv[1]
def cell_cfg(c):
    # the cell's own CLAUDE_CONFIG_DIR, as its launcher recorded it in ctl/run-cfg.tsv (row `cfg`); never an argument
    for line in open(os.path.join(c, "ctl", "run-cfg.tsv")):
        k, _, v = line.rstrip("\n").partition("\t")
        if k == "cfg": return v
    return None
print("EXPORT marker: %s" % open(os.path.join(exp, "EXPORTED-FROM.sha")).read().strip())
files = [os.path.join(d, f) for d, _, fs in os.walk(exp) for f in fs]
print("EXPORT files: %d" % len(files))
print("EXPORT dirs named withheld|mutants: %d" % sum(1 for d, ds, _ in os.walk(exp) for x in ds if x in ("withheld", "mutants")))
print("EXPORT paths containing 'withheld' or 'mutant' (case-insensitive): %d" % sum(1 for p in files if re.search(r"withheld|mutant", os.path.relpath(p, exp), re.I)))
print("EXPORT refused-file: %s" % ("PRESENT" if os.path.exists(os.path.join(exp, "EXPORT-REFUSED.txt")) else "absent"))
for P in ("Crc32", "FreeList", "LRU", "LZW", "Paxos"):
    f = os.path.join(exp, "tasks", "systems-v3", P, "brownfield", "solution.rs")
    if not os.path.exists(f): print("GIVEN %s MISSING" % P); continue
    b = open(f, "rb").read(); print("GIVEN %s blob %s (%d B)" % (P, hashlib.sha1(b"blob %d\0" % len(b) + b).hexdigest(), len(b)))
tool = os.path.join(exp, "harness", "systems-v3", "served_models_v3.py")
tally = collections.Counter(); n = 0
for c in sorted(glob.glob(os.path.join(home, "cells-hc1-*", "*"))):
    if "." in os.path.basename(c) or not os.path.isdir(os.path.join(c, "ctl")): continue
    n += 1
    slug = os.path.join(cell_cfg(c) or "/nonexistent", "projects", re.sub(r"[^A-Za-z0-9]", "-", os.path.join(c, "repo")))
    row = []
    for cond in ("opus", "sonnet"):
        p = subprocess.run([sys.executable, tool, "check-cell", "--condition", cond, "--slug", slug, "--cell", c, "--json"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        try: j = json.loads(p.stdout); v = "%s/set=%s/rc%d" % (j.get("verdict"), j.get("set_verdict"), p.returncode)
        except ValueError: v = "UNPARSED/rc%d:%s" % (p.returncode, (p.stderr or p.stdout)[:120].replace("\n", " "))
        row.append(v)
    tally[tuple(row)] += 1
    print("CELL %s\topus=%s\tsonnet=%s" % (os.path.relpath(c, home), row[0], row[1]))
print("CELLS %d" % n)
if n == 0: sys.exit("REFUSE: no HC1 cell under %s -- this is not the box the cells ran on" % home)
for k, v in sorted(tally.items()): print("TALLY opus=%s sonnet=%s : %d" % (k[0], k[1], v))
