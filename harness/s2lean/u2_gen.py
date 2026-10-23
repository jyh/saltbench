#!/usr/bin/env python3
r"""u2_gen.py — the O90 U2 use probe: "which of these library facts does this proof use?", keyed by Lean, never
by this script (the O90 test design, the PM's draft 4, §1, U2 row [F2] [G3]).

THE KEY. For one PASSED stage-B artifact (its archived `canonical.lean`: frozen statements + the agent's bodies,
assembled by assemble.py and checked by check.py), Lean elaborates the file again with a read-only probe appended
(PROBE_TAIL below) and prints, for every constant DEFINED IN THE FILE (module index none: the agent's helper
lemmas, `generated_spec`, the frozen `problem_spec`, and every auxiliary the elaborator made for them), the
constants its TYPE and its VALUE mention (`Expr.getUsedConstants`), plus facts about every imported constant those
mention (kind, module, instance, recursor, matcher, deprecated, type hash). This script then:
  CLOSURE  a worklist from the VALUE of `spec_isomorphism` (its proof term) through every constant defined in the
           file it reaches (TYPE and VALUE of each), stopping at imported constants, which are the leaves. So a
           proof split into named lemmas, private or not, reaches the same library facts as one inline term.
  LIBRARY  a leaf counts only if its defining module's root is in LIBRARY_ROOTS (Lean core and the mathlib
           family). The task's own `Imports.*` helper definitions are NOT library (rule NOT-LIBRARY).
  FILTER   the frozen FILTER below, applied to library leaves only (never to the file's own constants, so a
           `private` helper or a `_simp_1` aux lemma is traversed, not dropped). Each drop is counted by the
           first rule that fires.
The used set is what remains. Each member carries `via` (the file constant through which the worklist first
reached it; `spec_isomorphism` = in the proof term itself) and `only_via_problem_spec` (1 = unreachable when the
frozen `problem_spec` and its auxiliaries are leaves, i.e. it comes from the human spec's own definition, which
both arms share).

THE ITEMS. Per artifact and per KIND (theorem; def — opaque counts as def), the used members of that kind are
ordered by sha256(seed|problem|arm|used|name) and cut into chunks of k; each chunk gets m DISTRACTORS taken in
order from the POOL ordered by sha256(seed|problem|arm|pool|name), none reused within the artifact. Options are
presented in sha256(seed|problem|arm|order|item|name) order. The POOL for a kind: imported constants of that kind
whose top-level namespace (first name component; `_root_` for a one-component name) is the namespace of some used
member of that kind, after the SAME FILTER, minus the used set, minus any constant whose type hash equals a used
member's type hash (rule DUP-TYPE: an `alias` states the same fact under another name, and a reader could not be
wrong about it). The question asks "used by this proof", never "needed".

usage:
  u2_gen.py run    --ep EPDIR [EPDIR …] --out DIR [--seed S] [--k 4] [--m 4] [--items-per-kind 2]
                   [--work WDIR]                       # EPDIR holds manifest.json, bodies.json, canonical.lean
  u2_gen.py summary --out DIR                          # re-print the counts from DIR/report.json
  u2_gen.py lean-selftest [--work WDIR]                # Lean fixture arms + their mutants (needs Lean)
  u2_gen.py --selftest                                 # the pure arms + their mutants (no Lean)
env:
  LEANPROJ   lean project for `lake env lean` (default ~/lean-shared/clever)
  SSH_HOST   run Lean and read EPDIR on this host (unset = local)
  REMOTE_DIR scratch dir on SSH_HOST (default bench-dry/u2-2026-10-23/work, relative to ~)
exit: 0 ok · 2 harness error · 3 an artifact REFUSED (not a passed stage-B, sha mismatch, screen hit, Lean error)
LIMITS: see harness/s2lean/u2-2026-10-23/README.md (used is not needed; tactic-made terms count constants the agent
never wrote; type hash catches exact aliases only; the pool is namespace-bounded, not difficulty-matched).
"""
import argparse, hashlib, json, os, random, re, shlex, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
LEANPROJ = os.environ.get('LEANPROJ') or '~/lean-shared/clever'
SSH_HOST = os.environ.get('SSH_HOST') or ''
REMOTE_DIR = os.environ.get('REMOTE_DIR') or 'bench-dry/u2-2026-10-23/work'
ROOT = 'spec_isomorphism'
FROZEN_LOCAL_ROOTS = ('problem_spec',)          # the human spec: same text in both arms (only_via_problem_spec)
ITEM_KINDS = ('theorem', 'def')

# ---------------------------------------------------------------------------------------------------------------
# THE FROZEN FILTER (frozen 2026-10-23, before any O90 artifact exists). Applied to LIBRARY leaves only, and to the
# distractor POOL identically. Rules are tried in this order; a constant is counted under the FIRST that fires.
# ---------------------------------------------------------------------------------------------------------------
LIBRARY_ROOTS = ('Init', 'Std', 'Lean', 'Mathlib', 'Batteries', 'Aesop', 'Qq', 'ProofWidgets', 'Plausible',
                 'ImportGraph', 'LeanSearchClient')
# compiler/elaborator auxiliaries, by LAST name component. `recAux`/`casesAuxOn` are core's custom
# induction/cases eliminators (Nat's): on Lean 4.27 `induction n` elaborates through `Nat.recAux`, a plain def no
# recursor flag marks, so without them a tactic's eliminator would read as a library fact (found by the FxAux
# fixture, 2026-10-23, before any O90 artifact existed).
AUX_LAST = ('rec', 'recOn', 'casesOn', 'below', 'ibelow', 'brecOn', 'binductionOn', 'noConfusion', 'noConfusionType',
            'ctorIdx', 'toCtorIdx', 'ctorElim', 'ctorElimType', 'inj', 'injEq', 'sizeOf_spec', 'mk.inj', 'mk.injEq',
            'recAux', 'casesAuxOn')
