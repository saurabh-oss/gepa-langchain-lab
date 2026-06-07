# GEPA + LangChain Showcase Demo

This guide shows how to demonstrate the optimization power of GEPA and MEGA with **visible, tangible improvements**.

## The Problem We're Solving

Modern LLM applications often suffer from:
- ❌ Generic, unhelpful answers
- ❌ Answers not grounded in provided context
- ❌ Inconsistent response quality
- ❌ Poor routing decisions
- ❌ Wasted token usage

## The Solution: Closed-Loop Optimization

This boilerplate automates the process:
```
Raw LLM App → Measure Performance → Optimize → Better App → Repeat
```

## Quick Showcase (10 minutes)

### Step 1: Understand Your Baseline (2 min)

```bash
python -m src.benchmark
```

This shows:
- ✓ 8 comprehensive test questions
- ✓ Current performance score
- ✓ Where answers need improvement
- ✓ Different prompt variants that will be tested

**Output looks like:**
```
[Q1] How do I reset my password and make it more secure?
Expected: Settings > Account > Security > Change Password with 12+ chars...
Got: Reset password in settings...
Match Score: 65% ✗ Needs improvement
```

### Step 2: Optimize with GEPA (4 min)

```bash
python -m src.optimize
```

This will:
1. Generate 4 prompt variants (Base, Detailed, Strict, Conversational)
2. Test each on your 8 eval questions
3. Score which performs best
4. Show you the winner

**Look for:**
- Prompt variant scores (shows which style wins)
- Best performing variant name
- Example outputs from different approaches

### Step 3: Optimize with MEGA (2 min)

```bash
python -m src.optimize_mega
```

This will:
1. Test 4 workflow strategies
2. Show routing and retrieval trade-offs
3. Recommend the best configuration

**Look for:**
- Variant performance scores
- Which workflow won and why
- Improvement percentage

### Step 4: See the Improvement (2 min)

```bash
python -m src.app
```

Ask the same questions as before:
- "How do I reset my password and make it more secure?"
- "What is your refund policy for annual vs monthly plans?"
- "How reliable are webhooks?"

**You should notice:**
- More complete, structured answers
- Better grounding in actual facts
- Proper step-by-step instructions
- Relevant caveats and details

---

## Extended Showcase (30 minutes)

### 1. Manual Comparison Script

Create a side-by-side comparison:

```bash
# Terminal 1: Run baseline
python -m src.app

# Ask: "Which authentication methods are available on my plan?"
# Note the answer quality

# Terminal 2: View what was optimized
cat src/optimize.py  # See the variants being tested
```

### 2. MLflow Dashboard (Real-Time)

In another terminal:
```bash
mlflow ui --host 0.0.0.0 --port 5000
```

Visit `http://localhost:5000` to see:
- 📊 Each optimization run
- 📈 Metric progression
- 🔄 Different variants tested
- 📝 Trace logs for each question

### 3. Show the Knowledge Base

```bash
cat src/ingest.py
```

Show the expanded knowledge base (8 comprehensive docs with realistic details):
- Account Security
- API Keys Management  
- Billing & Refunds
- Authentication Methods
- Webhook Configuration
- Data Privacy & Compliance
- Rate Limiting
- Team Management

### 4. Show the Evaluation Set

```bash
grep -A 2 "question" src/eval.py
```

Show the 8 challenging test questions that require:
- Multi-step answers
- Specific details
- Context awareness
- Complete information

---

## Key Metrics to Highlight

When presenting, emphasize:

1. **Answer Completeness**
   - Before: "SSO is available on Enterprise plans"
   - After: "All plans: OAuth 2.0, JWT. Paid: MFA. Professional+: SAML SSO. Enterprise: Full SSO + passwordless"

2. **Structure & Organization**
   - Before: Long, rambling paragraphs
   - After: Numbered steps, clear sections, actionable format

3. **Context Grounding**
   - Before: Generic answers
   - After: Specific facts from documentation

4. **Consistency**
   - Before: Varies by prompt
   - After: Reliably follows optimized style

---

## Talking Points for Audiences

### For Product Teams
- ✓ Automated prompt optimization = faster iteration
- ✓ A/B testing at scale (test 100s of variants)
- ✓ Data-driven improvements (not guessing)
- ✓ Reproducible, measurable results

### For Engineering Teams
- ✓ No model fine-tuning needed
- ✓ Works with any LLM (OpenAI, Anthropic, Groq, etc.)
- ✓ Local evaluation = fast feedback loops
- ✓ MLflow integration for observability

### For Executives
- ✓ Reduce customer support tickets
- ✓ Improve customer satisfaction
- ✓ Lower LLM token costs (better routing)
- ✓ Production-ready architecture

---

## What Makes This Demo Effective

✅ **Real Data** — 8 documents covering realistic support topics
✅ **Challenging Questions** — Not trivial, shows real improvement
✅ **Visible Metrics** — Before/after scores you can see
✅ **Multiple Optimization Layers** — GEPA (prompts) + MEGA (workflows)
✅ **Real Execution** — Actually runs optimization, doesn't fake it
✅ **Open Source** — Code is transparent, auditable, customizable

---

## Customization for Your Domain

To use this for your own domain:

1. **Replace knowledge base** (src/ingest.py)
   - Add your 8+ most important documents
   - Include edge cases and complex scenarios

2. **Update eval set** (src/eval.py)
   - 8+ questions that matter for your use case
   - Include both simple and complex queries

3. **Adjust prompts** (src/prompts.py)
   - Add domain-specific prompt variants
   - GEPA will test and rank them

4. **Run showcase**
   - Same process, but with your data
   - Real improvements on your content

---

## Timeline for Full Showcase

```
00:00-02:00 | Setup & baseline (python -m src.benchmark)
02:00-06:00 | GEPA optimization (python -m src.optimize)
06:00-08:00 | MEGA optimization (python -m src.optimize_mega)
08:00-10:00 | See improvements (python -m src.app)
10:00-20:00 | Explore MLflow, show code, discuss architecture
20:00-30:00 | Q&A, customization discussion
```

---

## Success Criteria

The showcase is successful when the audience sees:

1. ✓ Baseline answers (flawed, incomplete)
2. ✓ Optimization process (systematic, data-driven)
3. ✓ Improved answers (noticeably better)
4. ✓ Metrics proving it (scores show improvement)
5. ✓ Code understanding (they see how it works)

---

**Remember:** The magic isn't that it's perfect—it's that it's **automated, measurable, and continuous**.
