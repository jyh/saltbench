# O57, v2: classify each conversation db by identity, not by size. METERED = a conversation id that appears as the stream's own
# conversation (init/step_update conversation_id in ctl/stream-*.ndjson, the cell's own or its _aside phases); SUB = every other db.
#   (A) sub-agent T  = Σ db T over SUB conversations      → tokens the agy meter never saw
#   (B) meter gap    = Σ db T over METERED − Σ meter T    → the meter's own reading of the stream vs the conversation's own record
import csv, glob, json, os, re, sys, collections, sqlite3
sys.path.insert(0, os.path.expanduser('~/bench-dry')); from pbsum import walk
def dbT(db):
    out = collections.Counter()
    for (d,) in sqlite3.connect("file:%s?mode=ro&immutable=1" % db, uri=True).execute("select data from gen_metadata"): walk(d, (), out)
    return out[(1,4,2)] + out[(1,4,3)] + out[(1,4,5)]
arm = dict(l.rstrip("\n").split("\t") for l in open(os.path.expanduser('~/bench-dry/cellarm.tsv')))
rows = [r for r in csv.DictReader((l for l in open(sys.argv[1]) if not l.startswith('#')), delimiter='\t') if r['shape'] == 'AGY']
agg = collections.defaultdict(collections.Counter)
print("cell\troot\tarm\tconvs\tmetered_ids\tmeterT\tdbT_metered\tsubT\tnote")
for r in rows:
    base = os.path.expanduser('~/%s/%s' % (r['root'], r['cell'])); aside = os.path.expanduser('~/%s/_aside/%s' % (r['root'], r['cell']))
    mT = sum(json.load(open(p)).get('T') or 0 for p in glob.glob(base + '/ctl/agy-meter-*.json'))
    ids = set()
    for sp in glob.glob(base + '/ctl/stream-*.ndjson') + glob.glob(aside + '/**/ctl/stream-*.ndjson', recursive=True):
        for line in open(sp, errors='replace'):
            for m in re.finditer(r'"conversation_id":\s*"([0-9a-f-]{36})"', line):
                if '"init"' in line or '"step_update"' in line[:40] or '"result"' in line[:40]: ids.add(m.group(1))
    # the stream's OWN conversation ids: those of init / result records (sub-agent ids appear only inside subagent_info)
    own = set()
    for sp in glob.glob(base + '/ctl/stream-*.ndjson') + glob.glob(aside + '/**/ctl/stream-*.ndjson', recursive=True):
        for line in open(sp, errors='replace'):
            try: o = json.loads(line)
            except Exception: continue
            for k in ('conversation_id',):
                if o.get(k): own.add(o[k])
            su = o.get('step_update') or {}
            if su.get('conversation_id'): own.add(su['conversation_id'])
            res = o.get('result') or {}
            if res.get('conversation_id'): own.add(res['conversation_id'])
    dbs = glob.glob(base + '/.agyhome/.gemini/antigravity-cli/conversations/*.db') + glob.glob(aside + '/**/conversations/*.db', recursive=True)
    met = sub = 0; seen = set()
    for d in dbs:
        cid = os.path.basename(d)[:-3]
        if cid in seen: continue
        seen.add(cid); t = dbT(d)
        if cid in own: met += t
        else: sub += t
    note = 'NO-OWN-ID' if not own else ''
    a = arm.get(r['cell'], 'UNMAPPED'); g = agg[a]
    g['cells'] += 1; g['meterT'] += mT; g['dbT_metered'] += met; g['subT'] += sub; g['cells_sub'] += (sub > 0); g['noown'] += (not own)
    print(f"{r['cell']}\t{r['root']}\t{a}\t{len(seen)}\t{len(own)}\t{mT}\t{met}\t{sub}\t{note}")
for a, g in agg.items():
    print(f"# {a}: cells {g['cells']} · meter T {g['meterT']:,} · (B) db T of metered convs {g['dbT_metered']:,} "
          f"({100*(g['dbT_metered']-g['meterT'])/max(g['meterT'],1):+.1f}% vs meter) · (A) SUB-AGENT T never metered {g['subT']:,} "
          f"(+{100*g['subT']/max(g['meterT'],1):.1f}% of meter) in {g['cells_sub']} cells · cells with no own id {g['noown']}")
