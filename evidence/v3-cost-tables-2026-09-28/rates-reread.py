#!/usr/bin/env python3
# YP step b: derive the Gemini list rates from the price page's TEXT, and check the Claude rows the meter uses against the Claude page.
# usage: rates-reread.py <gemini page .txt> <claude page .txt> <rates.tsv>   (each .txt is the page's HTML with tags stripped)
# Prints the Gemini rates TSV on stdout; exits 1 if any pattern fails to match or a Claude row disagrees with rates.tsv.
import re, sys
g, c, rates = (open(p).read() for p in sys.argv[1:4])
def one(pat, text, what):
    m = re.findall(pat, text)
    if len(m) != 1: sys.exit('REFUSED %s: %d matches for %s' % (what, len(m), pat))
    return m[0]
out = ['page_id\tlane_label\ttier\tinput\toutput_incl_thinking\tcache_read\tvalid']
fb = re.search(r'gemini-3\.8-flash Try it.*?Standard (.*?) Batch', g)
if not fb: sys.exit('REFUSED flash: no standard block')
f8 = fb.group(1)     # every price below is read INSIDE Flash's own Standard block, never from a later model's row
fl = (one(r'Input price Free of charge \$([\d.]+) through December 31, 2026\.', f8, 'flash input'),
      one(r'Output price \(including thinking tokens\) Free of charge \$([\d.]+) through December 31, 2026\.', f8, 'flash output'),
      one(r'Context caching price Free of charge \$([\d.]+) through December 31, 2026\.', f8, 'flash cache'))
out.append('gemini-3.8-flash\tgemini-3.8-flash-high\tall\t%s\t%s\t%s\tthrough 2026-12-31' % fl)
pro = re.search(r'gemini-3\.1-pro-preview and gemini-3\.1-pro-preview-customtools Try it.*?Standard (.*?) Batch', g)
if not pro: sys.exit('REFUSED pro: no standard block')
s = pro.group(1)
i = one(r'Input price Not available \$([\d.]+), prompts \$([\d.]+), prompts > 200k', s, 'pro input')
o = one(r'Output price \(including thinking tokens\) Not available \$([\d.]+), prompts \$([\d.]+), prompts > 200k', s, 'pro output')
k = one(r'Context caching price Not available \$([\d.]+), prompts \$([\d.]+), prompts > 200k', s, 'pro cache')
out.append('gemini-3.1-pro-preview\tgemini-3.1-pro-high\tprompt<=200k\t%s\t%s\t%s\t-' % (i[0], o[0], k[0]))
out.append('gemini-3.1-pro-preview\tgemini-3.1-pro-high\tprompt>200k\t%s\t%s\t%s\t-' % (i[1], o[1], k[1]))
upd = one(r'Last updated (\d{4}-\d{2}-\d{2}) UTC\. \[', g, 'gemini last-updated')
print('# derived from the Gemini API pricing page text; the page reads "Last updated %s UTC"' % upd)
print('\n'.join(out))
# the Claude rows the meter prices with: columns on the page are Input, Output, 5m writes, 1h writes, Hits and refreshes
hdr = one(r'(Name Input Output 5m writes 1h writes Hits and refreshes)', c, 'claude header')
bad = 0
for line in rates.splitlines():
    f = line.split('\t')
    if f[0] not in ('claude-opus-5', 'claude-sonnet-5'): continue
    name = {'claude-opus-5': 'Claude Opus 5', 'claude-sonnet-5': 'Claude Sonnet 5'}[f[0]]
    m = one(re.escape(name) + r' \$([\d.]+) / MTok \$([\d.]+) / MTok \$([\d.]+) / MTok \$([\d.]+) / MTok \$([\d.]+) / MTok', c, name)
    page = dict(zip(('input', 'output', 'w5', 'w1', 'read'), map(float, m)))
    tsv = dict(input=float(f[1]), w5=float(f[2]), w1=float(f[3]), read=float(f[4]), output=float(f[5]))
    ok = page == tsv; bad += not ok
    print('# CLAUDE %s page %s rates.tsv(read_on %s) %s -> %s' % (f[0], m, f[6], (f[1], f[5], f[2], f[3], f[4]), 'AGREE' if ok else 'DISAGREE'), file=sys.stderr)
sys.exit(1 if bad else 0)
