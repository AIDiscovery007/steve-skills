# Prompt Writing Techniques Reference (Midjourney V7)

Comprehensive guide to 10 core prompt writing techniques for AI image generation, optimized for Midjourney V7.

---

## Core Techniques Index

1. [Number Emphasis Technique](#1-number-emphasis-technique)
2. [Repetition Reinforcement Technique](#2-repetition-reinforcement-technique)
3. [Negative Exclusion Technique](#3-negative-exclusion-technique)
4. [Medium Definition Technique](#4-medium-definition-technique)
5. [Color Control Technique](#5-color-control-technique)
6. [Professional Terminology Technique](#6-professional-terminology-technique)
7. [Hierarchical Description Technique](#7-hierarchical-description-technique)
8. [Tension Creation Technique](#8-tension-creation-technique)
9. [Prompt Weighting Technique](#9-prompt-weighting-technique) **(NEW V7)**
10. [Positive-First Description Technique](#10-positive-first-description-technique) **(NEW V7)**

---

## 1. Number Emphasis Technique

### Principle

AI generators tend to create "rich" compositions with multiple elements. Using "1" before key elements actively constrains generation to exactly one instance, preventing unwanted repetition.

**The number "1" acts as a precision constraint:**
- Generate exactly one instance
- Make this the focal point
- Don't scatter or multiply
- Emphasize uniqueness

### Usage

**Syntax**: `1 [element]`

Place "1" directly before important subjects or elements you want to emphasize.

### Example

```
Streetwear graphic design, 1 close-up cropped face centered,
1 teal ribbed knit beanie pulled down to cover both eyes,
1 cigarette clenched between lips with faint smoke wisp,
moody editorial lighting, high-contrast print-ready look
--ar 4:5 --v 7
```

**Why it works:**
- "1 face" → prevents multiple faces
- "1 beanie" → emphasizes this as THE focal prop
- "1 cigarette" → prevents multiple/scattered cigarettes
- Creates focused, intentional composition

### When to Use

✅ **Use "1" when:**
- Clear, single focal point needed
- Preventing element multiplication
- Minimalist/focused compositions
- Portrait work (1 person)
- Product photography (1 product)

❌ **Don't use when:**
- You actually want multiple elements
- Creating crowd scenes
- Pattern/repetition desired

---

## 2. Repetition Reinforcement Technique

### Principle

AI models assign higher weight to concepts appearing multiple times. **Repeating key style elements 2-3 times reinforces their importance** and ensures prioritization.

**Repetition = Emphasis**
- First mention: Introduces concept
- Second mention: Reinforces style
- Third mention: Solidifies aesthetic
- More than 3: Diminishing returns

### Usage

Repeat core style descriptors 2-3 times using:
- Direct repetition (same words)
- Synonym variation (related terms)
- Conceptual echoing (similar aesthetics)

### Example

```
Retro 80s poster style, 1 woman with sunglasses,
vintage movie poster aesthetic, 80s design language,
bold graphic composition
--ar 2:3 --stylize 80 --v 7
```

**Repetition analysis:**
- "Retro 80s" → Direct mention
- "vintage movie poster" → Synonym reinforcement
- "80s design language" → Conceptual echo
- Triple reinforcement ensures strong retro aesthetic

### When to Use

✅ **Use repetition when:**
- Emphasizing specific style/aesthetic
- Ensuring AI captures particular mood
- Complex or nuanced styles
- Need guaranteed style adherence

❌ **Don't overuse when:**
- Simple, straightforward styles
- You want variety/experimentation

### Optimal Count

- **2 times**: Minimum for effective reinforcement
- **3 times**: Optimal for strong emphasis
- **4+ times**: Diminishing returns

---

## 3. Negative Exclusion Technique

### Principle

AI adds "helpful" or "typical" elements by default. **Actively exclude unwanted elements** to maintain control and achieve clean results.

**V7 UPDATE**: Minimize negative prompting in V7 - prefer positive descriptions (see Technique 10).

### Usage

**Two approaches:**

1. **In-prompt negatives**: "no [element]"
2. **Parameter negatives**: `--no [element,element]`

**Best in V7**: Use positive descriptions instead when possible.

### Example

❌ **V6 Approach** (excessive negatives):
```
modern poster design, no text, no watermark, no border,
no mockup --no text,watermark,border,mockup
```

✅ **V7 Approach** (positive description):
```
clean pure visual design, image-only composition,
minimalist poster aesthetic
--v 7
```

### When to Use in V7

✅ **Still use negatives for:**
- Specific technical exclusions
- Persistent problematic elements (e.g., `no hands` if hands keep appearing incorrectly)

✅ **Prefer positive descriptions for:**
- General cleanliness ("clean design" not "no clutter")
- Aesthetic qualities ("pure visual" not "no text")
- Compositional goals ("image-only" not "no watermark")

### Common Exclusions (V6 style - minimize in V7)

- `no text, no watermark, no border`
- `no hands` (when hands are problematic)
- `no background clutter`

**V7 Best Practice**: Describe what you DO want, not what you don't.

---

## 4. Medium Definition Technique

### Principle

**Medium determines overall texture, rendering style, and visual approach.** Define the creation medium first to establish the framework for all other descriptions.

### Usage

Start prompts with the medium:

```
[Medium] [subject description], [details...]
```

### Example

```
oil painting portrait, 1 elderly woman with weathered features,
warm earth tones with burgundy accents, chiaroscuro lighting,
Renaissance technique, impasto texture, visible brushstrokes
--ar 4:5 --stylize 100 --v 7
```

**Why medium first:**
- "Oil painting" → Sets texture foundation
- All subsequent descriptions interpreted within this medium
- Creates cohesive artistic approach

**Compare different mediums:**
- Oil painting → Rich, textured, layered
- Photography → Realistic, lens-based, lighting-focused
- 3D render → Clean, perfect, digital precision
- Watercolor → Soft, flowing, transparent

### Common Medium Categories

**Photography**: `35mm film photography`, `cinematic photography`, `documentary photography`
**Painting**: `oil painting`, `watercolor painting`, `acrylic painting`
**Digital**: `3D render`, `digital illustration`, `matte painting`
**Print**: `screen print`, `lithograph`, `woodblock print`

### When to Use

✅ **Always define medium for:**
- Starting new prompts
- Artistic/stylized work
- When medium impacts result

---

## 5. Color Control Technique

### Principle

**Strict color limitation = Style purity and cohesion.** Vague terms like "colorful" give AI too much freedom. **Specify exact colors** to maintain visual consistency.

### Usage

**Color Formula:**
```
[Main color/palette] with accents of [accent color 1] and [accent color 2]
```

### Example

```
minimalist poster, black and white base with accents of coral red,
clean geometric composition, modern design aesthetic
--ar 2:3 --stylize 70 --v 7
```

**Why it works:**
- "Black and white base" → Establishes dominant palette
- "accents of coral red" → Defines limited supporting color
- Prevents AI from adding random colors

### Color Specificity

❌ **Avoid vague terms:**
- "colorful", "nice colors", "vibrant"

✅ **Use specific names:**
- "electric blue and hot pink neon"
- "warm sepia tones with burgundy accents"
- "monochromatic navy to powder blue"

### Common Patterns

**Monochromatic:**
```
monochromatic blue palette, navy to powder blue tonal variation
```

**Complementary:**
```
deep orange base with accents of teal blue, high contrast
```

**Limited Palette:**
```
black ink with accents of light blue and green, minimal color
```

---

## 6. Professional Terminology Technique

### Principle

**Professional terminology = Precise control.** Domain-specific technical terms give AI exact instructions instead of generic descriptions with ambiguous interpretation.

### Usage

Use terminology from:
- Photography (camera, lens, lighting)
- Art (painting techniques, movements)
- Design (composition, layout principles)

### Example

```
portrait photography, 85mm lens, f/2.0 aperture,
shallow depth of field, Rembrandt lighting setup,
soft window light camera left, bokeh background,
natural skin tones, eye-level perspective
--ar 2:3 --stylize 50 --v 7
```

**Professional terms used:**
- "85mm lens" → Specific focal length (not "blurry background")
- "f/2.0 aperture" → Exact aperture (not "nice blur")
- "Rembrandt lighting" → Specific lighting pattern (not "dramatic light")
- "shallow depth of field" → Technical DOF term

### Key Term Categories

**Photography:**
- Focal length: `35mm`, `85mm`, `200mm`
- Aperture: `f/1.4`, `f/2.8`, `f/16`
- Lighting: `golden hour`, `Rembrandt lighting`, `three-point lighting`

**Art:**
- Techniques: `impasto`, `glazing`, `chiaroscuro`
- Movements: `Renaissance`, `Baroque`, `Art Deco`

**Design:**
- Composition: `rule of thirds`, `golden ratio`, `symmetrical composition`

### When to Use

✅ **Use professional terms when:**
- You know the specific technique
- Creating photography-style work
- Need precise technical control

---

## 7. Hierarchical Description Technique

### Principle

**Clear hierarchy = AI understands priority.** Describe elements in order of importance—from subject to details, core to periphery—helps AI prioritize and build logically.

### Usage

**Structure prompts as progressive layers:**
```
[Subject] → [Primary details] → [Secondary details] → [Atmosphere] → [Technical]
```

### Example

```
1 close-up face centered (subject layer),
teal ribbed knit beanie covering eyes (detail layer 1),
cigarette with faint smoke wisp (detail layer 2),
moody editorial lighting, subtle vignette (atmosphere),
high-contrast, print-ready look (technical)
--ar 4:5 --v 7
```

**How AI processes:**
1. Creates centered close-up face (foundation)
2. Adds beanie covering eyes (primary detail)
3. Adds cigarette with smoke (secondary detail)
4. Applies moody lighting (atmosphere)
5. Applies high contrast (technical quality)

### Common Patterns

**Portrait Hierarchy:**
```
Subject → Face/expression → Hair/clothing → Props → Lighting → Background → Technical
```

**Scene Hierarchy:**
```
Main subject → Primary elements → Secondary elements → Environment → Atmosphere → Technical
```

**Product Hierarchy:**
```
Product → Key features → Supporting elements → Background → Lighting → Technical
```

### When to Use

✅ **Use hierarchical description for:**
- Complex scenes with multiple elements
- Clear priorities needed
- Detailed, layered compositions

---

## 8. Tension Creation Technique

### Principle

**Tension = Balanced coexistence of opposing elements, creating complexity and depth.** Describing interplay of contrasting qualities creates sophisticated, nuanced results that avoid being one-dimensional.

### Usage

Combine contrasting qualities using "but," "yet," or "while":

```
[Quality A] but [Opposite Quality B]
[Quality A] yet [Opposite Quality B]
```

### Example (Conceptual Storytelling)

```
conceptual visual storytelling, clear and provocative yet close and human tone,
experimental but grounded design, narrative sequential composition,
realistic textures with conceptual abstraction, cinematic photography,
35mm lens look, f/2.8 aperture, soft natural light mixed with technical accents,
visual tension that invites questioning
--ar 16:9 --v 7
```

**Tension pairs used:**
- "clear and provocative YET close and human"
- "experimental BUT grounded"
- "realistic textures WITH conceptual abstraction"
- Creates sophisticated depth through contradictions

### Common Tension Pairs

**Style Tensions:**
- Experimental ↔ Grounded
- Abstract ↔ Representational
- Minimal ↔ Rich
- Modern ↔ Timeless

**Emotional Tensions:**
- Vulnerable ↔ Strong
- Warm ↔ Distant
- Intimate ↔ Universal

**Visual Tensions:**
- Sharp ↔ Soft
- Light ↔ Dark
- Organic ↔ Geometric

### When to Use

✅ **Use tension for:**
- Sophisticated, nuanced work
- Avoiding one-dimensional results
- Adding depth and complexity
- Professional/artistic projects

---

## 9. Prompt Weighting Technique **(NEW V7)**

### Principle

**V7 supports prompt weighting with `::` syntax to prioritize elements.** Higher numbers = more emphasis, allowing fine control over complex scenes with multiple elements.

### Usage

**Syntax:**
```
element1::2 element2:: element3::0.5
```

- No number (or `::1`) = Default weight
- `::2` = 2x emphasis
- `::0.5` = 0.5x (de-emphasize)
- `::0` = Exclude completely

### Example

```
sunset::2 mountain landscape:: lake reflection::0.5 clouds::0.5,
warm golden hour lighting, cinematic composition
--ar 16:9 --v 7
```

**Weighting analysis:**
- `sunset::2` → 2x emphasis (primary focus)
- `mountain landscape::` → Default weight (supporting element)
- `lake reflection::0.5` → De-emphasized (subtle presence)
- `clouds::0.5` → De-emphasized (background element)

### When to Use

✅ **Use weighting for:**
- Complex scenes with multiple elements
- Clear priority needed among elements
- Fine-tuning element balance
- When some elements overpower others

### Advanced Usage

**Character prominence:**
```
main character::2 supporting character:: background crowd::0.3
```

**Atmosphere control:**
```
dramatic lighting::1.5 subject:: subtle background::0.5
```

---

## 10. Positive-First Description Technique **(NEW V7)**

### Principle

**V7 responds better to positive descriptions than negatives.** Instead of describing what you DON'T want, describe what you DO want. This leverages V7's improved prompt following.

### Usage

Replace negative terms with positive descriptions:

❌ **Old way (V6):**
```
no text, no watermark, no border, no mockup
```

✅ **New way (V7):**
```
clean pure visual design, image-only composition
```

### Example Transformations

**Design work:**
- ❌ `no text, no watermark` → ✅ `clean visual design, pure imagery`
- ❌ `no clutter, no background detail` → ✅ `minimalist composition, simple backdrop`
- ❌ `no mockup, no border` → ✅ `direct presentation, frameless design`

**Photography:**
- ❌ `no hands` → ✅ `portrait crop, shoulders up composition`
- ❌ `no busy background` → ✅ `clean background, isolated subject`
- ❌ `no props` → ✅ `pure subject focus, minimal scene`

### Complete Example

❌ **V6 Approach:**
```
modern poster design, no text, no watermark, no border,
no clutter, no mockup --no text,watermark,border
```

✅ **V7 Approach:**
```
clean modern poster design, pure visual composition,
image-only presentation, minimalist aesthetic,
direct graphic approach
--v 7
```

### When to Still Use Negatives

✅ **Use `--no` for:**
- Specific technical exclusions
- Persistent unwanted elements (e.g., `--no hands` when hands consistently appear incorrectly)

✅ **Use positive descriptions for:**
- General aesthetic goals
- Composition preferences
- Style characteristics

### V7 Advantage

V7's improved prompt understanding means:
- Simpler, more direct prompts work better
- Positive descriptions are interpreted accurately
- Less need for defensive negative prompting
- More natural language processing

---

## Technique Integration

### Using Multiple Techniques Together

Most effective prompts combine 4-6 techniques.

### Integration Example

**Techniques applied:**
1. Medium Definition: "cinematic photography"
2. Number Emphasis: "1 cyberpunk street scene"
3. Repetition Reinforcement: "cyberpunk", "noir aesthetic", "Blade Runner" (style reinforcement)
4. Color Control: "electric blue and hot pink neon"
5. Professional Terminology: "35mm film grain", "high contrast lighting"
6. Hierarchical Description: Subject → Details → Atmosphere → Technical
7. Positive-First (V7): "atmospheric fog" instead of "no clear sky"

**Complete Prompt:**
```
cinematic photography, 1 cyberpunk street scene at night,
neon-lit alleyways with electric blue and hot pink signs,
wet reflective pavement, atmospheric fog, Blade Runner aesthetic,
moody noir atmosphere, 35mm film grain, high contrast lighting
--ar 16:9 --stylize 60 --v 7
```

### Technique Selection Guide

**For Realistic Photography:**
- ✅ Use: Medium Definition, Professional Terminology, Positive Descriptions (V7)
- ⚠️ Use carefully: Repetition (can make too stylized)

**For Artistic/Stylized Work:**
- ✅ Use: Medium Definition, Repetition Reinforcement, Color Control, Tension
- ⚠️ Use carefully: Professional terminology (don't over-tech)

**For Design/Posters:**
- ✅ Use: Color Control, Positive Descriptions (V7), Hierarchical Description
- ⚠️ Use carefully: Number Emphasis (only for focal elements)

**For Complex Scenes (V7):**
- ✅ Use: Prompt Weighting (::), Hierarchical Description, Positive Descriptions

---

## V7-Specific Best Practices

### 1. Prefer Positive Descriptions

V7 understands what you want better than what you don't want.

**V6 required:**
```
design, no text, no watermark, no border
```

**V7 prefers:**
```
clean visual design, pure imagery
```

### 2. Use Prompt Weighting for Complex Scenes

When multiple elements compete, use `::` weighting:

```
main subject::2 supporting elements:: background::0.5
```

### 3. Simpler Prompts Work Better

V7's improved prompt following means concise prompts often work better:

**V6 required:**
```
cinematic photography, moody lighting, 35mm lens, f/2.8 aperture,
shallow depth of field, bokeh background, dramatic atmosphere,
high contrast, film noir aesthetic
```

**V7 allows:**
```
cinematic noir portrait, 35mm f/2.8, atmospheric lighting
--v 7
```

### 4. Leverage Draft Mode

Use `--draft` for rapid iteration before final render:

```
1. Explore: [prompt] --draft (10x faster iterations)
2. Refine: [refined prompt] --draft
3. Final: [final prompt] --v 7 --q 2
```

---

## Quick Reference Summary

| Technique | Core Principle | Key Syntax | V7 Notes |
|-----------|---------------|------------|----------|
| 1. Number Emphasis | "1" prevents multiplication | `1 [element]` | Unchanged |
| 2. Repetition Reinforcement | Repetition = higher weight | Repeat 2-3 times | Unchanged |
| 3. Negative Exclusion | Actively exclude unwanted | `no [element], --no` | Minimize in V7 |
| 4. Medium Definition | Medium = foundation | Start with medium | Unchanged |
| 5. Color Control | Specific colors = cohesion | `[color] with accents of` | Unchanged |
| 6. Professional Terminology | Precise terms = precise control | Use domain vocabulary | Unchanged |
| 7. Hierarchical Description | Order = priority | Subject → Details → Atmosphere | Unchanged |
| 8. Tension Creation | Opposites = depth | `[quality] yet [opposite]` | Unchanged |
| 9. Prompt Weighting | Priority control | `element::2` | NEW in V7 |
| 10. Positive-First | Describe what you DO want | Positive descriptions | NEW in V7 |

---

## Technique Mastery Path

**Beginner**: Start with 2-3 techniques
- Medium Definition (always)
- Number Emphasis (for clear subjects)
- Positive Descriptions (V7 best practice)

**Intermediate**: Add 3-4 more techniques
- Color Control
- Hierarchical Description
- Repetition Reinforcement

**Advanced**: Master all 10 techniques
- Professional Terminology
- Tension Creation
- Prompt Weighting (V7)
- Seamless integration

---

Remember: These techniques are tools, not rules. Use them purposefully to achieve your vision. V7's improved capabilities mean simpler, more direct prompts often work better—combine techniques strategically, not mechanically.
