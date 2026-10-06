"""Download all images from one or more pages with the hosted Website Image Downloader.

Usage:  APIFY_TOKEN=... python python/download_images.py https://www.example.com/ [more URLs]
Writes images.zip (all files) and images.csv (url, width, height, format, bytes, alt, page).
"""
import csv
import os
import sys

from apify_client import ApifyClient  # pip install "apify-client>=3"

urls = sys.argv[1:] or ["https://www.example.com/"]
client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("sste/website-image-downloader").call(run_input={
    "startUrls": [{"url": u} for u in urls],
    "minWidth": 200,
    "minHeight": 200,
    "urlMustNotContain": ["logo", "icon", "sprite"],
    "maxImages": 500,
})

rows = list(client.dataset(run.default_dataset_id).iterate_items())
with open("images.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["imageUrl", "width", "height", "format", "bytes", "alt", "pageUrl"])
    for r in rows:
        w.writerow([r["imageUrl"], r["width"], r["height"], r["format"], r["bytes"], r.get("alt") or "", r.get("pageUrl") or ""])

record = client.key_value_store(run.default_key_value_store_id).get_record_as_bytes("images.zip")
if record:
    with open("images.zip", "wb") as f:
        f.write(record["value"])
print(f"{len(rows)} images -> images.csv" + (" + images.zip" if record else ""))
