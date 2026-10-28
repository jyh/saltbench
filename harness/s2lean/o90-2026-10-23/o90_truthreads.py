#!/usr/bin/env python3
"""o90_truthreads.py — the O90 truth axis's CLAUDE-side reads (AMENDMENT-O90-stage1 ADDENDUM 3 A3.3 · A3.4 · A3.4a, ADDENDUM 4):
read 2 (one fresh Claude session per CHUNK of at most 7 of an artifact's written sentences, ADDENDUM 7; blind to read 1), the confirmer's calibration on stage 0
leg (b)'s items, and the confirmer (one session per artifact with a FALSE flag, over the UNION of the reads' FALSE rows).
Every set writes rows `o90_flaglog.py --population` accepts. This driver is the ONLY writer of HALTED for its sets, and only
from an A3.5 trigger, which it keeps beside the set in HALT.txt (systems' N4). A confirmation the halt did not reach is written
`confirmed = UNSCORED` (it fails safe), and HALT.txt names that too (N5).
A read is `<client> -p --tools "" --strict-mcp-config --model <m> --output-format json` with the prompt on stdin, in an EMPTY
working directory, with CLAUDE_CONFIG_DIR = the pool's config dir. No tool is available, so no hook can fire.
Halts (A3.5; one cap across the three sets): the set stops when the summed client-reported `total_cost_usd` passes --cap-usd, at a
503, or at 3 failed reads in a row (a failed read: the client exits non-zero, reports is_error, or no line parses after its one
retry). Every unit is PAUSED after the first --pause-after reads (A3.5's metered 2): the operator reads the pool and re-runs.
  usage: o90_truthreads.py read2   --population P --state S --out D --cfg C [--model M] [--client X] [--cap-usd U] [--pause-after N]
         o90_truthreads.py calib   --legb ITEMS --specs <legb>/specs --out D --cfg C [...]
   every spending set takes --meter M (ONE file shared by all three: A3.5's one cap); past the metered first reads it needs
   --points-at-pause P, the pool's reading over them: USD per point = the meter's own USD over them / P, the guard 3 x it (A5.3)
         o90_truthreads.py confirm --population P --state S --flags LOG [--flags LOG2] --out D --cfg C [...]
         o90_truthreads.py merge   --flags LOG [--flags LOG2] [--confirmations D/confirmations.tsv] --out D   (no spend)
         o90_truthreads.py --selftest"""
import argparse, collections, hashlib, json, math, os, re, shutil, subprocess, sys, tempfile

READ_PROMPT = ("Below is a Lean file written by an agent, then numbered sentences from that agent's documentation of it. For EACH "
               "sentence, say whether it is FALSE of this Lean file: it states something the file's definitions and theorems do not "
               "say, or contradict. Answer one line per sentence, in the order given, exactly `<n>: OK` or `<n>: FALSE`.")
CONF_PROMPT = ("Below is a Lean file written by an agent, then numbered sentences that a reader judged false of it. A sentence is "
               "FALSE of this Lean file if it states something the file's definitions and theorems do not say, or contradict. For "
               "EACH sentence, first write the name of the Lean declaration the sentence is about and what that declaration states, "
               "then on its own line answer exactly `<n>: CONFIRMED-FALSE` or `<n>: NOT-FALSE`.")
READ_ANS = re.compile(r'^\s*(\d+):\s*(OK|FALSE)\s*$', re.M)
CONF_ANS = re.compile(r'^\s*(\d+):\s*(CONFIRMED-FALSE|NOT-FALSE)\s*$', re.M)
READ_CHUNK = 7   # ADDENDUM 7 (A7.3): a read's unit is (artifact, chunk); a0's artifacts are one chunk each
COLS = ["problem", "arm", "b_episode", "sentence", "sentence_sha256", "reader", "mechanism", "verdict", "confirmer", "confirmed"]


def render(lean, sentences, head):
    return head + "\n\n```lean\n" + lean.rstrip() + "\n```\n\n" + "\n".join("%d. %s" % (i, s) for i, s in enumerate(sentences, 1)) + "\n"


def parse(text, pat, n):
    """-> {index: answer} for indices 1..n answered exactly once; a duplicated or out-of-range index is dropped."""
    got = collections.defaultdict(list)
    for m in pat.finditer(text or ''):
        i = int(m.group(1))
        if 1 <= i <= n: got[i].append(m.group(2))
    return {i: v[0] for i, v in got.items() if len(v) == 1}


def call(client, cfg, model, prompt):
    """-> (ok, result_text, cost_usd, session, transient_503). ok is False on a non-zero exit or is_error."""
    with tempfile.TemporaryDirectory(prefix='o90tr-') as cwd:
        env = dict(os.environ, CLAUDE_CONFIG_DIR=cfg)
        r = subprocess.run([client, '-p', '--tools', '', '--strict-mcp-config', '--model', model, '--output-format', 'json'],
                           input=prompt, capture_output=True, text=True, cwd=cwd, env=env)
    blob = r.stdout + r.stderr
    try: j = json.loads(r.stdout)
    except ValueError: j = {}
    cost = float(j.get('total_cost_usd') or 0.0)
    ok = r.returncode == 0 and not j.get('is_error') and 'result' in j
    served = ','.join(sorted((j.get('modelUsage') or {}).keys())) or 'UNREAD'
    t503 = (not ok) and (' 503' in blob or '"503"' in blob or 'status 503' in blob)   # L1: a successful answer that quotes 503 is not a 503
    return ok, j.get('result', ''), cost, j.get('session_id', 'no-session'), t503, served


class Meter:
    """ONE meter for all three sets (systems' M2): the cap is A3.5's one cap, so every set appends to the same file."""
    def __init__(self, path, cap, pause_after):
        self.path, self.cap, self.pause_after = path, cap, pause_after
        self.rows = [l.rstrip('\n').split('\t') for l in open(path)][1:] if os.path.exists(path) else []
        self.fails = 0
    def spent(self): return sum(float(r[2]) for r in self.rows)
    def units(self): return list(dict.fromkeys(r[0] for r in self.rows))   # systems' L: a READ is a unit, its retry is not another
    def first_usd(self, n):
        first = set(self.units()[:n]); return sum(float(r[2]) for r in self.rows if r[0] in first)
    def record(self, unit, session, cost, ok, served):
        if not os.path.exists(self.path): open(self.path, 'w').write('unit\tsession\tcost_usd\tok\tserved_model\n')
        open(self.path, 'a').write('%s\t%s\t%.6f\t%s\t%s\n' % (unit, session, cost, 'yes' if ok else 'no', served))
        self.rows.append([unit, session, str(cost), 'yes' if ok else 'no', served])


def refuse_rerun(meter, label):
    """systems' M2 for the two sets with no intended stop: their rows are written at the end, so a set the meter already holds
    reads of was interrupted (or ran); a second run would be a second, unrecorded draw of the same reads. The lead decides."""
    if any(u.startswith(label + ':') for u in meter.units()):
        raise SystemExit('REFUSE: the meter already holds %s reads; a %s set is never re-run on it (an interrupted set is a case for the lead)' % (label, label))


