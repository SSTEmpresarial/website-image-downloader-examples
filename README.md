# Website Image Downloader — API & MCP examples

Download **all images from any website** (or just extract their URLs) with width, height, format, file size and alt text — as a ZIP, through a REST API, or as a tool for AI agents via MCP. Icons, sprites and tracking pixels are filtered out; `srcset`, `<picture>` and lazy-loaded images are handled.

This repo contains ready-to-run examples for the hosted [Website Image Downloader](https://apify.com/sste/website-image-downloader?utm_source=github&utm_medium=referral&utm_campaign=examples) (Apify Actor `sste/website-image-downloader`), plus dependency-light do-it-yourself extractors in Python and JavaScript.

| | |
|---|---|
| Store page | https://apify.com/sste/website-image-downloader |
| Docs & guides | https://website-image-downloader.pages.dev |
| MCP server | `https://mcp.apify.com?tools=sste/website-image-downloader` |
| Pricing | $0.20 per 1,000 images · $0.05 per 1,000 URLs in list mode · $0.001 per run |

## Quick start (cURL)

```bash
export APIFY_TOKEN=...   # Apify Console → Settings → Integrations
bash curl/download-all-images.sh https://www.example.com/
bash curl/list-image-urls.sh https://www.example.com/
```

## Python

```bash
pip install "apify-client>=3"
python python/download_images.py https://www.example.com/     # writes images.zip + images.csv
python python/diy_extract_image_urls.py https://www.example.com/  # no API, requests + BeautifulSoup
```

## JavaScript / Node.js

```bash
npm i apify-client cheerio
node javascript/download-images.mjs https://www.example.com/
node javascript/diy-extract-image-urls.mjs https://www.example.com/
```

## AI agents (MCP)

| Client | Config |
|---|---|
| Claude Desktop / Cursor / Windsurf | [`mcp/claude_desktop_config.json`](mcp/claude_desktop_config.json) |
| VS Code (`.vscode/mcp.json`) | [`mcp/vscode-mcp.json`](mcp/vscode-mcp.json) |
| Claude Code | `claude mcp add --transport http website-image-downloader "https://mcp.apify.com?tools=sste/website-image-downloader"` |
| Any client (stdio) | `npx -y @apify/actors-mcp-server --tools sste/website-image-downloader` |

Example prompts: [`mcp/prompts.md`](mcp/prompts.md). Registry entry: [`server.json`](server.json) (`io.github.SSTEmpresarial/website-image-downloader`).

## What the hosted tool handles

- largest `srcset` / `<picture>` candidate, lazy-load attributes (`data-src`, `data-srcset`, `data-lazy-src`, `data-original`, `data-bg`), `<noscript>`, CSS backgrounds, `og:image`
- real width/height/format from file bytes; filters by size, format and URL text; soft-404 detection; SHA-256 dedupe
- modes: `download` (ZIP + rows), `inspect` (rows only), `list` (URLs only)
- same-site crawling (depth 1–3), spending caps

Guides: [download all images from a website](https://website-image-downloader.pages.dev/guides/download-all-images-from-website/) · [extract image URLs](https://website-image-downloader.pages.dev/guides/extract-image-urls-from-webpage/) · [filter icons & tracking pixels](https://website-image-downloader.pages.dev/guides/filter-icons-tracking-pixels/) · [srcset & lazy loading](https://website-image-downloader.pages.dev/guides/srcset-lazy-loaded-images/) · [Shopify](https://website-image-downloader.pages.dev/guides/shopify-image-downloader/)

Only download images you have the right to use. MIT licensed examples.
