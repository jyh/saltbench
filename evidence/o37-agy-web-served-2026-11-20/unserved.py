#!/usr/bin/env python3
"""Print every search_web/read_url_content result step whose content is not a served summary/page."""
import glob, json, os
for p in sorted(glob.glob(os.path.expanduser("~/cells-*/*/.agyhome/.gemini/antigravity-cli/brain/*/.system_generated/logs/transcript_full.jsonl"))):
    rows = []
    for line in open(p, "rb"):
        try: rows.append(json.loads(line.decode("utf-8", "replace")))
        except Exception: rows.append(None)
    for i, r in enumerate(rows):
        if not isinstance(r, dict): continue
        for tc in r.get("tool_calls") or []:
            n = tc.get("name") if isinstance(tc, dict) else None
            if n in ("search_web", "read_url_content"):
                for r2 in rows[i+1:i+4]:
                    if isinstance(r2, dict) and r2.get("type") == "GENERIC":
                        c = str(r2.get("content", ""))
                        if "returned the following summary" not in c and "Content of" not in c:
                            print(p.split("/.agyhome/")[0], n, json.dumps(tc.get("args"))[:120], "||", " ".join(c.split())[:300])
                        break
# what does a served read_url_content look like
