---
name: autotune
description: "Autonomously optimize any markdown prompt document by running it repeatedly, scoring outputs against binary evals, mutating the prompt, and keeping improvements. Based on Karpathy's autoresearch methodology. Use when: optimize this prompt, improve this document, run autotune on, make this better, self-improve prompt, benchmark this prompt, tune this instructions, optimize my claude.md. Works on: SKILL.md, CLAUDE.md, instruction files, harness docs, or any .md prompt document. Outputs: an improved prompt file, a results log, and a changelog of every mutation tried."
---

# Autotune

Most prompts work about 70% of the time. The other 30% you get garbage. The fix isn't to rewrite the prompt from scratch. It's to let an agent run it dozens of times, score every output, and tighten the instructions until that 30% disappears.

This skill adapts Andrej Karpathy's autoresearch methodology (autonomous experimentation loops) to any markdown prompt document. Instead of optimizing ML training code, we optimize prompts.

---

## the core job

Take any existing prompt document, define what "good output" looks like as binary yes/no checks, then run an autonomous loop that:

1. Generates outputs from the prompt using test inputs
2. Scores every output against the eval criteria
3. Mutates the prompt to fix failures
4. Keeps mutations that improve the score, discards the rest
5. Repeats until the score ceiling is hit or the user stops it

**Output:** An improved prompt file + `results.tsv` log + `changelog.md` of every mutation attempted + a live HTML dashboard you can watch in your browser.

---

## before starting: gather context

**STOP. Do not run any experiments until all fields below are confirmed with the user. Ask for any missing fields before proceeding.**

**IMPORTANT: If you detect that the user has switched between different tasks within the same conversation turn, remind them to start a new session to avoid context contamination.**

