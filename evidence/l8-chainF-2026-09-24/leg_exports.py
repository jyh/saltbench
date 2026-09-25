"""Per leg of mode F: the export its cells were SCORED under, read from line 1 of every score file (`score_wave: tools from … (<sha12>)`),
and the export its chain RAN on, read from the lane's EXPORT.sha. The two must agree for every leg (T1, one sha per leg); a leg whose
score files disagree with each other or with EXPORT.sha makes this script exit 3. Nothing is typed.

usage: leg_exports.py <chain-run-dir> ...   (e.g. l8u-2026-09-24-paxos; score dirs are found beside it by the chain's naming)"""
import glob, os, re, sys

RUNS = os.path.expanduser('~/.fleet/executors/gemini.runs')
print('leg\tran_on\tscored_on\tscore_files\tverdict')
bad = 0
for d in sys.argv[1:]:
    d = d.rstrip('/'); base = os.path.basename(d); date_lane = base.split('l8u-')[1]
    ran = open(os.path.join(RUNS, d, 'EXPORT.sha')).read().split()[0][:12]
    for h in sorted(glob.glob(os.path.join(RUNS, d, 'harvest-*'))):
        if not os.path.exists(os.path.join(h, 'HARVESTED')):
            continue
        leg = os.path.basename(h)[len('harvest-'):]
        files = sorted(glob.glob(os.path.join(RUNS, 'l8u-%s-%s-score' % (leg, date_lane), '*.score.txt')))
        shas = {re.search(r'\(([0-9a-f]{12})\)', open(f).readline()).group(1) for f in files}
        ok = len(files) > 0 and shas == {ran}
        bad += not ok
        print('\t'.join([leg, ran, ','.join(sorted(shas)) or 'UNREAD', str(len(files)), 'OK' if ok else 'MISMATCH']))
sys.exit(3 if bad else 0)
