from config import HTML_DIR, MANUAL_DIR


def read_markdown_text(file_name):
    file_path = MANUAL_DIR / file_name
    with open(file_path, "r", encoding="utf-8") as file:
        raw_text = file.read()
    return raw_text


def write_html_text(file_name, html_text):
    file_path = HTML_DIR / file_name.replace(".md", ".html")
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(html_text)
