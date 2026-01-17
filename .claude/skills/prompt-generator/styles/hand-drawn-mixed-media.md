# Hand-Drawn Mixed Media Style

## Style Overview

An artistic illustration style that combines sketch linework with watercolor painting, emphasizing handcrafted quality and artistic imperfection. Perfect for visual expressions requiring warmth, approachability, and artistic atmosphere. Commonly used in picture book illustrations, social media covers, brand visuals, etc.

**Visual Characteristics**:

- Bold black ink outlines
- Soft watercolor rendering
- Visible brush strokes and paper texture
- Spontaneous yet deliberate composition
- Hand-written elements and decorative details

**Use Cases**:

- Social media cover images (Xiaohongshu, Instagram)
- Brand illustration and visual design
- Tech blog imagery (softening technical coldness)
- Children's picture books or story illustrations
- Art posters and print materials

---

## Core Prompt Components

### 1. Medium Definition (Required - Beginning of Prompt)

```text
Mixed media illustration, hand-drawn sketch style with watercolor
```

**Variant Options**:

- Emphasize sketch: `Charcoal and ink drawing with watercolor accents`
- Emphasize watercolor: `Watercolor painting with ink line art overlay`
- Emphasize mixed media: `Mixed media art combining pencil sketch, ink lines, and watercolor`

---

### 2. Line Quality (Core Feature)

```text
rough black ink outlines with visible brush strokes, loose sketchy linework, organic linework
```

**Adjustment Options**:

- Bold lines: `bold ink strokes, heavy black outlines, gestural drawing`
- Delicate lines: `delicate ink lines, refined sketchy details, controlled linework`
- Minimal lines: `minimal line art, selective outlines`

---

### 3. Coloring Method (Core Feature)

```text
watercolor wash in soft colors, expressive brushwork
```

**Adjustment Options**:

- Light watercolor: `light watercolor tint, subtle color wash`
- Rich watercolor: `rich watercolor layers, bold paint application`
- Selective coloring: `selective coloring, mostly monochrome with color accents`

---

### 4. Color Scheme (Adjust Based on Needs)

**Classic Palette** (Reference prototype):

```text
color palette of coral pink, orange-yellow accents, olive green elements, beige and grey background
```

**Other Color Schemes**:

- **Soft Neutral**: `soft pastel tones, muted earth colors, beige and cream palette`
- **Vibrant Bright**: `vibrant watercolor, bright coral, turquoise, sunny yellow`
- **Vintage Tones**: `vintage color palette, burnt orange, sage green, dusty rose`
- **Cool Tones**: `cool color scheme, soft blues, grey-greens, lavender accents`
- **Limited Palette**: `limited color palette of [2-3 colors]`

---

### 5. Texture and Surface (Enhance Realism)

```text
paper texture visible, artistic imperfection, handcrafted feel, no digital perfection
```

**Enhancement Options**:

- Paper texture: `grainy paper texture, canvas texture, rough watercolor paper`
- Handmade marks: `visible pencil marks, eraser smudges, paint splatters`
- Vintage texture: `aged paper, vintage book illustration texture`

---

### 6. Decorative Elements (Add Interest - Optional)

```text
decorative elements around [subject], whimsical details
```

**Specific Decoration Examples**:

- Natural elements: `hand-drawn flowers, leaves, butterflies, birds`
- Geometric decoration: `decorative borders, geometric patterns, ornamental frames`
- Text elements: `handwritten text elements, calligraphy accents, doodles`
- Abstract elements: `floating shapes, sparkles, swirls, artistic flourishes`

---

### 7. Artistic Style Positioning (Overall Atmosphere)

```text
artbook illustration aesthetic, storybook art style, vintage illustration vibe
```

**Style Variants**:

- Picture book feel: `children's book illustration, naive art style`
- Modern illustration: `contemporary illustration, editorial art style`
- Vintage illustration: `vintage watercolor painting, 1960s illustration aesthetic`
- Art book: `artistic picture book style, gallery illustration quality`

---

