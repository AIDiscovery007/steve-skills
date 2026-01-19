---
name: generating-images
description: Generate images via tuzi API from text prompts with Midjourney parameter support. Use when user wants to generate images, create AI art, convert prompts to actual images, or mentions "generate image", "create image", "tuzi API".
user-invocable: false
allowed-tools: Bash, Read
---

# Generating Images

Generate AI images from text prompts using the tuzi API. This skill automatically maps Midjourney-style parameters to tuzi API format.

## Quick Start

### 1. Configure Credentials

Create a `.env.local` file in the repository root with:

```bash
TUZI_API_KEY=your-api-key-here
TUZI_API_BASE=https://api.tu-zi.com
TUZI_MODEL=gemini-3-pro-image-preview-2k
```

### 2. Install Dependencies (One-time)

```bash
cd /Users/qiaochao/steve-skills/.claude/skills/generating-images
npm install
```

### 3. Generate Images

```bash
cd /Users/qiaochao/steve-skills/.claude/skills/generating-images && \
node tuzi-client.js "your prompt here --ar 16:9 --q 2"
```

---

## Usage

### CLI Interface

```bash
node tuzi-client.js "<prompt with optional Midjourney parameters>"
```

**Examples**:

```bash
# Simple prompt
node tuzi-client.js "a cat sitting on a windowsill"

# With aspect ratio
node tuzi-client.js "cyberpunk cityscape at night --ar 16:9"

# With quality setting
node tuzi-client.js "portrait of a woman --ar 2:3 --q 2"

# Full Midjourney-style prompt (parameters auto-stripped)
node tuzi-client.js "watercolor portrait, 1 young woman, soft pastel colors --ar 2:3 --stylize 120 --v 7"
```

### Response Format

**Success**:
```json
{
  "success": true,
  "imageUrl": "https://..."
}
```

**Error**:
```json
{
  "success": false,
  "error": "Error description",
  "category": "AUTH_ERROR|NETWORK_ERROR|GENERATION_ERROR|VALIDATION_ERROR",
  "suggestion": "How to fix this issue"
}
```

---

## Parameter Mapping

The client automatically converts Midjourney parameters to tuzi API format.

### Aspect Ratio (`--ar`)

| Midjourney | tuzi API Size |
|------------|---------------|
| `--ar 16:9` | 1792x1024 |
| `--ar 9:16` | 1024x1792 |
| `--ar 1:1` | 1024x1024 (default) |
| `--ar 2:3` | 1024x1536 |
| `--ar 3:2` | 1536x1024 |
| `--ar 4:5` | 1024x1280 |
| `--ar 5:4` | 1280x1024 |

### Quality (`--q`)

| Midjourney | tuzi API Quality |
|------------|------------------|
| `--q 0.25` | standard |
| `--q 0.5` | standard |
| `--q 1` | standard (default) |
| `--q 2` | hd |

### Style (`--style`)

| Midjourney | tuzi API Style |
|------------|----------------|
| `--style raw` | natural |

### Stripped Parameters

These Midjourney-specific parameters are removed from the prompt (not applicable to tuzi API):

- `--v [version]` - Midjourney version
- `--stylize [0-1000]` - Artistic interpretation
- `--chaos [0-100]` - Variation
- `--weird [0-3000]` - Experimental
- `--draft` - Draft mode
- `--oref`, `--cref`, `--sref` - Reference images
- `--cw` - Character weight
- `--personalize`, `--p` - Personalization
- `--niji` - Anime mode
- `--no [elements]` - Negative prompt

---

## Error Handling

### Error Categories

| Category | Description | Common Causes |
|----------|-------------|---------------|
| `AUTH_ERROR` | Authentication issues | Missing/invalid API key, incomplete configuration |
| `NETWORK_ERROR` | Network problems | Timeout, rate limit, connection issues |
| `GENERATION_ERROR` | Generation failed | API service issues, empty response |
| `VALIDATION_ERROR` | Invalid input | No prompt provided, invalid parameters |

