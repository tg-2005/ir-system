import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

from flask import Flask, render_template, request
from fetch_papers import fetch_arxiv_papers
from summarizer import summarize_text
from search_engine import PaperSearchEngine
import numpy as np

app = Flask(__name__)

_model = None
def get_model():
    global _model
    if _model is None:
        from sentence_transformers import SentenceTransformer
        _model = SentenceTransformer('all-MiniLM-L6-v2')
    return _model

def embed(texts):
    return get_model().encode(texts, convert_to_numpy=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    results, query = [], ""
    if request.method == 'POST':
        query = request.form.get('query', '').strip()
        if query:
            raw_papers = fetch_arxiv_papers(query, max_results=10)
            embeddings = embed([p['summary'] for p in raw_papers])
            engine     = PaperSearchEngine(np.array(embeddings), raw_papers)
            top5       = engine.search(embed([query]), top_k=5)
            for i, paper in enumerate(top5, 1):
                results.append({
                    'rank':    i,
                    'title':   paper['title'],
                    'summary': summarize_text(paper['summary']),
                    'url':     paper['url'],
                    'score':   paper['similarity_score']
                })
    return render_template('index.html', query=query, results=results)

if __name__ == '__main__':
    print("Open http://127.0.0.1:5000")
    app.run(debug=False, port=5000, use_reloader=False)
