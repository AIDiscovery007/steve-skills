# Midjourney V7 Parameters Reference (2025)

Complete guide to Midjourney V7 parameters with V6 compatibility notes.

---

## Version Selection

### --v 7 (DEFAULT - Recommended)

**Released:** April 3, 2025 | **Default Since:** June 17, 2025

**Key Improvements:**
- Enhanced prompt following and interpretation
- Superior text rendering in images
- Improved anatomy (hands, bodies, faces)
- Better coherence in complex scenes
- Richer textures and details

**Requirements:**
- **Mandatory personalization setup** (rate ~200 images before first use)
- Creates personal aesthetic profile

**When to Use:**
- All new projects (it's the default)
- When you need better text in images
- Complex prompts with multiple elements
- Projects leveraging personalization

```
your prompt here --v 7
```

### --v 6 (Legacy - Stable)

**Use Cases:**
- Proven results for specific workflows
- When V7 has unexpected behavior
- Don't want mandatory personalization
- Legacy project consistency

```
your prompt here --v 6
```

**Note:** Most V6 parameters work in V7. This guide focuses on V7 with V6 notes where different.

---

## V7 NEW Parameters

### --draft (10x Faster Iterations)

**Purpose:** Rapid prototyping and concept exploration

**Benefits:**
- **10x faster** generation
- **50% cost reduction**
- Perfect for iteration workflow

**Trade-offs:**
- Lower resolution output
- Reduced detail level
- Not for final renders

**Optimal Workflow:**
```
1. Exploration: your prompt --draft
   → Test composition, style, colors

2. Refinement: your refined prompt --draft
   → Adjust based on results

3. Final Render: your final prompt --v 7 --q 2
   → Full quality production
```

**Example:**
```
cyberpunk cityscape, neon lights --draft --ar 16:9
(iterate 5-10 times quickly)

cyberpunk cityscape, electric blue and hot pink neon,
wet streets, atmospheric haze --v 7 --q 2 --ar 16:9
(final render)
```

**Best For:**
- Concept exploration
- Quick iterations
- Testing prompt variations
- Learning what works
- Budget-conscious projects

---

### --oref [URL] (Visual Trait Consistency)

**Purpose:** Apply consistent visual traits across a batch of images

**What It Does:**
- Maintains overall visual characteristics
- Different from --sref (style) and --cref (character)
- Creates cohesive visual series

**Use Cases:**
- Brand visual consistency
- Series of images with unified look
- Consistent atmosphere across scenes
- Visual storytelling with coherent aesthetic

**Example:**
```
Image 1: forest scene --oref https://example.com/reference.jpg
Image 2: mountain scene --oref https://example.com/reference.jpg
Image 3: ocean scene --oref https://example.com/reference.jpg

All three maintain consistent visual traits from reference
```

**Combining References:**
- --sref: Style/aesthetic
- --cref: Character consistency
- --oref: Visual traits

---

## Personalization (Mandatory in V7)

### Setup Process

**First-Time V7 Users:**
1. System prompts you to rate ~200 images
2. Like/dislike images to build your aesthetic profile
3. V7 learns your preferences
4. Applies automatically to all generations

**What Personalization Does:**
- Adapts output to your aesthetic preferences
- Improves over time with more ratings
- Creates personalized default style

### --personalize (Apply Your Profile)

**Syntax:** `--personalize` or `-p`

**Usage:**
```
portrait photography --personalize
```

**When to Use:**
- Personal projects
- Work matching your taste
- Consistent "your style" aesthetic

**When NOT to Use:**
- Client work (their taste matters)
- Objective/neutral outputs
- Exploring outside your comfort zone

### --p [code] (Specific Profile)

**Purpose:** Use a specific personalization profile by code

**Usage:**
```
landscape --p abc123xyz
```

**Use Cases:**
- Share aesthetic profiles with team
- Switch between different style modes
- Apply collaborator's aesthetic
- Multiple brand styles

---

## Core Parameters

### --stylize [0-1000] (or -s)

**Purpose:** Control artistic interpretation level

**Range:** 0 (literal) to 1000 (maximum artistic)
**Default:** 100

**V7 Behavior:** More nuanced than V6, responds better to mid-range values

**Quick Guide:**
- `0-30`: Photographic realism, minimal interpretation
- `30-80`: Balanced, professional photography
- `80-150`: Artistic, stylized but recognizable
- `150-300`: Strong artistic interpretation
- `300+`: Experimental, abstract

**Examples:**
```
product photography --stylize 20 --style raw
editorial portrait --stylize 60
artistic poster --stylize 120
abstract art --stylize 250
```

---

### --chaos [0-100] (or -c)

**Purpose:** Control result variation and unpredictability

**Range:** 0 (predictable) to 100 (highly varied)
**Default:** 0

**Usage Guide:**
- `0-15`: Consistent results, commercial work
- `15-35`: Controlled variation, creative exploration
- `35-60`: High variation, seeking options
- `60-100`: Maximum experimentation

**V7 Note:** Produces more coherent variations than V6 even at high values

```
brand asset --chaos 5
poster design --chaos 25
experimental art --chaos 70
```

---

### --weird [0-3000] (or -w)

**Purpose:** Add unconventional, experimental aesthetics

**Range:** 0 (normal) to 3000 (maximum weirdness)
**Default:** 0

**V7 Behavior:** More controlled weird results than V6

**Value Guide:**
- `0-500`: Subtle uniqueness
- `500-1000`: Noticeably creative
- `1000-1500`: Experimental
- `1500-2500`: Highly unconventional
- `2500-3000`: Maximum boundary-pushing

**Use Cases:**
- Breaking creative blocks (--weird 800-1200)
- Unique brand identity (--weird 300-700)
- Surreal art (--weird 1500+)

```
portrait --weird 1000 --stylize 100
landscape --weird 600 --v 7
```

---

## Reference System

### --sref [URL] (Style Reference)

**Purpose:** Reference overall visual style from image

**What It Copies:** Color palette, texture, artistic approach
**What It Doesn't Copy:** Subject, composition

**Usage:**
```
portrait --sref https://example.com/style.jpg
```

**Multiple References:**
```
landscape --sref https://url1.jpg https://url2.jpg https://url3.jpg
```

---

### --cref [URL] (Character Reference)

**Purpose:** Maintain character consistency across generations

**What It Preserves:** Facial features, character identity
**Combine With:** --cw to control preservation level

**Usage:**
```
character in park --cref https://example.com/character.jpg
```

---

### --cw [0-100] (Character Weight)

**Purpose:** Control how much character to preserve

**Range:**
- `0`: Face/hair only (different outfits)
- `50`: Balanced preservation
- `100`: Complete preservation (including clothing)

**Usage:**
```
character at beach --cref [URL] --cw 0
(same face, different outfit)

character series --cref [URL] --cw 100
(exact replication)
```

---

## Technical Parameters

### --ar [ratio] (Aspect Ratio)

**Common Ratios:**
- `1:1`: Square (Instagram posts)
- `4:5`: Vertical (Instagram portrait)
- `2:3`: Portrait (phone wallpapers)
- `16:9`: Widescreen (desktop, YouTube)
- `21:9`: Cinematic ultra-wide

```
portrait --ar 2:3
desktop wallpaper --ar 16:9
Instagram post --ar 4:5
```

---

### --quality [0.25|0.5|1|2] (or -q)

**Purpose:** Control rendering quality/detail

**Options:**
- `0.25, 0.5`: Fast, lower detail (with --draft)
- `1`: Standard (default, recommended)
- `2`: High quality, more GPU time

**Workflow:**
```
Iteration: --draft --q 0.5
Final: --q 2
```

---

### --style raw

**Purpose:** Reduce Midjourney's default aestheticization

**V7 Note:** Less necessary than V6 due to better prompt following

**Use Cases:**
- Documentary photography
- Realistic product shots
- Literal interpretation needed

```
street photography --style raw --stylize 20
```

---

### --no [element,element] (Negative Prompting)

**Purpose:** Exclude specific elements

**V7 Best Practice:** Minimize use - V7 responds better to positive descriptions

**Instead of:**
```
❌ design --no text,watermark,border
```

**Prefer:**
```
✅ clean pure visual design, image-only composition
```

**When to Still Use:**
- Specific technical exclusions
- Persistent unwanted elements

```
portrait --no hands (if hands keep appearing incorrectly)
```

---

## Quick Decision Tables

### Photography
```
Documentary/Street:
--v 7 --style raw --stylize 20-40 --ar 3:2 --draft (iterate)

Professional Portrait:
--v 7 --stylize 40-70 --ar 2:3 --q 2 (final)

Product Photography:
--v 7 --style raw --stylize 10-30 --ar 1:1 --q 2

Cinematic:
--v 7 --stylize 70-120 --ar 16:9 or 21:9 --q 2
```

### Illustration & Art
```
Anime/Manga:
--niji 6 --stylize 100-150 --ar 2:3 or 4:5

Abstract/Experimental:
--v 7 --stylize 200-300 --weird 1500-2500 --chaos 40

Artistic Poster:
--v 7 --stylize 100-180 --ar 2:3 --q 2
```

### Design
```
Minimalist:
--v 7 --stylize 40-70 --ar 2:3 or 4:5

Pattern/Texture:
--v 7 --stylize 80 --tile --ar 1:1

Modern Graphic:
--v 7 --stylize 60-100 --ar 1:1 --q 2
```

### Character Design
```
Consistent Character (outfit variations):
--cref [URL] --cw 0 --v 7 --ar 2:3

Character Series (exact replication):
--cref [URL] --cw 100 --v 7 --ar 2:3
```

---

## Deprecated Features

### ~~Style Tuner~~ (Replaced by Personalization)

**Status:** No longer functional as of V7
**Command:** `~~--tune~~` removed

**Migration Path:**
- Old: Create style tuner → Get --style code → Use in prompts
- New: Complete personalization setup → Use --personalize or --p [code]

**Existing Style Codes:**
- Can still use with `--p [old-style-code]` in V7 (may work)
- But personalization profiles are the official replacement

### Other Deprecated
- ~~--test~~: Legacy parameter removed
- ~~--hd~~: Replaced by --quality system

---

## V7 Best Practices

### 1. Use Positive Descriptions

V7 responds better to describing what you **DO want** rather than what you don't.

**Old Way (V6):**
```
design, no text, no watermark, no border, no mockup
```

**New Way (V7):**
```
clean pure visual design, image-only composition
```

### 2. Leverage Personalization

V7's mandatory personalization adapts to your taste - use it!

```
portrait --personalize
```

### 3. Draft Mode Iteration

Don't render at full quality until you're confident:

```
1. Explore: prompt --draft (10x iterations)
2. Refine: refined prompt --draft
3. Final: final prompt --v 7 --q 2
```

### 4. Use Prompt Weighting (::)

For complex scenes with priority control:

```
sunset::2 mountains:: clouds::0.5
(sunset emphasized 2x, clouds de-emphasized)
```

### 5. Combine References Strategically

- --sref: Overall style
- --cref: Character consistency
- --oref: Visual trait consistency

Don't overload - pick what matters most.

### 6. Trust V7's Intelligence

V7 follows prompts better - you can be more direct and concise.

**V6 required:**
```
cinematic photography, moody lighting, 35mm lens, f/2.8 aperture,
shallow depth of field, bokeh background, dramatic atmosphere,
high contrast, film noir aesthetic, no watermark, no text
```

**V7 allows:**
```
cinematic noir portrait, 35mm f/2.8, atmospheric lighting
```

---

## Parameter Combination Best Practices

### Compatible Combinations

✅ **Photorealism:**
```
--v 7 --style raw --stylize 10-30 --draft (iterate) → --q 2 (final)
```

✅ **Artistic Expression:**
```
--v 7 --stylize 150-250 --weird 1000-2000 --chaos 30
```

✅ **Controlled Creativity:**
```
--v 7 --stylize 70-120 --chaos 15-25 --personalize
```

✅ **Character Series:**
```
--cref [URL] --cw 0-100 --v 7 --oref [URL]
```

### Conflicting Combinations

❌ **Avoid:**
- `--style raw` + high `--stylize` (contradictory)
- `--draft` + `--q 2` (draft overrides quality)
- `--chaos 0` + `--weird 2000` (defeats weird purpose)
- Excessive negative prompting in V7 (use positive descriptions)

---

## Quick Reference Summary

| Parameter | Range/Options | Default | V7 Notes |
|-----------|--------------|---------|----------|
| --v | 6, 7 | 7 | V7 is default since June 2025 |
| --draft | flag | off | NEW: 10x faster, 50% cost reduction |
| --oref | URL | none | NEW: Visual trait consistency |
| --stylize | 0-1000 | 100 | More nuanced in V7 |
| --chaos | 0-100 | 0 | More coherent in V7 |
| --weird | 0-3000 | 0 | More controlled in V7 |
| --personalize | flag/code | off | Mandatory setup in V7 |
| --sref | URL(s) | none | Style reference |
| --cref | URL | none | Character reference |
| --cw | 0-100 | 100 | Character weight |
| --ar | ratio | 1:1 | Aspect ratio |
| --q | 0.25/0.5/1/2 | 1 | Quality level |
| --style raw | flag | off | Less needed in V7 |
| --no | elements | none | Minimize in V7 |

---

## Migration from V6

### What Changed
- ✅ Better prompt following (be more concise)
- ✅ Improved anatomy (hands, bodies work better)
- ✅ Superior text rendering
- ✅ New --draft parameter
- ✅ New --oref parameter
- ❌ Mandatory personalization (rate 200 images)
- ❌ Style Tuner removed

### Update Your Prompts
1. Remove excessive negative prompting
2. Simplify - V7 understands better
3. Add --draft to iteration workflow
4. Complete personalization setup
5. Use positive descriptions
6. Consider prompt weighting (::) for complex scenes

---

Remember: V7 is more intelligent and responsive than V6. You can often achieve better results with simpler, more direct prompts. Trust the system, use draft mode for iteration, and leverage personalization.
