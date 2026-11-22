#!/usr/bin/env python3
"""ta_swarm_census.py — read-only, run on the run box from $HOME over each TA cell dir's ctl/stream-1.ndjson (the subject's main
conversation, as the client streams it). Per cell dir, one row: the agy `swarm` tool's DONE steps, the models of every `add` (a worker the
subject started), and the last `status` read's posts per member (last_post_seq). What it cannot see: a worker's own conversation, which
the client does not stream into the cell's file, so a worker's turns, tool calls and file writes are UNREAD here.
usage: python3 -I ta_swarm_census.py cells-ta-*/ta*/ctl/stream-1.ndjson > swarm.tsv"""
import json, sys

print('id\troot\tswarm_done_steps\tadded_models\tlast_status_posts')
for path in sys.argv[1:]:
    parts = path.split('/')
    n, added, posts = 0, [], '-'
    for line in open(path, errors='replace'):
        try:
            e = json.loads(line)
        except ValueError:
            continue
        su = e.get('step_update') or {}
        if su.get('tool_name') != 'swarm' or su.get('state') != 'DONE':
            continue
        n += 1
        ti = su.get('tool_info') or {}
        p = ti.get('parameters') or {}
        out = ti.get('output') or ''
        if p.get('action') == 'add':
            added.append(p.get('model', 'UNREAD'))
        if p.get('action') == 'status':
            try:
                d = json.loads(out[out.find('{'):])
                posts = ','.join('%s:%s' % (m.get('name'), m.get('last_post_seq')) for m in d.get('members', [])) or '-'
            except ValueError:
                posts = 'UNREAD'
    print('%s\t%s\t%d\t%s\t%s' % (parts[1], parts[0], n, ','.join(added) or '-', posts))
