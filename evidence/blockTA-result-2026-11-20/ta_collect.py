#!/usr/bin/env python3
"""ta_collect.py — copy the hand's block TA record INTO this directory, so ta_result_gen.py reads tracked files only.
Run once by the hand (gemini) on the box that holds its run record; the outputs are committed beside it.
  TA_RUNS (default ~/.fleet/executors/gemini.runs): the hand's private run record; two score dirs are read, named below, no glob over the root.
Outputs (each one a plain copy or a field-for-field extraction; nothing is computed here):
  flash-tally.tsv, argon-tally.tsv   the hand's tally.tsv of each wave, BYTE COPIES (one row per cell; categories in the last column)
  cell_facts.json                    every facts-<id>.json (wa_facts.py, read on the run box from each cell's own ctl/), concatenated,
                                     sorted by id. Flash's T-TA-F cell talfs101 has its facts under the tripwire's name, facts-ttaf.json (ALIAS below).
  receipts.tsv                       per cell, from its <id>.p1.score.txt (score_wave_v3.sh): verdict, TESTS, the scorer's TRUNCATED
                                     figure (a LINE count, 3 lines per timeout event), the interface hash, and the receipt's sha256/16.
                                     The receipts themselves are not copied: their first line names the scorer's private tool paths.
  meters.tsv                         per cell, from its <id>.meter.json (agy_meter_v3.py): requested model, served models, verdict, T.
                                     The meter's failure samples are not copied (they quote private paths).
  sextets/                           the hand's per-problem sextet files and per-wave total lines, BYTE COPIES (as posted on the bus).
  ct-sweep-2026-11-20.txt            the THE LINE sweep's instrument output (argon dir), BYTE COPY.
A cell named in a tally with no facts, receipt or meter file REFUSES (rc 2); nothing is written as blank or zero."""
import glob, hashlib, json, os, re, shutil, sys

HERE = os.path.dirname(os.path.abspath(__file__))
RUNS = os.environ.get('TA_RUNS') or os.path.expanduser('~/.fleet/executors/gemini.runs')
WAVES = (('flash', 'ta-flash-2026-11-17-score'), ('argon', 'ta-argon-2026-11-19-score'))
ALIAS = {'talfs101': 'ttaf'}   # the facts file the hand wrote for T-TA-F before the wave's per-cell naming; it holds exactly talfs101


def ids_of(tally):
    rows = open(tally).read().splitlines()
    return [r.split('\t')[0] for r in rows[1:] if r.strip()]


def main():
    facts, rec, met = [], [], []
    os.makedirs(os.path.join(HERE, 'sextets'), exist_ok=True)
    for wave, d in WAVES:
        src = os.path.join(RUNS, d)
        shutil.copyfile(os.path.join(src, 'tally.tsv'), os.path.join(HERE, '%s-tally.tsv' % wave))
        for f in sorted(glob.glob(os.path.join(src, '*-sextet.txt')) + glob.glob(os.path.join(src, '*-total-lines.txt'))):
            shutil.copyfile(f, os.path.join(HERE, 'sextets', os.path.basename(f)))
        for i in ids_of(os.path.join(src, 'tally.tsv')):
            need = [os.path.join(src, 'facts-%s.json' % ALIAS.get(i, i))] + [os.path.join(src, n % i) for n in ('%s.p1.score.txt', '%s.meter.json')]
            miss = [n for n in need if not os.path.isfile(n)]
            if miss:
                sys.exit('REFUSE rc 2: %s has no %s' % (i, ', '.join(os.path.basename(m) for m in miss)))
            fj = json.load(open(need[0]))
            if len(fj) != 1 or fj[0].get('id') != i:
                sys.exit('REFUSE rc 2: %s does not hold exactly cell %s' % (os.path.basename(need[0]), i))
            facts.append(dict(fj[0], wave=wave))
            raw = open(need[1], 'rb').read()
            text = raw.decode('utf-8', 'replace')
            v = re.findall(r'^%s\s+\S+\s+\S+\s+\S+\s+(PASS|FAIL|NOT-LANDED|NOT-SCORED)\b(.*)$' % re.escape(i), text, re.M)
            if len(v) != 1:
                sys.exit('REFUSE rc 2: %s.p1.score.txt carries %d verdict rows, 1 expected' % (i, len(v)))
            t = re.search(r'TESTS (\d+/\d+)', v[0][1])
            tr = re.search(r'TRUNCATED (\d+)\b', text)
            iface = re.search(r'share interface (\w+)', text)
            rec.append([i, wave, v[0][0], t.group(1) if t else 'UNREAD', tr.group(1) if tr else 'UNREAD',
                        iface.group(1)[:16] if iface else 'UNREAD', hashlib.sha256(raw).hexdigest()[:16]])
            m = json.load(open(need[2]))
            met.append([i, wave, m.get('requested_model', 'UNREAD'), ','.join(m.get('served_models') or ['UNREAD']),
                        m.get('verdict', 'UNREAD'), str(m.get('T', 'UNREAD'))])
    if os.path.isfile(os.path.join(RUNS, WAVES[1][1], 'ct-sweep-2026-11-20.txt')):
        shutil.copyfile(os.path.join(RUNS, WAVES[1][1], 'ct-sweep-2026-11-20.txt'), os.path.join(HERE, 'ct-sweep-2026-11-20.txt'))
    else:
        sys.exit('REFUSE rc 2: no ct-sweep-2026-11-20.txt')
    with open(os.path.join(HERE, 'cell_facts.json'), 'w') as f:
        json.dump(sorted(facts, key=lambda r: r['id']), f, indent=1, sort_keys=True)
        f.write('\n')
    for name, hdr, rows in (('receipts.tsv', ['id', 'wave', 'verdict', 'TESTS', 'scorer_truncated_lines', 'interface', 'receipt_sha256_16'], rec),
                            ('meters.tsv', ['id', 'wave', 'requested_model', 'served_models', 'meter_verdict', 'T'], met)):
        with open(os.path.join(HERE, name), 'w') as f:
            f.write('\t'.join(hdr) + '\n')
            for r in rows:
                f.write('\t'.join(r) + '\n')
    print('collected %d cells: facts %d · receipts %d · meters %d' % (len(facts), len(facts), len(rec), len(met)))


if __name__ == '__main__':
    main()