EQN_LAST = re.compile(r'^(eq_\d+|eq_def|_unfold|_sunfold|eq_unfold|_eq_\d+)$')
AUXNUM_COMPONENT = re.compile(r'^(match_\d+|proof_\d+)$')
NAME_SUBSTR = ('_private', '._', '_auxLemma')
# tactic CERTIFICATE machinery: lemmas `omega` / `ring` / `norm_num` / `linarith` / `simp` arith emit into a proof
# term, which no author chooses and no reader can name from the source (a proof that says `omega` reaches dozens of
# `Lean.Omega.*`). Counted by its own rule so the reviewer sees exactly what it removes.
TACTIC_PREFIXES = ('Lean.Omega.', 'Mathlib.Tactic.', 'Mathlib.Meta.', 'Lean.Meta.', 'Lean.Elab.', 'Lean.Parser.',
                   'Lean.Grind.', 'Nat.Linear.', 'Nat.SOM.', 'Lean.Simp.', 'Aesop.', 'Qq.', 'Linarith.', 'Mathlib.Linarith.')
# notation, parsers, macros, elaborators, delaborators: declarations of SYNTAX, not facts (`«term∏'_,_»` is a def
# whose type is Lean.ParserDescr). Keyed on the head constant of the type after its binders, which Lean reports.
SYNTAX_TYPEHEADS = ('Lean.ParserDescr', 'Lean.TrailingParserDescr', 'Lean.Parser.Parser', 'Lean.Parser.TrailingParser',
                    'Lean.Macro', 'Lean.Elab.Term.TermElab', 'Lean.Elab.Tactic.Tactic', 'Lean.Elab.Command.CommandElab',
                    'Lean.PrettyPrinter.Delaborator.Delab', 'Lean.PrettyPrinter.Unexpander', 'Lean.Syntax',
                    'Lean.Meta.Simp.Simproc', 'Lean.Meta.Simp.DSimproc', 'Lean.Elab.Term.TermElabM',
                    'Lean.Elab.Tactic.TacticM', 'Lean.Elab.Command.CommandElabM', 'Lean.Meta.MetaM', 'Lean.CoreM')
FILTER = [
    # (rule, what it drops)
    ('NOT-LIBRARY', 'defining module root not in LIBRARY_ROOTS (e.g. the task\'s Imports.* helpers)'),
    ('INSTANCE', 'tagged [instance] (Lean Meta.isInstanceCore)'),
    ('SYNTAX', 'the head of its type is in SYNTAX_TYPEHEADS (notation, parser, macro, elaborator, simproc, meta code)'),
    ('COMPILER-AUX', 'Lean flags it auxiliary recursor / noConfusion / matcher / recursor, or its last component is in AUX_LAST'),
    ('EQN-LEMMA', 'last component matches EQN_LAST (eq_N, eq_def, _unfold, _sunfold, eq_unfold, _eq_N)'),
    ('AUX-NUMBERED', 'a name component matches match_N or proof_N'),
    ('AUX-NAME', 'name contains one of NAME_SUBSTR (_private, ._, _auxLemma)'),
    ('TACTIC-INTERNAL', 'name starts with one of TACTIC_PREFIXES (tactic certificate machinery)'),
    ('DEPRECATED', 'tagged @[deprecated] (Lean Linter.isDeprecated)'),
]
FILTER_RULES = [r for r, _ in FILTER]


def components(name):
    """Lean name components; «…» quoting keeps a dot inside a component."""
    out, cur, q = [], '', False
    for ch in name:
        if ch == '«':
            q = True
        elif ch == '»':
            q = False
        if ch == '.' and not q:
            out.append(cur); cur = ''
        else:
            cur += ch
    out.append(cur)
    return out


def drop_rule(c):
    """c: a library-candidate record (dict from a U2LIB/U2POOL row). Returns the first FILTER rule that fires, or None."""
    if c['module'].split('.')[0] not in LIBRARY_ROOTS:
        return 'NOT-LIBRARY'
    if c['inst']:
        return 'INSTANCE'
    if c.get('typehead') in SYNTAX_TYPEHEADS:
        return 'SYNTAX'
    comps = components(c['name'])
    last2 = '.'.join(comps[-2:])
    if c['auxrec'] or c['noconf'] or c['matcher'] or c['isrec'] or comps[-1] in AUX_LAST or last2 in AUX_LAST:
        return 'COMPILER-AUX'
    if EQN_LAST.match(comps[-1]):
        return 'EQN-LEMMA'
    if any(AUXNUM_COMPONENT.match(x) for x in comps):
        return 'AUX-NUMBERED'
    if any(s in c['name'] for s in NAME_SUBSTR):
        return 'AUX-NAME'
    if c['name'].startswith(TACTIC_PREFIXES):
        return 'TACTIC-INTERNAL'
    if c['depr']:
        return 'DEPRECATED'
    return None


