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

### Run the Demo Pipeline

The fastest way to see the optimization system in action is with the included sample data:

**Step 1: Measure Baseline Performance**

**macOS/Linux:**
```bash
python -m demo.benchmark
```

**Windows:**
```powershell
python -m demo.benchmark
```

This shows baseline performance on 8 realistic test cases. You'll see ~62-65% answer match score, room for improvement.

**Step 2: Optimize Prompts with GEPA**

**macOS/Linux:**
```bash
python -m src.optimize
```

**Windows:**
```powershell
python -m src.optimize
```

GEPA will:
1. Generate prompt variants (base, detailed, concise, formal)
2. Evaluate each on the demo eval set
3. Select and register the best variant
4. Return detailed metrics (~1-2 minutes)

Expected result: ~78% answer match score.

**Step 3: (Optional) Optimize Workflow with MEGA**

**macOS/Linux:**
```bash
python -m src.optimize_mega
```

**Windows:**
```powershell
python -m src.optimize_mega
```

MEGA will:
1. Generate workflow variants (high_retrieval, with_refinement, reasoning_heavy, balanced)
2. Evaluate each on the demo eval set
3. Select the best workflow configuration
4. Return block-level performance scores (~2-3 minutes)

Expected result: ~81% answer match score (additional +3% over GEPA alone).

**Step 4: See Results in Action**

**macOS/Linux:**
```bash
python -m src.app
```

**Windows:**
```powershell
python -m src.app
```

Interactive demo. Ask questions and see improvements:
- More accurate answers
- Better grounding in documents
- Improved routing decisions (if MEGA was run)

Example questions to try:
- "How do I reset my password?"
- "What's your refund policy?"
- "Which authentication methods are available?"

**Full improvement flow: 62% → 81% (+30% over baseline)**

### Using Your Own Data

Once you understand the system with the demo, replace the sample data:

1. **Prepare your documents:**
   ```python
   # my_data.py
   from langchain_core.documents import Document
   
   MY_DOCUMENTS = [
       Document(page_content="Your document 1..."),
       Document(page_content="Your document 2..."),
       # ... more documents
   ]
   ```

2. **Prepare your evaluation set:**
   ```python
   MY_EVAL_SET = [
       {"question": "Q1", "expected": "Expected answer 1"},
       {"question": "Q2", "expected": "Expected answer 2"},
       # ... more test cases
   ]
   ```

3. **Run optimization on your data:**
   ```python
   from src.ingest import build_retriever
   from src.eval import run_eval
   from my_data import MY_DOCUMENTS, MY_EVAL_SET
   
   # Build retriever with your documents
   retriever = build_retriever(MY_DOCUMENTS)
   
   # Run evaluation
   results = run_eval(MY_EVAL_SET)
   
   # Then run optimization
   # python -m src.optimize
   # python -m src.optimize_mega
   ```

## Project Structure

```
gepa-langchain-lab/
├── src/                          # Production code (no sample data)
│   ├── __init__.py
│   ├── app.py                    # Main RAG application (core logic)
│   ├── ingest.py                 # Configurable retriever (accepts documents)
│   ├── eval.py                   # Configurable evaluation (accepts eval set)
│   ├── optimize.py               # GEPA prompt optimizer
│   ├── optimize_mega.py          # MEGA workflow optimizer
│   └── prompts.py                # Prompt templates
│
├── demo/                         # Demo & learning materials
│   ├── __init__.py
│   ├── sample_data.py            # 8 realistic sample documents
│   ├── eval_set.py               # 8 test questions with expected answers
│   ├── benchmark.py              # Baseline measurement tool
│   └── README.md                 # Demo quick start guide
│
├── docs/                         # GitHub Pages website
│   ├── index.html
│   ├── preview.png
│   ├── og-image.svg
│   ├── _config.yml
│   └── .nojekyll
│
├── README.md                     # Main documentation (this file)
├── requirements.txt              # Python dependencies
├── .env.example                  # Environment variable template
└── .gitignore                    # Git ignore rules
```

### Code Organization

**`/src` — Production Code**

The `src/` directory contains the core boilerplate with no sample data. Use this in production:

- **app.py** — Main RAG application. Your entry point.
- **ingest.py** — `build_retriever(documents)` function. Pass your own documents.
- **eval.py** — `run_eval(eval_set)` function. Pass your own evaluation set.
- **optimize.py** — GEPA prompt optimization. Works with any eval set.
- **optimize_mega.py** — MEGA workflow optimization. Works with any eval set.
- **prompts.py** — Prompt templates. Customize for your domain.

**`/demo` — Demo & Learning Materials**

