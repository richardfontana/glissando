# Copyright The glissando Authors
# SPDX-License-Identifier: Unlicense

def generate_html(slides: list[str]) -> str:
    slide_html = ''.join(
        f'<div class="slide{" active" if i == 0 else ""}" data-index="{i}">'
        f'<div class="slide-content">{content}</div>'
        f'</div>'
        for i, content in enumerate(slides)
    )

    return f"""<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
        <title>Presentation</title>
        <link rel="stylesheet" href="styles.css" />
    </head>
    <body>
        <div class="slide-container">
            {slide_html}
        </div>
        <script src="slides.js"></script>
    </body>
</html>
"""

