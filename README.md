# GEPA + LangChain Optimization Boilerplate

A production-ready architectural boilerplate for building and automatically optimizing LangChain RAG applications using MLflow tracing and GEPA prompt optimization.

## Architecture

This project implements a three-layer architecture for systematic LLM app improvement:

```
Build (LangChain) → Measure (MLflow) → Optimize (GEPA) → Repeat
```

**Components:**
- **LangChain** (`src/app.py`): Retrieval + generation orchestration with local keyword-based retrieval
- **MLflow** (auto-integrated): Execution tracing, metrics, and experiment tracking
- **GEPA** (`src/optimize.py`): Evolutionary prompt optimization with variant generation
- **MEGA** (`src/optimize_mega.py`): Workflow optimization for routing and tool selection

## Applicable Use Cases

This boilerplate generalizes to any retrieval-augmented LLM application:
- Support/customer service agents
- Internal knowledge assistants (HR, IT, compliance)
- Developer documentation assistants
- Tool-using workflows with retrieval
- Q&A systems with fact-based responses

## Setup

### 1. Create virtual environment

**macOS/Linux:**
```bash
python -m venv .venv
source .venv/bin/activate
```

**Windows (PowerShell):**
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

**Windows (Command Prompt):**
```cmd
python -m venv .venv
.venv\Scripts\activate.bat
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set environment variables

Create a `.env` file from `.env.example`:

**macOS/Linux:**
```bash
cp .env.example .env
# Edit .env and add your keys:
# GROQ_API_KEY=your-groq-api-key
# MLFLOW_TRACKING_URI=http://localhost:5000
```

**Windows (PowerShell):**
```powershell
Copy-Item .env.example .env
# Edit .env and add your keys
```

**Windows (Command Prompt):**
```cmd
copy .env.example .env
REM Edit .env and add your keys
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
   - Variant generation and evaluation

2. **Workflow Optimization (MEGA)** — Improves how the agent works
   - Better routing decisions
   - Optimal tool selection and ordering
   - Trade-offs between retrieval and reasoning
   - Block-level performance scoring

**Run both for comprehensive improvement.**

## Quick Start

### 1. Run the baseline app

**macOS/Linux:**
```bash
python -m src.app
```

**Windows:**
```powershell
python -m src.app
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

**macOS/Linux:**
```bash
python -m src.eval
```

**Windows:**
```powershell
python -m src.eval
```

This runs the app on a fixed set of questions and logs outputs. Check MLflow UI to see traces.

### 3. Optimize prompts with GEPA

**macOS/Linux:**
```bash
python -m src.optimize
```

**Windows:**
```powershell
python -m src.optimize
```

This runs GEPA for ~1-2 minutes. GEPA will:
1. Generate prompt variants (base, detailed, concise, formal)
2. Run them on your eval set
3. Score performance and select the best variant
4. Return metrics and recommendations

### 4. (Optional) Optimize workflow with MEGA

**macOS/Linux:**
```bash
python -m src.optimize_mega
```

**Windows:**
```powershell
python -m src.optimize_mega
```

This optimizes the agent workflow structure:
1. Generate workflow variants (high_retrieval, with_refinement, reasoning_heavy, balanced)
2. Evaluate each variant on your eval set
3. Score block-level performance
4. Return best workflow configuration with improvements

MEGA is optional but recommended for production agents.

### 5. Compare results

After running optimizations, re-run the baseline app:

**macOS/Linux:**
```bash
python -m src.app
```

**Windows:**
```powershell
python -m src.app
```

You should see improvements from both:
- **GEPA**: More accurate, grounded answers
- **MEGA**: Better routing and decision-making
- **Combined**: Superior performance across metrics

## Project Structure

```
gepa-langchain-lab/
├─ README.md              # Documentation (this file)
├─ requirements.txt       # Python dependencies
├─ .env.example           # Environment variable template
├─ .gitignore            # Git ignore rules
├─ src/
│  ├─ __init__.py         # Package marker
│  ├─ app.py              # Baseline RAG application with local retriever
│  ├─ eval.py             # Evaluation harness with test cases
│  ├─ ingest.py           # Simple keyword-based retriever (no external deps)
│  ├─ prompts.py          # System prompt templates
│  ├─ optimize.py         # GEPA prompt optimizer with variant generation
│  └─ optimize_mega.py    # MEGA workflow optimizer for routing/tools
├─ data/
│  └─ sample_docs.txt     # Sample knowledge base
├─ docs/
│  ├─ index.html          # GitHub Pages website
│  ├─ preview.png         # Social media preview card (1200x630px)
│  ├─ og-image.svg        # SVG architecture diagram
│  ├─ _config.yml         # Jekyll configuration
│  └─ .nojekyll           # GitHub Pages settings
└─ mlartifacts/           # MLflow experiment artifacts (local)
```

## Features

✨ **Zero External Dependencies for Retrieval** — Local keyword-based retriever works without embeddings APIs

🧠 **Dual Optimization** — Optimize both prompts (GEPA) and workflows (MEGA) in one framework

📊 **Built-in Evaluation** — Fixed eval set with ground truth answers for consistent measurement

🔄 **Local Development** — Run everything locally; no cloud services required

📈 **MLflow Integration** — Automatic tracing and experiment logging

🚀 **Production Ready** — Clean architecture suitable for fork and customization

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

Update the documents in `src/ingest.py`:

```python
# src/ingest.py - Replace DOCS list with your content
DOCS = [
    Document(page_content="Your document 1..."),
    Document(page_content="Your document 2..."),
    # ... add your documents
]
```

For production, integrate with a proper vector store:
```python
# Swap SimpleRetriever for FAISS, Pinecone, Weaviate, etc.
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(documents, embeddings)
return vectorstore.as_retriever(search_kwargs={"k": 3})
```

### 2. Customize Evaluation Set

Edit `EVAL_SET` in `src/eval.py` with your real test cases:

```python
EVAL_SET = [
    {
        "question": "Your question here?",
        "expected": "Your expected answer..."
    },
    # ... add more test cases
]
```

### 3. Change LLM Providers

Replace Groq with your preferred provider in `src/app.py`:

```python
# Option 1: OpenAI
from langchain_openai import ChatOpenAI
llm = ChatOpenAI(model="gpt-4o", temperature=0)

