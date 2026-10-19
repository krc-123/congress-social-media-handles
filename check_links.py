"""Check that every profile link in the handle CSVs still resolves.

Usage: python check_links.py [data/house_instagram.csv ...]
With no arguments it checks all four handle files. Prints one line per
link that fails, and a summary at the end. One request a second, on purpose.
"""
import csv
import sys
import time

import requests

FILES = [
    "data/house_instagram.csv",
    "data/house_x.csv",
    "data/senate_instagram.csv",
    "data/senate_x.csv",
]

HEADERS = {"User-Agent": "Mozilla/5.0 (link check for a public handle list)"}


def check(url):
    try:
        r = requests.get(url, headers=HEADERS, timeout=15, allow_redirects=True)
        return r.status_code
    except requests.RequestException as e:
        return type(e).__name__


def main(paths):
    failed = 0
    total = 0
    for path in paths:
        with open(path, newline="", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                url = row.get("profile_link", "").strip()
                if not url.startswith("http"):
                    continue
                total += 1
                status = check(url)
                if status != 200:
                    failed += 1
                    print(f"{path}\t{row.get('member')}\t{url}\t{status}")
                time.sleep(1)
    print(f"checked {total} links, {failed} did not return 200")


if __name__ == "__main__":
    main(sys.argv[1:] or FILES)
