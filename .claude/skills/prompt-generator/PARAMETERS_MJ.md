# Midjourney Complete Parameter Reference

Complete guide to Midjourney v6/v7 parameters, including version selection, creative controls, style references, and technical settings.

---

## Parameter Categories Overview

```
Version Control    → --v, --niji
Style Control      → --style, --stylize
Creative Control   → --chaos, --weird
Reference System   → --sref, --cref, --cw
Personalization    → --personalize, --p
Technical Settings → --ar, --q, --tile, --video, --no
```

---

## Version Parameters

### --v (Version)

**Purpose**: Select Midjourney model version

**Syntax**: `--v [6|7]`

**Available Versions**:
- `--v 6`: Version 6 (current stable, recommended for most uses)
- `--v 7`: Version 7 (latest, experimental features)

**Version 6 vs Version 7 Comparison**:

| Aspect | Version 6 | Version 7 |
|--------|-----------|-----------|
| Photorealism | Excellent | Enhanced |
| Color accuracy | High | Higher |
| Text rendering | Good | Improved |
| Prompt following | Strong | Stronger |
| Artistic interpretation | Balanced | More nuanced |
| Best for | General use, reliable results | Latest features, experimentation |

**When to Use**:
- `--v 6`: Most production work, reliable results, proven quality
- `--v 7`: Experimenting with latest features, cutting-edge results

**Example**:
```
cinematic portrait, dramatic lighting --v 6
abstract landscape, surreal colors --v 7
```

---

### --niji (Niji Mode)

**Purpose**: Specialized model for anime/manga/illustration styles

**Syntax**: `--niji [6]`

**Current Version**: `--niji 6`

**Characteristics**:
- Optimized for anime and manga aesthetics
- Better understanding of Japanese art styles
- Enhanced character design capabilities
- Vibrant color handling
- Stylized illustration rendering

**When to Use**:
- Anime or manga-style artwork
- Character design and illustration
- Japanese aesthetic references
- Stylized portraits with anime influence
- Vibrant, expressive illustrations

**Comparison with Standard Model**:

| Aspect | Standard Model (--v 6) | Niji Model (--niji 6) |
|--------|------------------------|----------------------|
| Best for | Realistic, photography, general art | Anime, manga, illustration |
| Color style | Natural, realistic | Vibrant, stylized |
| Character design | Realistic proportions | Anime proportions, expressive |
| Background style | Photographic/realistic | Stylized, artistic |

**Example**:
```
anime portrait, 1 girl with blue hair, magical girl outfit --niji 6 --ar 2:3
manga style illustration, action scene, dynamic pose --niji 6
```

---

## Style Parameters

### --style

**Purpose**: Apply style variations within a model version

**Syntax**: `--style [raw|expressive|scenic|cute]`

**Available Options**:

#### --style raw
**Effect**: Reduces default Midjourney aestheticization, produces more photographic/literal results

**When to Use**:
- Realistic photography
- Documentary style
- Product photography
- When you want literal interpretation
- Minimal artistic interpretation

**Example**:
```
street photography, candid moment --style raw --stylize 20
product shot, white background --style raw --stylize 0
```

#### --style expressive (--niji 6 only)
**Effect**: Increases expressiveness and emotional intensity in anime/illustration styles

**When to Use**:
- Dramatic anime scenes
- Emotional character moments
- Expressive illustrations
- When you want heightened artistic flair

**Example**:
```
anime battle scene, intense emotion --niji 6 --style expressive
```

#### --style scenic (--niji 6 only)
**Effect**: Emphasizes background and environmental details in anime style

**When to Use**:
- Landscape-focused anime art
- Environmental storytelling
- Background art
- Studio Ghibli-like scenes

**Example**:
```
anime fantasy landscape, detailed environment --niji 6 --style scenic
```

#### --style cute (--niji 6 only)
**Effect**: Emphasizes kawaii/cute aesthetic

**When to Use**:
- Chibi characters
- Cute character designs
- Kawaii aesthetic
- Playful, adorable illustrations

**Example**:
```
chibi character, adorable expression --niji 6 --style cute
```

---

### --stylize (or -s)

**Purpose**: Control how much artistic interpretation Midjourney applies

**Syntax**: `--stylize [0-1000]` or `-s [0-1000]`

**Range**: 0 (minimal interpretation) to 1000 (maximum artistic interpretation)

