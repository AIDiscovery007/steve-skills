# Output Mode Templates

This document defines standard format templates for three output modes.

---

## Quick Mode

### Use Cases
- User is experienced and familiar with prompt writing
- Quick iteration, only need core content
- Time-sensitive, need rapid generation

### Output Format

```markdown
# Generated Prompt

[Complete prompt in code block]

**Key Parameters**: --stylize [value] ([brief reason]), --ar [ratio] ([usage])

**Adjustment Tip**: [1-sentence core suggestion]
```

### Output Length
Approximately 150-200 words

### Example

```
# Generated Prompt

watercolor portrait, 1 young woman with flowing white hair,
elegant pose, soft pastel colors, dreamy atmosphere, delicate
brushstrokes, ethereal beauty --ar 2:3 --stylize 120 --niji 6

**Key Parameters**: --stylize 120 (watercolor style needs higher artistic interpretation), --niji 6 (anime/illustration mode)

**Adjustment Tip**: For more dreamlike feel increase stylize to 150, for more realistic reduce to 80
```

---

## Standard Mode - Default

### Use Cases
- Most regular usage scenarios
- Need to understand generation logic but not full tutorial
- Balance between detail and efficiency

### Output Format

```markdown
# Generated Prompt

## Complete Prompt
[Complete prompt]

## Core Approach
[3-5 bullet points of core method explanation, each 1 line]

## Parameter Rationale
- `--parameter [value]`: [Brief reason]
[List 3-5 key parameters]

## Adjustment Options
- **[Issue type]** → [Adjustment suggestion]
[2-3 common adjustment directions]
```

### Output Length
Approximately 300-400 words

### Example

```
# Generated Prompt

## Complete Prompt

cinematic photography, 1 cyberpunk street scene at night,
neon-lit alleyways with electric blue and hot pink signs,
wet reflective pavement, atmospheric fog, Blade Runner aesthetic,
moody noir atmosphere, 35mm film grain, high contrast lighting
--ar 16:9 --stylize 60 --v 6

## Core Approach
- Defined cinematic photography medium first for filmic quality
- Used "1" to emphasize singular focused scene
- Repeated cyberpunk/noir aesthetic 2-3 times for style reinforcement
- Specified precise color palette (electric blue, hot pink) instead of "colorful"
- Applied professional photography terminology (35mm, film grain, high contrast)

## Parameter Rationale
- `--stylize 60`: Balanced artistic interpretation - maintains realism while adding cinematic mood
- `--ar 16:9`: Cinematic widescreen ratio for narrative feel
- `--v 6`: Version 6 for better photographic realism and color accuracy

## Adjustment Options
- **Too dark/moody** → Reduce contrast, add "ambient lighting" or "soft glow"
- **Not cyberpunk enough** → Increase neon elements, add "holographic displays" or "digital rain"
- **Too stylized** → Lower --stylize to 30-40, add --style raw for photorealism
```

---

## Detailed Mode

### Use Cases
- Learning prompt writing principles
- Complex scenarios requiring deep understanding
- First-time use or need complete guidance

### Output Format

```markdown
# Generated Prompt

## Complete Prompt
[Complete prompt]

## Explanation

### Core Approach
[Detailed strategy explanation, 2-3 paragraphs]

### Key Techniques Applied
- **[Technique name]**: [How applied, why used]
[4-6 technique explanations]

### Parameter Selection Rationale
- `--parameter [value]`: [Detailed reasoning process]
[Complete explanation of all parameters]

## Usage Tips

### If Results Aren't Ideal
- **[Issue type]** → [Detailed adjustment strategy]
[4-5 common problem solutions]

### Optional Variants
[2-3 variant directions with detailed explanations]

---

Please let me know how it works, and I can optimize based on feedback!
```

### Output Length
Approximately 600-800 words (current full format)

### Example

