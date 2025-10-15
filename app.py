import os
import io
import pandas as pd
import json
from pdfminer.high_level import extract_text_to_fp
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

# --- LLM CLIENT IMPORTS ---
from google import genai 
from google.genai.errors import APIError

load_dotenv()

# --- FLASK APP INITIALIZATION (FIXED) ---
app = Flask(__name__) # <--- FIX: Initialize the Flask app here
CORS(app)

# 1. Configuration (Stored Securely on the Server)
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
LLM_MODEL = "gemini-2.5-flash" 

if not GEMINI_API_KEY:
    # Use standard logging or print for non-web errors
    print("FATAL ERROR: GEMINI_API_KEY environment variable not set in .env file.")
    # We won't raise the error yet to allow the server to start for easier debugging
    client = None
else:
    # Initialize the Gemini Client once
    try:
        client = genai.Client(api_key=GEMINI_API_KEY)
        print(f"Gemini Client initialized using model: {LLM_MODEL}")
    except Exception as e:
        print(f"Error initializing Gemini client: {e}")
        client = None

# --- FILE PARSING UTILITY ---

def extract_text_from_file(file):
    """Extracts text from PDF, CSV, or XLSX file streams."""
    filename = file.filename.lower()
    # Read file content into a memory buffer
    file_stream = io.BytesIO(file.read()) 
    
    try:
        if filename.endswith('.pdf'):
            output_string = io.StringIO()
            # pdfminer.six extracts text from the stream
            extract_text_to_fp(file_stream, output_string)
            return output_string.getvalue()

        elif filename.endswith('.csv'):
            # Use pandas to read CSV (assumes basic formatting)
            df = pd.read_csv(file_stream)
            # Convert the entire DataFrame to a single string for RAG
            return df.to_string(index=False)

        elif filename.endswith(('.xlsx', '.xls')):
            # Use pandas to read Excel (reads the first sheet by default)
            df = pd.read_excel(file_stream)
            return df.to_string(index=False)

    except Exception as e:
        print(f"File parsing error for {filename}: {e}")
        return None
    
    return None

# --- CORE LLM FUNCTION ---

def run_gemini_generation(system_prompt, user_prompt):
    """Handles the actual call to the Gemini API."""
    if not client:
        return "LLM Client not initialized. Check GEMINI_API_KEY in .env."
    try:
        response = client.models.generate_content(
            model=LLM_MODEL,
            contents=[user_prompt],
            config={"system_instruction": system_prompt}
        )
        return response.text
    except APIError as e:
        print(f"Gemini API Error: {e.message}")
        return f"Gemini API Error: {e.message}"
    except Exception as e:
        print(f"Unexpected Error: {e}")
        return f"An unexpected error occurred: {e}"

# --- API ENDPOINTS ---

@app.route('/api/rag/ask', methods=['POST'])
def ask_question():
    # 1. Get the file and query from request.files and request.form
    if 'document' not in request.files:
        return jsonify({"message": "No document file part ('document') in the request."}), 400
    
    file = request.files['document']
    # The query is sent as form data from the frontend's FormData object
    query = request.form.get('query', '').strip() 
    
    if file.filename == '' or not query:
        return jsonify({"message": "File and query are required."}), 400

    # 2. Extract text from the uploaded file
    doc_content = extract_text_from_file(file)
    if not doc_content:
        return jsonify({"message": "Unsupported file format or unable to extract text. Check server console for details."}), 400

    # 3. Proceed with LLM call (RAG Prompt)
    system_prompt = "You are an expert RAG system. Answer the user's QUESTION strictly based on the provided CONTEXT. Do NOT use external knowledge. If the information is not in the CONTEXT, state clearly that it is not available in the document. Respond concisely."
    user_prompt = f"CONTEXT:\n---\n{doc_content}\n---\n\nQUESTION: {query}\n\nANSWER:"
    
    answer = run_gemini_generation(system_prompt, user_prompt)

    if answer.startswith("Gemini API Error") or answer.startswith("LLM Client not initialized"):
        return jsonify({"message": answer}), 500

    return jsonify({"answer": answer})


@app.route('/api/rag/summarize', methods=['POST'])
def summarize_content():
    # 1. Get the file from request.files
    if 'document' not in request.files:
        return jsonify({"message": "No document file part ('document') in the request."}), 400
    
    file = request.files['document']
    
    if file.filename == '':
        return jsonify({"message": "File is required for summarization."}), 400

    # 2. Extract text from the uploaded file
    doc_content = extract_text_from_file(file)
    if not doc_content:
        return jsonify({"message": "Unsupported file format or unable to extract text. Check server console for details."}), 400
    
    # 3. Proceed with LLM call (Summarization Prompt)
    system_prompt = "You are a professional summarization assistant. Provide a comprehensive, multi-paragraph summary of the following document. Structure the summary logically, using headings or lists if appropriate."
    user_prompt = f"DOCUMENT CONTENT:\n---\n{doc_content}\n---\n\nProvide a detailed, structured summary of this document."
    
    summary = run_gemini_generation(system_prompt, user_prompt)
    
    if summary.startswith("Gemini API Error") or summary.startswith("LLM Client not initialized"):
        return jsonify({"message": summary}), 500
        
    return jsonify({"summary": summary})

if __name__ == '__main__':
    print(f"Starting Flask server on http://127.0.0.1:5000")
    app.run(debug=True)


"""from src.data_loader import load_all_documents
from src.vectorstore import FaissVectorStore
from src.search import RAGSearch

# Example usage
if __name__ == "__main__":
    
    docs = load_all_documents("data")
    store = FaissVectorStore("faiss_store")
    #store.build_from_documents(docs)
    store.load()
    #print(store.query("What is attention mechanism?", top_k=3))
    rag_search = RAGSearch()
    query = "What is attention mechanism?"
    summary = rag_search.search_and_summarize(query, top_k=3)
    print("Summary:", summary)
    
    """