### 8. Exclusions (Maintain Handcrafted Feel)

```text
no digital perfection, artistic and painterly
```

**Common Exclusions**:

- Avoid digital feel: `no digital rendering, no 3D, no photorealistic`
- Avoid excessive perfection: `no smooth gradients, no perfect symmetry`
- Avoid clutter: `no cluttered composition, no excessive details`

---

## Standard Parameter Configuration

### Basic Configuration

```text
--v 6 --ar [ratio] --stylize 250-350 --style raw
```

**Parameter Explanation**:

| Parameter | Recommended Value | Rationale |
|-----------|------------------|-----------|
| Version | `--v 6` | Standard mode (not niji), suitable for artistic illustration |
| Aspect Ratio | `--ar 2:3` / `--ar 3:4` | Portrait orientation suits characters and covers |
| Stylization | `--stylize 250-350` | Lower values maintain handcrafted rawness |
| Style Mode | `--style raw` | Reduces AI beautification, maintains authentic hand-drawn quality |

### Parameter Adjustments for Different Scenarios

**Social Media Covers**:

```text
--ar 3:4 --stylize 300
```

- 3:4 suits Xiaohongshu/Instagram
- Medium stylization maintains readability

**Art Posters/Print Materials**:

```text
--ar 2:3 --stylize 250 --q 2
```

- 2:3 classic poster ratio
- Lower stylization, higher quality

**Square Composition (Social Media Posts)**:

```text
--ar 1:1 --stylize 300
```

**Widescreen Banner**:

```text
--ar 16:9 --stylize 350
```

---

## Complete Prompt Template

### Universal Template Structure

```text
Mixed media illustration, hand-drawn sketch style with watercolor,
[subject description],
rough black ink outlines with visible brush strokes, loose sketchy linework,
watercolor wash in soft colors,
color palette of [specific colors],
paper texture visible, artistic imperfection,
decorative elements including [decoration elements],
whimsical details,
charcoal and ink drawing combined with watercolor paint,
artbook illustration aesthetic,
handcrafted feel, organic linework, expressive brushwork,
limited color palette,
vintage illustration vibe,
no digital perfection, artistic and painterly
--v 6 --ar [ratio] --stylize 300 --style raw
```

---

## Practical Application Examples

### Example 1: Tech Blog Cover

**Scenario**: Claude Code Best Practices Sharing (Xiaohongshu Cover)

```text
Mixed media illustration for tech blog cover, hand-drawn sketch style with watercolor, Claude AI mascot character in cute anthropomorphic style sitting at laptop coding, rough black ink outlines with visible brush strokes, loose sketchy linework, watercolor wash in soft colors, color palette of coral pink, orange-yellow highlights, olive green accents, beige and grey background, paper texture visible, artistic imperfection, decorative elements including hand-drawn code symbols, floating terminal windows, coffee cup, plant elements, whimsical tech details, charcoal and ink drawing combined with watercolor paint, artbook illustration aesthetic, handcrafted feel, organic linework, expressive brushwork, limited color palette, vintage illustration vibe with modern tech theme, clean composition with space for text overlay at top, visual hierarchy for social media cover, no digital perfection, artistic and painterly --v 6 --ar 3:4 --stylize 300 --style raw
```

**Key Adjustments**:

- Add tech elements: `code symbols, terminal windows`
- Lifestyle elements: `coffee cup, plant elements`
- Reserve text space: `space for text overlay at top`
- Vintage meets modern: `vintage illustration vibe with modern tech theme`

---

### Example 2: Japanese School Uniform Character (Soft Version)

**Scenario**: Elegant school uniform girl, outdoor campus scene

```text
Mixed media illustration, hand-drawn sketch style with watercolor, 1 elegant high school girl wearing school uniform, rough black ink outlines with visible brush strokes, loose sketchy linework, watercolor wash in soft colors, color palette of coral pink skirt, orange-yellow accents, olive green elements, beige and grey background, paper texture visible, artistic imperfection, decorative elements around character including hand-drawn flowers and butterflies, whimsical details, outdoor school campus setting with cherry blossoms, charcoal and ink drawing combined with watercolor paint, artbook illustration aesthetic, storybook art style, handcrafted feel, organic linework, expressive brushwork, limited color palette, vintage illustration vibe, no digital perfection, artistic and painterly --v 6 --ar 2:3 --stylize 300 --style raw
```

