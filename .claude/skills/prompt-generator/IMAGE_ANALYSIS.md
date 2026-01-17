# Image Reverse Engineering Framework

This document defines the standard process for extracting visual information from images and generating prompts.

---

## Overview

Image reverse engineering is the process of analyzing existing images to extract their visual characteristics and generate prompts that can recreate similar results. This is valuable for:
- Learning from reference images
- Recreating a specific style
- Understanding what makes an image work
- Building prompts based on visual inspiration

---

## Input Methods

### Method 1: Image in Conversation

- User directly sends/uploads image in the conversation
- Claude uses vision capability to automatically recognize
- No additional tools needed
- Most straightforward approach

**Processing**:
```
User message contains image
  → Directly use vision analysis
  → Extract visual features
  → Generate prompt
```

### Method 2: Local File Path

- User provides absolute path (e.g., `/Users/name/image.jpg`)
- Use Read tool to access the image file
- Supports common image formats (JPG, PNG, WebP, etc.)

**Processing**:
```
User provides file path
  → Use Read tool to access image
  → Analyze image content
  → Generate prompt
```

### Handling Logic

```
IF user message contains image
  → Use vision analysis directly
ELSE IF user provides file path string
  → Use Read tool to access file
  → Analyze image content
ELSE
  → Ask user which method they prefer
```

---

## Structured Analysis Framework

### The 7-Dimension Analysis System

Use these 7 dimensions systematically to analyze any image:

---

### 1. Subject Identification

**What to Analyze**:
- What is the core subject/object/character?
- Quantity and positional relationships
- Scale and proportions
- Focal point location

**Key Questions**:
- How many main subjects?
- Where are they positioned?
- What's the primary focus?
- Are there secondary elements?

**Output Example**:
> "1 young woman, centered composition, close-up portrait"
> "3 floating geometric shapes, triangular arrangement, foreground focus"

**Common Patterns**:
- Portrait: "1 [age] [gender], [position], [shot type]"
- Scene: "[number] [objects], [arrangement], [depth]"
- Abstract: "[shapes/forms], [pattern], [focus area]"

---

### 2. Style Classification

**What to Analyze**:
- Artistic medium (photography, painting, 3D render, illustration, etc.)
- Era/period style (modern, vintage 80s, retro, futuristic, etc.)
- Movement/genre (realistic, abstract, surreal, minimalist, etc.)

**Key Questions**:
- Is this photography or art/illustration?
- What time period does it reference?
- Is it realistic or stylized?
- What art movement does it belong to?

**Medium Categories**:
```
Photography:
  - Documentary photography
  - Studio photography
  - Film photography
  - Digital photography
  - Infrared/specialized

Painting:
  - Oil painting
  - Watercolor
  - Acrylic
  - Ink painting
  - Mixed media

Digital Art:
  - 3D render
  - Digital illustration
  - Vector art
  - Pixel art
  - Matte painting

Other:
  - Sculpture
  - Collage
  - Screen print
  - Linocut
```

**Era/Style References**:
- Vintage 1920s-1950s
- Retro 1960s-1980s
- Y2K/2000s aesthetic
- Contemporary/modern
- Futuristic/sci-fi

---

### 3. Composition Analysis

