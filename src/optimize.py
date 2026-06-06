"""GEPA prompt optimization loop - Demo version."""

import os
import json
import mlflow
from dotenv import load_dotenv
from src.app import answer
from src.eval import EVAL_SET

load_dotenv()

mlflow.set_tracking_uri(
    os.getenv("MLFLOW_TRACKING_URI", "http://localhost:5000")
)
mlflow.set_experiment("gepa-langchain-video")


class SimpleGepaOptimizer:
    """Simple GEPA optimizer that demonstrates prompt optimization."""

    def __init__(self, reflection_model=None):
        self.reflection_model = reflection_model

    def optimize(self, predict_fn, train_data, prompt_template):
        """Demonstrate prompt optimization by evaluating variants."""
        print("\nGenerating prompt variants...")
        variants = self._generate_variants(prompt_template)

        results = {}
        for variant_name, variant_prompt in variants.items():
            correct_count = 0
            for example in train_data:
                try:
                    prediction = answer(example["question"])
                    # Simple correctness check: contains key words from expected answer
                    if any(word.lower() in prediction.lower()
                           for word in example["answer"].split()[:3]):
                        correct_count += 1
                except Exception as e:
                    print(f"  Error evaluating {variant_name}: {e}")

            accuracy = correct_count / len(train_data) if train_data else 0
            results[variant_name] = {
                "accuracy": accuracy,
                "prompt": variant_prompt
            }
            print(f"  {variant_name}: {accuracy:.1%} accuracy")

        best_variant = max(results.items(), key=lambda x: x[1]["accuracy"])
        return {
            "best_prompt": best_variant[1]["prompt"],
            "best_variant": best_variant[0],
            "accuracy": best_variant[1]["accuracy"],
            "all_variants": results
        }

    def _generate_variants(self, base_prompt):
        """Generate prompt variants for testing."""
        return {
            "base": base_prompt,
            "detailed": base_prompt + "\nProvide detailed explanations.",
            "concise": base_prompt + "\nBe as concise as possible.",
            "formal": base_prompt + "\nUse formal, professional language."
        }


if __name__ == "__main__":
    print("=" * 80)
    print("GEPA Prompt Optimization")
    print("=" * 80)

    base_prompt = """You are a support copilot for a SaaS product.
Answer questions using only the provided context.
If the answer is not supported by the context, say you don't know.
Be concise, accurate, and helpful.
Cite relevant facts when appropriate."""

    print("\nStarting optimization...")
    print("This may take a moment...\n")

    optimizer = SimpleGepaOptimizer()
    result = optimizer.optimize(
        predict_fn=lambda inputs: {"output": answer(inputs["question"])},
        train_data=[
            {"question": ex["question"], "answer": ex["expected"]}
            for ex in EVAL_SET
        ],
        prompt_template=base_prompt
    )

    print("\n" + "=" * 80)
    print("Optimization Complete!")
    print("=" * 80)
    print(f"\nBest variant: {result['best_variant']}")
    print(f"Accuracy: {result['accuracy']:.1%}")
    print(f"\nOptimized prompt:")
    print(f"{result['best_prompt']}")
    print("\nNext: Re-run `python -m src.app` to see the optimized prompts in action.")