```
# Generated Prompt

## Complete Prompt

oil painting portrait, 1 elderly woman with weathered features,
warm golden hour lighting from window, Renaissance chiaroscuro technique,
rich earth tones with accents of burgundy and olive green,
contemplative expression, soft brushstrokes, impasto texture,
classical composition, intimate atmosphere, museum-quality detail
--ar 4:5 --stylize 100 --v 6

## Explanation

### Core Approach

This prompt uses a classical art photography approach combined with Renaissance painting techniques. The strategy is to first establish the medium (oil painting) to set the texture foundation, then layer specific technical details that reference historical art movements. By invoking "Renaissance chiaroscuro" and "impasto texture," we're giving the AI precise stylistic anchors rather than vague terms like "nice painting" or "dramatic."

The hierarchical description moves from subject (elderly woman) → lighting quality (golden hour from window) → technical execution (chiaroscuro, impasto) → color system (earth tones + specific accents) → atmosphere (contemplative, intimate). This layered approach ensures the AI prioritizes elements in the correct order.

### Key Techniques Applied

- **Medium Definition Technique**: Started with "oil painting portrait" to immediately establish the creation medium and texture framework. All subsequent descriptions operate within this medium's constraints.

- **Number Emphasis Technique**: Used "1 elderly woman" to emphasize a single subject and prevent the AI from generating multiple figures or scattered composition.

- **Hierarchical Description Technique**: Structured the prompt in layers: subject → lighting → technique → colors → atmosphere → technical details. This creates clear priority for the AI to process.

- **Professional Terminology Technique**: Used art history terms like "chiaroscuro" (dramatic light-dark contrast), "impasto" (thick paint texture), and "golden hour lighting" instead of generic terms like "nice light" or "thick paint."

- **Color Control Technique**: Specified "rich earth tones with accents of burgundy and olive green" instead of "warm colors" - this maintains color palette purity and prevents random color additions.

- **Tension Creation Technique**: Balanced "weathered features" with "museum-quality detail" to create depth - acknowledging age/imperfection while maintaining technical excellence.

### Parameter Selection Rationale

- `--stylize 100`: Oil painting is already a stylized medium, so we use medium-high stylize to enhance artistic interpretation while maintaining recognizable form. Too low (0-50) would make it look like a photo of an oil painting; too high (150+) would become abstract.

- `--ar 4:5`: Portrait orientation (slightly taller than wide) is traditional for portrait paintings and creates an intimate, classical composition feel. This ratio references historical portrait standards.

- `--v 6`: Version 6 provides superior handling of artistic mediums and better color accuracy for the specified earth tone palette. It also better understands art history references like "chiaroscuro."

- **No --raw used**: The --raw parameter would push toward photographic realism, which conflicts with the oil painting medium. We want artistic interpretation here, not realism.

- **No --chaos used**: Classical portraiture requires predictable, stable composition. Chaos would introduce unwanted experimental elements that conflict with the "museum-quality" and "classical composition" intent.

## Usage Tips

### If Results Aren't Ideal

- **Too abstract/unrecognizable** → Lower --stylize to 70-80, add "realistic proportions" to the prompt, or add descriptive details about facial features.

- **Doesn't look like oil painting** → Add more medium-specific terms: "visible brushstrokes," "canvas texture," "layered paint," "varnish finish." Consider adding artist references like "Rembrandt style" or "Vermeer lighting."

- **Colors are off** → Be more specific with the color palette. Replace "earth tones" with exact colors: "burnt sienna, raw umber, ochre yellow" and specify the exact accent colors.

- **Lighting is wrong** → Add more specific lighting directions: "soft window light from left side at 45-degree angle" or "single light source creating dramatic shadows."

- **Too modern/AI-looking** → Add --style raw cautiously (test at lower weights), increase references to classical techniques, add "traditional oil painting technique" or "16th century portrait style."

### Optional Variants

- **Younger subject**: Change "elderly woman with weathered features" to "young woman with porcelain skin" - adjust lighting from golden hour to "soft diffused light" for smoother appearance.

- **Different art period**: Replace "Renaissance chiaroscuro" with "Impressionist dappled light" or "Baroque dramatic lighting" - each references different historical techniques.

- **More contemporary**: Add "contemporary realism" or "modern portrait painting," remove historical references, consider adding "hyperrealistic detail" for 21st-century portrait style.

---

Please let me know how it works, and I can optimize based on feedback!
```

---

## Image Reverse Engineering Output Template

### Output Format

