# Image Generation Spec

Agent-readable instructions for generating branded images (social cards, banners, icons, diagrams, presentation slides) using brand-book design tokens.

## Library Selection

| Language | Library | Install | Best For |
|----------|---------|---------|----------|
| Python | `Pillow` (PIL) | `pip install Pillow` | Server-side generation, batch processing, simple compositing |
| Node.js | `sharp` | `npm install sharp` | High-performance resize/convert, production pipelines |
| Node.js | `@napi-rs/canvas` | `npm install @napi-rs/canvas` | Text rendering, complex layouts, Canvas API compatibility |
| Browser | Canvas API | Built-in | Client-side generation, dynamic previews |
| Node.js | `satori` + `resvg` | `npm install satori @resvg/resvg-js` | JSX-to-SVG-to-PNG, best for OG images with complex layouts |

**Default:** Use `Pillow` for Python contexts, `satori` + `resvg` for Node.js OG/social card generation, `sharp` for resize/convert pipelines.

---

## Image Types & Dimensions

| Type | Dimensions (px) | Aspect Ratio | Use Case |
|------|-----------------|--------------|----------|
| LinkedIn post | 1200 x 627 | ~1.91:1 | Shared link previews, article cards |
| Twitter/X card | 1200 x 675 | 16:9 | Summary large image cards |
| Instagram square | 1080 x 1080 | 1:1 | Feed posts, carousels |
| Instagram story | 1080 x 1920 | 9:16 | Stories, reels covers |
| Facebook share | 1200 x 630 | ~1.91:1 | Link previews, shared images |
| Open Graph | 1200 x 630 | ~1.91:1 | Default meta image for web pages |
| Email banner | 600 x 200 | 3:1 | Email header images (web-safe) |
| Blog header | 1200 x 630 | ~1.91:1 | Article featured images |
| Favicon | 32 x 32 | 1:1 | Browser tab icon |
| Favicon SVG | 32 x 32 | 1:1 | Modern browsers, scalable |
| Apple touch icon | 180 x 180 | 1:1 | iOS home screen |
| App icon | 512 x 512 | 1:1 | PWA, app stores |
| Android adaptive | 512 x 512 | 1:1 | Masked to circle/squircle |
| Presentation slide | 1920 x 1080 | 16:9 | Static slide exports |
| Diagram background | Variable | Variable | Whiteboard/diagram canvases |

### Safe Zones

All social cards and banners must keep text and logos within a safe zone:

```
+--------------------------------------------+
|  margin (8% of width on each side)         |
|  +--------------------------------------+  |
|  |                                      |  |
|  |          SAFE ZONE                   |  |
|  |     (text, logos, key content)       |  |
|  |                                      |  |
|  +--------------------------------------+  |
|  margin (10% of height top/bottom)         |
+--------------------------------------------+
```

---

## Token Loading

```python
import json

def load_image_tokens(brand_book_path):
    """Load and merge tokens needed for image generation."""
    with open(f'{brand_book_path}/tokens/primitives.tokens.json') as f:
        primitives = json.load(f)
    with open(f'{brand_book_path}/tokens/semantic.tokens.json') as f:
        semantic = json.load(f)
    with open(f'{brand_book_path}/tokens/component.tokens.json') as f:
        components = json.load(f)

    # Resolve common values for image generation
    return {
        'color': {
            'brand_primary': semantic['color']['brand']['primary']['$value'],
            'brand_secondary': semantic['color']['brand']['secondary']['$value'],
            'brand_accent': semantic['color']['brand'].get('accent', {}).get('$value', '#F59E0B'),
            'surface_default': semantic['color']['surface']['default']['$value'],
            'surface_subtle': semantic['color']['surface']['subtle']['$value'],
            'text_primary': semantic['color']['text']['primary']['$value'],
            'text_secondary': semantic['color']['text']['secondary']['$value'],
            'text_on_brand': '#FFFFFF',
            'border_default': semantic['color']['border']['default']['$value'],
            'data_series': [
                semantic['color']['data'][f'series-{i}']['$value']
                for i in range(1, 7)
            ],
        },
        'font': {
            'heading': semantic['fontFamily']['heading']['$value'],
            'body': semantic['fontFamily']['body']['$value'],
            'mono': semantic['fontFamily']['mono']['$value'],
        },
        'typography': {
            'h1': {'size': 36, 'weight': 700, 'lineHeight': 1.1},
            'h2': {'size': 28, 'weight': 600, 'lineHeight': 1.2},
            'h3': {'size': 22, 'weight': 600, 'lineHeight': 1.3},
            'body': {'size': 16, 'weight': 400, 'lineHeight': 1.5},
            'caption': {'size': 12, 'weight': 400, 'lineHeight': 1.4},
            'data_lg': {'size': 48, 'weight': 700, 'lineHeight': 1.0},
        },
        'spacing': {
            'xs': 4, 'sm': 8, 'md': 16, 'lg': 24, 'xl': 32, '2xl': 48, '3xl': 64,
        },
        'radius': {
            'sm': 4, 'md': 8, 'lg': 12, 'xl': 16,
        },
        'logo': components.get('logo', {}),
    }
```

