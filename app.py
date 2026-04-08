import os
import io
import pandas as pd
from pdfminer.high_level import extract_text_to_fp
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

from google import genai
from google.genai.errors import APIError

# RAG pipeline
from src.rag_pipeline import build_vector_store, retrieve_context

load_dotenv()

app = Flask(__name__)
CORS(app)

# --- CONFIG ---
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
LLM_MODEL = "gemini-2.5-flash"

if not GEMINI_API_KEY:
    print("FATAL: GEMINI_API_KEY missing")
    client = None
else:
    try:
        client = genai.Client(api_key=GEMINI_API_KEY)
        print(f"Gemini initialized: {LLM_MODEL}")
    except Exception as e:
        print(f"Gemini init error: {e}")
        client = None


# --- FILE PARSER ---
def extract_text_from_file(file):
    filename = file.filename.lower()
    file_stream = io.BytesIO(file.read())

    try:
        if filename.endswith(".pdf"):
            output = io.StringIO()
            extract_text_to_fp(file_stream, output)
            return output.getvalue()

        elif filename.endswith(".csv"):
            df = pd.read_csv(file_stream)
            return df.to_string(index=False)

        elif filename.endswith((".xlsx", ".xls")):
            df = pd.read_excel(file_stream)
            return df.to_string(index=False)

    except Exception as e:
        print(f"Parsing error: {e}")
        return None

    return None


# --- LLM CALL ---
def run_gemini(system_prompt, user_prompt):
    if not client:
        return "LLM not initialized"

    try:
        response = client.models.generate_content(
            model=LLM_MODEL,
            contents=[user_prompt],
            config={"system_instruction": system_prompt}
        )
        return response.text

    except APIError as e:
        return f"Gemini API Error: {e.message}"

    except Exception as e:
        return f"Unexpected error: {e}"


# --- ASK ENDPOINT ---
@app.route("/api/rag/ask", methods=["POST"])
def ask():

    if "document" not in request.files:
        return jsonify({"message": "Document missing"}), 400

    file = request.files["document"]
    query = request.form.get("query", "").strip()

    if file.filename == "" or not query:
        return jsonify({"message": "File + query required"}), 400

    doc_text = extract_text_from_file(file)

    if not doc_text:
        return jsonify({"message": "Failed to extract text"}), 400

    # Limit size (important for performance)
    doc_text = doc_text[:150000]

    try:
        # 🔥 REAL RAG PIPELINE
        vectorstore = build_vector_store(doc_text)
        context = retrieve_context(vectorstore, query, top_k=5)

    except Exception as e:
        return jsonify({"message": f"RAG error: {str(e)}"}), 500

    system_prompt = """
You are a strict RAG system.
Answer ONLY from CONTEXT.
If answer not found, say: Not present in document.
Be concise.
"""

    user_prompt = f"""
CONTEXT:
{context}

QUESTION:
{query}

ANSWER:
"""

    answer = run_gemini(system_prompt, user_prompt)

    if "Error" in answer or "LLM not initialized" in answer:
        return jsonify({"message": answer}), 500

    return jsonify({"answer": answer})


# --- SUMMARIZE ---
@app.route("/api/rag/summarize", methods=["POST"])
def summarize():

    if "document" not in request.files:
        return jsonify({"message": "Document missing"}), 400

    file = request.files["document"]

    if file.filename == "":
        return jsonify({"message": "File required"}), 400

    doc_text = extract_text_from_file(file)

    if not doc_text:
        return jsonify({"message": "Failed to extract text"}), 400

    system_prompt = """
You are a summarization expert.
Provide structured summary with key points.
"""

    user_prompt = f"""
DOCUMENT:
{doc_text}

SUMMARY:
"""

    summary = run_gemini(system_prompt, user_prompt)

    return jsonify({"summary": summary})


if __name__ == "__main__":
    print("Server running on http://127.0.0.1:5000")
    app.run(debug=True)
