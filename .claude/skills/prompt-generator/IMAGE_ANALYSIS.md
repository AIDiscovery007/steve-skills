# Image Reverse Engineering Framework (Midjourney V7)

Standard process for extracting visual information from images and generating prompts for Midjourney V7.

---

## Overview

Image reverse engineering analyzes existing images to extract visual characteristics and generate prompts that can recreate similar results.

**Value**:
- Learn from reference images
- Recreate specific styles
- Understand effective visual composition
- Build prompts from visual inspiration

---

## Input Methods

### Method 1: Image in Conversation
- User uploads image directly in conversation
- Use vision capability to analyze automatically
- Most straightforward approach

### Method 2: Local File Path
- User provides absolute path (e.g., `/Users/name/image.jpg`)
- Use Read tool to access image file
- Supports JPG, PNG, WebP, etc.

**Handling Logic**:
```
IF user message contains image
  → Use vision analysis directly
ELSE IF user provides file path
  → Use Read tool to access file
ELSE
  → Ask user which method they prefer
```

---

## 7-Dimension Analysis System

Use these dimensions systematically to analyze any image:

---

### 1. Subject Identification

**Analyze**:
- Core subject/object/character
- Quantity and position
- Scale and focal point

**Output Pattern**:
- Portrait: "1 [age] [gender], [position], [shot type]"
- Scene: "[number] [objects], [arrangement], [depth]"
- Abstract: "[shapes/forms], [pattern], [focus area]"

---

### 2. Style Classification

**Analyze**:
- Medium (photography, painting, 3D, illustration)
- Era/period style (modern, vintage, retro, futuristic)
- Movement/genre (realistic, abstract, surreal, minimalist)

**Medium Categories**:
- **Photography**: Documentary, studio, film, digital
- **Painting**: Oil, watercolor, acrylic, ink
- **Digital**: 3D render, digital illustration, vector art
- **Other**: Sculpture, collage, screen print

---

### 3. Composition Analysis

