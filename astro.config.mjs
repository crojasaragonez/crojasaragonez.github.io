// @ts-check
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

// https://astro.build/config
export default defineConfig({
  // NOTE: canonical URLs, OG tags and the sitemap all derive from this.
  // Change it here (and in public/robots.txt) when moving to a custom domain.
  site: 'https://crojasaragonez.github.io',
  integrations: [sitemap()],
});
