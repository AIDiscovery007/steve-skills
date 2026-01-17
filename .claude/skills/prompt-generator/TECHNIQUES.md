# Prompt Writing Techniques Reference

Comprehensive guide to the 8 core prompt writing techniques for AI image generation.

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

---

## 1. Number Emphasis Technique

### Principle

AI image generators tend to create "rich" compositions with multiple elements. Using "1" before key elements actively constrains the AI to generate exactly one instance, preventing unwanted repetition or scattered composition.

### Core Concept

**The number "1" acts as a precision constraint**, telling the AI:
- Generate exactly one instance of this element
- Make this the focal point
- Don't scatter or multiply this element
- Emphasize uniqueness and singularity

### Usage Method

**Syntax**: `1 [element]`

Place "1" directly before the most important subject or elements you want to emphasize.

### Examples

#### Example 1: Portrait

❌ **Bad** (vague, may generate multiple):
```
woman in red hat smoking cigarette
```
**Problem**: AI might generate multiple women, multiple hats, or scattered cigarettes

✅ **Good** (precise, controlled):
```
1 close-up face centered, 1 red hat, 1 cigarette
```
**Result**: Exactly one woman, one hat, one cigarette - focused composition

---

#### Example 2: Product Photography

❌ **Bad**:
```
coffee cup on table with flowers
```
**Problem**: May generate multiple cups, cluttered flowers

✅ **Good**:
```
1 ceramic coffee cup centered, 1 small flower arrangement
```
**Result**: Single cup as focus, controlled flower presence

---

#### Example 3: Scene Composition

❌ **Bad**:
```
tree in landscape with mountains
```
**Problem**: May generate multiple trees, cluttered landscape

✅ **Good**:
```
1 lone tree in foreground, mountain range background
```
**Result**: Emphasis on singular tree, clear focal point

---

### When to Use

✅ **Use "1" when**:
- You want a clear, single focal point
- Preventing element multiplication is crucial
- Creating minimalist or focused compositions
- The subject should be unique/singular
- Portrait work (1 person, 1 face)
- Product photography (1 product)

❌ **Don't use "1" when**:
- You actually want multiple elements
- Creating crowd or busy scenes
- Pattern or repetition is desired
- The element should naturally appear in multiples

### Common Patterns

**Portrait Photography**:
```
1 [age] [gender], 1 [distinctive feature], 1 [prop/accessory]
Example: 1 elderly man, 1 weathered hat, 1 walking cane
```

**Product Photography**:
```
1 [product] [position], 1 [accompanying element]
Example: 1 perfume bottle centered, 1 white rose
```

**Landscape with Focal Point**:
```
1 [main subject] in [position], [background elements]
Example: 1 red barn in valley, rolling green hills
```

---

### Advanced Application

**Multiple "1" Elements** (creating controlled complexity):
```
1 woman in red dress, 1 vintage bicycle, 1 street lamp,
cobblestone street, afternoon light
```
Each "1" element is controlled, but they coexist in a composed scene.

---

## 2. Repetition Reinforcement Technique

### Principle

AI models assign higher weight to concepts that appear multiple times in a prompt. **Repeating key style elements 2-3 times reinforces their importance** and ensures the AI prioritizes these characteristics.

### Core Concept

**Repetition = Emphasis**
- First mention: Introduces the concept
- Second mention: Reinforces the style
- Third mention: Solidifies the aesthetic
- More than 3: Diminishing returns, may cause over-emphasis

### Usage Method

Repeat core style descriptors 2-3 times throughout the prompt using:
- Direct repetition (same words)
- Synonym variation (related terms)
- Conceptual echoing (similar aesthetic descriptors)

### Examples

#### Example 1: Retro Poster Style

❌ **Bad** (single mention):
```
retro poster, woman with sunglasses
```
**Problem**: "Retro" mentioned only once, may be interpreted weakly

✅ **Good** (reinforced 3 times):
```
Retro 80s poster style, 1 woman with sunglasses,
vintage movie poster aesthetic, 80s design language
```
**Result**: Strong retro/80s emphasis through multiple reinforcements

**Breakdown**:
1. "Retro 80s poster style" - Direct style statement
2. "vintage movie poster" - Synonym reinforcement
3. "80s design language" - Conceptual echo

---

#### Example 2: Cinematic Mood

❌ **Bad**:
```
cinematic photo, moody lighting, urban scene
```

✅ **Good**:
```
cinematic photography, film noir aesthetic, moody atmosphere,
urban night scene, cinematic composition, dramatic lighting
```

**Repetition Analysis**:
- "Cinematic" appears 2x (photography, composition)
- "Moody/dramatic" reinforces emotional tone
- "Film noir" echoes cinematic concept

---

#### Example 3: Watercolor Style

❌ **Bad**:
```
watercolor painting of flowers
```

✅ **Good**:
```
watercolor painting, delicate floral composition,
soft watercolor washes, flowing pigment, aquarelle technique
```

**Repetition Strategy**:
- "Watercolor" + "aquarelle" (direct + synonym)
- "Soft washes" + "flowing pigment" (technique reinforcement)

---

### When to Use

✅ **Use repetition when**:
- Emphasizing a specific style or aesthetic
- Ensuring AI captures a particular mood
- Creating strong thematic consistency
- The style is complex or nuanced
- You need guaranteed style adherence

