#!/usr/bin/env python3
# YP step c raw (run on the run box): for every AGY-shape cell of record and every phase N with ctl/agy-meter-N.json, read
#   (1) the meter's per_key (the turn-level fold, which is T), (2) the per-REQUEST usage the stream carries on each DONE
#   agent_response step, deduped by (conversation, step), recovering records from interleaved lines where a whole record
#   survives, and (3) the turn loop's wall. It prints the step coverage beside the per-request figures, because Pro's price
#   has a 200k-prompt tier and a request whose usage was lost cannot be put in a tier.
# usage: agy-steps-raw.py <cellroots.tsv>      (reads ~/<root>/<cell>/ctl)
import csv, glob, json, os, re, sys
KEYS = ('input_tokens', 'output_tokens', 'cache_read_tokens', 'thinking_tokens')
DEC = json.JSONDecoder()
def records(path):
    good = bad = rec = 0
    for line in open(path, errors='replace'):
        try: yield json.loads(line); good += 1; continue
        except Exception: bad += 1
        # an interleaved line: try every '{"event"' start; keep what decodes whole
        for m in re.finditer(r'\{"event"', line):
            try: obj, _ = DEC.raw_decode(line, m.start()); rec += 1; yield obj
            except Exception: pass
    records.stat = (good, bad, rec)
cols = ['cell', 'root', 'phase', 'served', 'meter_input', 'meter_cache_read', 'meter_output', 'meter_thinking', 'meter_T',
        'steps', 'step_input', 'step_cache_read', 'step_output', 'step_thinking', 'coverage', 'max_prompt', 'n_over_200k',
        'bad_lines', 'recovered', 'lo_input', 'lo_output', 'lo_cache_read', 'lo_thinking', 'hi_input', 'hi_output',
        'hi_cache_read', 'hi_thinking', 'wall_s', 'done_reason', 'note']
TIER = 200000   # Pro's price tier is on each request's PROMPT = input + cache_read (the Gemini price page; step b)
print('\t'.join(cols))
for row in csv.DictReader((l for l in open(sys.argv[1]) if not l.startswith('#')), delimiter='\t'):
    if row['shape'] != 'AGY': continue
    ctl = os.path.expanduser('~/%s/%s/ctl' % (row['root'], row['cell']))
    phases = sorted(int(re.search(r'-(\d+)\.json$', p).group(1)) for p in glob.glob(ctl + '/agy-meter-*.json'))
    if not phases: print('\t'.join([row['cell'], row['root'], '-'] + ['-'] * (len(cols) - 4) + ['NO-METER'])); continue
    for n in phases:
        m = json.load(open('%s/agy-meter-%d.json' % (ctl, n))); pk = m.get('per_key', {})
        out = [row['cell'], row['root'], n, ','.join(m.get('served_models') or []) or '-'] + [pk.get(k, 0) for k in ('input_tokens', 'cache_read_tokens', 'output_tokens', 'thinking_tokens')] + [m.get('T')]
        # level 8 set a finished phase ASIDE before the next ran (its phase_facts name the path): read that phase's stream and turn
        # loop there when the cell's own ctl has none. The meter file stays the cell's own.
        aside = os.path.expanduser('~/%s/_aside/%s/phase%d/ctl' % (row['root'], row['cell'], n))
        note = []
        sp = '%s/stream-%d.ndjson' % (ctl, n)
        if not os.path.exists(sp) and os.path.exists('%s/stream-%d.ndjson' % (aside, n)):
            sp = '%s/stream-%d.ndjson' % (aside, n); note.append('ASIDE')
        if os.path.exists(sp):
            steps = {}
            for r in records(sp):
                su = r.get('step_update') if isinstance(r, dict) else None
                if not isinstance(su, dict) or not su.get('usage') or su.get('state') != 'DONE': continue
                steps[(su.get('conversation_id'), su.get('step_index'))] = su['usage']
            s = {k: sum(int(u.get(k, 0) or 0) for u in steps.values()) for k in KEYS}
            pr = [int(u.get('input_tokens', 0) or 0) + int(u.get('cache_read_tokens', 0) or 0) for u in steps.values()]
            full = all(s[k] == int(pk.get(k, 0) or 0) for k in KEYS)
            over = any(s[k] > int(pk.get(k, 0) or 0) for k in KEYS)
            cov = 'COMPLETE' if full else ('EXCEEDS-METER' if over else 'PARTIAL')
            g, b, rc = records.stat
            out += [len(steps), s['input_tokens'], s['cache_read_tokens'], s['output_tokens'], s['thinking_tokens'], cov,
                    max(pr) if pr else 0, sum(p > 200000 for p in pr), b, rc]
            for hi in (False, True):
                us = [u for u in steps.values() if (int(u.get('input_tokens', 0) or 0) + int(u.get('cache_read_tokens', 0) or 0) > TIER) == hi]
                out += [sum(int(u.get(k, 0) or 0) for u in us) for k in KEYS]   # KEYS order: input, output, cache_read, thinking
        else:
            out += ['-'] * 18; note.append('NO-STREAM')
        tl = '%s/agy-turnloop-%d.json' % (ctl, n)
        if not os.path.exists(tl) and os.path.exists('%s/agy-turnloop-%d.json' % (aside, n)): tl = '%s/agy-turnloop-%d.json' % (aside, n)
        if os.path.exists(tl):
            t = json.load(open(tl)); out += [t.get('wall_seconds', '-'), t.get('done_reason', '-')]
        else: out += ['-', '-']; note.append('NO-TURNLOOP')
        print('\t'.join(map(str, out + [';'.join(note) or '-'])))
