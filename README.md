# GEPA + LangChain Tutorial: Production RAG Assistant

This repo demonstrates how to build a production-grade LangChain RAG support copilot, trace it with MLflow, and automatically optimize its prompts using GEPA.

## What you'll learn

- Build a simple but realistic RAG assistant with LangChain
- Add MLflow tracing for observability and prompt versioning
- Use GEPA to improve prompts against an evaluation set automatically
- Compare baseline vs optimized behavior with metrics

## Why this matters

Most LLM apps start as prompt-driven demos. The real challenge is **improving quality systematically** as data grows. This tutorial shows a production-friendly optimization loop:

```
Build (LangChain) → Measure (MLflow) → Optimize (GEPA) → Repeat
```

## Architecture overview

- **LangChain**: orchestrates retrieval + generation (the execution layer)
- **MLflow**: tracing, experiment tracking, and prompt registry (the observability layer)
- **GEPA**: evolutionary prompt optimization using reflection (the improvement layer)

## Use cases

This pattern applies to any LLM app needing systematic improvement:

- Support copilots over knowledge bases
- Internal HR / IT / compliance assistants
- Developer copilots over code + docs
- Workflow agents that retrieve data then call tools

## Setup

### 1. Create environment

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set environment variables

Create a `.env` file from `.env.example`:

```bash
cp .env.example .env
# Edit .env and add your keys:
# GROQ_API_KEY=your-groq-api-key
# MLFLOW_TRACKING_URI=http://localhost:5000
```

### 4. Start MLflow UI

```bash
mlflow ui --host 0.0.0.0 --port 5000
```

Then visit `http://localhost:5000` in your browser to watch traces and experiments in real-time.

## Run the tutorial

### Step 1: Run the baseline app

```bash
python src/app.py
```

Ask a few questions and observe:
- How well does it answer?
- Are answers grounded in the docs?
- Any hallucinations or inconsistencies?

Example questions:
- "How do I reset my password?"
- "Can I get a refund after 20 days?"
- "Is SSO available for all plans?"

### Step 2: Run the evaluation set

```bash
python src/eval.py
```

This runs the app on a fixed set of questions and logs outputs. Check MLflow UI to see traces.

### Step 3: Optimize with GEPA

```bash
python src/optimize.py
```

This runs GEPA for ~1-2 minutes. GEPA will:
1. Sample prompt variants
2. Run them on your eval set
3. Reflect on what works vs. what fails
4. Keep a Pareto frontier of candidates
5. Register the best prompt back to MLflow

### Step 4: Compare before/after

Re-run the baseline app with the same questions:

```bash
python src/app.py
```

You should see:
- More accurate, grounded answers
- Fewer hallucinations
- More consistent tone

## File structure

```
gepa-langchain-lab/
├─ README.md                 # This file
├─ requirements.txt          # Dependencies
├─ .env.example              # Template for environment variables
├─ src/
│  ├─ prompts.py            # Prompt templates
│  ├─ ingest.py             # Vector store setup
│  ├─ app.py                # Baseline RAG app (run interactively)
│  ├─ eval.py               # Evaluation harness
│  └─ optimize.py           # GEPA optimization loop
├─ data/
│  └─ sample_docs.txt       # Sample knowledge base
└─ scripts/
   └─ video_recording_notes.md  # Recording plan
```

## Architecture diagram

```
┌─────────────────────────────────────────────────┐
│  Your LangChain RAG App (src/app.py)            │
│  - Retriever: vector store                      │
│  - Chain: retriever + LLM + prompt              │
└────────────────┬────────────────────────────────┘
                 │ Calls
                 ▼
┌─────────────────────────────────────────────────┐
│  MLflow (Tracing + Registry)                    │
│  - Traces: inputs, outputs, reasoning           │
│  - Metrics: accuracy, tokens, latency           │
│  - Prompts: versioned in registry               │
└────────────────┬────────────────────────────────┘
                 │ Reads traces & metrics
                 ▼
┌─────────────────────────────────────────────────┐
│  GEPA Optimizer (src/optimize.py)               │
│  - Reflection: LLM reads traces, proposes fixes │
│  - Evolution: genetic algorithm explores space  │
│  - Pareto: keeps best prompt variants           │
└─────────────────────────────────────────────────┘
```

## Key concepts

### Closed-loop optimization

Instead of hand-tuning prompts once, GEPA creates a **feedback loop**:

1. **Data**: real queries + reference answers
2. **Metrics**: clear evaluation criteria (correctness, groundedness, tone)
3. **Optimization**: GEPA uses LLM reflection + evolutionary search to improve
4. **Deployment**: best prompt is registered back and your app picks it up

### Why GEPA vs RL?

GEPA doesn't need to differentiate through your model. Instead:
- Works with prompts, configs, even code
- Uses explicit evaluation metrics (LLM-based, rule-based, human-graded)
- More sample-efficient than RL (~35× fewer evals in benchmarks)

### Why Groq?

Groq makes the tutorial better because:
- **Speed**: faster inference means quicker optimization loops
- **Cost**: free tier is generous
- **Simplicity**: LangChain integration is seamless

## Notes for recording a video

See `scripts/video_recording_notes.md` for a 10–12 minute script structure.

### Key talking points

1. "LangChain is how you **build** the agent."
2. "MLflow is how you **measure** it."
3. "GEPA is how you **improve** it automatically."
4. "This pattern scales to any LLM app: support bots, copilots, workflow agents."

## Next steps

- Expand the eval set with more real queries
- Add custom evaluators (e.g., groundedness checks)
- Integrate with a real vector DB (Pinecone, Weaviate, etc.)
- Run GEPA on a schedule as new eval data comes in
- Swap out Groq for your preferred LLM provider

## Resources

- [GEPA docs](https://gepa-ai.github.io/gepa/)
- [LangChain docs](https://python.langchain.com/)
- [MLflow docs](https://mlflow.org/)
- [Groq + LangChain integration](https://console.groq.com/docs/langchain)

## License

MIT
