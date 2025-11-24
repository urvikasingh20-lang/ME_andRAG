# 🤖 AI Portfolio Chatbot (RAG-Based System)

A personal AI-powered portfolio chatbot that answers questions about **Urvika Singh** using a Retrieval-Augmented Generation (RAG) pipeline built with LangChain, FAISS, and Hugging Face models.

---

## 📌 Project Overview

This project is a **context-aware AI assistant** that allows users to ask questions about the developer (Urvika Singh). Instead of hardcoded answers, it uses a **Retrieval-Augmented Generation (RAG)** approach to fetch relevant information from a custom knowledge base and generate accurate responses.

---

## 🧠 How It Works (RAG Pipeline)

```
User Query
     ↓
Text Embeddings (MiniLM)
     ↓
FAISS Vector Search
     ↓
Relevant Context Retrieval
     ↓
LLM Response Generation (Qwen Instruct)
```

---

## ✨ Features

- Answers questions about skills, projects, education, and achievements
- Uses FAISS vector database for semantic search
- Hugging Face models for embeddings and text generation
- Hallucination control using strict prompt engineering
- Works locally without paid APIs

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| Language | Python |
| LLM | Qwen2.5-0.5B-Instruct |
| Embeddings | HuggingFace MiniLM |
| Vector DB | FAISS |
| Framework | LangChain |
| Environment | Jupyter Notebook / Python |
| Version Control | Git + GitHub |

---

## 📁 Project Structure

```
rag-portfolio-chatbot/
│
├── app.py
├── myscript.py
├── requirements.txt
├── README.md
├── ABOUT_ME.txt
└── notebooks/
    └── ME_andRAG.ipynb
```

---

## ⚙️ Setup & Installation

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>
```

### 2. Create virtual environment (optional)

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### 3. Install requirements

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run

Run the chatbot in terminal:

```bash
python app.py
```

You will see:

```text
Hi I am Urvika Singh's AI portfolio assistant.
Type 'exit' to stop.
```

Ask questions like:

```text
Tell me about Urvika
What are her technical skills?
What projects has she done?
```

---

## 🔄 RAG Workflow Table

| Step | Description |
|------|------------|
| 1 | Load ABOUT_ME.txt |
| 2 | Split text into chunks |
| 3 | Generate embeddings |
| 4 | Store in FAISS |
| 5 | Retrieve relevant chunks |
| 6 | Generate LLM answer |

---

## 🧪 Example Queries

| Query | Expected Response |
|-------|-------------------|
| Tell me about Urvika | Short profile summary |
| What are her skills? | Bullet list of skills |
| What are her projects? | Project descriptions |

---

## ⚠️ Limitations

- Uses a small local LLM, so:
  - Formatting may not always be perfect
  - Long structured outputs can be inconsistent
- Only answers based on ABOUT_ME.txt
- Will respond with:
  > "I don't have that information in my knowledge base."
  if data is missing

---

## 🚀 Future Improvements

- Add web UI using Streamlit
- Support PDF and multi-file input
- Add chat memory
- Deploy to Hugging Face Spaces

---

## 👩‍💻 Author

**Urvika Singh**  
Aspiring AI/ML Engineer  

📧 Email: urvikasingh20@gmail.com  
🔗 LinkedIn: https://www.linkedin.com/in/urvika-singh/  
💻 GitHub: https://github.com/urvikasingh20-la  

---

## 📄 License

This project is licensed under the MIT License.
