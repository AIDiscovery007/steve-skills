# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a **Claude Code skills repository** containing custom slash commands and prompt engineering tools. The primary focus is AI image prompt generation for **Midjourney V7 (2025)** and Stable Diffusion.

**Last Updated**: January 2026 - Fully upgraded for Midjourney V7

## Repository Structure

```
steve-skills/
├── .claude/
│   ├── settings.local.json          # Claude Code permissions configuration
│   └── skills/
│       ├── manga-story-bible/       # Manga Story Development Skill (NEW)
│       │   ├── SKILL.md             # 6-Phase workflow for story creation
│       │   ├── STORY_STRUCTURE.md   # Story structure frameworks
│       │   ├── CHARACTER_SYSTEM.md  # Want/Need/Flaw character system
│       │   ├── WORLDBUILDING.md     # 3-layer worldbuilding framework
│       │   └── OUTPUT_FORMATS.md    # Output formats & skill integration
│       ├── manga-designer/          # Manga Panel Design Skill
│       │   ├── SKILL.md             # Panel layout workflow
│       │   ├── CHARACTER_BIBLE.md   # Character visual management
│       │   ├── NAME_WORKFLOW.md     # Storyboard workflow
│       │   ├── KOMA_DESIGN.md       # Panel design techniques
│       │   ├── TRANSITIONS.md       # Transition techniques
│       │   ├── styles/              # Style guides (shounen/shoujo)
│       │   ├── templates/           # Format templates
│       │   └── examples/            # Sample projects
│       ├── prompt-generator/        # AI Image Prompt Generation Skill (V7)
│       │   ├── SKILL.md             # Core workflow with V7 features
│       │   ├── TECHNIQUES.md        # 10 core techniques (8 classic + 2 V7)
│       │   ├── PARAMETERS_V7.md     # Midjourney V7 parameter reference
│       │   ├── IMAGE_ANALYSIS.md    # 7-dimension image analysis with V7
│       │   └── styles/              # Style guides
│       └── generating-images/       # Image Generation API Skill
│           ├── SKILL.md             # API documentation and usage
│           ├── tuzi-client.ts       # TypeScript source
│           ├── tuzi-client.js       # Compiled JavaScript client
│           ├── package.json         # Dependencies
│           ├── tsconfig.json        # TypeScript configuration
│           └── .env.local.example   # Configuration template
├── .env.local                       # API credentials (not in git)
├── hand_drawn.png                   # Reference image for hand-drawn style
├── jietou_anhei.png                 # Reference image for street dark style
└── shuicai.JPG                      # Reference image for watercolor style
```

---

## Skill Ecosystem

This repository contains four interconnected skills for manga/comic creation:

### Skill Overview

| Skill | Purpose | Input | Output |
|-------|---------|-------|--------|
| **manga-story-bible** | Pre-production | User concept | Story bible (text) |
| **manga-designer** | Panel layout | Story outline | Panel descriptions |
| **prompt-generator** | Prompt hub | Any visual need | AI image prompts |
| **generating-images** | Image generation | Prompts | Final images |

### Collaboration Flow

```
manga-story-bible ──→ manga-designer ──→ prompt-generator ──→ generating-images
    (前期创作)          (分镜排版)          (提示词优化)          (图像生成)
        │                   │                    ↑
        │                   └────────────────────┘
        │                                        ↑
        └────────────────────────────────────────┘
        (角色设定图/世界观概念图可直接调用)
```

### 1. manga-story-bible (漫画故事圣经)

**Purpose**: Pre-production story development system

**Core Capabilities**:
1. Deep concept exploration (Socratic questioning)
2. Story structure design (Climax-first, Kishotenketsu)
3. Character system development (Want/Need/Flaw framework)
4. Worldbuilding (3-layer framework)
5. Conflict architecture (Internal/External conflict matrix)
6. Standardized output (Integration with other skills)

**Workflow Phases**:
- Phase 0: Concept spark
- Phase 1: Story architecture
- Phase 2: Character alchemy
- Phase 3: World synthesis
- Phase 4: Conflict architecture
- Phase 5: Integration & export