**Default Value**: 100

**Decision Formula**: Artistic level of desired style = stylize value

**Detailed Value Guide**:

| Range | Effect | Visual Characteristics | Best For | Examples |
|-------|--------|------------------------|----------|----------|
| 0-20 | Minimal interpretation | Very literal, photographic, almost no artistic flair | Product shots, technical diagrams, literal documentation | News photos, catalog images |
| 20-50 | Low artistic | Maintains realism, slight enhancement | Realistic photography, portraits, street style | Documentary, editorial photos |
| 50-80 | Balanced low | Natural but polished | Professional photography, commercial work | Marketing materials, lifestyle photos |
| 80-120 | Balanced medium | Moderate stylization, artistic but recognizable | Art photography, posters, concept illustrations | Magazine covers, album art |
| 120-180 | High artistic | Strong stylization, clearly artistic interpretation | Artistic posters, stylized illustrations | Gallery prints, art exhibitions |
| 180-300 | Very high artistic | Heavy artistic interpretation, abstract elements | Experimental art, conceptual works | Contemporary art, installations |
| 300-1000 | Extreme artistic | Maximum artistic freedom, may be abstract/surreal | Pure artistic expression, avant-garde | Abstract art, experimental projects |

**Selection Logic by Style**:
```
【Realistic Photography】
  - Documentary/journalistic → 0-30
  - Professional portraits → 30-60
  - Art photography → 60-100

【Illustration/Art】
  - Technical illustration → 20-40
  - Editorial illustration → 80-120
  - Artistic/gallery work → 120-200
  - Abstract/experimental → 200+

【Posters/Design】
  - Minimalist design → 40-70
  - Retro posters → 60-100
  - Artistic posters → 100-150
  - Psychedelic/experimental → 150+

【3D Render】
  - Product visualization → 20-50
  - Architectural visualization → 40-80
  - Artistic 3D → 80-150
  - Surreal 3D → 150+
```

**Combining with Other Parameters**:
- `--stylize 20 --style raw`: Maximum photographic realism
- `--stylize 150 --niji 6`: Highly artistic anime style
- `--stylize 80 --v 6`: Balanced artistic interpretation

**Example**:
```
portrait photography --stylize 30 --style raw
retro poster design --stylize 90 --ar 2:3
abstract art --stylize 250 --chaos 30
```

---

## Creative Control Parameters

### --weird (or -w)

**Purpose**: Add unconventional, quirky, and experimental aesthetics

**Syntax**: `--weird [0-3000]` or `-w [0-3000]`

**Range**: 0 (normal) to 3000 (maximum weirdness)

**Default**: 0 (off)

**What It Does**:
- Introduces unconventional compositions
- Creates unexpected color combinations
- Generates quirky, experimental aesthetics
- Breaks conventional visual patterns
- Adds surreal or unusual elements

**Value Range Guide**:

| Range | Effect | Visual Impact | Use Cases |
|-------|--------|---------------|-----------|
| 0 | No weird | Normal, conventional aesthetics | Standard work, conventional styles |
| 1-500 | Subtle quirky | Slightly unconventional, mildly experimental | Adding subtle uniqueness, fresh perspective |
| 500-1000 | Moderately weird | Noticeably unconventional, creative twists | Creative projects, unique branding |
| 1000-1500 | Weird | Clearly experimental, breaks patterns | Artistic exploration, standout designs |
| 1500-2000 | Very weird | Highly experimental, surreal elements | Avant-garde art, provocative visuals |
| 2000-3000 | Extremely weird | Maximum unconventionality, unpredictable | Pure experimentation, boundary-pushing |

**When to Use --weird**:
- ✅ Breaking creative blocks (try --weird 800-1200)
- ✅ Experimental art projects
- ✅ Unique brand identity (--weird 300-700)
- ✅ Surreal conceptual work (--weird 1500+)
- ✅ Seeking unexpected inspiration

**When NOT to Use --weird**:
- ❌ Professional client work requiring conventional aesthetics
- ❌ Product photography
- ❌ Traditional portraits
- ❌ When you need predictable, conventional results

**Combining with --chaos**:
- `--weird 1000 --chaos 20`: Weird but somewhat predictable
- `--weird 1500 --chaos 50`: Maximum experimentation and variation
- `--weird 500 --chaos 0`: Subtle quirkiness, consistent results

