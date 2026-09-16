#!/usr/bin/env python3
"""HC1 concurrency census: for every HC1 stage-1 cell, which other cells (any wave, any client) on this box
overlapped its run window. Zero spend, read-only. Window = earliest ISO stamp in ctl/launch.log .. latest
end-N stamp; a cell with no end-N uses the newest mtime under ctl/ and is flagged NOEND."""
import glob, os, re, datetime as dt, sys
ISO = re.compile(r'(20\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ)')
def ts(s): return dt.datetime.strptime(s, '%Y-%m-%dT%H:%M:%SZ').replace(tzinfo=dt.timezone.utc).timestamp()
def window(cell):
    ctl = os.path.join(cell, 'ctl'); L = os.path.join(ctl, 'launch.log')
    if not os.path.isfile(L): return None
    starts = [ts(m) for m in ISO.findall(open(L, errors='replace').read())]
    if not starts: return None
    ends = []
    for e in glob.glob(os.path.join(ctl, 'end-[0-9]*')):
        m = ISO.findall(open(e, errors='replace').read())
        if m: ends.append(max(ts(x) for x in m))
    if ends: return min(starts), max(ends), 'END'
    newest = max(os.path.getmtime(os.path.join(ctl, f)) for f in os.listdir(ctl))
    return min(starts), newest, 'NOEND'
def client(cell):
    p = os.path.join(cell, 'ctl', 'client')
    return open(p).read().strip() if os.path.isfile(p) else '?'
home = os.path.expanduser('~')
cells = sorted(d for d in glob.glob(home + '/cells-*/*') if os.path.isdir(d + '/ctl'))
W = {}
for c in cells:
    w = window(c)
    if w: W[c] = w
hc1 = sorted((c for c in W if re.search(r'/cells-hc1-[^/]+/hc1[a-z]{2}\d\d$', c)), key=lambda c: W[c][0])
print('population: %d cell dirs with ctl/ · %d with a readable window · %d HC1 cells' % (len(cells), len(W), len(hc1)))
tot_any = 0
for c in hc1:
    s, e, k = W[c]
    ov = []
    for o, (s2, e2, k2) in W.items():
        if o == c or o in hc1: continue
        sec = min(e, e2) - max(s, s2)
        if sec > 0: ov.append((sec, o, client(o), k2))
    hc1_ov = [o for o in hc1 if o != c and min(e, W[o][1]) - max(s, W[o][0]) > 0]
    tot_any += 1 if ov else 0
    name = os.path.basename(c)
    print('%s %s..%s %5.1fmin %s  other-cells=%d  hc1-overlap=%d  %s' % (name, dt.datetime.utcfromtimestamp(s).strftime('%m-%dT%H:%M'), dt.datetime.utcfromtimestamp(e).strftime('%H:%M'), (e-s)/60, k, len(ov), len(hc1_ov), ' '.join(os.path.basename(x) for x in hc1_ov)))
    for sec, o, cl, k2 in sorted(ov, reverse=True)[:6]:
        print('     %6.1f min  %-6s %s %s' % (sec/60, cl, o.replace(home + '/', ''), '' if k2 == 'END' else k2))
print('HC1 cells with >=1 overlapping non-HC1 cell: %d of %d' % (tot_any, len(hc1)))

# --- per-arm exposure and the AT-FIRE reading (PREDICTIONS §6.3 item 3 is a preflight AT the fire)
arm_of = {'p': 'plain', 'b': 'placebo', 's': 'salt-diet'}
agg = {}
print('\nAT-FIRE and EXPOSURE per HC1 cell: shared = minutes of the window during which >=1 other cell ran (union, not a sum)')
for c in hc1:
    s, e, k = W[c]
    name = os.path.basename(c); arm = arm_of[name[4]]
    at_fire = [o for o, (s2, e2, k2) in W.items() if o not in hc1 and s2 <= s < e2]
    covered = sorted((max(s, s2), min(e, e2)) for o, (s2, e2, k2) in W.items() if o not in hc1 and min(e, e2) > max(s, s2))
    union = 0; cur = None
    for a, b in covered:
        if cur is None or a > cur[1]:
            if cur: union += cur[1] - cur[0]
            cur = [a, b]
        else: cur[1] = max(cur[1], b)
    if cur: union += cur[1] - cur[0]
    g = agg.setdefault(arm, [0, 0, 0.0, 0.0, 0])
    g[0] += 1; g[1] += 1 if covered else 0; g[2] += union / 60; g[3] += (e - s) / 60; g[4] += 1 if at_fire else 0
    print('  %s %-9s window %5.1f min · shared %5.1f min (%3.0f%%) · at fire: %s' % (name, arm, (e-s)/60, union/60, 100*union/(e-s), ', '.join(os.path.basename(x) for x in at_fire) or 'quiet'))
print('\nPER ARM: cells · cells with any overlap · cells NOT quiet at fire · shared minutes / window minutes')
for arm in ('plain', 'placebo', 'salt-diet'):
    n, ov, sh, wm, af = agg[arm]
    print('  %-9s %2d cells · %2d overlapped · %d not quiet at fire · %6.1f / %6.1f min = %4.1f%%' % (arm, n, ov, af, sh, wm, 100*sh/wm))
