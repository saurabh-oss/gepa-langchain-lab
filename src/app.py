"""Baseline LangChain RAG support copilot."""

import os
import mlflow
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from src.ingest import build_vectorstore
from src.prompts import BASE_SYSTEM_PROMPT

load_dotenv()

mlflow.set_tracking_uri(
    os.getenv("MLFLOW_TRACKING_URI", "http://localhost:5000")
)
mlflow.set_experiment("gepa-langchain-video")
mlflow.langchain.autolog()

retriever = build_vectorstore()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0,
    groq_api_key=os.getenv("GROQ_API_KEY"),
)

prompt = ChatPromptTemplate.from_messages([
    ("system", BASE_SYSTEM_PROMPT),
    ("human", "Question: {question}\n\nContext:\n{context}")
])


def retrieve_context(question: str) -> str:
    """Retrieve relevant context from the vector store."""
    docs = retriever.invoke(question)
    return "\n\n".join(d.page_content for d in docs)


def answer(question: str) -> str:
    """Answer a question using retrieval + generation."""
    context = retrieve_context(question)
    messages = prompt.format_messages(question=question, context=context)
    return llm.invoke(messages).content


if __name__ == "__main__":
    print("=" * 80)
    print("LangChain RAG Support Copilot")
    print("Type 'exit' or 'quit' to stop")
    print("=" * 80)

    while True:
        q = input("\nQuestion: ").strip()
        if q.lower() in {"exit", "quit"}:
            print("Goodbye!")
            break
        if not q:
            continue
        print(f"\nAnswer: {answer(q)}\n")
        print("-" * 80)