**Example**:
```
portrait --weird 1200 --stylize 100
landscape --weird 800 --v 6
abstract composition --weird 2500 --chaos 40
```

---

### --chaos (or -c)

**Purpose**: Control variation and unpredictability in results

**Syntax**: `--chaos [0-100]` or `-c [0-100]`

**Range**: 0 (very predictable) to 100 (highly varied)

**Default**: 0

**Decision Formula**: Creative exploration need = chaos value

**Value Range Guide**:

| Range | Effect | Applicable Scenarios | Results Consistency |
|-------|--------|----------------------|---------------------|
| 0-10 | High predictability | Commercial use, product images, consistency needed | Very similar results across generations |
| 10-25 | Moderate creativity | Artistic creation, poster design, controlled variation | Noticeable but controlled variation |
| 25-50 | High creativity | Exploratory creation, seeking options, brainstorming | Significant variation, diverse interpretations |
| 50-100 | Extreme experimentation | Maximum exploration, inspiration seeking, wild experimentation | Highly unpredictable, wildly different results |

**When to Use Different Chaos Values**:

**Low Chaos (0-15)**:
- Product photography requiring consistency
- Brand assets needing uniformity
- When you have a specific vision
- Series of images that should match
- Professional client work

**Medium Chaos (15-35)**:
- Creative exploration with some control
- Poster design with variation options
- Artistic projects with flexibility
- When you want options but within a range

**High Chaos (35-100)**:
- Breaking creative blocks
- Seeking unexpected inspiration
- Experimental art projects
- Exploring possibilities
- When you want maximum variety

**Example**:
```
product photography --chaos 5 --stylize 20
retro poster --chaos 20 --stylize 80
experimental art --chaos 60 --weird 1500
```

---

## Reference System Parameters

### --sref (Style Reference)

**Purpose**: Use reference images to guide the overall style and aesthetic

**Syntax**: `--sref [URL]` or `--sref [URL1] [URL2] [URL3]`

**What It Does**:
- References the overall visual style of an image
- Transfers color palette, texture, and artistic approach
- Does NOT copy the subject or composition
- Can use multiple references simultaneously

**When to Use**:
- Unique styles difficult to describe in words
- Consistent style across multiple generations
- Matching a specific visual reference
- Abstract concepts or hybrid styles
- Want to reproduce an existing work's aesthetic

**How to Use**:
1. Upload reference image to Discord/web
2. Copy image URL
3. Add `--sref [URL]` to prompt

**Multiple Style References**:
```
[prompt] --sref [URL1] [URL2] [URL3]
```
Midjourney will blend styles from all references

**Example**:
```
portrait of a woman --sref https://example.com/style-reference.jpg
landscape painting --sref https://url1.jpg https://url2.jpg
```

**Combining with Other Parameters**:
- `--sref [URL] --stylize 50`: Moderate interpretation of reference style
- `--sref [URL] --stylize 150`: Strong artistic interpretation of reference

---

### --cref (Character Reference)

**Purpose**: Maintain character consistency across multiple generations

**Syntax**: `--cref [URL]`

**NEW FEATURE** (v6+)

**What It Does**:
- Preserves character facial features across generations
- Maintains character identity in different scenes/poses
- Allows consistent character storytelling
- Essential for character design series

**How It Works**:
- Focuses on facial features, hairstyle, and character identity
- Does NOT preserve clothing by default (use --cw for that)
- Works best with clear, front-facing character images
- Can combine with --cw for more complete preservation

**When to Use**:
- Character design series
- Storyboarding with consistent characters
- Multiple scenes with same character
- Character in different situations/outfits
- Brand mascot development

**Best Practices**:
- Use clear reference images (good lighting, visible face)
- Front-facing or 3/4 view works best
- High-quality reference images produce better results
- Can use multiple --cref URLs for different character aspects

**Example**:
```
character walking in park --cref https://example.com/character.jpg
same character, different outfit --cref https://example.com/character.jpg
```

---

### --cw (Character Weight)

**Purpose**: Control how much of the character reference to preserve

**Syntax**: `--cw [0-100]`

**Range**: 0 (face/hair only) to 100 (complete preservation including clothing)

**Default**: 100

**NEW FEATURE** (works with --cref)

**Value Guide**:

| Value | What Gets Preserved | Use Cases |
|-------|---------------------|-----------|
| 0 | Face and hairstyle only | Same character, different outfits/clothing |
| 25 | Face, hair, some clothing elements | Variation in outfits but maintain some costume elements |
| 50 | Face, hair, general clothing style | Moderate outfit consistency |
| 75 | Face, hair, most clothing details | Strong outfit similarity |
| 100 | Everything - face, hair, clothing, accessories | Exact character replication including outfit |

**When to Use Different Values**:

**Low Weight (0-30)**:
- Same character in different outfits
- Fashion changes across scenes
- Character outfit variations
- Want to preserve identity, not clothing

**Medium Weight (30-70)**:
- Partial outfit consistency
- Similar but not identical clothing
- Balanced character/costume preservation
- Style variations

**High Weight (70-100)**:
- Complete character replication
- Consistent character across series
- Same outfit across scenes
- Brand mascot consistency

**Example**:
```
character at beach --cref https://character.jpg --cw 0
(preserves face/hair, different beach outfit)

character series --cref https://character.jpg --cw 100
(preserves everything including original outfit)

character variations --cref https://character.jpg --cw 50
(preserves character, allows outfit variation)
```

**Combining --cref and --cw**:
```
storyboard scene 1: hero in office --cref [URL] --cw 0
storyboard scene 2: hero in gym --cref [URL] --cw 0
storyboard scene 3: hero in suit --cref [URL] --cw 100
```

---

## Personalization Parameters

### --personalize (or -p)

**Purpose**: Apply your personal aesthetic preferences learned from your rankings

**Syntax**: `--personalize` or `-p`

**What It Does**:
- Uses your historical image rankings to understand your aesthetic
- Applies your learned preferences to new generations
- Creates results more aligned with your taste
- Builds a personal style profile over time

**Requirements**:
- Must have ranked images using Midjourney ranking system
- More rankings = better personalization
- Personal aesthetic profile improves over time

**When to Use**:
- Creating art aligned with your personal taste
- Consistent style matching your aesthetic preferences
- Personal projects
- When you want "your style" applied

**When NOT to Use**:
- Client work (their taste, not yours)
- Objective/neutral results
- Experimenting outside your comfort zone
- Generic/universal aesthetics

**Example**:
```
portrait --personalize --stylize 100
landscape painting --p -s 120
```

---

### --p [code]

**Purpose**: Use a specific personalization code (yours or shared)

**Syntax**: `--p [code]`

**What It Does**:
- Applies a specific aesthetic profile by code
- Allows using others' personalization profiles
- Share your aesthetic with collaborators
- Switch between different aesthetic modes

**How to Get Codes**:
- Generate your code via Midjourney settings
- Others can share their codes with you
- Each code represents a specific aesthetic profile

**Use Cases**:
- Team collaboration with shared aesthetic
- Applying a specific artistic direction
- Using curated aesthetic profiles
- Switching between different style modes

**Example**:
```
portrait --p abc123xyz --stylize 100
landscape --p code789 -s 80
```

---

## Technical Parameters

### --ar (Aspect Ratio)

**Purpose**: Set the width:height ratio of generated image

**Syntax**: `--ar [width]:[height]`

**Common Ratios and Use Cases**:

| Ratio | Orientation | Best For | Examples |
|-------|-------------|----------|----------|
| 1:1 | Square | Social media posts, avatars, Instagram, icons | Profile pictures, Instagram posts |
| 4:5 | Portrait | Instagram portrait, vertical posters | Instagram portraits, Pinterest pins |
| 2:3 | Portrait | Traditional portrait, phone wallpaper, book covers | Phone wallpapers, magazine covers |
| 9:16 | Tall portrait | Phone screens, TikTok, Instagram Stories | Vertical video thumbnails, Stories |
| 16:9 | Landscape | Desktop wallpapers, YouTube thumbnails, cinematic | Widescreen displays, video content |
| 21:9 | Ultra-wide | Cinematic feel, panoramic, ultrawide monitors | Movie posters, panoramic views |
| 3:2 | Landscape | Traditional photography, DSLR standard | Classic photography prints |

**Specialty Ratios**:
- `--ar 4:3`: Classic photography, retro feel, presentations
- `--ar 3:4`: Portrait photography, traditional print
- `--ar 5:4`: Medium format photography feel
- Custom ratios: Any ratio up to 2:1 or 1:2 supported

