"""Vector store ingestion and setup."""

from langchain_core.documents import Document
from langchain_core.retrievers import BaseRetriever
from langchain_core.callbacks.manager import CallbackManagerForRetrieverRun

DOCS = [
    Document(
        page_content="Reset password: Go to Settings > Security > Reset Password."
    ),
    Document(
        page_content="API keys expire every 90 days and must be rotated manually."
    ),
    Document(
        page_content="Refunds are available within 14 days for annual plans."
    ),
    Document(
        page_content="SSO is available on Enterprise plans only."
    ),
    Document(
        page_content="Webhook retries happen 5 times with exponential backoff."
    ),
]


class SimpleRetriever(BaseRetriever):
    """Simple keyword-based retriever for demo purposes."""

    def _get_relevant_documents(self, query: str, *, run_manager: CallbackManagerForRetrieverRun = None):
        """Retrieve documents based on keyword matching."""
        query_lower = query.lower()
        results = []
        for doc in DOCS:
            content_lower = doc.page_content.lower()
            # Simple keyword matching
            if any(word in content_lower for word in query_lower.split()):
                results.append(doc)
        # Return all docs if no matches found (fallback)
        return results if results else DOCS[:3]


def build_vectorstore():
    """Create and return a simple retriever for demo purposes."""
    return SimpleRetriever()