def require_read2_first(meter, args):
    """P1 (the PM): the metered first reads, and so the pause, belong to read 2 (A3.6 order). calib and confirm have no resume,
    so they refuse to run on a meter that has not yet passed them."""
    if len(meter.units()) < args.pause_after:
        raise SystemExit('REFUSE: %s runs after read 2 (A3.6): the shared meter holds %d reads, fewer than the %d metered first'
                         % (args.set, len(meter.units()), args.pause_after))
    if args.pause_after and not os.path.exists(args.meter + '.RESUMED'):   # P1' (systems): read 2 PAUSED is not read 2 past its pause
        raise SystemExit('REFUSE: %s runs after read 2 is past its pause (A3.6, A5.3): %s.RESUMED does not exist' % (args.set, args.meter))


def run_units(units, head, pat, args, meter, done, label, on_unit=None):
    """units: [(unit_id, lean, [sentences])]. -> {unit_id: (session, {i: answer} or None)}; writes HALT.txt / PAUSED on a stop.
    on_unit(uid, session, ans) runs as each unit lands, so a killed set keeps every read it made (systems' M2, 10-28)."""
    res, halt = {}, None
    for uid, lean, sents in units:
        if uid in done: continue
        if halt: break
        if meter.spent() > args.cap_usd: halt = 'spend: %.2f USD passed the cap %.2f' % (meter.spent(), args.cap_usd); break
        if len(meter.units()) >= args.pause_after:
            if not os.path.exists(args.meter + '.RESUMED'):
                open(args.meter + '.PAUSED', 'w').write('PAUSED after %d reads (A3.5): read the pool, then re-run with --points-at-pause and touch %s.RESUMED\n' % (len(meter.units()), args.meter))
                return res, 'PAUSED'
            if args.cap_usd == float('inf'):
                raise SystemExit('REFUSE: no read past the first %d until the pool\'s point reading over them is given (A5.3): pass --points-at-pause' % args.pause_after)
            pr = getattr(args, 'points_record', None)   # S1 (systems on #406): written just before the first call that USES the reading,
            if pr and not os.path.exists(pr[0]): open(pr[0], 'w').write(pr[1])   # so no refusal before it, in main or in a set, leaves one
        ans, session = None, 'no-session'
        for attempt in (1, 2):
            ok, text, cost, session, t503, served = call(args.client, args.cfg, args.model, render(lean, sents, head))
            got = parse(text, pat, len(sents)) if ok else {}
            meter.record('%s:%s' % (label, uid), session, cost, ok and bool(got), served)   # G1: one id space per SET
            if t503: halt = '503 on %s' % uid; break
            if got: ans = got; break
        meter.fails = 0 if ans else meter.fails + 1   # M1: a READ fails once, after its retry
        res[uid] = (session, ans)
        if on_unit: on_unit(uid, session, ans)
        if meter.fails >= 3 and not halt: halt = '3 failed reads in a row (last %s)' % uid
    if halt: open(os.path.join(args.out, 'HALT.txt'), 'w').write('HALT %s\n' % halt)
    return res, halt


def load_pop(path, expect):
    sha = hashlib.sha256(open(path, 'rb').read()).hexdigest()[:16]
    if sha != expect: raise SystemExit('REFUSE: population sha256/16 %s, not the registered %s (A3.6 (1))' % (sha, expect))
    rows = [l.rstrip('\n').split('\t') for l in open(path, encoding='utf-8') if not l.startswith('#')]
    assert rows[0] == ["problem", "arm", "b_episode", "sentence", "sentence_sha256", "given", "text"], rows[0]
    return [dict(zip(rows[0], r)) for r in rows[1:]], sha


def artifacts(pop, state, only=None):
    by = collections.OrderedDict()
    for r in pop:
        if r['given'] != 'no' or (only is not None and (r['b_episode'], r['sentence']) not in only): continue
        by.setdefault((r['problem'], r['arm'], r['b_episode']), []).append(r)
    out = []
    for (p, a, e), rs in by.items():
        lean = open(os.path.join(state, 'problem_%s' % p, a, 'B.artifact', 'stageB.lean'), encoding='utf-8', errors='replace').read()
        out.append(((p, a, e), lean, rs))
    return out


def leg_b_spec(specs, p, manifest):
    """The Lean leg (b)'s items were written against (systems' B1): <specs>/p<p>.lean, its sha256 (trailing newline stripped)
    checked against MANIFEST.tsv's spec_sha12."""
    txt = open(os.path.join(specs, 'p%s.lean' % p), encoding='utf-8').read()
    got = hashlib.sha256(txt.rstrip('\n').encode()).hexdigest()[:12]
    if manifest.get(p) != got: raise SystemExit('REFUSE: specs/p%s.lean sha %s, MANIFEST says %s' % (p, got, manifest.get(p)))
    return txt


