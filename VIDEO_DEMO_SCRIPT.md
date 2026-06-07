# Video Demo Script: GEPA + LangChain Optimization

A simple, visual explanation of the 4-step optimization journey.

---

## 🎬 INTRO (30 seconds)

**Say:**
> "Today we're going to demonstrate how to automatically improve an AI assistant using GEPA and MEGA optimization. We'll take a basic chatbot and make it significantly better—all measured with real metrics."

**Show:** Terminal screen, clean project folder

---

## 📊 Step 1: BENCHMARK (2 minutes)

**Command:**
```bash
python -m src.benchmark
```

### What's Happening?

**Think of it like:** *Taking a test before studying*

**In Simple Terms:**
- We ask our AI assistant 8 real questions
- We measure how good the answers are (0-100%)
- This is our "baseline" — our starting point

**Visual Flow:**
```
Question 1 → AI Assistant → Gets an Answer → Score: 65% ✗
Question 2 → AI Assistant → Gets an Answer → Score: 52% ✗
Question 3 → AI Assistant → Gets an Answer → Score: 48% ✗
...
Average Score: 62%
```

### What You'll See on Screen:

```
[Q1] How do I reset my password and make it more secure?
Expected: Settings > Account > Security > Change Password with 12+ chars...
Got: Reset password in settings...
Match Score: 65% ✗ Needs improvement
```

**Explain:**
- Green checkmark (✓) = Answer is good (70%+)
- Red X (✗) = Answer needs improvement (<70%)
- At the end: "Average Match Score: 62%"

**Say:**
> "Right now, our AI assistant is getting about 62% correct. It's giving vague, incomplete answers. Now let's improve it using GEPA."

---

## 🧠 Step 2: OPTIMIZE PROMPTS with GEPA (4 minutes)

**Command:**
```bash
python -m src.optimize
```

### What's Happening?

**Think of it like:** *Trying different teaching styles*

**In Simple Terms:**
- GEPA tests 4 different prompt strategies:
  1. **Base** — "Be helpful and detailed"
  2. **Strict** — "Only answer from the knowledge base"
  3. **Detailed** — "Give comprehensive answers with steps"
  4. **Conversational** — "Explain like a friendly teammate"
  
- It runs ALL 4 on your 8 test questions
- It scores which style works best
- It picks the winner

**Visual Flow:**
```
Test all 4 prompt variants:

Variant A: Base Style        → Test on Q1-Q8 → Score: 62%
Variant B: Strict Style      → Test on Q1-Q8 → Score: 55%
Variant C: Detailed Style    → Test on Q1-Q8 → Score: 78% ⭐ WINNER
Variant D: Conversational    → Test on Q1-Q8 → Score: 71%

Winner: "Detailed Style" will now be used
```

**What You'll See on Screen:**

```
Generating prompt variants...

[1/4] Evaluating 'base' variant...
  Score: 62%
[2/4] Evaluating 'strict' variant...
  Score: 55%
[3/4] Evaluating 'detailed' variant...
  Score: 78% ✓
[4/4] Evaluating 'conversational' variant...
  Score: 71%

Best variant: detailed
Accuracy: 78%
```

**Key Point to Explain:**
> "This is the magic of GEPA. Instead of us guessing which prompt is best, we let data decide. We test different styles and pick the winner. That's why it works so well."

---

## 🔄 Step 3: OPTIMIZE WORKFLOWS with MEGA (2 minutes)

**Command:**
```bash
python -m src.optimize_mega
```

### What's Happening?

**Think of it like:** *Optimizing a recipe - not just ingredients, but the cooking process*

**In Simple Terms:**
- GEPA optimized WHAT the AI says (the prompts)
- MEGA optimizes HOW it decides things:
  - When to search for information
  - How many sources to use
  - Whether to refine answers
  - How confident to be

**Visual Flow:**
```
Test different workflow strategies:

Strategy 1: High Retrieval    → Get lots of info → Test on Q1-Q8 → Score: 75%
Strategy 2: With Refinement   → Polish answers  → Test on Q1-Q8 → Score: 81% ⭐ WINNER
Strategy 3: Reasoning Heavy   → Think deeply    → Test on Q1-Q8 → Score: 68%
Strategy 4: Balanced          → Balanced mix    → Test on Q1-Q8 → Score: 74%

Winner: "With Refinement" strategy
Improvement: +15% better than baseline
```

**What You'll See on Screen:**

```
Generating workflow variants...

[1/4] Evaluating 'high_retrieval' variant...
  Score: 75%
[2/4] Evaluating 'with_refinement' variant...
  Score: 81% ✓
[3/4] Evaluating 'reasoning_heavy' variant...
  Score: 68%
[4/4] Evaluating 'balanced' variant...
  Score: 74%

Best Workflow Variant: with_refinement
Performance Score: 81%
Improvement: +15.0%
```

**Key Point to Explain:**
> "MEGA looks at the whole workflow — not just the prompt, but HOW the AI makes decisions. By combining GEPA (better prompts) and MEGA (better workflow), we get the best results."

---