---

## Font Loading

Image generation requires loading font files (TTF/OTF) directly. Google Fonts must be downloaded before rendering.

### Python (Pillow)

```python
from PIL import ImageFont
import os

def load_brand_fonts(font_dir):
    """Load brand font files for Pillow text rendering.

    Download Google Fonts TTF files to font_dir before calling:
      Inter-Regular.ttf, Inter-Bold.ttf, Inter-SemiBold.ttf,
      JetBrainsMono-Regular.ttf, JetBrainsMono-Bold.ttf
    """
    fonts = {}
    font_map = {
        'heading': 'Inter-Bold.ttf',
        'heading_semi': 'Inter-SemiBold.ttf',
        'body': 'Inter-Regular.ttf',
        'body_bold': 'Inter-Bold.ttf',
        'mono': 'JetBrainsMono-Regular.ttf',
    }
    for key, filename in font_map.items():
        path = os.path.join(font_dir, filename)
        fonts[key] = {
            'path': path,
            # Pre-load common sizes
            'sizes': {
                size: ImageFont.truetype(path, size)
                for size in [12, 14, 16, 18, 20, 22, 24, 28, 32, 36, 48, 64]
            },
        }
    return fonts

def get_font(fonts, style, size):
    """Get a font at a specific size, loading on demand if needed."""
    if size in fonts[style]['sizes']:
        return fonts[style]['sizes'][size]
    font = ImageFont.truetype(fonts[style]['path'], size)
    fonts[style]['sizes'][size] = font
    return font
```

### Node.js (satori)

```javascript
const fs = require('fs');

function loadBrandFonts(fontDir) {
  // satori requires ArrayBuffer font data
  return [
    {
      name: 'Inter',
      data: fs.readFileSync(`${fontDir}/Inter-Regular.ttf`).buffer,
      weight: 400,
      style: 'normal',
    },
    {
      name: 'Inter',
      data: fs.readFileSync(`${fontDir}/Inter-SemiBold.ttf`).buffer,
      weight: 600,
      style: 'normal',
    },
    {
      name: 'Inter',
      data: fs.readFileSync(`${fontDir}/Inter-Bold.ttf`).buffer,
      weight: 700,
      style: 'normal',
    },
    {
      name: 'JetBrains Mono',
      data: fs.readFileSync(`${fontDir}/JetBrainsMono-Regular.ttf`).buffer,
      weight: 400,
      style: 'normal',
    },
  ];
}
```

---

## Social Card Generation

### Python (Pillow)