**Example**:
```
portrait photography --ar 2:3
cinematic landscape --ar 21:9
Instagram post --ar 4:5
desktop wallpaper --ar 16:9
```

---

### --q (Quality)

**Purpose**: Control rendering quality/detail level

**Syntax**: `--q [0.25|0.5|1|2]`

**Options**:
- `--q 0.25`: Fastest, lowest detail (quick drafts)
- `--q 0.5`: Fast, reduced detail (iterations)
- `--q 1`: Standard quality (default, recommended)
- `--q 2`: High quality, more detail (final renders)

**When to Use**:
- `--q 0.25` or `--q 0.5`: Rapid iteration, testing concepts, drafts
- `--q 1`: Most production work (default, good balance)
- `--q 2`: Final high-quality renders, detailed work

**Note**: Higher quality uses more GPU minutes

**Example**:
```
concept draft --q 0.5
final render --q 2 --stylize 100
```

---

### --tile

**Purpose**: Generate seamlessly tiling/repeating patterns

**Syntax**: `--tile`

**What It Does**:
- Creates images that seamlessly repeat when tiled
- Perfect for patterns, textures, backgrounds
- Edges match perfectly for infinite tiling

**When to Use**:
- Fabric patterns
- Wallpaper designs
- Texture maps for 3D
- Background patterns
- Surface designs

**Example**:
```
floral pattern --tile --ar 1:1
geometric texture --tile --stylize 80
```

---

### --video

**Purpose**: Generate a video of the image generation process

**Syntax**: `--video`

**What It Does**:
- Creates short video showing generation progress
- Useful for process documentation
- Behind-the-scenes content
- Educational purposes

**Note**: Request video using reaction emoji after generation

**Example**:
```
portrait painting --video --stylize 120
```

---

### --no

**Purpose**: Exclude specific elements from generation (negative prompting)

**Syntax**: `--no [element1,element2,element3]`

**What It Does**:
- Tells Midjourney what NOT to include
- More reliable than "no [element]" in the prompt
- Can exclude multiple elements

**Common Exclusions**:
- `--no people`: No human figures
- `--no text`: No text or words
- `--no watermark`: No watermarks
- `--no hands`: No hands (often problematic)
- `--no background`: Minimize background elements

**Example**:
```
landscape --no people,buildings,text
product shot --no background,shadows
portrait --no hands --ar 2:3
```

**Note**: Also use negative terms in prompt text for emphasis:
```
clean design, no watermark, no border, no text --no watermark,border,text
```

---

## Quick Decision Guide

Comprehensive parameter selection for common scenarios:

### Realistic Photography

```
**Documentary/Street Photography**:
--v 6 --style raw --stylize 20-40 --ar 3:2 or 16:9 --q 1

**Professional Portrait**:
--v 6 --style raw --stylize 30-60 --ar 2:3 or 4:5 --q 1-2

**Product Photography**:
--v 6 --style raw --stylize 0-30 --ar 1:1 --q 2 --no background,shadows

**Cinematic Photography**:
--v 6 --stylize 60-100 --ar 16:9 or 21:9 --q 2
```

### Illustration & Art

```
**Anime/Manga Style**:
--niji 6 --stylize 100-150 --ar 2:3 or 4:5

**Anime with Environment Focus**:
--niji 6 --style scenic --stylize 120 --ar 16:9

**Cute/Chibi Characters**:
--niji 6 --style cute --stylize 100 --ar 1:1

**Art Poster/Illustration**:
--v 6 --stylize 100-180 --ar 2:3 --q 2

**Abstract/Experimental Art**:
--v 6 --stylize 200-300 --chaos 30-50 --weird 1500-2500
```

### Design & Posters

```
**Minimalist Design**:
--v 6 --stylize 40-70 --ar 2:3 or 4:5 --no clutter,complexity

**Retro/Vintage Poster**:
--v 6 --stylize 80-120 --chaos 10-20 --ar 2:3

**Modern Graphic Design**:
--v 6 --stylize 60-100 --ar 1:1 or 4:5 --q 2

**Pattern/Texture Design**:
--v 6 --stylize 80 --tile --ar 1:1
```

### Character Design

