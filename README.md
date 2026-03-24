# 📄 Research Paper Assistant

An AI-powered Streamlit app that lets you upload a research paper (PDF), get a structured summary, and chat with the paper using natural language.

---

## 🚀 Features

- **PDF Upload**: Upload any research paper in PDF format
- **Auto Summary**: Generates a structured 10-point summary including title, authors, key findings, limitations, and follow-up questions
- **Chat with your Paper**: Ask questions about the paper and get answers with evidence and page citations
- **Session Memory**: Chat history is preserved within the session

---

## 🛠️ Tech Stack

- [Streamlit](https://streamlit.io) — frontend and deployment
- [OpenAI API](https://platform.openai.com) — summarization, Q&A, and embeddings
- [PyMuPDF (fitz)](https://pymupdf.readthedocs.io) — PDF text extraction
- [NumPy](https://numpy.org) — cosine similarity for semantic search

---

## 📁 Project Structure

```
research-paper-agent/
├── app.py            # Main Streamlit app
├── pdf_utils.py      # PDF extraction and chunking
├── summarizer.py     # Paper summarization
├── qa.py             # Embeddings, retrieval, and Q&A
├── requirements.txt  # Dependencies
└── README.md
```

---

## ⚙️ Setup (Local)

1. **Clone the repo**
```bash
git clone https://github.com/Sruthijha/research-paper-agent.git
cd research-paper-agent
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Add your OpenAI API key** — create a `.env` file:
```
OPENAI_API_KEY=your_actual_key_here
```

4. **Run the app**
```bash
streamlit run app.py
```

---

## ☁️ Deployment (Streamlit Cloud)

1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io) and connect your repo
3. Set the main file path to `app.py`
4. Go to **Settings → Secrets** and add:
```toml
OPENAI_API_KEY = "your_actual_key_here"
```
5. Click **Deploy**

---

## 📌 How It Works

1. Upload a PDF research paper
2. Click **Generate Summary** — the app extracts text, summarizes it, and computes embeddings for all chunks
3. Ask questions in the chat — the app retrieves the most relevant chunks using cosine similarity and generates a cited answer

---

## 👩‍💻 Author

Built by [Sruthijha](https://github.com/Sruthijha)