❌ **Don't overuse when**:
- Simple, straightforward styles (over-emphasis can backfire)
- You want variety and experimentation
- The concept is already unambiguous

### Repetition Strategies

**Strategy 1: Direct Repetition**
```
cyberpunk city, neon-lit cyberpunk aesthetic, cyberpunk atmosphere
```

**Strategy 2: Synonym Variation**
```
retro poster, vintage design, nostalgic 80s aesthetic
```

**Strategy 3: Conceptual Echoing**
```
moody atmosphere, noir lighting, dramatic shadows, mysterious ambiance
```
(All reinforce "dark/dramatic" mood)

**Strategy 4: Medium + Technique + Style**
```
oil painting portrait, traditional oil technique, classical painting approach
```

---

### Optimal Repetition Count

- **2 times**: Minimum for effective reinforcement
- **3 times**: Optimal for strong emphasis without over-doing
- **4+ times**: Diminishing returns, may feel forced

### Advanced Application

**Layered Repetition** (combining strategies):
```
vintage 1920s portrait, Art Deco aesthetic, Gatsby-era glamour,
sepia-toned photograph, antique photo finish, 1920s fashion,
nostalgic elegance
```

**Analysis**:
- "Vintage/antique/nostalgic" = Era reinforcement (3x)
- "1920s" appears 2x directly
- "Art Deco/Gatsby-era" = Style era echoes
- Multiple layers reinforce the 1920s aesthetic powerfully

---

## 3. Negative Exclusion Technique

### Principle

AI models add "helpful" or "typical" elements by default. **You must actively exclude unwanted elements** through negative prompting to maintain control and achieve clean, focused results.

### Core Concept

**What you don't specify, AI might add anyway.**

Common AI assumptions:
- Text/watermarks on designs
- Borders/frames around images
- Background elements in portraits
- Mockups for product designs
- "Helpful" embellishments

**Negative exclusion prevents these assumptions.**

### Usage Method

**Two approaches**:

1. **In-prompt negatives**: Include "no [element]" in the prompt text
   ```
   clean design, no watermark, no border, no text
   ```

2. **Parameter-based negatives**: Use `--no` parameter
   ```
   [prompt] --no watermark,border,text
   ```

**Best Practice**: Use both for maximum effectiveness
```
clean poster design, no text, no watermark --no text,watermark,border
```

### Examples

#### Example 1: Clean Design

❌ **Bad** (assumes AI will understand "clean"):
```
modern poster design
```
**Problem**: AI may add text, borders, mockups, or ornamental elements

✅ **Good** (explicit exclusions):
```
modern poster design, no text, no watermark, no border,
no mockup --no text,watermark,border,mockup
```
**Result**: Pure visual design without unwanted additions

---

#### Example 2: Portrait Photography

❌ **Bad**:
```
professional portrait
```
**Problem**: May include hands (often problematic), busy background, props

✅ **Good**:
```
professional portrait, clean background, no hands,
no props --no hands,clutter,background-detail
```
**Result**: Focused portrait without distracting elements

---

#### Example 3: Product Photography

❌ **Bad**:
```
product shot of perfume bottle
```
**Problem**: May add text, labels, excessive decorations

✅ **Good**:
```
product shot of perfume bottle, minimal composition,
no text, no labels, no decorations --no text,labels,clutter
```
**Result**: Clean product focus

---

### Common Elements to Exclude

**For Design Work**:
- `no text, no watermark, no border, no frame, no mockup`
- `no logo, no typography, no labels`

**For Photography**:
- `no hands` (hands are often problematic in AI)
- `no busy background, no clutter, no background detail`
- `no props, no accessories` (if minimalism desired)

**For Portraits**:
- `no hands, no fingers`
- `no background people, no crowds`
- `no props, no objects`

**For Product Shots**:
- `no text, no labels, no branding`
- `no shadows, no reflections` (if desired)
- `no background, no context` (for isolated shots)

**For Artistic Work**:
- `no frame, no border, no mat`
- `no signature, no artist mark`
- `no text overlay`

---

### When to Use

✅ **Always use negative exclusion when**:
- Creating clean, minimal designs
- Product photography
- Poster/graphic design work
- You need precise control
- Previous generations included unwanted elements

❌ **Don't use when**:
- Those elements are actually desired
- Creating busy, maximalist compositions
- The AI naturally excludes them

### Effective Negative Patterns

**Minimalist Photography**:
```
[subject], clean composition, no clutter, no background detail,
no props --no clutter,detail,complexity
```

**Product Design**:
```
[product], no text, no labels, no watermark, no mockup,
pure product focus --no text,labels,watermark,mockup
```

**Portrait Work**:
```
[portrait description], no hands, no props, clean background
--no hands,props,background-clutter
```

**Graphic Design**:
```
[design description], no text, no border, no frame, no mockup
--no text,border,frame,mockup
```

---

### Advanced Application

**Combining with positive terms**:
```
clean modern poster, minimalist composition, pure visual design,
no text, no watermark, no border, no decorative elements
--no text,watermark,border,decoration
```

**Exclusion hierarchy** (exclude broad then specific):
```
portrait, no background detail, no props, no hands, no jewelry,
no accessories --no background-detail,props,hands,jewelry
```

---

## 4. Medium Definition Technique

### Principle

**The medium determines overall texture, rendering style, and visual approach.** Defining the creation medium first establishes the framework within which all other descriptions operate.

### Core Concept

