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

> [!WARNING]
> There is **no** `.github/workflows/deploy.yml` in this repo yet, so nothing
> deploys automatically. Add a workflow using `withastro/action`, then set
> **Settings → Pages → Source** to **GitHub Actions**.

Note that `site` in `astro.config.mjs` and the `Sitemap:` line in
`public/robots.txt` both hardcode `https://crojasaragonez.github.io` — update
both when moving to a custom domain.
