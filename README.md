
# 🧠 **KnowVault – AI-Powered Knowledge Vault and Document Intelligence Engine**

> **Your intelligent vault of knowledge — search, summarize, and discover with AI.**
> Powered by **Flask**, **LangChain**, **Gemini LLM**, and a modern **Next.js + Tailwind CSS** frontend, **KnowVault** transforms scattered documents into a smart, searchable knowledge base.

---

## 🚀 **Overview**

**KnowVault** is an AI-driven **Retrieval-Augmented Generation (RAG)** system that enables users to upload custom documents (TXT, CSV, PDF, DOCX, XLSX), automatically processes them into embeddings, and generates **context-aware answers** and **summaries** using the **Gemini LLM**.

This project demonstrates professional-grade **modularity**, **clarity**, and **AI integration**, ideal for production, research, or recruitment showcases.

---

## 🧩 **Key Features**

✅ Upload multiple document formats (TXT, PDF, CSV, DOCX, XLSX)  
✅ Smart text extraction and chunking  
✅ OpenAI/Gemini-based embeddings and vector storage  
✅ Accurate, context-based Q&A using RAG  
✅ One-click document summarization  
✅ Sleek and responsive **Next.js + Tailwind** frontend  
✅ Modular Flask backend for easy scaling  
✅ Deployment-ready for **Render (backend)** and **Vercel (frontend)** [Optional]

---

## 🏗️ **Architecture Diagram**

```mermaid 
flowchart TD 
  
A[📄 User Uploads Documents<br>(TXT, CSV, PDF, DOCX, XLSX)] --> B[🧩 Flask Backend]

B --> C[🪶 File Processing<br>Extract Text + Clean Data]
C --> D[🧱 Chunking<br>Split Text into Meaningful Parts]
D --> E[🧬 Embedding Generation<br>Gemini text-embedding-004]
E --> F[🗂️ Vector Storage<br>Stored Locally or in Memory]

G[💬 User Query Input] --> H[🔍 Convert Query → Embedding]
H --> I[📏 Similarity Search<br>Find Top-k Relevant Chunks]
I --> J[🧠 LLM Synthesis<br>gemini-2.5-flash-preview-05-20]
J --> K[🗣️ Contextual Answer Generation<br>Based on Retrieved Chunks]

F --> I
B -->|Serves Frontend| L[💻 Next.js + Tailwind Frontend<br>Responsive UI for Upload & Query]
K --> L
```

---

## ⚙️ **Tech Stack**

| Layer         | Technology                                            | Purpose                                  |
| ------------- | ----------------------------------------------------- | ---------------------------------------- |
| Backend       | **Flask (Python)**                                    | RESTful API, file handling, RAG pipeline |
| RAG Framework | **LangChain**                                         | Document loaders, chunking, retrieval    |
| Embeddings    | **Gemini text-embedding-004**                         | Vector representation of document text   |
| LLM           | **Gemini 2.5 Flash Preview**                          | Contextual answer and summary generation |
| Vector Store  | **Chroma (Local)**                                    | Persistent storage of embeddings         |
| Frontend      | **Next.js + Tailwind CSS**                            | Responsive and clean UI                  |
| Deployment    | **Render / Railway** (Backend), **Vercel** (Frontend) | Free hosting & scalability               |

---

## 🗂️ **Project Structure**

```
KnowVault/
│
├── backend/
│   ├── app.py                 # Flask entry point
│   ├── config.py              # API keys and constants
│   ├── requirements.txt
│   ├── routes/
│   │   ├── ingest_routes.py   # /upload endpoint
│   │   └── query_routes.py    # /query endpoint
│   ├── utils/
│   │   ├── pdf_loader.py      # Extract text from PDFs
│   │   ├── vector_store.py    # Handle embeddings and storage
│   │   └── rag_pipeline.py    # Core RAG logic
│   └── data/
│       ├── uploads/           # Uploaded documents
│       └── chroma_store/      # Local vector database
│
└── frontend/
    ├── pages/
    │   ├── index.js           # Home page UI
    ├── components/
    │   ├── UploadBox.js       # File upload interface
    │   ├── QueryBox.js        # Query input and button
    │   └── AnswerCard.js      # Display answers and sources
    ├── styles/
    │   └── globals.css
    └── utils/
        └── api.js             # Axios config for backend API
```