**Medium = Foundation**

Think of it like choosing your canvas:
- Oil painting → Rich, textured, layered
- Photography → Realistic, lens-based, lighting-focused
- 3D render → Clean, perfect, digital precision
- Watercolor → Soft, flowing, transparent
- Ink sketch → Linear, expressive, gestural

**All subsequent descriptions are interpreted through this medium.**

### Usage Method

**Start your prompt with the medium**:
```
[Medium] [subject description], [details...]

Examples:
- oil painting portrait of...
- 35mm film photography of...
- 3D render of...
- ink sketch of...
```

### Examples

#### Example 1: Portrait Comparison

❌ **Bad** (medium undefined):
```
portrait of elderly woman, dramatic lighting
```
**Problem**: Could be photo, painting, 3D, digital art - ambiguous

✅ **Good** (medium defined):
```
oil painting portrait of elderly woman, dramatic lighting,
impasto texture, visible brushstrokes
```
**Result**: Clear oil painting aesthetic with appropriate texture

**Alternative mediums**:
```
35mm film photography portrait of elderly woman, dramatic lighting
→ Photographic, realistic, film grain

digital illustration portrait of elderly woman, dramatic lighting
→ Digital art aesthetic, stylized

charcoal sketch portrait of elderly woman, dramatic lighting
→ Sketchy, expressive, monochrome
```

---

#### Example 2: Landscape

❌ **Bad**:
```
mountain landscape, beautiful scenery
```

✅ **Good options**:

**Watercolor**:
```
watercolor landscape painting, mountain vista, soft washes,
flowing pigment, paper texture
```

**Photography**:
```
landscape photography, mountain range, 35mm lens,
golden hour lighting, natural colors
```

**3D Render**:
```
3D rendered landscape, mountain environment, clean geometry,
smooth surfaces, digital precision
```

**Each medium produces completely different results.**

---

#### Example 3: Product Visualization

**Photography medium**:
```
commercial product photography, sleek smartphone,
studio lighting, reflective surface
```

**3D Render medium**:
```
3D product render, sleek smartphone, perfect geometry,
ray-traced reflections, digital precision
```

**Illustration medium**:
```
technical illustration, sleek smartphone, line work,
exploded view, diagram style
```

---

### Common Medium Categories

**Photography Mediums**:
- `35mm film photography`
- `medium format photography`
- `digital photography`
- `studio photography`
- `street photography`
- `documentary photography`

**Painting Mediums**:
- `oil painting`
- `watercolor painting`
- `acrylic painting`
- `gouache painting`
- `ink painting`

**Drawing Mediums**:
- `pencil sketch`
- `charcoal drawing`
- `ink sketch`
- `pen and ink`
- `graphite drawing`

**Digital Mediums**:
- `digital illustration`
- `3D render`
- `digital painting`
- `vector art`
- `pixel art`
- `matte painting`

**Print/Graphic Mediums**:
- `screen print`
- `linocut print`
- `woodblock print`
- `lithograph`
- `etching`

**Mixed/Specialty**:
- `collage`
- `mixed media`
- `photomontage`
- `sculptural photography`

---

### When to Use

✅ **Always define medium when**:
- Starting a new prompt
- Medium significantly impacts the result
- You have a specific visual approach in mind
- Creating anything beyond simple concepts

❌ **Medium may be optional when**:
- Creating abstract concepts where medium is irrelevant
- The prompt is extremely simple
- You want the AI to choose the medium

### Medium Impact Examples

**Same subject, different mediums**:

**Subject**: "Dragon in mountain landscape"

```
oil painting of dragon in mountain landscape
→ Painterly, textured, classical fantasy art feel

3D render of dragon in mountain landscape
→ Digital, clean, modern CG aesthetic

ink sketch of dragon in mountain landscape
→ Expressive, gestural, traditional illustration

matte painting of dragon in mountain landscape
→ Cinematic, detailed, concept art style

watercolor painting of dragon in mountain landscape
→ Soft, flowing, delicate artistic approach
```

**Each produces fundamentally different results.**

---

### Advanced Application

**Medium + Technique**:
```
oil painting portrait, impasto technique, palette knife work,
thick paint application, visible brushstrokes
```
(Defines both medium and specific technique within that medium)

**Medium + Era/Movement**:
```
oil painting portrait, Renaissance technique, chiaroscuro lighting,
classical composition, Old Master approach
```
(Defines medium and historical style)

**Hybrid Medium**:
```
mixed media collage, photography elements with painted texture,
layered paper, analog and digital combination
```
(Defines complex medium approach)

---

## 5. Color Control Technique

### Principle

**Strict color limitation = Style purity and cohesion.**

Vague color terms like "colorful" or "vibrant" give the AI too much freedom. **Specifying exact colors maintains visual consistency and prevents random color additions.**

### Core Concept

**Color Formula**:
```
[Main color/palette] with accents of [accent color 1] and [accent color 2]
```

This structure:
1. Establishes dominant color scheme
2. Defines supporting colors
3. Limits AI's color choices
4. Creates cohesive palette

### Usage Method

**Structure**:
1. Identify 1-2 dominant colors
2. Choose 1-2 accent colors
3. Use specific color names (not vague terms)
4. Apply the formula

### Examples

#### Example 1: Minimalist Design

❌ **Bad** (vague):
```
minimalist poster, nice colors
```
**Problem**: "Nice colors" is meaningless to AI - could be anything

