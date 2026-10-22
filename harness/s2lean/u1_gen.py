#!/usr/bin/env python3
r"""u1_gen.py — the O90 U1 membership generator: seeded (input, output) pairs over a CLEVER problem's
`problem_spec`, keyed yes/no by Lean, never by this script (the O90 test design, the PM's draft 4,
blob 61ebab1d7a58, §1, U1 row).

THE QUESTION AN ITEM ASKS. For a concrete input x and output y: does y satisfy the task's specification at x?
The proposition keyed is `problem_spec (fun _ … => y) x`, the human spec with the implementation fixed to the
constant y. Every CLEVER `problem_spec` ends `∃ result, impl x = result ∧ spec result`, so that proposition is
"spec holds of y at x".

WHERE THE PAIRS COME FROM, frozen before any artifact exists (the design's rule: generators, never items):
  INPUTS   the frozen view's own `#test` inputs, then per argument type its boundary values and SEEDED random
           values (`--seed`, mixed with the problem id). Types reached: Int · Nat · Rat · Bool · String ·
           List T · T × U. A signature outside that grammar is UNREACHED and reported, never guessed.
  OUTPUTS  REF problems (CLEVER's reference `implementation` is not `sorry`): the reference's value at each input,
           evaluated by Lean, and one mechanical perturbation of it. NOREF problems: each `#test` line's expected
           value and its perturbation (no reference exists to evaluate at a generated input).
  PERTURB  Int/Nat/Rat +1 · Bool not · String ++ "a" · List: drop the head, or [default] for [] ·
           T × U: perturb the first component. A perturbation whose repr equals its source is dropped
           (PERTURB-NOOP) and counted.

THE RULE THAT DROPS A PROBLEM. A spec that uses its function binder anywhere but the final
`∃ result, f x = result` calls the implementation on OTHER inputs (`result = 1 + impl tail`). Fixed to a constant,
such a spec asks `y = 1 + y`, or makes a clause vacuous: wrong in BOTH directions, so the problem is DROPPED
(SPEC-RECURSIVE) and counted, never keyed. Measured on U15: 146 · 142 · 112. The polarity control below saw two
of the three (146, 142 rejected their own tests); it could NOT see 112, whose recursion made the check vacuous.

THE KEY. Lean proves the proposition or its negation, trying a FROZEN ladder of tactics in order; the first rung
that proves either side keys the item:
  R0  by simp [problem_spec]                          KERNEL
  R1  by simp [problem_spec]; decide +kernel          KERNEL
  R2  by unfold problem_spec; decide +kernel          KERNEL
  RC  by simp [problem_spec]; native_decide           COMPILED (the design's "#eval of a Decidable instance";
                                                      it trusts the compiler, and the item says so)
An item no rung decides is DROPPED (UNDECIDED) and counted per problem. Both sides proved would be an
inconsistency; the script refuses (rc 4) rather than pick one.

usage:
  u1_gen.py plan   --ids 0 73 … [--seed S] [--n-random N] --out DIR     # writes eval files, no Lean
  u1_gen.py run    --ids 0 73 … [--seed S] [--n-random N] --out DIR     # plan + Lean + key → DIR/items.tsv
  u1_gen.py summary --out DIR                                            # re-print the counts from DIR/items.tsv
  u1_gen.py draw   [--seed S] --out DIR                                  # leg (a) draw → DIR/drawn.tsv (KERNEL only, <= 8/problem)
  u1_gen.py --selftest
env:
  VIEWS      frozen views dir (default <this dir>/views)
  CLEVER_GT  CLEVER checkout, src/lean4/human_eval (default ~/clever-gt/src/lean4/human_eval, read over SSH_HOST)
  LEANPROJ   lean project for `lake env lean` (default ~/lean-shared/clever)
  SSH_HOST   run Lean and read CLEVER_GT on this host (unset = local)
exit: 0 ok · 2 harness error · 3 a problem UNREACHED · 4 a both-sides proof (refused)
LIMITS: the key is the human spec's, so a spec that disagrees with its own tests (problem_18, amendment 11) keys
the spec, not the tests. Output balance (yes/no) is whatever the spec makes it and is reported, not tuned. NOREF
problems carry only test inputs. COMPILED keys trust the Lean compiler.
"""
import argparse, json, os, random, re, shlex, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
VIEWS = os.environ.get('VIEWS') or os.path.join(HERE, 'views')
CLEVER_GT = os.environ.get('CLEVER_GT') or '~/clever-gt/src/lean4/human_eval'
LEANPROJ = os.environ.get('LEANPROJ') or '~/lean-shared/clever'
SSH_HOST = os.environ.get('SSH_HOST') or ''