# ---------------------------------------------------------------------------------------------------------------
# THE LEAN PROBE, appended to a copy of the artifact. Read-only: it prints, it defines nothing (one #eval).
# ---------------------------------------------------------------------------------------------------------------
PROBE_TAIL = r'''

-- ===== u2_gen.py probe (appended; not part of the artifact) =====
open Lean Meta in
#eval show MetaM Unit from do
  let env ← getEnv
  let roots : Array Name := #[__ROOTS__]
  let wantPool : Bool := __POOL__
  let fh ← IO.FS.Handle.mk "__OUTFILE__" .write
  let emit (s : String) : IO Unit := fh.putStrLn s
  for r in roots do
    unless (env.find? r).isSome do throwError s!"U2: root {r} not found"
  let modName (n : Name) : String := match env.getModuleIdxFor? n with
    | some i => (env.header.moduleNames[i.toNat]!).toString
    | none => ""
  let kindOf (ci : ConstantInfo) : String := match ci with
    | .thmInfo _ => "theorem" | .defnInfo _ => "def" | .opaqueInfo _ => "def" | .axiomInfo _ => "axiom"
    | .inductInfo _ => "inductive" | .ctorInfo _ => "ctor" | .recInfo _ => "rec" | .quotInfo _ => "quot"
  let nsOf (n : Name) : String := if n.getPrefix.isAnonymous then "_root_" else n.getRoot.toString
  let b (x : Bool) : String := if x then "1" else "0"
  let row (tag : String) (n : Name) (ci : ConstantInfo) : String :=
    String.intercalate "\t" [tag, n.toString, kindOf ci, nsOf n, modName n,
      b (isInstanceCore env n), b (isAuxRecursor env n), b (isNoConfusion env n), b (isMatcherCore env n),
      b (isRecCore env n), b (Linter.isDeprecated env n), toString ci.type.hash,
      (match ci.type.getForallBody.getAppFn with | .const h _ => h.toString | _ => "")]
  emit s!"U2META\t{Lean.versionString}\t{env.header.moduleNames.size}"
  let locals := env.constants.foldStage2 (fun acc n ci => acc.push (n, ci)) (#[] : Array (Name × ConstantInfo))
  let mut libs : Std.HashSet Name := {}
  for (n, ci) in locals do
    let tr := ci.type.getUsedConstants
    let vr := match ci.value? (allowOpaque := true) with
      | some v => v.getUsedConstants
      | none => #[]
    emit ("U2LOCAL\t" ++ (Json.mkObj [("name", toJson n.toString), ("kind", toJson (kindOf ci)),
      ("type_refs", toJson (tr.map (·.toString))), ("value_refs", toJson (vr.map (·.toString)))]).compress)
    for c in tr ++ vr do
      if (env.getModuleIdxFor? c).isSome then libs := libs.insert c
  -- pool namespaces: those of every non-instance theorem/def the file mentions. A SUPERSET of what the draw needs
  -- (the namespaces of the filtered used members), so the Python-side filter and namespace rule stay the only rule.
  let mut nss : Std.HashSet String := {}
  for c in libs.toArray do
    if let some ci := env.find? c then
      emit (row "U2LIB" c ci)
      let k := kindOf ci
      if (k == "theorem" || k == "def") && !(isInstanceCore env c) then nss := nss.insert (nsOf c)
  if wantPool then
    let mut np := 0
    for (n, ci) in env.constants.map₁.toList do
      let k := kindOf ci
      if (k == "theorem" || k == "def") && nss.contains (nsOf n) then
        emit (row "U2POOL" n ci)
        np := np + 1
    emit s!"U2POOLN\t{np}"
  emit "U2END"
  fh.flush
  IO.println "U2DONE"
'''

LIB_FIELDS = ('name', 'kind', 'ns', 'module', 'inst', 'auxrec', 'noconf', 'matcher', 'isrec', 'depr', 'typehash', 'typehead')


def probe_tail(roots, pool, outfile):
    return (PROBE_TAIL.replace('__ROOTS__', ', '.join('`' + r for r in roots)).replace('__POOL__', 'true' if pool else 'false')
            .replace('__OUTFILE__', outfile))


def parse_probe(out):
    """Lean stdout -> {'meta', 'locals': {name: {kind, refs}}, 'lib': {name: rec}, 'pool': [rec], 'pool_n', 'end'}"""
    res = {'meta': None, 'locals': {}, 'lib': {}, 'pool': [], 'pool_n': None, 'end': False}
    for line in out.splitlines():
        if line.startswith('U2LOCAL\t'):
            j = json.loads(line.split('\t', 1)[1])
            res['locals'][j['name']] = {'kind': j['kind'], 'type_refs': j['type_refs'], 'value_refs': j['value_refs']}
        elif line.startswith('U2LIB\t') or line.startswith('U2POOL\t'):
            f = line.split('\t')
            rec = dict(zip(LIB_FIELDS, f[1:]))
            for k in ('inst', 'auxrec', 'noconf', 'matcher', 'isrec', 'depr'):
                rec[k] = rec[k] == '1'
            (res['lib'].__setitem__(rec['name'], rec) if f[0] == 'U2LIB' else res['pool'].append(rec))
        elif line.startswith('U2META\t'):
            res['meta'] = line.split('\t')[1:]
        elif line.startswith('U2POOLN\t'):
            res['pool_n'] = int(line.split('\t')[1])
        elif line == 'U2END':
            res['end'] = True
    return res


# ---------------------------------------------------------------------------------------------------------------
# CLOSURE and USED SET (pure; the mutants in MUT replace pieces of it in the self-tests)
# ---------------------------------------------------------------------------------------------------------------
MUT = set()   # names of active mutants; empty in production


def closure(locals_, root, leaf_locals=()):
    """worklist from root's VALUE through file constants (TYPE + VALUE). Returns {imported name: via}, ordered."""
    found, seen = {}, {root}
    work = [(root, c) for c in locals_[root]['value_refs']]
    while work:
        via, c = work.pop(0)
        if c in locals_:
            if c in seen:
                continue
            seen.add(c)
            if 'M-SKIP-LOCALS' in MUT:                  # mutant: do not traverse the file's own constants
                continue
            if 'M-FILTER-LOCALS' in MUT and any(s in c for s in NAME_SUBSTR):   # mutant: filter before closure
                continue
            if c in leaf_locals or any(c.startswith(x + '.') for x in leaf_locals):
                continue
            work.extend((c, d) for d in locals_[c]['type_refs'] + locals_[c]['value_refs'])
        elif c not in found:
            found[c] = via
    return found


def used_set(probe, root=ROOT):
    """-> (used: [rec + via + only_via_problem_spec], drops: [(name, kind, rule)], raw: {name: via})"""
    raw = closure(probe['locals'], root)
    shared = closure(probe['locals'], root, FROZEN_LOCAL_ROOTS)
    used, drops = [], []
    for n, via in raw.items():
        rec = probe['lib'].get(n)
        if rec is None:
            raise SystemExit(f'harness: {n} referenced but not described by the probe')
        rule = None if 'M-NO-FILTER' in MUT else drop_rule(rec)
        if rule:
            drops.append((n, rec['kind'], rule))
        else:
            used.append(dict(rec, via=via, only_via_problem_spec=int(n not in shared)))
    return used, drops, raw


# ---------------------------------------------------------------------------------------------------------------
# THE SEEDED DRAW (pure)
# ---------------------------------------------------------------------------------------------------------------
def h(seed, problem, arm, tag, name):
    return hashlib.sha256(f'{seed}|{problem}|{arm}|{tag}|{name}'.encode()).hexdigest()