### 2. manga-designer (漫画设计师)

**Purpose**: Panel layout and storyboard design

**Core Capabilities**:
1. Story structure design (Kishotenketsu / Three-Act)
2. Panel composition (RTL reading order, panel allocation)
3. Manga-specific techniques (breaking borders, focus lines, screentone)
4. Character visual management (--cref/--oref for AI consistency)
5. Editor-style feedback iteration
6. AI prompt generation integration

### 3. prompt-generator (提示词中台)

**Purpose**: Central hub for AI image prompt generation

**Core Capabilities**:
1. Text-to-prompt creation (V7 optimized)
2. Image reverse engineering (7-dimension framework)
3. Flexible output modes (Quick/Standard/Detailed)
4. V7 draft mode iteration
5. Multi-platform support (Midjourney V7, V6, Stable Diffusion)

### 4. generating-images (图像生成)

**Purpose**: API client for image generation

**Core Capabilities**:
1. Direct image generation via tuzi API
2. Midjourney parameter mapping
3. Error handling with retry logic
4. Integration with prompt-generator

### Skill Integration Points

| Stage | Integration | Output |
|-------|-------------|--------|
| manga-story-bible Phase 2 | → prompt-generator | Character design sheets |
| manga-story-bible Phase 3 | → prompt-generator | World concept art |
| manga-story-bible Phase 5 | → manga-designer | Story bible for paneling |
| manga-designer Phase 4 | → prompt-generator | Panel prompts |
| prompt-generator Phase 4.5 | → generating-images | Final images |

## The Prompt Generator Skill

### Purpose
A comprehensive AI image prompt generation system designed to create high-quality prompts for Midjourney and Stable Diffusion through intelligent conversation, structured analysis, and proven writing techniques.

### Core Capabilities

1. **Text-to-Prompt Creation**: Convert user descriptions into structured, effective prompts optimized for V7
2. **Image Reverse Engineering**: Analyze existing images using a 7-dimension framework to generate reproduction prompts
3. **Flexible Output Modes**: Quick (~150-200 words), Standard (~300-400 words), Detailed (~600-800 words)
4. **V7 Draft Mode Iteration** (NEW): 10x faster prototyping with --draft parameter for rapid exploration
5. **Multi-Platform Support**: Midjourney V7 (default), V6 (legacy), Stable Diffusion
6. **V7 Parameter Expertise**: --draft, --oref, enhanced personalization, prompt weighting (::), positive descriptions

### Modular Documentation Architecture

The skill uses a **streamlined modular documentation system** where each file serves a specific purpose:

- **SKILL.md**: Entry point with complete V7 workflow, all output templates merged inline, Phase 0 personalization setup
- **TECHNIQUES.md**: 10 core techniques (8 classic + 2 NEW V7: prompt weighting, positive descriptions)
- **PARAMETERS_V7.md**: Complete Midjourney V7 parameter reference with --draft, --oref, personalization, V6 compatibility notes
- **IMAGE_ANALYSIS.md**: 7-dimension framework updated for V7 (better text, improved anatomy, draft mode workflow)

**Note**: OUTPUT_TEMPLATES.md and REFERENCE.md have been removed - content integrated into SKILL.md for efficiency

### 7-Dimension Image Analysis Framework

When analyzing images for reverse engineering:

1. **Subject Identification**: Core objects, quantity, position, focus
2. **Style Classification**: Medium (photo/painting/3D), era, movement
3. **Composition Analysis**: Camera angle, framing, layout, visual flow
4. **Color System**: Dominant colors, accents, temperature, saturation
5. **Lighting Analysis**: Light source type, direction, contrast, effects
6. **Atmosphere & Mood**: Emotional feel, tone, concepts
7. **Technical Characteristics**: Sharpness, DOF, detail level, post-processing

### 10 Core Writing Techniques (8 Classic + 2 V7)