```python
from PIL import Image, ImageDraw, ImageFont

def generate_social_card(tokens, fonts, output_path, options):
    """Generate a branded social card image.

    Args:
        options: {
            'platform': 'linkedin' | 'twitter' | 'instagram' | 'facebook' | 'og',
            'title': str,
            'subtitle': str (optional),
            'category': str (optional, e.g., 'Insights', 'News'),
            'variant': 'solid' | 'gradient' | 'photo_overlay',
            'background_image': str (optional, path for photo_overlay variant),
            'logo_path': str (optional),
        }
    """
    # Dimensions by platform
    dims = {
        'linkedin': (1200, 627),
        'twitter': (1200, 675),
        'instagram': (1080, 1080),
        'instagram_story': (1080, 1920),
        'facebook': (1200, 630),
        'og': (1200, 630),
    }
    width, height = dims[options['platform']]

    # Create base image
    img = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(img)

    # Background variant
    bg_primary = tokens['color']['brand_primary']
    bg_secondary = tokens['color']['brand_secondary']

    if options.get('variant') == 'gradient':
        _draw_gradient(img, bg_primary, bg_secondary, direction='diagonal')
    elif options.get('variant') == 'photo_overlay' and options.get('background_image'):
        bg = Image.open(options['background_image']).resize((width, height))
        img.paste(bg)
        # Dark overlay for text readability
        overlay = Image.new('RGBA', (width, height), (*_hex_to_rgb(bg_primary), 180))
        img = Image.alpha_composite(img.convert('RGBA'), overlay).convert('RGB')
        draw = ImageDraw.Draw(img)
    else:
        draw.rectangle([0, 0, width, height], fill=bg_primary)

    # Safe zone margins
    margin_x = int(width * 0.08)
    margin_y = int(height * 0.10)

    # Category badge (optional)
    y_cursor = margin_y
    if options.get('category'):
        cat_font = get_font(fonts, 'body_bold', 14)
        cat_text = options['category'].upper()
        cat_bbox = draw.textbbox((0, 0), cat_text, font=cat_font)
        cat_w = cat_bbox[2] - cat_bbox[0] + 24
        cat_h = cat_bbox[3] - cat_bbox[1] + 12
        draw.rounded_rectangle(
            [margin_x, y_cursor, margin_x + cat_w, y_cursor + cat_h],
            radius=4,
            fill=bg_secondary,
        )
        draw.text(
            (margin_x + 12, y_cursor + 6),
            cat_text,
            font=cat_font,
            fill=tokens['color']['text_primary'],
        )
        y_cursor += cat_h + 24

    # Title
    title_font_size = _calc_title_size(options['title'], width, options['platform'])
    title_font = get_font(fonts, 'heading', title_font_size)
    title_lines = _wrap_text(draw, options['title'], title_font, width - 2 * margin_x)
    for line in title_lines:
        draw.text(
            (margin_x, y_cursor),
            line,
            font=title_font,
            fill=tokens['color']['text_on_brand'],
        )
        y_cursor += title_font_size * 1.2

    # Subtitle
    if options.get('subtitle'):
        y_cursor += 16
        sub_font = get_font(fonts, 'body', 18)
        sub_lines = _wrap_text(draw, options['subtitle'], sub_font, width - 2 * margin_x)
        for line in sub_lines:
            draw.text(
                (margin_x, y_cursor),
                line,
                font=sub_font,
                fill=(*_hex_to_rgb(tokens['color']['text_on_brand']), 200),
            )
            y_cursor += 26

    # Accent bar
    bar_y = height - margin_y - 60
    draw.rectangle(
        [margin_x, bar_y, margin_x + 80, bar_y + 4],
        fill=bg_secondary,
    )

    # Logo (bottom-right, respecting clear space)
    if options.get('logo_path') and os.path.exists(options['logo_path']):
        logo = Image.open(options['logo_path']).convert('RGBA')
        logo_h = 32
        logo_w = int(logo.width * (logo_h / logo.height))
        logo = logo.resize((logo_w, logo_h), Image.LANCZOS)
        logo_x = width - margin_x - logo_w
        logo_y = height - margin_y - logo_h
        img.paste(logo, (logo_x, logo_y), logo)

    # Save
    img.save(output_path, quality=95)
    return output_path
```

### Node.js (satori + resvg)

