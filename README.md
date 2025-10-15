
# 🧠 KnowVault : An AI-Powered Knowledge Base Search Engine

A **Retrieval-Augmented Generation (RAG)** system built with a **Python (Flask)** backend and a **modern HTML/Tailwind CSS** frontend.  
This app lets users upload various document types (PDF, CSV, Excel), ask contextual questions, or generate document summaries — all without needing to pre-build vector stores locally.

The architecture ensures secure API key management (Gemini API) on the server side and provides a **dark-themed, modern user interface** for smooth interaction.

---

## ✨ Features

- **📂 Dynamic File Upload** – Supports `.pdf`, `.xlsx`, `.xls`, and `.csv` file formats.  
- **🔒 Secure Backend Processing** – All parsing, extraction, and LLM calls are handled safely via Flask.  
- **🧩 RAG Query Mode** – Ask questions strictly based on the content of the uploaded file (context-aware Q&A).  
- **📝 Summarization Mode** – Generate a comprehensive summary of the uploaded file.  
- **🎨 Modern UI** – Responsive dark blue/indigo design using Tailwind CSS.  
- **⚡ Free-Tier LLM** – Powered by Google’s `gemini-2.5-flash` model.  

---

## ⚙️ Architecture

| Component | Technology | Role |
|------------|-------------|------|
| **Frontend (`index.html`)** | HTML, Tailwind CSS, JavaScript | Handles file uploads, user interactions, and sends requests to the API. Does **not** store API keys. |
| **Backend (`app.py`)** | Python, Flask, `google-genai` | Parses documents (`pdfminer.six`, `pandas`), extracts text, performs RAG or summarization using Gemini API, and returns responses. |

---

## 🚀 Setup & Installation

### 1. Prerequisites
- Python **3.9+**
- A valid **Gemini API Key**

---

### 2. Project Initialization

```bash
# Navigate to project root
cd RAG_basic

# Create a virtual environment
python -m venv venv

# Activate (Windows PowerShell)
.\venv\Scripts\Activate.ps1

# OR (Linux/macOS)
source venv/bin/activate
````

---

### 3. Install Dependencies

```bash
pip install flask flask-cors google-genai python-dotenv pdfminer.six openpyxl pandas
```

---

### 4. Configure API Key

Create a `.env` file inside your project root (`RAG_basic/.env`) and add your Gemini API key:

```env
GEMINI_API_KEY="YOUR_GEMINI_API_KEY_HERE"
```

---

## ▶️ Running the Application

### Step 1: Start the Backend Server

Make sure your virtual environment is active, then run:

```bash
python app.py
```

Server starts at:
👉 [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

### Step 2: Open the Frontend

Open the `index.html` file directly in your browser.

---

## 💡 Usage Guide

1. Click **“Select File”** and upload your PDF, CSV, or Excel file.
2. Type a question to enter **Q&A Mode**, or leave blank to summarize the file.
3. Click **Ask Question** or **Summarize All Content**.
4. The LLM response will appear in the **Server Response** section.

---

## ⚠️ Troubleshooting

| Issue                     | Possible Cause            | Solution                                                          |
| ------------------------- | ------------------------- | ----------------------------------------------------------------- |
| `ModuleNotFoundError`     | Missing dependencies      | Activate virtual environment and run `pip install [dependencies]` |
| `API Error: 400/401`      | Incorrect Gemini API Key  | Verify key in `.env` file                                         |
| `Connection Error`        | Flask server not running  | Ensure you ran `python app.py` and it's on port 5000              |
| `Unsupported File Format` | Missing parsing libraries | Ensure `pdfminer.six`, `openpyxl`, and `pandas` are installed     |

---

## 📁 Folder Structure

```
RAG_basic/
│
├── app.py
├── index.html
├── .env
├── venv/
├── static/
│   └── (optional Tailwind assets)
├── src/
└── faiss_store/
```

---

## 🧩 Tech Stack

* **Backend:** Flask, Python, Google GenAI
* **Frontend:** HTML, Tailwind CSS, JavaScript
* **LLM Model:** Gemini 2.5 Flash
* **Libraries:** pdfminer.six, pandas, openpyxl

---

## 🪄 Future Improvements

* Add multi-file RAG support
* Integrate streaming LLM responses
* Include database for chat history

---

## 🧑‍💻 Author

**Janavi** — Student, AI Developer & Research Enthusiast
🔗 *Feel free to fork, modify, and experiment with this project!*

---
