
# 🔍 Know Vault — AI-Powered Knowledge Base Search Engine

**Know Vault** is an intelligent, AI-powered **Knowledge Base Search Engine** that uses **Retrieval-Augmented Generation (RAG)** to search across multiple documents and generate synthesized, context-aware answers.  

It combines document parsing, semantic retrieval, and LLM-based reasoning to help users instantly extract insights from large collections of PDFs or text files.

---

## 🎯 Objective

To build a **knowledge-base search system** that:
- Searches across multiple text/PDF documents
- Retrieves relevant context using embeddings or RAG
- Synthesizes concise, human-like answers via an LLM

---

## 🧩 Core Features

- **📂 Multi-Document Ingestion:** Upload and index multiple PDFs or text files.
- **🔍 Smart Semantic Search:** Uses embeddings or retrieval pipelines to find the most relevant content.
- **🧠 LLM-Powered Synthesis:** Summarizes and answers queries using the context retrieved from uploaded documents.
- **💬 Interactive Query Mode:** Ask any question and get a synthesized answer.
- **🌐 Optional Frontend (UI):** Simple interface for uploading documents and querying the knowledge base.

---

## ⚙️ Architecture Overview

| Component | Technology | Role |
|------------|-------------|------|
| **Backend** | Python, Flask | Handles document ingestion, text parsing, embedding generation, and LLM query synthesis |
| **Embedding & Retrieval** | FAISS + Langchain| Indexes and retrieves relevant document chunks |
| **LLM Layer** | Gemini API  | Synthesizes the final answer from retrieved context |
| **Frontend (optional)** | HTML + Tailwind CSS + Javascript | User interface for document upload and query submission |

---

## 🧠 LLM Usage Guidance

Example Prompt:

> “Using these documents, answer the user’s question succinctly.”

This prompt ensures the LLM focuses strictly on provided content, not hallucinations.

---

## 🚀 Setup & Installation

### 1. Prerequisites
- Python **3.9+**
- Valid API key (Gemini / OpenAI / Claude / Local LLM)
- Git

---

### 2. Clone the Repository

```bash
git clone https://github.com/your-username/know-vault.git
cd know-vault
````

---

### 3. Set Up Virtual Environment

```bash
python -m venv venv
.\venv\Scripts\activate.ps1  # Windows
# or
source venv/bin/activate     # Linux/macOS
```

---

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 5. Configure API Key

Create a `.env` file in the project root and add:

```env
LLM_API_KEY="YOUR_API_KEY_HERE"
```

---

### 6. Run the Backend

```bash
python app.py
```

Server runs at [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

### 7. (Optional) Run the Frontend

Open `index.html` in your browser and start querying your knowledge base.

---

## 💡 Example Workflow

1. Upload your **documents (PDF/Text)**.
2. The backend extracts and indexes the content.
3. Enter a **query** like:

   > “Summarize the key findings from all research papers.”
4. System retrieves relevant chunks → sends them to LLM → returns a **synthesized, concise answer**.

---

## ⚠️ Troubleshooting

| Issue                 | Cause                | Solution                                              |
| --------------------- | -------------------- | ----------------------------------------------------- |
| `ModuleNotFoundError` | Missing dependencies | Run `pip install -r requirements.txt`                 |
| `401 Unauthorized`    | Invalid API key      | Verify key in `.env`                                  |
| No answers returned   | No relevant matches  | Check document content or adjust embedding parameters |
| Server not responding | Flask not running    | Ensure `python app.py` is active on port 5000         |

---

## 🧩 Deliverables

* ✅ Complete GitHub repository with working RAG system
* ✅ README documentation (this file)

---

## 🧠 Evaluation Focus

* **Retrieval Accuracy:** Quality of context retrieval from indexed documents
* **Answer Synthesis:** Clarity and correctness of generated responses
* **Code Quality:** Clean, modular, and well-structured Python code
* **LLM Integration:** Effective use of Gemini/OpenAI APIs for synthesis

---

## 🧑‍💻 Author

**Janavi** — Student & AI Developer

Passionate about building practical AI systems that bridge **data retrieval and intelligent synthesis**.

---




