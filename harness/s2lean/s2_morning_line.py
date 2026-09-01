#!/usr/bin/env python3
r"""s2_morning_line.py — the S2-Lean stage-0 report, computed the ONE pre-declared way (repair round 1: D6 draw,
D8 flagged/leaked, D9 morning line, D10 recall instrument, D16 per-stage cap).
usage: s2_morning_line.py <STATE dir> <k>        (env ML_ARMS=a0,a1,a2 selects the arms; default a0,a1)
       s2_morning_line.py --selftest             drives THIS script's own argv over a synthetic state (amendment 7)
reads: <STATE>/*/manifest.json (substrate S2-Lean/CLEVER, arms in ML_ARMS; SMOKE*/DRY* terminations dropped);
       <STATE>/../logs/s2-landings.log for the driver's SYNTHETIC landings `<none> <task> <stage> <arm> <term> 0`
       (env S2_LANDINGS overrides the path); beside this script: draw.py (IMPORTED — the k drawn, excluded ids already
       removed), flagged.json (flagged_spec_ids, excluded_ids, nl_leaked_ids), view_status.json (c_dead).
       Recall instrument inputs: the scored stage-A body from <STATE>/s2/<task>/<arm>/A.bodies.json when its sha256
       equals the B row's a_bodies_sha256, else <STATE>/<a_episode>/bodies.json; the proof from <STATE>/<ep>/bodies.json;
       the human problem_spec body from views/problem_k/frozen.json (env VIEWS, else <this dir>/views, else
       <STATE>/../s2views).
RULES (stated here, before computing):
 - the SCORED row for (task, stage, arm) is the LATEST by end_utc among rows whose termination base (before '+') is
   DONE|ROUNDS_EXHAUSTED|WALLCLOCK|TOKEN_CEILING; earlier scored rows are SUPERSEDED (labelled, not counted); VOID(…),
   HARNESS_ERROR(…) and every other termination are UNSCORED (listed, not counted).
 - a stage-B row is an ORPHAN when its a_episode is not the episode of the scored stage-A row for (task, arm), or
   there is no scored stage-A row: reported and NOT counted (the (task, B, arm) cell is then NOT PROVEN).
 - proven(task, stage, arm) = scored ∧ not orphan ∧ passed. A drawn problem with no scored row — never landed, unscored
   only, or skipped by a synthetic landing (NOT_PROVEN(no_stage_A_pass), NOT_RUN(view_dead)) — counts NOT PROVEN.
 - F3 = proven(·, B, a0) over the k drawn; draw.py removes the excluded ids BEFORE the first k, so the denominator is
   k (|D|). Beside it: the rate over the unflagged drawn subset U = D ∖ flagged_spec_ids, and the rate without
   nl_leaked_ids. The C line is over the C-eligible drawn subset D ∖ c_dead (view_status.json); c_dead problems are
   reported as their own class NOT_RUN(view_dead). Stage C ALSO prints the REGISTERED POPULATION line over
   UC = U ∖ c_dead (amendment 12): amendment 11's gate is a COUNT over UC, and the printed CE rate is not that
   gate's denominator — the two can point opposite ways on the same run.
 - bands: rate ≥ 80 % ⇒ HOLD (too easy at this tier); rate < 20 % ⇒ HOLD (a floor); 20 % ≤ rate < 80 % ⇒ RUN THE
   SALT ARM. If the all-drawn band and the unflagged band differ ⇒ HOLD (F5, fallback row). F3 is READABLE only when
   every drawn problem has a resolution for (B, a0) — a scored row or a synthetic landing; otherwise the reading is
   printed PROVISIONAL and marked F3 NOT YET READABLE.
 - RECALL INSTRUMENT (D10; computed after the run, never fed back): for every stage-B pass, sim = difflib
   SequenceMatcher ratio between the normalised token sequences (comments stripped, whitespace-insensitive) of the
   agent's generated_spec body and the human problem_spec body (the text after the header's ':='); trivial = the
   stripped proof matches ^(by\s+)?(intro\s+\w+\s*;?\s*)?(exact\s+)?(Iff\.rfl|Iff\.refl\s+_|rfl|fun\s+_\s*=>\s*Iff\.rfl)\s*$;
   recall_suspect = sim ≥ 0.80 OR trivial; f_high = suspect passes / passes (plain arm a0, over passes whose bodies
   are on disk; passes with no bodies on disk are listed as UNKNOWN and excluded from f_high with a warning).
   READING RULE: f_high ≥ 0.5 ⇒ the F3 band is NOT read — RECALL-SUSPECT ⇒ HOLD for council (F5); else the band is read.
 - classes per cell come from check.class (PASS|SCREEN|COMPILE|KERNEL_REJECTED|STATEMENT_ALTERED|AXIOMS_FAIL|TIMEOUT|
   HARNESS|PROVENANCE); KERNEL_REJECTED, STATEMENT_ALTERED and PROVENANCE (stage-B generated_spec != the scored
   stage-A body, AP-4) are printed as their own lines, AXIOMS_FAIL as 'axiom-only failures'.
 - the cap the salt arm consumes is PER STAGE: the a0 p90 of the same stage over DONE|ROUNDS_EXHAUSTED rows (D16).
 - no p-value, by design (b/c/n_d are printed as counts; |b−c| < 5 is labelled INDISTINGUISHABLE).
 - ARMS (amendment 7, 2026-08-31): the scored arm set is ML_ARMS (ordered, comma-separated; default "a0,a1", which
   reproduces the frozen report). a0 must be present and is the primary: F3, the D16 per-stage cap and the recall
   instrument are DEFINED on the plain arm and are not re-pointed by this switch. Every unordered pair of the arm
   set gets its own b/c/n_d line, labelled with the ARM NAMES — the frozen tool hard-wired a0-vs-a1 and, worse,
   captioned a1 "the salt arm", which a1 is not: a1 is the PLACEBO and a2 is the salt arm. Roles are named from
   ARM_ROLE below so the report cannot mislabel them again."""
