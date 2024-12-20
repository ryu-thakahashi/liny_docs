import os
import re
from pathlib import Path

import markdown

dir_path = Path(__file__).resolve().parents[1]
manual_path = dir_path / "manuals"
html_path = manual_path / "html"


def read_markdown_text(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        raw_text = file.read()
    return format_markdown_text(raw_text)


def css_link_tag():
    css_files = os.listdir(manual_path / "css")
    css_links = []
    for css_file in css_files:
        if not css_file.endswith(".css"):
            continue
        css_links.append(f'<link rel="stylesheet" href="../css/{css_file}">')

    return "\n".join(css_links)


def modify_img_path(md_text):
    return re.sub("image/", r"../image/", md_text)


def format_markdown_text(markdown_text: str):
    md_text = css_link_tag() + "\n" + markdown_text
    modified_img_path_md = modify_img_path(md_text)
    return modified_img_path_md


def add_ToC_to_html(html_text):
    ToC_dict = {
        "<!-- vscode-markdown-toc -->": "<div class='toc-002'><div>目次</div>",
        "<!-- /vscode-markdown-toc -->": "</div>",
    }
    for key, value in ToC_dict.items():
        html_text = html_text.replace(key, value)
    return html_text


def write_html_text(file_path, html_text):
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(add_ToC_to_html(html_text))


manual_files = os.listdir(manual_path)
for manual_file in manual_files:
    if not manual_file.endswith(".md"):
        continue

    manual_file_path = manual_path / manual_file
    markdown_text = read_markdown_text(manual_file_path)

    html_text = markdown.markdown(markdown_text)

    res_file_name = manual_file[:-3] + ".html"
    html_file_path = html_path / res_file_name
    write_html_text(html_file_path, html_text)
