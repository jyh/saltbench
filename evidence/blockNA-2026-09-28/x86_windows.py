"""The x86 lane's agy condition windows, for block NA's x86-concurrency column (§NA0 row 6, §NA4, §NA6).
A window runs from a ledger FIRE to the same (cond, attempt)'s next terminal event (any EVENT beginning CONDITION-, DISCARD or STOP);
a FIRE with no terminal row ends at the END-MARKER's own stamp, and says so in its `end_src` column. Read from every
~/.fleet/executors/gemini.runs/x86-*/ledger.tsv. Nothing is typed.   usage: python3 x86_windows.py > x86_windows.tsv"""
import glob, os, re, sys
RUNS = os.path.expanduser('~/.fleet/executors/gemini.runs')
print('\t'.join(['wave', 'cond', 'attempt', 'start', 'end', 'end_event', 'end_src']))
for led in sorted(glob.glob(os.path.join(RUNS, 'x86-*', 'ledger.tsv'))):
    wave = os.path.basename(os.path.dirname(led))
    rows = [l.rstrip('\n').split('\t') for l in open(led)][1:]
    for i, r in enumerate(rows):
        if len(r) < 6 or r[5] != 'FIRE':
            continue
        end = next((x for x in rows[i + 1:] if x[1:3] == r[1:3] and re.match(r'CONDITION-|DISCARD|STOP', x[5])), None)
        if end:
            print('\t'.join([wave, r[1], r[2], r[0], end[0], end[5], 'ledger']))
        else:
            mk = os.path.join(os.path.dirname(led), 'END-MARKER')
            m = re.search(r'(\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ)', open(mk).read()) if os.path.exists(mk) else None
            print('\t'.join([wave, r[1], r[2], r[0], m.group(1) if m else 'UNREAD', 'NO-TERMINAL-ROW', 'END-MARKER' if m else 'UNREAD']))