import collections, difflib, glob, hashlib, json, math, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import draw as drawmod  # noqa: E402

# ---- the scored arm set (amendment 7). Default reproduces the frozen a0/a1 report.
# REFUSE, never coerce: a silently-dropped arm is exactly the defect this repairs — the frozen tool discarded all 30
# a2 rows as "other-arm" and reported a complete-looking a0/a1 table beside them.
ARM_ROLE = {"a0": "plain/control", "a1": "placebo", "a2": "salt"}
def parse_arms(spec):
    arms = [a.strip() for a in str(spec).split(",") if a.strip()]
    for a in arms:
        if not re.match(r"^a[0-9]+$", a):
            sys.exit("REFUSE: ML_ARMS token %r is not an arm name (^a[0-9]+$). Arms are registered in the amendments." % a)
    if len(set(arms)) != len(arms):
        sys.exit("REFUSE: ML_ARMS has a repeated arm: %s" % arms)
    if "a0" not in arms:
        sys.exit("REFUSE: ML_ARMS must contain a0. F3, the D16 per-stage cap and the recall instrument are DEFINED on "
                 "the plain arm a0; scoring without it would print those three under a name that does not mean them.")
    return arms
ARMS = parse_arms(os.environ.get("ML_ARMS") or "a0,a1")
def role(a): return ARM_ROLE.get(a, "role unregistered")

if len(sys.argv) > 1 and sys.argv[1] == "--selftest":
    import selftest_morning_line as _st  # noqa: E402
    sys.exit(_st.main())

st, k = os.path.abspath(sys.argv[1]), int(sys.argv[2])
FL = json.load(open(os.path.join(HERE, "flagged.json")))
VS_PATH = os.path.join(HERE, "view_status.json")
VS = json.load(open(VS_PATH)) if os.path.exists(VS_PATH) else None
CDEAD = set(VS.get("c_dead", [])) if VS else set()
EXC, FLG, NLK = set(FL["excluded_ids"]), set(FL["flagged_spec_ids"]), set(FL.get("nl_leaked_ids", []))
assert sorted(EXC) == sorted(drawmod.EXCLUDED), "flagged.json excluded_ids != draw.EXCLUDED"
pid = drawmod.pid
D = drawmod.draw(k)
assert not any(pid(t) in EXC for t in D)
U = [t for t in D if pid(t) not in FLG]
DNL = [t for t in D if pid(t) not in NLK]
CE = [t for t in D if pid(t) not in CDEAD]
# UC = THE REGISTERED STAGE-C POPULATION (amendment 12, 2026-09-01): the unflagged drawn subset MINUS the
# C-dead. Stage C's printed block is over CE (the C-eligible DRAWN subset) and stage B's F3 line is over U —
# so before this line existed the instrument had an unflagged line for stage B and NONE for stage C, while
# amendment 11's gate is a COUNT over exactly this set. At a plausible outcome the printed rate over CE and
# the gate over UC point OPPOSITE ways (9/22 = 41 % reads "RUN THE SALT ARM"; 9/12 is a CEILING HOLD).
# ⇒ a printed rate whose denominator differs from the gate's is a green light waiting to happen.
UC = [t for t in D if pid(t) not in FLG and pid(t) not in CDEAD]
Dset = set(D)
ids = lambda ts: [pid(t) for t in ts]