```javascript
const satori = require('satori');
const { Resvg } = require('@resvg/resvg-js');

async function generateSocialCard(tokens, fonts, outputPath, options) {
  const dims = {
    linkedin: { width: 1200, height: 627 },
    twitter: { width: 1200, height: 675 },
    instagram: { width: 1080, height: 1080 },
    og: { width: 1200, height: 630 },
  };
  const { width, height } = dims[options.platform];

  // JSX-like structure for satori
  const svg = await satori(
    {
      type: 'div',
      props: {
        style: {
          width: '100%',
          height: '100%',
          display: 'flex',
          flexDirection: 'column',
          justifyContent: 'center',
          padding: '64px 96px',
          backgroundColor: tokens.color.brand_primary,
          fontFamily: 'Inter',
        },
        children: [
          options.category && {
            type: 'div',
            props: {
              style: {
                fontSize: 14,
                fontWeight: 700,
                textTransform: 'uppercase',
                letterSpacing: '0.05em',
                color: tokens.color.text_primary,
                backgroundColor: tokens.color.brand_secondary,
                padding: '6px 16px',
                borderRadius: 4,
                alignSelf: 'flex-start',
                marginBottom: 24,
              },
              children: options.category,
            },
          },
          {
            type: 'div',
            props: {
              style: {
                fontSize: options.title.length > 60 ? 32 : 44,
                fontWeight: 700,
                color: '#FFFFFF',
                lineHeight: 1.15,
                marginBottom: 16,
              },
              children: options.title,
            },
          },
          options.subtitle && {
            type: 'div',
            props: {
              style: {
                fontSize: 20,
                color: 'rgba(255,255,255,0.8)',
                lineHeight: 1.4,
              },
              children: options.subtitle,
            },
          },
          // Accent bar
          {
            type: 'div',
            props: {
              style: {
                width: 80,
                height: 4,
                backgroundColor: tokens.color.brand_secondary,
                marginTop: 'auto',
              },
            },
          },
        ].filter(Boolean),
      },
    },
    { width, height, fonts }
  );

  const resvg = new Resvg(svg, { fitTo: { mode: 'width', value: width } });
  const pngData = resvg.render().asPng();
  require('fs').writeFileSync(outputPath, pngData);
}
```

---

## Icon Generation

### Favicon & App Icon Set

```python
def generate_icon_set(tokens, logo_path, output_dir):
    """Generate complete icon set from logo/mark.

    Produces:
      favicon-32.png, favicon-16.png, apple-touch-icon.png,
      icon-192.png, icon-512.png, favicon.ico
    """
    sizes = {
        'favicon-16': (16, 16, 1),       # (width, height, padding_ratio)
        'favicon-32': (32, 32, 0),
        'apple-touch-icon': (180, 180, 0.1),
        'icon-192': (192, 192, 0.1),
        'icon-512': (512, 512, 0.1),
    }

    logo = Image.open(logo_path).convert('RGBA')

    for name, (w, h, pad_ratio) in sizes.items():
        icon = Image.new('RGBA', (w, h), _hex_to_rgba(tokens['color']['brand_primary']))

        # Scale logo with padding
        pad = int(w * pad_ratio)
        inner = w - 2 * pad
        logo_resized = logo.resize((inner, inner), Image.LANCZOS)
        icon.paste(logo_resized, (pad, pad), logo_resized)

        icon.save(os.path.join(output_dir, f'{name}.png'))

    # Generate .ico (multi-size)
    img_16 = Image.open(os.path.join(output_dir, 'favicon-16.png'))
    img_32 = Image.open(os.path.join(output_dir, 'favicon-32.png'))
    img_32.save(
        os.path.join(output_dir, 'favicon.ico'),
        format='ICO',
        sizes=[(16, 16), (32, 32)],
    )
```

### Android Adaptive Icon

