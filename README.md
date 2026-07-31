# Carlos Luis Rojas Aragonés — Personal Website

Static personal brand site built with [Astro](https://astro.build), deployed to GitHub Pages.

**Live URL:** https://crojasaragonez.github.io/website/

## Develop

```bash
npm install
npm run dev
```

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

## Deploy

Pushes to `main` deploy via `.github/workflows/deploy.yml`. In the GitHub repo, set **Settings → Pages → Source** to **GitHub Actions**.