LADDER = [('R0', 'by simp [problem_spec]', 'KERNEL'),
          ('R1', 'by simp [problem_spec]; decide +kernel', 'KERNEL'),
          ('R2', 'by unfold problem_spec; decide +kernel', 'KERNEL'),
          ('RC', 'by simp [problem_spec]; native_decide', 'COMPILED')]

PRELUDE = '''
class U1Perturb (α : Type) where p : α → α
instance : U1Perturb Int := ⟨(· + 1)⟩
instance : U1Perturb Nat := ⟨(· + 1)⟩
instance : U1Perturb Rat := ⟨(· + 1)⟩
instance : U1Perturb Bool := ⟨not⟩
instance : U1Perturb String := ⟨(· ++ "a")⟩
instance {α : Type} [Inhabited α] : U1Perturb (List α) := ⟨fun l => match l with | [] => [default] | _ :: t => t⟩
instance {α β : Type} [U1Perturb α] : U1Perturb (α × β) := ⟨fun (a, b) => (U1Perturb.p a, b)⟩
'''


class Unreached(Exception):
    pass


class SpecRecursive(Exception):
    """A dropped-by-rule problem: counted and reported, never an error."""


# ---------- the type grammar ----------
def parse_type(s):
    s = s.strip()
    while s.startswith('(') and s.endswith(')') and _balanced(s[1:-1]):
        s = s[1:-1].strip()
    depth = 0
    for i, ch in enumerate(s):
        depth += ch in '([' ; depth -= ch in ')]'
        if ch == '×' and depth == 0:
            return ('Prod', parse_type(s[:i]), parse_type(s[i + 1:]))
    if s.startswith('List '):
        return ('List', parse_type(s[5:]))
    if s in ('Int', 'Nat', 'Rat', 'Bool', 'String'):
        return (s,)
    raise Unreached('type ' + s)


def _balanced(s):
    d = 0
    for ch in s:
        d += ch == '(' ; d -= ch == ')'
        if d < 0:
            return False
    return d == 0


def lean_type(t):
    if t[0] == 'List':
        return 'List ' + _paren(lean_type(t[1]))
    if t[0] == 'Prod':
        return _paren(lean_type(t[1])) + ' × ' + _paren(lean_type(t[2]))
    return t[0]


def _paren(s):
    return '(' + s + ')' if ' ' in s else s


def parse_signature(sig):
    """`def implementation (a: T) (b c: U) : R :=` -> ([(name, type)], R)"""
    m = re.match(r'\s*def\s+implementation\s*(.*?)\s*:\s*([^:]+?)\s*:=\s*$', sig.strip(), re.S)
    if not m:
        raise Unreached('signature ' + sig.strip())
    args = []
    for grp in re.findall(r'\(([^()]*(?:\([^()]*\)[^()]*)*)\)', m.group(1)):
        names, typ = grp.split(':', 1)
        for n in names.split():
            args.append((n, parse_type(typ)))
    return args, parse_type(m.group(2))


def spec_binder_uses(spec):
    """(binder name, uses in the spec outside comments). 2 = the binder and the final `∃ result, f x = result`."""
    body = re.sub(r'--[^\n]*', '', spec)
    m = re.search(r'def problem_spec\s*\(\s*(\w+)\s*:', body)
    if not m:
        raise Unreached('problem_spec binder')
    return m.group(1), len(re.findall(rf'\b{m.group(1)}\b', body))