---

### Example 3: Product Display Illustration

**Scenario**: Coffee brand visual design

```text
Mixed media illustration, hand-drawn sketch style with watercolor, coffee cup and beans arrangement with decorative elements, rough black ink outlines with visible brush strokes, loose sketchy linework, watercolor wash in warm earth tones, color palette of warm brown, cream, soft orange, sage green accents, paper texture visible, artistic imperfection, decorative elements including hand-drawn leaves, steam swirls, botanical details, whimsical cafe atmosphere, charcoal and ink drawing combined with watercolor paint, artbook illustration aesthetic, handcrafted artisanal feel, organic linework, expressive brushwork, limited warm color palette, vintage coffee shop illustration vibe, clean composition for branding use, no digital perfection, artistic and painterly --v 6 --ar 1:1 --stylize 280 --style raw
```

---

### Example 4: Children's Picture Book Style

**Scenario**: Fairy tale story illustration

```text
Mixed media illustration, hand-drawn sketch style with watercolor, child character in magical garden with fantasy elements, rough black ink outlines with visible brush strokes, loose sketchy linework, watercolor wash in bright playful colors, color palette of sky blue, sunshine yellow, grass green, coral pink, lavender accents, paper texture visible, artistic imperfection, decorative elements including hand-drawn flowers, butterflies, stars, magical sparkles, whimsical storybook details, charcoal and ink drawing combined with watercolor paint, children's book illustration aesthetic, storybook art style, handcrafted feel, organic linework, expressive brushwork, cheerful color palette, vintage picture book vibe, no digital perfection, artistic and painterly --v 6 --ar 4:5 --stylize 250 --style raw
```

---

## Quick Usage Guide

### Step 1: Determine Subject and Scene

Clarify what you want to create: character, object, scene, etc.

### Step 2: Select Color Scheme

Choose from the color schemes above or customize 2-4 colors

### Step 3: Add Decorative Elements

Select appropriate decorations based on theme: natural, geometric, text, abstract

### Step 4: Adjust Parameters

- Social media cover → `--ar 3:4`
- Art poster → `--ar 2:3`
- Square post → `--ar 1:1`
- Keep stylization between 250-350

### Step 5: Fill Universal Template

Insert the above elements into the universal template

---

## Common Adjustment Needs

### If Lines Are Too Bold/Too Delicate

**Lines too bold** → Adjust description:

```text
delicate ink lines, refined sketchy details, controlled linework
```

**Lines too delicate** → Adjust description:

```text
bold ink strokes, heavy black outlines, strong gestural drawing
```

---

### If Colors Are Too Light/Too Saturated

**Colors too light** → Adjust description:

```text
rich watercolor layers, bold paint application, saturated colors
```

**Colors too saturated** → Adjust description:

```text
light watercolor tint, subtle color wash, soft pastel tones
```

---

### If Handcrafted Feel Is Insufficient

**Enhance handcrafted feel**:

- Add: `grainy texture, visible pencil marks, paint splatters, imperfect edges`
- Lower `--stylize` to 200-250
- Emphasize: `rough handmade quality, artisan illustration`

---

### If Too Cluttered

**Simplify composition**:

- Reduce decorative element descriptions
- Add: `clean composition, minimal background, focus on main subject`
- Use: `selective details, simplified design`

---

### If Text Space Needed

**Top space**:

```text
clean composition with space for text overlay at top, main subject in lower two-thirds
```

**Bottom space**:

```text
character in upper portion, space for text at bottom third
```

**Middle space**:

```text
centered text area, subject framing the composition sides
```

---

## Style Variants

### Minimalist Version (Less is More)

**Reduce elements**:

- Remove excessive decoration
- Use: `minimal line art, clean simple composition, lots of negative space`
- Lower stylize to 200

