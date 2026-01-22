// Simple global lightbox for Sphinx pages (no markdown changes required)
// Applies to images in the main content area and anchors linking to image files.
(function () {
  if (window.__SF_LIGHTBOX_INIT__) return; // avoid double init
  window.__SF_LIGHTBOX_INIT__ = true;

  function ready(fn) {
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', fn);
    } else {
      fn();
    }
  }

  ready(function () {
    const contentRoot =
      document.querySelector('main, article, .document, .bd-article, .sphinx-content') ||
      document.body;

    // Collect candidate images, avoid typical layout chrome
    const excludedContainers = 'header, nav, footer, aside, .sidebar, .related, .navbar, .logo';
    const allImgs = Array.from(contentRoot.querySelectorAll('img'));
    const imgs = allImgs.filter((img) => !img.closest(excludedContainers));

    if (!imgs.length) return;

    // Build overlay once
    const overlay = document.createElement('div');
    overlay.id = 'sf-lightbox-overlay';
    overlay.setAttribute('aria-hidden', 'true');
    overlay.innerHTML = [
      '<div class="sf-lightbox-backdrop" role="presentation"></div>',
      '<figure class="sf-lightbox-figure" role="dialog" aria-modal="true">',
      '  <img class="sf-lightbox-img" alt="" draggable="false" />',
      '  <figcaption class="sf-lightbox-caption"></figcaption>',
      '  <div class="sf-lightbox-toolbar" aria-label="Zoom controls" role="group">',
      '    <button class="sf-lb-btn sf-lb-zoom-in" data-action="zoom-in" title="放大 (Ctrl/滚轮)">+</button>',
      '    <button class="sf-lb-btn sf-lb-zoom-out" data-action="zoom-out" title="缩小">−</button>',
      '    <button class="sf-lb-btn sf-lb-reset" data-action="reset" title="重置 (双击)">100%</button>',
      '  </div>',
      '  <button class="sf-lightbox-close" aria-label="Close">×</button>',
      '</figure>'
    ].join('');

    document.body.appendChild(overlay);

    const imgEl = overlay.querySelector('.sf-lightbox-img');
    const capEl = overlay.querySelector('.sf-lightbox-caption');
    const figureEl = overlay.querySelector('.sf-lightbox-figure');
    const toolbarEl = overlay.querySelector('.sf-lightbox-toolbar');

    // Zoom & pan state
    let scale = 1;
    const minScale = 1;
    const maxScale = 5;
    const step = 0.2;
    let tx = 0, ty = 0; // translate
    let isPanning = false;
    let startX = 0, startY = 0;
    let pinchStartDist = 0, pinchStartScale = 1;

    function clamp(v, min, max) {
      return Math.max(min, Math.min(max, v));
    }
    function updateTransform() {
      imgEl.style.transform = 'translate(' + tx + 'px,' + ty + 'px) scale(' + scale + ')';
      // Toggle grab cursor when zoomed
      if (scale > 1) {
        imgEl.classList.add('is-zoomed');
      } else {
        imgEl.classList.remove('is-zoomed');
      }
    }

    function openLightbox(src, alt) {
      if (!src) return;
      imgEl.src = src;
      imgEl.alt = alt || '';
      capEl.textContent = alt || '';
      // reset zoom/pan state on open
      scale = 1; tx = 0; ty = 0; updateTransform();
      overlay.classList.add('is-open');
      overlay.setAttribute('aria-hidden', 'false');
      document.body.classList.add('sf-lightbox-open');
    }

    function closeLightbox() {
      overlay.classList.remove('is-open');
      overlay.setAttribute('aria-hidden', 'true');
      document.body.classList.remove('sf-lightbox-open');
      // do not clear src to allow quick reopen
    }

    overlay.addEventListener('click', function (e) {
      if (
        e.target === overlay ||
        e.target.classList.contains('sf-lightbox-backdrop') ||
        e.target.classList.contains('sf-lightbox-close')
      ) {
        closeLightbox();
      }
    });

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') closeLightbox();
      if (!overlay.classList.contains('is-open')) return;
      if (e.key === '+' || e.key === '=') { // '+' can be shift+'='
        scale = clamp(scale + step, minScale, maxScale);
        updateTransform();
      } else if (e.key === '-') {
        scale = clamp(scale - step, minScale, maxScale);
        updateTransform();
      } else if (e.key === '0') {
        scale = 1; tx = 0; ty = 0; updateTransform();
      }
    });

    const imageExtRe = /\.(png|jpe?g|gif|webp|bmp|svg)(\?.*)?$/i;

    imgs.forEach((img) => {
      // Skip if explicitly opted out
      if (img.dataset.noLightbox === 'true' || img.classList.contains('no-lightbox')) return;

      const alt = img.getAttribute('alt') || '';
      const link = img.closest('a');

      if (link) {
        const href = link.getAttribute('href') || '';
        if (imageExtRe.test(href)) {
          // If the image is wrapped by an anchor to another image file, intercept
          link.addEventListener('click', function (e) {
            e.preventDefault();
            openLightbox(href, alt);
          });
          link.style.cursor = 'zoom-in';
        } else {
          // Non-image link: don't hijack behavior
        }
      } else {
        img.style.cursor = 'zoom-in';
        img.addEventListener('click', function () {
          const src = img.currentSrc || img.src; // respect srcset when available
          openLightbox(src, alt);
        });
      }
    });

    // Toolbar actions
    if (toolbarEl) {
      toolbarEl.addEventListener('click', function (e) {
        const btn = e.target.closest('button[data-action]');
        if (!btn) return;
        const action = btn.dataset.action;
        if (action === 'zoom-in') {
          scale = clamp(scale + step, minScale, maxScale);
        } else if (action === 'zoom-out') {
          scale = clamp(scale - step, minScale, maxScale);
        } else if (action === 'reset') {
          scale = 1; tx = 0; ty = 0;
        }
        updateTransform();
      });
    }

    // Mouse wheel zoom
    figureEl.addEventListener('wheel', function (e) {
      e.preventDefault();
      const delta = e.deltaY || 0;
      if (delta < 0) {
        scale = clamp(scale + step, minScale, maxScale);
      } else if (delta > 0) {
        scale = clamp(scale - step, minScale, maxScale);
      }
      updateTransform();
    }, { passive: false });

    // Double click to toggle zoom
    imgEl.addEventListener('dblclick', function () {
      if (scale === 1) {
        scale = 2;
      } else {
        scale = 1; tx = 0; ty = 0;
      }
      updateTransform();
    });

    // Drag to pan (mouse)
    imgEl.addEventListener('mousedown', function (e) {
      if (scale <= 1) return;
      isPanning = true;
      startX = e.clientX - tx;
      startY = e.clientY - ty;
      imgEl.classList.add('is-panning');
      e.preventDefault();
    });
    window.addEventListener('mousemove', function (e) {
      if (!isPanning) return;
      tx = e.clientX - startX;
      ty = e.clientY - startY;
      updateTransform();
    });
    window.addEventListener('mouseup', function () {
      isPanning = false;
      imgEl.classList.remove('is-panning');
    });

    // Touch: pan with 1 finger, pinch with 2 fingers
    figureEl.addEventListener('touchstart', function (e) {
      if (e.touches.length === 2) {
        const dx = e.touches[0].clientX - e.touches[1].clientX;
        const dy = e.touches[0].clientY - e.touches[1].clientY;
        pinchStartDist = Math.hypot(dx, dy);
        pinchStartScale = scale;
      } else if (e.touches.length === 1) {
        startX = e.touches[0].clientX - tx;
        startY = e.touches[0].clientY - ty;
      }
    }, { passive: true });
    figureEl.addEventListener('touchmove', function (e) {
      if (e.touches.length === 2) {
        e.preventDefault();
        const dx = e.touches[0].clientX - e.touches[1].clientX;
        const dy = e.touches[0].clientY - e.touches[1].clientY;
        const dist = Math.hypot(dx, dy);
        const ratio = dist / (pinchStartDist || dist);
        scale = clamp(pinchStartScale * ratio, minScale, maxScale);
        updateTransform();
      } else if (e.touches.length === 1 && scale > 1) {
        e.preventDefault();
        tx = e.touches[0].clientX - startX;
        ty = e.touches[0].clientY - startY;
        updateTransform();
      }
    }, { passive: false });
    figureEl.addEventListener('touchend', function () {
      // noop; state naturally resets for next gesture
    });
  });
})();
