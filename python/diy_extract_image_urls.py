"""Do-it-yourself image URL extractor (no API): img, largest srcset, picture, lazy-load attributes, og:image.

Usage:  pip install requests beautifulsoup4 && python python/diy_extract_image_urls.py https://www.example.com/
Limitations vs the hosted tool: no size filtering, no dedupe by content, no CSS backgrounds, no crawling.
"""
import sys
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup


def largest_from_srcset(srcset):
    best, best_score = None, -1
    for part in (srcset or "").split(", "):
        bits = part.strip().split()
        if not bits or bits[0].startswith(("data:", "blob:")):
            continue
        desc = bits[1] if len(bits) > 1 else "1x"
        try:
            score = float(desc[:-1]) * (1 if desc.endswith("w") else 1000)
        except ValueError:
            score = 1000
        if score > best_score:
            best, best_score = bits[0], score
    return best


def image_urls(page_url):
    html = requests.get(page_url, headers={"User-Agent": "Mozilla/5.0"}, timeout=30).text
    soup = BeautifulSoup(html, "html.parser")
    found = []
    for img in soup.find_all("img"):
        src = (largest_from_srcset(img.get("srcset")) or largest_from_srcset(img.get("data-srcset"))
               or img.get("data-src") or img.get("data-lazy-src") or img.get("data-original") or img.get("src"))
        if src and not src.startswith("data:"):
            found.append(urljoin(page_url, src))
    for source in soup.select("picture source[srcset]"):
        best = largest_from_srcset(source["srcset"])
        if best:
            found.append(urljoin(page_url, best))
    og = soup.find("meta", property="og:image")
    if og and og.get("content"):
        found.append(urljoin(page_url, og["content"]))
    return list(dict.fromkeys(found))


if __name__ == "__main__":
    for u in image_urls(sys.argv[1] if len(sys.argv) > 1 else "https://www.example.com/"):
        print(u)
