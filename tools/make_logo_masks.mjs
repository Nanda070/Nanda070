// Renders brand silhouettes (white on transparent, 512×512) used by generate_profile_assets.py.
// Run from a folder with `sharp` and `simple-icons` installed:  node make_logo_masks.mjs <out-dir>
import sharp from 'sharp';
import { siPython, siTypescript, siPostgresql } from 'simple-icons';
import path from 'node:path';

const out = process.argv[2] ?? 'logo-masks';
const icons = { python: siPython, typescript: siTypescript, postgresql: siPostgresql };
for (const [name, icon] of Object.entries(icons)) {
  const svg = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="512" height="512"><path fill="#fff" d="${icon.path}"/></svg>`;
  await sharp(Buffer.from(svg)).png().toFile(path.join(out, `${name}.png`));
  console.log('wrote', name);
}
