/**
 * Brand Book Remotion Theme
 *
 * TypeScript interfaces + default theme object for all Remotion compositions.
 * Auto-derived from tokens. Pre-filled with Digital Energy defaults.
 *
 * Usage in Remotion:
 *   import { brandTheme } from './path/to/remotion-theme';
 *   export const MyComposition: React.FC = () => {
 *     return <div style={{ backgroundColor: brandTheme.colors.surface.default }}>...</div>;
 *   };
 */

// ============================================================
// TYPE DEFINITIONS
// ============================================================

export interface BrandColors {
  brand: {
    primary: string;
    secondary: string;
    accent: string;
  };
  surface: {
    default: string;
    subtle: string;
    strong: string;
    inverse: string;
    brand: string;
  };
  text: {
    primary: string;
    secondary: string;
    heading: string;
    link: string;
    inverse: string;
    caption: string;
  };
  border: {
    default: string;
    strong: string;
    brand: string;
  };
  feedback: {
    error: { fg: string; bg: string };
    success: { fg: string; bg: string };
    warning: { fg: string; bg: string };
    info: { fg: string; bg: string };
  };
  data: {
    series: string[];
    positive: string;
    negative: string;
    neutral: string;
  };
  audience: Record<string, string>;
}

export interface BrandTypography {
  fontFamily: {
    heading: string;
    body: string;
    mono: string;
  };
  fontSize: {
    xs: number;
    sm: number;
    base: number;
    md: number;
    lg: number;
    xl: number;
    '2xl': number;
    '3xl': number;
    '4xl': number;
    '5xl': number;
  };
  fontWeight: {
    light: number;
    regular: number;
    medium: number;
    semibold: number;
    bold: number;
  };
  lineHeight: {
    tight: number;
    snug: number;
    normal: number;
    relaxed: number;
  };
}

export interface BrandSpacing {
  base: number;
  scale: Record<string, number>;
}

export interface BrandMotion {
  duration: {
    fast: number;
    default: number;
    slow: number;
    enter: number;
    exit: number;
  };
  easing: {
    default: string;
    in: string;
    out: string;
    bounce: string;
  };
  spring: {
    default: { damping: number; stiffness: number; mass: number };
    gentle: { damping: number; stiffness: number; mass: number };
    bouncy: { damping: number; stiffness: number; mass: number };
  };
}

export interface BrandComposition {
  width: number;
  height: number;
  fps: number;
  durationInFrames: number;
}

export interface BrandElevation {
  zIndex: {
    base: number;
    dropdown: number;
    sticky: number;
    fixed: number;
    overlay: number;
    modal: number;
    popover: number;
    tooltip: number;
    notification: number;
    max: number;
  };
}

export interface BrandBreakpoints {
  mobile: number;
  tablet: number;
  desktop: number;
  wide: number;
}

export interface BrandTheme {
  colors: BrandColors;
  typography: BrandTypography;
  spacing: BrandSpacing;
  elevation: BrandElevation;
  breakpoints: BrandBreakpoints;
  motion: BrandMotion;
  compositions: {
    landscape: BrandComposition;
    portrait: BrandComposition;
    square: BrandComposition;
  };
  logo: {
    watermarkOpacity: number;
    watermarkPosition: 'bottom-right' | 'bottom-left' | 'top-right' | 'top-left';
    watermarkSize: number;
    watermarkMargin: number;
  };
}

// ============================================================
// DEFAULT THEME (Digital Energy)
// ============================================================