**Classic Techniques**:
1. **Number Emphasis**: Use "1" to prevent element multiplication and emphasize focus
2. **Repetition Reinforcement**: Repeat key styles 2-3 times for emphasis
3. **Negative Exclusion**: Actively exclude unwanted elements (minimize in V7)
4. **Medium Definition**: Define creation medium first for texture foundation
5. **Color Control**: Use "main color + accents of + accent color" structure
6. **Professional Terminology**: Use precise technical terms over vague adjectives
7. **Hierarchical Description**: Layer from subject → details → atmosphere → technical
8. **Tension Creation**: Balance opposing elements for depth

**NEW V7 Techniques**:
9. **Prompt Weighting**: Use `::` syntax to prioritize elements (e.g., `sunset::2 mountains::`)
10. **Positive-First Description**: Describe what you DO want, not what you don't (V7 best practice)

### Key Midjourney V7 Parameters

**V7 NEW Parameters**:
- `--draft`: 10x faster iterations, 50% cost reduction (use for exploration)
- `--oref [URL]`: Visual trait consistency across batches
- `--personalize` / `--p [code]`: Enhanced personalization system (mandatory V7 setup)

**Essential Parameters**:
- `--v 7` (default), `--v 6` (legacy): Version control
- `--stylize [0-1000]`, `--chaos [0-100]`, `--weird [0-3000]`: Creative control
- `--cref [URL]`, `--cw [0-100]`: Character reference and weight
- `--sref [URL]`: Style reference
- `--ar [ratio]`: Aspect ratio
- `--q [0.25|0.5|1|2]`: Quality level
- `--style raw`: Photographic realism
- `--niji 6`: Anime/illustration mode

**V7 Decision Logic**:
- Iteration phase → --draft (10x faster)
- Final render → --v 7 --q 2
- Realistic photography → low --stylize, --style raw
- Artistic/stylized → medium-high --stylize
- Experimental → --weird, high --chaos
- Character consistency → --cref + --cw
- Visual trait consistency → --oref
- Positive descriptions → Preferred over --no in V7

### Workflow Phases

The skill follows a 6-phase V7 interaction model:

0. **Phase 0**: V7 personalization setup (first-time V7 users only - rate ~200 images)
1. **Phase 1**: Initial setup (output mode, task type, V7 vs V6 selection)
2. **Phase 1.5**: Image analysis (reverse engineering tasks - 7-dimension framework)
3. **Phase 2**: Structure design (choose appropriate template based on complexity)
4. **Phase 3**: Generate prompt (apply 10 techniques, V7 best practices)
5. **Phase 4**: Formatted output (Quick/Standard/Detailed modes, all templates inline)
6. **Phase 4.5**: Optional API generation (integrates with `generating-images` skill)
7. **Phase 5**: V7 draft mode optimization (--draft iterations → final --v 7 --q 2 render)

## The Generating Images Skill

### Purpose
A dedicated API client for generating images from text prompts using the tuzi API. Works standalone or integrated with `prompt-generator`.

### Core Capabilities

1. **Direct Image Generation**: Generate images from text prompts via tuzi API
2. **Midjourney Parameter Mapping**: Automatically converts --ar, --q, --style raw to tuzi format
3. **Error Handling**: Categorized errors with retry logic and troubleshooting suggestions
4. **Integration**: Seamless integration with prompt-generator Phase 4.5

### Parameter Mapping

| Midjourney | tuzi API |
|------------|----------|
| `--ar 16:9` | 1792x1024 |
| `--ar 9:16` | 1024x1792 |
| `--ar 1:1` | 1024x1024 |
| `--q 2` | hd |
| `--style raw` | natural |

### Configuration

Requires `.env.local` in repository root:
```
TUZI_API_KEY=your-api-key
TUZI_API_BASE=https://api.tu-zi.com
TUZI_MODEL=gemini-3-pro-image-preview-2k
```

### Usage

```bash
cd .claude/skills/generating-images && node tuzi-client.js "your prompt --ar 16:9"
```

## Working with This Repository

### Accessing the Skill

The prompt-generator skill is accessible via the slash command:
```
/prompt-generator
```

This command is whitelisted in `.claude/settings.local.json` for direct use.

### Reading Skill Documentation