```python
def generate_adaptive_icon(tokens, logo_path, output_dir):
    """Generate Android adaptive icon layers.

    Adaptive icons have:
      - Background layer (512x512, solid brand color)
      - Foreground layer (512x512, logo centered in safe zone)
    Safe zone is inner 66% (circular mask area).
    """
    size = 512
    safe_zone = int(size * 0.66)
    offset = (size - safe_zone) // 2

    # Background layer
    bg = Image.new('RGB', (size, size), _hex_to_rgb(tokens['color']['brand_primary']))
    bg.save(os.path.join(output_dir, 'adaptive-background.png'))

    # Foreground layer (transparent with centered logo)
    fg = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    logo = Image.open(logo_path).convert('RGBA')
    logo_resized = logo.resize((safe_zone, safe_zone), Image.LANCZOS)
    fg.paste(logo_resized, (offset, offset), logo_resized)
    fg.save(os.path.join(output_dir, 'adaptive-foreground.png'))
```

---

## Email Banner

```python
def generate_email_banner(tokens, fonts, output_path, options):
    """Generate a branded email banner (600x200).

    Constraints:
      - 600px wide (email standard)
      - No transparency (email clients)
      - Simple layout (limited CSS in emails)
      - Web-safe colors, no gradients in some clients
    """
    width, height = 600, 200
    img = Image.new('RGB', (width, height), _hex_to_rgb(tokens['color']['brand_primary']))
    draw = ImageDraw.Draw(img)

    # Accent stripe at bottom
    stripe_h = 4
    draw.rectangle(
        [0, height - stripe_h, width, height],
        fill=tokens['color']['brand_secondary'],
    )

    # Logo (left-aligned, vertically centered)
    margin = 32
    if options.get('logo_path') and os.path.exists(options['logo_path']):
        logo = Image.open(options['logo_path']).convert('RGBA')
        logo_h = 40
        logo_w = int(logo.width * (logo_h / logo.height))
        logo = logo.resize((logo_w, logo_h), Image.LANCZOS)
        logo_y = (height - logo_h) // 2
        # Composite onto RGB
        temp = Image.new('RGBA', (width, height), (*_hex_to_rgb(tokens['color']['brand_primary']), 255))
        temp.paste(logo, (margin, logo_y), logo)
        img = temp.convert('RGB')
        draw = ImageDraw.Draw(img)
        text_x = margin + logo_w + 24
    else:
        text_x = margin

    # Title text
    if options.get('title'):
        title_font = get_font(fonts, 'heading', 22)
        draw.text(
            (text_x, height // 2 - 14),
            options['title'],
            font=title_font,
            fill='#FFFFFF',
        )

    img.save(output_path, format='PNG')
```

---

## Blog / Article Header

```python
def generate_blog_header(tokens, fonts, output_path, options):
    """Generate a branded blog header image (1200x630).

    Args:
        options: {
            'title': str,
            'author': str (optional),
            'date': str (optional),
            'variant': 'solid' | 'split' | 'minimal',
        }
    """
    width, height = 1200, 630
    img = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(img)

    if options.get('variant') == 'split':
        # Left half: brand color with text. Right half: subtle pattern/color
        mid = width // 2
        draw.rectangle([0, 0, mid, height], fill=tokens['color']['brand_primary'])
        draw.rectangle([mid, 0, width, height], fill=tokens['color']['surface_subtle'])
    elif options.get('variant') == 'minimal':
        draw.rectangle([0, 0, width, height], fill=tokens['color']['surface_default'])
    else:
        draw.rectangle([0, 0, width, height], fill=tokens['color']['brand_primary'])

    margin_x = 96
    margin_y = 80
    text_color = (
        tokens['color']['text_primary']
        if options.get('variant') == 'minimal'
        else '#FFFFFF'
    )

    # Title
    title_size = 40 if len(options['title']) > 50 else 48
    title_font = get_font(fonts, 'heading', title_size)
    max_w = (width // 2 - margin_x - 24) if options.get('variant') == 'split' else (width - 2 * margin_x)
    lines = _wrap_text(draw, options['title'], title_font, max_w)
    y = margin_y
    for line in lines:
        draw.text((margin_x, y), line, font=title_font, fill=text_color)
        y += int(title_size * 1.2)

    # Accent bar below title
    y += 16
    bar_color = (
        tokens['color']['brand_primary']
        if options.get('variant') == 'minimal'
        else tokens['color']['brand_secondary']
    )
    draw.rectangle([margin_x, y, margin_x + 80, y + 4], fill=bar_color)

    # Author / date
    if options.get('author') or options.get('date'):
        meta_parts = [p for p in [options.get('author'), options.get('date')] if p]
        meta_text = ' \u00b7 '.join(meta_parts)
        meta_font = get_font(fonts, 'body', 16)
        meta_color = (
            tokens['color']['text_secondary']
            if options.get('variant') == 'minimal'
            else 'rgba(255,255,255,0.7)'
        )
        draw.text((margin_x, height - margin_y), meta_text, font=meta_font, fill=meta_color)

    img.save(output_path, quality=95)
```