export const brandTheme: BrandTheme = {
  colors: {
    brand: {
      primary: '#1B365D',
      secondary: '#22C55E',
      accent: '#F59E0B',
    },
    surface: {
      default: '#F8FAFC',
      subtle: '#F1F5F9',
      strong: '#E2E8F0',
      inverse: '#0D1F30',
      brand: '#1B365D',
    },
    text: {
      primary: '#1E293B',
      secondary: '#64748B',
      heading: '#142945',
      link: '#243B53',
      inverse: '#FFFFFF',
      caption: '#94A3B8',
    },
    border: {
      default: '#E2E8F0',
      strong: '#CBD5E1',
      brand: '#334E68',
    },
    feedback: {
      error: { fg: '#B91C1C', bg: '#FEF2F2' },
      success: { fg: '#15803D', bg: '#F0FDF4' },
      warning: { fg: '#B45309', bg: '#FFFBEB' },
      info: { fg: '#1D4ED8', bg: '#EFF6FF' },
    },
    data: {
      series: ['#334E68', '#22C55E', '#3B82F6', '#F59E0B', '#8B5CF6', '#EC4899'],
      positive: '#22C55E',
      negative: '#EF4444',
      neutral: '#94A3B8',
    },
    audience: {
      grower: '#65A30D',
      'district-heat': '#EA580C',
      'industrial-heat': '#B45309',
      neocloud: '#2563EB',
      enterprise: '#4338CA',
      institution: '#0F766E',
    },
  },

  typography: {
    fontFamily: {
      heading: 'Inter',
      body: 'Inter',
      mono: 'JetBrains Mono',
    },
    fontSize: {
      xs: 12,
      sm: 14,
      base: 16,
      md: 18,
      lg: 20,
      xl: 24,
      '2xl': 30,
      '3xl': 36,
      '4xl': 42,
      '5xl': 48,
    },
    fontWeight: {
      light: 300,
      regular: 400,
      medium: 500,
      semibold: 600,
      bold: 700,
    },
    lineHeight: {
      tight: 1.1,
      snug: 1.25,
      normal: 1.5,
      relaxed: 1.75,
    },
  },

  elevation: {
    zIndex: {
      base: 0,
      dropdown: 10,
      sticky: 20,
      fixed: 30,
      overlay: 40,
      modal: 50,
      popover: 100,
      tooltip: 200,
      notification: 500,
      max: 9999,
    },
  },

  breakpoints: {
    mobile: 320,
    tablet: 768,
    desktop: 1024,
    wide: 1440,
  },

  spacing: {
    base: 4,
    scale: {
      '0': 0,
      '1': 4,
      '2': 8,
      '3': 12,
      '4': 16,
      '5': 20,
      '6': 24,
      '8': 32,
      '10': 40,
      '12': 48,
      '16': 64,
      '20': 80,
      '24': 96,
    },
  },

  motion: {
    duration: {
      fast: 5,      // 150ms at 30fps = ~5 frames
      default: 9,   // 300ms at 30fps = ~9 frames
      slow: 15,     // 500ms at 30fps = ~15 frames
      enter: 11,    // 350ms at 30fps = ~11 frames
      exit: 8,      // 250ms at 30fps = ~8 frames
    },
    easing: {
      default: 'cubic-bezier(0.4, 0, 0.2, 1)',
      in: 'cubic-bezier(0.4, 0, 1, 1)',
      out: 'cubic-bezier(0, 0, 0.2, 1)',
      bounce: 'cubic-bezier(0.34, 1.56, 0.64, 1)',
    },
    spring: {
      default: { damping: 20, stiffness: 170, mass: 1 },
      gentle: { damping: 30, stiffness: 120, mass: 1 },
      bouncy: { damping: 12, stiffness: 200, mass: 0.8 },
    },
  },

  compositions: {
    landscape: {
      width: 1920,
      height: 1080,
      fps: 30,
      durationInFrames: 300, // 10 seconds
    },
    portrait: {
      width: 1080,
      height: 1920,
      fps: 30,
      durationInFrames: 270, // 9 seconds
    },
    square: {
      width: 1080,
      height: 1080,
      fps: 30,
      durationInFrames: 270, // 9 seconds
    },
  },

  logo: {
    watermarkOpacity: 0.15,
    watermarkPosition: 'bottom-right',
    watermarkSize: 48,
    watermarkMargin: 24,
  },
};

// ============================================================
// HELPER FUNCTIONS
// ============================================================

/** Convert milliseconds to frames at the given fps */
export const msToFrames = (ms: number, fps: number = 30): number =>
  Math.round((ms / 1000) * fps);

/** Get a composition config by name */
export const getComposition = (
  name: keyof BrandTheme['compositions']
): BrandComposition => brandTheme.compositions[name];

/** Get a data series color by index (wraps around) */
export const getDataColor = (index: number): string =>
  brandTheme.colors.data.series[index % brandTheme.colors.data.series.length];

/** Get audience accent color by segment ID */
export const getAudienceColor = (segmentId: string): string =>
  brandTheme.colors.audience[segmentId] ?? brandTheme.colors.brand.primary;
