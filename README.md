# Carlos Luis Rojas Aragonés Personal Website

Static personal brand site built with [Astro](https://astro.build). Configured to serve from `/` (e.g. `https://crojasaragonez.github.io/` or a custom domain).

## Develop

```bash
npm install
npm run dev
```

Open the URL Astro prints (root `/`).

## Build

```bash
npm run build
npm run preview
```

## Content

- Site copy, experience & metrics: `src/data/site.ts`
- About page: `src/pages/about.astro`
- Blog posts: `src/content/blog/`
- Talks: `src/content/talks/`
- Images (processed by `astro:assets`): `src/assets/`
- Static files served as-is: `public/` (`resume.pdf`, `og.jpg`, favicons, `robots.txt`)

Images must live in `src/assets/` and be imported, so Astro can emit AVIF/WebP
variants with content-hashed filenames. Files in `public/` are served untouched.

## Social share card

`public/og.jpg` (1200×630) is the site-wide Open Graph image, referenced by
`BaseLayout.astro`. Pass `image="foo.jpg"` to `BaseLayout` to override per page.

## Deploy

`.github/workflows/deploy.yml` builds and publishes to GitHub Pages on every
push to `main`. Pull requests are built but never published, so a broken build
cannot reach the live site.

### One-time setup

> [!IMPORTANT]
> **The repository must be named `crojasaragonez.github.io`.** GitHub Pages
> serves any other repository under `/<repo-name>/`, but `astro.config.mjs`
> declares the site at the root — so under a different name every link, asset
> and canonical URL would 404.

1. **Settings → General → Repository name** → `crojasaragonez.github.io`
2. **Settings → Pages → Source** → **GitHub Actions**
3. Point your local clone at the new name (GitHub redirects the old URL, but
   don't depend on it):

   ```bash
   git remote set-url origin git@github.com:crojasaragonez/crojasaragonez.github.io.git
   ```

### Changing the URL later

`site` in `astro.config.mjs` and the `Sitemap:` line in `public/robots.txt` both
hardcode `https://crojasaragonez.github.io`. To move to a custom domain, update
both and add `public/CNAME` containing the bare domain.

> [!CAUTION]
> Serving from a sub-path (setting `base` in `astro.config.mjs`) needs code
> changes first. Components build links as `` `${base}about/` ``, and Astro's
> `BASE_URL` has **no** trailing slash once `base` is set — producing
> `/personal_websiteabout/`. Normalise `BASE_URL` everywhere before setting it.
