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

## Optimization Strategy

This boilerplate implements **two complementary optimization layers:**

1. **Prompt Optimization (GEPA)** — Improves what the agent says
   - Better answer quality and relevance
   - Fewer hallucinations
   - More consistent tone and format

2. **Workflow Optimization (MEGA)** — Improves how the agent works
   - Better routing decisions
   - Optimal tool selection and ordering
   - Trade-offs between retrieval and reasoning

**Run both for comprehensive improvement.**

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

### 3. Optimize prompts with GEPA

```bash
python src/optimize.py
```

This runs GEPA for ~1-2 minutes. GEPA will:
1. Sample prompt variants
2. Run them on your eval set
3. Reflect on what works vs. what fails
4. Keep a Pareto frontier of candidates
5. Register the best prompt back to MLflow

### 4. (Optional) Optimize workflow with MEGA

```bash
python src/optimize_mega.py
```

This optimizes the agent workflow structure:
1. Generate workflow variants (different routing, retrieval settings)
2. Evaluate each variant on your eval set
3. Score block-level performance
4. Return best workflow configuration

MEGA is optional but recommended for production agents.

### 5. Compare results

After running optimizations, re-run the baseline app:

```bash
python src/app.py
```

You should see improvements from both:
- **GEPA**: More accurate, grounded answers
- **MEGA**: Better routing and decision-making
- **Combined**: Superior performance across metrics

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
│  ├─ optimize.py         # GEPA prompt optimizer
│  └─ optimize_mega.py    # MEGA workflow optimizer (optional)
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
└─────────────┬──────────────────┬────────────────┘
              │ Calls            │ Calls
              ▼                  ▼
   ┌──────────────────┐  ┌────────────────────┐
   │ MLflow Tracing   │  │ MLflow Tracing     │
   │ (for GEPA)       │  │ (for MEGA)         │
   └────────┬─────────┘  └────────┬───────────┘
            │ Reads               │ Reads
            ▼                     ▼
┌─────────────────────────────────────────────────┐
│  Evaluation Harness (src/eval.py)               │
│  - Fixed test set with expected answers         │
│  - Shared by both GEPA and MEGA                 │
└─────────────────────────────────────────────────┘
            │ Evaluates
            ├─────────────────┬──────────────────┐
            ▼                 ▼                  ▼
┌───────────────────┐ ┌──────────────────────────┐
│ GEPA Optimizer    │ │ MEGA Optimizer           │
│ (src/optimize.py) │ │ (src/optimize_mega.py)   │
├───────────────────┤ ├──────────────────────────┤
│ Optimizes:        │ │ Optimizes:               │
│ - Prompts         │ │ - Workflow routing       │
│ - System config   │ │ - Tool selection         │
│ - Answer template │ │ - Retrieval settings     │
└───────────────────┘ └──────────────────────────┘
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

### Prompt vs. Workflow Optimization

**GEPA (Prompt Optimization):**
- What the agent *says*
- Improves answer quality, tone, formatting
- Works on textual parameters
- ~35× more sample-efficient than RL

**MEGA (Workflow Optimization):**
- How the agent *works*
- Optimizes routing, tool selection, decision logic
- Works on structural parameters
- Block-level performance scoring
- Complements GEPA for comprehensive improvement

**Use Together:** Run GEPA first to improve answers, then MEGA to improve routing.

### Why Groq?

Groq makes the boilerplate better because:
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

### 5. Extend Workflow Optimization (MEGA)

MEGA is optional but powerful for production agents. Customize it by:
- Adding new workflow variants in `WorkflowOptimizer.generate_variants()`
- Implementing custom block-level scorers
- Adding constraints (latency, cost limits)
- Integrating tool selection and reranking logic

Example custom variant:
```python
def generate_variants(self):
    # ... existing variants ...
    
    # Custom variant: my_strategy
    custom = {
        "name": "my_strategy",
        "blocks": {...},
        "routing": {
            "when_to_retrieve": "selective",
            "max_retrieval_docs": 2,
            "use_reranker": True,
        }
    }
    variants.append(custom)
```

### 6. Add Production Integrations
- Run `src/optimize.py` on a schedule (cron, DAG, etc.)
- Run `src/optimize_mega.py` after GEPA completes
- Integrate MLflow UI with your monitoring stack
- Persist optimized prompts and workflows
- Monitor both GEPA and MEGA improvements over time

## Resources

- [GEPA docs](https://gepa-ai.github.io/gepa/)
- [LangChain docs](https://python.langchain.com/)
- [MLflow docs](https://mlflow.org/)
- [Groq + LangChain integration](https://console.groq.com/docs/langchain)

## License

MIT