def mod2(c):
    return '.'.join(c['module'].split('.')[:2])


def draw(used, pool, seed, problem, arm, k=4, m=4, per_kind=2):
    """-> (items: [dict], pool_report: {kind: {candidates, dropped-by-rule, dup_type, in_used, eligible}})"""
    items, rep = [], {}
    usednames = {u['name'] for u in used}
    for kind in ITEM_KINDS:
        U = [u for u in used if u['kind'] == kind]
        if not U:
            continue
        nss = {u['ns'] for u in U}
        hashes = {u['typehash'] for u in U}
        r = {'candidates': 0, 'dropped': {}, 'dup_type': 0, 'in_used': 0, 'eligible': 0}
        elig = []
        for c in pool:
            if c['kind'] != kind or c['ns'] not in nss:
                continue
            r['candidates'] += 1
            if c['name'] in usednames and 'M-DRAW-NO-EXCLUDE' not in MUT:
                r['in_used'] += 1; continue
            rule = drop_rule(c)
            if rule:
                r['dropped'][rule] = r['dropped'].get(rule, 0) + 1; continue
            if c['typehash'] in hashes and 'M-DRAW-NO-DUPTYPE' not in MUT:
                r['dup_type'] += 1; continue
            elig.append(c)
        r['eligible'] = len(elig)
        rep[kind] = r
        if 'M-DRAW-UNSEEDED' in MUT:
            U = random.sample(U, len(U)); elig = random.sample(elig, len(elig))
        else:
            U = sorted(U, key=lambda u: h(seed, problem, arm, 'used', u['name']))
            elig = sorted(elig, key=lambda c: h(seed, problem, arm, 'pool', c['name']))
        # MATCHED distractors: distractor j is matched to used member j mod k of its item (its ANCHOR) — the first
        # untaken eligible constant, in pool-hash order, with the anchor's namespace AND module family (first two
        # module components, e.g. Init.Data · Mathlib.Algebra); failing that, the anchor's namespace alone; failing
        # that (an anchor alone in its namespace, e.g. HAdd.hAdd), any eligible pool member of the kind ('pool'). The
        # level is recorded per distractor. An item that cannot get m distractors is not made.
        taken = set()
        for i in range(per_kind):
            chunk = U[i * k:(i + 1) * k]
            if not chunk:
                break
            dis = []
            for j in range(m):
                a_ = chunk[j % len(chunk)]
                levels = [('ns', lambda c: c['ns'] == a_['ns']), ('pool', lambda c: True)]
                if 'M-DRAW-NO-MODMATCH' not in MUT:
                    levels.insert(0, ('ns+module2', lambda c: c['ns'] == a_['ns'] and mod2(c) == mod2(a_)))
                pick = next(((c, lv) for lv, pred in levels for c in elig if c['name'] not in taken and pred(c)), None)
                if pick is None:
                    break
                taken.add(pick[0]['name'])
                dis.append(dict(pick[0], match=pick[1], anchor=a_['name']))
            if len(dis) < m:
                break
            iid = f'p{problem}-{arm}-{kind}-{i}'
            opts = [(c['name'], 'used', c) for c in chunk] + [(c['name'], 'not-used', c) for c in dis]
            opts.sort(key=lambda o: h(seed, problem, arm, 'order:' + iid, o[0]))
            items.append({'item': iid, 'problem': problem, 'arm': arm, 'kind': kind, 'k': len(chunk), 'm': len(dis),
                          'options': [{'name': n, 'key': key, 'module': c['module'], 'via': c.get('via', '-'),
                                       'match': c.get('match', '-'), 'anchor': c.get('anchor', '-')}
                                      for n, key, c in opts]})
    return items, rep


# ---------------------------------------------------------------------------------------------------------------
# LEAN I/O
# ---------------------------------------------------------------------------------------------------------------
def sh(cmd, **kw):
    return subprocess.run(cmd, capture_output=True, text=True, **kw)


def qpath(path):
    """shell-quote a remote path, keeping a leading ~/ expandable"""
    return '"$HOME"/' + shlex.quote(path[2:]) if path.startswith('~/') else shlex.quote(path)


def fetch(path):
    """bytes of a file on SSH_HOST (or local)"""
    if SSH_HOST:
        r = subprocess.run(['ssh', SSH_HOST, 'cat ' + qpath(path)], capture_output=True)
        if r.returncode:
            raise FileNotFoundError(f'{SSH_HOST}:{path}: {r.stderr.decode().strip()}')
        return r.stdout
    return open(os.path.expanduser(path), 'rb').read()


def probe_path(tag, workdir):
    """where the probe writes: a path on the host that runs Lean (absolute, no ~)"""
    if SSH_HOST:
        home = sh(['ssh', SSH_HOST, 'printf %s "$HOME"']).stdout.strip()
        if not home:
            raise SystemExit(f'harness: cannot read $HOME on {SSH_HOST}')
        return f'{home}/{REMOTE_DIR}/{tag}.probe'
    return os.path.abspath(os.path.join(workdir, tag + '.probe'))


def run_lean(src, tag, workdir, timeout=1800, probe=None):
    """-> (rc, lean output, probe file text or '')"""
    local = os.path.join(workdir, tag + '.lean')
    open(local, 'w').write(src)
    if SSH_HOST:
        remote = f'{REMOTE_DIR}/{tag}.lean'
        r = sh(['ssh', SSH_HOST, 'mkdir -p ' + shlex.quote(REMOTE_DIR)])
        if r.returncode:
            raise SystemExit(f'harness: mkdir on {SSH_HOST}: {r.stderr.strip()}')
        r = sh(['scp', '-q', local, f'{SSH_HOST}:{remote}'])
        if r.returncode:
            raise SystemExit(f'harness: scp: {r.stderr.strip()}')
        cmd = f'cd {LEANPROJ} && bash -lc ' + shlex.quote(f'lake env lean ~/{remote}')
        r = sh(['ssh', SSH_HOST, cmd], timeout=timeout)
    else:
        r = sh(['bash', '-lc', f'cd {LEANPROJ} && lake env lean {shlex.quote(local)}'], timeout=timeout)
    out = r.stdout + r.stderr
    open(os.path.join(workdir, tag + '.out'), 'w').write(out)
    ptext = ''
    if probe:
        if SSH_HOST:
            r2 = sh(['scp', '-q', f'{SSH_HOST}:{probe}', os.path.join(workdir, tag + '.probe')])
            ptext = open(os.path.join(workdir, tag + '.probe')).read() if r2.returncode == 0 else ''
        elif os.path.exists(probe):
            ptext = open(probe).read()
    return r.returncode, out, ptext