When working with the prompt-generator skill:
- **Always start with SKILL.md** for the complete V7 workflow (includes all output templates inline)
- **Use the Read tool** to access specific modules as needed:
  - TECHNIQUES.md for detailed technique explanations
  - PARAMETERS_V7.md for complete parameter reference
  - IMAGE_ANALYSIS.md for 7-dimension framework
- **Follow V7 best practices**: Draft mode iteration, positive descriptions, prompt weighting
- **Reference modular docs** at appropriate workflow phases (noted in SKILL.md)

### Image Handling

The repository contains reference images in the root:
- Use the **Read tool** to access local image files for analysis
- Images can be analyzed using the 7-dimension framework
- Support for JPG, PNG formats

### Understanding the Philosophy

This skill emphasizes:
- **Principles over templates**: Every prompt should be original, not copied
- **Structured thinking**: From concept to details, macro to micro
- **Precise control**: Every word has purpose, no keyword piling
- **Modular learning**: Read relevant documentation when needed, not everything at once
- **Systematic analysis**: Use frameworks (7-dimension, 10 techniques) for consistency
- **V7-first approach**: Leverage V7 features (draft mode, personalization, positive descriptions)
- **Efficient iteration**: Draft mode exploration → refinement → final high-quality render

### Common Patterns

When generating prompts:

**For simple scenarios** (single subject, clear style):
```
Style → Subject → Details → Atmosphere → Parameters
```

**For complex scenarios** (abstract concepts, multi-dimensional):
```
Concept → Theme → Audience → Emotion → Narrative → Visual → Technical → Exclusion → Parameters
```

**For image reverse engineering**:
```
7-dimension analysis → User confirmation → Extract keywords →
Structured assembly → Apply techniques → Generate with parameters
```

## Important Principles

### Default Workflow: Prompt Design First

When users request image generation, **always prioritize prompt design over direct generation**:

1. **Default behavior**: Deeply analyze the user's requirements and craft an optimized prompt first
2. **Exception**: Only generate images directly if the user explicitly says "直接生成" / "directly generate" / "skip prompt design"
3. **Rationale**: A well-designed prompt produces significantly better results than quick generation

**Workflow Decision Logic**:
```
User input contains image request?
├─ YES: User says "直接生成" / "directly generate"?
│       ├─ YES → Use generating-images skill directly
│       └─ NO → Use prompt-generator skill first → Then offer generation
└─ NO: Handle other requests normally
```

### Do's ✅
- Always understand user intent through Phase 1 questioning
- Apply writing principles, not templates
- Use modular documentation - read relevant .md files when needed
- Provide output matching user's chosen mode (Quick/Standard/Detailed - all templates in SKILL.md)
- Systematically analyze images using all 7 dimensions
- Match parameters to style positioning
- **V7**: Default to --v 7, use --draft for iteration, apply positive descriptions
- **V7**: Recommend draft mode workflow (explore → refine → final render)

### Don'ts ❌
- Don't pile keywords without structure
- Don't abuse parameters
- Don't use vague adjectives instead of precise descriptions
- Don't guess image content - use proper analysis framework
- **V7**: Don't use excessive negatives (prefer positive descriptions)
- **V7**: Don't skip draft mode for iteration (10x faster)
- **V7**: Don't forget personalization setup for first-time V7 users

## File Organization Philosophy

This repository uses a **streamlined, modular architecture** with two complementary skills:

### Skill Separation
- **prompt-generator**: Prompt creation, techniques, and optimization
- **generating-images**: API integration for direct image generation

### Modular Documentation
- Core workflow in single entry points (SKILL.md for each skill)
- Detailed reference materials in separate, focused documents
- Style guides in dedicated subdirectories
- Reference images in root for easy access

### Integration Design
- prompt-generator Phase 4.5 calls generating-images for direct generation
- Skills can be used independently or together
- Shared configuration (.env.local in repository root)

This approach optimizes for:
- **Separation of concerns**: Prompt creation vs. image generation
- **Reduced context usage**: Only read what's needed for current task
- **Maintainability**: Each skill can be updated independently
- **Flexibility**: Use skills standalone or in combination