**What to Analyze**:
- Camera angle/viewpoint (low angle, eye level, bird's eye view)
- Shot type/framing (close-up, medium shot, wide shot)
- Layout structure (rule of thirds, centered, symmetrical)
- Negative space usage
- Leading lines and visual flow

**Key Questions**:
- What's the viewing perspective?
- How close/far is the subject?
- Is it balanced or dynamic?
- Where does the eye travel?

**Common Compositional Patterns**:

**Camera Angles**:
- Low angle: Looking up, dramatic, heroic
- Eye level: Natural, intimate, conversational
- High angle: Looking down, vulnerable, overview
- Bird's eye view: Directly overhead, pattern-focused
- Dutch angle: Tilted, dynamic tension

**Framing**:
- Extreme close-up: Face details, textures
- Close-up: Head and shoulders
- Medium shot: Waist up
- Full shot: Entire subject
- Wide shot: Subject in environment

**Layout**:
- Rule of thirds: Subject at intersection points
- Centered: Symmetrical, formal, balanced
- Golden ratio: Natural, harmonious proportions
- Diagonal: Dynamic, movement
- Frame within frame: Layered depth

---

### 4. Color System

**What to Analyze**:
- Dominant colors (1-2 main colors)
- Accent colors (2-3 supporting colors)
- Color temperature (warm, cool, neutral)
- Saturation level (high saturation, muted, desaturated)
- Color relationships (complementary, analogous, monochromatic)

**Key Questions**:
- What are the 2-3 most prominent colors?
- Is it warm-toned or cool-toned?
- Are colors vibrant or muted?
- Is there a limited palette or many colors?

**Expression Methods**:

❌ **Avoid Vague Terms**:
- "colorful"
- "nice colors"
- "pretty palette"
- "good color scheme"

✅ **Use Specific Descriptions**:
- "electric blue and hot pink"
- "warm autumn palette with golden and rust tones"
- "monochromatic blue ranging from navy to powder blue"
- "muted earth tones with sage green accent"

**Color Palette Templates**:
```
[Dominant color] with accents of [accent color 1] and [accent color 2]

Examples:
- "black ink with accents of light blue and green"
- "warm sepia tones with burgundy and gold accents"
- "cool gray base with electric cyan highlights"
```

**Saturation Levels**:
- High saturation: "vibrant neon," "electric," "bold"
- Medium saturation: "rich," "warm," "balanced"
- Low saturation: "muted," "desaturated," "washed out," "pastel"
- Monochrome: "black and white," "grayscale," "sepia-toned"

---

### 5. Lighting Analysis

**What to Analyze**:
- Light source type (natural sunlight, studio lighting, neon lights, etc.)
- Light direction (front lit, backlit, side lit)
- Contrast level (high contrast, soft lighting, low contrast)
- Special lighting effects (lens flare, god rays, rim lighting, etc.)
- Quality (hard light vs soft light)

**Key Questions**:
- Where is the light coming from?
- Is it natural or artificial light?
- Hard shadows or soft transitions?
- Any special light effects?

**Light Source Types**:
```
Natural:
- Golden hour sunlight (warm, low angle)
- Overcast daylight (soft, diffused)
- Direct sunlight (harsh, high contrast)
- Moonlight (cool, low intensity)

Artificial:
- Studio lighting (controlled, even)
- Neon signs (colored, atmospheric)
- Street lights (warm orange, pools of light)
- Candlelight (warm, flickering, intimate)

Specialized:
- Volumetric lighting (god rays, beams)
- Rim lighting (edge highlighting)
- Under-lighting (dramatic, eerie)
- Practical lights (visible sources in scene)
```

**Directional Patterns**:
- Front lit: Even, minimal shadows, commercial
- Side lit: Dimensional, dramatic, sculptural
- Back lit: Silhouette, halo, rim light
- Top lit: Natural, outdoor feel
- Bottom lit: Unnatural, dramatic, horror

**Contrast Levels**:
- High contrast: "chiaroscuro," "dramatic shadows," "deep blacks"
- Medium contrast: "balanced lighting," "defined but soft shadows"
- Low contrast: "flat lighting," "soft diffused light," "minimal shadows"

---

### 6. Atmosphere & Mood

**What to Analyze**:
- Overall emotional feel (serene, moody, energetic, mysterious)
- Emotional tone (warm and inviting, cold and distant)
- Concepts or messages conveyed
- Viewer's emotional response

**Key Questions**:
- How does this image make you feel?
- What emotion is it trying to convey?
- What's the overall vibe?
- Is it calm or energetic? Welcoming or distant?

**Mood Categories**:

**Emotional Qualities**:
- Serene, peaceful, tranquil, calm
- Moody, melancholic, somber, pensive
- Energetic, dynamic, vibrant, lively
- Mysterious, enigmatic, cryptic
- Dramatic, intense, powerful
- Whimsical, playful, lighthearted
- Dark, ominous, foreboding
- Ethereal, dreamy, surreal

**Atmospheric Descriptors**:
- Warm and inviting
- Cold and distant
- Intimate and personal
- Grand and epic
- Cozy and comfortable
- Stark and minimal
- Rich and luxurious
- Gritty and raw

---

### 7. Technical Characteristics

**What to Analyze**:
- Sharpness and depth of field (shallow DOF, tack sharp)
- Detail level (ultra-detailed, soft focus, selective focus)
- Texture and material quality (glossy, matte, textured)
- Post-processing effects (film grain, vignette, chromatic aberration)
- Image quality indicators (4K, high resolution, crisp)

**Key Questions**:
- Is the entire image sharp or only parts?
- How detailed are the textures?
- Are there visible surface qualities?
- Any post-processing effects?
- What's the technical quality level?

**Depth of Field**:
- Shallow DOF: "bokeh background," "f/1.4 aperture," "subject isolation"
- Deep DOF: "everything in focus," "f/16," "landscape photography"
- Selective focus: "focus on foreground," "background blur"

**Detail Level**:
- Ultra-detailed: "8K detail," "hyper-realistic textures," "every pore visible"
- High detail: "sharp details," "crisp," "well-defined"
- Moderate detail: "balanced clarity," "natural sharpness"
- Soft detail: "soft focus," "dreamy blur," "gentle diffusion"

**Texture Qualities**:
- Glossy: "reflective surface," "shiny," "polished"
- Matte: "non-reflective," "flat finish," "diffused surface"
- Rough: "textured surface," "grainy," "coarse"
- Smooth: "seamless," "clean surface," "pristine"

**Post-Processing Effects**:
- Film grain: "35mm grain," "analog noise," "film texture"
- Vignette: "darkened edges," "vignetting," "focused center"
- Chromatic aberration: "color fringing," "lens aberration"
- Color grading: "teal and orange," "cinematic color," "LUT applied"

---

## Prompt Generation Workflow

### Step 1: Systematic Analysis

Use all 7 dimensions to analyze the image systematically:
1. Subject Identification → What is it?
2. Style Classification → What medium/era/genre?
3. Composition Analysis → How is it framed?
4. Color System → What colors dominate?
5. Lighting Analysis → Where's the light coming from?
6. Atmosphere & Mood → What's the feeling?
7. Technical Characteristics → What's the quality/technical approach?

### Step 2: Extract Keywords

From each dimension, extract the 2-3 most critical descriptive terms:

**Example Analysis**:
```
Subject: "1 elderly man, close-up portrait"
Style: "oil painting, Renaissance technique"
Composition: "centered, eye-level, intimate framing"
Colors: "warm earth tones with burgundy accents"
Lighting: "chiaroscuro, single light source from left"
Atmosphere: "contemplative, timeless, dignified"
Technical: "impasto texture, visible brushstrokes, museum quality"
```

### Step 3: Structured Assembly

Assemble according to prompt writing principles:
```
Medium/Style → Subject → Key Details → Composition
→ Colors → Lighting → Atmosphere → Technical → Parameters
```

**Example Assembly**:
```
oil painting portrait, 1 elderly man with weathered features,
centered composition, intimate framing, warm earth tones with
burgundy accents, chiaroscuro lighting from left side,
contemplative atmosphere, Renaissance technique, impasto texture,
visible brushstrokes, museum-quality detail
--ar 4:5 --stylize 100
```

### Step 4: Apply Core Techniques

Enhance with prompt writing techniques:
- Use "1" to emphasize main subject
- Repeat key style terms 2-3 times
- Add necessary negative exclusions
- Use professional terminology

**Enhanced Version**:
```
oil painting portrait, 1 elderly man with weathered features,
Renaissance chiaroscuro technique, warm golden hour lighting
from window, rich earth tones with accents of burgundy and olive green,
contemplative expression, soft brushstrokes, impasto texture,
classical composition, intimate atmosphere, museum-quality detail,
no modern elements, no background distractions
--ar 4:5 --stylize 100 --v 6
```

### Step 5: User Confirmation

Ask the user:
```
Based on the image analysis, I've identified:
- [Subject]: [description]
- [Style]: [description]
- [Colors]: [description]
- [Atmosphere]: [description]

Please confirm:
- Do you want to fully reproduce this style, or make adjustments?
- Any specific elements you want to emphasize or change?
```

### Step 6: Generate and Optimize

Generate final prompt based on user feedback. Consider:
- **Full reproduction**: Use all identified elements + consider `--sref [image URL]`
- **Style preservation**: Keep style/color/lighting, change subject
- **Subject preservation**: Keep subject, modify style/atmosphere
- **Hybrid approach**: Mix elements from image with new requirements

---

## Common Scenario Examples

### Scenario 1: Cyberpunk City Night Scene

**Visual Characteristics**:
- Subject: Low-angle view of neon-lit buildings
- Style: Cinematic photography + cyberpunk aesthetic
- Colors: Electric blue + hot pink neon
- Lighting: Multiple light sources + atmospheric haze
- Atmosphere: Mysterious, dystopian, noir

**Generated Prompt**:
```
cinematic cyberpunk cityscape, low-angle night photography,
towering neon-lit skyscrapers, electric blue and hot pink neon signs,
wet reflective streets, atmospheric haze, Blade Runner aesthetic,
35mm film photography, high contrast, moody atmosphere
--ar 2:3 --stylize 75
```

---

### Scenario 2: Watercolor Portrait

**Visual Characteristics**:
- Subject: Young woman, soft features
- Style: Watercolor painting, delicate
- Colors: Soft pastels (pink, lavender, mint)
- Lighting: Diffused, gentle, dreamy
- Atmosphere: Ethereal, romantic, serene

**Generated Prompt**:
```
watercolor portrait, 1 young woman with flowing hair,
soft pastel colors, gentle pink and lavender tones,
delicate brushstrokes, dreamy diffused lighting,
ethereal atmosphere, paper texture visible,
wet-on-wet technique, serene expression
--ar 2:3 --stylize 120 --niji 6
```

---

### Scenario 3: Product Photography

**Visual Characteristics**:
- Subject: Single product, centered
- Style: Commercial photography, clean
- Colors: White background, product colors prominent
- Lighting: Studio lighting, even, no harsh shadows
- Atmosphere: Professional, clean, commercial

**Generated Prompt**:
```
commercial product photography, 1 [product] centered on white background,
studio lighting, soft shadows, high-key lighting,
clean minimalist composition, professional catalog style,
sharp focus, ultra-detailed, 4K quality
--ar 1:1 --stylize 20 --style raw
```

---

### Scenario 4: Abstract Geometric Art

**Visual Characteristics**:
- Subject: Geometric shapes, overlapping
- Style: Modern digital art, clean edges
- Colors: Bold primary colors (red, blue, yellow)
- Lighting: Flat, no realistic lighting
- Atmosphere: Dynamic, energetic, modern

**Generated Prompt**:
```
abstract geometric composition, overlapping shapes,
bold primary colors, red blue and yellow palette,
clean sharp edges, modern minimalist design,
flat graphic style, dynamic arrangement,
Bauhaus influence, high contrast
--ar 1:1 --stylize 150 --v 6
```

---

### Scenario 5: Film Photography Portrait

**Visual Characteristics**:
- Subject: Person in environmental portrait
- Style: 35mm film photography, analog
- Colors: Warm tones, slight color shift
- Lighting: Natural light, soft shadows
- Atmosphere: Nostalgic, intimate, authentic

**Generated Prompt**:
```
35mm film photography, 1 person environmental portrait,
natural window lighting, warm analog color tones,
slight grain texture, Kodak Portra aesthetic,
soft shadows, intimate atmosphere, candid moment,
authentic documentary style, f/2.0 shallow depth of field
--ar 4:5 --stylize 40 --v 6
```

---

## Output Format Template

See OUTPUT_TEMPLATES.md for the complete "Image Reverse Engineering Output Template"

**Quick Reference Structure**:
```markdown
# Image Analysis & Prompt Generation

## Visual Analysis Summary
[3-5 key visual features]

## Generated Prompt
[Complete prompt for Midjourney]

## Key Elements Breakdown
- Medium & Style: [...]
- Subject & Composition: [...]
- Color Palette: [...]
- Lighting & Atmosphere: [...]
- Technical Characteristics: [...]

## Adjustment Options
[3 common adjustment directions]
```

---

## Best Practices

### Do's ✅

1. **Analyze systematically** - Use all 7 dimensions, don't skip
2. **Be specific** - "electric blue and hot pink" not "colorful"
3. **Use professional terms** - "chiaroscuro" not "nice lighting"
4. **Confirm with user** - Verify interpretation before generating
5. **Provide options** - Offer adjustment directions
6. **Consider --sref** - Mention image reference parameter for close matching

### Don'ts ❌

1. **Don't use vague terms** - Avoid "beautiful," "nice," "good"
2. **Don't assume intent** - Ask if user wants exact reproduction or variation
3. **Don't skip negative terms** - Exclude unwanted elements
4. **Don't ignore medium** - Always identify photography vs painting vs 3D
5. **Don't over-complicate** - Focus on dominant characteristics
6. **Don't forget parameters** - Match parameters to identified style

---

## Troubleshooting

### Problem: Generated prompt doesn't match original image

**Solutions**:
- Use `--sref [original image URL]` for direct style reference
- Increase specificity in color and lighting descriptions
- Lower --stylize if output is too artistic
- Add --style raw for more photographic results
- Increase detail in subject description

### Problem: Image is too complex to analyze

**Solutions**:
- Break down into foreground/midground/background
- Identify the 3 most dominant visual elements
- Ask user what aspect they want to emphasize
- Focus on overall mood rather than every detail
- Generate base prompt, then offer refinement

### Problem: Unclear what medium/style the image is

**Solutions**:
- Look for tell-tale signs (brush strokes = painting, grain = film photo)
- Check for digital perfection vs organic imperfection
- Ask user if they know the original medium
- Make best educated guess and note uncertainty to user
- Provide multiple interpretations for user to choose

---

## Advanced Tips

### Combining Multiple References

When user provides multiple reference images:
1. Analyze each image separately using 7 dimensions
2. Identify common threads (style, color, mood)
3. Identify unique elements from each
4. Ask user which aspects to prioritize
5. Generate hybrid prompt incorporating key elements

### Handling Partial Information

If you can only see part of an image or quality is low:
1. Analyze what IS visible systematically
2. Note uncertainty about unclear elements
3. Ask user for clarification on ambiguous aspects
4. Generate prompt based on available information
5. Offer to refine once more info is available

### Cultural and Era-Specific References

When images reference specific time periods or cultures:
- Include era indicators: "1920s flapper style," "80s synthwave"
- Reference cultural movements: "Japanese ukiyo-e," "Art Deco"
- Use period-appropriate terminology
- Consider adding relevant artist references
- Research if unfamiliar with the style

---

## Integration with Main Workflow

This image analysis framework integrates with the main skill workflow at **Phase 1.5**:

```
Phase 1: User selects "Image Reverse Engineering" task type
  ↓
Phase 1.5: IMAGE ANALYSIS (this document)
  - Identify input method
  - Apply 7-dimension framework
  - Confirm analysis with user
  ↓
Phase 2: Structure Design (choose appropriate template)
  ↓
Phase 3: Generate Prompt (apply techniques)
  ↓
Phase 4: Formatted Output (use reverse engineering template)
  ↓
Phase 5: Multi-round Optimization
```

---

## Quick Reference Checklist

Before generating prompt from image, confirm:

- [ ] Identified input method (conversation image vs file path)
- [ ] Analyzed all 7 dimensions systematically
- [ ] Extracted specific keywords (no vague terms)
- [ ] Confirmed interpretation with user
- [ ] Chose appropriate prompt structure
- [ ] Applied relevant writing techniques
- [ ] Selected matching parameters
- [ ] Provided adjustment options
- [ ] Used reverse engineering output template