def lean_errors(out, tag):
    return re.findall(rf'{re.escape(tag)}\.lean:(\d+):\d+: error[^\n]*', out)


def leanproj_manifest_sha():
    try:
        return hashlib.sha256(fetch(LEANPROJ + '/lake-manifest.json')).hexdigest()
    except FileNotFoundError:
        return None


# ---------------------------------------------------------------------------------------------------------------
# RUN
# ---------------------------------------------------------------------------------------------------------------
def load_episode(ep, workdir):
    """-> (meta dict, canonical source) or raises Refused"""
    tag = os.path.basename(ep.rstrip('/'))
    man = json.loads(fetch(f'{ep}/manifest.json'))
    meta = {'episode': tag, 'stage': man.get('stage'), 'arm': man.get('arm'), 'passed': man.get('passed'),
            'problem': str(man.get('instance_id', '')).replace('problem_', ''),
            'run_leanproj_manifest_sha256': (man.get('leanproj_sha') or {}).get('manifest')}
    if meta['stage'] != 'B' or meta['passed'] is not True:
        raise Refused(f'not a passed stage-B episode (stage {meta["stage"]}, passed {meta["passed"]})')
    src_b = fetch(f'{ep}/canonical.lean')
    want = (man.get('check') or {}).get('canonical_sha256')
    try:
        want = json.loads(fetch(f'{ep}/check.json')).get('canonical_sha256') or want
    except FileNotFoundError:
        pass
    got = hashlib.sha256(src_b).hexdigest()
    meta['canonical_sha256'] = got
    if want and want != got:
        raise Refused(f'canonical.lean sha256 {got[:12]} != check.json canonical_sha256 {want[:12]}')
    if not want:
        raise Refused('no canonical_sha256 recorded for this episode; refusing an unpinned artifact')
    sys.path.insert(0, HERE)
    import screen as scr
    bodies = json.loads(fetch(f'{ep}/bodies.json'))
    hits = scr.screen_bodies(bodies)
    if hits:
        raise Refused(f'screen.py flags the bodies: {hits}')   # never elaborate agent meta-code outside the fence
    return meta, src_b.decode('utf-8')


class Refused(Exception):
    pass


def run(eps, out, seed, k, m, per_kind, workdir):
    os.makedirs(out, exist_ok=True)
    os.makedirs(workdir, exist_ok=True)
    proj_sha = leanproj_manifest_sha()
    report = {'seed': seed, 'k': k, 'm': m, 'items_per_kind': per_kind, 'filter': FILTER, 'library_roots': LIBRARY_ROOTS,
              'leanproj_manifest_sha256_now': proj_sha, 'artifacts': [], 'refused': []}
    used_rows, drop_rows, item_rows = [], [], []
    for ep in eps:
        try:
            meta, src = load_episode(ep, workdir)
        except Refused as e:
            report['refused'].append({'episode': ep, 'why': str(e)}); print(f'REFUSED {ep}: {e}'); continue
        tag = f'u2-{meta["episode"]}'
        pp = probe_path(tag, workdir)
        rc, o, ptext = run_lean(src.rstrip('\n') + '\n' + probe_tail([ROOT], True, pp), tag, workdir, probe=pp)
        errs = lean_errors(o, tag)
        pr = parse_probe(ptext)
        if rc or errs or not pr['end']:
            why = f'Lean rc {rc}, {len(errs)} error lines, end marker {pr["end"]}: {errs[:3]}'
            report['refused'].append({'episode': ep, 'why': why}); print(f'REFUSED {ep}: {why}'); continue
        if pr['pool_n'] != len(pr['pool']):
            raise SystemExit(f'harness: pool rows {len(pr["pool"])} != announced {pr["pool_n"]} (truncated output?)')
        used, drops, raw = used_set(pr)
        items, poolrep = draw(used, pr['pool'], seed, meta['problem'], meta['arm'], k, m, per_kind)
        by_rule = {}
        for _, _, r_ in drops:
            by_rule[r_] = by_rule.get(r_, 0) + 1
        a = dict(meta, lean=pr['meta'], probe_sha256=hashlib.sha256(ptext.encode()).hexdigest(),
                 pool_rows=len(pr['pool']),
                 file_constants=len(pr['locals']), reached_imported=len(raw), dropped=len(drops),
                 dropped_by_rule=by_rule, used=len(used),
                 used_by_kind={kk: sum(u['kind'] == kk for u in used) for kk in sorted({u['kind'] for u in used})},
                 used_only_via_problem_spec=sum(u['only_via_problem_spec'] for u in used),
                 used_direct_in_proof_term=sum(u['via'] == ROOT for u in used),
                 pool=poolrep, items=len(items))
        report['artifacts'].append(a)
        for u in sorted(used, key=lambda u: (u['kind'], u['name'])):
            used_rows.append([meta['episode'], meta['problem'], meta['arm'], u['name'], u['kind'], u['module'], u['via'],
                              u['only_via_problem_spec']])
        for n, kd, r_ in sorted(drops, key=lambda d: (d[2], d[0])):
            drop_rows.append([meta['episode'], meta['problem'], meta['arm'], n, kd, r_])
        for it in items:
            for pos, op in enumerate(it['options']):
                item_rows.append([it['item'], meta['episode'], it['problem'], it['arm'], it['kind'], it['k'], it['m'], pos,
                                  op['name'], op['key'], op['module'], op['via'], op['match'], op['anchor']])
        print(f'{meta["episode"]} problem_{meta["problem"]} {meta["arm"]}: reached {len(raw)} imported · dropped '
              f'{len(drops)} {by_rule} · used {len(used)} {a["used_by_kind"]} · items {len(items)}')
    w = lambda name, hdr, rows: open(os.path.join(out, name), 'w').write(
        '\t'.join(hdr) + '\n' + ''.join('\t'.join(map(str, r_)) + '\n' for r_ in rows))
    w('used.tsv', ['episode', 'problem', 'arm', 'name', 'kind', 'module', 'via', 'only_via_problem_spec'], used_rows)
    w('drops.tsv', ['episode', 'problem', 'arm', 'name', 'kind', 'rule'], drop_rows)
    w('items.tsv', ['item', 'episode', 'problem', 'arm', 'kind', 'k', 'm', 'position', 'option', 'key', 'module', 'via',
                    'match', 'anchor'],
      item_rows)
    json.dump(report, open(os.path.join(out, 'report.json'), 'w'), indent=1, sort_keys=True)
    summary(report)
    return 3 if report['refused'] else 0