# ---------- values, rendered as Lean source ----------
BOUND = {'Int': ['0', '1', '-1', '2'], 'Nat': ['0', '1', '2', '3'], 'Rat': ['0', '1', '-1', '1/2'],
         'Bool': ['false', 'true', 'false', 'true'], 'String': ['""', '"a"', '"ab"', '"Ab b"']}
ALPHA = 'abAB .'


def boundary(t, k):
    if t[0] in BOUND:
        return BOUND[t[0]][k % 4]
    if t[0] == 'List':
        return '[' + ', '.join(boundary(t[1], j) for j in range(k % 4)) + ']'
    return '(' + boundary(t[1], k) + ', ' + boundary(t[2], k) + ')'


def rand_val(t, r):
    if t[0] == 'Int':
        return str(r.randint(-9, 9))
    if t[0] == 'Nat':
        return str(r.randint(0, 20))
    if t[0] == 'Rat':
        return f'{r.randint(-9, 9)}/{r.randint(1, 4)}'
    if t[0] == 'Bool':
        return r.choice(['true', 'false'])
    if t[0] == 'String':
        return json.dumps(''.join(r.choice(ALPHA) for _ in range(r.randint(0, 5))))
    if t[0] == 'List':
        return '[' + ', '.join(rand_val(t[1], r) for _ in range(r.randint(0, 4))) + ']'
    return '(' + rand_val(t[1], r) + ', ' + rand_val(t[2], r) + ')'


def typed(v, t):
    return f'(({v}) : {lean_type(t)})'


def parse_tests(text):
    """frozen `#test implementation ARGS = EXPECTED` lines -> [(ARGS, EXPECTED)]; `==` as CLEVER writes it once."""
    out = []
    for line in text.splitlines():
        m = re.match(r'\s*#test\s+implementation\s+(.*?)\s+==?\s+(.*?)\s*$', line)
        if m:
            out.append((m.group(1), m.group(2)))
    return out


# ---------- files ----------
def read_ref(pid):
    path = f'{CLEVER_GT}/problem_{pid}.lean'
    if SSH_HOST:
        r = subprocess.run(['ssh', SSH_HOST, 'cat ' + path], capture_output=True, text=True)
        if r.returncode:
            raise SystemExit(f'harness: cannot read {path} on {SSH_HOST}: {r.stderr.strip()}')
        text = r.stdout
    else:
        text = open(os.path.expanduser(path)).read()
    sec = {}
    for name in ('implementation_signature', 'implementation'):
        m = re.search(rf'-- start_def {name}\n(.*?)-- end_def {name}\n', text, re.S)
        sec[name] = m.group(1) if m else ''
    body = sec['implementation'].strip()
    return None if body in ('', 'sorry') else sec['implementation_signature'] + sec['implementation']


def plan(pid, seed, n_random):
    j = json.load(open(os.path.join(VIEWS, f'problem_{pid}', 'frozen.json')))
    name, uses = spec_binder_uses(j['problem_spec'])
    if uses != 2:
        raise SpecRecursive(f'`{name}` is used {uses} times (2 = binder + final application): the spec calls the '
                            'implementation on other inputs, so fixing it to a constant does not ask membership')
    args, rtype = parse_signature(j['implementation_signature'])
    ref = read_ref(pid)
    tests = parse_tests(j['test_cases'])
    inputs = [('test', a) for a, _ in tests]
    if ref:
        r = random.Random(f'{seed}:{pid}')
        for k in range(4):
            inputs.append(('boundary', ' '.join(typed(boundary(t, k), t) for _, t in args)))
        for _ in range(n_random):
            inputs.append(('random', ' '.join(typed(rand_val(t, r), t) for _, t in args)))
    seen, uniq = set(), []
    for src, a in inputs:
        if a not in seen:
            seen.add(a); uniq.append((src, a))
    rt = lean_type(rtype)
    lines = ['import Imports.AllImports', PRELUDE]
    if ref:
        lines.append(ref)
    evals = []
    for k, (src, a) in enumerate(uniq):
        if ref:
            base = f'(implementation {a})'
        else:
            base = f'(({dict(tests)[a]}) : {rt})'
        evals.append((k, src, a))
        lines.append(f'#eval IO.println ("U1OUT {k} " ++ reprStr ({base} : {rt}))')
        lines.append(f'#eval IO.println ("U1PRT {k} " ++ reprStr (U1Perturb.p ({base} : {rt})))')
    return {'pid': pid, 'args': args, 'rtype': rt, 'ref': bool(ref), 'spec': j['problem_spec'],
            'evals': evals, 'eval_src': '\n'.join(lines) + '\n'}


