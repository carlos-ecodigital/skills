/**
 * Brand Book Tailwind CSS v3 Configuration
 *
 * Auto-derived from tokens/primitives.tokens.json and tokens/semantic.tokens.json.
 * Pre-filled with Digital Energy defaults. Override per brand-config after intake.
 *
 * Usage: Import in your tailwind.config.js:
 *   const brandTheme = require('./path/to/tailwind-config.js');
 *   module.exports = { theme: { extend: brandTheme } };
 *
 * Token mapping comments show the source token path for traceability.
 */

module.exports = {
  colors: {
    // --- Primitive color hues (8 families x 11 shades) ---

    // primitives.color.primary.*
    primary: {
      50:  '#F0F4F8',
      100: '#D9E2EC',
      200: '#BCCCDC',
      300: '#9FB3C8',
      400: '#627D98',
      500: '#334E68',
      600: '#243B53',
      700: '#1B365D', // brand primary
      800: '#142945',
      900: '#0D1F30',
      950: '#091620',
    },

    // primitives.color.secondary.*
    secondary: {
      50:  '#F0FDF4',
      100: '#DCFCE7',
      200: '#BBF7D0',
      300: '#86EFAC',
      400: '#4ADE80',
      500: '#22C55E', // brand secondary
      600: '#16A34A', // WCAG safe for white text
      700: '#15803D',
      800: '#166534',
      900: '#14532D',
      950: '#0A3318',
    },

    // primitives.color.neutral.*
    neutral: {
      50:  '#F8FAFC',
      100: '#F1F5F9',
      200: '#E2E8F0',
      300: '#CBD5E1',
      400: '#94A3B8',
      500: '#64748B',
      600: '#475569',
      700: '#334155',
      800: '#1E293B',
      900: '#0F172A',
      950: '#020617',
    },

    // primitives.color.accent.*
    accent: {
      50:  '#FFFBEB',
      100: '#FEF3C7',
      200: '#FDE68A',
      300: '#FCD34D',
      400: '#FBBF24',
      500: '#F59E0B',
      600: '#D97706',
      700: '#B45309',
      800: '#92400E',
      900: '#78350F',
      950: '#451A03',
    },

    // primitives.color.error.*
    error: {
      50:  '#FEF2F2',
      100: '#FEE2E2',
      200: '#FECACA',
      300: '#FCA5A5',
      400: '#F87171',
      500: '#EF4444',
      600: '#DC2626',
      700: '#B91C1C',
      800: '#991B1B',
      900: '#7F1D1D',
      950: '#450A0A',
    },

    // primitives.color.tertiary.*
    tertiary: {
      50:  '#EFF6FF',
      100: '#DBEAFE',
      200: '#BFDBFE',
      300: '#93C5FD',
      400: '#60A5FA',
      500: '#3B82F6',
      600: '#2563EB',
      700: '#1D4ED8',
      800: '#1E40AF',
      900: '#1E3A8A',
      950: '#172554',
    },

    // primitives.color.info.*
    info: {
      50:  '#EFF6FF',
      100: '#DBEAFE',
      200: '#BFDBFE',
      300: '#93C5FD',
      400: '#60A5FA',
      500: '#3B82F6',
      600: '#2563EB',
      700: '#1D4ED8',
      800: '#1E40AF',
      900: '#1E3A8A',
      950: '#172554',
    },

    // primitives.color.success.*
    success: {
      50:  '#F0FDF4',
      100: '#DCFCE7',
      200: '#BBF7D0',
      300: '#86EFAC',
      400: '#4ADE80',
      500: '#22C55E',
      600: '#16A34A',
      700: '#15803D',
      800: '#166534',
      900: '#14532D',
      950: '#0A3318',
    },

    // --- Semantic color aliases ---
    // semantic.color.data.*
    'data-1': '#334E68',
    'data-2': '#22C55E',
    'data-3': '#3B82F6',
    'data-4': '#F59E0B',
    'data-5': '#8B5CF6',
    'data-6': '#EC4899',
    'data-positive': '#22C55E',
    'data-negative': '#EF4444',
    'data-neutral': '#94A3B8',

    // semantic.color.audience.* (hyphenated: audience-{segment})
    audience: {
      grower:          '#65A30D',
      'district-heat': '#EA580C',
      'industrial-heat': '#B45309',
      neocloud:        '#2563EB',
      enterprise:      '#4338CA',
      institution:     '#0F766E',
    },
  },

  fontFamily: {
    // primitives.font.family.*
    heading: ['Inter', 'system-ui', 'sans-serif'],
    body:    ['Inter', 'system-ui', 'sans-serif'],
    mono:    ['JetBrains Mono', 'monospace'],
  },

  fontSize: {
    // primitives.font.size.*
    'xs':   ['12px', { lineHeight: '1.5' }],
    'sm':   ['14px', { lineHeight: '1.5' }],
    'base': ['16px', { lineHeight: '1.5' }],
    'md':   ['18px', { lineHeight: '1.5' }],
    'lg':   ['20px', { lineHeight: '1.25' }],
    'xl':   ['24px', { lineHeight: '1.25' }],
    '2xl':  ['30px', { lineHeight: '1.25' }],
    '3xl':  ['36px', { lineHeight: '1.1' }],
    '4xl':  ['42px', { lineHeight: '1.1' }],
    '5xl':  ['48px', { lineHeight: '1.1' }],
  },

  fontWeight: {
    // primitives.font.weight.*
    light:    300,
    regular:  400,
    medium:   500,
    semibold: 600,
    bold:     700,
  },

  lineHeight: {
    // primitives.font.lineHeight.*
    tight:   '1.1',
    snug:    '1.25',
    normal:  '1.5',
    relaxed: '1.75',
  },

  letterSpacing: {
    // primitives.font.letterSpacing.*
    tight:  '-0.025em',
    normal: '0em',
    wide:   '0.05em',
  },

  spacing: {
    // primitives.space.*
    '0':  '0px',
    '1':  '4px',
    '2':  '8px',
    '3':  '12px',
    '4':  '16px',
    '5':  '20px',
    '6':  '24px',
    '8':  '32px',
    '10': '40px',
    '12': '48px',
    '16': '64px',
    '20': '80px',
    '24': '96px',
    '32': '128px',
    '40': '160px',
    '48': '192px',
  },

  borderRadius: {
    // primitives.radius.*
    'none': '0px',
    'sm':   '2px',
    'md':   '4px',
    'lg':   '8px',
    'xl':   '12px',
    'full': '9999px',
  },

  boxShadow: {
    // primitives.shadow.*
    'xs': '0 1px 2px 0 rgba(0, 0, 0, 0.05)',
    'sm': '0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px -1px rgba(0, 0, 0, 0.1)',
    'md': '0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -2px rgba(0, 0, 0, 0.1)',
    'lg': '0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -4px rgba(0, 0, 0, 0.1)',
    'xl': '0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 8px 10px -6px rgba(0, 0, 0, 0.1)',
  },

  transitionDuration: {
    // primitives.duration.*
    'fast':    '150ms',
    'default': '300ms',
    'slow':    '500ms',
    'enter':   '350ms',
    'exit':    '250ms',
  },

  transitionTimingFunction: {
    // primitives.easing.*
    'default': 'cubic-bezier(0.4, 0, 0.2, 1)',
    'in':      'cubic-bezier(0.4, 0, 1, 1)',
    'out':     'cubic-bezier(0, 0, 0.2, 1)',
    'bounce':  'cubic-bezier(0.34, 1.56, 0.64, 1)',
  },

  zIndex: {
    // primitives.elevation.zindex.*
    'base':         0,
    'dropdown':     10,
    'sticky':       20,
    'fixed':        30,
    'overlay':      40,
    'modal':        50,
    'popover':      100,
    'tooltip':      200,
    'notification': 500,
    'max':          9999,
  },

  screens: {
    // primitives.breakpoint.*
    'mobile':  '320px',
    'tablet':  '768px',
    'desktop': '1024px',
    'wide':    '1440px',
  },
};