# ---- landings (synthetic driver rows) and manifests
LAND = os.environ.get("S2_LANDINGS") or os.path.join(os.path.dirname(st), "logs", "s2-landings.log")
synth = {}
if os.path.exists(LAND):
    for l in open(LAND):
        p = l.split()
        if len(p) >= 5 and p[0] == "<none>": synth[(p[1], p[2], p[3])] = p[4]
SCORED = ("DONE", "ROUNDS_EXHAUSTED", "WALLCLOCK", "TOKEN_CEILING")
def base(t): return str(t or "").split("+")[0]
allm = []
for p in glob.glob(os.path.join(st, "*", "manifest.json")):
    try: allm.append(json.load(open(p)))
    except Exception as e: print("WARNING unreadable manifest %s: %s" % (p, e))
man = [m for m in allm if m.get("substrate") == "S2-Lean/CLEVER" and m.get("arm") in ARMS and not str(m.get("termination", "")).startswith(("SMOKE", "DRY"))]
man.sort(key=lambda m: (m.get("end_utc") or 0, m.get("episode") or ""))
rows = collections.defaultdict(list)
for m in man: rows[(m["instance_id"], m["stage"], m["arm"])].append(m)
scor, superseded, unscored = {}, [], []
for key, ms in rows.items():
    sc = [m for m in ms if base(m["termination"]) in SCORED]
    if sc:
        scor[key] = sc[-1]; superseded += [(m, sc[-1]["episode"]) for m in sc[:-1]]
    unscored += [m for m in ms if base(m["termination"]) not in SCORED]
orphan = {}   # over DRAWN tasks only (rows for undrawn problems are listed separately and never counted)
for (t, s, a), m in scor.items():
    if s != "B" or t not in Dset: continue
    A = scor.get((t, "A", a)); ae = m.get("a_episode")
    if A is None or ae != A.get("episode"): orphan[(t, s, a)] = (ae, A.get("episode") if A else None)
def counted(key): return key in scor and key not in orphan
def proven(key): return counted(key) and bool(scor[key].get("passed"))
def klass(m):
    c = m.get("check") or {}
    if c.get("class"): return c["class"]
    if m.get("passed") or c.get("passed"): return "PASS"
    if not c: return "HARNESS"
    if c.get("compiled") is False: return "COMPILE"
    if c.get("axioms_ok") is False: return "AXIOMS_FAIL"
    return "FAIL"
def status(key):
    if key in orphan: return "ORPHAN(a_episode=%s≠scored A %s)" % orphan[key]
    if key in scor: return "PASS" if scor[key].get("passed") else "FAIL:" + klass(scor[key])
    if key in synth: return "SKIP:" + synth[key]
    if rows.get(key): return "UNSCORED(%s)" % ",".join(base(m["termination"]) for m in rows[key])
    return "NO_LANDING"
def resolved(key): return counted(key) or key in synth
def metered(m): return m.get("metered_sum_governing") or m.get("metered_sum")
def pct(v, q):
    v = sorted(v); return v[min(len(v) - 1, int(math.ceil(q * len(v)) - 1))] if v else None
def band(n, d):
    if not d: return "n/a (empty subset)"
    r = n / d
    return "HOLD (≥80%: too easy at this tier)" if r >= 0.8 else ("HOLD (<20%: a floor, not a reason to add arms)" if r < 0.2 else "RUN THE SALT ARM (20–80%)")
def rate(n, d): return "%d/%d = %s" % (n, d, ("%.1f%%" % (100.0 * n / d)) if d else "n/a")
def grouped(keys):
    g = collections.defaultdict(list)
    for key in keys: g[status(key)].append(pid(key[0]))
    return "  ".join("%s: %s" % (s, v) for s, v in sorted(g.items()))