def summary(report):
    for a in report['artifacts']:
        print(f'SUMMARY {a["episode"]} p{a["problem"]} {a["arm"]}: used {a["used"]} {a["used_by_kind"]} '
              f'(direct {a["used_direct_in_proof_term"]}, only via problem_spec {a["used_only_via_problem_spec"]}) · '
              f'dropped {a["dropped"]} · items {a["items"]}')
    print(f'TOTAL: {len(report["artifacts"])} artifacts · used {sum(a["used"] for a in report["artifacts"])} · '
          f'items {sum(a["items"] for a in report["artifacts"])} · refused {len(report["refused"])}')


# ---------------------------------------------------------------------------------------------------------------
# SELF-TESTS. Every arm is run clean, then under each mutant that should turn it red.
# ---------------------------------------------------------------------------------------------------------------
def lib(name, kind='theorem', module='Mathlib.X', **fl):
    rec = {'name': name, 'kind': kind, 'ns': components(name)[0] if len(components(name)) > 1 else '_root_',
           'module': module, 'typehash': fl.pop('typehash', 'h:' + name), 'typehead': fl.pop('typehead', '')}
    for f in ('inst', 'auxrec', 'noconf', 'matcher', 'isrec', 'depr'):
        rec[f] = fl.pop(f, False)
    return rec


def synthetic():
    L = lambda vr, tr=(): {'kind': 'theorem', 'type_refs': list(tr), 'value_refs': list(vr)}
    locals_ = {
        'spec_isomorphism': L(['congrArg', 'helper', '_private.F.0.phelper', 'problem_spec']),
        'helper': L(['List.append_nil']),
        '_private.F.0.phelper': L(['List.length_cons'], ['instHAdd']),
        'problem_spec': {'kind': 'def', 'type_refs': [], 'value_refs': ['List.foldl', 'Imports.fib', 'problem_spec.match_1']},
        'problem_spec.match_1': {'kind': 'def', 'type_refs': [], 'value_refs': ['List.casesOn']},
        'unreached': L(['Nat.succ_le']),
    }
    libs = [lib('congrArg', module='Init.Prelude'), lib('List.append_nil', module='Init.Data.List'),
            lib('List.length_cons', module='Init.Data.List'), lib('instHAdd', 'def', 'Init.Prelude', inst=True),
            lib('List.foldl', 'def', 'Init.Prelude'), lib('Imports.fib', 'def', 'Imports.AllImports'),
            lib('List.casesOn', 'def', 'Init.Prelude', auxrec=True), lib('Nat.succ_le')]
    return {'locals': locals_, 'lib': {r['name']: r for r in libs}, 'pool': [], 'pool_n': 0, 'end': True}


