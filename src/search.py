import os
from dotenv import load_dotenv
# Import the new, free-tier LLM provider (Gemini)
from langchain_google_genai import ChatGoogleGenerativeAI 
# Using relative imports for modules within the src package
from .vectorstore import FaissVectorStore
from .data_loader import load_all_documents 

load_dotenv()

class RAGSearch:
    def __init__(self, persist_dir: str = "faiss_store", embedding_model: str = "all-MiniLM-L6-v2", llm_model: str = "gemini-2.5-flash"):
        
        # 1. Initialize Vector Store
        self.vectorstore = FaissVectorStore(persist_dir, embedding_model)
        
        # Load or build vectorstore
        faiss_path = os.path.join(persist_dir, "faiss.index")
        meta_path = os.path.join(persist_dir, "metadata.pkl")
        
        if not (os.path.exists(faiss_path) and os.path.exists(meta_path)):
            # load_all_documents is imported at the top of the file, removed redundant internal import
            docs = load_all_documents("data")
            self.vectorstore.build_from_documents(docs)
        else:
            self.vectorstore.load()
            
        # 2. Initialize Gemini LLM
        # Fetch the API key from the environment variable GEMINI_API_KEY
        google_api_key = os.getenv("GEMINI_API_KEY") 
        
        if not google_api_key:
            raise ValueError("GEMINI_API_KEY environment variable not set. Please create one.")
            
        self.llm = ChatGoogleGenerativeAI(
            model=llm_model, 
            google_api_key=google_api_key
        )
        print(f"[INFO] Gemini LLM initialized: {llm_model}")

    def search_and_summarize(self, query: str, top_k: int = 5) -> str:
        # 1. Retrieval
        results = self.vectorstore.query(query, top_k=top_k)
        texts = [r["metadata"].get("text", "") for r in results if r["metadata"]]
        context = "\n\n".join(texts)
        
        if not context:
            return "No relevant documents found."
        
        # 2. Augmentation and Generation
        prompt = f"""Summarize the following context for the query: '{query}'\n\nContext:\n{context}\n\nSummary:"""
        
        # The invoke method sends the prompt to the Gemini model
        response = self.llm.invoke(prompt)
        
        return response.content

# Example usage
if __name__ == "__main__":
    try:
        rag_search = RAGSearch()
        query = "What are Artificial Intelligence?"
        summary = rag_search.search_and_summarize(query, top_k=3)
        print("\nQuery:", query)
        print("\nSummary:", summary)
    except ValueError as e:
        print(f"ERROR: {e}")