# ---- recall instrument (D10)
def strip_comments(s):
    s = re.sub(r"/-.*?-/", " ", s or "", flags=re.S); return re.sub(r"--[^\n]*", " ", s)
def toks(s): return re.findall(r"\w[\w'.!?]*|\S", strip_comments(s))
def sim(a, b): return difflib.SequenceMatcher(None, toks(a), toks(b), autojunk=False).ratio()
TRIV = re.compile(r"^(by\s+)?(intro\s+\w+\s*;?\s*)?(exact\s+)?(Iff\.rfl|Iff\.refl\s+_|rfl|fun\s+\w+\s*=>\s*Iff\.rfl)\s*$")
def trivial(p): return bool(TRIV.match(" ".join(strip_comments(p).split())))
def human_body(task):
    for bd in (os.environ.get("VIEWS"), os.path.join(HERE, "views"), os.path.join(os.path.dirname(st), "s2views")):
        p = os.path.join(bd, task, "frozen.json") if bd else None
        if p and os.path.exists(p):
            ps = json.load(open(p))["problem_spec"]; m = re.search(r":=[ \t]*\n", ps)
            return ps[m.end():] if m else ps
    return None
def agent_body(m):
    p = os.path.join(st, "s2", m["instance_id"], m["arm"], "A.bodies.json")
    if os.path.exists(p) and m.get("a_bodies_sha256") and hashlib.sha256(open(p, "rb").read()).hexdigest() == m["a_bodies_sha256"]:
        return json.load(open(p)).get("generated_spec_body")
    ae = m.get("a_episode"); p = os.path.join(st, ae, "bodies.json") if ae else None
    return json.load(open(p)).get("generated_spec_body") if p and os.path.exists(p) else None
def proof_body(m):
    p = os.path.join(st, m["episode"], "bodies.json")
    return json.load(open(p)).get("spec_isomorphism_proof") if os.path.exists(p) else None
def recall(arm):
    out = []
    for t in D:
        key = (t, "B", arm)
        if not proven(key): continue
        m = scor[key]; g, h, pr = agent_body(m), human_body(t), proof_body(m)
        if g is None or h is None or pr is None:
            out.append((t, None, None, None, "UNKNOWN(missing %s)" % ",".join(n for n, v in (("agent_body", g), ("human_body", h), ("proof", pr)) if v is None))); continue
        s, tr = sim(g, h), trivial(pr)
        out.append((t, s, tr, s >= 0.80 or tr, "SUSPECT" if (s >= 0.80 or tr) else "ok"))
    return out

# ---- report
consts = sorted({(m.get("max_turns"), m.get("wall_ceiling_s"), m.get("token_ceiling"), m.get("model_requested"), m.get("effort")) for m in man})
print("S2-LEAN STAGE-0 MORNING LINE  k=%d  drawn |D|=%d (excluded ids %s removed at the draw)  flagged∩D=%d %s  nl_leaked∩D=%s  c_dead∩D=%s (view_status.json %s)" % (
    k, len(D), sorted(EXC), len(D) - len(U), sorted(set(ids(D)) - set(ids(U))), sorted(set(ids(D)) - set(ids(DNL))), sorted(set(ids(D)) - set(ids(CE))), "read" if VS else "ABSENT"))
print("  manifests: %d considered (%d dropped as SMOKE/DRY/other-substrate/other-arm), scored cells %d, superseded %d, unscored %d, orphan B rows %d, synthetic landings %d (%s)  constants=%s  arms=%s" % (
    len(man), len(allm) - len(man), len(scor), len(superseded), len(unscored), len(orphan), len(synth), LAND if os.path.exists(LAND) else "no landings log at " + LAND, consts,
    " ".join("%s(%s)" % (a, role(a)) for a in ARMS)))
