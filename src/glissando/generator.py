# Copyright The glissando Authors
# SPDX-License-Identifier: MIT

def generate_html(slides: list[str]) -> str:
    slide_html = ''.join(
        f'<div class="slide{" active" if i == 0 else ""}" data-index="{i}">'
        f'<div class="slide-content">'
        f'{"<div class=\"title-content\">" + content + "</div>" if i == 0 else content}'
        f'</div>'
        '</div>'
        for i, content in enumerate(slides)
    )
    
    # Generate slide indicators
    indicators_html = ''.join(
        f'<div class="slide-indicator{" active" if i == 0 else ""}" data-index="{i}"></div>'
        for i in range(len(slides))
    )

    return f"""<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Presentation</title>
        <link rel="stylesheet" href="styles.css">
    </head>
    <body>
        <div class="slide-container">
            {slide_html}
            <div class="slide-indicators">
                {indicators_html}
            </div>
            <div class="slide-counter">1 / {len(slides)}</div>
            <button class="fullscreen-button" title="Toggle fullscreen">⛶</button>
        </div>
        <script>
            document.addEventListener('DOMContentLoaded', function() {{
                var currentSlide = 0;
                var slides = document.querySelectorAll('.slide');
                var indicators = document.querySelectorAll('.slide-indicator');
                var counter = document.querySelector('.slide-counter');
                var fullscreenButton = document.querySelector('.fullscreen-button');
                var totalSlides = slides.length;
                
                // Set initial state
                updateSlideState(0);
                
                // Update slide counter
                updateCounter(0);
                
                function updateCounter(index) {{
                    counter.textContent = (index + 1) + ' / ' + totalSlides;
                }}
                
                function updateSlideState(index) {{
                    // Update slides
                    for (var i = 0; i < slides.length; i++) {{
                        slides[i].classList.remove('active');
                        indicators[i].classList.remove('active');
                    }}
                    
                    slides[index].classList.add('active');
                    indicators[index].classList.add('active');
                    
                    // Update counter
                    updateCounter(index);
                    
                    // Update current slide index
                    currentSlide = index;
                }}
    
                function showSlide(index) {{
                    // Validate index bounds
                    if (index < 0) {{
                        index = 0;
                    }} else if (index >= slides.length) {{
                        index = slides.length - 1;
                    }}
                    
                    if (index === currentSlide) {{
                        return;
                    }}
                    
                    console.log('Changing from slide ' + currentSlide + ' to slide ' + index);
                    
                    // Update all slide states
                    updateSlideState(index);
                }}
    
                // Keyboard navigation
                document.addEventListener('keydown', function(e) {{
                    if (e.key === 'ArrowLeft') {{
                        showSlide(currentSlide - 1);
                    }} else if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'Enter') {{
                        showSlide(currentSlide + 1);
                    }}
                }});
                
                // Indicator click navigation
                indicators.forEach(function(indicator) {{
                    indicator.addEventListener('click', function() {{
                        var index = parseInt(this.getAttribute('data-index'));
                        showSlide(index);
                    }});
                }});
                
                // Fullscreen toggle
                fullscreenButton.addEventListener('click', function() {{
                    toggleFullscreen();
                }});
                
                function toggleFullscreen() {{
                    if (!document.fullscreenElement) {{
                        document.documentElement.requestFullscreen().catch(err => {{
                            console.log(`Error attempting to enable fullscreen: ${{err.message}}`);
                        }});
                        fullscreenButton.innerHTML = '⤢';
                    }} else {{
                        if (document.exitFullscreen) {{
                            document.exitFullscreen();
                            fullscreenButton.innerHTML = '⛶';
                        }}
                    }}
                }}
                
                // Swipe support for touch devices
                var touchStartX = 0;
                var touchEndX = 0;
                
                document.addEventListener('touchstart', function(e) {{
                    touchStartX = e.changedTouches[0].screenX;
                }}, false);
                
                document.addEventListener('touchend', function(e) {{
                    touchEndX = e.changedTouches[0].screenX;
                    handleSwipe();
                }}, false);
                
                function handleSwipe() {{
                    var threshold = 50; // minimum distance for swipe
                    if (touchEndX < touchStartX - threshold) {{
                        // Swipe left, next slide
                        showSlide(currentSlide + 1);
                    }} else if (touchEndX > touchStartX + threshold) {{
                        // Swipe right, previous slide
                        showSlide(currentSlide - 1);
                    }}
                }}
            }});
        </script>
    </body>
</html>
"""
