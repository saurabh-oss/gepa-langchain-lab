"""Evaluation harness for the RAG copilot."""

from src.app import answer

EVAL_SET = [
    {
        "question": "How do I reset my password?",
        "expected": "Settings > Security > Reset Password"
    },
    {
        "question": "How long are API keys valid?",
        "expected": "90 days"
    },
    {
        "question": "Can I get a refund after 20 days?",
        "expected": "14 days"
    },
    {
        "question": "Is SSO available for all plans?",
        "expected": "Enterprise plans only"
    },
]


def run_eval():
    """Run evaluation on the fixed eval set."""
    results = []
    for i, ex in enumerate(EVAL_SET, 1):
        pred = answer(ex["question"])
        results.append({
            "id": i,
            "question": ex["question"],
            "expected": ex["expected"],
            "prediction": pred,
        })
    return results


if __name__ == "__main__":
    print("=" * 80)
    print("Running Evaluation Set")
    print("=" * 80)

    results = run_eval()
    for row in results:
        print(f"\n[Q{row['id']}] {row['question']}")
        print(f"Expected: {row['expected']}")
        print(f"Predicted: {row['prediction']}")
        print("-" * 80)

    print(f"\nEvaluated {len(results)} questions.")
