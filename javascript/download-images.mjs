// Download all images from a page with the hosted Website Image Downloader; saves images.zip.
// Usage: APIFY_TOKEN=... node javascript/download-images.mjs https://www.example.com/
import { writeFileSync } from 'node:fs';
import { ApifyClient } from 'apify-client'; // npm i apify-client

const urls = process.argv.slice(2);
const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
const run = await client.actor('sste/website-image-downloader').call({
    startUrls: (urls.length ? urls : ['https://www.example.com/']).map((url) => ({ url })),
    minWidth: 200,
    minHeight: 200,
    maxImages: 500,
});
const { items } = await client.dataset(run.defaultDatasetId).listItems();
for (const i of items) console.log(`${i.width}x${i.height}\t${i.format}\t${i.imageUrl}`);
const zip = await client.keyValueStore(run.defaultKeyValueStoreId).getRecord('images.zip', { buffer: true });
if (zip) writeFileSync('images.zip', zip.value);
console.log(`${items.length} images${zip ? ' -> images.zip' : ''}`);