✅ **Good** (specific):
```
minimalist poster, black and white base with accents of coral red
```
**Result**: Clear, limited palette creates sophisticated look

---

#### Example 2: Nature Scene

❌ **Bad**:
```
forest landscape, colorful
```
**Problem**: "Colorful" → AI adds random colors, loses cohesion

✅ **Good**:
```
forest landscape, rich green tones with accents of golden sunlight
and rust-colored leaves
```
**Result**: Cohesive natural palette

---

#### Example 3: Cyberpunk Scene

❌ **Bad**:
```
cyberpunk city, neon lights
```
**Problem**: "Neon lights" → AI might use all neon colors chaotically

✅ **Good**:
```
cyberpunk cityscape, electric blue and hot pink neon,
dark cyan shadows, minimal color palette
```
**Result**: Specific iconic cyberpunk colors, controlled palette

---

### Color Naming Strategies

**Use Specific Color Names**:

❌ **Avoid**:
- colorful, vibrant, nice colors, pretty palette
- blue (which blue?), red (which red?), green (which green?)

✅ **Use Specific Names**:
- electric blue, navy blue, powder blue, cobalt blue
- crimson red, rust red, burgundy, scarlet
- sage green, forest green, mint green, olive green
- hot pink, dusty rose, magenta, blush pink

**Color Families to Specify**:
```
Blues: navy, cobalt, electric blue, powder blue, teal, cyan
Reds: crimson, burgundy, rust, scarlet, coral, vermillion
Greens: sage, forest, olive, mint, emerald, lime
Yellows: golden, mustard, lemon, ochre, amber
Neutrals: warm gray, cool gray, charcoal, taupe, ivory
```

---

### Color Palette Patterns

#### Pattern 1: Monochromatic
```
monochromatic blue palette, ranging from navy to powder blue,
tonal variation, cohesive color scheme
```

#### Pattern 2: Complementary
```
deep orange base with accents of teal blue,
complementary color scheme, high contrast
```

#### Pattern 3: Analogous
```
warm autumn palette, golden yellow, burnt orange, and rust red,
harmonious color flow
```

#### Pattern 4: Limited Palette
```
black ink with accents of light blue and green,
minimal color palette, restrained color use
```

#### Pattern 5: Duotone
```
duotone effect, hot pink and electric blue only,
two-color palette, graphic color treatment
```

---

### When to Use

✅ **Use color control when**:
- Creating cohesive designs
- Establishing brand identity
- Minimalist or sophisticated aesthetics
- You need color consistency
- Previous generations had color issues

❌ **Less critical when**:
- Creating intentionally chaotic/maximalist work
- Realistic photography (natural colors)
- You want AI to surprise you with color choices

### Common Color Scenarios

**Minimalist/Modern**:
```
[subject], monochromatic gray palette with single red accent
[subject], black and white with metallic gold highlights
[subject], muted earth tones, beige and warm gray
```

**Vintage/Retro**:
```
[subject], warm sepia tones, aged photograph palette
[subject], vintage 70s colors, burnt orange and avocado green
[subject], faded pastel colors, nostalgic color treatment
```

**Bold/Graphic**:
```
[subject], bold primary colors, red yellow and blue
[subject], high contrast, pure black and vibrant cyan
[subject], neon palette, hot pink and electric green
```

**Natural/Organic**:
```
[subject], earthy palette, warm browns and sage green
[subject], ocean colors, deep teal and seafoam green
[subject], forest tones, moss green and rich browns
```

**Moody/Atmospheric**:
```
[subject], cool blue-gray tones, muted palette
[subject], warm amber lighting, golden and rust tones
[subject], midnight blue with silver accents
```

---

### Advanced Application

**Color + Mood Connection**:
```
melancholic portrait, desaturated blue-gray tones,
cool palette enhancing emotional distance
```
(Color reinforces emotional intent)

**Color + Light Integration**:
```
sunset scene, warm golden hour palette, orange and pink sky,
warm ambient light matching color scheme
```
(Color and lighting work together)

**Color + Medium Synergy**:
```
watercolor landscape, transparent blue washes,
soft color bleeds, muted aquarelle palette
```
(Color description matches medium characteristics)

---

## 6. Professional Terminology Technique

### Principle

**Professional terminology = Precise control; vague adjectives = ambiguous interpretation.**

Using domain-specific technical terms from photography, art, and design gives the AI exact instructions instead of generic descriptions that could be interpreted many ways.

### Core Concept

**Replace vague adjectives with precise technical terms.**

Vague terms like "nice," "good," "beautiful," "dramatic" are interpreted differently by everyone (including AI). Professional terminology has specific, agreed-upon meanings in each field.

### Usage Method

**Learn terminology from three main domains**:
1. Photography (camera, lens, lighting techniques)
2. Art (painting techniques, art movements, style terms)
3. Design (composition, layout, graphic principles)

**Replace generic descriptions with specific technical terms.**

---

## Photography Domain

### Camera & Lens Terms

**Focal Length**:
```
❌ Bad: blurry background
✅ Good: 85mm lens, shallow depth of field, f/1.8 aperture
```

**Common Focal Lengths**:
- `14-24mm`: Ultra-wide, expansive, distortion
- `35mm`: Standard wide, documentary feel
- `50mm`: Normal perspective, natural view
- `85mm`: Portrait lens, flattering compression
- `200mm`: Telephoto, compressed perspective

