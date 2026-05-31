"""Vector store ingestion and setup."""

import os
from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

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


def build_vectorstore():
    """Create and return a FAISS vector store from sample documents."""
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=50
    )
    chunks = splitter.split_documents(DOCS)
    embeddings = OpenAIEmbeddings()
    return FAISS.from_documents(chunks, embeddings)
