# Prompt Engineering Essentials Reference

This document contains 5 carefully analyzed cases that demonstrate the underlying logic and core techniques of prompt writing. These are not "templates" to copy, but examples to "learn from" and "understand," helping you master the essence of prompt engineering.

---

## Case 1: Urban Streetwear - The Art of Focus Control

### Original Prompt

```
Streetwear graphic design on a solid black background, 1 close-up cropped face centered,
1 teal ribbed knit beanie pulled down to cover both eyes, 1 small embroidered cursive wordmark
stitched on the beanie, 1 cigarette clenched between the lips with a faint smoke wisp,
1 set of metallic grill teeth visible, moody editorial lighting, subtle vignette,
fine film grain, high-contrast print-ready look, add 1 large brush-script title as
abstract paint strokes beneath the face and 2 lines of tiny clean stamp text centered below
(not readable), premium drop poster composition, flat 2D artwork, no mockup, no watermark,
no border, no readable text, no letters, no words --no mockup --chaos 12 --ar 4:5 --raw --stylize 20
```

### In-Depth Analysis

#### 1. The Philosophy of Using "1"

**❌ Common Misconception**: It's just a quantity word meaning "one"

**✅ True Essence**: **Emphasizes focus and uniqueness**, telling the AI this is the main element and preventing the image from being scattered

Specific Applications:
- `1 close-up cropped face` - Focus on one face, no multiple faces
- `1 teal ribbed knit beanie` - Emphasize this hat as the focal prop
- `1 cigarette` - One cigarette, don't show multiple
- `1 set of metallic grill teeth` - One set of grills, unifying visual elements
- `1 large brush-script title` - One title element, no repeats

**Key Insight**: AI models tend to generate "rich" images, and the number "1" is an **active constraint** against this tendency.

#### 2. Hierarchical Description Structure

This prompt follows a rigorous hierarchical structure:

```
【Subject Layer】face centered (composition core)
    ↓
【Detail Layer 1】beanie
  - Material: ribbed knit
  - Color: teal
  - Decoration: embroidered cursive wordmark
  - Position: pulled down to cover both eyes
    ↓
【Detail Layer 2】cigarette
  - Position: clenched between the lips
  - Dynamic: faint smoke wisp
    ↓
【Detail Layer 3】grill teeth
  - Material: metallic
  - State: visible
    ↓
【Atmosphere Layer】
  - moody editorial lighting
  - subtle vignette
  - fine film grain
    ↓
【Technical Layer】
  - high-contrast
  - print-ready look
  - flat 2D artwork
    ↓
【Negative Layer】(6 negative terms!)
  - no mockup
  - no watermark
  - no border
  - no readable text
  - no letters
  - no words
```

**Key Insight**: From core to periphery, from subject to atmosphere, from creation to exclusion, forming a **complete visual control system**.

#### 3. The Power of Negative Terms

Note that "no mockup" appears **twice**:
1. In the description: "no mockup"
2. In the parameters: `--no mockup`

Adding other negative terms, there are **6 negative instructions** in total.

**Why so many negatives?**
- AI will add many "helpful" elements by default (borders, watermarks, readable text, etc.)
- Street style posters need **pure visual impact**, no extra decoration
- Negative terms are a **necessary means to actively exclude interference**

**Practical Checklist**:
- `no mockup` - No mockup effect
- `no watermark` - No watermark
- `no border` - No border
- `no readable text` - No readable text
- `no letters` - No letters
- `no words` - No words

#### 4. The Intrinsic Logic of Parameters

**`--stylize 20` (low value)**
- **Why low?** Street photography style needs to maintain **realism and detail**
- High stylize will make the image overly artistic, losing the raw street feel
- Low value = fidelity priority

**`--chaos 12` (medium)**
- Provides some creative space, but not too random
- Street style needs some unexpected elements, but overall controllable

**`--raw`**
- Emphasizes photographic realism, no excessive processing
- Suitable for realistic style prompts

**`--ar 4:5`**
- Vertical ratio, golden ratio for posters
- Suitable for portrait subjects

**Key Insight**: Parameter selection should **serve the style positioning**, not be randomly set.

