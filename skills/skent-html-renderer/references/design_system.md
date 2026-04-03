# Design System (extracted from front-design skill)

## Typography

### Display Font (Headings)
- **Primary**: Crimson Pro — elegant serif with authority
- **Secondary**: Playfair Display — editorial feel
- **Fallback**: Georgia, 'Times New Roman', serif

### Body Font
- **Primary**: IBM Plex Sans — humanist sans-serif, excellent readability
- **Secondary**: Source Sans Pro
- **Fallback**: 'Helvetica Neue', Arial, sans-serif

### Mono Font
- **Primary**: SF Mono, Fira Code
- **Fallback**: 'Courier New', monospace

### Font Sizes
```
h1: 2.75rem / 2.25rem (mobile)
h2: 1.5rem / 1.25rem (mobile)
h3: 1.2rem
body: 16px
small: 0.875rem
```

## Color Palettes

### Analytical (Gold/Dark)
```
--bg-primary:     #0f1419   (near-black blue)
--bg-secondary:   #1a2332   (dark navy)
--bg-tertiary:    #232d3f   (muted navy)
--text-primary:   #e8eaed   (off-white)
--text-secondary: #9aa0a6   (gray)
--text-muted:     #6b7280   (dark gray)
--accent:         #d4af37   (gold)
--accent-hover:   #e8c252   (bright gold)
--accent-green:   #34d399   (signal green)
--accent-red:     #f87171   (signal red)
--accent-yellow:  #fbbf24   (signal yellow)
--border:         #2d3748   (subtle border)
```

### News (Light/Blue)
```
--bg-primary:     #fafafa   (off-white)
--bg-secondary:   #ffffff   (white)
--bg-tertiary:    #f3f4f6   (light gray)
--text-primary:   #1a1a1a   (near-black)
--text-secondary: #6b7280   (gray)
--accent:         #3b82f6   (blue)
--accent-hover:   #2563eb   (darker blue)
--border:         #e5e7eb   (light border)
```

## Motion

### Animations
```css
/* Section fade-in on load */
@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Staggered delays */
animation-delay: 0.05s, 0.1s, 0.15s... per child element

/* Easing */
--ease-out: cubic-bezier(0.16, 1, 0.3, 1);
transition: all 0.2s var(--ease-out);
```

## Layout

### Container
- Max width: 900px
- Padding: 3rem (desktop), 1.5rem (mobile)
- Line height: 1.75 (body), 1.3 (headings)

## Components

### Tables
- Zebra striping: `nth-child(even)` with `rgba(255,255,255,0.03)` or `rgba(0,0,0,0.02)`
- Hover: subtle accent tint `rgba(212,175,55,0.05)`
- Header: background-secondary + bottom border 2px

### Lists (custom bullets)
- Use `▸` (right-pointing small triangle) as bullet character
- Color: accent gold
- Negative text-indent to offset

### Blockquotes
- Left border: 3px solid accent
- Background: bg-secondary
- Border radius: 0 8px 8px 0
- Italic text

### Code
- Inline: `bg-tertiary`, padding 0.15em 0.4em, rounded 4px
- Blocks: bg-secondary, border 1px solid border, border-radius 8px

## Anti-patterns

- DO NOT use Inter, Roboto, or Arial for display
- DO NOT use pure black (#000) or pure white (#fff)
- DO NOT use default browser styling
- DO NOT use flat colors — use subtle gradients and shadows