def pure_arms():
    """-> [(arm name, ok)]"""
    arms = []
    def check(name, ok):
        arms.append((name, bool(ok)))
    P = synthetic()
    used, drops, raw = used_set(P)
    names = {u['name'] for u in used}
    check('closure: a lemma reached through a public helper (List.append_nil)', 'List.append_nil' in names)
    check('closure: a lemma reached through a PRIVATE helper (List.length_cons)', 'List.length_cons' in names)
    check('closure: an unreached file constant contributes nothing (Nat.succ_le)', 'Nat.succ_le' not in raw)
    dr = {n: r_ for n, _, r_ in drops}
    check('filter: an instance reached is dropped as INSTANCE', dr.get('instHAdd') == 'INSTANCE')
    check('filter: a task helper is dropped as NOT-LIBRARY', dr.get('Imports.fib') == 'NOT-LIBRARY')
    check('filter: a casesOn reached through a file matcher is dropped as COMPILER-AUX', dr.get('List.casesOn') == 'COMPILER-AUX')
    check('filter: no used name fires a FILTER rule (non-vacuous: holds with no drops too)',
          all(drop_rule(u) is None for u in used))
    via = {u['name']: u for u in used}
    check('only_via_problem_spec: List.foldl comes only from problem_spec', via.get('List.foldl', {}).get('only_via_problem_spec') == 1)
    check('only_via_problem_spec: congrArg is in the proof term itself', via.get('congrArg', {}).get('only_via_problem_spec') == 0
          and via['congrArg']['via'] == ROOT)
    cases = {'eq_self': None, 'proof_irrel': None, 'List.foo.eq_1': 'EQN-LEMMA', 'List.foo.eq_def': 'EQN-LEMMA',
             'Nat.add._sunfold': 'EQN-LEMMA', 'List.map.match_1': 'AUX-NUMBERED', 'Nat.foo.proof_2': 'AUX-NUMBERED',
             '_private.Init.X.0.foo': 'AUX-NAME', 'Foo._simp_1': 'AUX-NAME', 'Foo._auxLemma.3': 'AUX-NAME',
             'Nat.rec': 'COMPILER-AUX', 'Nat.recAux': 'COMPILER-AUX', 'List.below': 'COMPILER-AUX', 'Prod.mk.injEq': 'COMPILER-AUX',
             'Nat.noConfusion': 'COMPILER-AUX', 'Lean.Omega.LinearCombo.add_eval': 'TACTIC-INTERNAL',
             'Mathlib.Tactic.Ring.add_pf_add_zero': 'TACTIC-INTERNAL', 'Lean.Name': None}
    for n, want in cases.items():
        check(f'filter: {n} -> {want}', drop_rule(lib(n)) == want)
    check('filter: a notation def (type head Lean.ParserDescr) -> SYNTAX',
          drop_rule(lib("«term∏'_,_»", 'def', typehead='Lean.ParserDescr')) == 'SYNTAX')
    check('filter: a deprecated alias -> DEPRECATED', drop_rule(lib('Foo.old', depr=True)) == 'DEPRECATED')
    check('filter: a matcher flagged by Lean -> COMPILER-AUX', drop_rule(lib('Foo.weird', matcher=True)) == 'COMPILER-AUX')
    # the draw
    used = [lib(f'List.u{i}') for i in range(9)] + [lib(f'Nat.d{i}', 'def') for i in range(3)]
    # SMALL on purpose: 6 eligible List theorems, so every eligible distractor IS drawn and a planted in-used or alias
    # entry that slips a guard must appear (a 40-member pool hid both mutants: they were simply never picked)
    pool = [lib(f'List.p{i}') for i in range(6)] + [lib(f'Nat.q{i}', 'def') for i in range(10)] + \
           [lib(f'Set.x{i}') for i in range(5)] + [lib('List.u0')] + [lib('List.alias', typehash='h:List.u3')] + \
           [lib('List.p0.eq_1'), lib('List.instFoo', inst=True)]
    d1 = draw(used, pool, 's', '7', 'a0'); d2 = draw(used, pool, 's', '7', 'a0'); d3 = draw(used, pool, 't', '7', 'a0')
    check('draw: same seed gives byte-identical items', json.dumps(d1, sort_keys=True) == json.dumps(d2, sort_keys=True))
    check('draw: another seed moves it', json.dumps(d1[0], sort_keys=True) != json.dumps(d3[0], sort_keys=True))
    un = {u['name'] for u in used}
    opts = [o for it in d1[0] for o in it['options']]
    check('draw: every distractor is outside the used set', all(o['name'] not in un for o in opts if o['key'] == 'not-used'))
    check('draw: every key option is in the used set', all(o['name'] in un for o in opts if o['key'] == 'used'))
    kinds = {u['name']: u['kind'] for u in used + pool}
    check('draw: options share their item kind', all(kinds[o['name']] == it['kind'] for it in d1[0] for o in it['options']))
    check('draw: distractors only from used namespaces (no Set.*)', not any(o['name'].startswith('Set.') for o in opts))
    check('draw: an exact alias (same type hash) is never a distractor', 'List.alias' not in {o['name'] for o in opts})
    check('draw: filtered pool members never drawn', not ({'List.p0.eq_1', 'List.instFoo'} & {o['name'] for o in opts}))
    dis = [o['name'] for o in opts if o['key'] == 'not-used']
    check('draw: no distractor reused within an artifact', len(dis) == len(set(dis)))
    check('draw: 1 theorem item of 4+4 (6 eligible < 8: no short distractor item), 1 def item of 3+4 (short used chunk)',
          [(it['kind'], it['k'], it['m']) for it in d1[0]] == [('theorem', 4, 4), ('def', 3, 4)])
    check('draw: report counts the alias and the in-used duplicate',
          d1[1]['theorem']['dup_type'] == 1 and d1[1]['theorem']['in_used'] == 1)
    # module-family matching: 2 Init + 2 Mathlib anchors, 10 + 10 pool members of each family
    mu = [lib(f'List.a{i}', module=['Init.Data.List.Basic', 'Mathlib.Data.List.Basic'][i % 2]) for i in range(4)]
    mp = [lib(f'List.b{i}', module=['Init.Data.List.Lemmas', 'Mathlib.Data.List.Defs'][i % 2]) for i in range(20)]
    dm = draw(mu, mp, 's', '7', 'a0', per_kind=1)[0]
    dd = [o for it in dm for o in it['options'] if o['key'] == 'not-used']
    fam = {c['name']: mod2(c) for c in mu + mp}
    check('draw: matched distractors share their anchor\'s module family when the pool has one',
          len(dd) == 4 and all(o['match'] == 'ns+module2' and fam[o['name']] == fam[o['anchor']] for o in dd))
    return arms


MUTANTS = {   # mutant -> the arms (by name prefix) that must go red under it
    'M-SKIP-LOCALS': ['closure: a lemma reached through a public helper', 'closure: a lemma reached through a PRIVATE'],
    'M-FILTER-LOCALS': ['closure: a lemma reached through a PRIVATE'],
    'M-NO-FILTER': ['filter: an instance reached', 'filter: no used name fires'],
    # the in-used exclusion alone is MASKED at the output by DUP-TYPE (a used constant in the pool carries its own
    # type hash), so its mutant shows only in the report counts; both guards off must break disjointness itself
    'M-DRAW-NO-EXCLUDE': ['draw: report counts'],
    'M-DRAW-NO-EXCLUDE+M-DRAW-NO-DUPTYPE': ['draw: every distractor is outside'],
    'M-DRAW-NO-DUPTYPE': ['draw: an exact alias'],
    'M-DRAW-UNSEEDED': ['draw: same seed gives byte-identical'],
    'M-DRAW-NO-MODMATCH': ['draw: matched distractors'],
}


def run_with_mutants(arms_fn, mutants, label):
    fails = 0
    base = arms_fn()
    for name, ok in base:
        print(('PASS ' if ok else 'FAIL ') + name); fails += not ok
    for mu, must in mutants.items():
        MUT.clear(); MUT.update(mu.split('+'))
        try:
            res = dict(arms_fn())
        except SystemExit as e:
            res = {}; print(f'  ({mu} raised {e})')
        finally:
            MUT.clear()
        red = [a for a in res if not res[a]]
        hit = all(any(r_.startswith(p) for r_ in red) for p in must) if res else True
        print(f'MUTANT {mu}: {"RED" if hit else "NOT RED"} ({len(red)} arms failed: {red})')
        fails += not hit
    print(f'{label}', 'FAIL' if fails else 'OK', f'({len(base)} arms, {len(mutants)} mutants, {fails} failed)')
    return 1 if fails else 0


