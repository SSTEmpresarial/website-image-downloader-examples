#!/usr/bin/env bash
# Downloads all images (>= 200x200 px) from a page; prints the image list and the ZIP location.
# Usage: APIFY_TOKEN=... bash curl/download-all-images.sh https://www.example.com/
set -euo pipefail
URL="${1:?page URL}"
curl -sS -X POST "https://api.apify.com/v2/acts/sste~website-image-downloader/run-sync-get-dataset-items" \
  -H "Authorization: Bearer $APIFY_TOKEN" -H "Content-Type: application/json" \
  -d "{\"startUrls\":[{\"url\":\"$URL\"}],\"minWidth\":200,\"minHeight\":200,\"maxImages\":200}"
echo
echo "The files are in the run's images.zip (Apify Console → Runs → Output), or use python/download_images.py to save it."