---

## Presentation Slide Export

Export slide-master layouts as static PNG images:

```python
def export_slide_as_image(tokens, fonts, slide_data, output_path):
    """Export a single slide as a 1920x1080 PNG.

    Args:
        slide_data: {
            'master': 'title' | 'content' | 'data' | 'comparison' | 'closing',
            'title': str,
            'subtitle': str (optional),
            'body': str (optional),
            'metrics': list (optional, for data master),
            'background': 'brand' | 'white' | 'dark',
        }
    """
    width, height = 1920, 1080
    img = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(img)

    # Background
    bg_map = {
        'brand': tokens['color']['brand_primary'],
        'white': tokens['color']['surface_default'],
        'dark': '#111827',
    }
    bg_color = bg_map.get(slide_data.get('background', 'white'), tokens['color']['surface_default'])
    draw.rectangle([0, 0, width, height], fill=bg_color)

    is_dark = slide_data.get('background') in ('brand', 'dark')
    text_color = '#FFFFFF' if is_dark else tokens['color']['text_primary']
    sub_color = 'rgba(255,255,255,0.7)' if is_dark else tokens['color']['text_secondary']

    margin = 120  # Presentation margin (generous)

    if slide_data['master'] == 'title':
        # Title slide: centered, large text
        title_font = get_font(fonts, 'heading', 64)
        lines = _wrap_text(draw, slide_data['title'], title_font, width - 2 * margin)
        total_h = len(lines) * 72
        y = (height - total_h) // 2 - 40
        for line in lines:
            bbox = draw.textbbox((0, 0), line, font=title_font)
            line_w = bbox[2] - bbox[0]
            draw.text(((width - line_w) // 2, y), line, font=title_font, fill=text_color)
            y += 72

        # Accent bar centered
        bar_w = 120
        draw.rectangle(
            [(width - bar_w) // 2, y + 16, (width + bar_w) // 2, y + 20],
            fill=tokens['color']['brand_secondary'],
        )

        if slide_data.get('subtitle'):
            sub_font = get_font(fonts, 'body', 24)
            bbox = draw.textbbox((0, 0), slide_data['subtitle'], font=sub_font)
            sub_w = bbox[2] - bbox[0]
            draw.text(((width - sub_w) // 2, y + 48), slide_data['subtitle'], font=sub_font, fill=sub_color)

    elif slide_data['master'] == 'data':
        # Data slide: title top, metric cards in grid
        title_font = get_font(fonts, 'heading', 36)
        draw.text((margin, margin), slide_data['title'], font=title_font, fill=text_color)

        if slide_data.get('metrics'):
            _draw_metric_grid(draw, fonts, tokens, slide_data['metrics'],
                              margin, margin + 80, width - 2 * margin, height - margin - 80 - margin,
                              is_dark)

    # Other masters follow similar patterns...

    img.save(output_path, quality=95)
```

---

## Diagram Backgrounds

