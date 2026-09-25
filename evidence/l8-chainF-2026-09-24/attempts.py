"""Mode F's attempt record (A2.2: "the per-cell table carries each cell's ATTEMPT NUMBER"), derived from the supervisors' own
ledgers. Nothing is typed. A condition is (served model, problem, arm); its attempts are every FIRE of it across the legs named
on the command line, numbered in fire-time order, so a leg re-fired whole (ADDENDUM 11: Paxos-flash-rr -> Paxos-flash-rr2)
continues its predecessor's count rather than restarting it.

The outcome of an attempt is the ledger's own terminal event for that (cond, attempt): CONDITION-CLEAN, DISCARDED, or the
supervisor's STOP. An attempt with no terminal event is UNENDED, never CLEAN. Exactly one attempt per condition may be CLEAN,
and it is the one whose cells enter the table; a condition with zero or several CLEAN attempts makes this script exit 3.

usage: attempts.py <supervisor-run-dir> ...   (each holding ledger.tsv; the leg name is read from the directory name)"""
import collections, os, re, sys

TERMINAL = ('CONDITION-CLEAN', 'DISCARDED', 'STOP')

def ledger(d):
    for l in open(os.path.join(d, 'ledger.tsv')):
        f = l.rstrip('\n').split('\t')
        if len(f) >= 7 and re.match(r'\d{4}-', f[0]):
            yield f

def main(dirs):
    att = collections.OrderedDict()          # (leg, cond, attempt) -> record
    for d in dirs:
        leg = re.match(r'l8u-(.+?)-\d{4}-\d\d-\d\d-', os.path.basename(d.rstrip('/'))).group(1)
        model = 'gemini-3.1-pro-high' if '-pro-' in leg else 'gemini-3.8-flash-high' if '-flash-' in leg else 'UNREAD'
        pending_stop = None
        for utc, cond, a, root, prefix, ev, detail in (f[:7] for f in ledger(d)):
            if ev == 'FIRE':
                prob, arm = detail.split()[:2]
                att[(leg, cond, a)] = dict(model=model, problem=prob, arm=arm, leg=leg, cond=cond, leg_attempt=a,
                                           root=root, fired=utc, outcome='UNENDED', ended='-', detail='-')
            elif ev == 'STOP' and cond == '-':
                # the supervisor's STOP is leg-wide (cond and attempt '-'): it ends every attempt of this leg still open
                for (l2, _, _), r in att.items():
                    if l2 == leg and r['outcome'] == 'UNENDED':
                        r.update(outcome='STOP:' + detail.split(':')[0].split(' condition')[0], ended=utc, detail=detail[:160])
            elif ev in TERMINAL and (leg, cond, a) in att:
                r = att[(leg, cond, a)]
                r.update(outcome=ev if ev != 'STOP' else 'STOP:' + detail.split(':')[0], ended=utc,
                         detail=detail.split(' · CELLS ')[-1][:160] if ev == 'CONDITION-CLEAN' else detail[:160])
    by = collections.OrderedDict()
    for r in sorted(att.values(), key=lambda r: r['fired']):
        by.setdefault((r['model'], r['problem'], r['arm']), []).append(r)
    bad = 0
    print('\t'.join(['model', 'problem', 'arm', 'attempt', 'leg', 'leg_cond', 'leg_attempt', 'root', 'fired', 'ended', 'outcome', 'detail']))
    for k, rs in by.items():
        clean = sum(1 for r in rs if r['outcome'] == 'CONDITION-CLEAN')
        if clean != 1:
            bad += 1
            print('# ⛔ %s: %d CLEAN attempts (exactly 1 required)' % ('/'.join(k), clean), file=sys.stderr)
        for n, r in enumerate(rs, 1):
            det = re.sub(r'/Users/[^/\s]+/', '~/', r['detail'])     # a run-box home path is a location, not a fact of the attempt
            print('\t'.join([*k, str(n), r['leg'], r['cond'], r['leg_attempt'], r['root'], r['fired'], r['ended'], r['outcome'], det]))
    sys.exit(3 if bad else 0)

if __name__ == '__main__':
    main(sys.argv[1:])