```
**Character Series (Consistent Character)**:
--cref [URL] --cw 0 (for outfit variations)
--cref [URL] --cw 100 (for exact replication)
--niji 6 --ar 2:3

**Character Exploration (Variations)**:
--chaos 20-40 --stylize 100-150 --niji 6 --ar 2:3

**Realistic Character**:
--v 6 --style raw --stylize 50-80 --ar 2:3
```

### Experimental/Creative

```
**Breaking Creative Blocks**:
--weird 800-1500 --chaos 30-50 --stylize 100-180

**Maximum Experimentation**:
--weird 2000-3000 --chaos 60-100 --stylize 200+

**Surreal Art**:
--weird 1500-2500 --stylize 150-250 --ar 1:1 or 4:5

**Unique Brand Identity**:
--weird 300-700 --stylize 80-120 --personalize
```

---

## Parameter Combination Best Practices

### Complementary Combinations

**Photographic Realism Maximum**:
```
--v 6 --style raw --stylize 0-20 --chaos 0 --q 2
```

**Artistic Expression Maximum**:
```
--v 6 --stylize 200-300 --chaos 40 --weird 2000
```

**Controlled Creativity**:
```
--v 6 --stylize 80-120 --chaos 15-25 --q 1-2
```

**Consistent Character Series**:
```
--cref [URL] --cw 0 --niji 6 --chaos 10 --ar 2:3
```

### Conflicting Combinations (Avoid)

❌ **Don't combine**:
- `--style raw` + high `--stylize` (contradictory intentions)
- `--chaos 0` + `--weird 2000` (defeats purpose of weird)
- `--niji 6` + `--style raw` (niji is stylized by nature)
- `--cref` without appropriate subject in prompt

---

## Advanced Tips

### Iteration Strategy

1. **Start broad**: Use moderate parameters to explore
   ```
   [prompt] --v 6 --stylize 80 --ar 2:3
   ```

2. **Refine direction**: Adjust based on initial results
   - Too artistic? → Lower --stylize, add --style raw
   - Too conventional? → Increase --weird, --stylize
   - Need variation? → Increase --chaos

3. **Final polish**: Optimize for final output
   ```
   [refined prompt] --q 2 --stylize [optimal value] --ar [final ratio]
   ```

### Parameter Testing

Test parameters systematically:
```
Same prompt with --stylize 50, 100, 150, 200
Same prompt with --weird 0, 500, 1000, 2000
Same prompt with --chaos 0, 20, 50, 80
```

Track which values work best for your style.

---

## Version History & Updates

**Current Focus**: v6 and v7

**Deprecated Parameters** (not covered):
- `--v 4`, `--v 5`, `--v 5.1`, `--v 5.2` (older versions)
- `--hd`, `--test` (legacy quality modes)

**Future Features** (subject to change):
- Additional --style variants
- Enhanced personalization options
- New creative control parameters

---

## Quick Reference Table

| Parameter | Range/Options | Default | Primary Use |
|-----------|---------------|---------|-------------|
| --v | 6, 7 | 6 | Version selection |
| --niji | 6 | Off | Anime/illustration mode |
| --style | raw, expressive, scenic, cute | None | Style variation |
| --stylize (-s) | 0-1000 | 100 | Artistic interpretation level |
| --chaos (-c) | 0-100 | 0 | Result variation |
| --weird (-w) | 0-3000 | 0 | Unconventional aesthetics |
| --sref | URL(s) | None | Style reference image |
| --cref | URL | None | Character reference |
| --cw | 0-100 | 100 | Character preservation level |
| --personalize (-p) | flag or code | Off | Personal aesthetic |
| --ar | ratio | 1:1 | Aspect ratio |
| --q | 0.25, 0.5, 1, 2 | 1 | Render quality |
| --tile | flag | Off | Seamless tiling |
| --video | flag | Off | Generation video |
| --no | elements | None | Negative prompting |

---

## Final Recommendations

1. **Start simple**: Don't use all parameters at once
2. **Understand each parameter**: Know what each does before combining
3. **Test systematically**: Change one parameter at a time to understand effects
4. **Match parameters to intent**: Align parameter choices with artistic goals
5. **Save successful combinations**: Document what works for future reference
6. **Iterate intelligently**: Adjust based on results, not randomly
7. **Use references wisely**: --sref and --cref are powerful but should complement, not replace, good prompts

---

Remember: Parameters are tools to achieve your vision, not formulas to follow blindly. Understanding their effects allows you to make intentional choices that serve your creative goals.
