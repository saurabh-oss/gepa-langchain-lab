# Video Recording Plan: GEPA + LangChain

**Duration:** 10–12 minutes  
**Target audience:** LLM/AI engineers building production apps  
**Platform:** YouTube, Dev.to, etc.

## Scene structure

### 1. Hook (0:00–0:30)
**Problem statement**
- "Most LLM apps start as prompt-driven demos."
- "In production, 'mostly works' is not good enough."
- Show a bad output or hallucination from the baseline.

**Narration:**
> "You built a LangChain RAG assistant. It works... most of the time. But how do you systematically improve it without hand-tuning prompts forever?"

### 2. The baseline app (0:30–2:30)
**Show the code structure**
- Open `src/app.py` and walk through briefly:
  - Retriever (vector store)
  - Prompt template
  - LLM call
- Emphasize: This is a **normal LangChain pattern** everyone recognizes.

**Live demo**
- Run `python src/app.py`
- Ask 2–3 questions:
  - "How do I reset my password?"
  - "Can I get a refund after 20 days?"
- Highlight: some answers are good, some are weak.

**Talking point:**
> "LangChain is how you *build* the agent. Simple, familiar, production-ready."

### 3. Observability with MLflow (2:30–3:30)
**Open MLflow UI**
- Run `mlflow ui --host 0.0.0.0 --port 5000`
- Show the trace view:
  - Inputs
  - Retriever output
  - LLM response
  - Token count and latency

**Talking point:**
> "MLflow shows us exactly what the system is doing. No instrumentation needed; autologging handles it."

### 4. Evaluation harness (3:30–4:30)
**Show `src/eval.py`**
- Explain the 4 eval questions
- Expected answers for each

**Run evaluation**
```bash
python src/eval.py
```

- Show outputs for all 4 questions
- Highlight: some are correct, some are vague or miss details

**Talking point:**
> "You can't improve what you don't measure. An evaluation set is the foundation."

### 5. GEPA optimization (4:30–7:00)
**Explain GEPA in 60 seconds**
- "GEPA = Genetic + Pareto + reflection"
- Uses LLM to read traces and suggest prompt improvements
- Evolutionary search to explore prompt variants
- Keeps a Pareto frontier of high-quality options

Show the code in `src/optimize.py`:
- Registering the system prompt
- Calling `optimize_prompts()` with a Groq model
- Using a correctness scorer

**Run optimization**
```bash
python src/optimize.py
```

**Narrate what's happening:**
> "GEPA is now reading the traces, reflecting on what works, and proposing new prompts. It's testing variants and keeping the best ones."

Let this run to completion (1–2 minutes).

**Talking point:**
> "Instead of hand-tuning prompts, GEPA evolves them using data and explicit metrics."

### 6. Before/after comparison (7:00–9:30)
**Re-run the baseline app**
```bash
python src/app.py
```

Ask the same 4 questions again. Show side-by-side:
- **Before**: answers were vague, sometimes off-topic
- **After**: more accurate, better-grounded, more consistent tone

**Talking point:**
> "Same questions, same data, better answers. That's what systematic optimization looks like."

### 7. Architectural lesson (9:30–11:00)
**Show or draw the three-layer architecture:**

```
┌─────────────────────┐
│  LangChain (Run)    │
├─────────────────────┤
│  MLflow (Measure)   │
├─────────────────────┤
│  GEPA (Improve)     │
└─────────────────────┘
```

**Generalization**
- "Replace docs with HR policies → same pattern"
- "Replace RAG with tool-using agent → same pattern"
- "Replace support bot with internal copilot → same pattern"

**Talking point:**
> "This architecture works for almost any LLM app. Build with LangChain, measure with MLflow, improve with GEPA."

### 8. Closing (11:00–12:00)
**Key takeaways:**
1. Closed-loop optimization beats manual prompt tuning
2. Evaluation metrics are essential
3. GEPA is sample-efficient (~35× fewer evaluations than RL)
4. Pattern is generic—apply it to your use case

**Call to action:**
- Link to the GitHub repo
- Link to GEPA docs, LangChain docs, MLflow docs
- "Fork this repo, adapt the docs and eval set to your use case, and ship a better system."

---

## Narration script (for reference)

**Full script to read aloud:**

> In this video, we're going to take a normal LangChain RAG app and turn it into a system that improves itself.
>
> Here's the problem most of us face: you build a chatbot or assistant, it works okay, but in production you realize 'okay' is not enough. You need higher quality, fewer hallucinations, and lower costs. But tweaking prompts by hand is tedious and doesn't scale.
>
> GEPA is an open-source framework that solves this. Instead of hand-tuning, you set up an evaluation harness with real examples and metrics, then GEPA automatically explores prompt variants and keeps the best ones.
>
> Let's build it. Here's the baseline: a simple LangChain RAG app that retrieves from a small document corpus and answers questions. It uses Groq for speed. Run it, ask a few questions... and you'll see it works, but not perfectly.
>
> MLflow automatically traces every call—retrieval, reasoning, outputs, tokens. Now we have visibility.
>
> Next, we define an evaluation set: four representative questions with expected answers. This is what we'll optimize against.
>
> Now we run GEPA. It will take the baseline system prompt, generate variants, run each one on the eval set, score them using a Correctness metric, and keep a Pareto frontier of good candidates. This is reflection plus evolutionary search.
>
> While GEPA runs, here's what's happening behind the scenes: an LLM is reading execution traces—what the system was asked, what it retrieved, what it answered—and proposing better prompts. GEPA then mutates those proposals and tests them.
>
> After optimization completes, we re-run the app with the same questions. Watch how much better the answers are: more accurate, more grounded, more consistent.
>
> Architecturally, this is clean: LangChain orchestrates execution, MLflow measures it, GEPA improves it. And it generalizes. Replace the docs with HR policies or IT runbooks, or change the agent to a tool-using system—the pattern stays the same.
>
> That's the power of this approach: it's not magic, it's just data-driven optimization applied to text.

---

## Recording tips

- **Pacing**: Let silence happen. Don't fill every second.
- **Zoom level**: Make code readable on screen (font size 14+).
- **Tab visibility**: Show only one main tab at a time.
- **Terminal output**: Enlarge terminal so viewers can see results clearly.
- **Pauses**: After running a command, wait for it to finish; viewers need time to read output.

## Checklist before recording

- [ ] `.env` file set with valid `GROQ_API_KEY` and `MLFLOW_TRACKING_URI`
- [ ] `mlflow ui` is running on `http://localhost:5000`
- [ ] Virtual environment activated and all packages installed
- [ ] Sample docs are in place (`data/sample_docs.txt`)
- [ ] Terminal is clean and readable (light terminal with dark background or vice versa)
- [ ] Screen recording software is ready (OBS, ScreenFlow, etc.)
- [ ] Microphone is working and levels are good
- [ ] No browser notifications or other pop-ups during recording
- [ ] Internet is stable (GEPA and Groq will call external APIs)
