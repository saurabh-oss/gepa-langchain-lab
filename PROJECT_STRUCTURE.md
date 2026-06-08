# Project Structure

This document explains the organization of the GEPA + LangChain boilerplate.

## Directory Layout

```
gepa-langchain-lab/
├── src/                          # Production code
│   ├── __init__.py
│   ├── app.py                    # Main RAG application (core logic)
│   ├── ingest.py                 # Retriever implementation
│   ├── eval.py                   # Evaluation utilities
│   ├── optimize.py               # GEPA prompt optimizer
│   ├── optimize_mega.py          # MEGA workflow optimizer
│   └── prompts.py                # Prompt templates
│
├── demo/                          # Demo & sample materials
│   ├── __init__.py
│   ├── sample_data.py            # 8 sample documents
│   ├── eval_set.py               # 8 test questions
│   ├── benchmark.py              # Benchmark tool
│   └── README.md                 # Demo instructions
│
├── docs/                          # GitHub Pages website
│   ├── index.html
│   ├── preview.png
│   ├── og-image.svg
│   ├── _config.yml
│   └── .nojekyll
│
├── data/                          # Optional: local data files
│   └── sample_docs.txt
│
├── README.md                      # Main documentation
├── PROJECT_STRUCTURE.md           # This file
├── requirements.txt               # Python dependencies
└── .env.example                   # Environment template
```

## Code Organization

### `/src` — Production Code

The `src/` directory contains the core boilerplate that you'll use in production.

**Key files:**
- **app.py** — Main RAG application. Use this as your foundation.
- **ingest.py** — `build_retriever(documents)` function. Pass your own documents.
- **eval.py** — `run_eval(eval_set)` function. Pass your own evaluation examples.
- **optimize.py** — GEPA prompt optimization. Works with any eval set.
- **optimize_mega.py** — MEGA workflow optimization. Works with any eval set.
- **prompts.py** — Prompt templates. Customize for your domain.

**No demo data in `/src`** — All sample data is in `/demo`.

### `/demo` — Demo & Learning Materials

The `demo/` directory contains everything needed to understand and run the optimization pipeline.

**Key files:**
- **sample_data.py** — 8 realistic documents (SaaS support domain).
- **eval_set.py** — 8 test questions with expected answers.
- **benchmark.py** — Tool to measure baseline performance before optimization.
- **README.md** — Instructions for running the demo.

**How to use:**
1. Understand the demo by running it with sample data
2. Replace `sample_data.py` and `eval_set.py` with your own
3. Run the optimization pipeline on your data

## Workflow

### Running the Demo (with sample data)

```bash
# 1. See baseline performance
python -m demo.benchmark

# 2. Optimize prompts
python -m src.optimize

# 3. Optimize workflows
python -m src.optimize_mega

# 4. Test improvements
python -m src.app
```

### Running on Production Data

```python
# 1. Replace demo data with your own
from my_data import MY_DOCUMENTS, MY_EVAL_SET

# 2. Build retriever with your documents
from src.ingest import build_retriever
retriever = build_retriever(MY_DOCUMENTS)

# 3. Run evaluation
from src.eval import run_eval
results = run_eval(MY_EVAL_SET)

# 4. Optimize
python -m src.optimize  # Uses MY_EVAL_SET
python -m src.optimize_mega  # Uses MY_EVAL_SET
```

## Key Design Principles

1. **Separation of Concerns**
   - `/src` = Production boilerplate (no sample data)
   - `/demo` = Learning materials and sample data
   - `/docs` = Website

2. **Configuration Over Convention**
   - Functions accept parameters (e.g., `build_retriever(documents)`)
   - No hardcoded paths or data
   - Easy to swap implementations

3. **Production Ready**
   - No demo clutter in main codebase
   - Clear interfaces for integration
   - Minimal dependencies

4. **Demo First Learning**
   - Run demo to understand the system
   - Then adapt for your use case
   - Complete example provided

## Customization Guide

### Step 1: Understand the Demo
```bash
cd /repo
python -m demo.benchmark  # See what you're optimizing
```

### Step 2: Prepare Your Data
```python
# my_data.py
from langchain_core.documents import Document

MY_DOCUMENTS = [
    Document(page_content="Your content here..."),
    # ... more documents
]

MY_EVAL_SET = [
    {"question": "Q1", "expected": "Expected answer"},
    # ... more test cases
]
```

### Step 3: Run Optimization
```bash
# The optimizer will use your data
python -m src.optimize      # GEPA
python -m src.optimize_mega # MEGA
```

### Step 4: Deploy
```python
# production.py
from src.app import answer
from my_data import MY_DOCUMENTS
from src.ingest import build_retriever

retriever = build_retriever(MY_DOCUMENTS)
# ... deploy answer() function
```

## File Dependencies

```
src/app.py
  ├── src/ingest.py → build_retriever(documents)
  ├── src/prompts.py → BASE_SYSTEM_PROMPT
  └── demo/sample_data.py (for demo, not required)

src/optimize.py
  ├── src/app.py → answer()
  ├── src/eval.py → run_eval()
  ├── src/prompts.py → prompt variants
  └── demo/eval_set.py (for demo, not required)

demo/benchmark.py
  ├── src/app.py → answer()
  ├── demo/eval_set.py → SAMPLE_EVAL_SET
  └── src/prompts.py
```

## Extending the Boilerplate

### Add Custom Retriever
```python
# src/custom_retriever.py
from src.ingest import build_retriever as build_simple

class VectorStoreRetriever:
    def __init__(self, index):
        self.index = index
    
    def invoke(self, query):
        # Custom retrieval logic
        pass
```

### Add Custom Optimizer
```python
# src/custom_optimizer.py
class MyOptimizer:
    def optimize(self, eval_set):
        # Your optimization logic
        pass
```

### Add Custom Metrics
```python
# src/metrics.py
def custom_score(expected, predicted):
    # Your scoring logic
    pass
```

## Summary

- **Use `/src` for production** — Clean, configurable code
- **Use `/demo` to learn** — Runnable example with sample data
- **Customize at the `/src` level** — Keep demo separate
- **Deploy from `/src`** — Not from `/demo`
