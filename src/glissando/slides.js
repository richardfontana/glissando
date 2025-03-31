/* 
 * Copyright The glissando Authors 
 * SPDX-License-Identifier: Unlicense                                
 */

document.addEventListener('DOMContentLoaded', function () {
  console.log("DOM fully loaded");

  let currentSlide = 0;
  const slides = document.querySelectorAll('.slide');

  function showSlide(index) {
    if (index < 0 || index >= slides.length) return;
    slides[currentSlide].classList.remove('active');
    slides[index].classList.add('active');
    currentSlide = index;
    console.log(`Switched to slide ${index}`);
  }

  // Ensure only the first slide is visible
  slides.forEach((slide, i) => {
    slide.classList.remove('active');
    if (i === 0) slide.classList.add('active');
  });

  document.addEventListener('keydown', function (e) {
    if (e.key === 'ArrowRight') {
      showSlide(currentSlide + 1);
    } else if (e.key === 'ArrowLeft') {
      showSlide(currentSlide - 1);
    }
  });
});