---

## Case 2: Retro 80s - Repetition Reinforcement Strategy

### Original Prompt

```
An Asian woman in a red leather suit with a shotgun and sunglasses on the background
with intense gradation, the top text reads "shot." Retro posters in the 80s style,
kaizu movie posters, animation style in the 70s --ar 2:3 --raw --stylize 50
```

### In-Depth Analysis

#### 1. Style Repetition Reinforcement Method

Observe carefully, the style description includes:
- "Retro posters in the 80s style"
- "kaizu movie posters"
- "animation style in the 70s"

All three descriptions emphasize **the same core: retro style**.

**Why repeat?**
- When AI processes prompts, **repeated concepts are given higher weight**
- Through **strategic repetition**, ensure AI prioritizes this style above all
- Prevents the style from being diluted or overwhelmed by other elements

**Application Tips**:
- Identify core style → Repeat emphasis using 2-3 different expressions
- "80s style" + "movie posters" + "70s animation" = triple reinforcement

#### 2. The Power of Specificity

Compare two descriptions:

**❌ Weak Description**: "a woman with a gun"
- Low information content, AI has too much room for interpretation

**✅ Strong Description**: "An Asian woman in a red leather suit with a shotgun and sunglasses"
- Ethnic characteristic: Asian
- Clothing material + color: red leather suit
- Prop: shotgun (not gun, but shotgun)
- Accessory: sunglasses

**Key Insight**: Every element has **clear modifiers**, leaving no ambiguous space.

#### 3. Background Handling Technique

Note the background description: "on the background with intense gradation"

**Not saying**: "colorful background" or "gradient background"
**But saying**: "intense gradation" (strong gradient)

**Essence**: Use **visual effects** rather than specific objects to describe the background
- Don't say "what's there" (objects)
- Say "how it looks" (effects)

#### 4. Parameter Comparison Understanding

**`--stylize 50`** vs Case 1's `--stylize 20`

**Why higher?**
- Retro style itself is a **highly stylized** art form
- Need to enhance those typical 80s visual characteristics (vibrant colors, exaggerated composition)
- High stylize = style characteristics priority

**`--ar 2:3`**
- Vertical poster ratio
- Classic movie poster format

**Key Insight**: Even for posters, different styles require **different parameter strategies**.

---

## Case 3: Cartoon Sketch - The Mantra of Minimalism

### Original Prompt

```
a simple ink sketch, cartoon-style depiction of a couple of cute child cats.
simple line in black ink with accents of light blue and green.
--ar 9:16 --sref 3153713690 --profile nvhdcvc
```

### In-Depth Analysis

#### 1. The Minimalist Mantra

The word "simple" appears **twice**:
1. "a simple ink sketch"
2. "simple line in black ink"

**Why repeat "simple"?**
- AI naturally tends to **add details and complexity**
- Must use repeated "simple" to **counteract** this tendency
- This is a "mantra-like" forced constraint

**Key Insight**: When you want a minimalist style, saying "simple" once is not enough—you need to **emphasize it multiple times**.

#### 2. Medium Priority Principle

Notice the beginning of the prompt:

**❌ Inefficient Order**: "draw some cute kittens in ink sketch style"
- Content first, medium second

**✅ Efficient Order**: "a simple ink sketch, cartoon-style depiction of..."
- **Define medium first**, then content

**Why medium priority?**
- Medium determines **overall texture and expression**
- First establish the medium, all subsequent descriptions will be interpreted within this framework
- "ink sketch" tells AI: use lines, not blocks; use black and white, not colors (except accent colors)

#### 3. Color Limitation Strategy

Color description: "simple line in black ink with accents of light blue and green"

**Structure Analysis**:
```
Main color: black ink (dominant color)
    +
Accent word: accents of (key phrase!)
    +
Accent colors: light blue and green (limited auxiliary colors)
```

**The Magic of "accents of"**:
- Clearly indicates these colors are only **accents**, not main colors
- Prevents AI from letting auxiliary colors overshadow the main

**Key Insight**: **Strictly limiting colors** maintains style purity.

#### 4. Parameter Innovation

