import numpy as np
from sentence_transformers import SentenceTransformer
from langchain.text_splitter import RecursiveCharacterTextSplitter
import faiss

# Global embedding model (load once)
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")


def build_vector_store(doc_text: str):
    """
    Converts raw document text into FAISS vector store
    """

    # Step 1: Chunking
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150
    )

    chunks = splitter.split_text(doc_text)

    if not chunks:
        raise ValueError("No chunks created from document")

    # Step 2: Embeddings
    embeddings = embedding_model.encode(chunks)

    embeddings = np.array(embeddings).astype("float32")

    # Step 3: FAISS index
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)

    # Store chunks alongside
    return {
        "index": index,
        "chunks": chunks
    }


def retrieve_context(vectorstore, query: str, top_k: int = 5):
    """
    Retrieves top-k relevant chunks for a query
    """

    query_embedding = embedding_model.encode([query]).astype("float32")

    index = vectorstore["index"]
    chunks = vectorstore["chunks"]

    distances, indices = index.search(query_embedding, top_k)

    retrieved_chunks = []
    for idx in indices[0]:
        if idx < len(chunks):
            retrieved_chunks.append(chunks[idx])

    return "\n\n".join(retrieved_chunks)
