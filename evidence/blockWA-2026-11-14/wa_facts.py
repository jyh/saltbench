"""Block WA per-cell facts, read on the run box from each cell's own ctl/ record. Nothing is typed.
Block NA's cell_facts.py (evidence/blockNA-2026-09-28/, same tree) is imported unchanged for its columns; this file adds what WA's §WA6
and ADDENDUM 1 ask for beyond NA's:
  init_model        the set of `"model"` values in ctl/stream-1.ndjson. MEASURED 2026-11-14 on wawfp101: the one occurrence is the
                    client's `init` event, so this is the model the client says the session runs, NOT a per-response served id. The agy
                    stream carries no per-response model field that this file reads; NA's `served` column is requested_model for the
                    same reason. Both are printed; neither is a served-set reading in the Claude lane's sense
  client_sha256     ctl/built-from.tsv's client_sha256, first 16 hex (the binary that ran the cell, hashed at launch)
  cut_turns_all     lines carrying `print timeout` across BOTH client stderr files (agy-stderr-1.txt and agy-turnloop-stderr-1.txt);
                    NA's cut_turns reads the first file only, and both columns are printed so neither hides the other
  landed_tags       the repo's `landed-*` tags (`git tag -l`), comma-joined: a phase-1 cell may carry landed-2 from the P-PERSIST turn
A value that cannot be read is UNREAD.
usage (on the run box, $HOME relative):  python3 wa_facts.py <cell_facts.py path> <root>/<id> ...   -> JSON list on stdout"""
import json, os, re, subprocess, sys

H = os.path.expanduser('~')
NA_FACTS, cells = sys.argv[1], sys.argv[2:]
base = json.loads(subprocess.run([sys.executable, '-I', NA_FACTS] + cells, capture_output=True, text=True, check=True).stdout)
out = []
for rec in base:
    c = os.path.join(H, rec['root'], rec['id'], 'ctl')
    try:
        txt = open(os.path.join(c, 'stream-1.ndjson'), errors='replace').read()
        s = sorted(set(re.findall(r'"model"\s*:\s*"([^"]+)"', txt)))
        rec['init_model'] = ','.join(s) if s else 'UNREAD'
    except OSError:
        rec['init_model'] = 'UNREAD'
    try:
        b = dict(l.rstrip('\n').split('\t', 1) for l in open(os.path.join(c, 'built-from.tsv')) if '\t' in l)
        v = b.get('client_sha256', '').split()
        rec['client_sha256'] = v[0][:16] if v else 'UNREAD'
    except OSError:
        rec['client_sha256'] = 'UNREAD'
    n, seen = 0, 0
    for f in ('agy-stderr-1.txt', 'agy-turnloop-stderr-1.txt'):
        try:
            n += sum('print timeout' in l for l in open(os.path.join(c, f), errors='replace')); seen += 1
        except OSError:
            pass
    rec['cut_turns_all'] = n if seen == 2 else 'UNREAD'
    g = subprocess.run(['git', '-C', os.path.join(H, rec['root'], rec['id'], 'repo'), 'tag', '-l', 'landed-*'], capture_output=True, text=True)
    rec['landed_tags'] = ','.join(sorted(g.stdout.split())) if g.returncode == 0 and g.stdout.strip() else 'UNREAD'
    out.append(rec)
json.dump(out, sys.stdout, indent=1, sort_keys=True)
print()
