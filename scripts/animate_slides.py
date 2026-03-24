#!/usr/bin/env python3
"""
Labtec Safety — Slide Animator
===============================
Konvertiert exportierte Slides (PNG/JPG/PDF) in eine animierte HTML-Praesentation.

Nutzung:
  1. Slides aus Google Slides / NotebookLM als Bilder exportieren:
     - Google Slides: Datei → Herunterladen → PNG-Bilder (.png)
     - Oder als PDF exportieren (wird automatisch konvertiert)

  2. Skript ausfuehren:
     python3 scripts/animate_slides.py slides/       # Ordner mit Bildern
     python3 scripts/animate_slides.py slides.pdf    # PDF-Datei
     python3 scripts/animate_slides.py slides/ --style zoom   # Animations-Stil

  3. Ausgabe: reports/animated_presentation.html (im Browser oeffnen)

Animations-Stile:
  fade     — Sanftes Ein-/Ausblenden (Standard)
  slide    — Slides gleiten horizontal
  zoom     — Zoom-Effekt
  flip     — 3D-Flip
  cascade  — Elemente kaskadieren nacheinander ein

Steuerung im Browser:
  Pfeiltasten / Leertaste  — Naechste/Vorherige Slide
  F                        — Fullscreen
  O                        — Uebersicht aller Slides
  Nummer + Enter           — Direkt zu Slide springen
"""

import argparse
import base64
import glob
import os
import sys
import subprocess
from pathlib import Path


def pdf_to_images(pdf_path: str, output_dir: str) -> list[str]:
    """Konvertiert PDF zu PNG-Bildern via pdftoppm oder sips (macOS)."""
    os.makedirs(output_dir, exist_ok=True)

    # Versuch 1: pdftoppm (poppler-utils)
    try:
        subprocess.run(
            ["pdftoppm", "-png", "-r", "300", pdf_path, os.path.join(output_dir, "slide")],
            check=True, capture_output=True
        )
        images = sorted(glob.glob(os.path.join(output_dir, "slide-*.png")))
        if images:
            print(f"  ✓ {len(images)} Slides aus PDF extrahiert (pdftoppm)")
            return images
    except (FileNotFoundError, subprocess.CalledProcessError):
        pass

    # Versuch 2: magick/convert (ImageMagick)
    for cmd in ["magick", "convert"]:
        try:
            subprocess.run(
                [cmd, "-density", "300", pdf_path, "-quality", "95",
                 os.path.join(output_dir, "slide-%03d.png")],
                check=True, capture_output=True
            )
            images = sorted(glob.glob(os.path.join(output_dir, "slide-*.png")))
            if images:
                print(f"  ✓ {len(images)} Slides aus PDF extrahiert ({cmd})")
                return images
        except (FileNotFoundError, subprocess.CalledProcessError):
            pass

    print("  ✗ PDF-Konvertierung fehlgeschlagen.")
    print("    Installiere poppler-utils oder ImageMagick:")
    print("      macOS:  brew install poppler")
    print("      Linux:  sudo apt install poppler-utils")
    sys.exit(1)


def load_images(source: str) -> list[str]:
    """Laedt Bilder aus Ordner oder konvertiert PDF."""
    source_path = Path(source)

    if source_path.is_file() and source_path.suffix.lower() == ".pdf":
        tmp_dir = str(source_path.parent / "slide_images_tmp")
        return pdf_to_images(str(source_path), tmp_dir)

    if source_path.is_dir():
        extensions = ("*.png", "*.jpg", "*.jpeg", "*.webp", "*.svg")
        images = []
        for ext in extensions:
            images.extend(glob.glob(os.path.join(source, ext)))
        images.sort()
        if not images:
            print(f"  ✗ Keine Bilder in {source} gefunden.")
            sys.exit(1)
        print(f"  ✓ {len(images)} Slides gefunden")
        return images

    print(f"  ✗ '{source}' ist weder ein Ordner noch eine PDF-Datei.")
    sys.exit(1)


def image_to_data_uri(image_path: str) -> str:
    """Konvertiert Bild zu Base64 Data-URI fuer eingebettetes HTML."""
    ext = Path(image_path).suffix.lower()
    mime_types = {
        ".png": "image/png",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".webp": "image/webp",
        ".svg": "image/svg+xml",
    }
    mime = mime_types.get(ext, "image/png")

    with open(image_path, "rb") as f:
        data = base64.b64encode(f.read()).decode("utf-8")

    return f"data:{mime};base64,{data}"


