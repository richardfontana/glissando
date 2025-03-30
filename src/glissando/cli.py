# Copyright The glissando Authors
# SPDX-License-Identifier: MIT

import sys 
import os 
import shutil
from importlib.resources import files
from .parser import parse_markdown_to_slides 
from .generator import generate_html

def main():
    if len(sys.argv) != 2:
        print("Usage: glissando <markdown-file.md>")
        sys.exit(1)
    md_file = sys.argv[1]
    if not md_file.endswith('.md'):
        print("Error: Please provide a .md file")
        sys.exit(1)
    if not os.path.exists('styles.css'):
        css_source = files('glissando') / 'styles.css'
        shutil.copy(css_source, 'styles.css')
        print("Copied styles.css to current directory")

    try:
        with open(md_file, 'r', encoding='utf-8') as f:
            md_text = f.read()
    except FileNotFoundError:
        print(f"Error: File '{md_file}' not found")
        sys.exit(1)

    slides = parse_markdown_to_slides(md_text)
    if not slides:
        print("Error: No valid slides found in the markdown file")
        sys.exit(1)

    html = generate_html(slides)
    with open('presentation.html', 'w', encoding='utf-8') as f:
        f.write(html)
        print("Generated presentation.html")

if __name__ == "__main__":
    main()
