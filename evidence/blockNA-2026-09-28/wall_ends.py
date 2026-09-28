"""Which end fired for block NA's TURN-TIMEOUT cells: the wall (A7.2's AGY_MAX_WALL) or the controller's turn patience.
Runs ON THE RUN BOX, so that the client log's local-time stamps convert with that box's own zone. Read-only.
usage: scp wall_ends.py <run-box>:/tmp/na_wall_ends.py; ssh <run-box> "python3 /tmp/na_wall_ends.py <root/id> ..." > wall_ends.tsv
       (with --caps, prints every named cell's ctl/caps.tsv instead: the per-cell record, a second method beside the CAPS line)

THE MECHANISM (agy_turnloop_v3.py, blob 0004386efa3c at export e10f420d596f, and 8259d5f35437 at 59508ac5e7ad; the end logic is
the same in both): a continue turn is sent, then `_wait_turn(n, min(wall_deadline, now + turn_timeout))`, and a False return is
recorded TURN-TIMEOUT. WALL-CAP is recorded only at the loop's top, after a result has ARRIVED. So when the wall falls inside a
turn's wait, the wait ends at the wall and the record says TURN-TIMEOUT.

THE READING, per cell. t0 = the launch log's "TURN LOOP ON" stamp, W = t0 + caps.tsv max_wall. The client runs its queued messages
one at a time and logs "Print mode" as it starts each one, so message k+1's start is where result k was emitted. The last continue
turn (number c = continue_turns) was sent after result c: s_c >= start of message c+1. Its patience deadline is then
>= s_c + turn_timeout. If W is earlier than that lower bound, the wall bound the wait, whatever the exact send time.
The awaited result (c+1) is emitted at message c+2's start, when that message exists; that time is printed beside W.
The map needs one client message per result. A turn the client auto-denies emits NO result, so when the counts differ the timing
columns are not read, and a cell whose loop ENDED before W is decided on that alone (the wall cannot have bound it)."""
import datetime, json, os, re, sys

def utc(s):
    return datetime.datetime.strptime(s, '%Y-%m-%dT%H:%M:%SZ').replace(tzinfo=datetime.timezone.utc)

def client_starts(log, year):
    out = []
    for l in open(log, encoding='utf-8', errors='replace'):
        m = re.match(r'[IWE](\d\d)(\d\d) (\d\d:\d\d:\d\d)\.\d+ +\d+ session\.go:\d+\] Print mode: conversation=', l)
        if m:
            loc = datetime.datetime.strptime('%d-%s-%s %s' % (year, m.group(1), m.group(2), m.group(3)), '%Y-%m-%d %H:%M:%S')
            out.append(loc.astimezone(datetime.timezone.utc))   # naive -> this box's local zone
    return out

def fmt(t):
    return t.strftime('%Y-%m-%dT%H:%M:%SZ') if t else '-'

args = sys.argv[1:]
if args and args[0] == '--caps':
    print('\t'.join(['cell', 'max_wall', 'max_turns', 'print_timeout', 'turn_timeout']))
    for c in args[1:]:
        p = os.path.expanduser('~/%s/ctl/caps.tsv' % c)
        kv = dict(l.rstrip('\n').split('\t', 1) for l in open(p)) if os.path.exists(p) else {}
        print('\t'.join([c] + [kv.get(k, 'MISSING') for k in ['max_wall', 'max_turns', 'print_timeout', 'turn_timeout']]))
    sys.exit(0)

print('\t'.join(['cell', 'done_reason', 'wall_seconds', 'continue_turns', 'loop_on', 'W_wall_deadline', 'last_send_lb',
                 'patience_deadline_lb', 'awaited_result_at', 'awaited_minus_W_s', 'loop_end', 'messages_vs_results', 'bound_by']))
for c in args:
    d = os.path.expanduser('~/%s/ctl' % c)
    j = json.load(open(os.path.join(d, 'agy-turnloop-1.json')))
    caps = dict(l.rstrip('\n').split('\t', 1) for l in open(os.path.join(d, 'caps.tsv')))
    ll = open(os.path.join(d, 'launch.log'), encoding='utf-8', errors='replace').read()
    on = utc(re.findall(r'^(\S+) TURN LOOP ON', ll, re.M)[-1])
    end = utc(re.findall(r'^(\S+) TURN LOOP STDERR', ll, re.M)[-1])
    W = on + datetime.timedelta(seconds=int(caps['max_wall']))
    st = client_starts(os.path.join(d, 'agy-client-1.log'), on.year)
    k = j['continue_turns']
    send_lb = st[k] if len(st) > k else None                       # message k+1 started => result k emitted
    pat_lb = send_lb + datetime.timedelta(seconds=float(caps['turn_timeout'])) if send_lb else None
    awaited = st[k + 1] if len(st) > k + 1 else None               # message k+2 started => result k+1 emitted
    aligned = len(st) == j['results']        # one client message per result; denied turns emit none, which breaks the map
    if not aligned:
        send_lb = pat_lb = awaited = None
    if end < W:
        bound = 'TURN-PATIENCE (the loop ended %ds before W)' % (W - end).total_seconds()
    elif pat_lb is None:
        bound = 'UNREAD'
    elif W < pat_lb:
        bound = 'WALL (W precedes the patience deadline by >= %ds)' % (pat_lb - W).total_seconds()
    else:
        bound = 'TURN-PATIENCE (patience deadline precedes W by <= %ds)' % (W - pat_lb).total_seconds()
    print('\t'.join([c, j['done_reason'], str(j['wall_seconds']), str(k), fmt(on), fmt(W), fmt(send_lb), fmt(pat_lb),
                     fmt(awaited), '%+d' % (awaited - W).total_seconds() if awaited else '-', fmt(end),
                     '%d/%d%s' % (len(st), j['results'], '' if aligned else ' NOT ALIGNED: timing columns not read'), bound]))
