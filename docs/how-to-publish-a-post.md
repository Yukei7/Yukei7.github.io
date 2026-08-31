# How To Publish A New Post

## 1. Create the post file

Add a new Markdown or MDX file under `src/content/blog/`.

The easiest option is to start from [docs/post-template.md](/home/yukei/git/Yukei7.github.io/docs/post-template.md).

Example:

```md
---
title: "My New Post"
excerpt: "Short summary used on listing pages."
publishDate: "2026-08-31"
updatedDate: "2026-08-31"
category: "CS"
categorySlug: "CS"
tag: "Astro"
tagSlug: "Astro"
permalink: "/2026/08/31/my-new-post/"
isFeatured: false
---

Write the post here.
```

For new posts, prefer normal Markdown instead of pasted legacy HTML from the old site export.

## 2. Keep the permalink stable

If you want a custom public URL, set `permalink`. If you omit it, the post will still be available under the standard `/blog/[id]/` route.

## 3. Add assets if needed

If the post needs images or downloads, put them under `public/` and link them with absolute paths such as:

```md
![Example](/images/example.png)
```

If you want to keep the old date-folder style, that also works:

```md
![Example](/2026/08/31/my-new-post/example.png)
```

## 4. Math syntax

For new posts, use MathJax-friendly Markdown text:

```md
Inline math: \(a^2 + b^2 = c^2\)

Display math:

\[
\int_0^1 x^2 \, dx = \frac{1}{3}
\]
```

Do not use legacy exported fragments like:

```html
<script type="math/tex; mode=display">...</script>
```

## 5. Update featured status if desired

Set `isFeatured: true` if you want the post to appear in the featured section on the homepage.

## 6. Run local checks

```bash
npm run dev
```

Verify:

- the post page loads
- the post appears on `/blog/`
- the tag page includes it if `tag` and `tagSlug` are set
- images and math render correctly

## 7. Build before publishing

```bash
npm run build
npm run preview
```

## 8. Publish

Commit and push to `master`. GitHub Pages deployment is handled by `.github/workflows/deploy.yml`.