def generate_html(images: list[str], style: str, title: str, autoplay: int) -> str:
    """Generiert die animierte HTML-Praesentation."""

    # Slides als Data-URIs einbetten
    slides_html = []
    for i, img_path in enumerate(images):
        data_uri = image_to_data_uri(img_path)
        slide_num = i + 1
        slides_html.append(
            f'      <div class="slide" data-slide="{slide_num}">'
            f'<img src="{data_uri}" alt="Slide {slide_num}" />'
            f'<div class="slide-number">{slide_num} / {len(images)}</div>'
            f'</div>'
        )

    slides_joined = "\n".join(slides_html)

    # Animations-CSS je nach Stil
    animation_css = {
        "fade": """
      .slide { opacity: 0; transition: opacity 0.6s ease; }
      .slide.active { opacity: 1; }
    """,
        "slide": """
      .slide {
        opacity: 0;
        transform: translateX(100%);
        transition: all 0.5s cubic-bezier(0.25, 0.46, 0.45, 0.94);
      }
      .slide.active {
        opacity: 1;
        transform: translateX(0);
      }
      .slide.prev {
        opacity: 0;
        transform: translateX(-100%);
      }
    """,
        "zoom": """
      .slide {
        opacity: 0;
        transform: scale(0.85);
        transition: all 0.6s cubic-bezier(0.34, 1.56, 0.64, 1);
      }
      .slide.active {
        opacity: 1;
        transform: scale(1);
      }
    """,
        "flip": """
      .slides-container { perspective: 1200px; }
      .slide {
        opacity: 0;
        transform: rotateY(90deg);
        transition: all 0.7s ease;
        backface-visibility: hidden;
      }
      .slide.active {
        opacity: 1;
        transform: rotateY(0deg);
      }
    """,
        "cascade": """
      .slide {
        opacity: 0;
        transform: translateY(40px) scale(0.95);
        transition: all 0.7s cubic-bezier(0.25, 0.46, 0.45, 0.94);
      }
      .slide.active {
        opacity: 1;
        transform: translateY(0) scale(1);
      }
    """,
    }

    css = animation_css.get(style, animation_css["fade"])

    autoplay_js = ""
    if autoplay > 0:
        autoplay_js = f"""
    // Autoplay
    let autoplayTimer = setInterval(() => nextSlide(), {autoplay * 1000});
    document.addEventListener('keydown', () => {{
      clearInterval(autoplayTimer);
      autoplayTimer = null;
    }});
    """

    html = f"""<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
  <style>
    * {{ margin: 0; padding: 0; box-sizing: border-box; }}

    body {{
      background: #0a0e1a;
      color: #fff;
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif;
      overflow: hidden;
      height: 100vh;
      user-select: none;
    }}

    /* Slide Container */
    .slides-container {{
      position: relative;
      width: 100vw;
      height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
    }}

    .slide {{
      position: absolute;
      width: 100%;
      height: 100%;
      display: flex;
      align-items: center;
      justify-content: center;
      pointer-events: none;
    }}

    .slide.active {{
      pointer-events: auto;
      z-index: 2;
    }}

    .slide img {{
      max-width: 95%;
      max-height: 92vh;
      object-fit: contain;
      border-radius: 8px;
      box-shadow: 0 20px 60px rgba(0,0,0,0.5);
    }}

    .slide-number {{
      position: absolute;
      bottom: 16px;
      right: 24px;
      font-size: 14px;
      color: rgba(255,255,255,0.5);
      font-variant-numeric: tabular-nums;
    }}

    /* Animation styles */
    {css}

    /* Progress Bar */
    .progress-bar {{
      position: fixed;
      top: 0;
      left: 0;
      height: 3px;
      background: linear-gradient(90deg, #009b91, #1e326e);
      transition: width 0.4s ease;
      z-index: 100;
    }}

    /* Navigation */
    .nav-btn {{
      position: fixed;
      top: 50%;
      transform: translateY(-50%);
      z-index: 50;
      background: rgba(255,255,255,0.08);
      border: 1px solid rgba(255,255,255,0.12);
      color: #fff;
      width: 48px;
      height: 48px;
      border-radius: 50%;
      cursor: pointer;
      font-size: 20px;
      display: flex;
      align-items: center;
      justify-content: center;
      backdrop-filter: blur(8px);
      transition: all 0.2s;
      opacity: 0;
    }}
    .slides-container:hover .nav-btn {{ opacity: 1; }}
    .nav-btn:hover {{ background: rgba(0,155,145,0.3); }}
    .nav-prev {{ left: 16px; }}
    .nav-next {{ right: 16px; }}

    /* Uebersicht */
    .overview {{
      position: fixed;
      inset: 0;
      background: rgba(10,14,26,0.95);
      backdrop-filter: blur(20px);
      z-index: 200;
      display: none;
      padding: 40px;
      overflow-y: auto;
    }}
    .overview.visible {{ display: block; }}
    .overview-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
      gap: 20px;
      max-width: 1400px;
      margin: 0 auto;
    }}
    .overview-item {{
      cursor: pointer;
      border-radius: 8px;
      overflow: hidden;
      border: 2px solid transparent;
      transition: all 0.2s;
    }}
    .overview-item:hover,
    .overview-item.current {{ border-color: #009b91; }}
    .overview-item img {{
      width: 100%;
      display: block;
    }}
    .overview-label {{
      padding: 8px;
      text-align: center;
      font-size: 13px;
      color: rgba(255,255,255,0.6);
      background: rgba(255,255,255,0.05);
    }}
    .overview-title {{
      text-align: center;
      font-size: 14px;
      color: rgba(255,255,255,0.4);
      margin-bottom: 24px;
    }}

    /* Hilfe-Overlay */
    .help {{
      position: fixed;
      bottom: 16px;
      left: 24px;
      font-size: 12px;
      color: rgba(255,255,255,0.25);
      z-index: 50;
      opacity: 0;
      transition: opacity 0.3s;
    }}
    .slides-container:hover .help {{ opacity: 1; }}
  </style>
</head>
<body>

  <div class="progress-bar" id="progress"></div>

  <div class="slides-container" id="container">
{slides_joined}

    <button class="nav-btn nav-prev" onclick="prevSlide()">&#8249;</button>
    <button class="nav-btn nav-next" onclick="nextSlide()">&#8250;</button>

    <div class="help">
      ← → Navigieren &nbsp;|&nbsp; F Fullscreen &nbsp;|&nbsp; O Uebersicht &nbsp;|&nbsp; Nummer+Enter = Sprung
    </div>
  </div>

  <div class="overview" id="overview">
    <div class="overview-title">Uebersicht — Klick oder Nummer+Enter zum Springen</div>
    <div class="overview-grid" id="overviewGrid"></div>
  </div>

  <script>
    const slides = document.querySelectorAll('.slide');
    const total = slides.length;
    let current = 0;
    let numberBuffer = '';
    let numberTimeout = null;

    function showSlide(index) {{
      slides.forEach((s, i) => {{
        s.classList.remove('active', 'prev');
        if (i < index) s.classList.add('prev');
      }});
      slides[index].classList.add('active');
      document.getElementById('progress').style.width =
        ((index + 1) / total * 100) + '%';
      current = index;

      // Update overview
      document.querySelectorAll('.overview-item').forEach((item, i) => {{
        item.classList.toggle('current', i === index);
      }});
    }}

    function nextSlide() {{
      if (current < total - 1) showSlide(current + 1);
    }}

    function prevSlide() {{
      if (current > 0) showSlide(current - 1);
    }}

    function toggleOverview() {{
      document.getElementById('overview').classList.toggle('visible');
    }}

    function toggleFullscreen() {{
      if (!document.fullscreenElement) {{
        document.documentElement.requestFullscreen();
      }} else {{
        document.exitFullscreen();
      }}
    }}

    // Keyboard navigation
    document.addEventListener('keydown', (e) => {{
      const overview = document.getElementById('overview');

      // Number input for direct slide jump
      if (e.key >= '0' && e.key <= '9') {{
        numberBuffer += e.key;
        clearTimeout(numberTimeout);
        numberTimeout = setTimeout(() => {{ numberBuffer = ''; }}, 1500);
        return;
      }}

      if (e.key === 'Enter' && numberBuffer) {{
        const target = parseInt(numberBuffer) - 1;
        if (target >= 0 && target < total) {{
          showSlide(target);
          if (overview.classList.contains('visible')) {{
            overview.classList.remove('visible');
          }}
        }}
        numberBuffer = '';
        return;
      }}

      numberBuffer = '';

      switch(e.key) {{
        case 'ArrowRight':
        case ' ':
        case 'PageDown':
          e.preventDefault();
          nextSlide();
          break;
        case 'ArrowLeft':
        case 'PageUp':
          e.preventDefault();
          prevSlide();
          break;
        case 'Home':
          showSlide(0);
          break;
        case 'End':
          showSlide(total - 1);
          break;
        case 'f':
        case 'F':
          toggleFullscreen();
          break;
        case 'o':
        case 'O':
          toggleOverview();
          break;
        case 'Escape':
          if (overview.classList.contains('visible')) {{
            overview.classList.remove('visible');
          }}
          break;
      }}
    }});

    // Touch/swipe support
    let touchStartX = 0;
    document.addEventListener('touchstart', (e) => {{
      touchStartX = e.touches[0].clientX;
    }});
    document.addEventListener('touchend', (e) => {{
      const diff = touchStartX - e.changedTouches[0].clientX;
      if (Math.abs(diff) > 50) {{
        if (diff > 0) nextSlide();
        else prevSlide();
      }}
    }});

    // Build overview grid
    const grid = document.getElementById('overviewGrid');
    slides.forEach((slide, i) => {{
      const item = document.createElement('div');
      item.className = 'overview-item' + (i === 0 ? ' current' : '');
      const img = slide.querySelector('img');
      item.innerHTML = `<img src="${{img.src}}" /><div class="overview-label">Slide ${{i+1}}</div>`;
      item.onclick = () => {{
        showSlide(i);
        toggleOverview();
      }};
      grid.appendChild(item);
    }});

    // Init
    showSlide(0);

    {autoplay_js}
  </script>
</body>
</html>"""

    return html


