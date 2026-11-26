"""Per argon NCA cell: phase-1 and phase-2 wall_seconds and landed, from each cell's own ctl/agy-turnloop-{1,2}.json. Read-only.
Roots: every ~/cells-nca-*-argon-* dir; the cell is the one subdir holding ctl/. A missing file reads UNREAD."""
import glob, json, os
H = os.path.expanduser('~')
for root in sorted(glob.glob(os.path.join(H, 'cells-nca-*-argon-*'))):
    cells = [d for d in sorted(os.listdir(root)) if os.path.isdir(os.path.join(root, d, 'ctl'))]
    for c in cells or ['NO-CELL']:
        row = [os.path.basename(root), c]
        for ph in (1, 2):
            try:
                f = os.path.join(root, c, 'ctl', 'agy-turnloop-%d.json' % ph)
                if ph == 1 and not os.path.exists(f):   # after the phase-2 hand-off, phase 1's ctl is set aside
                    f = os.path.join(root, '_aside', c, 'phase1', 'ctl', 'agy-turnloop-1.json')
                t = json.load(open(f))
                row += [str(t.get('wall_seconds', 'UNREAD')), str(t.get('landed', 'UNREAD'))]
            except (OSError, ValueError):
                row += ['UNREAD', 'UNREAD']
        print('\t'.join(row))