# Option 2: Anthropic
from langchain_anthropic import ChatAnthropic
llm = ChatAnthropic(model="claude-3-5-sonnet-20241022")

# Option 3: Keep Groq
from langchain_groq import ChatGroq
llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0)
```

### 4. Modify Prompts

Edit `BASE_SYSTEM_PROMPT` in `src/prompts.py`:

```python
BASE_SYSTEM_PROMPT = """You are a specialized assistant for your domain.
[Add domain-specific instructions]
Use the provided context to answer accurately.
[Add your custom rules]"""
```

### 5. Extend Workflow Optimization (MEGA)

Add custom workflow variants in `src/optimize_mega.py`:

```python
def generate_variants(self):
    # ... existing variants ...
    
    # Custom variant: my_strategy
    custom = {
        "name": "my_strategy",
        "blocks": {
            "retrieve": {"name": "Retriever", "enabled": True, "weight": 1.0},
            "generate": {"name": "Generator", "enabled": True, "weight": 1.0},
            "custom": {"name": "CustomBlock", "enabled": True, "weight": 0.5},
        },
        "routing": {
            "when_to_retrieve": "selective",
            "max_retrieval_docs": 2,
            "min_confidence": 0.8,
            "use_refinement": True,
        },
    }
    variants.append(custom)
    return variants
```

### 6. Add Production Integrations

**Schedule optimizations (macOS/Linux with cron):**
```bash
# Run GEPA every 6 hours
0 */6 * * * cd /path/to/gepa-langchain-lab && /path/to/.venv/bin/python -m src.optimize >> /var/log/gepa.log 2>&1

# Run MEGA after GEPA
30 */6 * * * cd /path/to/gepa-langchain-lab && /path/to/.venv/bin/python -m src.optimize_mega >> /var/log/mega.log 2>&1
```

**Windows Task Scheduler:**
- Create new task with program: `C:\path\to\.venv\Scripts\python.exe`
- Arguments: `-m src.optimize`
- Working directory: `C:\path\to\gepa-langchain-lab`
- Set desired schedule

**General production checklist:**
- Monitor MLflow UI at `http://localhost:5000`
- Persist optimized prompts and workflows
- Version control your eval sets
- Log optimization results for analysis
- Set up alerts for performance degradation

## Troubleshooting

### "ModuleNotFoundError: No module named 'src'"
**Solution:** Always use module syntax to run scripts:
```bash
python -m src.app      # ✓ Correct
python src/app.py      # ✗ Wrong
```

### "Missing GROQ_API_KEY"
**Solution:** Add your Groq API key to `.env`:
```bash
GROQ_API_KEY=your-actual-api-key-here
MLFLOW_TRACKING_URI=http://localhost:5000
```

Get your key at [console.groq.com](https://console.groq.com)

### MLflow UI not loading
**Solution:** Ensure MLflow is running in a separate terminal:
```bash
mlflow ui --host 0.0.0.0 --port 5000
```

Then visit `http://localhost:5000`

### Slow optimization runs
**Solution:** This is normal. The GEPA/MEGA optimizers evaluate multiple variants, which takes time. For faster demos, reduce `EVAL_SET` size in `src/eval.py`.

### Windows: Command not recognized
**Solution:** Make sure you're using the correct activation script:
- PowerShell: `.venv\Scripts\Activate.ps1`
- Command Prompt: `.venv\Scripts\activate.bat`

## Development Commands

### Run all tests quickly

**macOS/Linux:**
```bash
python -m src.eval && python -m src.optimize && python -m src.optimize_mega
```

**Windows:**
```powershell
python -m src.eval; python -m src.optimize; python -m src.optimize_mega
```

### View MLflow experiments

```bash
mlflow ui --host 0.0.0.0 --port 5000
```

Visit `http://localhost:5000` and explore:
- **Experiments**: Track different optimization runs
- **Runs**: View traces, parameters, and metrics
- **Models**: Compare registered prompts over time

### Clean up artifacts (macOS/Linux)

```bash
rm -rf mlruns/ mlartifacts/ .mlflow/
```

### Clean up artifacts (Windows)

```powershell
Remove-Item -Recurse -Force mlruns, mlartifacts, .mlflow
```

## Contributing

This is a boilerplate meant for forking. To customize:

1. Clone the repo
2. Update `src/ingest.py` with your data
3. Update `EVAL_SET` in `src/eval.py` with your test cases
4. Modify `BASE_SYSTEM_PROMPT` in `src/prompts.py`
5. Run optimization pipeline
6. Deploy optimized prompts

## Project Status

✅ **Fully Functional**
- Local keyword-based retriever (no external deps)
- GEPA prompt optimization with variants
- MEGA workflow optimization
- MLflow integration and tracing
- GitHub Pages website with social preview cards

## Resources

- [GEPA GitHub](https://github.com/gepa-ai/gepa)
- [LangChain Documentation](https://python.langchain.com/)
- [MLflow Documentation](https://mlflow.org/)
- [Groq API Console](https://console.groq.com/)
- [Groq + LangChain Integration](https://console.groq.com/docs/langchain)
- [GitHub Pages Setup](https://pages.github.com/)

## License

MIT - Feel free to fork and customize for your use case