def run_lean(src, tag, workdir):
    local = os.path.join(workdir, tag + '.lean')
    open(local, 'w').write(src)
    if SSH_HOST:
        remote = f'bench-dry/u1/{tag}.lean'
        subprocess.run(['ssh', SSH_HOST, 'mkdir -p bench-dry/u1'], check=True, capture_output=True)
        subprocess.run(['scp', '-q', local, f'{SSH_HOST}:{remote}'], check=True)
        cmd = f'cd {LEANPROJ} && bash -lc ' + shlex.quote(f'lake env lean ~/{remote}')
        r = subprocess.run(['ssh', SSH_HOST, cmd], capture_output=True, text=True, timeout=3600)
    else:
        r = subprocess.run(['bash', '-lc', f'cd {LEANPROJ} && lake env lean {shlex.quote(local)}'],
                           capture_output=True, text=True, timeout=3600)
    out = r.stdout + r.stderr
    open(os.path.join(workdir, tag + '.out'), 'w').write(out)
    return r.returncode, out


def error_lines(out, tag):
    return set(int(m) for m in re.findall(rf'{re.escape(tag)}\.lean:(\d+):\d+: error', out))


def key_items(p, items, workdir):
    """items: [(item_id, prop)] -> {item_id: (key, rung, trust)}"""
    keyed, todo = {}, list(items)
    for rung, tac, trust in LADDER:
        if not todo:
            break
        tag = f'u1-p{p["pid"]}-{rung}'
        lines = ['import Imports.AllImports', *p['spec'].split('\n'), '']
        where = {}
        for iid, prop in todo:
            for side, stmt in (('yes', prop), ('no', f'¬ ({prop})')):
                assert '\n' not in stmt, iid
                lines.append(f'theorem u1_{iid.replace("-", "_")}_{side} : {stmt} := {tac}')
                where[len(lines)] = (iid, side)
        rc, out = run_lean('\n'.join(lines) + '\n', tag, workdir)
        bad = error_lines(out, tag)
        if re.search(r'error: unexpected token|error: unknown (identifier|constant) .problem_spec', out):
            raise SystemExit(f'harness: {tag} does not parse; see {tag}.out (a parse error is never a key)')
        if rc and not bad:
            raise SystemExit(f'harness: {tag} failed with no per-line error (rc {rc}); see {tag}.out')
        proved = {}
        for ln, (iid, side) in where.items():
            if ln not in bad:
                proved.setdefault(iid, []).append(side)
        nxt = []
        for iid, prop in todo:
            s = proved.get(iid, [])
            if len(s) == 2:
                print(f'REFUSED: both sides of {iid} proved at {rung}', file=sys.stderr)
                sys.exit(4)
            if s:
                keyed[iid] = (s[0], rung, trust)
            else:
                nxt.append((iid, prop))
        todo = nxt
    for iid, _ in todo:
        keyed[iid] = ('DROPPED', 'UNDECIDED', '-')
    return keyed