---

## 🧠 **How KnowVault Works**

1️⃣ **Upload Documents** → TXT, CSV, DOCX, XLSX, PDF  
2️⃣ **Processing & Chunking** → Extract and split content into digestible pieces  
3️⃣ **Embedding Creation** → Convert text into vector form using Gemini API  
4️⃣ **Storage** → Save embeddings locally using Chroma  
5️⃣ **Query Handling** → Convert user query to embedding and retrieve top relevant chunks  
6️⃣ **Synthesis** → LLM generates factual, context-aware answers  
7️⃣ **Frontend Display** → Show generated answer + document sources  

---

## 🧩 **API Endpoints**

| Endpoint     | Method | Description                                                        |
| ------------ | ------ | ------------------------------------------------------------------ |
| `/upload`    | POST   | Uploads and processes PDF/TXT/CSV/DOCX/XLSX files                  |
| `/query`     | POST   | Takes a user query and returns an AI-generated answer with sources |
| `/summarize` | POST   | Summarizes the uploaded documents                                  |

**Example Response:**

```json
{
  "answer": "The uploaded documents discuss AI trends in data analytics.",
  "sources": ["AI_Report.pdf (Page 3)", "Trends2024.docx (Page 2)"]
}
```

---

## ⚙️ **Setup and Run Locally**

### 1. Clone Repository

```bash
git clone https://github.com/your-username/KnowVault.git
cd KnowVault
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure API Key

Get your **Gemini API key** from [Google AI Studio](https://aistudio.google.com/app/apikey).

Set it as an environment variable:

**macOS/Linux:**

```bash
export GEMINI_API_KEY="YOUR_API_KEY_HERE"
```

**Windows:**

```cmd
set GEMINI_API_KEY=YOUR_API_KEY_HERE
```

### 5. Run the Application

```bash
python app.py
```

The backend will start at 👉 **[http://127.0.0.1:5000/](http://127.0.0.1:5000/)**

---

## 💻 **Frontend Setup (Next.js + Tailwind)**

Navigate to frontend folder:

```bash
cd frontend
npm install
npm run dev
```

Your frontend will be live at 👉 **[http://localhost:3000](http://localhost:3000)**

---

## 🌐 **Deployment**

| Component                 | Platform                                                        | Command                       |
| ------------------------- | --------------------------------------------------------------- | ----------------------------- |
| **Backend**               | [Render](https://render.com/) / [Railway](https://railway.app/) | `gunicorn app:app`            |
| **Frontend**              | [Vercel](https://vercel.com/)                                   | Auto-deploy via GitHub        |
| **Environment Variables** | `.env`                                                          | `GEMINI_API_KEY=your_api_key` |

---

## 🎥 **Demo Flow**

🟢 **Step 1:** Upload a few PDFs or DOCX files  
🟢 **Step 2:** Ask a natural question (e.g., “Summarize the key findings”)  
🟢 **Step 3:** View AI-generated contextual answer + document sources  
🟢 **Step 4 (Bonus):** Click “Summarize Documents” for quick insights  

**🎬 Example Command:**

```bash
curl -X POST http://127.0.0.1:5000/query -H "Content-Type: application/json" -d '{"query": "What are the main themes discussed?"}'
```

---

## 🧱 **Evaluation Focus**

✅ Retrieval accuracy  
✅ Synthesis quality  
✅ Code structure & modularity  
✅ Clean and responsive UI  
✅ LLM integration (Gemini)  
✅ Bonus: Source display + Summarization  

---

## 🧑‍💻 **Author**

**Janavi Singh**
🎓 Software Engineering Student | AI-ML & Data Science Enthusiast
🔗 [LinkedIn](https://linkedin.com/in/janavi-singh) • [GitHub](https://github.com/your-username)

---

## ⭐ **Support & Contributions**

If you found this project insightful or inspiring,
⭐ **Star this repo** and share it with fellow AI enthusiasts!

---
