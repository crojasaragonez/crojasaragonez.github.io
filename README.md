# Carlos Luis Rojas Aragonés — Personal Website

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

- Site copy & metrics: `src/data/site.ts`
- Blog posts: `src/content/blog/`
- Talks: `src/content/talks/`
- Testimonials: `src/content/testimonials/`
- Résumé PDF: `public/resume.pdf`

## Deploy (manual)

`.github/workflows/deploy.yml` is ready. After you push to GitHub, set **Settings → Pages → Source** to **GitHub Actions**.