**Aperture Terms**:
```
❌ Bad: everything sharp
✅ Good: f/16 aperture, deep depth of field, landscape photography
```

**Aperture Values**:
- `f/1.4 - f/2.8`: Shallow DOF, subject isolation, bokeh
- `f/4 - f/5.6`: Moderate DOF, balanced sharpness
- `f/8 - f/11`: Deep DOF, most sharp
- `f/16 - f/22`: Everything in focus, landscape

---

### Lighting Terms

**Natural Light**:
```
❌ Bad: nice lighting, good light
✅ Good: golden hour lighting, warm directional sunlight,
        soft shadows, 30 minutes before sunset
```

**Professional Lighting Terms**:
- `golden hour`: Warm, low-angle sun (first/last hour of daylight)
- `blue hour`: Cool twilight period after sunset
- `overcast daylight`: Soft, diffused, even lighting
- `direct sunlight`: Harsh, high-contrast, strong shadows
- `window light`: Soft directional natural light
- `backlighting`: Light from behind subject
- `rim lighting`: Edge highlighting from backlight
- `side lighting`: Light from 90° angle, dimensional

**Studio Lighting**:
```
❌ Bad: professional lighting
✅ Good: three-point lighting setup, key light camera left,
        fill light camera right, rim light behind
```

**Studio Terms**:
- `key light`: Main light source, primary illumination
- `fill light`: Secondary light, softens shadows
- `rim light` / `back light`: Separates subject from background
- `softbox lighting`: Soft, diffused, even light
- `hard light`: Direct, creating strong shadows
- `high-key lighting`: Bright, minimal shadows
- `low-key lighting`: Dark, dramatic shadows

**Artistic Lighting**:
```
❌ Bad: dramatic lighting
✅ Good: chiaroscuro lighting, strong contrast between light and dark,
        tenebrism technique, single light source
```

**Art Lighting Terms**:
- `chiaroscuro`: Strong light-dark contrast (Italian, "light-dark")
- `tenebrism`: Extreme chiaroscuro, dramatic shadows
- `Rembrandt lighting`: Triangular light on shadowed cheek
- `butterfly lighting`: Light from above, shadow under nose

---

### Photography Style Terms

**Shot Types**:
```
❌ Bad: close picture
✅ Good: extreme close-up, macro photography, 1:1 magnification
```

**Frame Types**:
- `extreme close-up`: Face details, intimate
- `close-up`: Head and shoulders
- `medium shot`: Waist up
- `full shot`: Entire subject
- `wide shot`: Subject in environment
- `establishing shot`: Environmental context

**Angles**:
- `low angle`: Camera below subject, looking up
- `high angle`: Camera above, looking down
- `eye level`: Natural perspective
- `bird's eye view`: Directly overhead
- `Dutch angle`: Tilted, dynamic tension

---

## Art Domain

### Painting Techniques

**Brush Techniques**:
```
❌ Bad: thick paint
✅ Good: impasto technique, palette knife application,
        thick paint texture, visible brushstrokes
```

**Technique Terms**:
- `impasto`: Thick paint application, textured surface
- `glazing`: Thin transparent layers
- `scumbling`: Dry brush over dry paint
- `wet-on-wet`: Painting into wet paint
- `alla prima`: Completing in one session
- `pointillism`: Dots of color
- `crosshatching`: Layered parallel lines

**Painting Styles**:
```
❌ Bad: old-fashioned painting
✅ Good: Renaissance technique, sfumato shading,
        classical composition, Old Master approach
```

**Art Movement Terms**:
- `Renaissance`: Classical, balanced, realistic proportions
- `Baroque`: Dramatic, ornate, emotional
- `Impressionist`: Loose brushwork, light focus, color emphasis
- `Art Nouveau`: Flowing lines, organic forms, decorative
- `Art Deco`: Geometric, glamorous, symmetrical
- `Abstract Expressionist`: Gestural, emotional, non-representational

---

### Color & Composition Terms

**Color Theory**:
```
❌ Bad: colors work well together
✅ Good: complementary color scheme, orange and teal,
        high color contrast, balanced palette
```

**Color Terms**:
- `complementary colors`: Opposite on color wheel (red/green)
- `analogous colors`: Adjacent on wheel (blue/green/cyan)
- `triadic colors`: Three equally spaced (red/yellow/blue)
- `monochromatic`: Single hue variations
- `split-complementary`: Base + two adjacent to complement
- `warm palette`: Reds, oranges, yellows
- `cool palette`: Blues, greens, purples

**Composition Terms**:
```
❌ Bad: well-composed, balanced
✅ Good: rule of thirds composition, subject at intersection point,
        golden ratio spiral, balanced negative space
```

**Layout Terms**:
- `rule of thirds`: Grid dividing frame into 9 sections
- `golden ratio`: 1.618:1 natural proportion
- `golden spiral`: Logarithmic spiral based on golden ratio
- `symmetrical composition`: Mirrored balance
- `asymmetrical balance`: Visual weight distributed unevenly
- `negative space`: Empty space around subject
- `leading lines`: Lines directing eye to subject
- `frame within frame`: Using elements to frame subject
- `diagonal composition`: Dynamic angle, movement

---

## Design Domain

**Typography Terms** (when applicable):
```
❌ Bad: text looks good
✅ Good: sans-serif typography, geometric letterforms,
        tight kerning, modern type treatment
```