FIXTURE = r'''import Imports.AllImports

namespace FxDirect
def generated_spec (xs : List Nat) : Prop := (xs ++ []).length = xs.length
theorem spec_isomorphism : ∀ xs : List Nat, generated_spec xs :=
  fun xs => congrArg List.length (List.append_nil xs)
end FxDirect

namespace FxVia
def generated_spec (xs : List Nat) : Prop := (xs ++ []).length = xs.length
theorem helper (xs : List Nat) : xs ++ [] = xs := List.append_nil xs
theorem spec_isomorphism : ∀ xs : List Nat, generated_spec xs :=
  fun xs => congrArg List.length (helper xs)
end FxVia

namespace FxPriv
def generated_spec (xs : List Nat) : Prop := (xs ++ []).length = xs.length
private theorem helper (xs : List Nat) : xs ++ [] = xs := List.append_nil xs
theorem spec_isomorphism : ∀ xs : List Nat, generated_spec xs :=
  fun xs => congrArg List.length (helper xs)
end FxPriv

namespace FxAux
theorem zero_add' (n : Nat) : 0 + n = n := by
  induction n with
  | zero => rfl
  | succ k ih => rw [Nat.add_succ, ih]
theorem spec_isomorphism : ∀ n : Nat, 0 + n = n := fun n => zero_add' n
end FxAux
'''
FX_ROOTS = ['FxDirect.spec_isomorphism', 'FxVia.spec_isomorphism', 'FxPriv.spec_isomorphism', 'FxAux.spec_isomorphism']


def lean_arms_from(pr):
    """the Lean fixture arms, over one parsed probe of FIXTURE. Expected sets are DERIVED from the Direct fixture's
    own proof term (Lean's getUsedConstants), never typed."""
    arms = []
    def check(name, ok):
        arms.append((name, bool(ok)))
    direct_term = {c for c in pr['locals']['FxDirect.spec_isomorphism']['value_refs'] if c in pr['lib']}
    expect = {c for c in direct_term if pr['lib'][c]['kind'] == 'theorem' and drop_rule(pr['lib'][c]) is None}
    check(f'derive: the Direct fixture\'s proof term names library theorems ({sorted(expect)})', len(expect) >= 2)
    for fx in ('FxVia', 'FxPriv'):
        root = fx + '.spec_isomorphism'
        own = set(pr['locals'][root]['value_refs'])
        hidden = expect - own
        check(f'non-vacuous: {fx}\'s own proof term lacks {sorted(hidden)}', len(hidden) >= 1)
        u = {x['name'] for x in used_set(pr, root)[0]}
        check(f'transitivity: {fx} reports every theorem Direct reports', expect <= u)
    u_aux, d_aux, raw_aux = used_set(pr, 'FxAux.spec_isomorphism')
    rules = {r_ for _, _, r_ in d_aux}
    check(f'filter live: the induction fixture reaches an INSTANCE and a COMPILER-AUX ({sorted(rules)})',
          {'INSTANCE', 'COMPILER-AUX'} <= rules)
    check('filter live: no used name fires a FILTER rule', all(drop_rule(x) is None for x in u_aux))
    check('filter live: no used name is a Lean-flagged instance/recursor/matcher',
          not any(x['inst'] or x['auxrec'] or x['isrec'] or x['matcher'] or x['noconf'] for x in u_aux))
    check('private: FxPriv\'s helper is a _private file constant', any(n.startswith('_private.') and n.endswith('FxPriv.helper')
                                                                     for n in pr['locals']))
    return arms


def lean_selftest(workdir):
    os.makedirs(workdir, exist_ok=True)
    tag = 'u2-fixture'
    pp = probe_path(tag, workdir)
    rc, o, ptext = run_lean(FIXTURE + probe_tail(FX_ROOTS, False, pp), tag, workdir, probe=pp)
    errs = lean_errors(o, tag)
    pr = parse_probe(ptext)
    print(f'LEAN fixture: rc {rc} · errors {len(errs)} · end {pr["end"]} · file constants {len(pr["locals"])} · '
          f'imported described {len(pr["lib"])} · lean {pr["meta"]}')
    if rc or errs or not pr['end']:
        print(o[-3000:]); print('LEAN-SELFTEST FAIL (fixture did not elaborate)'); return 1
    return run_with_mutants(lambda: lean_arms_from(pr),
                            {'M-SKIP-LOCALS': ['transitivity: FxVia', 'transitivity: FxPriv'],
                             'M-FILTER-LOCALS': ['transitivity: FxPriv'],
                             'M-NO-FILTER': ['filter live: no used name fires', 'filter live: no used name is']},
                            'LEAN-SELFTEST')


def main():
    if sys.argv[1:] == ['--selftest']:
        sys.exit(run_with_mutants(pure_arms, MUTANTS, 'SELFTEST'))
    ap = argparse.ArgumentParser()
    ap.add_argument('mode', choices=['run', 'summary', 'lean-selftest'])
    ap.add_argument('--ep', nargs='+')
    ap.add_argument('--seed', default='o90-u2-2026-10-23')
    ap.add_argument('--k', type=int, default=4)
    ap.add_argument('--m', type=int, default=4)
    ap.add_argument('--items-per-kind', type=int, default=2)
    ap.add_argument('--out')
    ap.add_argument('--work')
    a = ap.parse_args()
    if a.mode == 'lean-selftest':
        sys.exit(lean_selftest(a.work or tempfile.mkdtemp(prefix='u2-selftest-')))
    if not a.out:
        ap.error('--out is required')
    if a.mode == 'summary':
        summary(json.load(open(os.path.join(a.out, 'report.json'))))
        return
    if not a.ep:
        ap.error('--ep is required for run')
    sys.exit(run(a.ep, a.out, a.seed, a.k, a.m, a.items_per_kind, a.work or os.path.join(a.out, 'work')))


if __name__ == '__main__':
    main()
