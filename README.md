## 🔍 Research Paper Search Engine

A full-stack web application that allows users to search academic papers using natural language queries. It fetches relevant research papers from **arXiv**, uses **semantic search** to rank them, and generates **AI-powered summaries** of each paper’s key findings — all in real time and optimized to run on CPU.

---

## 🚀 Features

-  Search scholarly papers using plain language
-  Fetches real-time papers from **arXiv API**
-  Uses **vector embeddings** for semantic search
-  Generates **short AI summaries** for each paper
-  Optimized for **CPU-only environments**
-  Built with **Flask**

---

## 🛠️ Tech Stack

| Layer        | Technology |
|--------------|------------|
| Frontend     | Flask (Jinja2), HTML, Bootstrap 5 |
| Backend      | Flask, REST routing |
| Embeddings   | SentenceTransformers (MiniLM) |
| Summarization| HuggingFace Transformers (DistilBART) |
| Search Engine| FAISS (CPU version) |
| Data Source  | arXiv API |

---

# 📁 Project Structure
research_paper_search/
│
├── app.py # Flask app 
├── fetch_papers.py # Gets papers from arXiv
├── embedder.py # Embeds text into vectors
├── summarizer.py # Summarizes paper abstracts
├── search_engine.py # FAISS search logic
├── requirements.txt # Python dependencies
└── templates/
└── index.html # Frontend UI

---

# Installation

# Clone the repository

```bash
git clone https://github.com/abrahambenny46/research-paper-search.git
cd research-paper-search
```
# Install required packages

pip install -r requirements.txt

# Run the Application

python app.py

# Then open your browser and visit:
http://localhost:5000


# How It Works
1.User enters a query (e.g., "transformers in computer vision").
2.The app uses the arXiv API to fetch recent related papers.
3.Each abstract is embedded into a vector using MiniLM (a small Transformer model).
4.The user’s query is embedded and compared using FAISS to find the top matching papers.
5.The top 5 papers are summarized using the DistilBART model.
6.The results are displayed beautifully in the browser.

# Contributing
Contributions are welcome!
Feel free to:
Fork the repo,
Create a feature branch,
Submit a pull request