def main():
    parser = argparse.ArgumentParser(
        description="Labtec Slide Animator — Exportierte Slides in animierte HTML-Praesentation verwandeln"
    )
    parser.add_argument(
        "source",
        help="Ordner mit Slide-Bildern (PNG/JPG) oder PDF-Datei"
    )
    parser.add_argument(
        "--style", "-s",
        choices=["fade", "slide", "zoom", "flip", "cascade"],
        default="fade",
        help="Animations-Stil (Standard: fade)"
    )
    parser.add_argument(
        "--output", "-o",
        default=None,
        help="Ausgabe-Datei (Standard: reports/animated_presentation.html)"
    )
    parser.add_argument(
        "--title", "-t",
        default="Web-Analytics Report — labtec-safety.ch",
        help="Praesentation-Titel"
    )
    parser.add_argument(
        "--autoplay", "-a",
        type=int,
        default=0,
        help="Autoplay-Intervall in Sekunden (0 = aus)"
    )

    args = parser.parse_args()

    print()
    print("  ╔══════════════════════════════════════════╗")
    print("  ║   Labtec Safety — Slide Animator         ║")
    print("  ╚══════════════════════════════════════════╝")
    print()

    # Bilder laden
    images = load_images(args.source)

    # HTML generieren
    print(f"  → Animations-Stil: {args.style}")
    html = generate_html(images, args.style, args.title, args.autoplay)

    # Speichern
    output = args.output
    if output is None:
        output = os.path.join(os.path.dirname(os.path.dirname(__file__)), "reports", "animated_presentation.html")

    os.makedirs(os.path.dirname(output), exist_ok=True)

    with open(output, "w", encoding="utf-8") as f:
        f.write(html)

    size_mb = os.path.getsize(output) / (1024 * 1024)
    print(f"  ✓ Gespeichert: {output} ({size_mb:.1f} MB)")
    print()
    print("  Steuerung:")
    print("  ─────────")
    print("  ← →  Navigieren       F  Fullscreen")
    print("  O    Uebersicht       Leertaste  Weiter")
    print("  1-9 + Enter  Direkt zu Slide springen")
    if args.autoplay > 0:
        print(f"  Autoplay: alle {args.autoplay}s (Taste druecken zum Stoppen)")
    print()


if __name__ == "__main__":
    main()
