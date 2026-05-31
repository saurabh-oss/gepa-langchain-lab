"""GEPA prompt optimization loop."""

import os
import mlflow
from dotenv import load_dotenv
from mlflow.genai import optimize_prompts, register_prompt
from mlflow.genai.optimizers import GepaPromptOptimizer
from mlflow.genai.scorers import Correctness
from src.app import answer
from src.eval import EVAL_SET

load_dotenv()

mlflow.set_tracking_uri(
    os.getenv("MLFLOW_TRACKING_URI", "http://localhost:5000")
)
mlflow.set_experiment("gepa-langchain-video")


def predict_fn(inputs):
    """Prediction function that wraps the RAG copilot."""
    return {"output": answer(inputs["question"])}


if __name__ == "__main__":
    print("=" * 80)
    print("GEPA Prompt Optimization")
    print("=" * 80)
    print("\nRegistering prompt...")

    system_prompt = register_prompt(
        name="support-system-prompt",
        template="""You are a support copilot for a SaaS product.
Answer questions using only the provided context.
If the answer is not supported by the context, say you don't know.
Be concise, accurate, and helpful.
Cite relevant facts when appropriate."""
    )

    print(f"Registered prompt: {system_prompt.uri}")
    print("\nStarting optimization...")
    print("This may take 1-2 minutes...\n")

    result = optimize_prompts(
        predict_fn=predict_fn,
        train_data=[
            {"question": ex["question"], "answer": ex["expected"]}
            for ex in EVAL_SET
        ],
        prompt_uris=[system_prompt.uri],
        optimizer=GepaPromptOptimizer(reflection_model="openai:/gpt-4o"),
        scorers=[Correctness(model="openai:/gpt-4o")],
    )

    print("\n" + "=" * 80)
    print("Optimization Complete!")
    print("=" * 80)
    print(f"\nResult: {result}")
    print("\nNext: Re-run `python src/app.py` to see the optimized prompts in action.")
