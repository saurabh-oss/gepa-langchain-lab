"""Benchmark and comparison tool for optimization improvements.

Run this after GEPA optimization to see before/after results side-by-side.
"""

import os
from dotenv import load_dotenv
from src.app import answer
from src.eval import EVAL_SET
from src.prompts import BASE_SYSTEM_PROMPT

load_dotenv()


def score_answer(expected: str, predicted: str) -> float:
    """Simple relevance scoring: how many expected keywords appear in prediction."""
    expected_words = set(w.lower() for w in expected.split() if len(w) > 3)
    predicted_lower = predicted.lower()

    matches = sum(1 for word in expected_words if word in predicted_lower)
    return matches / len(expected_words) if expected_words else 0.0


def run_benchmark():
    """Run benchmark on all eval questions and show results."""
    print("=" * 100)
    print("BENCHMARK: Baseline Performance".center(100))
    print("=" * 100)
    print("\nEvaluating on 8 comprehensive test cases...\n")

    results = []
    total_score = 0.0

    for i, example in enumerate(EVAL_SET, 1):
        question = example["question"]
        expected = example["expected"]

        try:
            predicted = answer(question)
            score = score_answer(expected, predicted)
            total_score += score

            results.append({
                "id": i,
                "question": question,
                "expected": expected,
                "predicted": predicted,
                "score": score
            })

            print(f"\n[Q{i}] {question}")
            print("-" * 100)
            print(f"Expected Knowledge: {expected[:80]}...")
            print(f"Got: {predicted[:80]}...")
            print(f"Match Score: {score:.0%} {'✓ Good' if score >= 0.7 else '✗ Needs improvement'}")

        except Exception as e:
            print(f"\n[Q{i}] {question}")
            print(f"ERROR: {e}")
            results.append({
                "id": i,
                "question": question,
                "expected": expected,
                "predicted": f"ERROR: {e}",
                "score": 0.0
            })
            total_score += 0.0

    # Summary
    avg_score = total_score / len(EVAL_SET)

    print("\n" + "=" * 100)
    print("SUMMARY".center(100))
    print("=" * 100)
    print(f"\nAverage Match Score: {avg_score:.0%}")
    print(f"Questions with >70% match: {sum(1 for r in results if r['score'] >= 0.7)}/{len(EVAL_SET)}")
    print("\n" + "=" * 100)
    print("INTERPRETATION".center(100))
    print("=" * 100)

    if avg_score >= 0.8:
        print("\n✓ EXCELLENT: Baseline is performing very well!")
    elif avg_score >= 0.6:
        print("\n⚠ GOOD: Baseline is decent but has room for improvement.")
        print("  Run GEPA optimization to improve answer quality and relevance.")
    else:
        print("\n✗ NEEDS IMPROVEMENT: Baseline could be much better.")
        print("  GEPA optimization should show clear improvements.")

    print("\nNext Steps:")
    print("1. Run: python -m src.optimize")
    print("2. This will test prompt variants and select the best one")
    print("3. Then re-run this benchmark to see improvements")
    print("=" * 100)

    return {
        "avg_score": avg_score,
        "results": results,
        "total_questions": len(EVAL_SET),
    }


def compare_prompts():
    """Compare different prompt variants on a sample question."""
    from src.prompts import (
        BASE_SYSTEM_PROMPT, STRICT_PROMPT, DETAILED_PROMPT, CONVERSATIONAL_PROMPT
    )

    print("\n" + "=" * 100)
    print("PROMPT VARIANT COMPARISON".center(100))
    print("=" * 100)

    if not EVAL_SET:
        print("No eval set available")
        return

    sample_q = EVAL_SET[0]["question"]

    print(f"\nQuestion: {sample_q}")
    print("-" * 100)

    prompts = {
        "Base (Current)": BASE_SYSTEM_PROMPT,
        "Strict (Minimal)": STRICT_PROMPT,
        "Detailed (Thorough)": DETAILED_PROMPT,
        "Conversational (Friendly)": CONVERSATIONAL_PROMPT,
    }

    print("\nPrompt Strategies (what will be tested):\n")
    for name, prompt in prompts.items():
        print(f"\n📋 {name}:")
        print(f"   {prompt[:120]}...")

    print("\n" + "-" * 100)
    print("Note: GEPA will test these variants and select the best for your eval set")
    print("=" * 100)


if __name__ == "__main__":
    print("\n")
    print("╔" + "═" * 98 + "╗")
    print("║" + "GEPA + LangChain BENCHMARK TOOL".center(98) + "║")
    print("║" + "Measure baseline performance before optimization".center(98) + "║")
    print("╚" + "═" * 98 + "╝")

    result = run_benchmark()
    compare_prompts()

    print("\n💡 TIP: After running python -m src.optimize, the prompts will be tested")
    print("   and the best one will be selected automatically.")
    print("\nTo see the optimized prompt in action, run: python -m src.app")
