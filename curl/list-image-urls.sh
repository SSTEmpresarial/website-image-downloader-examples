#!/usr/bin/env bash
# Lists every image URL on a page without downloading (mode=list, $0.05 per 1,000 URLs).
# Usage: APIFY_TOKEN=... bash curl/list-image-urls.sh https://www.example.com/
set -euo pipefail
URL="${1:?page URL}"
curl -sS -X POST "https://api.apify.com/v2/acts/sste~website-image-downloader/run-sync-get-dataset-items?fields=imageUrl,alt,foundIn" \
  -H "Authorization: Bearer $APIFY_TOKEN" -H "Content-Type: application/json" \
  -d "{\"startUrls\":[{\"url\":\"$URL\"}],\"mode\":\"list\",\"maxImages\":1000}"
echo
