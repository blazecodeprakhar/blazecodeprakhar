#!/usr/bin/env python3
"""Generate an animated GitHub-streak SVG (squares light up one by one).
Reads from data/contributions.json (produced by fetch_contributions.py) to guarantee sync.
Usage: python generate_streak_svg.py [username] [output.svg]
"""
import sys, json, os, datetime, urllib.request

USER = sys.argv[1] if len(sys.argv) > 1 else "blazecodeprakhar"
OUT  = sys.argv[2] if len(sys.argv) > 2 else "streak.svg"

HERE = os.path.dirname(os.path.abspath(__file__))
DATA_JSON = os.path.join(HERE, "..", "data", "contributions.json")


def level_for(count):
    if count == 0:
        return 0
    if count <= 5:
        return 1
    if count <= 15:
        return 2
    if count <= 30:
        return 3
    return 4


def get_data(user):
    # Primary: local data/contributions.json built from fetch_contributions.py
    if os.path.exists(DATA_JSON):
        try:
            raw = json.load(open(DATA_JSON))
            contribs = []
            for d in raw.get("days", []):
                contribs.append({
                    "date": d["date"],
                    "count": d["count"],
                    "level": d.get("level", level_for(d["count"]))
                })
            total = raw.get("total_contributions", sum(c["count"] for c in contribs))
            return contribs, total
        except Exception as e:
            print(f"Error reading {DATA_JSON}: {e}")

    # Secondary: fetch using fetch_contributions module directly
    try:
        import fetch_contributions
        days = fetch_contributions.fetch_days()
        data = fetch_contributions.build_data(days)
        contribs = [{"date": d["date"], "count": d["count"], "level": level_for(d["count"])} for d in data["days"]]
        return contribs, data["total_contributions"]
    except Exception as e:
        print(f"Fetch module failed ({e}), trying fallback API...")

    # Tertiary fallback: jogruber API
    url = f"https://github-contributions-api.jogruber.de/v4/{user}?y=last"
    try:
        with urllib.request.urlopen(url, timeout=25) as r:
            raw = json.loads(r.read().decode())
            return raw["contributions"], raw["total"]["lastYear"]
    except Exception as e:
        here = os.path.join(HERE, "contrib.json")
        if os.path.exists(here):
            print("API failed (%s); using local contrib.json" % e)
            raw = json.load(open(here))
            return raw["contributions"], raw["total"]["lastYear"]
        raise


contribs, total = get_data(USER)

# ---- layout ----
CELL, GAP, RAD, LEFT, TOP = 13, 3, 2.5, 34, 24
COLORS = ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353"]
FLASH = "#b4ffaa"
GRAY = "#7d8590"
MONTHS = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

n = len(contribs)
NW = (n + 6) // 7
W = LEFT + NW*(CELL+GAP) + 6
H = TOP + 7*(CELL+GAP) + 22

# timing (seconds)
REVEAL, DUR = 3.6, 0.55
maxorder = (NW-1) + 6*0.55

rects, labels = [], []
sd = datetime.date.fromisoformat(contribs[0]["date"])
last_m = None
for wk in range(NW):
    d = sd + datetime.timedelta(days=wk*7)
    if d.month != last_m:
        last_m = d.month
        labels.append(f'<text class="lbl" x="{LEFT+wk*(CELL+GAP)}" y="{TOP-8}">{MONTHS[d.month-1]}</text>')
for name, r in [("Mon",1),("Wed",3),("Fri",5)]:
    labels.append(f'<text class="lbl" x="2" y="{TOP+r*(CELL+GAP)+CELL-2}">{name}</text>')

for i, c in enumerate(contribs):
    wk, row, lvl = i//7, i%7, c["level"]
    x = LEFT + wk*(CELL+GAP); y = TOP + row*(CELL+GAP)
    delay = round((wk + row*0.55)/maxorder * REVEAL, 3)
    cls = "c g" if lvl >= 1 else "c e"
    rects.append(
        f'<rect class="{cls}" x="{x}" y="{y}" width="{CELL}" height="{CELL}" rx="{RAD}" '
        f'fill="{COLORS[lvl]}" style="animation-delay:{delay}s"/>'
    )

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="-apple-system,Segoe UI,Helvetica,Arial,sans-serif">
<style>
  text.lbl {{ fill:{GRAY}; font-size:13px; font-weight:600; }}
  text.total {{ fill:#e6edf3; font-size:15px; font-weight:700; }}
  .c {{ transform-box:fill-box; transform-origin:center; opacity:0; animation:pop {DUR}s ease-out both; }}
  .g {{ animation:pop {DUR}s ease-out both, flash {DUR+0.15}s ease-out both; }}
  @keyframes pop {{ 0%{{opacity:0;transform:scale(.2)}} 60%{{opacity:1;transform:scale(1.1)}} 100%{{opacity:1;transform:scale(1)}} }}
  @keyframes flash {{ 0%{{filter:brightness(2.4)}} 45%{{filter:brightness(2.4)}} 100%{{filter:brightness(1)}} }}
  @media (prefers-reduced-motion: reduce) {{ .c {{ opacity:1 !important; animation:none !important; }} }}
</style>
<rect width="{W}" height="{H}" fill="none"/>
{''.join(labels)}
{''.join(rects)}
<text class="total" x="{LEFT}" y="{H-6}">{total:,} contributions in the last year</text>
</svg>'''

open(OUT, "w").write(svg)
print(f"Wrote {OUT}: {n} days, {total:,} contributions, {len(svg)//1024} KB")

