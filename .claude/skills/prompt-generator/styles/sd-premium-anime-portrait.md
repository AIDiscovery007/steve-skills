# SD Premium Anime Portrait Style

## Style Overview

A high-quality Stable Diffusion prompt template for generating premium anime character illustrations with cover art quality. Features a carefully curated artist mix (quasarcake, mochizuki kei, wlop, monmon2133) that produces vibrant, detailed anime portraits with strong visual impact. Optimized for SDXL and compatible checkpoints.

**Visual Characteristics**:

- Extremely detailed anime illustration
- Cover art / key visual quality
- Vibrant saturated colors
- Sharp focus with high contrast
- Dynamic composition with visual impact
- Professional anime studio aesthetic
- Clean linework with subtle outlines
- Rich texture and material rendering
- 8K/32K ultra-high detail level

**Best For**:

- Anime character portraits
- Light novel / manga cover art
- Game character illustrations
- Visual novel CGs
- Character design showcases
- Wallpaper-quality artwork
- Japanese aesthetic characters (kimono, traditional wear)
- Fantasy warrior / weapon-wielding characters

**Platform**: Stable Diffusion (SDXL recommended)

---

## Core Prompt Components

### 1. Quality Foundation Tags (Required - Beginning)

```text
masterpiece, best quality, high quality, extremely detailed CG unity 8k wallpaper, extremely detailed, High Detail, vibrant colors
```

**Quality Tier Options**:

- **Maximum Quality** (Default):
  ```text
  masterpiece, best quality, high quality, extremely detailed CG unity 8k wallpaper, extremely detailed, High Detail, 32K UHD
  ```

- **Balanced Quality** (Faster generation):
  ```text
  masterpiece, best quality, high quality, extremely detailed, sharp focus
  ```

- **Stylized Quality** (More artistic freedom):
  ```text
  masterpiece, best quality, very aesthetic, absurdres, sharp focus
  ```

---

### 2. Style Definition Tags (Core Feature)

```text
anime style, cover art, extreme aesthetic, very aesthetic, Visual impact, colorful, sharp focus, impactful picture, offcial art
```

**Style Variations**:

- **Cover Art Focus**:
  ```text
  anime style, cover art, key visual, promotional art, official art
  ```

- **Illustration Focus**:
  ```text
  anime style, illustration, detailed illustration, beautiful illustration
  ```

- **CG/Game Art Focus**:
  ```text
  anime style, game CG, visual novel CG, detailed CG illustration
  ```

- **Wallpaper Focus**:
  ```text
  anime style, wallpaper, desktop wallpaper, high resolution background art
  ```

---

### 3. Artist Mix (Core Feature - Signature Look)

```text
(artist:quasarcake:0.8), (mon (monmon2133):0.5), (mochizuki kei:0.95), (wlop:0.6)
```

**Artist Contribution Analysis**:

| Artist | Weight | Contribution |
|--------|--------|--------------|
| mochizuki kei | 0.95 | Primary style - clean anime aesthetic, elegant character design |
| quasarcake | 0.8 | Vibrant colors, dynamic compositions, detailed rendering |
| wlop | 0.6 | Painterly quality, lighting effects, ethereal atmosphere |
| monmon2133 | 0.5 | Subtle anime stylization, character proportions |

**Alternative Artist Mixes**:

- **Softer/Ethereal**:
  ```text
  (wlop:0.9), (artist:ask (askzy):0.7), (fuzichoco:0.6)
  ```

- **Bold/Dynamic**:
  ```text
  (lack:0.8), (redjuice:0.7), (shalltear (character):0.5)
  ```

- **Classic Anime**:
  ```text
  (kantoku:0.8), (anmi:0.7), (tiv:0.6)
  ```

- **Painterly/Semi-Realistic**:
  ```text
  (wlop:0.9), (guweiz:0.7), (ross tran:0.5)
  ```

---

### 4. Custom Enhancement Tags (Optional - Checkpoint Specific)

```text
hycg, hysp, dynamic_outline
```

**Note**: These tags may be specific to certain checkpoints or LoRAs. Remove if not using compatible models.

**Common Enhancement Tags**:

- For outline emphasis: `dynamic_outline, bold lineart, clean linework`
- For color vibrancy: `vibrant colors, saturated colors, rich colors`
- For detail: `intricate details, fine details, highly detailed`

---

### 5. Subject Definition (Customizable Core)

**Example Subject (Japanese Warrior Girl)**:

```text
1girl, solo, looking at viewer, short hair, hair ornament, red eyes, gloves, white background, ribbon, holding, bare shoulders, jewelry, hair ribbon, upper body, weapon, flower, white hair, earrings, parted lips, japanese clothes, sword, hair flower, kimono, necklace, holding weapon, from side, sash, profile, holding sword, obi, red gloves, beads, black kimono
```

