# Setup checklist

## 1. Upload the files

Push to the `main` branch of `Nanda070/nanda070`:

- `README.md`
- `assets/dark.svg`, `assets/light.svg`, `assets/source-avatar.jpg`, `assets/portrait-*.npy`
- `tools/` (banner generator and logo masks)
- `.github/workflows/snake.yml` (unchanged)

## 2. Contribution snake

The snake images come from the `output` branch. If they do not show up: open the repository's **Settings → Actions → General**, set **Workflow permissions** to **Read and write**, then run **Actions → Generate Contribution Snake** once.

## 3. Check both themes

Switch GitHub between dark and light appearance and reload the profile. GitHub's image cache can serve an old banner for a while: bump `?v=1` in the three banner URLs in `README.md` after regenerating it.

## Regenerating the banner

From the repository root, with Pillow, NumPy and SciPy installed:

```bash
python tools/generate_profile_assets.py
```

To rebuild the logo masks (Python, TypeScript, PostgreSQL) run `tools/make_logo_masks.mjs` in a folder with `sharp` and `simple-icons` installed:

```bash
node make_logo_masks.mjs path/to/tools/logo-masks
```

The banner and generator are adapted from the profile of [yousefJooX](https://github.com/yousefJooX/yousefJooX). Logo shapes come from [Simple Icons](https://simpleicons.org) (CC0).
