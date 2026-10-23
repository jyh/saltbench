#!/usr/bin/env python3
"""o90_pins.py — the O90 stage-1 amendment's pin update to harness/HASHES.txt (desk AEY, 2026-10-23).
WHY NOT hashes.sh: a full regeneration also needs the S2-Rust inputs (VERUS_ROOT, LYNETTE_BIN, BENCH_REPO) and the CLEVER
source, none of which this amendment touches. This tool recomputes ONLY the keys the amendment changes, with hashes.sh's own
formulas (a file's sha256; a rendering = sha256(base + arm) with bytes=), and REFUSES unless every other line is unchanged.
  usage: o90_pins.py [--apply] [--client <version>]   (run from harness/; default prints the diff and changes nothing)
Keys it may touch, and no others: s2lean/episode_s2.sh · s2lean/run_s2_stage0.sh · s2lean/prompt_B_pu.md · s2lean/prompt_C_prior.md
· s2lean/o90_selftest.sh · s2lean/u1_gen.py · s2lean/u2_gen.py · s2lean/smoke_s2.sh · settings.s2.json · s2lean/served_model_check.py · arms/a5.md arms/a6.md arms/a7.md · rendered-s2-a5|a6|a7(__EP__) · rendered-a5|a6|a7(__EP__) · claude-version."""
import hashlib, os, sys
os.chdir(os.path.dirname(os.path.abspath(__file__)) + "/../..")
def sha(p): return hashlib.sha256(open(p, "rb").read()).hexdigest()
def rend(base, arm):
    b = open(base, "rb").read() + open(arm, "rb").read(); return "%s bytes=%d" % (hashlib.sha256(b).hexdigest(), len(b))
client = sys.argv[sys.argv.index("--client") + 1] if "--client" in sys.argv else None
lines = open("HASHES.txt").read().split("\n")
# u1_gen.py is here because #382 merged it into s2lean/ UNPINNED, and episode_s2.sh REFUSES any s2lean/ file that is not
# pinned: every S2-Lean episode synced from main since 10-22 would have refused (measured 2026-10-23 by a census of s2lean/*).
FILES = ["s2lean/episode_s2.sh", "s2lean/run_s2_stage0.sh", "s2lean/prompt_B_pu.md", "s2lean/prompt_C_prior.md", "s2lean/o90_selftest.sh",
         "s2lean/u1_gen.py", "s2lean/u2_gen.py",
         "s2lean/smoke_s2.sh", "settings.s2.json", "s2lean/served_model_check.py"]   # systems' re-read F1: the stage's config dir denied; S3 probes the live CFG
NEW = {f: sha(f) for f in FILES if os.path.exists(f)}
for a in ("a5", "a6", "a7"):
    NEW["arms/%s.md" % a] = sha("arms/%s.md" % a)
    NEW["rendered-s2-%s(__EP__)" % a] = rend("s2lean/base.md", "arms/%s.md" % a)
    NEW["rendered-%s(__EP__)" % a] = rend("base.md", "arms/%s.md" % a)
if client: NEW["claude-version"] = client
# the three arms MUST render byte-identically to a0 in both tables: that is the whole claim of the P+U / U3 arms' CLAUDE.md
for t in ("rendered-s2-%s(__EP__)", "rendered-%s(__EP__)"):
    a0 = [l.split(" ", 1)[1] for l in lines if l.startswith(t % "a0" + " ")]
    assert len(a0) == 1, (t, a0)
    for a in ("a5", "a6", "a7"): assert NEW[t % a] == a0[0], ("%s does not render as a0" % (t % a), NEW[t % a], a0[0])
def key(l): return l.split(" ", 1)[0] if l and not l.startswith("#") else None
out, seen = [], set()
for l in lines:
    k = key(l)
    if k in NEW:
        out.append("%s %s" % (k, NEW[k])); seen.add(k)
    else:
        out.append(l)
    # insert new keys after their nearest sibling (glob order of hashes.sh)
    for after, newk in (("arms/a2.md", "arms/a5.md"), ("arms/a5.md", "arms/a6.md"), ("arms/a6.md", "arms/a7.md"),
                        ("s2lean/prompt_C.md", "s2lean/prompt_B_pu.md"), ("s2lean/prompt_B_pu.md", "s2lean/prompt_C_prior.md"),
                        ("s2lean/run_s2_stage0.sh", "s2lean/o90_selftest.sh"),
                        ("s2lean/selftest_scaffold.py", "s2lean/served_model_check.py"), ("s2lean/served_model_check.py", "s2lean/u1_gen.py"), ("s2lean/u1_gen.py", "s2lean/u2_gen.py"),
                        ("rendered-s2-a2(__EP__)", "rendered-s2-a5(__EP__)"), ("rendered-s2-a5(__EP__)", "rendered-s2-a6(__EP__)"), ("rendered-s2-a6(__EP__)", "rendered-s2-a7(__EP__)"),
                        ("rendered-a2(__EP__)", "rendered-a5(__EP__)"), ("rendered-a5(__EP__)", "rendered-a6(__EP__)"), ("rendered-a6(__EP__)", "rendered-a7(__EP__)")):
        if key(out[-1]) == after and newk in NEW and newk not in seen and not any(key(x) == newk for x in lines):
            out.append("%s %s" % (newk, NEW[newk])); seen.add(newk)
missing = set(NEW) - seen
if missing: sys.exit("REFUSE: no place found for %s" % sorted(missing))
# every line NOT in NEW is byte-identical and in the same order
old_rest = [l for l in lines if key(l) not in NEW]; new_rest = [l for l in out if key(l) not in NEW]
if old_rest != new_rest: sys.exit("REFUSE: a line outside the amendment's keys changed")
keys = [key(l) for l in out if key(l)]
import collections
dup = [k for k, n in collections.Counter((l.split(" ")[0], l.split(" ")[1]) if len(l.split(" ")) >= 3 and not l.split(" ")[1].startswith(("bytes=",)) and l.split(" ")[0] in ("frozen", "frozenA", "view-A", "view-C", "prompt-canonical") else l.split(" ")[0] for l in out if key(l)).items() if n > 1]
if dup: sys.exit("REFUSE: duplicate keys %s" % dup)
changed = [(a, b) for a, b in zip(lines, out) if a != b] if len(lines) == len(out) else None
for k in sorted(NEW):
    was = [l for l in lines if key(l) == k]; print("%-28s %s -> %s" % (k, was[0].split(" ", 1)[1][:16] if was else "(new)", NEW[k][:16]))
if "--apply" in sys.argv:
    open("HASHES.txt", "w").write("\n".join(out)); print("APPLIED: %d keys; %d other lines unchanged" % (len(NEW), len(old_rest)))
else:
    print("DRY: nothing written (%d keys; %d other lines unchanged)" % (len(NEW), len(old_rest)))
