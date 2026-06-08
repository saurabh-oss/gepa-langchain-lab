"""Evaluation harness for RAG applications.

This module provides utilities for evaluating RAG system performance.
For demo purposes, use demo.eval_set.SAMPLE_EVAL_SET.
For production, provide your own list of evaluation examples.
"""

from typing import List, Dict, Any, Optional
from src.app import answer


def run_eval(eval_set: Optional[List[Dict[str, str]]] = None) -> List[Dict[str, Any]]:
    """Run evaluation on an eval set.

    Args:
        eval_set: List of dicts with 'question' and 'expected' keys.
                 If None, loads demo eval set.

    Returns:
        List of results with id, question, expected, prediction.

    Example:
        from demo.eval_set import SAMPLE_EVAL_SET
        results = run_eval(SAMPLE_EVAL_SET)
    """
    if eval_set is None:
        try:
            from demo.eval_set import SAMPLE_EVAL_SET
            eval_set = SAMPLE_EVAL_SET
        except ImportError:
            raise ValueError(
                "No eval set provided. "
                "Either pass eval_set to run_eval() or ensure demo module is available."
            )

    results = []
    for i, ex in enumerate(eval_set, 1):
        pred = answer(ex["question"])
        results.append({
            "id": i,
            "question": ex["question"],
            "expected": ex["expected"],
            "prediction": pred,
        })
    return results


# For backwards compatibility and demo convenience
try:
    from demo.eval_set import SAMPLE_EVAL_SET as EVAL_SET
except ImportError:
    EVAL_SET = []