**Analyze**:
- Camera angle (low, eye level, bird's eye, dutch angle)
- Framing (close-up, medium shot, wide shot)
- Layout (rule of thirds, centered, diagonal, golden ratio)
- Negative space and visual flow

---

### 4. Color System

**Analyze**:
- Dominant colors (1-2 main)
- Accent colors (2-3 supporting)
- Temperature (warm, cool, neutral)
- Saturation (high, medium, low, monochrome)

**Expression Formula**:
```
[Dominant color] with accents of [accent color 1] and [accent color 2]
```

❌ **Avoid**: "colorful", "nice colors", "vibrant"
✅ **Use**: "electric blue and hot pink neon", "warm sepia with burgundy accents"

---

### 5. Lighting Analysis

**Analyze**:
- Light source type (natural, studio, neon, candlelight)
- Direction (front, side, back, top, bottom)
- Contrast level (high, medium, low)
- Special effects (lens flare, god rays, rim light)

**Light Sources**:
- Natural: Golden hour, overcast, direct sunlight, moonlight
- Artificial: Studio, neon, street lights, candlelight
- Specialized: Volumetric, rim lighting, under-lighting

---

### 6. Atmosphere & Mood

**Analyze**:
- Emotional feel (serene, moody, energetic, mysterious)
- Tone (warm/inviting, cold/distant, intimate/universal)
- Concepts or messages conveyed

**Mood Descriptors**:
- Serene, moody, energetic, mysterious, dramatic, whimsical, dark, ethereal
- Warm and inviting, cold and distant, intimate and personal, grand and epic

---

### 7. Technical Characteristics **(V7 Enhanced)**

**Analyze**:
- Sharpness/depth of field (shallow DOF, tack sharp)
- Detail level (ultra-detailed, soft focus)
- Texture quality (glossy, matte, rough, smooth)
- Post-processing (film grain, vignette, color grading)
- **V7 Specific**: Text elements (V7 renders text better), anatomy quality (V7 improved hands/bodies)

**V7 Advantages**:
- Better text rendering in images
- Improved anatomy (hands, faces, bodies more accurate)
- Better coherence in complex scenes

---

## Prompt Generation Workflow

### Step 1: Systematic Analysis
Apply all 7 dimensions to extract characteristics

### Step 2: Extract Keywords
From each dimension, extract 2-3 critical descriptive terms

**Example**:
```
Subject: "1 elderly man, close-up portrait"
Style: "oil painting, Renaissance technique"
Composition: "centered, intimate framing"
Colors: "warm earth tones with burgundy accents"
Lighting: "chiaroscuro, window light from left"
Atmosphere: "contemplative, dignified"
Technical: "impasto texture, visible brushstrokes"
```

### Step 3: Structured Assembly

```
Medium/Style → Subject → Details → Composition → Colors → Lighting → Atmosphere → Technical → Parameters
```

**Example**:
```
oil painting portrait, 1 elderly man with weathered features,
centered composition, warm earth tones with burgundy accents,
chiaroscuro lighting from window, contemplative atmosphere,
Renaissance technique, impasto texture, visible brushstrokes,
museum-quality detail
--ar 4:5 --stylize 100 --v 7
```

### Step 4: Apply Writing Techniques

- Use "1" to emphasize main subject
- Repeat key style terms 2-3 times
- Use professional terminology
- **V7**: Use positive descriptions instead of negatives

### Step 5: User Confirmation

```
Based on the image analysis, I've identified:
- Subject: [description]
- Style: [description]
- Colors: [description]
- Atmosphere: [description]

Please confirm:
- Do you want to fully reproduce this style, or make adjustments?
- Any specific elements you want to emphasize or change?
```

### Step 6: Generate with V7 Workflow

**V7 Draft Mode Iteration**:
1. Test with `--draft` to verify style match
2. Refine colors/composition with `--draft`
3. Final render with `--v 7 --q 2`

**Consider**:
- Full reproduction → Use `--sref [image URL]` for style matching
- Style preservation → Keep style/colors, change subject
- Subject preservation → Keep subject, modify style
- Hybrid approach → Mix elements

---

## Example Scenarios

### Scenario 1: Cyberpunk Night Photography

**Generated Prompt**:
```
cinematic cyberpunk cityscape, low-angle night photography,
neon-lit skyscrapers, electric blue and hot pink neon signs,
wet reflective streets, atmospheric haze, Blade Runner aesthetic,
35mm film grain, high contrast, moody noir atmosphere
--ar 2:3 --stylize 75 --v 7
```

---

### Scenario 2: Commercial Product Shot

**Generated Prompt**:
```
commercial product photography, 1 [product] centered on white background,
studio lighting, soft shadows, high-key lighting,
clean minimalist composition, professional catalog style,
sharp focus, ultra-detailed, 4K quality
--ar 1:1 --stylize 20 --style raw --v 7
```

---

### Scenario 3: Film Photography Portrait

**Generated Prompt**:
```
35mm film photography, 1 person environmental portrait,
natural window lighting, warm analog color tones,
Kodak Portra aesthetic, soft shadows, intimate atmosphere,
candid documentary style, f/2.0 shallow depth of field
--ar 4:5 --stylize 40 --v 7
```

---

## V7-Specific Features

### Enhanced Capabilities

1. **Better Text Rendering**
   - V7 handles text in images much better than V6
   - Can attempt short text, logos, signage
   - Still not 100% reliable, but significantly improved

2. **Improved Anatomy**
   - Hands, faces, bodies more accurate
   - Better proportions and positioning
   - More coherent in complex poses

3. **Stronger Prompt Following**
   - More accurate interpretation of descriptions
   - Better adherence to specific requests
   - Simpler prompts often work better

### V7 Parameters

**Recommended for Image Reverse Engineering**:
- `--v 7`: Default (better accuracy)
- `--draft`: For iteration/testing
- `--sref [URL]`: For style matching
- `--cref [URL]`: For character consistency
- `--oref [URL]`: For visual trait consistency
- `--q 2`: For final high-quality render

---

## Output Format

Use the Image Reverse Engineering template from SKILL.md Phase 4:

```markdown
# Image Analysis & Prompt Generation

## Visual Analysis Summary
[3-5 bullet points of key characteristics]

---

## Generated Prompt

### Midjourney V7 Version
```
[Complete prompt]
```

---

## Key Elements Breakdown
- **Medium & Style**: [explanation]
- **Subject & Composition**: [explanation]
- **Color Palette**: [explanation]
- **Lighting & Atmosphere**: [explanation]
- **Technical Characteristics**: [explanation]

## Parameter Recommendations
[V7 parameter reasoning]

## V7 Iteration Strategy
1. Test with `--draft` to verify style match
2. Refine details with `--draft`
3. Final render with `--v 7 --q 2`

---

## Adjustment Options

- **Fully reproduce** → Use `--sref [image URL]`
- **Keep style, change subject** → [suggestion]
- **Keep subject, change style** → [suggestion]
```

---

## Best Practices

### Do's ✅

1. **Analyze systematically** - Use all 7 dimensions
2. **Be specific** - "electric blue and hot pink" not "colorful"
3. **Use professional terms** - "chiaroscuro" not "nice lighting"
4. **Confirm with user** - Verify interpretation
5. **Leverage V7 features** - Draft mode, better prompt following
6. **Consider --sref** - For close style matching

### Don'ts ❌

1. **Don't use vague terms** - Avoid "beautiful", "nice", "good"
2. **Don't assume intent** - Ask about reproduction vs variation
3. **Don't ignore medium** - Always identify medium type
4. **Don't over-complicate** - Focus on dominant characteristics
5. **Don't forget V7 workflow** - Use draft mode for iteration

---

## Troubleshooting

### Generated prompt doesn't match original

**Solutions**:
- Use `--sref [original image URL]` for direct style reference
- Increase specificity in color/lighting descriptions
- Lower --stylize if too artistic
- Add --style raw for photographic results
- Use --draft to test before final render

### Image too complex to analyze

**Solutions**:
- Break into foreground/midground/background
- Identify 3 most dominant elements
- Ask user what to emphasize
- Focus on overall mood vs every detail
- Generate base prompt, offer refinement

### Unclear medium/style

**Solutions**:
- Look for tell-tale signs (brush strokes, grain, perfection level)
- Ask user if they know original medium
- Make educated guess, note uncertainty
- Provide multiple interpretations
- Use V7's better prompt understanding

---

## Advanced Techniques

### Multiple Reference Images

1. Analyze each separately (7 dimensions)
2. Identify common threads
3. Identify unique elements
4. Ask user priorities
5. Generate hybrid prompt

### Partial/Low Quality Images

1. Analyze visible elements systematically
2. Note uncertainty about unclear aspects
3. Ask for clarification
4. Generate based on available info
5. Offer refinement when more info available

### Era/Culture-Specific References

- Include era indicators ("1920s flapper", "80s synthwave")
- Reference movements ("Japanese ukiyo-e", "Art Deco")
- Use period-appropriate terms
- Consider artist references

---

## Integration with Main Workflow

This framework integrates at **Phase 1.5** of SKILL.md:

```
Phase 1: User selects "Image Reverse Engineering"
  ↓
Phase 1.5: IMAGE ANALYSIS (this document)
  - Identify input method
  - Apply 7-dimension framework
  - Confirm with user
  ↓
Phase 2: Structure Design
  ↓
Phase 3: Generate Prompt
  ↓
Phase 4: Formatted Output
  ↓
Phase 5: V7 Draft Mode Optimization
```

---

## Quick Checklist

Before generating prompt from image:

- [ ] Identified input method (conversation vs file path)
- [ ] Analyzed all 7 dimensions systematically
- [ ] Extracted specific keywords (no vague terms)
- [ ] Confirmed interpretation with user
- [ ] Chose appropriate prompt structure
- [ ] Applied relevant writing techniques
- [ ] Selected V7-appropriate parameters
- [ ] Considered --draft for iteration
- [ ] Considered --sref for style matching
- [ ] Provided adjustment options
- [ ] Used proper output template from SKILL.md

---

Remember: V7's improved capabilities mean you can be more concise and direct. The 7-dimension framework ensures systematic analysis, while V7's better prompt following ensures accurate reproduction. Always use draft mode for iteration before final high-quality renders.