**Subject Structure**:

```text
[count][gender], [pose/action], [gaze], [hair details], [eye details], [clothing], [accessories], [held items], [composition], [background]
```

---

### 6. Comprehensive Negative Prompt (Required)

```text
unaestheticXLv13, negativeXL_D, watermark, signature, Artist name, Navel, bad anatomy, blurry, disembodied limb, Two navel eyes, worst quality, artist name, Hand with excessive fingers, Foot with excessive toes, Hand with surplus fingers, Hand with deficient fingers, Abnormal anatomy, Poorly formed hands, Deformed hands and fingers, Additional limbs, Excessive limbs, Abnormal finger interlocking duplicate, cropped, text, jpeg, artifacts, signature, watermark, username, blurry, artist name, trademark, title, muscular, sd character, multiple view, Reference sheet, long body, malformed limbs, multiple breasts, cloned face, malformed, mutated, bad anatomy, disfigured, bad proportions, duplicate, bad feet, artist name, extra limbs, ugly, fused anus, text font ui, missing, bad foot quality, twisted toes, asymmetric toes, abnormal toe shapes, misplaced toes, missing toes, extra toes, oversized/small toes, misaligned ankles, mismatched foot sizes, scars or blemishes, nipple-like toes, swollen or deformed toes, overlapping toes, excess toenail, incorrect toe count, uneven toe count, unnatural foot proportions
```

**Negative Prompt Categories**:

| Category | Tags |
|----------|------|
| **Quality** | worst quality, blurry, jpeg artifacts, low quality |
| **Anatomy** | bad anatomy, malformed limbs, extra fingers, deformed hands |
| **Watermarks** | watermark, signature, artist name, text, username |
| **Composition** | cropped, multiple view, reference sheet |
| **Body Issues** | extra limbs, duplicate, bad proportions, disfigured |
| **Embeddings** | unaestheticXLv13, negativeXL_D (SDXL specific) |

**Simplified Negative** (For faster iteration):

```text
worst quality, low quality, blurry, bad anatomy, extra fingers, malformed hands, watermark, signature, text, cropped, ugly, deformed
```

---

## Complete Prompt Templates

### Template A: Japanese Warrior Portrait (Original Reference)

**Positive**:
```text
hycg, hysp, dynamic_outline, masterpiece, best quality, high quality, extremely detailed CG unity 8k wallpaper, extremely detailed, High Detail, vibrant colors, anime style, cover art, (artist:quasarcake:0.8), (mon (monmon2133):0.5), (mochizuki kei:0.95), (wlop:0.6), extreme aesthetic, masterpiece, best quality, good quality, newest, very aesthetic, absurdres, Visual impact, 32K UHD, colorful, sharp focus, impactful picture, offcial art, 1girl, solo, looking at viewer, short hair, hair ornament, red eyes, gloves, white background, ribbon, holding, bare shoulders, jewelry, hair ribbon, upper body, weapon, flower, white hair, earrings, parted lips, japanese clothes, sword, hair flower, kimono, necklace, holding weapon, from side, sash, profile, holding sword, obi, red gloves, beads, black kimono
```

**Negative**:
```text
unaestheticXLv13, negativeXL_D, watermark, signature, Artist name, Navel, bad anatomy, blurry, disembodied limb, Two navel eyes, worst quality, artist name, Hand with excessive fingers, Foot with excessive toes, Hand with surplus fingers, Hand with deficient fingers, Abnormal anatomy, Poorly formed hands, Deformed hands and fingers, Additional limbs, Excessive limbs, Abnormal finger interlocking duplicate, cropped, text, jpeg, artifacts, signature, watermark, username, blurry, artist name, trademark, title, muscular, sd character, multiple view, Reference sheet, long body, malformed limbs, multiple breasts, cloned face, malformed, mutated, bad anatomy, disfigured, bad proportions, duplicate, bad feet, artist name, extra limbs, ugly, fused anus, text font ui, missing, bad foot quality, twisted toes, asymmetric toes, abnormal toe shapes, misplaced toes, missing toes, extra toes, oversized/small toes, misaligned ankles, mismatched foot sizes, scars or blemishes, nipple-like toes, swollen or deformed toes, overlapping toes, excess toenail, incorrect toe count, uneven toe count, unnatural foot proportions
```

---

### Template B: Universal Character Portrait

**Positive**:
```text
masterpiece, best quality, high quality, extremely detailed CG unity 8k wallpaper, extremely detailed, High Detail, vibrant colors, anime style, cover art, (artist:quasarcake:0.8), (mon (monmon2133):0.5), (mochizuki kei:0.95), (wlop:0.6), extreme aesthetic, very aesthetic, absurdres, Visual impact, colorful, sharp focus, impactful picture, offcial art,
[INSERT CHARACTER DESCRIPTION HERE]
```

