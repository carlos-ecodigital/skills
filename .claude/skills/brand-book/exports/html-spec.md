# HTML Design System Spec

Agent-readable instructions for generating a self-contained, interactive, single-page HTML design system document for any brand. The output serves as both internal reference (browsable source of truth for the brand's visual system) and external media kit base (strip internal sections for a clean brand guidelines PDF via browser print).

Modeled on Carbon Design System structure. Zero external dependencies except Google Fonts CDN.

## Output

Single file: `{brand-slug}-design-system.html`

- **Target size:** <2MB including base64 images
- **External deps:** Google Fonts CDN `<link>` only
- **Logo:** Base64-encoded inline (PNG) or raw SVG inline
- **Responsive:** Sidebar nav collapses to hamburger on mobile
- **Print-friendly:** `@media print` styles for clean PDF export

---

## Generation Approach

The agent reads all token files + brand-config, then constructs the HTML string programmatically. No template engine required — plain string concatenation or template literals.

### Required Inputs

| Input | Source | Purpose |
|-------|--------|---------|
| Brand config | `brand-configs/{brand}.md` | Brand name, description, audiences, personality |
| Primitive tokens | `tokens/primitives.tokens.json` | Raw values: colors, sizes, spacing |
| Semantic tokens | `tokens/semantic.tokens.json` | Mapped values: surface, text, border, brand |
| Component tokens | `tokens/component.tokens.json` | UI component specs: buttons, cards, inputs |
| CSS variables | `exports/css-variables.css` | Embed directly into `<style>` |
| Logo files | From brand materials | Base64-encode or inline SVG |

### Build Steps

1. Read all inputs listed above
2. Parse JSON tokens into lookup maps
3. Construct HTML string section-by-section (see Page Structure below)
4. Inline CSS: embed css-variables.css content + page-specific styles
5. Inline JS: dark/light toggle, smooth-scroll nav, copy-to-clipboard, expandable sections
6. Write single `.html` file

---

## HTML Document Structure

```html
<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{Brand Name} Design System</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family={heading-font}:wght@400;500;600;700&family={body-font}:wght@400;500;600;700&family={mono-font}&display=swap" rel="stylesheet">
  <style>/* All CSS inlined here — see CSS Architecture section */</style>
</head>
<body>
  <nav id="sidebar"><!-- Sidebar navigation --></nav>
  <main id="content"><!-- All sections --></main>
  <script>/* All JS inlined here — see JavaScript section */</script>
</body>
</html>
```

---

## Page Structure & Sections

### 1. Sidebar Navigation

Fixed left sidebar (280px) with brand logo, section links, and dark/light toggle.

```html
<nav id="sidebar">
  <div class="sidebar-header">
    <img src="data:image/svg+xml;base64,{logo}" alt="{Brand Name}" class="sidebar-logo">
    <span class="sidebar-brand-name">{Brand Name}</span>
  </div>
  <ul class="sidebar-nav">
    <li><a href="#hero" class="nav-link active">Overview</a></li>
    <li class="nav-group">
      <span class="nav-group-label">Foundation</span>
      <ul>
        <li><a href="#colors">Colors</a></li>
        <li><a href="#typography">Typography</a></li>
        <li><a href="#spacing">Spacing</a></li>
        <li><a href="#elevation">Elevation</a></li>
        <li><a href="#motion">Motion</a></li>
      </ul>
    </li>
    <li class="nav-group">
      <span class="nav-group-label">Components</span>
      <ul>
        <li><a href="#buttons">Buttons</a></li>
        <li><a href="#inputs">Inputs</a></li>
        <li><a href="#cards">Cards</a></li>
        <li><a href="#tables">Tables</a></li>
        <li><a href="#callouts">Callouts</a></li>
        <li><a href="#badges">Badges & Tags</a></li>
        <li><a href="#modals">Modals</a></li>
        <li><a href="#toasts">Toasts</a></li>
        <li><a href="#tooltips">Tooltips</a></li>
        <li><a href="#toggles">Toggles</a></li>
        <li><a href="#skeleton">Loading States</a></li>
        <li><a href="#dividers">Dividers</a></li>
        <li><a href="#charts">Charts</a></li>
      </ul>
    </li>
    <li class="nav-group">
      <span class="nav-group-label">Patterns</span>
      <ul>
        <li><a href="#logo-usage">Logo Usage</a></li>
        <li><a href="#photography">Photography</a></li>
        <li><a href="#data-viz">Data Visualization</a></li>
        <li><a href="#responsive">Responsive</a></li>
        <li><a href="#dark-light">Dark / Light Mode</a></li>
      </ul>
    </li>
    <li class="nav-group">
      <span class="nav-group-label">Resources</span>
      <ul>
        <li><a href="#accessibility">Accessibility</a></li>
        <li><a href="#token-architecture">Token Architecture</a></li>
        <li><a href="#downloads">Downloads</a></li>
        <li><a href="#dos-donts">Do & Don't</a></li>
      </ul>
    </li>
  </ul>
  <div class="sidebar-footer">
    <button id="theme-toggle" aria-label="Toggle dark mode">
      <span class="toggle-icon-light">☀</span>
      <span class="toggle-icon-dark">☾</span>
    </button>
    <span class="sidebar-version">v{version} · {date}</span>
  </div>
</nav>
```

**Mobile behavior:** At `<768px`, sidebar becomes hamburger menu (fixed top bar, slide-in overlay).

---

### 2. Hero / Overview Section

Brand identity summary with primary swatches and type specimen.

```html
<section id="hero" class="section">
  <div class="hero-content">
    <h1>{Brand Name} Design System</h1>
    <p class="hero-subtitle">{brand-config description or tagline}</p>
    <div class="hero-swatches">
      <!-- Primary, secondary, accent swatches -->
      <div class="swatch swatch-large" style="background: var(--color-brand-primary)">
        <span class="swatch-label">Primary</span>
        <span class="swatch-value">{hex}</span>
      </div>
      <!-- Repeat for secondary, accent -->
    </div>
    <div class="hero-type-specimen">
      <span class="specimen-heading" style="font-family: var(--font-heading)">{heading font} · Heading</span>
      <span class="specimen-body" style="font-family: var(--font-body)">{body font} · Body</span>
      <span class="specimen-mono" style="font-family: var(--font-mono)">{mono font} · Data</span>
    </div>
  </div>
</section>
```

---

### 3. Foundation Sections

#### 3.1 Color System (`#colors`)

**Sub-sections:**

**Primitive hue ladders:** Render each color family (primary, secondary, accent, success, warning, error, info, neutral) as a horizontal row of 11 swatches (50–950). Each swatch shows hex value, contrast ratio against white and black.

```html
<div class="color-family">
  <h4>Primary</h4>
  <div class="color-row">
    <!-- For each shade 50-950 -->
    <div class="color-swatch" style="background: {hex}">
      <span class="swatch-shade">{shade}</span>
      <span class="swatch-hex">{hex}</span>
      <span class="swatch-contrast">↑{ratio-vs-white} ↓{ratio-vs-black}</span>
    </div>
  </div>
</div>
```

**Semantic color mappings:** Table showing token name → resolved hex → usage description.

| Token | Value | Usage |
|-------|-------|-------|
| `color.brand.primary` | `{hex}` | Primary brand identity, nav, key UI |
| `color.surface.default` | `{hex}` | Page background |
| ... | ... | ... |

**Audience accent palette:** (If brand-config defines audience segments) Grid of audience-specific accent colors with segment name, hex, and use case.

**Data viz palette:** Ordered series colors for charts (series-1 through series-6+), with sequential and diverging variants if defined.

**Accessibility badges:** For every semantic text/surface pairing, render a badge showing contrast ratio and WCAG AA/AAA pass/fail.

```html
<div class="a11y-badge pass">
  <span class="a11y-pairing">{text-token} on {surface-token}</span>
  <span class="a11y-ratio">{ratio}:1</span>
  <span class="a11y-level">AA ✓</span>
</div>
```

#### 3.2 Typography (`#typography`)

**Font specimens:** For each font family (heading, body, mono), render the full alphabet, numbers 0–9, and special characters in the actual font.

**Type scale table:** Render all `font.size.*` tokens as actual-size text samples.

```html
<div class="type-scale-row">
  <span class="type-token">font.size.{name}</span>
  <span class="type-size">{value}</span>
  <span class="type-sample" style="font-size: {value}">{Sample text}</span>
</div>
```

**Weight reference:** Show each available weight (400, 500, 600, 700) as a text sample.

**Line height reference:** Show each line-height option with multi-line sample text.

**Usage rules:** Table mapping context → font family + weight + size (from component tokens).

#### 3.3 Spacing (`#spacing`)

**Scale visualization:** Render spacing tokens as visual bars with pixel dimensions.

```html
<div class="spacing-row">
  <span class="spacing-token">space.{n}</span>
  <span class="spacing-value">{value}</span>
  <div class="spacing-bar" style="width: {value}; height: 16px; background: var(--color-brand-primary)"></div>
</div>
```

**Contextual guide:** Table showing where each spacing value is used (component padding, section gaps, grid gutters).

#### 3.4 Elevation (`#elevation`)

**Z-index stack:** Visual stack diagram showing all 10 z-index levels with labels and values.

```html
<div class="z-stack">
  <!-- Rendered bottom-to-top -->
  <div class="z-level" style="z-index: {value}; transform: translateY({offset}px)">
    <span class="z-name">{name}</span>
    <span class="z-value">{value}</span>
  </div>
</div>
```

**Shadow examples:** Render each shadow token as a card with that shadow applied.

**Philosophy note:** Display the brand's elevation philosophy (shadow-based / background-based / hybrid) from `primitives.elevation.philosophy`.

#### 3.5 Motion (`#motion`)

**Duration scale:** For each duration token, render a bar that animates at that speed on hover/click.

**Easing curves:** For each easing token, render a CSS cubic-bezier visualization (animated dot tracing the curve).

**Personality examples:** Show motion tokens applied to real interactions: button hover, card entrance, page transition.

---

### 4. Component Sections

Each component section follows the same structure:

```html
<section id="{component}" class="section">
  <h2>{Component Name}</h2>
  <p class="section-desc">{purpose description from component token $extensions}</p>

  <!-- Live demo -->
  <div class="demo-container">
    <div class="demo-preview">
      <!-- Rendered component with actual token values -->
    </div>
    <div class="demo-tokens">
      <!-- Token reference table -->
    </div>
  </div>

  <!-- Variants (if applicable) -->
  <h3>Variants</h3>
  <div class="variant-grid">
    <!-- Each variant rendered side by side -->
  </div>

  <!-- States (if applicable) -->
  <h3>States</h3>
  <div class="state-grid">
    <!-- default, hover, focus, active, disabled -->
  </div>

  <!-- Do & Don't (from $extensions if present) -->
  <div class="do-dont-row">
    <div class="do-card">
      <span class="do-label">✓ Do</span>
      <p>{do text from $extensions}</p>
    </div>
    <div class="dont-card">
      <span class="dont-label">✗ Don't</span>
      <p>{dont text from $extensions}</p>
    </div>
  </div>
</section>
```

#### 4.1 Buttons (`#buttons`)

Render all button states and variants from `component.button.*`:
- **Primary** (filled): default, hover, active, disabled
- **Secondary** (outlined): default, hover, active, disabled
- **Ghost** (text-only): default, hover, active, disabled
- **Sizes:** sm, md, lg (if defined)
- **With icons:** leading icon, trailing icon

#### 4.2 Inputs (`#inputs`)

Render from `component.input.*`:
- **Text input:** default, hover, focus (with ring), error (with help text), disabled
- **Textarea:** same states
- **Checkbox** from `component.checkbox.*`: off, on, indeterminate, disabled
- **Radio** from `component.radio.*`: off, on, disabled
- **Select** from `component.select.*`: closed, open (dropdown visible), with options

All inputs should be interactive (actual `<input>`, `<select>`, `<textarea>` elements styled with brand tokens).

#### 4.3 Cards (`#cards`)

Render from `component.card.*`:
- **Default card:** with title, body text, optional image
- **Hover state:** show elevation/shadow change on hover
- **Metric card:** large number + label + trend indicator
- **Audience-tinted card:** (if audience accents defined) card with left border in audience color

#### 4.4 Tables (`#tables`)

Render from `component.table.*`:
- **Standard table:** with header row, alternating row colors, border styles
- **Compact table:** tighter padding
- **Data table:** with monospace numbers, right-aligned numerics
- **Responsive behavior:** horizontal scroll wrapper on mobile

#### 4.5 Callouts (`#callouts`)

Render from `component.callout.*`:
- **Info:** blue accent
- **Success:** green accent
- **Warning:** amber accent
- **Error:** red accent
- **Audience-specific:** (if defined) callout with audience accent color

Each callout shows the left-border or top-border accent style per brand tokens.

#### 4.6 Badges & Tags (`#badges`)

Render from `component.badge.*`:
- **Status badges:** active, inactive, pending
- **Audience tags:** (if audience accents defined) one badge per audience segment
- **Size variants:** sm, md

#### 4.7 Modals (`#modals`)

Render from `component.modal.*`:
- **Demo button** that opens an actual modal overlay
- **Modal** with backdrop, container, header, body, footer
- **Animation** on open/close per modal animation tokens
- Show backdrop opacity from `modal.backdrop.opacity`

Implementation: Use a `<dialog>` element or custom overlay with JS show/hide.

#### 4.8 Toasts (`#toasts`)

Render from `component.toast.*`:
- **4 variants:** success, error, warning, info — each with semantic color
- **Demo button** that triggers a toast notification
- **Position** per `toast.position` token (top-right default)
- **Auto-dismiss** per `toast.duration` token

Implementation: JS creates toast elements, positions them, and auto-removes after duration.

#### 4.9 Tooltips (`#tooltips`)

Render from `component.tooltip.*`:
- **Demo elements** with hover-triggered tooltips
- **Positions:** top, bottom, left, right
- **Delay** per `tooltip.delay` token
- **Style:** dark background per tooltip tokens

#### 4.10 Toggles (`#toggles`)

Render from `component.toggle.*`:
- **Off state / On state** side by side
- **Interactive toggle** that actually switches
- **Disabled state**
- Show track and thumb dimensions from tokens

#### 4.11 Loading States (`#skeleton`)

Render from `component.skeleton.*`:
- **Shimmer variant:** gray shapes with animated shimmer
- **Pulse variant:** shapes with opacity pulse
- **Shape presets:** text lines, heading, avatar circle, image rectangle
- **Demo:** button to toggle between loaded content and skeleton state

#### 4.12 Dividers (`#dividers`)

Render from `component.divider.*`:
- **Horizontal rule:** default border style and color
- **Section divider:** with spacing tokens applied
- **Labeled divider:** centered text with lines on either side

#### 4.13 Charts (`#charts`)

Render from `component.chart.*` and `semantic.color.data.*`:
- **Color palette display:** ordered series swatches
- **Sample bar chart:** using data series colors (CSS-only, no chart library needed)
- **KPI card:** large metric number + label + trend
- **Citation style:** below-chart source attribution format

---

### 5. Pattern Sections

#### 5.1 Logo Usage (`#logo-usage`)

From `component.header.*` and brand-config logo rules:
- **Logo variants:** full color, white/reversed, monochrome (render each)
- **Clear space:** visual diagram showing minimum clear space around logo
- **Minimum size:** show logo at minimum allowed size
- **Do & Don't:** logo placement examples (correct vs. incorrect)

#### 5.2 Photography Style (`#photography`)

From brand-config imagery rules:
- **Style description:** industrial/facilities, editorial, abstract, etc.
- **Treatment rules:** tint, overlay, or no treatment
- **Aspect ratios:** recommended ratios for different contexts
- **Icon style:** outline, filled, or duo-tone (from intake Q7.4)

#### 5.3 Data Visualization (`#data-viz`)

From `semantic.color.data.*` and `component.chart.*`:
- **Palette order:** series-1 through series-6 swatches with descriptions
- **Sequential palette:** light-to-dark single-hue ramp
- **Diverging palette:** (if defined) two-hue diverging scale
- **Chart rules:** axis style, grid lines, label placement, citation format
- **KPI card pattern:** metric + label + trend indicator + sparkline area

#### 5.4 Responsive (`#responsive`)

From `primitives.breakpoint.*`:
- **Breakpoint table:** mobile, tablet, desktop, wide with px values
- **Layout adaptation rules:** what changes at each breakpoint
- **Component behavior:** which components stack, collapse, or hide
- **Media query reference:** copy-able CSS media query strings

#### 5.5 Dark / Light Mode (`#dark-light`)

From `semantic.color-mode.*`:
- **Side-by-side comparison:** key UI elements in light vs. dark mode
- **Token mapping table:** which tokens invert and which stay constant
- **Brand colors note:** brand identity colors remain unchanged in both modes
- **Implementation:** CSS custom property swap approach

```html
<div class="mode-comparison">
  <div class="mode-panel light">
    <h4>Light Mode</h4>
    <!-- Rendered UI snippet with light tokens -->
  </div>
  <div class="mode-panel dark">
    <h4>Dark Mode</h4>
    <!-- Same UI snippet with dark tokens -->
  </div>
</div>
```

---

### 6. Resource Sections

#### 6.1 Accessibility (`#accessibility`)

- **WCAG summary:** target level (AA or AAA), key requirements
- **Contrast ratio table:** all semantic text/surface pairings with ratios
- **Color vision deficiency:** note on palette CVD testing results
- **Focus indicators:** focus ring style from component tokens
- **Motion sensitivity:** `prefers-reduced-motion` support note

#### 6.2 Token Architecture (`#token-architecture`)

- **3-tier diagram:** Primitive → Semantic → Component with arrows
- **Token counts:** number of tokens per tier
- **Naming convention:** `{tier}.{category}.{property}.{variant}` pattern
- **Example chain:** trace one value from primitive through semantic to component

*Internal only — strip this section for external media kit.*

#### 6.3 Downloads (`#downloads`)

- **Export formats available:** Tailwind config, CSS variables, Remotion theme, Figma variables
- **File descriptions:** what each export contains and how to use it
- **Copy buttons:** for quick CSS variable or Tailwind snippets

*Internal only — strip this section for external media kit.*

#### 6.4 Do & Don't (`#dos-donts`)

Aggregate all `$extensions.do` and `$extensions.dont` from component tokens into a visual gallery:

```html
<div class="do-dont-grid">
  <div class="do-dont-pair">
    <div class="do-example">
      <div class="do-label">✓ Do</div>
      <div class="do-visual"><!-- Rendered correct example --></div>
      <p>{do text}</p>
    </div>
    <div class="dont-example">
      <div class="dont-label">✗ Don't</div>
      <div class="dont-visual"><!-- Rendered incorrect example --></div>
      <p>{dont text}</p>
    </div>
  </div>
</div>
```

---

## CSS Architecture

All CSS is inlined in a single `<style>` block. Structure:

```css
/* === 1. CSS VARIABLES (from css-variables.css) === */
:root { /* Embed full css-variables.css content here */ }

/* Dark mode overrides */
[data-theme="dark"] {
  --color-surface-default: {dark.surface-default resolved};
  --color-surface-subtle: {dark.surface-subtle resolved};
  --color-text-primary: {dark.text-primary resolved};
  --color-text-secondary: {dark.text-secondary resolved};
  --color-text-heading: {dark.text-heading resolved};
  --color-border-default: {dark.border-default resolved};
  --color-border-subtle: {dark.border-subtle resolved};
}

/* === 2. RESET & BASE === */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html { scroll-behavior: smooth; font-size: 16px; }
body {
  font-family: var(--font-body);
  color: var(--color-text-primary);
  background: var(--color-surface-default);
  line-height: var(--line-height-normal);
  display: flex;
}

/* === 3. LAYOUT === */
#sidebar {
  position: fixed;
  left: 0; top: 0; bottom: 0;
  width: 280px;
  background: var(--color-surface-subtle);
  border-right: 1px solid var(--color-border-default);
  overflow-y: auto;
  z-index: 40; /* elevation.zindex.overlay */
  padding: var(--space-6) 0;
  transition: transform 0.3s var(--ease-default);
}

#content {
  margin-left: 280px;
  padding: var(--space-8) var(--space-10);
  max-width: 960px;
  width: 100%;
}

/* === 4. SECTION STYLES === */
.section { margin-bottom: var(--space-16); }
.section h2 {
  font-family: var(--font-heading);
  font-size: var(--font-size-2xl);
  font-weight: var(--font-weight-bold);
  color: var(--color-text-heading);
  margin-bottom: var(--space-6);
  padding-bottom: var(--space-3);
  border-bottom: 2px solid var(--color-brand-primary);
}

/* === 5. COMPONENT DEMO STYLES === */
.demo-container {
  background: var(--color-surface-subtle);
  border: 1px solid var(--color-border-default);
  border-radius: var(--radius-md);
  padding: var(--space-6);
  margin: var(--space-4) 0;
}

.demo-preview {
  padding: var(--space-6);
  background: var(--color-surface-default);
  border-radius: var(--radius-sm);
  margin-bottom: var(--space-4);
}

.demo-tokens {
  font-family: var(--font-mono);
  font-size: var(--font-size-xs);
  color: var(--color-text-secondary);
}

/* === 6. SWATCH & COLOR STYLES === */
.color-row { display: flex; gap: 2px; margin-bottom: var(--space-4); }
.color-swatch {
  flex: 1;
  aspect-ratio: 1;
  min-width: 60px;
  display: flex; flex-direction: column;
  justify-content: flex-end;
  padding: var(--space-2);
  font-size: 10px;
  border-radius: var(--radius-sm);
}
/* Auto text color for readability */
.color-swatch.light-bg { color: var(--color-neutral-900); }
.color-swatch.dark-bg { color: var(--color-neutral-50); }

/* === 7. DO & DON'T STYLES === */
.do-dont-row { display: grid; grid-template-columns: 1fr 1fr; gap: var(--space-4); }
.do-card { border-left: 3px solid var(--color-success); padding: var(--space-4); }
.dont-card { border-left: 3px solid var(--color-error); padding: var(--space-4); }

/* === 8. RESPONSIVE === */
@media (max-width: 768px) {
  #sidebar {
    transform: translateX(-100%);
    width: 280px;
  }
  #sidebar.open { transform: translateX(0); }
  #content { margin-left: 0; padding: var(--space-4); }
  .mobile-header {
    display: flex;
    position: fixed; top: 0; left: 0; right: 0;
    height: 56px;
    background: var(--color-surface-default);
    border-bottom: 1px solid var(--color-border-default);
    z-index: 30;
    align-items: center;
    padding: 0 var(--space-4);
  }
  .hamburger { display: block; }
  .color-row { flex-wrap: wrap; }
  .color-swatch { min-width: 40px; }
  .do-dont-row { grid-template-columns: 1fr; }
}

/* === 9. PRINT === */
@media print {
  #sidebar { display: none; }
  #content { margin-left: 0; max-width: 100%; }
  .demo-container { break-inside: avoid; }
  .section { break-before: auto; break-inside: avoid-column; }
  body { font-size: 11pt; }
  a { text-decoration: none; color: inherit; }
  .no-print { display: none; } /* Tag internal-only sections */
}
```

### Determining Text Color on Swatches

For each swatch, calculate relative luminance of the background color. If luminance > 0.5, use dark text; otherwise use light text.

```javascript
function textColorForBg(hex) {
  const r = parseInt(hex.slice(1,3), 16) / 255;
  const g = parseInt(hex.slice(3,5), 16) / 255;
  const b = parseInt(hex.slice(5,7), 16) / 255;
  const luminance = 0.2126 * r + 0.7152 * g + 0.0722 * b;
  return luminance > 0.5 ? '#1E293B' : '#F8FAFC';
}
```

---

## JavaScript

All JS inlined in a single `<script>` block at end of `<body>`.

### Required Behaviors

#### 1. Dark/Light Toggle

```javascript
const toggle = document.getElementById('theme-toggle');
const html = document.documentElement;

toggle.addEventListener('click', () => {
  const current = html.getAttribute('data-theme');
  const next = current === 'dark' ? 'light' : 'dark';
  html.setAttribute('data-theme', next);
  localStorage.setItem('theme', next);
});

// Restore preference
const saved = localStorage.getItem('theme');
if (saved) html.setAttribute('data-theme', saved);
```

#### 2. Smooth Scroll Navigation

```javascript
document.querySelectorAll('.nav-link').forEach(link => {
  link.addEventListener('click', (e) => {
    e.preventDefault();
    const target = document.querySelector(link.getAttribute('href'));
    if (target) target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    // Close mobile sidebar
    document.getElementById('sidebar').classList.remove('open');
  });
});
```

#### 3. Active Section Highlighting

```javascript
const sections = document.querySelectorAll('.section');
const navLinks = document.querySelectorAll('.nav-link');

const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      navLinks.forEach(link => link.classList.remove('active'));
      const activeLink = document.querySelector(`.nav-link[href="#${entry.target.id}"]`);
      if (activeLink) activeLink.classList.add('active');
    }
  });
}, { rootMargin: '-20% 0px -80% 0px' });

sections.forEach(s => observer.observe(s));
```

#### 4. Copy-to-Clipboard

For hex values, token names, and CSS snippets:

```javascript
document.querySelectorAll('[data-copy]').forEach(el => {
  el.addEventListener('click', () => {
    navigator.clipboard.writeText(el.getAttribute('data-copy'));
    el.classList.add('copied');
    setTimeout(() => el.classList.remove('copied'), 1500);
  });
});
```

#### 5. Mobile Hamburger

```javascript
const hamburger = document.querySelector('.hamburger');
const sidebar = document.getElementById('sidebar');
const overlay = document.querySelector('.sidebar-overlay');

if (hamburger) {
  hamburger.addEventListener('click', () => sidebar.classList.toggle('open'));
  overlay.addEventListener('click', () => sidebar.classList.remove('open'));
}
```

#### 6. Modal Demo

```javascript
document.querySelectorAll('[data-modal-open]').forEach(btn => {
  btn.addEventListener('click', () => {
    const modal = document.getElementById(btn.getAttribute('data-modal-open'));
    modal.classList.add('active');
  });
});
document.querySelectorAll('[data-modal-close]').forEach(btn => {
  btn.addEventListener('click', () => {
    btn.closest('.modal-overlay').classList.remove('active');
  });
});
```

#### 7. Toast Demo

```javascript
function showToast(variant) {
  const container = document.getElementById('toast-container');
  const toast = document.createElement('div');
  toast.className = `toast toast-${variant}`;
  toast.textContent = `This is a ${variant} toast notification`;
  container.appendChild(toast);
  // Auto-remove per duration token
  setTimeout(() => {
    toast.classList.add('toast-exit');
    setTimeout(() => toast.remove(), 300);
  }, /* component.toast.duration value */ 5000);
}
```

#### 8. Skeleton Demo

```javascript
document.querySelectorAll('[data-skeleton-toggle]').forEach(btn => {
  btn.addEventListener('click', () => {
    const target = document.getElementById(btn.getAttribute('data-skeleton-toggle'));
    target.classList.toggle('loading');
  });
});
```

#### 9. Expandable Sections (Optional)

For long token reference tables, allow collapse/expand:

```javascript
document.querySelectorAll('.expandable-trigger').forEach(trigger => {
  trigger.addEventListener('click', () => {
    const content = trigger.nextElementSibling;
    content.classList.toggle('collapsed');
    trigger.setAttribute('aria-expanded', !content.classList.contains('collapsed'));
  });
});
```

---

## Token-to-HTML Mapping Reference

Quick reference for which tokens drive which HTML sections:

| Section | Primary Token Source | Fallback |
|---------|---------------------|----------|
| Hero swatches | `semantic.color.brand.*` | `primitives.color.primary.700` |
| Color ladders | `primitives.color.*` | — (all shades required) |
| Semantic mapping table | `semantic.color.*` | — |
| Audience accents | `semantic.color.audience.*` | Skip if not defined |
| Data viz palette | `semantic.color.data.*` | `primitives.color` subset |
| Type specimens | `primitives.typography.*` | — |
| Type scale | `semantic.typography.scale.*` | `primitives.typography.size.*` |
| Spacing bars | `primitives.spacing.*` | — |
| Z-index stack | `primitives.elevation.zindex.*` | — |
| Shadows | `semantic.elevation.shadow.*` | — |
| Motion | `primitives.duration.*`, `primitives.easing.*` | — |
| Buttons | `component.button.*` | — |
| Inputs | `component.input.*` | — |
| Cards | `component.card.*` | — |
| Tables | `component.table.*` | — |
| Callouts | `component.callout.*` | — |
| Badges | `component.badge.*` | — |
| Modals | `component.modal.*` | — |
| Toasts | `component.toast.*` | — |
| Tooltips | `component.tooltip.*` | — |
| Toggles | `component.toggle.*` | — |
| Skeleton | `component.skeleton.*` | — |
| Dividers | `component.divider.*` | — |
| Charts | `component.chart.*` | — |
| Breakpoints | `primitives.breakpoint.*` | — |
| Dark mode | `semantic.color-mode.dark.*` | Invert surface/text manually |
| Logo | Brand-config + material files | — |
| Accessibility | Computed from semantic pairings | — |

---

## Dual-Purpose Usage

### Internal Reference (Full Document)

Keep all sections. This is the complete design system documentation for engineers, designers, and agents.

### External Media Kit

Strip these sections before sharing externally:
- **Token Architecture** (`#token-architecture`) — internal implementation detail
- **Downloads** (`#downloads`) — internal export files
- **Do & Don't** (`#dos-donts`) — internal usage rules (optional — may keep for brand partners)

To strip: add `class="no-print internal-only"` to these sections. CSS hides them in print. For HTML sharing, add a JS toggle or generate a separate "external" build.

The remaining sections form a professional brand guidelines document suitable for:
- Partners and co-branding situations
- Media and press kits
- Vendor and contractor onboarding
- Event and conference materials

---

## Quality Checklist

Before delivering the generated HTML file, verify:

| Check | Method | Pass Criteria |
|-------|--------|---------------|
| Valid HTML5 | W3C validator or browser dev tools | Zero errors |
| All CSS vars resolve | Open in browser, check for unstyled elements | No fallback colors visible |
| Dark/light toggle works | Click toggle, verify all sections update | All surfaces, text, borders invert |
| Mobile responsive | Resize to 375px width | Sidebar collapses, content readable |
| Print layout | Ctrl+P / Cmd+P | Sidebar hidden, single-column, no cut-off sections |
| Interactive demos work | Click buttons, toggles, modal triggers | All demos functional |
| Contrast ratios correct | Spot-check 5 pairings | Match a11y badges shown |
| Copy buttons work | Click hex/token values | Clipboard contains correct value |
| File size | Check file size | <2MB |
| No external deps | Grep for `http` in `<link>` and `<script>` | Only Google Fonts CDN |
| Logo renders | View hero and sidebar | Logo visible in both locations |
| All sections populated | Scroll through page | No empty or placeholder sections |