def run(ids, seed, n_random, out):
    os.makedirs(out, exist_ok=True)
    rows, unreached = [], []
    for pid in ids:
        try:
            p = plan(pid, seed, n_random)
        except Unreached as e:
            unreached.append((pid, str(e)))
            continue
        except SpecRecursive as e:
            rows.append([pid, f'p{pid}-*', '-', '-', '-', '-', 'DROPPED', 'SPEC-RECURSIVE', '-'])
            print(f'DROPPED problem_{pid}: SPEC-RECURSIVE: {e}')
            continue
        tag = f'u1-p{pid}-eval'
        rc, o = run_lean(p['eval_src'], tag, out)
        vals = {}
        for m in re.finditer(r'^U1(OUT|PRT) (\d+) (.*)$', o, re.M):
            vals[(m.group(1), int(m.group(2)))] = m.group(3)
        bad = error_lines(o, tag)
        items, meta = [], {}
        lam = 'fun ' + ' '.join('_' for _ in p['args']) + ' => '
        for k, src, a in p['evals']:
            out_v, prt_v = vals.get(('OUT', k)), vals.get(('PRT', k))
            if out_v is None:
                rows.append([pid, f'p{pid}-{k}-out', src, 'ref' if p['ref'] else 'test', a, '-', 'DROPPED', 'NO-VALUE', '-'])
                continue
            for which, v in (('ref' if p['ref'] else 'test', out_v), ('perturb', prt_v)):
                iid = f'p{pid}-{k}-{which}'
                if which == 'perturb' and (v is None or v == out_v):
                    rows.append([pid, iid, src, which, a, v or '-', 'DROPPED', 'PERTURB-NOOP', '-'])
                    continue
                meta[iid] = (src, which, a, v)
                items.append((iid, f'problem_spec ({lam}(({v}) : {p["rtype"]})) {a}'))
        keyed = key_items(p, items, out)
        for iid, (src, which, a, v) in meta.items():
            k_, rung, trust = keyed[iid]
            rows.append([pid, iid, src, which, a, v, k_, rung, trust])
    with open(os.path.join(out, 'items.tsv'), 'w') as f:
        f.write('\t'.join(['problem', 'item', 'input_source', 'output_source', 'input', 'output', 'key', 'rung', 'trust']) + '\n')
        for r_ in rows:
            f.write('\t'.join(map(str, r_)) + '\n')
    for pid, why in unreached:
        print(f'UNREACHED problem_{pid}: {why}')
    summary(rows)
    return 3 if unreached else 0


def summary(rows):
    by = {}
    for r_ in rows:
        d = by.setdefault(r_[0], {'yes': 0, 'no': 0, 'DROPPED': 0})
        d[r_[6]] = d.get(r_[6], 0) + 1
    for pid, d in by.items():
        print(f'problem_{pid}: yes {d["yes"]} · no {d["no"]} · dropped {d["DROPPED"]}')
    t = {k: sum(d[k] for d in by.values()) for k in ('yes', 'no', 'DROPPED')}
    print(f'TOTAL: yes {t["yes"]} · no {t["no"]} · dropped {t["DROPPED"]} over {len(by)} problems')
    # THE POLARITY CONTROL: a NOREF item pairs a #test input with that test's own expected value, so it must key
    # yes unless the spec contradicts its own tests (problem_18's class, amendment 11). A swapped yes/no reads
    # here first. REF test rows are not in it: the reference's value need not equal the test's expected value.
    ctl = [r_ for r_ in rows if r_[2] == 'test' and r_[3] == 'test' and r_[6] != 'DROPPED']
    off = sorted({r_[0] for r_ in ctl if r_[6] != 'yes'})
    print(f'POLARITY CONTROL: {sum(r_[6] == "yes" for r_ in ctl)} of {len(ctl)} keyed NOREF test pairs read yes; '
          f'problems with a no: {off or "none"} (each is a spec that rejects its own test, or a defect here)')