### Troubleshooting

**1. `ENV_NOT_FOUND` - API credentials not configured**

```
Solution: Create .env.local in repository root with:
- TUZI_API_KEY
- TUZI_API_BASE
- TUZI_MODEL
```

**2. Authentication failed (401/403)**

```
Solution: Check your .env.local:
- Verify API key is correct
- No extra spaces or quotes
- Key is active on tuzi platform
```

**3. Network timeout**

```
Solution:
- Check internet connection
- Retry the request
- API service may be temporarily unavailable
```

**4. Rate limit exceeded (429)**

```
Solution: Wait a moment and try again
```

### Retry Logic

The client automatically retries failed requests:
- 3 retry attempts with exponential backoff (2s, 4s, 8s)
- No retry for auth errors (401, 403) or validation errors (400, 422)

---

## Integration with prompt-generator

This skill works seamlessly with the **prompt-generator** skill:

### Workflow

1. Use `/prompt-generator` to create high-quality prompts
2. After Phase 4 output, choose "Generate image directly"
3. prompt-generator calls this skill automatically
4. Image URL is returned and displayed

### Manual Integration

If calling directly after prompt-generator:

```bash
# Copy the prompt from prompt-generator output, then:
cd /Users/qiaochao/steve-skills/.claude/skills/generating-images && \
node tuzi-client.js "your complete prompt --ar 16:9 --stylize 60 --v 7"
```

The client will:
1. Extract mappable parameters (--ar, --q, --style raw)
2. Strip Midjourney-specific parameters
3. Send clean prompt to tuzi API

---

## Technical Details

### Dependencies

- Node.js (uses native `https`, `fs`, `path` modules)
- TypeScript types: `@types/node` (dev dependency only)

### Files

| File | Purpose |
|------|---------|
| `tuzi-client.ts` | TypeScript source |
| `tuzi-client.js` | Compiled JavaScript (run this) |
| `package.json` | Dependencies |
| `tsconfig.json` | TypeScript configuration |
| `.env.local.example` | Configuration template |

### Recompiling TypeScript

If you modify `tuzi-client.ts`:

```bash
cd /Users/qiaochao/steve-skills/.claude/skills/generating-images && \
npx tsc tuzi-client.ts
```

---

## Best Practices

1. **Use with prompt-generator**: Generate optimized prompts first, then use this skill
2. **Start simple**: Test with basic prompts before complex ones
3. **Check aspect ratio**: Ensure --ar matches your intended use case
4. **Handle errors gracefully**: Check the `success` field in responses
5. **Keep prompts clean**: Midjourney-specific parameters are stripped, so focus on descriptive text

---

## Critical: Bash Tool Invocation

**IMPORTANT**: When calling this skill via the Bash tool, **DO NOT set explicit `timeout` parameter**.

### Correct Usage (Synchronous)

```bash
# Good - no timeout parameter, command runs synchronously
node /Users/qiaochao/steve-skills/.claude/skills/generating-images/tuzi-client.js "your prompt --ar 16:9"
```

### Incorrect Usage (Background Execution)

```bash
# Bad - setting timeout causes command to run in background
# This leads to "Network timeout" errors and requires TaskOutput to retrieve results
Bash(command="...", timeout=120000)  # DON'T DO THIS
```

### Why This Matters

- Setting explicit `timeout` parameter causes Bash tool to treat the command as a long-running task
- The command gets pushed to background execution
- Results must be retrieved via `TaskOutput`, which often times out before API responds
- **Solution**: Omit the `timeout` parameter entirely, let Bash use default synchronous behavior

### Recommended Invocation Pattern

```python
# In Claude Code, call like this:
Bash(command='node /path/to/tuzi-client.js "prompt"', description="Generate image via tuzi API")
# NO timeout parameter!
```

---

## Related Skills

- **prompt-generator**: Generate high-quality AI image prompts with Midjourney V7 optimization
  - Use `/prompt-generator` to create prompts
  - Phase 4.5 offers direct integration with this skill