**Layout Terms**:
```
❌ Bad: nicely arranged
✅ Good: grid system layout, modular spacing,
        hierarchical structure, visual rhythm
```

**Graphic Style Terms**:
- `minimalist design`: Reduced elements, essential only
- `maximalist design`: Rich, layered, abundant
- `brutalist design`: Raw, stark, unrefined
- `Swiss design`: Grid-based, sans-serif, objective
- `bauhaus`: Geometric, functional, no ornament

---

### Comprehensive Examples

#### Example 1: Portrait Photography

❌ **Bad** (all vague terms):
```
beautiful portrait, nice lighting, good background
```

✅ **Good** (professional terminology):
```
portrait photography, 85mm lens, f/2.0 aperture,
shallow depth of field, Rembrandt lighting setup,
soft window light camera left, subtle fill light camera right,
bokeh background, natural skin tones, eye-level perspective
```

---

#### Example 2: Landscape Photography

❌ **Bad**:
```
pretty landscape, good colors, nice light
```

✅ **Good**:
```
landscape photography, 24mm wide-angle lens, f/11 aperture,
deep depth of field, golden hour lighting, warm directional sunlight,
rule of thirds composition, leading lines to horizon,
high dynamic range, rich color saturation
```

---

#### Example 3: Oil Painting

❌ **Bad**:
```
painting with thick paint, dramatic lighting
```

✅ **Good**:
```
oil painting portrait, impasto technique, palette knife application,
visible brushstrokes, chiaroscuro lighting, tenebrism approach,
rich earth tone palette, Renaissance composition,
classical proportions, glazing in shadows
```

---

### When to Use

✅ **Always use professional terminology when**:
- You know the specific technique/term
- Creating photography-style work
- Replicating art styles or movements
- Need precise technical control
- Want sophisticated, professional results

❌ **Use simpler terms when**:
- Creating casual, spontaneous work
- The technical detail isn't relevant
- You genuinely don't know the right term (don't fake it)

### Building Your Terminology Vocabulary

**Photography Resources**:
- Learn camera settings (aperture, shutter, ISO)
- Study lighting setups (3-point, Rembrandt, butterfly)
- Understand lens characteristics (wide, normal, telephoto)

**Art Resources**:
- Study art movements (Renaissance, Baroque, Impressionism)
- Learn painting techniques (impasto, glazing, scumbling)
- Understand composition rules (thirds, golden ratio)

**Design Resources**:
- Learn layout principles (grid, hierarchy, balance)
- Study design movements (Bauhaus, Swiss, Brutalist)
- Understand color theory (complementary, analogous)

---

## 7. Hierarchical Description Technique

### Principle

**Clear hierarchy = AI understands priority.**

Describing elements in order of importance—from subject to details, from core to periphery—helps the AI prioritize what matters most and build the image in logical layers.

### Core Concept

**Hierarchical Order**:
1. Subject (what is it?)
2. Primary details (key characteristics)
3. Secondary details (supporting elements)
4. Atmosphere/mood (feeling)
5. Technical aspects (quality, finish)

**Each layer builds on the previous, creating depth and complexity.**

### Usage Method

**Structure your prompt as progressive layers**:
```
[Subject layer] → [Detail layer 1] → [Detail layer 2] →
[Atmosphere layer] → [Technical layer]
```

### Examples

#### Example 1: Portrait

❌ **Bad** (flat, no hierarchy):
```
face with beanie and cigarette, good lighting
```
**Problem**: No clear priority, AI doesn't know what's most important

✅ **Good** (hierarchical layers):
```
Subject layer: 1 close-up face centered
Detail layer 1: teal ribbed knit beanie pulled down to cover eyes
Detail layer 2: cigarette clenched between lips with faint smoke
Atmosphere layer: moody editorial lighting, subtle vignette
Technical layer: high-contrast, print-ready look
```

**How AI processes this**:
1. Creates centered close-up face (foundation)
2. Adds teal beanie covering eyes (primary detail)
3. Adds cigarette with smoke (secondary detail)
4. Applies moody lighting and vignette (atmosphere)
5. Applies high contrast finish (technical quality)

---

#### Example 2: Product Photography

❌ **Bad**:
```
perfume bottle with flowers, nice background
```

✅ **Good**:
```
Subject: 1 luxury perfume bottle centered
Primary detail: geometric glass design with golden cap
Secondary detail: 1 white rose beside bottle
Background: soft gradient background, cream to white
Lighting: soft key light from left, subtle reflections
Technical: ultra-sharp focus, 4K detail, commercial quality
```

---

#### Example 3: Landscape

❌ **Bad**:
```
mountain landscape with trees and lake
```

✅ **Good**:
```
Foreground: 1 lone pine tree on rocky outcrop
Midground: alpine lake with mirror reflection
Background: mountain range with snow-capped peaks
Atmosphere: early morning mist, ethereal quality
Lighting: soft pre-sunrise light, cool blue hour tones
Technical: deep depth of field, tack sharp, f/16 aperture
```

---

### Layering Patterns

#### Pattern 1: Portrait Hierarchy
```
Subject → Face/expression → Hair/clothing →
Props/accessories → Lighting → Background → Technical
```

**Example**:
```
1 young woman, serene expression, flowing white hair,
elegant white dress, 1 red rose in hand,
soft window light, minimal gray background,
shallow depth of field, high-resolution detail
```

