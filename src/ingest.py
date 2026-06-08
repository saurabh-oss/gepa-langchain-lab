"""Retriever implementation for RAG applications.

This module provides a configurable retriever that works with custom documents.
For demo purposes, use demo.sample_data.SAMPLE_DOCUMENTS.
For production, provide your own list of Document objects.
"""

from typing import List, Optional
from langchain_core.documents import Document
from langchain_core.retrievers import BaseRetriever
from langchain_core.callbacks.manager import CallbackManagerForRetrieverRun


def build_retriever(documents: Optional[List[Document]] = None) -> BaseRetriever:
    """Build a retriever from documents.

    Args:
        documents: List of LangChain Document objects. If None, uses demo data.

    Returns:
        A SimpleRetriever instance.

    Example:
        from demo.sample_data import SAMPLE_DOCUMENTS
        retriever = build_retriever(SAMPLE_DOCUMENTS)
    """
    if documents is None:
        # For backwards compatibility with demo, try to load sample data
        try:
            from demo.sample_data import SAMPLE_DOCUMENTS
            documents = SAMPLE_DOCUMENTS
        except ImportError:
            raise ValueError(
                "No documents provided. "
                "Either pass documents to build_retriever() or ensure demo module is available."
            )

    return SimpleRetriever(documents=documents)


class SimpleRetriever(BaseRetriever):
    """Simple keyword-based retriever for RAG applications.

    This retriever matches documents based on keyword overlap with the query.
    For production use, integrate with FAISS, Pinecone, or other vector stores.
    """

    documents: List[Document]

    class Config:
        arbitrary_types_allowed = True

    def _get_relevant_documents(self, query: str, *, run_manager: CallbackManagerForRetrieverRun = None):
        """Retrieve documents based on keyword matching."""
        query_lower = query.lower()
        results = []
        for doc in self.documents:
            content_lower = doc.page_content.lower()
            # Simple keyword matching
            if any(word in content_lower for word in query_lower.split()):
                results.append(doc)
        # Return all docs if no matches found (fallback)
        return results if results else self.documents[:3]


def build_vectorstore(documents: Optional[List[Document]] = None):
    """Create and return a retriever. Alias for build_retriever()."""
    return build_retriever(documents)
