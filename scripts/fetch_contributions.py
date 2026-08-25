#!/usr/bin/env python3
"""
Scrape real daily contribution counts from GitHub's public, unauthenticated
contributions endpoint (the same fragment the profile page itself uses) and
write data/contributions.json with the raw days plus derived stats
(current streak, longest streak, best day, monthly totals).

No token, no auth, no GraphQL -- just the public HTML GitHub already serves.
Run daily by .github/workflows/update-profile-art.yml or via local auto-update scripts.
"""
import datetime
import json
import os
import re
import sys
import time

import requests
from bs4 import BeautifulSoup

USERNAME = os.environ.get("GH_PROFILE_USER", "blazecodeprakhar")
BASE_URL = f"https://github.com/users/{USERNAME}/contributions"
OUT_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "contributions.json")


def fetch_days():
    # Cache-busting URL parameter + strict no-cache headers to get live data from GitHub
    cache_buster = int(time.time())
    url = f"{BASE_URL}?cb={cache_buster}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "Cache-Control": "no-cache, no-store, must-revalidate",
        "Pragma": "no-cache",
        "Expires": "0",
    }
    
    resp = requests.get(url, headers=headers, timeout=30)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    cells = soup.select("td.ContributionCalendar-day")
    if not cells:
        print("no calendar cells found -- github markup may have changed", file=sys.stderr)
        sys.exit(1)

    days = []
    for td in cells:
        date = td.get("data-date")
        if not date:
            continue
        
        td_id = td.get("id")
        aria_desc = td.get("aria-describedby")
        
        # Strategy 1: tool-tip linked by 'for' attribute matching td's id
        tooltip_el = soup.find("tool-tip", attrs={"for": td_id}) if td_id else None
        
        # Strategy 2: tool-tip or element referenced by aria-describedby
        if not tooltip_el and aria_desc:
            tooltip_el = soup.find(id=aria_desc)
            
        # Strategy 3: child element within td
        if not tooltip_el:
            tooltip_el = td.find("tool-tip")

        text = ""
        if tooltip_el:
            text = tooltip_el.get_text(strip=True)
        elif td.get("aria-label"):
            text = td.get("aria-label")

        if td.get("data-count") is not None:
            try:
                count = int(td.get("data-count"))
                days.append({"date": date, "count": count})
                continue
            except ValueError:
                pass

        if not text or re.search(r"no contributions", text, re.I):
            count = 0
        else:
            # Handle comma-separated numbers (e.g. "1,048 contributions")
            m = re.search(r"([\d,]+)\s+contribution", text, re.I)
            if not m:
                m = re.search(r"([\d,]+)", text)
            count = int(m.group(1).replace(",", "")) if m else 0

        days.append({"date": date, "count": count})

    days.sort(key=lambda d: d["date"])
    return days


def compute_current_streak(days):
    if not days:
        return 0, None, None

    idx = len(days) - 1
    # If today's count is 0 (day just started in user's timezone), look back one day so streak doesn't break
    if idx >= 0 and days[idx]["count"] == 0:
        idx -= 1

    streak = 0
    end_idx = idx
    while idx >= 0 and days[idx]["count"] > 0:
        streak += 1
        idx -= 1

    if streak == 0 or end_idx < 0:
        return 0, None, None
    start_idx = idx + 1
    return streak, days[start_idx]["date"], days[end_idx]["date"]


def compute_longest_streak(days):
    if not days:
        return 0, None, None

    longest = run = 0
    longest_start = longest_end = None
    run_start_idx = None

    for i, d in enumerate(days):
        if d["count"] > 0:
            if run == 0:
                run_start_idx = i
            run += 1
            if run > longest:
                longest = run
                longest_start = days[run_start_idx]["date"]
                longest_end = days[i]["date"]
        else:
            run = 0

    return longest, longest_start, longest_end


def build_data(days):
    if not days:
        return {}

    total = sum(d["count"] for d in days)
    active_days = sum(1 for d in days if d["count"] > 0)
    best = max(days, key=lambda d: d["count"]) if days else {"date": None, "count": 0}
    cur_len, cur_start, cur_end = compute_current_streak(days)
    long_len, long_start, long_end = compute_longest_streak(days)

    monthly = {}
    for d in days:
        key = d["date"][:7]
        monthly[key] = monthly.get(key, 0) + d["count"]
    monthly_list = [{"month": k, "total": v} for k, v in sorted(monthly.items())]

    return {
        "username": USERNAME,
        "generated_at": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "range": {"start": days[0]["date"], "end": days[-1]["date"]},
        "total_contributions": total,
        "active_days": active_days,
        "avg_per_active_day": round(total / active_days, 1) if active_days else 0,
        "current_streak": {"length": cur_len, "start": cur_start, "end": cur_end},
        "longest_streak": {"length": long_len, "start": long_start, "end": long_end},
        "best_day": {"date": best["date"], "count": best["count"]},
        "monthly": monthly_list,
        "days": days,
    }


if __name__ == "__main__":
    days = fetch_days()
    data = build_data(days)
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w") as f:
        json.dump(data, f, indent=2)
    print(f"wrote {OUT_PATH}: {data['total_contributions']} contributions, "
          f"range {data['range']['start']} -> {data['range']['end']}, "
          f"current streak {data['current_streak']['length']}, "
          f"longest streak {data['longest_streak']['length']}, "
          f"best day {data['best_day']['count']} on {data['best_day']['date']}")

