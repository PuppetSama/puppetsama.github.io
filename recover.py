import os
from bs4 import BeautifulSoup
from markdownify import markdownify as md
import yaml
from pathlib import Path

ROOT = "."
OUTPUT = "content/posts"

os.makedirs(OUTPUT, exist_ok=True)

def extract_post(html_path):
    with open(html_path, "r", encoding="utf-8") as f:
        html = f.read()

    soup = BeautifulSoup(html, "html.parser")

    # ===== 标题 =====
    title = "Untitled"

    if soup.title:
        title = soup.title.text.strip()

    h1 = soup.find("h1")
    if h1:
        title = h1.text.strip()

    # ===== 日期 =====
    parts = Path(html_path).parts

    year = "2020"
    month = "01"
    day = "01"

    for i, p in enumerate(parts):
        if p.isdigit() and len(p) == 4:
            year = p

            if i + 1 < len(parts):
                month = parts[i + 1]

            break

    date = f"{year}-{month}-01"

    # ===== 正文 =====
    article = None

    candidates = [
        "article",
        ".post-content",
        ".entry-content",
        ".content",
        ".post",
    ]

    for selector in candidates:
        if selector.startswith("."):
            article = soup.select_one(selector)
        else:
            article = soup.find(selector)

        if article:
            break

    if not article:
        article = soup.body

    content_html = str(article)

    markdown = md(content_html)

    # ===== frontmatter =====
    frontmatter = {
        "title": title,
        "date": date,
        "draft": False,
        "url": "/" + "/".join(parts[-4:-1]) + "/",
    }

    md_text = "---\n"
    md_text += yaml.dump(frontmatter, allow_unicode=True)
    md_text += "---\n\n"
    md_text += markdown

    slug = parts[-2]

    output_path = os.path.join(OUTPUT, f"{slug}.md")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(md_text)

    print(f"Recovered: {output_path}")

def scan():
    for root, dirs, files in os.walk(ROOT):
        for file in files:
            if file == "index.html":
                path = os.path.join(root, file)

                # 跳过首页
                if root == ".":
                    continue

                # 只处理文章目录
                if any(part.isdigit() and len(part) == 4 for part in Path(path).parts):
                    extract_post(path)

scan()

print("Done.")