def draw(rows, seed, cap=8):
    """The leg (a) draw (the PM's ruling F2/F3): per problem, KERNEL-keyed items only, a seeded shuffle, up to cap//2
    yes and cap//2 no, then filled to cap from the larger side. Returns rows with a stratum column appended:
    test-input (a frozen #test input) or generated-input (boundary or random)."""
    out = []
    for pid in sorted({r_[0] for r_ in rows}, key=int):
        pool = sorted((r_ for r_ in rows if r_[0] == pid and r_[8] == 'KERNEL' and r_[6] in ('yes', 'no')),
                      key=lambda r_: r_[1])
        r = random.Random(f'{seed}:draw:{pid}')
        r.shuffle(pool)
        yes = [r_ for r_ in pool if r_[6] == 'yes']; no = [r_ for r_ in pool if r_[6] == 'no']
        half = cap // 2
        take = yes[:half] + no[:half]
        rest = yes[half:] + no[half:]
        take += rest[:max(0, cap - len(take))]
        for r_ in sorted(take, key=lambda r_: r_[1]):
            out.append(list(r_) + ['test-input' if r_[2] == 'test' else 'generated-input'])
    return out


def selftest():
    fails = 0
    def check(name, ok):
        nonlocal fails
        print(('PASS ' if ok else 'FAIL ') + name); fails += not ok
    check('signature: two args', parse_signature('def implementation (numbers: List Rat) (threshold: Rat) : Bool :=')
          == ([('numbers', ('List', ('Rat',))), ('threshold', ('Rat',))], ('Bool',)))
    check('signature: shared binder', [n for n, _ in parse_signature('def implementation (s0 s1: String) : Bool :=')[0]] == ['s0', 's1'])
    check('signature: pair type', parse_signature('def implementation (i: Int × Int) (j: Int × Int) : String :=')[0][0][1]
          == ('Prod', ('Int',), ('Int',)))
    check('signature: no space before colon', parse_signature('def implementation (n: Nat): Bool :=')[1] == ('Bool',))
    try:
        parse_signature('def implementation (f: Nat → Nat) : Nat :='); check('UNREACHED on a function type', False)
    except Unreached:
        check('UNREACHED on a function type', True)
    check('tests: = and ==', parse_tests('#test implementation [] [] = []\n#test implementation ["this"] [] == []')
          == [('[] []', '[]'), ('["this"] []', '[]')])
    check('tests: commented lines are not tests', parse_tests('-- #test implementation 5 = [2,3]') == [])
    r1, r2 = random.Random('7:0'), random.Random('7:0')
    t = ('List', ('Prod', ('Int',), ('String',)))
    check('seeded draw is reproducible', [rand_val(t, r1) for _ in range(5)] == [rand_val(t, r2) for _ in range(5)])
    check('boundary k=0 of a list is []', boundary(('List', ('Int',)), 0) == '[]')
    check('boundary k=2 of a list has 2 elements', boundary(('List', ('Int',)), 2) == '[0, 1]')
    check('typed renders a type ascription', typed('-1', ('Int',)) == '((-1) : Int)')
    check('error_lines reads a tagged error', error_lines('x/u1-p0-R1.lean:12:3: error: no', 'u1-p0-R1') == {12})
    check('error_lines ignores another tag', error_lines('x/u1-p0-R1.lean:12:3: error: no', 'u1-p0-R0') == set())
    plain = 'def problem_spec\n-- f\n(impl: List Int → Int)\n(xs: List Int) :=\nlet spec (r: Int) := r = 0\n∃ result, impl xs = result ∧ spec result'
    rec = plain.replace('r = 0', 'r = 1 + impl xs.tail')
    renamed = rec.replace('impl', 'implementation')
    commented = plain.replace('r = 0', 'r = 0 -- impl is not called here')
    check('binder uses: a plain spec reads 2', spec_binder_uses(plain) == ('impl', 2))
    check('binder uses: a recursive spec reads 3', spec_binder_uses(rec)[1] == 3)
    check('binder uses: follows the binder NAME (implementation)', spec_binder_uses(renamed) == ('implementation', 3))
    check('binder uses: a comment is not a use', spec_binder_uses(commented)[1] == 2)
    check('binder uses: `impl` inside `implementation` is not counted', spec_binder_uses(
          plain.replace('r = 0', 'r = implementation_size')) [1] == 2)
    def row(pid, i, key, trust='KERNEL', src='random'):
        return [pid, f'p{pid}-{i}', src, 'ref', 'x', 'y', key, 'R1', trust]
    rows = [row('7', i, 'yes') for i in range(10)] + [row('7', 10 + i, 'no') for i in range(2)] + \
           [row('7', 20, 'yes', 'COMPILED'), row('7', 21, 'DROPPED', '-')] + [row('9', i, 'no', src='test') for i in range(3)]
    d = draw(rows, 's')
    d7 = [r_ for r_ in d if r_[0] == '7']
    check('draw: cap 8 per problem', len(d7) == 8)
    check('draw: balanced where possible (2 no available, so 2 no + 6 yes)', sum(r_[6] == 'no' for r_ in d7) == 2)
    check('draw: COMPILED never drawn', all(r_[8] == 'KERNEL' for r_ in d))
    check('draw: DROPPED never drawn', all(r_[6] in ('yes', 'no') for r_ in d))
    check('draw: a small problem gives all it has', len([r_ for r_ in d if r_[0] == '9']) == 3)
    check('draw: stratum from the input source', {r_[9] for r_ in d if r_[0] == '9'} == {'test-input'})
    check('draw: reproducible', draw(rows, 's') == d)
    check('draw: the seed moves it', [r_[1] for r_ in draw(rows, 't')] != [r_[1] for r_ in d])
    print('SELFTEST', 'FAIL' if fails else 'OK', f'({fails} failed)')
    return 1 if fails else 0