```python
def generate_diagram_background(tokens, output_path, options):
    """Generate a branded diagram/whiteboard background.

    Args:
        options: {
            'width': int,
            'height': int,
            'grid': bool (show dot grid),
            'grid_spacing': int (default 24),
            'variant': 'light' | 'dark' | 'brand',
        }
    """
    width = options.get('width', 1600)
    height = options.get('height', 900)
    img = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(img)

    # Background
    if options.get('variant') == 'dark':
        bg = '#111827'
        dot_color = '#374151'
    elif options.get('variant') == 'brand':
        bg = tokens['color']['brand_primary']
        dot_color = _lighten(tokens['color']['brand_primary'], 0.15)
    else:
        bg = tokens['color']['surface_default']
        dot_color = tokens['color']['border_default']

    draw.rectangle([0, 0, width, height], fill=bg)

    # Dot grid
    if options.get('grid', True):
        spacing = options.get('grid_spacing', 24)
        for x in range(spacing, width, spacing):
            for y in range(spacing, height, spacing):
                draw.ellipse([x - 1, y - 1, x + 1, y + 1], fill=dot_color)

    img.save(output_path, format='PNG')
```

---

## Utility Functions

```python
import os
from PIL import Image, ImageDraw

def _hex_to_rgb(hex_color):
    """Convert hex color string to RGB tuple."""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def _hex_to_rgba(hex_color, alpha=255):
    """Convert hex color string to RGBA tuple."""
    r, g, b = _hex_to_rgb(hex_color)
    return (r, g, b, alpha)

def _wrap_text(draw, text, font, max_width):
    """Wrap text to fit within max_width. Returns list of lines."""
    words = text.split()
    lines = []
    current = ''
    for word in words:
        test = f'{current} {word}'.strip()
        bbox = draw.textbbox((0, 0), test, font=font)
        if bbox[2] - bbox[0] <= max_width:
            current = test
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines

def _draw_gradient(img, color_start, color_end, direction='horizontal'):
    """Draw a linear gradient on the image."""
    w, h = img.size
    r1, g1, b1 = _hex_to_rgb(color_start)
    r2, g2, b2 = _hex_to_rgb(color_end)

    for i in range(w if direction == 'horizontal' else h):
        ratio = i / (w if direction == 'horizontal' else h)
        r = int(r1 + (r2 - r1) * ratio)
        g = int(g1 + (g2 - g1) * ratio)
        b = int(b1 + (b2 - b1) * ratio)
        if direction == 'horizontal':
            ImageDraw.Draw(img).line([(i, 0), (i, h)], fill=(r, g, b))
        elif direction == 'vertical':
            ImageDraw.Draw(img).line([(0, i), (w, i)], fill=(r, g, b))
        elif direction == 'diagonal':
            # Approximate diagonal gradient
            ImageDraw.Draw(img).line([(i, 0), (i, h)], fill=(r, g, b))

def _lighten(hex_color, amount):
    """Lighten a hex color by a fraction (0.0-1.0)."""
    r, g, b = _hex_to_rgb(hex_color)
    r = min(255, int(r + (255 - r) * amount))
    g = min(255, int(g + (255 - g) * amount))
    b = min(255, int(b + (255 - b) * amount))
    return f'#{r:02x}{g:02x}{b:02x}'

def _calc_title_size(title, img_width, platform):
    """Calculate appropriate title font size based on text length and platform."""
    char_count = len(title)
    if platform == 'instagram':
        return 48 if char_count < 30 else 36 if char_count < 60 else 28
    return 44 if char_count < 40 else 36 if char_count < 70 else 28

def _draw_metric_grid(draw, fonts, tokens, metrics, x, y, w, h, is_dark):
    """Draw a grid of metric cards within the given bounds."""
    count = len(metrics)
    cols = min(count, 4)
    rows = (count + cols - 1) // cols
    card_w = (w - (cols - 1) * 24) // cols
    card_h = (h - (rows - 1) * 24) // rows

    for i, metric in enumerate(metrics):
        col = i % cols
        row = i // cols
        cx = x + col * (card_w + 24)
        cy = y + row * (card_h + 24)

        # Card background
        card_bg = 'rgba(255,255,255,0.1)' if is_dark else tokens['color']['surface_subtle']
        draw.rounded_rectangle(
            [cx, cy, cx + card_w, cy + card_h],
            radius=8,
            fill=card_bg,
        )

        # Value (large number)
        val_font = get_font(fonts, 'mono', 48)
        value_text = str(metric.get('value', ''))
        draw.text((cx + 24, cy + 24), value_text, font=val_font,
                   fill='#FFFFFF' if is_dark else tokens['color']['text_primary'])

        # Label
        label_font = get_font(fonts, 'body', 16)
        draw.text((cx + 24, cy + card_h - 48), metric.get('label', ''),
                   font=label_font,
                   fill='rgba(255,255,255,0.7)' if is_dark else tokens['color']['text_secondary'])
```

