#!/bin/bash
# views_selftest.sh — the VIEWS SELF-TEST (repair D7): compile every stage-A view (A.lean, sorry body), every stage-B
# PRISTINE file (frozen statements only, sorry bodies — generated_spec body `sorry`, isomorphism proof `by sorry`) and
# every stage-C view (C.lean, sorry bodies) under `lake env lean` in the pinned CLEVER project, and write
# view_status.json = {"problem_k": {"A": ok|error, "B": ok|error, "C": ok|error, "first_error": str}, "c_dead": [ids]}.
# Verdict rule (pre-stated): A and B are ok iff rc == 0. C is ok iff EVERY `error:` in its log is the sorry-evaluation
# abort of a `#test` line ("aborting evaluation since the expression depends on the 'sorry' axiom") — that error is the
# placeholder's, not the view's; any other error is a view that is dead BEFORE any agent text ⇒ c_dead. first_error is
# the first non-placeholder error line (empty when none). Run FROM THE SEAT (never the Studio): ~161×3 compiles,
# ~4–8 s each, -j parallel. Seat-side gate before `stage_views.sh ship`.
#   usage: views_selftest.sh <views dir> <clever src/lean4> <out view_status.json> [-j N] [--work DIR]
#   env: PATH must reach `lake` (the script prepends $HOME/.elan/bin). Never runs lake build/update/exe cache/elan.
set -u
V="${1:?views dir}"; PROJ="${2:?clever src/lean4}"; OUT="${3:?out view_status.json}"; shift 3
J=8; WORK=""
while [ $# -gt 0 ]; do case "$1" in -j) J="$2"; shift 2 ;; --work) WORK="$2"; shift 2 ;; *) echo "unknown arg $1" >&2; exit 2 ;; esac; done
[ -n "$WORK" ] || WORK="$(mktemp -d "${TMPDIR:-/tmp}/views_selftest.XXXXXX")"
export PATH="$HOME/.elan/bin:$PATH"
[ -f "$PROJ/lakefile.lean" ] || { echo "REFUSE: $PROJ is not a lake project" >&2; exit 3; }
[ -e "$PROJ/.lake/build/lib/lean/Imports/AllImports.olean" ] || { echo "REFUSE: Imports.AllImports is not built in $PROJ (never built here; build it yourself)" >&2; exit 3; }
mkdir -p "$WORK/src" "$WORK/log"
echo "views_selftest: views=$V proj=$PROJ out=$OUT work=$WORK j=$J toolchain=$(cat "$PROJ/lean-toolchain")"

# 1. write the sweep sources: A = A.lean verbatim, C = C.lean verbatim, B = the §1 pristine layout from frozen.json
python3 - "$V" "$WORK/src" <<'PY' || exit 4
import json, os, sys
V, W = sys.argv[1], sys.argv[2]
dirs = sorted((d for d in os.listdir(V) if d.startswith("problem_")), key=lambda d: int(d.split("_")[1]))
assert len(dirs) == 161, "expected 161 problem_* views, found %d" % len(dirs)
n = 0
for d in dirs:
    p = os.path.join(V, d); fz = json.load(open(os.path.join(p, "frozen.json")))
    pre = fz.get("preamble") or ""
    hdr = "import Imports.AllImports\n" + (pre + "\n" if pre else "") + "\n/--\n%s\n-/\n" % fz["nl"]
    for st, body in (("A", open(os.path.join(p, "A.lean")).read()), ("C", open(os.path.join(p, "C.lean")).read())):
        assert body.startswith(hdr), "%s %s does not start with the frozen header (preamble mismatch?)" % (d, st)
        open(os.path.join(W, "%s_%s.lean" % (d, st)), "w").write(body)
    # stage-B PRISTINE: frozen statements, sorry bodies, no agent text (assemble.py --pristine B emits the same layout)
    B = hdr + "\n%s\nsorry\n\n%s\n\n%s\nby sorry\n" % (fz["generated_spec_header"], fz["problem_spec"], fz["isomorphism_theorem"])
    open(os.path.join(W, "%s_B.lean" % d), "w").write(B); n += 1
print("sources written:", n * 3)
PY

# 2. compile, J-way parallel, each in the lake project's env; log + rc per file
ls "$WORK/src"/*.lean | sort > "$WORK/files.txt"
cat > "$WORK/one.sh" <<EOF
#!/bin/bash
f="\$1"; b="\$(basename "\$f" .lean)"; cd "$PROJ" || exit 9
t0=\$(date +%s); lake env lean "\$f" > "$WORK/log/\$b.log" 2>&1; rc=\$?; echo "\$rc \$((\$(date +%s)-t0))" > "$WORK/log/\$b.rc"
echo "\$b rc=\$rc \$((\$(date +%s)-t0))s"
EOF
chmod +x "$WORK/one.sh"
t0=$(date +%s)
xargs -P "$J" -n 1 "$WORK/one.sh" < "$WORK/files.txt" > "$WORK/compile.log" 2>&1
echo "compiled $(wc -l < "$WORK/files.txt" | tr -d ' ') files in $(( $(date +%s) - t0 )) s (j=$J)"

# 3. classify and write view_status.json
python3 - "$WORK" "$OUT" <<'PY' || exit 5
import json, os, re, sys
W, OUT = sys.argv[1], sys.argv[2]
ABORT = "aborting evaluation since the expression depends on the 'sorry' axiom"
ERR = re.compile(r"^(.*?\.lean):(\d+):(\d+): error(\(.*?\))?: (.*)$")
ids = sorted({int(f.split("_")[1]) for f in os.listdir(os.path.join(W, "src")) if f.endswith(".lean")})
status, dead = {}, {"A": [], "B": [], "C": []}
for i in ids:
    row = {}
    first_error = ""
    for st in ("A", "B", "C"):
        b = "problem_%d_%s" % (i, st)
        rcp = os.path.join(W, "log", b + ".rc")
        if not os.path.exists(rcp):
            row[st] = "error"; first_error = first_error or "%s: no rc file (compile did not run)" % st; dead[st].append(i); continue
        rc = int(open(rcp).read().split()[0])
        log = open(os.path.join(W, "log", b + ".log"), errors="replace").read().splitlines()
        errs = [l for l in log if ERR.match(l)]
        real = [l for l in errs if ABORT not in l]
        if st == "C": ok = not real
        else: ok = rc == 0 and not real
        row[st] = "ok" if ok else "error"
        if not ok:
            dead[st].append(i)
            fe = real[0] if real else (errs[0] if errs else "rc=%d (no error line; see log)" % rc)
            fe = re.sub(r"^.*?problem_\d+_[ABC]\.lean:", "%s:" % st, fe)
            first_error = first_error or fe
    row["first_error"] = first_error
    status["problem_%d" % i] = row
status["c_dead"] = dead["C"]
json.dump(status, open(OUT, "w"), indent=1); open(OUT, "a").write("\n")
print("A ok %d/%d  B ok %d/%d  C ok %d/%d" % (len(ids) - len(dead["A"]), len(ids), len(ids) - len(dead["B"]), len(ids), len(ids) - len(dead["C"]), len(ids)))
print("A dead:", dead["A"]); print("B dead:", dead["B"]); print("C dead (%d):" % len(dead["C"]), dead["C"])
for i in dead["C"]: print("  C %d: %s" % (i, status["problem_%d" % i]["first_error"][:160]))
for st in ("A", "B"):
    for i in dead[st]: print("  %s %d: %s" % (st, i, status["problem_%d" % i]["first_error"][:160]))
REF = [39, 44, 54, 62, 65, 77, 81, 87, 97, 110, 111, 112, 113, 119, 153, 155, 157, 160]   # the refuters' sweep at 86f9e04
print("refuters' C-dead list agreement: %s  (derived-only: %s, refuters-only: %s)" % (dead["C"] == REF, sorted(set(dead["C"]) - set(REF)), sorted(set(REF) - set(dead["C"]))))
print("wrote", OUT)
PY