```text
Mixed media illustration, minimal hand-drawn sketch with selective watercolor, [subject], simple black ink outlines, loose linework, watercolor wash in 2-3 colors only, clean white background with paper texture, artistic simplicity, no decorative elements, clean modern illustration, handcrafted feel, limited color palette, no digital perfection --v 6 --ar [ratio] --stylize 200 --style raw
```

---

### Maximalist Version

**Increase elements**:

- More decorative details
- Use: `ornate details, decorative borders, rich embellishments, layered composition`
- Raise stylize to 350-400

```text
Mixed media illustration, elaborate hand-drawn sketch with rich watercolor, [subject], bold black ink outlines with intricate details, expressive sketchy linework, layered watercolor wash in vibrant colors, color palette of [4-5 colors], visible paper texture, artistic richness, abundant decorative elements including [multiple decorations], ornate whimsical details, charcoal and ink with multiple watercolor layers, artbook illustration aesthetic, handcrafted artistic quality, organic expressive linework, vintage illustration vibe with modern flair, no digital perfection, artistic and painterly --v 6 --ar [ratio] --stylize 350 --style raw
```

---

### Enhanced Vintage Version

**Strengthen vintage feel**:

- Use: `aged paper texture, vintage book illustration, retro color palette, nostalgic feel`
- Colors: Muted, aged tones

```text
Mixed media illustration, vintage hand-drawn sketch with watercolor, [subject], rough ink outlines in faded black, nostalgic sketchy linework, muted watercolor wash, color palette of sepia tones, faded coral, dusty green, aged cream background, aged paper texture with subtle stains, artistic vintage imperfection, decorative elements in retro style, antique book illustration aesthetic, handcrafted vintage feel, organic weathered linework, 1960s illustration vibe, no digital perfection, artistic and painterly --v 6 --ar [ratio] --stylize 280 --style raw
```

---

## Combining with Other Styles

### + Japanese Anime Elements

Maintain mixed media texture while using anime proportions and features:

```text
Add: anime character proportions, manga-inspired features
Note: May need --niji 6 but will lose some hand-drawn texture
```

---

### + Modern Flat Design

Reduce line complexity, use more geometric shapes:

```text
Add: geometric shapes, flat design elements, modern minimalist aesthetic
Adjust: simplified forms, clean vector-like outlines
```

---

### + Ink Wash Painting Elements

Emphasize Eastern aesthetics, use ink bleeding:

```text
Add: ink wash painting influence, Chinese brush painting techniques, fluid ink bleeds
Colors: black ink dominant, subtle color accents
```

---

## Important Notes

### ✅ Should Do

1. **Always define medium**: Begin with `Mixed media illustration, hand-drawn sketch style with watercolor`
2. **Emphasize imperfection**: Add `artistic imperfection, no digital perfection` to avoid AI over-beautification
3. **Use --style raw**: Maintain authentic hand-drawn quality
4. **Limit color count**: 2-5 colors to simulate real handmade creation
5. **Add texture descriptions**: `paper texture, visible brush strokes` enhances realism

### ❌ Should Avoid

1. **Don't use --niji**: Will shift style toward anime and lose artistic illustration feel (unless intentionally blending)
2. **Don't stylize too high**: Above 400 loses handcrafted roughness
3. **Don't over-describe perfection**: Avoid `perfect, flawless, polished` etc.
4. **Don't mix in photorealistic terms**: Such as `photorealistic, 8K, ultra detailed` will conflict
5. **Don't use too many colors**: More than 5 main colors appears cluttered, loses handmade simplicity

---

## Version History

- **v1.0** (2026-01-16): Initial version, extracted from hand-drawn mixed media reference image
  - Core components: Sketch lines + watercolor painting
  - Standard parameters: --v 6 --stylize 250-350 --style raw
  - Includes 4 practical application examples

---

## Usage License

This style template is open for use, freely adjustable and combinable based on actual needs. Recommend saving commonly used personalized versions to improve work efficiency.