---

## Format Selection Guide

| Scenario | Format | Compression | Notes |
|----------|--------|-------------|-------|
| Social cards, OG images | PNG | Lossless | Sharp text, clean edges |
| Photo-heavy backgrounds | JPEG | quality=90 | Smaller file size |
| Web delivery (modern) | WebP | quality=85 | 25-35% smaller than JPEG |
| Icons with transparency | PNG | Lossless | Alpha channel required |
| Favicons | ICO + PNG | - | ICO for legacy, PNG for modern |
| Diagrams, technical | SVG | - | Scalable, editable |
| Print (300 DPI) | PNG/TIFF | Lossless | High resolution required |

### Resolution Guide

| Context | DPI | Multiplier | Example: 1200x630 card |
|---------|-----|------------|------------------------|
| Screen / web | 72 | @1x | 1200 x 630 px |
| Retina / HiDPI | 144 | @2x | 2400 x 1260 px |
| Print (standard) | 150 | - | Scale to physical size |
| Print (high quality) | 300 | - | Scale to physical size |

```python
def generate_retina(generate_fn, tokens, fonts, output_path, options, scale=2):
    """Wrapper to generate @2x retina images.

    Renders at 2x dimensions, saves at full resolution.
    Consumer should serve with CSS: width={original_w}px, height={original_h}px.
    """
    # Temporarily double all dimension-related values
    retina_options = {**options, '_scale': scale}
    # The generate function should check for _scale and multiply dimensions
    generate_fn(tokens, fonts, output_path.replace('.png', '@2x.png'), retina_options)
```

---

## Logo Compositing Rules

From Phase 6 (Logo) intake decisions:

| Rule | Guidance |
|------|----------|
| **Clear space** | Minimum clear space = logo height on all sides. No text or graphic elements within this zone. |
| **Minimum size** | Digital: 24px height minimum. Print: 10mm height minimum. |
| **On brand primary** | Use white (knockout) version of logo. |
| **On white/light** | Use full-color or dark version of logo. |
| **On photography** | Use white version with minimum 60% opacity dark overlay on image. |
| **On brand secondary** | Use dark version. Test contrast; secondary may be light. |
| **Placement** | Default: bottom-right for social cards, top-left for documents, centered for icons. |
| **Do not** | Rotate, stretch, apply effects, change colors, or place on busy backgrounds without overlay. |

---

## Accessibility

| Requirement | Guidance |
|-------------|----------|
| **Text contrast** | All text overlaid on images must meet WCAG 2.1 AA (4.5:1 for body, 3:1 for large text 24px+). Use dark overlays on photos. |
| **Alt text** | Every generated image must be accompanied by descriptive alt text. Social cards: `"{title} - {brand_name} {category}"`. Icons: `"{brand_name} logo"`. |
| **Color not sole indicator** | If images convey data (charts, diagrams), include text labels. Do not rely on color alone. |
| **Animated content** | If generating animated images (GIF), provide `prefers-reduced-motion` static fallback. Keep animations under 5 seconds or provide pause control. |
| **Text in images** | Minimize text baked into images. For critical content, ensure the text is also available in HTML/document context. Social cards are acceptable as supplementary. |

---

## Feeding Questions

This export is fed by answers from:
- **Phase 0:** Material extraction (existing social card styles, image assets, logo files)
- **Phase 1:** Color identity (brand colors, accent colors, data series palette)
- **Phase 2:** Typography (font families, heading/body weights)
- **Phase 3:** Layout (spacing preferences, margins)
- **Phase 6:** Logo (logo files, clear space rules, placement, minimum size, color variants)
- **Phase 7:** Photography/imagery (image treatment, background patterns, overlay opacity)

See `references/question-deliverable-map.md` for complete traceability.