def read_chunks(arts, k):
    """A7.3/A7.4: each artifact's written rows in file order, cut into consecutive chunks of k (the last holds the rest);
    an artifact's chunks are consecutive, so a halt splits at most one artifact. -> [(uid, lean, rows)]"""
    return [('%s/%s/%s#%d' % (key + (j // k + 1,)), lean, rs[j:j + k]) for key, lean, rs in arts for j in range(0, len(rs), k)]


def cmd_read2(args):
    pop, sha = load_pop(args.population, args.expect_sha)
    units = read_chunks(artifacts(pop, args.state), getattr(args, 'chunk', READ_CHUNK))
    have = existing_units(args.out)
    done = {uid for uid, lean, rs in units if all((r['b_episode'], r['sentence']) in have for r in rs)}
    meter = Meter(args.meter, args.cap_usd, args.pause_after)
    byuid = {uid: rs for uid, lean, rs in units}
    def land(uid, session, ans):   # systems' M2: a read's rows are written the moment it lands, never only at the set's end
        append_rows(args.out, [[r['problem'], r['arm'], r['b_episode'], r['sentence'], r['sentence_sha256'], session, 'claude',
                                (ans or {}).get(i, 'UNSCORED'), '-', '-'] for i, r in enumerate(byuid[uid], 1)], sha)
    res, stop = run_units([(uid, lean, [r['text'] for r in rs]) for uid, lean, rs in units], READ_PROMPT, READ_ANS, args, meter, done, 'read2', land)
    rows = []
    for uid, lean, rs in units:
        if uid in done or uid in res or stop == 'PAUSED': continue
        rows += [[r['problem'], r['arm'], r['b_episode'], r['sentence'], r['sentence_sha256'], 'halt-%s' % r['b_episode'], 'claude', 'HALTED', '-', '-'] for r in rs]
    append_rows(args.out, rows, sha)
    return stop


def existing_units(out):
    """-> {(b_episode, sentence)} already in rows.tsv; a chunk is done when every one of its sentences is (A7.3)."""
    p = os.path.join(out, 'rows.tsv')
    if not os.path.exists(p): return set()
    return {(r[2], r[3]) for r in (l.rstrip('\n').split('\t') for l in open(p)) if r[0] != 'problem'}


def append_rows(out, rows, sha):
    p = os.path.join(out, 'rows.tsv')
    new = not os.path.exists(p)
    with open(p, 'a') as f:   # ONE write per call, so a unit's rows reach the file together (systems' LOW 1 on #414)
        f.write(('\t'.join(COLS) + '\n' if new else '') + ''.join('\t'.join(r) + '\n' for r in rows))
    open(os.path.join(out, 'POPULATION.sha'), 'w').write(sha + '\n')


def cmd_confirm(args):
    pop, sha = load_pop(args.population, args.expect_sha)
    flagged = collections.OrderedDict()
    for f in args.flags:
        for r in (l.rstrip('\n').split('\t') for l in open(f)):
            if r[0] != 'problem' and r[7] == 'FALSE': flagged[(r[2], r[3])] = True
    arts = artifacts(pop, args.state, only=set(flagged))
    meter = Meter(args.meter, args.cap_usd, args.pause_after); require_read2_first(meter, args); refuse_rerun(meter, 'confirm')
    res, stop = run_units([('%s/%s/%s' % k, lean, [r['text'] for r in rs]) for k, lean, rs in arts], CONF_PROMPT, CONF_ANS, args, meter, set(), 'confirm')
    with open(os.path.join(args.out, 'confirmations.tsv'), 'w') as f:
        f.write('b_episode\tsentence\tconfirmer\tconfirmed\n')
        for k, lean, rs in arts:
            uid = '%s/%s/%s' % k
            session, ans = res.get(uid, ('halt-confirm-%s' % k[2], None))
            for i, r in enumerate(rs, 1):
                a = (ans or {}).get(i)
                v = 'HALTED' if uid not in res else {'CONFIRMED-FALSE': 'yes', 'NOT-FALSE': 'no'}.get(a, 'UNSCORED')
                f.write('%s\t%s\t%s\t%s\n' % (r['b_episode'], r['sentence'], session, v))
    if stop and stop != 'PAUSED':
        open(os.path.join(args.out, 'HALT.txt'), 'a').write('an artifact the confirmer did not reach is confirmed=HALTED and leaves the A3.4b denominator whole (A5.4)\n')
    open(os.path.join(args.out, 'POPULATION.sha'), 'w').write(sha + '\n')
    return stop


def cmd_merge(args):
    """The final flag log: every read row (read 1's and read 2's), with each FALSE row's confirmer and confirmed joined from
    confirmations.tsv. A FALSE with no confirmation (the confirmer never reached it) is confirmer `none`, confirmed UNSCORED."""
    conf = {}
    if args.confirmations:
        for r in (l.rstrip('\n').split('\t') for l in open(args.confirmations)):
            if r[0] != 'b_episode': conf[(r[0], r[1])] = (r[2], r[3])
    out = ['\t'.join(COLS)]
    for f in args.flags:
        for r in (l.rstrip('\n').split('\t') for l in open(f)):
            if r[0] == 'problem': continue
            if r[7] == 'FALSE':
                if args.confirmations and (r[2], r[3]) not in conf:
                    raise SystemExit('REFUSE: FALSE %s %s has no confirmations row: the confirmer was given other flags (M3)' % (r[2], r[3]))
                r[8], r[9] = conf.get((r[2], r[3]), ('none', 'UNSCORED'))
            out.append('\t'.join(r))
    open(os.path.join(args.out, 'flaglog.tsv'), 'w').write('\n'.join(out) + '\n')
    return None


def cmd_calib(args):
    raw = [l.rstrip('\n').split('\t') for l in open(args.legb, encoding='utf-8')]
    items = [dict(zip(raw[0], r)) for r in raw[1:]]
    mf = [l.rstrip('\n').split('\t') for l in open(os.path.join(args.specs, 'MANIFEST.tsv'))]
    manifest = {r[0]: r[3] for r in mf[1:]}
    # B2 (systems; the PM's crossed split, A5.2): a TRUE item never shares a session with its own mutant, and every session is
    # MIXED. Session A = TRUE items of odd pair index K + PLANTED items of even K; session B = the complement.
    by = collections.OrderedDict()
    for it in items:
        kk = int(re.search(r'-s(\d+)$', it['slot']).group(1))
        side = 'A' if (it['key'] == 'TRUE') == (kk % 2 == 1) else 'B'
        by.setdefault((it['problem'], side), []).append(it)
    units = [('%s/%s' % k, leg_b_spec(args.specs, k[0], manifest), [it['sentence'] for it in its]) for k, its in by.items()]
    meter = Meter(args.meter, args.cap_usd, args.pause_after); require_read2_first(meter, args); refuse_rerun(meter, 'calib')
    res, stop = run_units(units, CONF_PROMPT, CONF_ANS, args, meter, set(), 'calib')
    with open(os.path.join(args.out, 'calib.tsv'), 'w') as f:
        f.write('item_id\tkey\tmut_true\tconfirmer\tanswer\n')
        for k, its in by.items():
            session, ans = res.get('%s/%s' % k, ('unreached', None))
            for i, it in enumerate(its, 1):
                f.write('%s\t%s\t%s\t%s\t%s\n' % (it['item_id'], it['key'], it['mut_true'], session, (ans or {}).get(i, 'UNSCORED')))
    summarize_calib(os.path.join(args.out, 'calib.tsv'))
    return stop


def upper95(k, n):
    """One-sided 95 % exact (Clopper-Pearson) upper bound on a rate with k of n."""
    if n == 0: return float('nan')
    if k == n: return 1.0
    lo, hi = k / n, 1.0
    for _ in range(80):
        mid = (lo + hi) / 2
        if sum(math.comb(n, j) * mid ** j * (1 - mid) ** (n - j) for j in range(k + 1)) > 0.05: lo = mid
        else: hi = mid
    return hi


def summarize_calib(path):
    rows = [dict(zip(['item_id', 'key', 'mut_true', 'confirmer', 'answer'], l.rstrip('\n').split('\t'))) for l in open(path)][1:]
    t = [r for r in rows if r['key'] == 'TRUE' and r['answer'] != 'UNSCORED']
    fp = sum(r['answer'] == 'CONFIRMED-FALSE' for r in t)
    out = ['CALIBRATION (A3.4a): TRUE scored %d · confirmed FALSE %d · rate %.4f · 95 %% upper %.4f · UNSCORED %d'
           % (len(t), fp, fp / len(t) if t else float('nan'), upper95(fp, len(t)), sum(r['key'] == 'TRUE' and r['answer'] == 'UNSCORED' for r in rows))]
    for mt in ('NO', 'YES'):
        pl = [r for r in rows if r['key'] == 'PLANTED' and r['mut_true'] == mt and r['answer'] != 'UNSCORED']
        out.append('  PLANTED mut_true=%s scored %d · confirmed FALSE %d (recall)' % (mt, len(pl), sum(r['answer'] == 'CONFIRMED-FALSE' for r in pl)))
    open(os.path.join(os.path.dirname(path), 'calib-summary.txt'), 'w').write('\n'.join(out) + '\n')
    print('\n'.join(out))
    return fp, len(t)


STUB = r'''#!/usr/bin/env python3
import sys, json, os, re
p = sys.stdin.read(); mode = os.environ.get('STUB_MODE', 'ok')
n = len(re.findall(r'^\d+\. ', p, re.M)); conf = 'CONFIRMED-FALSE' in p
cnt = os.environ['STUB_COUNT']; k = int(open(cnt).read() or 0) + 1 if os.path.exists(cnt) else 1; open(cnt, 'w').write(str(k))
if mode == 'fail' or (mode == 'fail-after-1' and k > 1): print(json.dumps({"is_error": True, "result": "x"})); sys.exit(1)
if mode == '503' and k == 2: sys.stderr.write('API Error: status 503\n'); sys.exit(1)
if mode == 'ok-503-text': print(json.dumps({"result": '\n'.join('%d: OK' % i for i in range(1, n + 1)) + '\nnote: status 503 appears in a quoted sentence', "total_cost_usd": 0.01, "session_id": "s-%s-%d" % (os.path.basename(cnt), k)})); sys.exit(0)
if mode == 'garbage-first' and k == 1: print(json.dumps({"result": "no answers", "total_cost_usd": 0.01, "session_id": "s-%s-%d" % (os.path.basename(cnt), k)})); sys.exit(0)
ans = '\n'.join('%d: %s' % (i, ('CONFIRMED-FALSE' if i % 2 else 'NOT-FALSE') if conf else ('FALSE' if i == 1 else 'OK')) for i in range(1, n + 1))
if mode == 'drop-last': ans = '\n'.join(ans.splitlines()[:-1])
print(json.dumps({"result": ans, "total_cost_usd": float(os.environ.get('STUB_COST', '0.5')), "session_id": "s-%s-%d" % (os.path.basename(cnt), k)}))
'''


def selftest():
    ok = n = 0
    def arm(name, cond):
        nonlocal ok, n
        n += 1; ok += bool(cond); print(('PASS ' if cond else 'FAIL ') + name)
    def rows_of(path): return [l.rstrip('\n').split('\t') for l in open(path)][1:]
    with tempfile.TemporaryDirectory() as t:
        stub = os.path.join(t, 'claude'); open(stub, 'w').write(STUB); os.chmod(stub, 0o755)
        st = os.path.join(t, 'state')
        for p, a in (('5', 'a5'), ('5', 'a0'), ('6', 'a5')):
            d = os.path.join(st, 'problem_' + p, a, 'B.artifact'); os.makedirs(d); open(os.path.join(d, 'stageB.lean'), 'w').write('theorem t%s%s : True := trivial\n' % (p, a))
        pop = os.path.join(t, 'sentences.tsv')
        rows = [['5', 'a5', 'e55', 'doc:1', 'h1', 'no', 'The theorem states truth here.'], ['5', 'a5', 'e55', 'explain:1', 'h2', 'no', 'It also says another thing.'],
                ['5', 'a0', 'e50', 'doc:1', 'h3', 'no', 'The a0 file says one thing.'], ['5', 'a0', 'e50', 'doc:2', 'h4', 'yes', 'Given text from the task.'],
                ['6', 'a5', 'e65', 'explain:1', 'h5', 'no', 'Problem six has a sentence.']]
        open(pop, 'w').write('problem\tarm\tb_episode\tsentence\tsentence_sha256\tgiven\ttext\n' + ''.join('\t'.join(r) + '\n' for r in rows) + '# TOTAL\n')
        psha = hashlib.sha256(open(pop, 'rb').read()).hexdigest()[:16]
        k = [0]
        def args(out, meter=None, **kw):
            os.makedirs(out, exist_ok=True); k[0] += 1
            a = argparse.Namespace(set='test', population=pop, state=st, out=out, cfg=t, model='claude-opus-5', client=stub, cap_usd=100.0, pause_after=99,
                                   flags=[], legb=None, specs=None, confirmations=None, expect_sha=psha,
                                   meter=meter or os.path.join(t, 'meter-%d.tsv' % k[0])); a.__dict__.update(kw)
            # pause_after=0 models a set that runs after read 2 on a meter already past its metered, resumed first reads
            if a.pause_after == 0: open(a.meter + '.RESUMED', 'w').write('')
            return a
        def env(mode, cnt, cost='0.5'): os.environ.update(STUB_MODE=mode, STUB_COUNT=os.path.join(t, cnt), STUB_COST=cost)
        here = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, here); import o90_flaglog as F
        popd = F.load_population(open(pop))
        env('ok', 'c1'); o = os.path.join(t, 'r2'); cmd_read2(args(o)); lg = rows_of(os.path.join(o, 'rows.tsv')); r2rows = os.path.join(o, 'rows.tsv')
        arm('read 2 writes one row per WRITTEN sentence, never a given one', len(lg) == 4 and not any(r[3] == 'doc:2' for r in lg))
        arm('read 2 rows carry the parsed verdicts and the session as reader',
            [r[7] for r in lg] == ['FALSE', 'OK', 'FALSE', 'FALSE'] and all(r[5].startswith('s-') and r[6] == 'claude' for r in lg))
        env('ok', 'c1k'); ak1 = args(os.path.join(t, 'r2-k1'), chunk=1); cmd_read2(ak1); lk = rows_of(os.path.join(ak1.out, 'rows.tsv'))
        arm('A7.3: an artifact longer than the chunk is read in consecutive chunks, each numbered from 1 and mapped back to its own row',
            len(Meter(ak1.meter, 0, 99).units()) == 4 and [(r[3], r[7]) for r in lk if r[2] == 'e55'] == [('doc:1', 'FALSE'), ('explain:1', 'FALSE')]
            and len({r[5] for r in lk if r[2] == 'e55'}) == 2 and len(lg) == 4)
        env('ok', 'c1h'); ah1 = args(os.path.join(t, 'r2-k1h'), chunk=1, cap_usd=0.4); sh = cmd_read2(ah1); lh = rows_of(os.path.join(ah1.out, 'rows.tsv'))
        arm('A7.4: a spend halt between chunks splits that ONE artifact: its read chunk keeps its verdict, the rest is HALTED',
            sh.startswith('spend') and [(r[3], r[7]) for r in lh if r[2] == 'e55'] == [('doc:1', 'FALSE'), ('explain:1', 'HALTED')]
            and sum(r[7] == 'HALTED' for r in lh) == 3)
        ok1 = os.path.join(t, 'r2-k1kill'); os.makedirs(ok1); hl = open(os.path.join(ak1.out, 'rows.tsv')).readlines()
        open(os.path.join(ok1, 'rows.tsv'), 'w').write(hl[0] + [l for l in hl if '\te55\tdoc:1\t' in l][0])   # killed after e55's chunk 1 landed
        env('ok', 'c1kill'); ak2 = args(ok1, chunk=1); cmd_read2(ak2); lr = rows_of(os.path.join(ok1, 'rows.tsv'))
        arm('A7.3 + M2: a set killed between an artifact\'s chunks re-reads only the chunks that did not land (3 calls, each sentence once)',
            len(Meter(ak2.meter, 0, 99).units()) == 3 and sorted((r[2], r[3]) for r in lr) == sorted({(r[2], r[3]) for r in lr}) and len(lr) == 4)
        try: F.load(open(r2rows), popd); raw_ok = True
        except SystemExit: raw_ok = False
        arm('read 2 rows alone are NOT a flag log (a FALSE needs its confirmation)', raw_ok is False)
        try: cmd_read2(args(os.path.join(t, 'r2-badsha'), expect_sha='0' * 16)); refused = False
        except SystemExit as e: refused = 'not the registered' in str(e)
        arm('a population that is not the registered sha refuses (L4)', refused)
        env('drop-last', 'c2'); o = os.path.join(t, 'r2b'); cmd_read2(args(o)); lg = rows_of(os.path.join(o, 'rows.tsv'))
        arm('a sentence with no parseable answer is UNSCORED, not dropped', sum(r[7] == 'UNSCORED' for r in lg) == 3 and len(lg) == 4)
        env('garbage-first', 'c3'); a3 = args(os.path.join(t, 'r2c')); cmd_read2(a3); m = rows_of(a3.meter)
        arm('a read with no parseable line is retried once, and the meter records the served model', len(m) == 4 and m[0][3] == 'no' and len(m[0]) == 5)
        env('ok', 'c4'); a4 = args(os.path.join(t, 'r2d'), cap_usd=0.4); s = cmd_read2(a4); lg = rows_of(os.path.join(a4.out, 'rows.tsv'))
        arm('a spend halt writes HALTED for every unreached sentence and the trigger beside the set (N4)',
            s.startswith('spend') and 'spend' in open(os.path.join(a4.out, 'HALT.txt')).read() and sum(r[7] == 'HALTED' for r in lg) == 2 and sum(r[7] != 'HALTED' for r in lg) == 2)
        om = os.path.join(t, 'merge-halted'); cmd_merge(args(om, flags=[os.path.join(a4.out, 'rows.tsv')])); mg = rows_of(os.path.join(om, 'flaglog.tsv'))
        try: F.load(open(os.path.join(om, 'flaglog.tsv')), popd); acc2 = True
        except SystemExit as e: acc2 = str(e)
        arm('with no confirmer run, an unconfirmed FALSE merges as none/UNSCORED, never dropped, and the flag log accepts it',
            acc2 is True and any(r[7] == 'FALSE' and r[8:] == ['none', 'UNSCORED'] for r in mg))
        env('fail', 'c5'); a5 = args(os.path.join(t, 'r2e')); s = cmd_read2(a5); m = rows_of(a5.meter)
        arm('3 failed READS halt the set, each read counted once after its retry (M1)', s and s.startswith('3 failed') and len(m) == 6)
        env('503', 'c6'); s = cmd_read2(args(os.path.join(t, 'r2f')))
        arm('a 503 on a failed read halts the set', s and s.startswith('503'))
        env('ok-503-text', 'c6b'); s = cmd_read2(args(os.path.join(t, 'r2f2')))
        arm('a successful answer that quotes 503 does not halt (L1)', s is None)
        try: cmd_confirm(args(os.path.join(t, 'conf-first'), flags=[r2rows], pause_after=2)); p1 = False
        except SystemExit as e: p1 = 'runs after read 2' in str(e)
        arm('confirm and calib refuse before read 2 has passed the metered first reads (P1)', p1)
        envs = dict(os.environ); env('ok', 'c6c'); ap_ = args(os.path.join(t, 'r2-paused'), pause_after=2); cmd_read2(ap_)
        try: cmd_confirm(args(os.path.join(t, 'conf-during-pause'), meter=ap_.meter, flags=[r2rows], pause_after=2)); p1b = False
        except SystemExit as e: p1b = 'past its pause' in str(e)
        arm('confirm refuses while read 2 is PAUSED, before writing anything (systems\' P1\')', p1b and not os.path.exists(os.path.join(t, 'conf-during-pause', 'confirmations.tsv')))
        env('ok', 'c7'); a7 = args(os.path.join(t, 'r2g'), pause_after=2); s = cmd_read2(a7); lg = [l for l in open(os.path.join(a7.out, 'rows.tsv'))][1:]
        arm('the set PAUSES after the metered first reads, writing no HALTED', s == 'PAUSED' and os.path.exists(a7.meter + '.PAUSED') and not any('HALTED' in l for l in lg))
        open(a7.meter + '.RESUMED', 'w').write('')
        try: cmd_read2(args(a7.out, meter=a7.meter, pause_after=2, cap_usd=float('inf'))); norate = False
        except SystemExit as e: norate = 'point reading' in str(e)
        arm('no read past the metered first reads until the pool\'s point reading is given (A5.3)', norate)
        env('garbage-first', 'c7b'); a7b = args(os.path.join(t, 'r2g2'), pause_after=2); s = cmd_read2(a7b)
        arm('the pause counts READS, not attempts: a retried first read still leaves room for a second (systems\' L)',
            s == 'PAUSED' and len(Meter(a7b.meter, 0, 2).units()) == 2 and len(rows_of(a7b.meter)) == 3)
        open(a7b.meter + '.RESUMED', 'w').write('')   # S1: the record is written at the reading's first USE, so this run must read past the pause
        r = subprocess.run([sys.executable, os.path.abspath(__file__), 'read2', '--population', pop, '--state', st, '--out', a7b.out, '--cfg', t,
                            '--client', stub, '--meter', a7b.meter, '--expect-sha', psha, '--points-at-pause', '0.5'], capture_output=True, text=True)
        exp = 'USD per point %.4f' % (Meter(a7b.meter, 0, 2).first_usd(2) / 0.5)
        arm('USD per point is computed from the meter\'s own first reads and the point reading, and printed (systems\' T1)', exp in r.stdout)
        exp2 = 'guard %.4f USD = 1.5 points (read 2\'s share, A7.6)' % (1.5 * Meter(a7b.meter, 0, 2).first_usd(2) / 0.5)
        arm('A7.6: read 2\'s guard is 1.5 of the 3 points, derived from the same rate', exp2 in r.stdout)
        r2_ = subprocess.run([sys.executable, os.path.abspath(__file__), 'read2', '--population', pop, '--state', st, '--out', a7b.out, '--cfg', t,
                              '--client', stub, '--meter', a7b.meter, '--expect-sha', psha, '--points-at-pause', '0.7'], capture_output=True, text=True)
        r3_ = subprocess.run([sys.executable, os.path.abspath(__file__), 'read2', '--population', pop, '--state', st, '--out', a7b.out, '--cfg', t,
                              '--client', stub, '--meter', a7b.meter, '--expect-sha', psha, '--points-at-pause', '0.5', '--pause-after', '3'], capture_output=True, text=True)
        arm('the point reading AND its window are recorded; a different reading or a different window refuses (systems\' LOW, L1)',
            os.path.exists(a7b.meter + '.points') and open(a7b.meter + '.points').read().strip() == '0.5 2' and r2_.returncode == 1 and 'records 0.5 over 2' in r2_.stdout + r2_.stderr
            and r3_.returncode == 1 and 'records 0.5 over 2' in r3_.stdout + r3_.stderr)
        open(a7b.meter + '.points', 'w').write('')
        r4_ = subprocess.run([sys.executable, os.path.abspath(__file__), 'read2', '--population', pop, '--state', st, '--out', a7b.out, '--cfg', t,
                              '--client', stub, '--meter', a7b.meter, '--expect-sha', psha, '--points-at-pause', '0.5'], capture_output=True, text=True)
        arm('an empty record refuses by name, not by a crash (L2)', r4_.returncode == 1 and 'empty or unreadable' in r4_.stdout + r4_.stderr)
        mfresh = os.path.join(t, 'meter-fresh.tsv')
        r5_ = subprocess.run([sys.executable, os.path.abspath(__file__), 'read2', '--population', pop, '--state', st, '--out', os.path.join(t, 'r2-early'),
                              '--cfg', t, '--client', stub, '--meter', mfresh, '--expect-sha', psha, '--points-at-pause', '0.5'], capture_output=True, text=True)
        arm('a run refused before the window closes writes NO record, so the true reading is still accepted later (systems\' P1 on #404)',
            r5_.returncode == 1 and 'before the first' in r5_.stdout + r5_.stderr and not os.path.exists(mfresh + '.points'))
        mq = os.path.join(t, 'meter-q1.tsv'); shutil.copy(a7b.meter, mq)
        r6_ = subprocess.run([sys.executable, os.path.abspath(__file__), 'read2', '--population', pop, '--state', st, '--out', os.path.join(t, 'r2-q1'),
                              '--client', stub, '--meter', mq, '--expect-sha', psha, '--points-at-pause', '0.05'], capture_output=True, text=True)
        r7_ = subprocess.run([sys.executable, os.path.abspath(__file__), 'read2', '--population', pop, '--state', st, '--out', os.path.join(t, 'r2-q1b'),
                              '--cfg', t, '--client', stub, '--meter', mq, '--expect-sha', '0' * 16, '--points-at-pause', '0.05'], capture_output=True, text=True)
        arm('a run refused at the SET level (no --cfg; a wrong population sha) writes no record (systems\' Q1)',
            r6_.returncode == 1 and '--cfg is required' in r6_.stdout + r6_.stderr and r7_.returncode == 1
            and 'not the registered' in r7_.stdout + r7_.stderr and not os.path.exists(mq + '.points'))
        r8_ = subprocess.run([sys.executable, os.path.abspath(__file__), 'read2', '--population', pop, '--state', st, '--out', os.path.join(t, 'r2-q2'),
                              '--cfg', t, '--client', stub, '--expect-sha', psha, '--points-at-pause', '0.5'], capture_output=True, text=True)
        arm('--points-at-pause with no --meter refuses by name, not a TypeError (systems\' Q2)', r8_.returncode == 1 and '--meter is required' in r8_.stdout + r8_.stderr)
        open(mq + '.points', 'w').write('0.5 2 junk\n')
        r9_ = subprocess.run([sys.executable, os.path.abspath(__file__), 'read2', '--population', pop, '--state', st, '--out', os.path.join(t, 'r2-p2'),
                              '--cfg', t, '--client', stub, '--meter', mq, '--expect-sha', psha, '--points-at-pause', '0.5'], capture_output=True, text=True)
        arm('a record with anything beside "<points> <pause_after>" refuses (systems\' P2)', r9_.returncode == 1 and 'empty or unreadable' in r9_.stdout + r9_.stderr)
        mr1 = os.path.join(t, 'meter-r1.tsv'); shutil.copy(a7b.meter, mr1)   # past its first 2 reads, never RESUMED, no record
        rr1 = subprocess.run([sys.executable, os.path.abspath(__file__), 'confirm', '--population', pop, '--state', st, '--out', os.path.join(t, 'conf-r1'),
                              '--cfg', t, '--client', stub, '--meter', mr1, '--expect-sha', psha, '--flags', r2rows, '--points-at-pause', '0.05'], capture_output=True, text=True)
        arm('a calib/confirm refused by the A3.6 order writes no record, so the true reading is still accepted after read 2 resumes (systems\' R1)',
            rr1.returncode == 1 and 'past its pause' in rr1.stdout + rr1.stderr and not os.path.exists(mr1 + '.points'))
        rr2 = subprocess.run([sys.executable, os.path.abspath(__file__), 'merge', '--out', os.path.join(t, 'merge-r2'), '--flags', r2rows,
                              '--points-at-pause', '0.5'], capture_output=True, text=True)
        arm('merge with --points-at-pause refuses by name, not a TypeError (systems\' R2)',
            rr2.returncode == 1 and 'merge spends nothing' in rr2.stdout + rr2.stderr and 'Traceback' not in rr2.stderr)
        # G1 (systems): a later set's rows never count toward the first reads, so the guard does not move after confirm runs
        before = Meter(a7b.meter, 0, 2).first_usd(2); open(a7b.meter + '.RESUMED', 'w').write('')
        env('ok', 'c7c'); cmd_confirm(args(os.path.join(t, 'conf-g1'), meter=a7b.meter, flags=[r2rows], pause_after=2))
        arm('the guard\'s first-reads USD is unchanged after confirm runs on the same meter (systems\' G1)', Meter(a7b.meter, 0, 2).first_usd(2) == before
            and all(':' in r[0] for r in rows_of(a7b.meter)))
        s2 = cmd_read2(a7); lg = rows_of(os.path.join(a7.out, 'rows.tsv'))
        arm('a resumed set reads only what it had not read', s2 is None and len(lg) == 4 and len({r[3] + r[2] for r in lg}) == 4)
        env('ok', 'c8', cost='0.3'); shared = os.path.join(t, 'shared-meter.tsv')
        s1 = cmd_read2(args(os.path.join(t, 'r2h'), meter=shared, cap_usd=1.0)); s = cmd_read2(args(os.path.join(t, 'r2i'), meter=shared, cap_usd=1.0))
        n2 = sum(r[7] != 'HALTED' for r in rows_of(os.path.join(t, 'r2i', 'rows.tsv'))) if os.path.exists(os.path.join(t, 'r2i', 'rows.tsv')) else -1
        # set 1 spends 0.9 (3 reads at 0.3) under the 1.0 cap; only a SHARED meter halts set 2 after its first read
        arm('ONE meter across sets: a second set halts on the first set\'s spend (M2)', s1 is None and s and s.startswith('spend') and n2 == 2)
        env('ok', 'c9'); oc = os.path.join(t, 'conf'); cmd_confirm(args(oc, flags=[r2rows], pause_after=0)); c = rows_of(os.path.join(oc, 'confirmations.tsv'))
        arm('the confirmer reads only FALSE-flagged written sentences, one session per artifact',
            sorted(r[1] + r[0] for r in c) == sorted(['doc:1e55', 'doc:1e50', 'explain:1e65']) and len({r[2] for r in c}) == 3)
        om2 = os.path.join(t, 'merge'); cmd_merge(args(om2, flags=[r2rows], confirmations=os.path.join(oc, 'confirmations.tsv')))
        try: lgm = F.load(open(os.path.join(om2, 'flaglog.tsv')), popd); acc3 = True
        except SystemExit as e: acc3 = str(e)
        arm('read 2 + the confirmations merge into a log the flag log accepts, each FALSE carrying its confirmation',
            acc3 is True and all(r['confirmed'] in ('yes', 'no') for r in lgm if r['verdict'] == 'FALSE'))
        extra = os.path.join(t, 'read1.tsv'); open(extra, 'w').write('\t'.join(COLS) + '\n' + '\t'.join(['5', 'a5', 'e55', 'explain:1', 'h2', 'g1', 'gemini', 'FALSE', '-', '-']) + '\n')
        try: cmd_merge(args(os.path.join(t, 'merge-m3'), flags=[r2rows, extra], confirmations=os.path.join(oc, 'confirmations.tsv'))); m3 = False
        except SystemExit as e: m3 = 'no confirmations row' in str(e)
        arm('a FALSE the given confirmations never saw REFUSES the merge (M3)', m3)
        env('ok', 'c10', cost='0.5'); oc2 = os.path.join(t, 'conf2'); cmd_confirm(args(oc2, flags=[r2rows], cap_usd=0.4, pause_after=0)); c = rows_of(os.path.join(oc2, 'confirmations.tsv'))
        arm('an artifact the confirmer did not reach is confirmed HALTED, and HALT.txt says so (N5, A5.4)',
            any(r[3] == 'HALTED' for r in c) and 'leaves the A3.4b denominator' in open(os.path.join(oc2, 'HALT.txt')).read())
        om3 = os.path.join(t, 'merge-chalt'); cmd_merge(args(om3, flags=[r2rows], confirmations=os.path.join(oc2, 'confirmations.tsv')))
        lgh = F.load(open(os.path.join(om3, 'flaglog.tsv')), popd); ax = F.readings(lgh, popd)[0]
        arm('a confirm halt merges into a log the flag log accepts, the unreached artifact read as such',
            any(x[3] == 'UNREACHED by the confirmer' for x in ax))
        sp = os.path.join(t, 'specs'); os.makedirs(sp); mf = ['problem\tpath\tsha\tspec_sha12\tbytes']
        for p in ('5', '6'):
            body = 'def problem_spec (x : Nat) : Prop :=\n  x = x\n'; open(os.path.join(sp, 'p%s.lean' % p), 'w').write(body)
            mf.append('%s\tv\tx\t%s\t%d' % (p, hashlib.sha256(body.rstrip('\n').encode()).hexdigest()[:12], len(body)))
        open(os.path.join(sp, 'MANIFEST.tsv'), 'w').write('\n'.join(mf) + '\n')
        lb = os.path.join(t, 'legb.tsv')
        open(lb, 'w').write('item_id\tproblem\tslot\tkey\toperator\tsource_item\tmut_true\tsentence\n' + ''.join(
            '\t'.join(x) + '\n' for x in [['b1T', '5', 'p5-s1', 'TRUE', '-', '-', '-', 'a'], ['b1M', '5', 'p5-s1', 'PLANTED', 'op', 'b1T', 'NO', 'b'],
                                          ['b3T', '5', 'p5-s2', 'TRUE', '-', '-', '-', 'e'], ['b3M', '5', 'p5-s2', 'PLANTED', 'op', 'b3T', 'NO', 'f'],
                                          ['b2T', '6', 'p6-s1', 'TRUE', '-', '-', '-', 'c'], ['b2M', '6', 'p6-s1', 'PLANTED', 'op', 'b2T', 'YES', 'd']]))
        env('ok', 'c11'); ocal = os.path.join(t, 'cal'); cmd_calib(args(ocal, legb=lb, specs=sp, pause_after=0)); cal = rows_of(os.path.join(ocal, 'calib.tsv'))
        sm = open(os.path.join(ocal, 'calib-summary.txt')).read()
        arm('calibration reads leg (b)\'s own specs, reports TRUE false positives and PLANTED recall by mut_true (B1)',
            'TRUE scored 3 · ' in sm and 'mut_true=NO scored 2' in sm and 'mut_true=YES scored 1' in sm)
        sess = {r[0]: r[3] for r in cal}; key = {r[0]: r[1] for r in cal}
        mixed = all(len({key[i] for i in sess if sess[i] == sv}) == 2 for sv in {sess['b1T'], sess['b1M']})
        arm('the crossed split: no TRUE shares a session with its own mutant, and the sessions are MIXED (B2, A5.2)',
            sess['b1T'] != sess['b1M'] and sess['b3T'] != sess['b3M'] and sess['b2T'] != sess['b2M'] and mixed)
        open(os.path.join(sp, 'p6.lean'), 'a').write('-- edited\n')
        try: cmd_calib(args(os.path.join(t, 'cal2'), legb=lb, specs=sp, pause_after=0)); b1 = False
        except SystemExit as e: b1 = 'MANIFEST' in str(e)
        arm('a spec file that does not match MANIFEST refuses (B1)', b1)
        ms1 = os.path.join(t, 'meter-s1.tsv'); shutil.copy(a7b.meter, ms1); open(ms1 + '.RESUMED', 'w').write('')   # past its pause, resumed, no record
        base = [sys.executable, os.path.abspath(__file__), 'calib', '--state', st, '--cfg', t, '--client', stub, '--meter', ms1, '--points-at-pause', '0.05']
        rs1 = subprocess.run(base + ['--out', os.path.join(t, 'cal-s1'), '--legb', lb, '--specs', sp], capture_output=True, text=True)
        rs1b = subprocess.run(base + ['--out', os.path.join(t, 'cal-s1b'), '--specs', sp], capture_output=True, text=True)
        arm('a refusal INSIDE a set (a spec off its MANIFEST; no --legb) writes no record: it is written only before the first call that uses it (systems\' S1)',
            rs1.returncode == 1 and 'MANIFEST' in rs1.stdout + rs1.stderr and rs1b.returncode == 1 and '--legb is required' in rs1b.stdout + rs1b.stderr
            and 'Traceback' not in rs1b.stderr and not os.path.exists(ms1 + '.points'))
        cf = os.path.join(t, 'cfg-hook'); os.makedirs(cf); json.dump({'hooks': {'SessionStart': [{}]}}, open(os.path.join(cf, 'settings.json'), 'w'))
        try: check_cfg(cf); l2 = False
        except SystemExit as e: l2 = 'SessionStart' in str(e)
        cf2 = os.path.join(t, 'cfg-ok'); os.makedirs(cf2); json.dump({'hooks': {'PreToolUse': [{}]}}, open(os.path.join(cf2, 'settings.json'), 'w'))
        arm('a config dir with a non-tool hook refuses; a PreToolUse-only one passes (L2)', l2 and check_cfg(cf2) is None)
        arm('the 95 % upper bound at 0 of 45 is 6.4 %', abs(upper95(0, 45) - 0.0644) < 0.0005)
        # systems' M2 (on gemini's read-1 driver, 10-28): a killed set must not lose the reads it made. The kill is modelled as an
        # exception out of the SECOND call (a SIGKILL leaves the same files: whatever was written before it, nothing after).
        g = globals(); real_call = g['call']; nk = [0]
        def dying_call(*a_):
            nk[0] += 1
            if nk[0] == 2: raise KeyboardInterrupt('killed')
            return real_call(*a_)
        env('ok', 'c12'); ok12 = os.path.join(t, 'r2-kill'); ak = args(ok12); g['call'] = dying_call
        try: cmd_read2(ak)
        except KeyboardInterrupt: pass
        finally: g['call'] = real_call
        kept = rows_of(os.path.join(ok12, 'rows.tsv')) if os.path.exists(os.path.join(ok12, 'rows.tsv')) else []
        arm('M2: read 2 killed during its 2nd artifact keeps the 1st artifact\'s rows', len(kept) == 2 and {r[2] for r in kept} == {'e55'})
        env('ok', 'c12b'); cmd_read2(argparse.Namespace(**dict(vars(ak)))); allr = rows_of(os.path.join(ok12, 'rows.tsv'))
        arm('M2: the re-run reads only what did not land (2 calls, not 3) and rows.tsv holds each sentence once',
            int(open(os.path.join(t, 'c12b')).read()) == 2 and len(allr) == 4 and len({(r[2], r[3]) for r in allr}) == 4)
        env('ok', 'c13'); oc3 = os.path.join(t, 'conf3'); a13 = args(oc3, flags=[r2rows], pause_after=0); cmd_confirm(a13)
        try: cmd_confirm(argparse.Namespace(**dict(vars(a13)))); again = False
        except SystemExit as e: again = 'confirm' in str(e)
        arm('M2: confirm on a meter that already holds confirm reads REFUSES (no silent second draw)', again)
        pf6 = os.path.join(sp, 'p6.lean'); b6 = open(pf6).read().replace('-- edited\n', ''); open(pf6, 'w').write(b6)   # undo B1's edit: read, THEN truncate
        env('ok', 'c14'); ocal3 = os.path.join(t, 'cal3'); a14 = args(ocal3, legb=lb, specs=sp, pause_after=0); cmd_calib(a14)
        try: cmd_calib(argparse.Namespace(**dict(vars(a14)))); again = False
        except SystemExit as e: again = 'calib' in str(e)
        arm('M2: calib on a meter that already holds calib reads REFUSES', again)
    print('SELFTEST %d/%d' % (ok, n))
    return ok == n


def check_cfg(cfg):
    """L2 (systems): with --tools "" a tool hook cannot fire, but a session hook (SessionStart, UserPromptSubmit, Stop …) can."""
    p = os.path.join(cfg, 'settings.json')
    hooks = (json.load(open(p)).get('hooks') or {}) if os.path.exists(p) else {}
    bad = sorted(set(hooks) - {'PreToolUse', 'PostToolUse'})
    if bad: raise SystemExit('REFUSE: %s carries hook events that fire without a tool: %s' % (p, ', '.join(bad)))


def main():
    if sys.argv[1:] == ['--selftest']: sys.exit(0 if selftest() else 1)
    ap = argparse.ArgumentParser(); ap.add_argument('set', choices=['read2', 'calib', 'confirm', 'merge'])
    for a in ('--population', '--state', '--out', '--cfg', '--legb', '--specs', '--confirmations', '--meter', '--expect-sha'): ap.add_argument(a)
    ap.add_argument('--flags', action='append', default=[]); ap.add_argument('--model', default='claude-opus-5'); ap.add_argument('--client', default='claude')
    ap.add_argument('--points-at-pause', type=float); ap.add_argument('--pause-after', type=int, default=2)
    a = ap.parse_args(); os.makedirs(a.out, exist_ok=True)
    # Q1/Q2 (systems on #404): every set-level refusal runs BEFORE the point record can be written, so no refused run leaves one
    if a.set != 'merge':
        for need in ('meter', 'cfg') + (('legb', 'specs') if a.set == 'calib' else ()):
            if getattr(a, need) is None: raise SystemExit('REFUSE: --%s is required for a set that spends' % need.replace('_', '-'))
        check_cfg(a.cfg)
    if a.set in ('read2', 'confirm') and not a.expect_sha: raise SystemExit('REFUSE: --expect-sha (the registered population sha256/16) is required')
    if a.set in ('read2', 'confirm'): load_pop(a.population, a.expect_sha)
    if a.set == 'merge' and a.points_at_pause is not None:   # R2 (systems on #405)
        raise SystemExit('REFUSE: --points-at-pause prices a set that spends; merge spends nothing')
    if a.set in ('calib', 'confirm'): require_read2_first(Meter(a.meter, 0, a.pause_after), a)   # R1 (systems on #405): the A3.6 order, before the record
    # A5.3 (systems' T1): the cap of record is 3 POINTS. The USD guard is DERIVED: the meter's own USD over the first metered reads,
    # divided by the pool's point reading over the same window (the one number the operator gives), times 3. Never a typed rate.
    a.cap_usd = float('inf')
    if a.points_at_pause is not None:
        if a.points_at_pause <= 0: raise SystemExit('REFUSE: --points-at-pause must be > 0 (a window that moved the pool 0 points prices nothing)')
        pf = a.meter + '.points'   # systems: the reading AND its window are RECORDED beside the meter; every later run must match both
        if os.path.exists(pf):
            rec = open(pf).read().split()
            try:
                if len(rec) != 2: raise ValueError(rec)   # P2 (systems): exactly "<points> <pause_after>", nothing beside it
                rp, rw = float(rec[0]), int(rec[1])
            except (IndexError, ValueError): raise SystemExit('REFUSE: %s is empty or unreadable (want "<points> <pause_after>")' % pf)
            if (rp, rw) != (a.points_at_pause, a.pause_after):
                raise SystemExit('REFUSE: --points-at-pause %s over --pause-after %d, but %s records %s over %d' % (a.points_at_pause, a.pause_after, pf, rp, rw))
        m = Meter(a.meter, 0, a.pause_after)
        if len(m.units()) < a.pause_after: raise SystemExit('REFUSE: --points-at-pause given before the first %d reads exist on the meter' % a.pause_after)
        a.points_record = (pf, '%r %d\n' % (a.points_at_pause, a.pause_after))   # P1/Q1/R1/S1 (systems): run_units writes it at first use
        # ADDENDUM 7 (A7.6, the PM's word 10-28): read 2 runs first on the shared meter and halts at 1.5 of the 3 points, so the
        # calibration and the confirmer, which decide the axis, keep the rest. Their guard stays the whole 3 (the meter is shared).
        share = 1.5 if a.set == 'read2' else 3.0
        rate = m.first_usd(a.pause_after) / a.points_at_pause; a.cap_usd = share * rate
        print('USD per point %.4f (%.4f USD over the first %d reads / %.3f points) · guard %.4f USD = %g points%s'
              % (rate, m.first_usd(a.pause_after), a.pause_after, a.points_at_pause, a.cap_usd, share,
                 " (read 2's share, A7.6)" if a.set == 'read2' else ''))
    stop = {'read2': cmd_read2, 'calib': cmd_calib, 'confirm': cmd_confirm, 'merge': cmd_merge}[a.set](a)
    print('STOP %s' % stop if stop else 'DONE')


if __name__ == '__main__':
    main()
