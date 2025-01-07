import os

from config import MANUAL_DIR
from file_converter import FileConverter
from io_files import read_markdown_text, write_html_text


def is_md_file(file_name: str):
    return file_name.endswith(".md")


if __name__ == "__main__":

    manual_files = os.listdir(MANUAL_DIR)
    for manual_md_file in manual_files:
        if not is_md_file(manual_md_file):
            continue
        md_text = read_markdown_text(manual_md_file)
        html_text = FileConverter(md_text).convert()
        write_html_text(manual_md_file, html_text)