for stage, label, dom in (("A", "spec compiles", D), ("B", "ISOMORPHISM PROVEN (the F3 quantity)", D), ("C", "impl + correctness proven (over the C-eligible drawn subset)", CE)):
    for a in ARMS:
        keys = [(t, stage, a) for t in dom]
        ok = [key for key in keys if proven(key)]; cnt = [key for key in keys if counted(key)]; res = [key for key in keys if resolved(key)]
        ms = [metered(scor[key]) for key in cnt if metered(scor[key])]
        cls = collections.Counter(klass(scor[key]) if not scor[key].get("passed") else "PASS" for key in cnt)
        print("  stage %s %s: %s proven %d/%d (counted rows %d, resolved %d)  classes=%s  metered p50=%s p90=%s max=%s  terms=%s" % (
            stage, label, a, len(ok), len(dom), len(cnt), len(res), dict(cls), pct(ms, .5), pct(ms, .9), max(ms) if ms else None,
            dict(collections.Counter(base(scor[key]["termination"]) for key in cnt))))
        print("     proven: %s" % ids([key[0] for key in ok]))
        notp = [key for key in keys if not proven(key)]
        if notp: print("     not proven (%d): %s" % (len(notp), grouped(notp)))
        if stage == "C":
            dead = [(t, "C", a) for t in D if t not in CE]
            if dead: print("     NOT_RUN(view_dead) — not counted (%d): %s" % (len(dead), grouped(dead)))
            okU = [(t, "C", a) for t in UC if proven((t, "C", a))]
            print("     REGISTERED POPULATION UC = U ∖ c_dead (amendment 11's gate is a COUNT over THIS set, not a rate over the %d above)  n=%d ids %s: %s proven %d/%d = %s" % (
                len(CE), len(UC), ids(UC), a, len(okU), len(UC), rate(len(okU), len(UC))))
    for _i in range(len(ARMS)):
        for _j in range(_i + 1, len(ARMS)):
            x, y = ARMS[_i], ARMS[_j]
            b = sum(1 for t in dom if proven((t, stage, x)) and not proven((t, stage, y)))
            c = sum(1 for t in dom if proven((t, stage, y)) and not proven((t, stage, x)))
            print("     pairs over %d: b(%s only)=%d c(%s only)=%d n_d=%d |b-c|=%d %s" % (len(dom), x, b, y, c, b + c, abs(b - c), "INDISTINGUISHABLE (|b-c| < 5)" if abs(b - c) < 5 else "reported as counts; no p-value"))
            if stage == "C":
                bU = sum(1 for t in UC if proven((t, stage, x)) and not proven((t, stage, y)))
                cU = sum(1 for t in UC if proven((t, stage, y)) and not proven((t, stage, x)))
                print("     pairs over the REGISTERED %d: b(%s only)=%d c(%s only)=%d n_d=%d |b-c|=%d %s" % (
                    len(UC), x, bU, y, cU, bU + cU, abs(bU - cU), "INDISTINGUISHABLE (|b-c| < 5)" if abs(bU - cU) < 5 else "reported as counts; no p-value"))
# own classes
def cells(pred): return [(pid(t), s, a) for (t, s, a), m in sorted(scor.items()) if (t, s, a) not in orphan and pred(m)]
print("  KERNEL_REJECTED: %s" % cells(lambda m: klass(m) == "KERNEL_REJECTED" and not m.get("passed")))
print("  STATEMENT_ALTERED: %s" % [(x, (scor[("problem_%d" % x[0], x[1], x[2])].get("check") or {}).get("statement_diffs")) for x in cells(lambda m: klass(m) == "STATEMENT_ALTERED" and not m.get("passed"))])
print("  PROVENANCE (stage-B generated_spec != scored stage-A body, AP-4): %s" % cells(lambda m: klass(m) == "PROVENANCE"))
print("  axiom-only failures (AXIOMS_FAIL: compiled, kernel replay ok, statements identical, axioms outside the allowlist): %s" % [
    (x, (scor[("problem_%d" % x[0], x[1], x[2])].get("check") or {}).get("axioms")) for x in cells(lambda m: klass(m) == "AXIOMS_FAIL" and not m.get("passed"))])