**`--sref 3153713690`**
- Style reference ID, directly referencing a specific visual style

**`--profile nvhdcvc`**
- Profile parameter, may contain specific generation settings

**Essence**: When words can't precisely describe style, directly **reference style ID**.

This is a "hybrid strategy":
- Text description → Basic framework
- sref + profile → Style details

**Key Insight**: Complex style = Text description + Style reference ID

---

## Case 4: Fusion Creature - Layered Concept Definition

### Original Prompt

```
A mythical chimera beast, a fusion creature combining the physical characteristics
of a shark and a dog into one single animal.
--sref <https://s.mj.run/fh_vN3DJYMM> <https://s.mj.run/6RpJaDMNV2E>
```

### In-Depth Analysis

#### 1. Three-Layer Concept Definition Method

This seemingly brief prompt actually uses precise **layered definition**:

```
【Layer 1: Type Definition】
"A mythical chimera beast"
→ Defines the category of existence: this is a mythical creature

【Layer 2: Fusion Logic】
"a fusion creature combining..."
→ Explains how to create: through fusion

【Layer 3: Specific Combination】
"the physical characteristics of a shark and a dog"
→ Specifies component elements: shark + dog

【Layer 4: Unity Emphasis】
"into one single animal"
→ Prevents separation: one creature, not two
```

**Why need "into one single animal"?**
- Prevents AI from generating "a shark and a dog side by side"
- Emphasizes **unity of fusion**

**Key Insight**: Complex concepts require **progressive layered definition**, from abstract to concrete.

#### 2. The Necessity of Visual References

Provided **two image URLs**:
- `https://s.mj.run/fh_vN3DJYMM`
- `https://s.mj.run/6RpJaDMNV2E`

**Why need image references?**
- Words can't fully convey the specific visual effect of "shark + dog fusion"
- Image references provide **specific fusion style** (realistic? cartoon? abstract?)

**Application Scenarios**:
- Abstract concepts (emotions, atmosphere)
- Hybrid creatures/objects
- Unique styles difficult to describe in words

**Key Insight**: For complex or abstract concepts, **text + images** combination is needed for accurate communication.

#### 3. Balance of Brevity and Precision

The entire prompt has only 20+ words (excluding parameters), but immense information:
- Defined type (mythical creature)
- Explained method (fusion)
- Specified elements (shark, dog)
- Emphasized unity (single creature)
- Provided visual references (2 URLs)

**Key Insight**: Not longer is better, but **every word carries key information**.

---

## Case 5: Conceptual Storytelling - The Pinnacle of Multi-Dimensional Narrative

### Original Prompt

```
conceptual visual storytelling about innovation as process, narrative and sequential
composition showing before-during-after transformation, visual metaphor of changing
a process rather than an object, theme "si lo haces igual no es innovación", innovation
as a conscious decision not an accident, designed for individuals with critical mindset,
positioning a high-impact social and technological design agency, clear and provocative
yet close and human tone, emotion of active curiosity, experimental but grounded,
process-driven visuals, contrast between repetition and divergence, subtle disruption
in systems, human-scale technology, no corporate clichés, contemporary design language,
cinematic photography, 35mm lens look, shallow depth of field, selective focus guiding
the sequence, strong focal point with evolving elements across the frame, high dynamic
range lighting, soft natural light mixed with technical accents, realistic textures
with conceptual abstraction, editorial style, high-detail, ultra-sharp subject,
clean background with meaningful negative space, visual tension that invites questioning,
professional art direction, photorealistic with conceptual layers, global contemporary
aesthetic, shot as a cinematic still, f/2.8 aperture look, ISO 100 clarity, --raw
```

### In-Depth Analysis

#### 1. Multi-Layered Narrative Structure

This is the most complex prompt case, using **multi-dimensional layering**:

```
【Concept Layer】(What is it?)
  - conceptual visual storytelling
  - visual metaphor
  - process-driven visuals

【Theme Layer】(What about?)
  - innovation as process
  - innovation as a conscious decision not an accident
  - theme "si lo haces igual no es innovación"
  - changing a process rather than an object

【Audience Layer】(For whom?)
  - designed for individuals with critical mindset
  - positioning a high-impact social and technological design agency

【Emotion Layer】(What feeling?)
  - clear and provocative yet close and human tone
  - emotion of active curiosity
  - experimental but grounded

【Narrative Layer】(How to tell?)
  - narrative and sequential composition
  - before-during-after transformation
  - strong focal point with evolving elements across the frame

【Visual Tension Layer】(What tension?)
  - contrast between repetition and divergence
  - subtle disruption in systems
  - visual tension that invites questioning

【Technical Layer】(How to shoot?)
  - cinematic photography, 35mm lens look
  - f/2.8 aperture look, ISO 100 clarity
  - shallow depth of field, selective focus
  - high dynamic range lighting
  - soft natural light mixed with technical accents

【Exclusion Layer】(What not?)
  - no corporate clichés
```

**Key Insight**: Complex concepts require **multiple dimensions defined simultaneously**, none can be missing.

#### 2. Precision of Professional Terminology

Notice the extensive use of **photography professional terminology**:

**Lens Parameters**:
- "35mm lens look" - Standard lens perspective
- "f/2.8 aperture look" - Large aperture shallow depth of field effect
- "ISO 100 clarity" - Low ISO high clarity

**Photography Techniques**:
- "shallow depth of field" - Shallow DOF
- "selective focus" - Selective focusing
- "high dynamic range lighting" - HDR lighting

**Why use professional terminology?**
- Adjectives ("beautiful light") → Vague, AI can interpret freely
- Professional terms ("f/2.8 aperture look") → Precise, AI knows the specific effect

**Key Insight**: Using **professional domain terminology** can precisely control the image, more effective than adjectives.

#### 3. Creating Contrast and Tension

Notice these **coexisting opposing elements**:

- "clear and provocative **yet** close and human" - Clear and provocative yet intimate and human
- "experimental **but** grounded" - Experimental but grounded
- "contrast between repetition and divergence" - Contrast between repetition and divergence
- "realistic textures with conceptual abstraction" - Realistic textures with conceptual abstraction

**The Role of These Contrasts**:
- Create **visual tension** and **cognitive conflict**
- Give the image depth and complexity
- Avoid single-dimensional flatness

**Formula**:
```
Tension = Balanced coexistence of opposing elements
```

**Key Insight**: Advanced prompts are not unidirectional descriptions, but **creating harmonious contradictions**.

#### 4. Parameter Minimalism Principle

Note: This long prompt only uses **one parameter**: `--raw`

**Why not more parameters?**
- Text description is already detailed and precise enough
- Too many parameters will **interfere** with text description control
- `--raw` only enhances photographic realism, doesn't interfere with others

**Key Insight**: When text description is detailed and precise enough, **parameters should be restrained**.

#### 5. Strategic Use of Negative Terms

Only one negative term: "no corporate clichés"

**Why only one?**
- Other elements are already fully defined through positive descriptions
- "no corporate clichés" is a **key exclusion**, preventing falling into commercial advertising tropes

**Key Insight**: Negative terms should **precisely target** key issues, not cover everything.

---

## Core Writing Principles Summary

### Principle 1: Structured Thinking (Macro to Micro)

```
Simple Scenario:
  Style definition → Subject description → Detail layers → Atmosphere → Parameters

Medium Scenario:
  Style definition → Subject + props → Background effects → Repetition reinforcement → Parameters

Complex Scenario:
  Concept → Theme → Audience → Emotion → Narrative → Visual tension → Technical → Exclusion → Parameters
```

### Principle 2: Language Technique Toolbox

#### A. Number Emphasis Technique
- "1" = Focus/Uniqueness/Prevent scatter
- Application: Add numbers before key elements

#### B. Repetition Reinforcement Technique
- Key words appear 2-3 times = Increase weight
- Application: Core styles, main elements

#### C. Negative Exclusion Technique
- Explicitly saying "don't want" is as important as saying "want"
- Application: Exclude common but unwanted elements

#### D. Medium Definition Technique
- Prioritize defining creation medium (oil painting, sketch, photography, etc.)
- Application: All artistic prompts