---

#### Pattern 2: Scene Hierarchy
```
Main subject → Primary elements → Secondary elements →
Environment → Atmosphere → Lighting → Technical
```

**Example**:
```
1 vintage bicycle, worn leather seat and handlebar grips,
woven basket with flowers, cobblestone street setting,
nostalgic European atmosphere, warm afternoon light,
35mm film photography, slight grain
```

---

#### Pattern 3: Product Hierarchy
```
Product → Key features → Supporting elements →
Background → Lighting → Surface/texture → Technical
```

**Example**:
```
1 ceramic coffee cup, minimalist white design,
thin gold rim detail, 1 small plant beside cup,
clean white background, soft overhead lighting,
matte surface finish, ultra-detailed, 4K quality
```

---

### When to Use

✅ **Use hierarchical description when**:
- Creating complex scenes with multiple elements
- You need clear priorities
- Building detailed, layered compositions
- Combining many elements cohesively
- Professional or detailed work

❌ **Less critical when**:
- Creating very simple subjects
- Single-element compositions
- Abstract or minimalist work

### Advanced Hierarchy Techniques

**Embedded Sub-Hierarchies**:
```
Subject: 1 elderly craftsman
  Face details: weathered features, focused expression
  Hand details: calloused hands, holding tool
  Clothing: leather apron, rolled-up sleeves
Props: workbench with scattered tools
  Tool details: vintage hammer, worn wood plane
Environment: rustic workshop, soft dust particles in air
Lighting: single window light from left, dramatic shadows
```

**Spatial Hierarchy** (near to far):
```
Foreground: detailed close-up element
Midground: main subject with clear details
Background: softer, supporting environment
Atmosphere: overall mood tying layers together
```

---

## 8. Tension Creation Technique

### Principle

**Tension = Balanced coexistence of opposing elements, creating complexity and depth.**

Describing the interplay of contrasting qualities (experimental yet grounded, clear yet provocative) creates sophisticated, nuanced results that avoid being one-dimensional.

### Core Concept

**Simple concepts are one-dimensional:**
- "experimental design" → could be chaotic or weird
- "clear message" → could be boring or generic

**Tension creates depth:**
- "experimental but grounded" → innovative yet accessible
- "clear and provocative yet close and human" → contradictions create interest

**Opposing elements balance each other, creating sophisticated complexity.**

### Usage Method

**Combine contrasting qualities using "but," "yet," or "while":**
```
[Quality A] but [Opposite Quality B]
[Quality A] yet [Opposite Quality B]
[Quality A] while [Opposite Quality B]
```

### Examples

#### Example 1: Design Aesthetic

❌ **Bad** (one-dimensional):
```
experimental design
```
**Problem**: Could be chaotically weird or inaccessibly avant-garde

✅ **Good** (tension-balanced):
```
experimental but grounded design, innovative forms yet familiar structure
```
**Result**: Pushes boundaries while remaining accessible

---

#### Example 2: Portrait Mood

❌ **Bad**:
```
emotional portrait
```

✅ **Good**:
```
vulnerable yet strong expression, soft features with intense gaze,
delicate but powerful presence
```
**Result**: Complex emotional depth

---

#### Example 3: Visual Style

❌ **Bad**:
```
realistic painting
```

✅ **Good**:
```
realistic textures with conceptual abstraction,
photographic detail yet artistic interpretation
```
**Result**: Sophisticated blend of realism and artistry

---

### Tension Pairs (Opposites that Balance)

**Style Tensions**:
- Experimental ↔ Grounded
- Abstract ↔ Representational
- Minimal ↔ Rich
- Modern ↔ Timeless
- Bold ↔ Subtle
- Chaotic ↔ Structured

**Emotional Tensions**:
- Vulnerable ↔ Strong
- Warm ↔ Distant
- Intimate ↔ Universal
- Joyful ↔ Melancholic
- Calm ↔ Intense

**Visual Tensions**:
- Sharp ↔ Soft
- Light ↔ Dark
- Simple ↔ Complex
- Organic ↔ Geometric
- Rough ↔ Polished

**Conceptual Tensions**:
- Clear ↔ Mysterious
- Familiar ↔ Strange
- Controlled ↔ Spontaneous
- Precise ↔ Loose
- Rational ↔ Emotional

---

### Tension Applications

#### Application 1: Conceptual Work

```
abstract concept, clear message yet open to interpretation,
structured chaos, rational foundation with emotional overtones
```

**Effect**: Intellectual yet accessible

---

#### Application 2: Portrait Photography

```
editorial portrait, soft diffused lighting yet dramatic shadows,
intimate composition with universal appeal,
natural expression with carefully controlled styling
```

**Effect**: Professional yet genuine

---

#### Application 3: Illustration Style

```
playful illustration, loose gestural lines yet precise composition,
energetic but balanced, spontaneous feel with deliberate structure
```

**Effect**: Lively yet intentional

---

#### Application 4: Product Design

```
minimalist product design, simple forms with rich material quality,
understated yet luxurious, functional while beautiful
```

**Effect**: Sophisticated simplicity

---

### When to Use

✅ **Use tension technique when**:
- Creating sophisticated, nuanced work
- Avoiding one-dimensional results
- Adding depth and complexity
- Professional or artistic projects
- You want to avoid clichés

