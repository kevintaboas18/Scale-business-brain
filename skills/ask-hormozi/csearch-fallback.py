#!/usr/bin/env python3
"""Grep-based fallback search over the local MoreMozi segment corpus.
Citations are read from each segment's front-matter timestamp_url -- never generated.
Usage: csearch.py "phrase one" "phrase two" ... [--limit N]
Scoring: count of distinct query phrases present (case-insensitive), then total hits.
"""
import os, re, sys, glob

ROOT = "/home/user/Scale-business-brain/corpus/segments"
STOP = set("the a an and or of to in is it that this for with you your we our i on be as at".split())

def parse(path):
    try:
        txt = open(path, encoding="utf-8", errors="replace").read()
    except Exception:
        return None
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", txt, re.S)
    if not m:
        return None
    fm, body = m.group(1), m.group(2)
    meta = {}
    for line in fm.split("\n"):
        mm = re.match(r'^(\w+):\s*"?(.*?)"?\s*$', line)
        if mm:
            meta[mm.group(1)] = mm.group(2)
    return meta, body

def main():
    args = [a for a in sys.argv[1:]]
    limit = 6
    if "--limit" in args:
        i = args.index("--limit"); limit = int(args[i+1]); args = args[:i] + args[i+2:]
    phrases = [p.lower() for p in args if p.strip()]
    if not phrases:
        print("no phrases"); return
    results = []
    for path in glob.glob(os.path.join(ROOT, "*", "*.md")):
        p = parse(path)
        if not p: continue
        meta, body = p
        low = body.lower()
        hits = {ph: low.count(ph) for ph in phrases}
        distinct = sum(1 for ph in phrases if hits[ph] > 0)
        if distinct == 0: continue
        total = sum(hits.values())
        results.append((distinct, total, meta, body, path, hits))
    results.sort(key=lambda r: (-r[0], -r[1]))
    seen_ep = {}
    out = []
    for distinct, total, meta, body, path, hits in results:
        ep = meta.get("episode_id", "")
        if seen_ep.get(ep, 0) >= 1:   # max 1 segment per video
            continue
        seen_ep[ep] = seen_ep.get(ep, 0) + 1
        out.append((distinct, total, meta, body, hits))
        if len(out) >= limit: break
    for distinct, total, meta, body, hits in out:
        print("=" * 78)
        print(f"TITLE: {meta.get('title','?')}")
        print(f"URL:   {meta.get('timestamp_url','?')}")
        print(f"SCORE: phrases={distinct}/{len(phrases)} hits={total} -> {hits}")
        print("-" * 78)
        # print the sentences around the strongest phrase
        best = max((h for h in hits.items() if h[1] > 0), key=lambda x: x[1])[0]
        idx = body.lower().find(best)
        s = max(0, idx - 900); e = min(len(body), idx + 1300)
        print(body[s:e].strip())
        print()

main()