## ✨ Step 4: SEE THE IMPROVEMENTS (2 minutes)

**Command:**
```bash
python -m src.app
```

### What's Happening

**Think of it like:** *Taking a test AFTER studying and improving*

**In Simple Terms:**
- This runs the AI with BOTH optimizations:
  - Best prompt from GEPA
  - Best workflow from MEGA
- Ask the same questions as Step 1
- See how much better the answers are now

### The Transformation

**BEFORE (Step 1 - Baseline):**
```
Q: How do I reset my password and make it more secure?
A: Go to settings and reset your password.
   Score: 65% ✗
```

**AFTER (Step 4 - Optimized):**
```
Q: How do I reset my password and make it more secure?
A: Navigate to Settings > Account > Security > Change Password.
   Use at least 12 characters including uppercase, lowercase, 
   numbers, and special characters. Then enable two-factor 
   authentication in Settings > Security > 2FA for additional 
   protection.
   Score: 92% ✓
```

**What You'll See on Screen:**

```
================================================================================
LangChain RAG Support Copilot
Type 'exit' or 'quit' to stop
================================================================================

Question: How do I reset my password and make it more secure?

Answer: Navigate to Settings > Account > Security > Change Password. 
Use at least 12 characters including uppercase, lowercase, numbers, 
and special characters. Then enable two-factor authentication in 
Settings > Security > 2FA for additional protection.

================================================================================
```

**Key Differences to Point Out:**
- ✓ Much longer, more detailed
- ✓ Step-by-step instructions
- ✓ Specific security recommendations
- ✓ Actionable advice
- ✓ Grounded in actual knowledge

---

## 📈 FINAL COMPARISON CHART (for video)

**Show this side-by-side:**

| Aspect | Before | After |
|--------|--------|-------|
| **Answer Length** | 10 words | 50+ words |
| **Detail Level** | Vague | Specific steps |
| **Grounded** | Generic | References actual system |
| **Actionable** | Incomplete | Full instructions |
| **Score** | 62% | 81% |

---

## 🎓 Key Takeaways to Explain

**Say this at the end:**

> "Let me summarize what just happened:
>
> 1. **Benchmark** — We measured where we started (62%)
> 
> 2. **GEPA** — We tested 4 different prompt styles and found that detailed, structured prompts work 16% better
>
> 3. **MEGA** — We tested 4 different workflows and found that refining answers improves them another 3%
>
> 4. **Result** — Combined: 62% → 81% improvement. That's a 30% boost in quality.
>
> And the best part? This all happened automatically, with real measurements. We didn't guess — we tested and measured."

---

## 💡 Talking Points for Q&A

**"What if I want to optimize my own domain?"**
> "You would replace the documents in `src/ingest.py` with your own, update the evaluation set with your own questions, and run the exact same pipeline. GEPA and MEGA will optimize for YOUR domain."

**"Does this work with other LLMs?"**
> "Yes! We use Groq here, but you can swap in OpenAI, Anthropic, or any LLM. The optimization process stays the same."

**"How long does this take?"**
> "The benchmark takes 1 minute, GEPA takes 4 minutes, MEGA takes 2 minutes. Total: about 7 minutes to see real improvements."

**"What if my domain is different?"**
> "Perfect! This is exactly why the boilerplate exists. You customize the data and questions, run the same pipeline, and get optimized results for YOUR specific use case."

---

## 🎥 Video Structure

```
0:00-0:30   | Intro: What we're doing
0:30-3:00   | Step 1: Benchmark (show baseline)
3:00-7:00   | Step 2: GEPA optimization (show variants being tested)
7:00-9:00   | Step 3: MEGA optimization (show workflow strategies)
9:00-11:00  | Step 4: See improvements (show better answers)
11:00-12:00 | Summary & comparison chart
12:00-15:00 | Q&A / Customization discussion
```

---

## 📝 Visual Cues for Video

- **Use colors:**
  - 🔴 Red for "before" / poor performance
  - 🟢 Green for "after" / good performance
  - 🟡 Yellow for "in progress"

- **Zoom in** on the percentage scores as they appear

- **Pause** at the final comparison to let viewers absorb the improvement

- **Use text overlays** to highlight key metrics:
  - "Baseline: 62%"
  - "After GEPA: 78%"
  - "After MEGA: 81%"
  - "Total improvement: +30%"

---

## 🚀 Demo Commands (Copy-Paste Ready)

```bash
# Step 1: Baseline
python -m src.benchmark

# Step 2: Optimize with GEPA
python -m src.optimize

# Step 3: Optimize with MEGA
python -m src.optimize_mega

# Step 4: See improvements
python -m src.app

# Ask these questions:
# - How do I reset my password and make it more secure?
# - What is your refund policy for annual vs monthly plans?
# - How reliable are webhooks?
```

---

## Final Notes

- Keep the demo **flowing and fast** — don't get stuck on technical details
- **Emphasize the metrics** — that's what makes this impressive
- **Show the transformation** — before/after answers are the real demo
- **Keep it interactive** — ask questions in Step 4, don't just show answers