1. **Target prompt** — Which prompt document do you want to optimize? (need the exact path to the .md file — can be SKILL.md, CLAUDE.md, or any markdown instruction file)
2. **Test inputs** — What 3-5 different prompts/scenarios should we test the prompt with? (variety matters — pick inputs that cover different use cases so we don't overfit to one scenario)
3. **Eval criteria** — What 3-6 binary yes/no checks define a good output? (these are your "test questions" — see [references/eval-guide.md](references/eval-guide.md) for how to write good evals)
4. **Runs per experiment** — How many times should we run the prompt per mutation? Default: 5. (more runs = more reliable scores, but slower and more expensive. 5 is the sweet spot for most prompts.)
5. **Run interval** — How often should experiments cycle? Default: every 2 minutes. (shorter = faster iteration, but costs more)
6. **Budget cap** — Optional. Max number of experiment cycles before stopping. Default: no cap (runs until you stop it).

---

## step 1: read the prompt

Before changing anything, read and understand the target prompt completely.

1. Read the full target .md file
2. Read any files in `references/` that the prompt links to
3. Identify the prompt's core purpose, process steps, and output format
4. Note any existing quality checks or anti-patterns already in the prompt

DO NOT skip this. You need to understand what the prompt does before you can improve it.

---

## step 2: build the eval suite

Convert the user's eval criteria into a structured test. Every check must be binary — pass or fail, no scales.

**Format each eval as:**

```
EVAL [number]: [Short name]
Question: [Yes/no question about the output]
Pass condition: [What "yes" looks like — be specific]
Fail condition: [What triggers a "no"]
```

**Rules for good evals:**
- Binary only. Yes or no. No scales. Scales compound variability and give unreliable results.
- Specific enough to be consistent. "Is the text readable?" is too vague. "Are all words spelled correctly with no truncated sentences?" is testable.
- Not so narrow that the prompt games the eval. "Contains fewer than 200 words" will make the prompt optimize for brevity at the expense of everything else.
- 3-6 evals is the sweet spot. More than that and the prompt starts parroting eval criteria back instead of actually improving.

See [references/eval-guide.md](references/eval-guide.md) for detailed examples of good evals vs bad evals.

**Max score calculation:**
```
max_score = [number of evals] × [runs per experiment]
```

Example: 4 evals × 5 runs = max score of 20.

---

## step 3: generate the live dashboard

Before running any experiments, create a live HTML dashboard at `autotune-[name]/dashboard.html` and open it in the browser.

The dashboard must:
- Auto-refresh every 10 seconds (reads from results.tsv)
- Show a score progression line chart (experiment number on X axis, pass rate % on Y axis)
- Show a colored bar for each experiment: green = keep, red = discard, blue = baseline
- Show a table of all experiments with: experiment #, score, pass rate, status, description
- Show per-eval breakdown: which evals pass most/least across all runs
- Show current status: "Running experiment [N]..." or "Idle"
- Use clean styling with soft colors (white background, pastel accents, clean sans-serif font)

Generate the dashboard as a single self-contained HTML file with inline CSS and JavaScript. Use Chart.js loaded from CDN for the line chart. The JS should fetch `results.json` (which you update after each experiment alongside results.tsv) and re-render.

**Open it immediately** after creating it: start an HTTP server in the background, then open via `http://`:

```bash
cd /path/to/autotune-[name]/
python3 -m http.server 8080 &
open http://localhost:8080/dashboard.html
```

Tell the user: **"Dashboard available at http://localhost:8080 — keep this server running during the experiment loop."**

**CORS note:** When opening `dashboard.html` directly via `file://`, the browser blocks `fetch('results.json')`. To fix this, embed the current `results.json` content directly in the `<script>` as a fallback before attempting the fetch:
```html
const embeddedData = { /* copy results.json content here */ };
render(embeddedData);
// then try fetch as live update when served via http
```

**Update `results.json`** after every experiment so the dashboard stays current. The JSON format:

```json
{
  "prompt_name": "[name]",
  "status": "running",
  "current_experiment": 3,
  "baseline_score": 70.0,
  "best_score": 90.0,
  "experiments": [
    {
      "id": 0,
      "score": 14,
      "max_score": 20,
      "pass_rate": 70.0,
      "status": "baseline",
      "description": "original prompt — no changes"
    }
  ],
  "eval_breakdown": [
    {"name": "Text legibility", "pass_count": 8, "total": 10},
    {"name": "Clear structure", "pass_count": 9, "total": 10}
  ]
}
```

When the run finishes (user stops it or ceiling hit), update `status` to `"complete"` so the dashboard shows a "Done" state with final summary.

---

## step 4: establish baseline

Run the prompt AS-IS before changing anything. This is experiment #0.

1. Create a working directory: `autotune-[name]/` alongside the target prompt file (or in a sensible location)
2. IMPORTANT: Add the new directory to `.gitignore` so experiment artifacts are not committed:
   ```
   # Autotune output directories (per-prompt experiment results)
   .claude/skills/*/autotune-*/
   ```
   If the project already has ignore entries, append the pattern.
3. Create `results.tsv` with the header row
4. Create `results.json` and `dashboard.html`, then start the HTTP server and open via `http://localhost:8080/dashboard.html`
5. Back up the original prompt as `[original-filename].baseline` (e.g., `claude.md.baseline`)
6. Run the prompt [N] times using the test inputs
7. Score every output against every eval
8. Record the baseline score and update both results.tsv and results.json

**results.tsv format (tab-separated):**

```
experiment	score	max_score	pass_rate	status	description
0	14	20	70.0%	baseline	original prompt — no changes
```

**IMPORTANT:** After establishing baseline, confirm the score with the user before proceeding. If baseline is already 90%+, the prompt may not need optimization — ask the user if they want to continue.

---

## step 5: run the experiment loop

This is the core autotune loop. Once started, run autonomously until stopped.

**LOOP:**

1. **Analyze failures.** Look at which evals are failing most. Read the actual outputs that failed. Identify the pattern — is it a formatting issue? A missing instruction? An ambiguous directive?

2. **Form a hypothesis.** Pick ONE thing to change. Don't change 5 things at once — you won't know what helped.

   Good mutations:
   - Add a specific instruction that addresses the most common failure
   - Reword an ambiguous instruction to be more explicit
   - Add an anti-pattern ("DO NOT do X") for a recurring mistake
   - Move a buried instruction higher in the prompt (priority = position)
   - Add or improve an example that shows the correct behavior
   - Remove an instruction that's causing the prompt to over-optimize for one thing at the expense of others

   Bad mutations:
   - Rewriting the entire prompt from scratch
   - Adding 10 new rules at once
   - Making the prompt longer without a specific reason
   - Adding vague instructions like "make it better" or "be more creative"

3. **Make the change.** Edit the prompt file with ONE targeted mutation.

4. **Run the experiment.** Execute the prompt [N] times with the same test inputs.

5. **Score it.** Run every output through every eval. Calculate total score.

6. **Decide: keep or discard.**
   - Score improved → **KEEP.** Log it. This is the new baseline.
   - Score stayed the same → **DISCARD.** Revert the prompt to previous version. The change added complexity without improvement.
   - Score got worse → **DISCARD.** Revert the prompt to previous version.

7. **Log the result** in results.tsv.

8. **Repeat.** Go back to step 1 of the loop.

**NEVER STOP.** Once the loop starts, do not pause to ask the user if you should continue. They may be away from the computer. Run autonomously until:
- The user manually stops you
- You hit the budget cap (if one was set)
- You hit 95%+ pass rate for 3 consecutive experiments (diminishing returns)

**If you run out of ideas:** Re-read the failing outputs. Try combining two previous near-miss mutations. Try a completely different approach to the same problem. Try removing things instead of adding them. Simplification that maintains the score is a win.

---

## step 6: write the changelog

After each experiment (whether kept or discarded), append to `changelog.md`:

```markdown
## Experiment [N] — [keep/discard]

**Score:** [X]/[max] ([percent]%)
**Change:** [One sentence describing what was changed]
**Reasoning:** [Why this change was expected to help]
**Result:** [What actually happened — which evals improved/declined]
**Failing outputs:** [Brief description of what still fails, if anything]
```

This changelog is the most valuable artifact. It's a research log that any future agent (or smarter future model) can pick up and continue from.

---

## step 7: deliver results

When the user returns or the loop stops, present:

1. **Score summary:** Baseline score → Final score (percent improvement)
2. **Total experiments run:** How many mutations were tried
3. **Keep rate:** How many mutations were kept vs discarded
4. **Top 3 changes that helped most** (from the changelog)
5. **Remaining failure patterns** (what the prompt still gets wrong, if anything)
6. **The improved prompt file** (already saved in place)
7. **Location of results.tsv and changelog.md** for reference

---

## output format

The skill produces four files in `autotune-[name]/`:

```
autotune-[name]/
├── dashboard.html       # live browser dashboard (auto-refreshes)
├── results.json         # data file powering the dashboard
├── results.tsv         # score log for every experiment
├── changelog.md         # detailed mutation log
└── [original-filename].baseline  # original prompt before optimization
```

Plus the improved prompt file saved back to its original location.

**results.tsv example:**

```
experiment	score	max_score	pass_rate	status	description
0	14	20	70.0%	baseline	original prompt — no changes
1	16	20	80.0%	keep	added explicit instruction to avoid vague language
2	16	20	80.0%	discard	tried enforcing bullet point style — no improvement
3	18	20	90.0%	keep	replaced "make it clear" with specific readability criteria
4	18	20	90.0%	discard	added strict length limit — no improvement
5	19	20	95.0%	keep	added worked example showing correct format
```

---

## example: optimizing a CLAUDE.md project instruction file

**Context gathered:**
- Target prompt: `~/project/CLAUDE.md`
- Test inputs: "Add a new feature", "Fix a bug in auth", "Refactor the database layer", "Write tests for API", "Review code for security"
- Evals: (1) Does it follow project conventions? (2) Are the instructions specific enough to act on? (3) Does it avoid conflicting with existing patterns? (4) Is the output actionable?
- Runs per experiment: 5
- Max score: 20

**Baseline run (experiment 0):**
Generated outputs for 5 tasks. Scored each against 4 evals. Result: 14/20 (70%).
Common failures: vague instruction words like "clean", "proper", vague error handling guidance.

**Experiment 1 — KEEP (16/20, 80%):**
Change: Replaced "use proper error handling" with "return error codes from [ERR_001-ERR_050] enum and log to stderr with timestamp".
Result: Actionability eval improved. Other evals held steady.

**Experiment 2 — DISCARD (15/20, 75%):**
Change: Added "Always use TypeScript strict mode".
Result: Too restrictive — conflicted with existing JavaScript files. Reverted.

**Experiment 3 — KEEP (18/20, 90%):**
Change: Added examples of what "project conventions" actually means (file naming: kebab-case, imports sorted alphabetically, test files co-located with source).
Result: Convention eval went from 3/5 to 5/5. Other evals held.

**Experiment 4 — DISCARD (18/20, 90%):**
Change: Added anti-pattern "DO NOT use abbreviations in variable names".
Result: No change. Some abbreviations (e.g., `idx`, `req`, `res`) are project-standard. Reverted.

**Experiment 5 — KEEP (19/20, 95%):**
Change: Added a "convention cheat sheet" section showing 3 before/after examples of common patterns.
Result: Hit 19/20. One remaining failure: complex multi-file refactoring tasks still occasionally miss related test updates. Diminishing returns — stopped.

**Final delivery:**
- Baseline: 14/20 (70%) → Final: 19/20 (95%)
- 5 experiments, 3 kept, 2 discarded
- Top changes: specific error code enums, convention examples with before/after
- Remaining issue: multi-file refactoring sometimes skips related test files (1/25 failure rate)

---

## how this connects to other skills

**What feeds into autotune:**
- Any existing prompt document that needs optimization (SKILL.md, CLAUDE.md, etc.)
- User-defined eval criteria (or help them define evals using the eval guide)

**What autotune feeds into:**
- The improved prompt replaces the original
- The changelog can be passed to future models for continued optimization
- The eval suite can be reused whenever the prompt is updated

---

## the test

A good autotune run:

1. **Started with a baseline** — never changed anything before measuring the starting point
2. **Used binary evals only** — no scales, no vibes, no "rate this 1-10"
3. **Changed one thing at a time** — so you know exactly what helped
4. **Kept a complete log** — every experiment recorded, kept or discarded
5. **Improved the score** — measurable improvement from baseline to final
6. **Didn't overfit** — the prompt got better at the actual job, not just at passing the specific test inputs
7. **Ran autonomously** — didn't stop to ask permission between experiments

If the prompt "passes" all evals but the actual output quality hasn't improved — the evals are bad, not the prompt. Go back to step 2 and write better evals.