```markdown
# Image Analysis & Prompt Generation

## Visual Analysis Summary
[3-5 bullet points of key visual characteristics]

---

## Generated Prompt

### Midjourney Version
[Complete prompt]

### (Optional) Stable Diffusion Version
**Positive**: [Positive prompt]
**Negative**: [Negative prompt]
**Settings**: [Parameters]

---

## Key Elements Breakdown
- **Medium & Style**: [Explanation]
- **Subject & Composition**: [Explanation]
- **Color Palette**: [Explanation]
- **Lighting & Atmosphere**: [Explanation]
- **Technical Characteristics**: [Explanation]

## Parameter Recommendations
[Parameter selection reasoning]

---

## Adjustment Options

If you want to:
- **Fully reproduce this style** → [Suggestion]
- **Keep style, change subject** → [Suggestion]
- **Keep subject, change style** → [Suggestion]

---

Need me to generate variants or further optimize?
```

### Example

```
# Image Analysis & Prompt Generation

## Visual Analysis Summary
- Main subject: Low-angle view of neon-lit cyberpunk buildings in rainy urban environment
- Style: Cinematic photography with strong Blade Runner aesthetic influence
- Color palette: Dominant electric blue and hot pink neon against dark cyan-tinted shadows
- Lighting: Multiple neon light sources with atmospheric haze and wet surface reflections
- Atmosphere: Mysterious, dystopian noir with futuristic tension

---

## Generated Prompt

### Midjourney Version

cinematic cyberpunk cityscape, low-angle night photography,
towering neon-lit skyscrapers, electric blue and hot pink neon signs,
wet reflective streets, atmospheric haze, rain-soaked pavement,
Blade Runner aesthetic, noir atmosphere, 35mm film photography,
high contrast, moody lighting, dystopian urban environment
--ar 2:3 --stylize 75 --v 6

---

## Key Elements Breakdown
- **Medium & Style**: Cinematic photography with cyberpunk/noir film aesthetic - not illustration or 3D render
- **Subject & Composition**: Low-angle perspective looking up at buildings creates sense of scale and immersion; vertical composition emphasizes building height
- **Color Palette**: Highly controlled palette with electric blue (primary neon), hot pink (accent neon), and dark cyan-tinted shadows - avoiding generic "colorful"
- **Lighting & Atmosphere**: Multiple neon light sources creating complex reflections on wet surfaces; atmospheric haze adds depth and mystery
- **Technical Characteristics**: Film photography grain, high contrast between bright neons and dark shadows, reflective wet surfaces doubling the light sources

## Parameter Recommendations
- `--stylize 75`: Medium-high to maintain cinematic mood while preserving photographic realism
- `--ar 2:3`: Vertical ratio emphasizes towering buildings and matches the low-angle perspective
- `--v 6`: Better handling of complex lighting scenarios and photographic realism
- Consider `--style raw` if output is too artistic/painterly - this would push toward pure photography

---

## Adjustment Options

If you want to:
- **Fully reproduce this style** → Use the prompt as-is; consider adding `--sref [original image URL]` for closer matching
- **Keep style, change subject** → Replace "towering skyscrapers" with other subjects like "narrow alleyway," "market stalls," or "abandoned factory"
- **Keep subject, change style** → Remove noir/Blade Runner references, adjust color palette (e.g., "warm amber and purple" for different mood), modify --stylize

---

Need me to generate variants or further optimize?
```

---

## Output Mode Selection Logic

### When to Ask User (Phase 1)

```
**Output Detail Level** (optional, defaults to Standard):
- Quick: Just the prompt and key points
- Standard: Balanced explanation (recommended)
- Detailed: Complete principles and learning content
```

### Smart Detection (if user doesn't explicitly choose)

**Trigger Quick Mode** if user mentions:
- "fast," "quick," "brief," "just the prompt," "no explanation"

**Trigger Detailed Mode** if user mentions:
- "detailed," "learn," "explain," "teach me," "how does it work," "principles"

**Trigger Standard Mode** (default):
- First-time users (recommend Standard)
- No specific indication
- Any ambiguous cases

### Context-Based Override

- **User is iterating rapidly** (3+ prompts in conversation) → Suggest Quick mode
- **User asks "why" questions** → Switch to Detailed mode
- **User gives feedback like "don't need explanation"** → Switch to Quick mode
- **User is a beginner** (asks basic questions) → Keep Standard or Detailed mode
