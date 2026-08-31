from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_ROOT = ROOT / "src" / "content" / "blog"
LEGACY_ROOT = ROOT / "archive" / "hexo-export"


def extract(text: str, pattern: str, default: str = "") -> str:
    match = re.search(pattern, text, re.S)
    return match.group(1).strip() if match else default


def yaml_escape(value: str) -> str:
    value = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{value}"'


def build_markdown(post_path: Path) -> str:
    text = post_path.read_text(encoding="utf-8")
    title = extract(text, r"<title>(.*?) \| [^<]+</title>")
    description = extract(text, r'<meta name="description" content="(.*?)">')
    date = extract(text, r'article:published_time" content="([^"]+)"')[:10]
    updated = extract(text, r'article:modified_time" content="([^"]+)"')[:10]
    category_slug = ""
    category_name = ""
    parts = re.search(
        r'post-meta-item-text">分类于</span>\s*<span[^>]*>\s*<a href="/categories/([^/]+)/"[^>]*>\s*<span itemprop="name">(.*?)</span>',
        text,
        re.S,
    )
    if parts:
        category_slug = parts.group(1).strip()
        category_name = parts.group(2).strip()
    tag = extract(text, r'article:tag" content="([^"]+)"')
    tag_slug = extract(text, r'<a href="/tags/([^/]+)/"[^>]*rel="tag">')
    body = extract(
        text,
        r'<div class="post-body" itemprop="articleBody">\s*(.*?)\s*</div>\s*<footer class="post-footer">',
    )

    relative_permalink = "/" + post_path.parent.relative_to(LEGACY_ROOT).as_posix() + "/"
    is_featured = post_path.parent.name in {"intro-to-Git", "20200518LDR"}
    frontmatter = [
        "---",
        f"title: {yaml_escape(title)}",
        f"excerpt: {yaml_escape(description)}" if description else "",
        f"publishDate: {yaml_escape(date)}",
        f"updatedDate: {yaml_escape(updated)}" if updated else "",
        f"category: {yaml_escape(category_name)}" if category_name else "",
        f"categorySlug: {yaml_escape(category_slug)}" if category_slug else "",
        f"tag: {yaml_escape(tag)}" if tag else "",
        f"tagSlug: {yaml_escape(tag_slug)}" if tag_slug else "",
        f"permalink: {yaml_escape(relative_permalink)}",
        f"isFeatured: {'true' if is_featured else 'false'}",
        "---",
        "",
        body.strip(),
        "",
    ]

    return "\n".join(line for line in frontmatter if line != "")


def main() -> None:
    legacy_posts = sorted(LEGACY_ROOT.rglob("index.html"))
    legacy_posts = [
        path
        for path in legacy_posts
        if re.match(r"^\d{4}/\d{2}/\d{2}/[^/]+/index\.html$", path.relative_to(LEGACY_ROOT).as_posix())
    ]

    for legacy in legacy_posts:
        relative_dir = legacy.parent.relative_to(LEGACY_ROOT)
        destination = OUTPUT_ROOT / f"{relative_dir.name}.md"
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(build_markdown(legacy), encoding="utf-8")
        print(f"Wrote {destination.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
