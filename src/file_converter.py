import os

import markdown

from config import CSS_DIR


class FileConverter:
    def __init__(self, md_text: str):
        self.md_text = md_text

    @property
    def converted_html(self):
        if not hasattr(self, "html"):
            self.convert()
        return self.html

    @property
    def css_files(self):
        return os.listdir(CSS_DIR)

    def add_css_tag(self):
        css_links = []
        for css_file in self.css_files:
            css_links.append(f'<link rel="stylesheet" href="../css/{css_file}">')
        self.md_text = "\n".join(css_links) + "\n" + self.md_text

    def modify_img_path(self):
        self.md_text = self.md_text.replace("image/", r"../image/")

    def add_ToC_to_html(self, html_text):
        ToC_dict = {
            "<!-- vscode-markdown-toc -->": "<div class='toc-002'><div>目次</div>",
            "<!-- /vscode-markdown-toc -->": "</div>",
        }
        for key, value in ToC_dict.items():
            html_text = html_text.replace(key, value)
        return html_text

    def convert_to_html(self):
        html = markdown.markdown(self.md_text)
        self.html = self.add_ToC_to_html(html)

    def convert(self):
        self.add_css_tag()
        self.modify_img_path()
        html = markdown.markdown(self.md_text)
        return self.add_ToC_to_html(html)
