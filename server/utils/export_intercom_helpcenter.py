#!/usr/bin/env python
# -*- coding: utf-8-*-

import json
import os
import re
import time

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md

main_url = "https://intercom.help/finazilla/fi/"


def fetch_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None


def parse_collection(collection_url):
    html = fetch_url(collection_url)
    if not html:
        return []

    soup = BeautifulSoup(html, "html.parser")
    articles = []

    for article_link in soup.find_all("a", href=lambda x: x and "/articles/" in x):
        article_url = article_link["href"]
        article_html = fetch_url(article_url)
        if not article_html:
            continue

        article_soup = BeautifulSoup(article_html, "html.parser")
        title = article_soup.find("h1")
        content = article_soup.find("article")

        if title and content:
            articles.append(
                {
                    "title": title.get_text(strip=True),
                    "url": article_url,
                    "content_html": content.prettify(),
                    "content_md": md(str(content), heading_style="ATX"),
                }
            )

    return articles


def scrape_help_center():
    html = fetch_url(main_url)
    if not html:
        return

    soup = BeautifulSoup(html, "html.parser")
    collections = []

    for card in soup.find_all("a", class_="collection-link"):
        collection_url = card["href"]
        collection_name = card.find("div", class_=lambda x: x and "font-semibold" in x)
        if collection_name:
            collection_name = collection_name.get_text(strip=True)
        else:
            collection_name = "Unnamed Collection"

        print(f"Processing Collection: {collection_name}")
        articles = parse_collection(collection_url)
        collections.append(
            {"name": collection_name, "url": collection_url, "articles": articles}
        )

        time.sleep(1)  # Be nice to the server

    return collections


def generate_markdown_only(article):
    markdown_content = ""
    markdown_content += f"## {article['title']}\n\n"
    markdown_content += article["content_md"] + "\n\n"
    return markdown_content


def generate_ultra_compact(article):
    compact_content = ""
    compact_content += f"## {article['title']}\n\n"
    content = article["content_md"]
    # Remove URLs
    content = re.sub(
        r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+",
        "",
        content,
    )
    # Remove image-like Markdown patterns starting with [![](
    content = re.sub(r"\[!\[\]\(.*?\)", "", content)
    # Remove specific Kuva labels within backticks
    content = re.sub(r"`Kuva:.*?`", "", content)
    # Remove image references
    content = re.sub(r"!\[.*?\]\(.*?\)", "", content)
    # Remove empty lines
    content = re.sub(r"\n\s*\n", "\n\n", content)
    content += f"\n\nartikkelin osoite on {article['url']}"
    compact_content += content.strip() + "\n\n"
    return compact_content


def main():
    help_center_data = scrape_help_center()

    for collection in help_center_data:
        for article in collection["articles"]:

            markdown_content = generate_ultra_compact(article)
            title = article["title"]
            safe_title = re.sub(r'[<>:"/\\|?*]', '_', title)

            collection_name = collection["name"]
            safe_collection_name = re.sub(r'[<>:"/\\|?*]', '_', collection_name)

            output_directory = "../articles"
            os.makedirs(output_directory, exist_ok=True)
            file_path = os.path.join(output_directory, f"{safe_collection_name} - {safe_title}.md")

            with open(file_path, "w", encoding="utf-8") as f:
                f.write(markdown_content)
                print(f"Markdown-only content saved to {safe_title}")


if __name__ == "__main__":
    main()