**Negative**:
```text
unaestheticXLv13, negativeXL_D, worst quality, low quality, blurry, bad anatomy, extra fingers, malformed hands, deformed hands and fingers, extra limbs, bad proportions, watermark, signature, text, cropped, ugly, disfigured, mutated, duplicate
```

---

## Practical Application Examples

### Example 1: Fantasy Mage Character

**Positive**:
```text
masterpiece, best quality, high quality, extremely detailed CG unity 8k wallpaper, extremely detailed, High Detail, vibrant colors, anime style, cover art, (artist:quasarcake:0.8), (mon (monmon2133):0.5), (mochizuki kei:0.95), (wlop:0.6), extreme aesthetic, very aesthetic, absurdres, Visual impact, colorful, sharp focus, impactful picture, offcial art, 1girl, solo, looking at viewer, long hair, purple hair, gradient hair, glowing eyes, blue eyes, magic circle, floating, wizard hat, cape, staff, holding staff, magical particles, starry background, night sky, elegant dress, jewelry, confident expression, dynamic pose, full body, fantasy setting
```

---

### Example 2: Modern Fashion Portrait

**Positive**:
```text
masterpiece, best quality, high quality, extremely detailed CG unity 8k wallpaper, extremely detailed, High Detail, vibrant colors, anime style, cover art, (artist:quasarcake:0.8), (mon (monmon2133):0.5), (mochizuki kei:0.95), (wlop:0.6), extreme aesthetic, very aesthetic, absurdres, Visual impact, colorful, sharp focus, impactful picture, offcial art, 1girl, solo, looking at viewer, black hair, ponytail, brown eyes, casual clothes, hoodie, headphones around neck, smartphone, urban background, city lights, bokeh, evening, street fashion, confident smile, upper body, contemporary setting
```

---

### Example 3: Elegant Gothic Portrait

**Positive**:
```text
masterpiece, best quality, high quality, extremely detailed CG unity 8k wallpaper, extremely detailed, High Detail, vibrant colors, anime style, cover art, (artist:quasarcake:0.8), (mon (monmon2133):0.5), (mochizuki kei:0.95), (wlop:0.6), extreme aesthetic, very aesthetic, absurdres, Visual impact, colorful, sharp focus, impactful picture, offcial art, 1girl, solo, looking at viewer, long white hair, red eyes, pale skin, gothic lolita dress, black dress, lace, roses, thorns, dark atmosphere, cathedral background, stained glass, dramatic lighting, melancholic expression, sitting, elegant pose, detailed fabric
```

---

### Example 4: Action Battle Scene

**Positive**:
```text
masterpiece, best quality, high quality, extremely detailed CG unity 8k wallpaper, extremely detailed, High Detail, vibrant colors, anime style, cover art, (artist:quasarcake:0.8), (mon (monmon2133):0.5), (mochizuki kei:0.95), (wlop:0.6), extreme aesthetic, very aesthetic, absurdres, Visual impact, colorful, sharp focus, impactful picture, offcial art, 1girl, solo, dynamic pose, action scene, silver hair, flowing hair, wind effect, determined expression, armor, futuristic armor, energy sword, glowing weapon, combat stance, motion blur, particle effects, debris, dramatic angle, from below, intense lighting, battlefield background
```

---

## Subject Component Library

### Hair Styles

```text
short hair, long hair, very long hair, medium hair, twintails, ponytail, braid, side braid, french braid, bun, messy hair, straight hair, wavy hair, curly hair, hime cut, bob cut, asymmetrical hair, hair over one eye, bangs, blunt bangs, side bangs, swept bangs, parted bangs, hair between eyes
```

### Hair Colors

```text
black hair, brown hair, blonde hair, white hair, silver hair, gray hair, red hair, pink hair, blue hair, purple hair, green hair, orange hair, gradient hair, multicolored hair, streaked hair, two-tone hair
```

### Eye Features

```text
[color] eyes, heterochromia, glowing eyes, detailed eyes, sparkling eyes, half-closed eyes, closed eyes, looking at viewer, looking away, looking up, looking down, eye contact
```

### Expressions

```text
smile, gentle smile, confident smile, smirk, serious, determined, melancholic, sad, happy, surprised, embarrassed, blushing, parted lips, open mouth, closed mouth, teeth showing
```

### Poses

```text
standing, sitting, kneeling, lying down, leaning, crossed arms, hands on hips, hand on chest, hand raised, reaching out, dynamic pose, action pose, relaxed pose, elegant pose, combat stance
```

### Compositions