print("  ORPHAN B rows (a_episode ≠ the scored A row; reported, NOT counted): %s" % [(pid(t), a, scor[(t, s, a)]["episode"], "a_episode=%s" % ae, "scored A=%s" % Ae, "a_bodies_sha256=%s" % (scor[(t, s, a)].get("a_bodies_sha256") or "")[:12]) for (t, s, a), (ae, Ae) in sorted(orphan.items())])
print("  superseded rows (not counted): %s" % [(pid(m["instance_id"]), m["stage"], m["arm"], m["episode"], base(m["termination"]), "superseded by " + by) for m, by in superseded])
print("  unscored rows (not counted): %s" % [(pid(m["instance_id"]), m["stage"], m["arm"], m["episode"], m["termination"]) for m in unscored])
nd = sorted({(pid(t), s, a, status((t, s, a))) for (t, s, a) in list(scor) + list(synth) if t not in Dset})
print("  rows for problems NOT in the draw (excluded or beyond k; not counted): %s" % nd)
# F3
p_all = [t for t in D if proven((t, "B", "a0"))]; p_u = [t for t in U if proven((t, "B", "a0"))]; p_nl = [t for t in DNL if proven((t, "B", "a0"))]
b_all, b_u, b_nl = band(len(p_all), len(D)), band(len(p_u), len(U)), band(len(p_nl), len(DNL))
unres = [t for t in D if not resolved((t, "B", "a0"))]
print("  F3 (plain arm a0, stage B, proven over the k=%d drawn): %s ⇒ %s   proven ids: %s" % (len(D), rate(len(p_all), len(D)), b_all, ids(p_all)))
print("     unflagged drawn subset U (n=%d, ids %s): %s ⇒ %s   proven ids: %s" % (len(U), ids(U), rate(len(p_u), len(U)), b_u, ids(p_u)))
print("     without nl_leaked %s (n=%d): %s ⇒ %s" % (sorted(NLK), len(DNL), rate(len(p_nl), len(DNL)), b_nl))
differ = b_all != b_u
print("     bands all-drawn vs unflagged: %s" % ("DIFFER ⇒ HOLD (F5: fallback row)" if differ else "agree"))
print("     resolution (B, a0): %d/%d drawn problems resolved (scored row or synthetic landing)%s" % (len(D) - len(unres), len(D), "" if not unres else "; UNRESOLVED %s ⇒ F3 NOT YET READABLE (PROVISIONAL)" % ids(unres)))
rc = recall("a0"); known = [r for r in rc if r[1] is not None]; sus = [r for r in known if r[3]]
f_high = (len(sus) / len(known)) if known else None
print("  RECALL INSTRUMENT (D10, plain arm, stage-B passes n=%d, with bodies on disk %d): suspect %d (sim≥0.80: %d, trivial proof: %d)  f_high=%s ⇒ %s" % (
    len(rc), len(known), len(sus), sum(1 for r in known if r[1] >= 0.80), sum(1 for r in known if r[2]),
    "n/a" if f_high is None else "%.2f" % f_high,
    "n/a (no passes)" if f_high is None else ("RECALL-SUSPECT ⇒ HOLD for council (F5); the F3 band is NOT read" if f_high >= 0.5 else "below the 0.5 cut; the band is read")))
for t, s, tr, su, lab in rc: print("     %s sim=%s trivial=%s %s" % (t, "n/a" if s is None else "%.3f" % s, tr, lab))
if len(known) < len(rc): print("     WARNING: %d passes have no bodies on disk (excluded from f_high) — resolve before reading" % (len(rc) - len(known)))
for _a in ARMS[1:]:
    rca = recall(_a)
    if rca: print("     (arm %s [%s], for information: passes %d, suspect %d)" % (_a, role(_a), len(rca), sum(1 for r in rca if r[3])))
if f_high is not None and f_high >= 0.5: reading = "RECALL-SUSPECT ⇒ HOLD for council (F5); band not read"
elif differ: reading = "HOLD (F5: all-drawn band %s ≠ unflagged band %s)" % (b_all.split(" ")[0], b_u.split(" ")[0])
else: reading = b_all
print("  READING: %s%s" % ("PROVISIONAL (F3 NOT YET READABLE) — " if unres else "", reading))
caps = {}
for stage in ("A", "B", "C"):
    ms = [metered(m) for (t, s, a), m in scor.items() if s == stage and a == "a0" and (t, s, a) not in orphan and base(m["termination"]) in ("DONE", "ROUNDS_EXHAUSTED") and metered(m)]
    caps[stage] = (pct(ms, .9), len(ms))
print("  p90 the cap rule consumes (D16, per stage, a0 DONE|ROUNDS_EXHAUSTED): %s" % " ".join("%s=%s (n=%d)" % (s, v[0], v[1]) for s, v in caps.items()))
print("  no p-value, by design.")
