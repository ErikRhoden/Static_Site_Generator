import os
import shutil

from copystatic import copy_files_recursive
from markdown_blocks import extract_title, generate_page


dir_path_static = "./static"
dir_path_public = "./public"
content_md_path = 'content/index.md'
template_html_path = 'template.html'
output_html_path = 'public/index.html'


def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

    print("Generating HTML content...")
    generate_page(content_md_path, template_html_path, output_html_path)

if __name__ == '__main__':
    main()