❌ **Less useful when**:
- Creating straightforward, simple subjects
- Tension would confuse the concept
- One-dimensional is actually desired

### Common Tension Patterns

**Pattern 1: Style + Groundedness**
```
[bold style] but [grounded element]

Examples:
- experimental typography yet legible text
- surreal imagery but recognizable forms
- abstract composition yet balanced structure
```

**Pattern 2: Emotion + Control**
```
[emotional quality] yet [controlled aspect]

Examples:
- passionate expression yet composed posture
- raw emotion but refined execution
- intimate feeling yet professional finish
```

**Pattern 3: Visual + Conceptual**
```
[visual characteristic] with [contrasting depth]

Examples:
- simple visual language with complex meaning
- ornate decoration yet minimalist philosophy
- rough texture but refined concept
```

---

### Advanced Tension Techniques

**Multiple Tension Layers**:
```
portrait: vulnerable expression yet confident posture,
soft lighting but strong shadows, intimate framing with universal theme,
contemporary style yet timeless quality
```
(Multiple tensions create rich complexity)

**Tension in Progression**:
```
starts minimal and controlled, builds to expressive chaos,
resolves in balanced harmony
```
(Narrative tension through progression)

**Cultural Tension**:
```
traditional Japanese aesthetics with contemporary minimalism,
Eastern philosophy meets Western design, ancient wisdom in modern form
```
(Cross-cultural creative tension)

---

## Technique Integration

### Using Multiple Techniques Together

**Most prompts should combine 4-6 techniques for optimal results.**

#### Integration Example 1: Portrait

**Techniques applied**:
1. Medium Definition: "oil painting portrait"
2. Number Emphasis: "1 elderly woman"
3. Color Control: "warm earth tones with burgundy accents"
4. Professional Terminology: "chiaroscuro lighting, impasto texture"
5. Hierarchical Description: Subject → Details → Atmosphere → Technical
6. Tension: "weathered features yet dignified presence"

**Complete Prompt**:
```
oil painting portrait, 1 elderly woman with weathered features yet dignified presence,
warm earth tones with accents of burgundy and olive green,
chiaroscuro lighting from window, impasto texture, visible brushstrokes,
contemplative expression, Renaissance technique, museum-quality detail,
no modern elements --ar 4:5 --stylize 100
```

---

#### Integration Example 2: Product Photography

**Techniques applied**:
1. Medium Definition: "commercial product photography"
2. Number Emphasis: "1 perfume bottle"
3. Negative Exclusion: "no text, no labels, no background clutter"
4. Professional Terminology: "soft key light, f/2.8 aperture"
5. Hierarchical Description: Product → Details → Background → Lighting
6. Color Control: "clear glass with golden liquid, cream background"

**Complete Prompt**:
```
commercial product photography, 1 luxury perfume bottle centered,
geometric glass design, golden liquid inside, minimal composition,
cream gradient background, soft key light from left,
f/2.8 aperture, shallow depth of field, ultra-sharp focus,
no text, no labels, no clutter --ar 4:5 --stylize 30 --style raw
```

---

### Technique Selection Guide

**For Realistic Photography**:
- ✅ Use: Medium Definition, Professional Terminology, Negative Exclusion
- ⚠️ Use carefully: Repetition (can make it too stylized)
- ❌ Skip: Heavy tension (keep it straightforward)

**For Artistic/Stylized Work**:
- ✅ Use: Medium Definition, Repetition Reinforcement, Color Control, Tension
- ⚠️ Use carefully: Professional terminology (don't over-tech)
- ❌ Skip: Excessive negative exclusion (allow artistic freedom)

**For Design/Posters**:
- ✅ Use: Color Control, Negative Exclusion, Hierarchical Description
- ⚠️ Use carefully: Number Emphasis (only for focal elements)
- ❌ Skip: Heavy professional photography terms (unless photo-based)

---

## Quick Reference Summary

| Technique | Core Principle | When to Use | Key Syntax |
|-----------|---------------|-------------|------------|
| 1. Number Emphasis | "1" prevents multiplication | Focused subjects, minimalism | `1 [element]` |
| 2. Repetition Reinforcement | Repetition = higher weight | Style emphasis | Repeat 2-3 times |
| 3. Negative Exclusion | Actively exclude unwanted | Clean designs, precision | `no [element], --no` |
| 4. Medium Definition | Medium = foundation | Always (unless abstract) | Start with medium |
| 5. Color Control | Specific colors = cohesion | Color matters | `[color] with accents of [color]` |
| 6. Professional Terminology | Precise terms = precise control | Technical/professional work | Use domain vocabulary |
| 7. Hierarchical Description | Order = priority | Complex scenes | Subject → Details → Atmosphere |
| 8. Tension Creation | Opposites = depth | Sophisticated work | `[quality] yet [opposite]` |

---

## Technique Mastery Path

**Beginner**: Start with 2-3 techniques
- Medium Definition (always)
- Number Emphasis (for clear subjects)
- Negative Exclusion (for clean results)

**Intermediate**: Add 3-4 more techniques
- Color Control
- Hierarchical Description
- Repetition Reinforcement

**Advanced**: Master all 8 techniques
- Professional Terminology
- Tension Creation
- Seamless integration of all techniques

---

Remember: These techniques are tools, not rules. Use them purposefully to achieve your specific vision, not as a checklist to blindly follow. Understanding why each technique works empowers you to apply them creatively and effectively.
