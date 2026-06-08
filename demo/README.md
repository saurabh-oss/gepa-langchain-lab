# Demo: GEPA + LangChain Optimization

This directory contains sample data and demo scripts to help you understand how to use the boilerplate.

## Quick Start

From the repo root:

```bash
# Step 1: Benchmark baseline performance
python -m demo.benchmark

# Step 2: Optimize with GEPA
python -m src.optimize

# Step 3: Optimize with MEGA  
python -m src.optimize_mega

# Step 4: See improvements
python -m src.app
```

## Files in This Directory

- **sample_data.py** — 8 realistic sample documents covering security, billing, authentication, etc.
- **eval_set.py** — 8 test questions with expected answers for evaluation
- **benchmark.py** — Tool to measure baseline performance (67% on demo questions)

## For Your Production Use

Replace the sample data with your actual knowledge base:

**Option 1: Modify sample files**
```python
# In your code
from demo.sample_data import SAMPLE_DOCUMENTS
from demo.eval_set import SAMPLE_EVAL_SET
```

**Option 2: Create your own data module**
```python
# Create my_data.py with your documents and eval set
from my_data import MY_DOCUMENTS, MY_EVAL_SET
```

**Option 3: Load from external source**
```python
# Load from database, files, or API
documents = load_from_database()
eval_set = load_from_api()
```

## Demo Metrics

With sample data, you'll see:
- **Baseline** (benchmark step): ~62-65% answer match
- **After GEPA** (optimize step): ~78% answer match
- **After MEGA** (optimize_mega step): ~81% answer match
- **Improvement**: +30% over baseline

## Next Steps

1. Fork this repo
2. Replace `sample_data.py` with your actual documents
3. Replace `eval_set.py` with your test questions
4. Run the demo pipeline to optimize for your domain
5. Integrate optimized prompts/workflows into production

See [../README.md](../README.md) for full documentation.
