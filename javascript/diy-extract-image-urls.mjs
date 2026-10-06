// Do-it-yourself image URL extractor (no API): img, largest srcset, picture, lazy-load attributes, og:image.
// Usage: npm i cheerio && node javascript/diy-extract-image-urls.mjs https://www.example.com/
import * as cheerio from 'cheerio';

const largest = (srcset = '') => srcset.split(/,\s+/).map((p) => p.trim().split(/\s+/))
    .filter(([u]) => u && !/^(data|blob):/.test(u))
    .map(([u, d = '1x']) => [u, (parseFloat(d) || 1) * (d.endsWith('w') ? 1 : 1000)])
    .sort((a, b) => b[1] - a[1])[0]?.[0];

export async function imageUrls(pageUrl) {
    const html = await (await fetch(pageUrl, { headers: { 'user-agent': 'Mozilla/5.0' } })).text();
    const $ = cheerio.load(html);
    const out = new Set();
    $('img').each((_, el) => {
        const $el = $(el);
        const src = largest($el.attr('srcset')) || largest($el.attr('data-srcset'))
            || $el.attr('data-src') || $el.attr('data-lazy-src') || $el.attr('src');
        if (src && !src.startsWith('data:')) out.add(new URL(src, pageUrl).href);
    });
    $('picture source[srcset]').each((_, el) => {
        const best = largest($(el).attr('srcset'));
        if (best) out.add(new URL(best, pageUrl).href);
    });
    const og = $('meta[property="og:image"]').attr('content');
    if (og) out.add(new URL(og, pageUrl).href);
    return [...out];
}

for (const u of await imageUrls(process.argv[2] || 'https://www.example.com/')) console.log(u);