```text
portrait, upper body, cowboy shot, full body, close-up, from above, from below, from side, from behind, dutch angle, profile, three-quarter view, looking back
```

### Backgrounds

```text
simple background, white background, gradient background, detailed background, outdoors, indoors, sky, clouds, sunset, night sky, starry sky, city, nature, forest, ocean, fantasy setting, futuristic setting
```

---

## Recommended Generation Settings

### SDXL Settings

| Parameter | Recommended Value |
|-----------|------------------|
| **Steps** | 25-40 |
| **Sampler** | DPM++ 2M Karras / Euler a |
| **CFG Scale** | 7-9 |
| **Resolution** | 1024x1024 (square) / 832x1216 (portrait) / 1216x832 (landscape) |
| **Clip Skip** | 2 |

### Hires Fix Settings (For upscaling)

| Parameter | Recommended Value |
|-----------|------------------|
| **Upscaler** | 4x-UltraSharp / ESRGAN_4x |
| **Hires Steps** | 15-20 |
| **Denoising** | 0.4-0.55 |
| **Upscale** | 1.5x-2x |

---

## Quick Customization Guide

### Step 1: Copy Base Quality + Artist Mix

```text
masterpiece, best quality, high quality, extremely detailed CG unity 8k wallpaper, extremely detailed, High Detail, vibrant colors, anime style, cover art, (artist:quasarcake:0.8), (mon (monmon2133):0.5), (mochizuki kei:0.95), (wlop:0.6), extreme aesthetic, very aesthetic, absurdres, Visual impact, colorful, sharp focus, impactful picture, offcial art,
```

### Step 2: Add Character Count + Gender

```text
1girl, solo,
```

or `1boy, solo,` / `2girls,` / `1girl, 1boy,`

### Step 3: Add Pose + Gaze

```text
looking at viewer, [pose],
```

### Step 4: Add Appearance Details

```text
[hair length] [hair color] hair, [eye color] eyes, [expression],
```

### Step 5: Add Clothing + Accessories

```text
[clothing type], [accessories], [held items],
```

### Step 6: Add Composition + Background

```text
[shot type], [background description]
```

### Step 7: Use Full Negative Prompt

Copy the comprehensive negative prompt from above.

---

## Troubleshooting

### Issue: Hands/Fingers Look Wrong

**Solutions**:
- Ensure negative prompt includes all hand-related terms
- Add to positive: `detailed hands, beautiful hands, perfect fingers`
- Use inpainting to fix specific areas
- Lower CFG scale slightly (try 6-7)

### Issue: Face Looks Distorted

**Solutions**:
- Add to positive: `detailed face, beautiful face, perfect face`
- Add to negative: `deformed face, ugly face, asymmetrical face`
- Use ADetailer extension
- Ensure resolution is adequate (min 768px on shortest side)

### Issue: Colors Too Saturated/Flat

**Solutions**:
- Adjust artist weights (lower quasarcake for less saturation)
- Add: `balanced colors, natural lighting` for softer look
- Add: `high contrast, vivid colors` for more punch
- Adjust CFG scale

### Issue: Style Not Matching Artist Mix

**Solutions**:
- Verify checkpoint compatibility with artist tags
- Increase/decrease individual artist weights
- Try different artist combinations
- Check if using correct SDXL model

---

## Style Variants

### Variant A: Soft Ethereal

```text
masterpiece, best quality, extremely detailed, soft lighting, ethereal atmosphere, dreamy, pastel colors, gentle expression, (wlop:0.95), (artist:ask (askzy):0.7), delicate details, flowing fabric, light particles, magical atmosphere
```

### Variant B: Bold Dynamic

```text
masterpiece, best quality, extremely detailed, dynamic lighting, high contrast, bold colors, dramatic pose, (lack:0.85), (redjuice:0.7), action lines, impact frame, intense expression, powerful atmosphere
```

### Variant C: Elegant Classic

```text
masterpiece, best quality, extremely detailed, soft studio lighting, elegant composition, refined details, (kantoku:0.9), (anmi:0.7), graceful pose, beautiful fabric, sophisticated atmosphere, clean background
```

---

## Version History

- **v1.0** (2026-01-17): Initial version
  - Extracted from user's SD prompt for premium anime portrait
  - Core artist mix: quasarcake + mochizuki kei + wlop + monmon2133
  - Comprehensive negative prompt with anatomy fixes
  - 4 practical examples (warrior, mage, modern, gothic)
  - Subject component library for easy customization
  - SDXL recommended settings included

---

## Usage License

This style template is open for use in Stable Diffusion prompt generation for anime character illustrations. Freely adjustable based on specific project needs and checkpoint compatibility. Artist weights and negative prompts may need adjustment based on model used.
