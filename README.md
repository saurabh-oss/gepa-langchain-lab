# GEPA + LangChain Optimization Boilerplate

A production-ready architectural boilerplate for building and automatically optimizing LangChain RAG applications using MLflow tracing and GEPA prompt optimization.

## Architecture

This project implements a three-layer architecture for systematic LLM app improvement:

```
Build (LangChain) → Measure (MLflow) → Optimize (GEPA) → Repeat
```

**Components:**
- **LangChain** (`src/app.py`): Retrieval + generation orchestration
- **MLflow** (auto-integrated): Execution tracing, metrics, and prompt versioning
- **GEPA** (`src/optimize.py`): Evolutionary prompt optimization with reflection

## Applicable Use Cases

This boilerplate generalizes to any retrieval-augmented LLM application:
- Support/customer service agents
- Internal knowledge assistants (HR, IT, compliance)
- Developer documentation assistants
- Tool-using workflows with retrieval

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

## Quick Start

### 1. Run the baseline app

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

### 2. Run the evaluation set

```bash
python src/eval.py
```

This runs the app on a fixed set of questions and logs outputs. Check MLflow UI to see traces.

### 3. Optimize with GEPA

```bash
python src/optimize.py
```

This runs GEPA for ~1-2 minutes. GEPA will:
1. Sample prompt variants
2. Run them on your eval set
3. Reflect on what works vs. what fails
4. Keep a Pareto frontier of candidates
5. Register the best prompt back to MLflow

### 4. Compare before/after

Re-run the baseline app with the same questions:

```bash
python src/app.py
```

You should see:
- More accurate, grounded answers
- Fewer hallucinations
- More consistent tone

## Project Structure

```
gepa-langchain-lab/
├─ README.md              # This file
├─ requirements.txt       # Python dependencies
├─ .env.example           # Environment template
├─ src/
│  ├─ __init__.py         # Package marker
│  ├─ prompts.py          # Prompt templates
│  ├─ ingest.py           # Vector store initialization
│  ├─ app.py              # Baseline RAG application
│  ├─ eval.py             # Evaluation harness
│  └─ optimize.py         # GEPA optimization runner
├─ data/
│  └─ sample_docs.txt     # Sample knowledge base
└─ .gitignore
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

## Customization Guide

### 1. Replace Sample Data
- Update `data/sample_docs.txt` or modify `src/ingest.py` to load your documents
- Adjust vector store (swap FAISS for Pinecone, Weaviate, etc.)

### 2. Customize Evaluation Set
- Edit `EVAL_SET` in `src/eval.py` with your real queries and expected answers
- Add custom evaluation metrics beyond `Correctness` if needed

### 3. Change LLM Providers
- Replace `ChatGroq` in `src/app.py` with `ChatOpenAI`, `ChatAnthropic`, etc.
- Update `src/optimize.py` reflection/scoring models as needed

### 4. Modify Prompts
- Edit `BASE_SYSTEM_PROMPT` in `src/prompts.py`
- Adjust retrieval template in `src/app.py` prompt chain

### 5. Add Production Integrations
- Run `src/optimize.py` on a schedule (cron, DAG, etc.)
- Integrate MLflow UI with your monitoring stack
- Add persistence layer for prompt versions

## Resources

- [GEPA docs](https://gepa-ai.github.io/gepa/)
- [LangChain docs](https://python.langchain.com/)
- [MLflow docs](https://mlflow.org/)
- [Groq + LangChain integration](https://console.groq.com/docs/langchain)

## License

MIT