def main():
    if sys.argv[1:] == ['--selftest']:
        sys.exit(selftest())
    ap = argparse.ArgumentParser()
    ap.add_argument('mode', choices=['plan', 'run', 'summary', 'draw'])
    ap.add_argument('--ids', nargs='+', type=int)
    ap.add_argument('--seed', default='o90-u1-2026-10-22')
    ap.add_argument('--n-random', type=int, default=4)
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    if a.mode == 'draw':
        hdr = open(os.path.join(a.out, 'items.tsv')).readline().rstrip('\n').split('\t')
        rows = [l.rstrip('\n').split('\t') for l in open(os.path.join(a.out, 'items.tsv'))][1:]
        d = draw(rows, a.seed)
        with open(os.path.join(a.out, 'drawn.tsv'), 'w') as f:
            f.write('\t'.join(hdr + ['stratum']) + '\n')
            for r_ in d:
                f.write('\t'.join(r_) + '\n')
        by = {}
        for r_ in d:
            by.setdefault(r_[0], [0, 0]); by[r_[0]][r_[6] == 'no'] += 1
        print(f'DRAW seed={a.seed}: {len(d)} items · yes {sum(v[0] for v in by.values())} · no {sum(v[1] for v in by.values())} · '
              f'test-input {sum(r_[9] == "test-input" for r_ in d)} · generated-input {sum(r_[9] == "generated-input" for r_ in d)}')
        print('per problem (yes/no): ' + ' '.join(f'{k}:{v[0]}/{v[1]}' for k, v in sorted(by.items(), key=lambda kv: int(kv[0]))))
        return
    if a.mode == 'summary':
        rows = [l.rstrip('\n').split('\t') for l in open(os.path.join(a.out, 'items.tsv'))][1:]
        summary(rows)
        return
    if not a.ids:
        ap.error('--ids is required for plan and run')
    if a.mode == 'plan':
        os.makedirs(a.out, exist_ok=True)
        for pid in a.ids:
            try:
                p = plan(pid, a.seed, a.n_random)
            except Unreached as e:
                print(f'UNREACHED problem_{pid}: {e}'); continue
            except SpecRecursive as e:
                print(f'DROPPED problem_{pid}: SPEC-RECURSIVE: {e}'); continue
            open(os.path.join(a.out, f'u1-p{pid}-eval.lean'), 'w').write(p['eval_src'])
            print(f'problem_{pid}: {"REF" if p["ref"] else "NOREF"} · {len(p["evals"])} inputs')
        return
    sys.exit(run(a.ids, a.seed, a.n_random, a.out))


if __name__ == '__main__':
    main()
