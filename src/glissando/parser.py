# Copyright The glissando Authors
# SPDX-License-Identifier: MIT

import markdown

def parse_markdown_to_slides(md_text: str) -> list[str]:
    sections = [s.strip() for s in md_text.split('---') if s.strip()]
    if not sections:
        return []
    slides = [markdown.markdown(section, extensions=['extra']) for section in sections]
    return slides
