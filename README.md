# Yuqi Yan

Personal website built with Astro.

## Local development

1. Use Node.js `22.12.0` or newer.
2. Run `npm install`.
3. Run `npm run dev`.

## Project structure

- `src/content.config.ts` defines the `blog` and `pages` content collections.
- `src/content/blog/` contains blog posts.
- `src/content/pages/` contains standalone content pages such as `about` and `resume`.
- `src/data/site-config.ts` contains site title, navigation, hero content, social links, and pagination settings.
- `src/pages/` contains the Astro routes.
- `public/` contains static files.
- `archive/hexo-export/` contains the legacy Hexo output kept only for recovery and migration reference.