The `demo/` directory shows how to use the system with realistic sample data:

- **sample_data.py** — 8 realistic documents (SaaS support domain).
- **eval_set.py** — 8 test questions with expected answers.
- **benchmark.py** — Baseline performance measurement tool.
- **README.md** — Demo-specific instructions.

**Key Design Principles:**
1. **Separation of Concerns** — `/src` is pure boilerplate; `/demo` is learning material
2. **Configuration Over Convention** — Functions accept parameters, no hardcoded data
3. **Production Ready** — Clean codebase, minimal dependencies, easy to fork

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

### 1. Prepare Your Data

Create a data module with your documents and evaluation set:

```python
# my_data.py
from langchain_core.documents import Document

MY_DOCUMENTS = [
    Document(page_content="Your content about topic 1"),
    Document(page_content="Your content about topic 2"),
    # ... add all your documents
]

MY_EVAL_SET = [
    {
        "question": "What is your policy on X?",
        "expected": "The expected answer that the assistant should give"
    },
    {
        "question": "How do I do Y?",
        "expected": "Step-by-step instructions for Y"
    },
    # ... add comprehensive test cases
]
```

Good eval sets have 8-20 questions covering all major topics.

### 2. Run Optimization on Your Data

Pass your data to the optimization functions:

```python
from src.ingest import build_retriever
from src.eval import run_eval
from my_data import MY_DOCUMENTS, MY_EVAL_SET

# Option A: Build retriever and evaluate
retriever = build_retriever(MY_DOCUMENTS)
results = run_eval(MY_EVAL_SET)

# Option B: Run optimization programmatically
from src.optimize import GEPAOptimizer

optimizer = GEPAOptimizer()
best_prompt = optimizer.optimize(MY_EVAL_SET)
```

Or use command-line (modifies `demo/eval_set.py` to use your data temporarily):

```bash
python -m src.optimize    # Tests GEPA variants
python -m src.optimize_mega  # Tests MEGA variants
python -m src.app  # See results interactively
```

### 3. Integrate with Vector Store (Production)

Replace the simple keyword-based retriever with a vector store:

```python
# src/ingest.py - modify build_retriever()
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

def build_retriever(documents=None):
    if documents is None:
        from demo.sample_data import SAMPLE_DOCUMENTS
        documents = SAMPLE_DOCUMENTS
    
    # Use vector embeddings instead of keyword matching
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(documents, embeddings)
    return vectorstore.as_retriever(search_kwargs={"k": 3})
```

Supported options: FAISS, Pinecone, Weaviate, Chroma, Milvus, etc.

### 4. Customize System Prompt

Edit `BASE_SYSTEM_PROMPT` in `src/prompts.py` for your domain:

```python
BASE_SYSTEM_PROMPT = """You are a specialized customer support assistant.
Your role is to help users with account management, billing, and technical issues.
Always cite the relevant documentation section when answering.
Be concise but thorough. Use a friendly, professional tone."""
```

GEPA will automatically create variants of this prompt during optimization.

### 5. Change LLM Providers

Replace Groq in `src/app.py` if desired:

```python
# Option 1: OpenAI
from langchain_openai import ChatOpenAI
llm = ChatOpenAI(model="gpt-4o", temperature=0)

# Option 2: Anthropic Claude
from langchain_anthropic import ChatAnthropic
llm = ChatAnthropic(model="claude-opus-4-1", temperature=0)

# Option 3: Keep Groq (fast and free tier)
from langchain_groq import ChatGroq
llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0)
```

### 6. Schedule Regular Optimization (Production)

**macOS/Linux with cron:**
```bash
# Run GEPA every 6 hours
0 */6 * * * cd /path/to/repo && /path/to/.venv/bin/python -m src.optimize >> /var/log/gepa.log 2>&1

# Run MEGA every 12 hours
0 */12 * * * cd /path/to/repo && /path/to/.venv/bin/python -m src.optimize_mega >> /var/log/mega.log 2>&1
```

**Windows Task Scheduler:**
1. Press `Win + R`, type `taskschd.msc`
2. Right-click "Task Scheduler" → New Task
3. Set program: `C:\path\to\.venv\Scripts\python.exe`
4. Set arguments: `-m src.optimize`
5. Set working directory: `C:\path\to\gepa-langchain-lab`
6. Set schedule (e.g., every 6 hours)

**Production checklist:**
- Version control your eval sets (for reproducibility)
- Monitor MLflow UI at `http://localhost:5000`
- Log optimization metrics over time
- Set alerts if performance degrades
- Review optimized prompts before deployment

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
