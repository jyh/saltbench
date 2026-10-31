#!/usr/bin/env python3
"""o90_fisher_checks.py FLAGLOG READ1 READ2 -> the figures the PM's #419 read asked to be written beside the decision:
each reader's a5-vs-a0 flag-rate one-sided Fisher (A3.4b's fairness condition), and the strict count (any sentence with an
UNSCORED read dropped). One-sided Fisher: P(X >= x) for a5's count under the hypergeometric with the margins fixed."""
import sys, math, collections
def fisher_ge(a, n1, b, n2):
    K, N = a + b, n1 + n2
    return sum(math.comb(K, x) * math.comb(N - K, n1 - x) for x in range(a, min(K, n1) + 1)) / math.comb(N, n1)
def tsv(p):
    r = [l.rstrip('\n').split('\t') for l in open(p)]; return [dict(zip(r[0], x)) for x in r[1:]]
for name, p in (('read 1 (gemini)', sys.argv[2]), ('read 2 (claude)', sys.argv[3])):
    c = collections.Counter()
    for r in tsv(p):
        if r['verdict'] in ('OK', 'FALSE'): c[(r['arm'], 'n')] += 1; c[(r['arm'], 'f')] += r['verdict'] == 'FALSE'
    print('FLAG-RATE FISHER %s: a5 %d/%d vs a0 %d/%d one-sided p = %.4f' % (name, c[('a5','f')], c[('a5','n')], c[('a0','f')], c[('a0','n')],
          fisher_ge(c[('a5','f')], c[('a5','n')], c[('a0','f')], c[('a0','n')])))
# strict: a sentence counts only if NO read of it is UNSCORED
fl = tsv(sys.argv[1]); h = list(fl[0].keys())
by = collections.defaultdict(list)
for r in fl: by[(r['arm'], r['b_episode'], r['sentence'])].append(r)
c = collections.Counter()
for (arm, ep, s), rs in by.items():
    if any(r['verdict'] not in ('OK', 'FALSE') for r in rs): continue
    if any(r['verdict'] == 'FALSE' and r['confirmed'] not in ('yes', 'no') for r in rs): continue
    c[(arm, 'n')] += 1; c[(arm, 'f')] += any(r['verdict'] == 'FALSE' and r['confirmed'] == 'yes' for r in rs)
print('STRICT (drop any sentence with an UNSCORED read): a5 %d/%d vs a0 %d/%d one-sided p = %.4f' % (c[('a5','f')], c[('a5','n')], c[('a0','f')], c[('a0','n')],
      fisher_ge(c[('a5','f')], c[('a5','n')], c[('a0','f')], c[('a0','n')])))
c = collections.Counter()
for (arm, ep, s), rs in by.items():
    if any(r['verdict'] not in ('OK', 'FALSE') for r in rs) and not any(r['verdict'] == 'FALSE' for r in rs): continue
    if any(r['verdict'] == 'FALSE' and r['confirmed'] not in ('yes', 'no') for r in rs): continue   # a flag the confirmer left UNSCORED
    c[(arm, 'n')] += 1; c[(arm, 'f')] += any(r['verdict'] == 'FALSE' and r['confirmed'] == 'yes' for r in rs)
print('CONTROL (rule E1 as flaglog applies it, recomputed here): a5 %d/%d vs a0 %d/%d one-sided p = %.4f' % (c[('a5','f')], c[('a5','n')], c[('a0','f')], c[('a0','n')],
      fisher_ge(c[('a5','f')], c[('a5','n')], c[('a0','f')], c[('a0','n')])))
# per artifact under the M2-literal rule: an artifact with ANY unscored sentence (at a read or at the confirmer) is UNSCORED
art = collections.defaultdict(list)
for (arm, ep, s), rs in by.items(): art[(arm, ep)].append(rs)
c = collections.Counter()
for (arm, ep), sents in art.items():
    if any(r['verdict'] not in ('OK', 'FALSE') or (r['verdict'] == 'FALSE' and r['confirmed'] not in ('yes', 'no')) for rs in sents for r in rs): c[(arm, 'UNSCORED')] += 1
    elif any(r['verdict'] == 'FALSE' and r['confirmed'] == 'yes' for rs in sents for r in rs): c[(arm, 'FALSE')] += 1
    else: c[(arm, 'zero')] += 1
for arm in ('a5', 'a0'):
    print('PER ARTIFACT, M2-literal: %s %d FALSE · %d UNSCORED · %d zero (artifacts with written prose)' % (arm, c[(arm, 'FALSE')], c[(arm, 'UNSCORED')], c[(arm, 'zero')]))
