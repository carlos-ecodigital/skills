# Remotion Composition Blueprints

6 video composition blueprints for Remotion-generated content. All values reference `exports/remotion-theme.ts` and semantic tokens. Each blueprint includes dimensions, fps, timing, layout, animation sequences, and token references.

**Consumed by:** Any agent producing video content via Claude Code + Remotion.

**Token dependency:** `exports/remotion-theme.ts`, `semantic.tokens.json`.

**Usage:**
```tsx
import { brandTheme, getComposition, getDataColor, getAudienceColor } from './remotion-theme';

// Get composition settings
const comp = getComposition('landscape'); // { width: 1920, height: 1080, fps: 30, durationInFrames: 300 }
```

---

## Global Video Rules

### Frame Rates
| Format | FPS | Rationale |
|---|---|---|
| Social / marketing | 30 fps | Standard web video |
| Data visualization | 30 fps | Smooth number transitions |
| Premium / cinematic | 60 fps | Upgrade via brand-config |

### Color Space
- sRGB for all web/social output
- Background: `brandTheme.colors.surface.default` (#F8FAFC) unless dark variant specified
- Text rendering: subpixel antialiasing disabled (video)

### Safe Zones (all compositions)
| Zone | Inset | Purpose |
|---|---|---|
| Action safe | 5% from each edge | All critical content |
| Title safe | 10% from each edge | All text elements |
| Logo zone | Bottom-right, 24px margin | Watermark per `brandTheme.logo` |

### Text Rules for Video
- Minimum font size: 24px (landscape), 20px (square), 28px (portrait)
- Maximum line width: 70% of composition width
- Always use solid background or text shadow for readability
- Avoid thin weights (< 500) for body text in video -- screen rendering loses detail

### Animation Principles
All animations use values from `brandTheme.motion`:

| Principle | Implementation |
|---|---|
| Entrance | Elements enter from meaningful direction (data: bottom-up, text: left-to-right) |
| Personality | Score 3 = balanced center — use moderate/standard values for all motion. Only diverge from standard when personality axis score is ≤2 or ≥4 |
| Duration | `brandTheme.motion.duration.enter` (11 frames / 350ms) default |
| Easing | `brandTheme.motion.easing.out` for entrances, `.in` for exits |
| Spring | `brandTheme.motion.spring.default` for organic motion |
| Stagger | 3-5 frame offset between sequential elements |
| Hold | Minimum 60 frames (2 seconds) for any text to be readable |
| Exit | `brandTheme.motion.duration.exit` (8 frames / 250ms), fade or slide |

---

## Composition 1: Title Card

**Purpose:** Opening title, section dividers, key reveals. Social media hooks.

### Dimensions & Timing
| Property | Landscape | Portrait | Square |
|---|---|---|---|
| Size | 1920x1080 | 1080x1920 | 1080x1080 |
| Duration | 150 frames (5s) | 150 frames (5s) | 120 frames (4s) |
| FPS | 30 | 30 | 30 |

### Sequence Timeline (landscape, 150 frames)
| Frame | Element | Animation |
|---|---|---|
| 0-10 | Background fade in | Opacity 0 -> 1, `duration.fast` |
| 5-16 | Brand accent line appears | Width 0 -> 200px, `easing.out` |
| 10-21 | Title text slides up | translateY(40px) -> 0, `spring.default` |
| 18-29 | Subtitle fades in | Opacity 0 -> 1, `duration.enter` |
| 30-120 | Hold (readable) | Static, min 90 frames |
| 120-135 | All elements fade out | Opacity 1 -> 0, `duration.exit` |
| 135-150 | Transition to next | Background remains or cross-fade |

### Layout
```
┌─────────────────────────────────────────┐
│                                         │
│                                         │
│   ════════════                          │  <- accent line (200px, 4px, brand.secondary)
│   TITLE TEXT                            │  <- brandTheme.typography.fontSize['5xl'] (48px), bold
│   Subtitle text                         │  <- fontSize['xl'] (24px), regular, text.secondary
│                                         │
│                                         │
│                           [logo watermark]│
└─────────────────────────────────────────┘
```

### Token Mapping
| Element | Property | Token | Value |
|---|---|---|---|
| Background | backgroundColor | `brandTheme.colors.surface.default` | #F8FAFC |
| Title | color | `brandTheme.colors.text.heading` | #142945 |
| Title | fontSize | `brandTheme.typography.fontSize['5xl']` | 48 |
| Title | fontWeight | `brandTheme.typography.fontWeight.bold` | 700 |
| Title | fontFamily | `brandTheme.typography.fontFamily.heading` | Inter |
| Subtitle | color | `brandTheme.colors.text.secondary` | #64748B |
| Subtitle | fontSize | `brandTheme.typography.fontSize.xl` | 24 |
| Accent line | backgroundColor | `brandTheme.colors.brand.secondary` | #22C55E |
| Accent line | height | -- | 4px |
| Accent line | width | -- | 200px (animated from 0) |

### Variants
- **Dark title:** `surface.inverse` bg, `text.inverse` for title
- **Brand splash:** `surface.brand` bg, white text, secondary accent line
- **Reveal:** Background blur from image, text over semi-transparent overlay

---

## Composition 2: Metric Counter

**Purpose:** Animated number reveals for KPIs, statistics, financial data.

### Dimensions & Timing
| Property | Landscape | Portrait | Square |
|---|---|---|---|
| Size | 1920x1080 | 1080x1920 | 1080x1080 |
| Duration | 180 frames (6s) | 150 frames (5s) | 150 frames (5s) |
| FPS | 30 | 30 | 30 |

### Sequence Timeline (landscape, 180 frames)
| Frame | Element | Animation |
|---|---|---|
| 0-5 | Background | Instant or fade |
| 5-16 | Label appears | Fade in, `duration.enter` |
| 10-55 | Number counts up | Interpolate from 0 to target, `easing.out` (45 frames) |
| 55-60 | Unit/suffix appears | Fade in |
| 60-65 | Trend indicator | Slide in from right, `spring.gentle` |
| 65-150 | Hold | Static, readable |
| 150-165 | Exit | Fade out all |
| 165-180 | Transition | Background hold or fade |

### Layout
```
┌─────────────────────────────────────────┐
│                                         │
│         IT Load Capacity                │  <- label, top
│                                         │
│           42 MW                         │  <- big number, mono font, centered
│                                         │
│         ▲ +15% YoY                      │  <- trend indicator
│                                         │
│         [optional context line]         │
│                           [logo watermark]│
└─────────────────────────────────────────┘
```

### Number Animation
```tsx
// Counter interpolation
const count = interpolate(
  frame,
  [10, 55],       // 45 frames = 1.5 seconds
  [0, targetValue],
  { extrapolateRight: 'clamp' }
);

// Format with locale-appropriate separators
const formatted = Math.round(count).toLocaleString();
```

### Token Mapping
| Element | Property | Token | Value |
|---|---|---|---|
| Number | fontFamily | `brandTheme.typography.fontFamily.mono` | JetBrains Mono |
| Number | fontSize | -- | 96px (landscape), 64px (portrait), 72px (square) |
| Number | fontWeight | `brandTheme.typography.fontWeight.bold` | 700 |
| Number | color | `brandTheme.colors.brand.primary` | #1B365D |
| Label | fontSize | `brandTheme.typography.fontSize.xl` | 24 (landscape), 28 (portrait) |
| Label | color | `brandTheme.colors.text.secondary` | #64748B |
| Trend up | color | `brandTheme.colors.data.positive` | #22C55E |
| Trend down | color | `brandTheme.colors.data.negative` | #EF4444 |
| Trend delta | fontSize | -- | 20 (landscape), 32 (portrait), 24 (square) |

### Portrait Layout (1080x1920)
```
┌─────────────────────────────────┐
│                                 │
│                                 │
│                                 │
│       IT Load Capacity          │  <- label, 28px, centered
│                                 │
│            42 MW                │  <- big number, mono, 64px, centered
│                                 │
│          ▲ +15% YoY             │  <- trend, 32px
│                                 │
│      [optional context]         │
│                                 │
│                                 │
│                  [logo watermark]│
└─────────────────────────────────┘
```

### Variants
- **Multi-metric:** 2-3 numbers animating in stagger (5-frame offset per metric)
- **Before/after:** Two numbers, left muted (old), right branded (new), with arrow between
- **Comparison counter:** Two numbers counting simultaneously, different colors

---

## Composition 3: Chart Animation

**Purpose:** Animated data visualizations -- bar charts, line charts, pie charts.

### Dimensions & Timing
| Property | Landscape | Square |
|---|---|---|
| Size | 1920x1080 | 1080x1080 |
| Duration | 300 frames (10s) | 240 frames (8s) |
| FPS | 30 | 30 |

### Sequence Timeline (bar chart, landscape, 300 frames)
| Frame | Element | Animation |
|---|---|---|
| 0-10 | Background + title | Fade in |
| 10-21 | Axes appear | Draw from origin point, `duration.enter` |
| 21-25 | Grid lines | Fade in, opacity 0 -> 0.3 |
| 25-70 | Bars grow | Height 0 -> target, staggered (3 frames each), `spring.default` |
| 70-80 | Data labels appear | Fade in above bars |
| 80-85 | Legend appears | Fade in below chart |
| 85-260 | Hold | Static, readable |
| 260-275 | Exit elements | Fade out |
| 275-300 | Transition | Background hold |

### Chart Area (landscape)
| Property | Value |
|---|---|
| Chart origin | x: 160, y: 800 (bottom-left, with padding) |
| Chart width | 1600px |
| Chart height | 600px |
| Title position | x: 160, y: 80 |
| Legend position | x: 160, y: 920 |

### Bar Chart Animation
```tsx
// Per-bar growth with spring physics
const barHeight = spring({
  frame: frame - (barIndex * 3), // 3-frame stagger
  fps: 30,
  config: brandTheme.motion.spring.default, // { damping: 20, stiffness: 170, mass: 1 }
});

// Color from data series
const barColor = getDataColor(barIndex);
```

### Line Chart Animation
```tsx
// Progressive line reveal using clip path
const progress = interpolate(
  frame,
  [25, 90], // 65 frames = ~2.2 seconds
  [0, 1],
  { extrapolateRight: 'clamp', easing: Easing.out(Easing.cubic) }
);

// Clip path reveals line left-to-right
const clipWidth = chartWidth * progress;
```

### Pie/Donut Animation
```tsx
// Sequential segment reveal
const segmentAngle = spring({
  frame: frame - (segmentIndex * 5),
  fps: 30,
  config: brandTheme.motion.spring.gentle,
});
```

### Token Mapping
| Element | Token | Value |
|---|---|---|
| Axis lines | `brandTheme.colors.text.secondary` | #64748B, 2px |
| Grid lines | `brandTheme.colors.border.default` | #E2E8F0, 1px |
| Series colors | `brandTheme.colors.data.series` | Array of 6 colors |
| Data labels | `brandTheme.typography.fontFamily.mono` | JetBrains Mono, 16px |
| Title | `brandTheme.typography.fontSize['2xl']` | 30px, bold |
| Legend text | `brandTheme.typography.fontSize.sm` | 14px |

---

## Composition 4: Comparison Split

**Purpose:** Side-by-side reveals, before/after, us vs. them.

### Dimensions & Timing
| Property | Landscape | Square |
|---|---|---|
| Size | 1920x1080 | 1080x1080 |
| Duration | 240 frames (8s) | 210 frames (7s) |
| FPS | 30 | 30 |

### Sequence Timeline (landscape, 240 frames)
| Frame | Element | Animation |
|---|---|---|
| 0-10 | Background | Fade in |
| 10-21 | Center divider | Height 0 -> full, `easing.out` |
| 15-26 | Left label | Fade in + slide right, `spring.default` |
| 20-31 | Right label | Fade in + slide left, `spring.default` |
| 30-55 | Left content | Staggered fade in (items), 5-frame stagger |
| 40-65 | Right content | Staggered fade in (items), 5-frame stagger |
| 65-200 | Hold | Static |
| 200-220 | Highlight winner | Right side scale 1.02, subtle glow |
| 220-240 | Transition | Fade out |

### Layout
```
┌────────────────────┬────────────────────┐
│                    │                    │
│   Left panel       │   Right panel      │
│   (muted/before)   │   (branded/after)  │
│                    │                    │
│   • Item 1         │   • Item 1  ✓     │
│   • Item 2         │   • Item 2  ✓     │
│   • Item 3         │   • Item 3  ✓     │
│                    │                    │
│    [label]          │    [label]         │
└────────────────────┴────────────────────┘
```

### Token Mapping
| Element | Token | Value |
|---|---|---|
| Left bg | `brandTheme.colors.surface.subtle` | #F1F5F9 |
| Right bg | `brandTheme.colors.surface.default` | #F8FAFC |
| Divider | `brandTheme.colors.border.strong` | #CBD5E1, 2px |
| Left label | `brandTheme.colors.text.secondary` | Muted |
| Right label | `brandTheme.colors.brand.primary` | Branded |
| Check marks | `brandTheme.colors.data.positive` | #22C55E |
| Highlight glow | `brandTheme.colors.brand.secondary` | 10% opacity, 20px blur |

---

## Composition 5: Text Reveal

**Purpose:** Key statement, tagline, or headline reveal with emphasis animation.

### Dimensions & Timing
| Property | Landscape | Portrait | Square |
|---|---|---|---|
| Size | 1920x1080 | 1080x1920 | 1080x1080 |
| Duration | 120 frames (4s) | 120 frames (4s) | 90 frames (3s) |
| FPS | 30 | 30 | 30 |

### Sequence Timeline (120 frames)
| Frame | Element | Animation |
|---|---|---|
| 0-5 | Background | Instant |
| 5-20 | Line 1 words | Word-by-word fade in, 2-frame stagger per word |
| 20-35 | Line 2 words | Same stagger, continues from line 1 |
| 35-45 | Emphasis word | Scale 1.0 -> 1.05 -> 1.0, color change to `brand.secondary`, `spring.bouncy` |
| 45-100 | Hold | Static |
| 100-115 | Exit | Fade out |
| 115-120 | Pad | Black/bg for transition |

### Word-by-Word Animation
```tsx
// Calculate per-word timing
const words = text.split(' ');
const framesPerWord = 2;
const startFrame = 5;

words.map((word, i) => {
  const wordStart = startFrame + (i * framesPerWord);
  const opacity = interpolate(
    frame,
    [wordStart, wordStart + brandTheme.motion.duration.fast],
    [0, 1],
    { extrapolateRight: 'clamp' }
  );
  const translateY = interpolate(
    frame,
    [wordStart, wordStart + brandTheme.motion.duration.fast],
    [20, 0],
    { extrapolateRight: 'clamp', easing: Easing.out(Easing.cubic) }
  );
  return { word, opacity, translateY };
});
```

### Token Mapping
| Element | Token | Landscape | Portrait | Square |
|---|---|---|---|---|
| Text | `brandTheme.typography.fontSize` | 42px ('4xl') | 36px ('3xl') | 36px ('3xl') |
| Text weight | `brandTheme.typography.fontWeight.bold` | 700 | 700 | 700 |
| Text color | `brandTheme.colors.text.heading` | #142945 | #142945 | #142945 |
| Emphasis color | `brandTheme.colors.brand.secondary` | #22C55E | #22C55E | #22C55E |
| Background | `brandTheme.colors.surface.default` | #F8FAFC | #F8FAFC | #F8FAFC |
| Text alignment | -- | left | center | center |

### Portrait Layout (1080x1920)
```
┌─────────────────────────────────┐
│                                 │
│                                 │
│                                 │
│                                 │
│        Word by word             │  <- 36px, bold, center-aligned
│      text reveal with           │
│       emphasis word              │  <- emphasis in brand.secondary
│                                 │
│                                 │
│                                 │
│                  [logo watermark]│
└─────────────────────────────────┘
```

### Variants
- **Dark reveal:** `surface.inverse` bg, `text.inverse` text
- **Typewriter:** Characters instead of words, mono font, cursor blinking
- **Highlight sweep:** Yellow/branded highlight bar sweeps under emphasis text

---

## Composition 6: Social Carousel Card

**Purpose:** Individual card in a carousel series. Instagram/LinkedIn carousel format.

### Dimensions & Timing
| Property | Value |
|---|---|
| Size | 1080x1080 (square only) |
| Duration | 90 frames (3s) per card |
| FPS | 30 |

### Sequence Timeline (90 frames per card)
| Frame | Element | Animation |
|---|---|---|
| 0-8 | Card background | Fade/slide in from right |
| 8-19 | Card number badge | Scale bounce, `spring.bouncy` |
| 15-26 | Heading | Slide up + fade, `spring.default` |
| 22-33 | Body content | Fade in |
| 33-75 | Hold | Static |
| 75-90 | Exit | Fade/slide left for next card |

### Layout
```
┌─────────────────────────────────┐
│ [Logo]                     1/5  │  <- card number badge (top-right)
│                                 │
│  ══════════                     │  <- accent stripe
│                                 │
│  Heading Text                   │  <- 36px, bold
│  (max 3 lines)                  │
│                                 │
│  Body text or bullet            │
│  points with key                │
│  information.                   │
│                                 │
│  ┌──────────┐                   │
│  │  Visual  │                   │
│  │ element  │                   │
│  └──────────┘                   │
│                                 │
│         @handle or CTA          │  <- footer zone
└─────────────────────────────────┘
```

### Token Mapping
| Element | Token | Value |
|---|---|---|
| Background | `brandTheme.colors.surface.default` | #F8FAFC |
| Card number bg | `brandTheme.colors.brand.primary` | #1B365D |
| Card number text | `brandTheme.colors.text.inverse` | #FFFFFF, 16px, bold |
| Card number shape | -- | 36px circle |
| Heading | `brandTheme.typography.fontSize['3xl']` | 36px, bold |
| Body | `brandTheme.typography.fontSize.lg` | 20px (larger for mobile viewing) |
| Accent stripe | `brandTheme.colors.brand.secondary` | 4px height, 120px width |
| Footer CTA | `brandTheme.typography.fontSize.base` | 16px, `brand.primary` |
| Safe margin | -- | 60px all sides (extra padding for mobile) |

### Carousel Series Rules
- **First card:** Title card -- brand name/logo prominent, topic headline, "Swipe ->" CTA
- **Middle cards:** Content cards -- numbered badge, heading + body or heading + visual
- **Last card:** CTA card -- action prompt, contact info, branded bg

### Variants
- **Dark cards:** Alternating light/dark for visual rhythm
- **Branded accent:** Each card has different audience accent color
- **Stats carousel:** Each card is a single metric counter

---

## Watermark & Logo Overlay

Applied to all compositions as a final layer.

### Specifications
| Property | Token | Value |
|---|---|---|
| Position | `brandTheme.logo.watermarkPosition` | bottom-right |
| Size | `brandTheme.logo.watermarkSize` | 48px height |
| Margin | `brandTheme.logo.watermarkMargin` | 24px from edges |
| Opacity | `brandTheme.logo.watermarkOpacity` | 0.15 |
| Variant | -- | White on dark bg, dark on light bg |
| Animation | -- | Fade in with first content, persist through exit |

---

## Export Settings

### Social Platforms
| Platform | Format | Size | FPS | Codec |
|---|---|---|---|---|
| LinkedIn | Landscape or Square | 1920x1080 or 1080x1080 | 30 | H.264 |
| Instagram Feed | Square | 1080x1080 | 30 | H.264 |
| Instagram Story/Reel | Portrait | 1080x1920 | 30 | H.264 |
| Twitter/X | Landscape | 1920x1080 | 30 | H.264 |
| Website hero | Landscape | 1920x1080 | 30 | WebM + H.264 fallback |

### Quality Settings
| Setting | Value |
|---|---|
| Bitrate | 8-12 Mbps (social), 20+ Mbps (website) |
| Audio | None (motion graphics) or 128kbps AAC |
| Max file size | 512MB (LinkedIn), 4GB (general) |
| Max duration | 10 minutes (LinkedIn), 60s (Instagram Reel) |

### Reduced Motion Export
For accessibility, generate a static alternative:
- Export frame at 50% of duration (the "hold" frame)
- Save as PNG/JPG alongside video
- Use as `poster` attribute or fallback image