#### E. Color Control Technique
- Structure: Main color + accents of + accent colors
- Application: Scenarios requiring precise color control

#### F. Professional Terminology Technique
- Photography: 35mm, f/2.8, ISO 100, shallow depth of field
- Art: chiaroscuro, impasto, tenebrism
- Application: Scenarios requiring precise technical control

### Principle 3: Parameter Selection Decision Tree

#### stylize Value Selection

| Value Range | Effect | Applicable Scenarios |
|-------------|--------|----------------------|
| 0-50 | Maintain realism | Realistic photography, product images, street style |
| 50-100 | Balanced stylization | Retro posters, concept illustrations |
| 100-200 | Strong stylization | Art posters, stylized illustrations |
| 200+ | Extreme artistic | Pure artistic expression |

**Decision Logic**: Higher artistic level of style itself → Higher stylize value

#### chaos Value Selection
- 0-10: Predictable, suitable for commercial use
- 10-20: Moderate creativity, suitable for artistic creation
- 20+: Highly experimental, suitable for exploratory creation

#### raw Usage Scenarios
- ✅ Use: Realistic photography, street style, documentary style
- ❌ Don't use: Highly stylized, abstract art, illustration

#### sref Usage Scenarios
- Unique styles difficult to describe in words
- Need to precisely match a specific visual reference
- Hybrid creatures/abstract concepts

### Principle 4: Advanced Strategies

#### A. Text-Parameter Balance Principle
```
Detailed text + Simple parameters = Precise control (Case 5)
Simple text + Rich parameters = Style reference (Case 3)
```

#### B. Focus Control Pyramid
```
Strong control: 1 + centered + focal point
Medium control: close-up, cropped, prominent
Weak control: visible, showing, featuring
```

#### C. Tension Creation Formula
```
Tension = Coexistence of opposing elements
  - experimental but grounded
  - clear yet human
  - realistic with abstraction
  - repetition and divergence
```

---

## Learning Path Recommendations

### Beginner (Master Basics)
1. Learn to use "1" to emphasize focus
2. Master basic structure: style → subject → details → atmosphere
3. Learn to use negative terms to exclude interference
4. Understand basic roles of stylize and chaos

**Practice**: Imitate Cases 1 and 3, generate simple scenarios

### Intermediate (Apply Techniques)
1. Master repetition reinforcement strategy
2. Learn medium priority and color control
3. Understand parameter-style matching logic
4. Use sref to reference styles

**Practice**: Following Case 2's logic, generate retro styles from different eras

### Advanced (Create Tension)
1. Master multi-layered narrative structure
2. Learn to use professional terminology for precise control
3. Create contrast and visual tension
4. Understand text-parameter balance principle

**Practice**: Try generating conceptual works similar to Case 5

---

## Key Reminders

### ✅ Should Do

1. **Understand intent first**: First understand what the user wants to express, then decide structure
2. **Think in layers**: From concept to details, from subject to atmosphere
3. **Use precise words**: Every word has purpose, avoid vague descriptions
4. **Strategic repetition**: Repeat key elements 2-3 times for reinforcement
5. **Parameters serve style**: Parameters should match style positioning

### ❌ Should Not Do

1. **Don't pile keywords**: Not more is better, needs logic
2. **Don't ignore negatives**: Must explicitly exclude what should be excluded
3. **Don't abuse parameters**: Too many parameters interfere with each other
4. **Don't ignore medium**: Creation medium determines overall texture
5. **Don't be single-dimensional**: Advanced works need multi-dimensional balance

---

## Final Insight

These 5 cases demonstrate not "templates", but **thinking methods**:

1. **Case 1** teaches us: How to create focus through precise control
2. **Case 2** teaches us: How to ensure style through repetition reinforcement
3. **Case 3** teaches us: How to create purity through restraint
4. **Case 4** teaches us: How to define complex concepts through layering
5. **Case 5** teaches us: How to create depth through multiple dimensions

**A true prompt engineer** doesn't memorize these cases, but **internalizes these principles** and applies them flexibly when facing any new scenario.

Remember: **Don't copy templates, understand the logic.**
