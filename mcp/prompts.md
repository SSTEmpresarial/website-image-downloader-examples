# Example prompts for agents (MCP)

Server: `https://mcp.apify.com?tools=sste/website-image-downloader` · tool: `sste--website-image-downloader`

- Download all product images larger than 600 px from https://shop.example.com/collections/sale and give me the ZIP link.
- List every image on https://example.com/blog/post with its alt text and flag the ones without alt text.
- Which images on https://example.com/ are larger than 500 KB? Suggest which ones to convert to WebP.
- Get the og:image of each of these URLs: ...
- Collect all images of at least 1200x800 from https://example.com/press, then summarize what they show from their alt text.

Tips: use `mode: "list"` or `"inspect"` when files are not needed; keep `maxImages` small; raise `minWidth`/`minHeight` to skip thumbnails.
