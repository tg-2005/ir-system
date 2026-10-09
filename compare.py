"""
compare.py
----------
Command-line comparison tool for Research Paper Search:
Compares:
  1. Original Baseline: arXiv Keyword Search Ranking
  2. Our Proposed System: MiniLM Sentence Embeddings + FAISS Vector Search Ranking

Usage:
  python compare.py "graph neural networks drug discovery"
"""

import io
import sys
import argparse
import numpy as np

# Force UTF-8 on Windows
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

from fetch_papers import fetch_arxiv_papers
from embedder import embed_texts
from search_engine import PaperSearchEngine


def compare_search(query: str, top_k: int = 5):
    print("=" * 80)
    print(f"QUERY: '{query}'")
    print("=" * 80)
    print("\nFetching candidate papers from arXiv API...")

    raw_papers = fetch_arxiv_papers(query, max_results=10)
    if not raw_papers:
        print("No papers retrieved.")
        return

    # Assign original arXiv ranking
    for idx, p in enumerate(raw_papers, start=1):
        p['original_rank'] = idx

    print(f"Fetched {len(raw_papers)} papers from arXiv.")
    print("Generating MiniLM vector embeddings and indexing with FAISS...\n")

    # Generate embeddings and re-rank with FAISS
    summaries = [p['summary'] for p in raw_papers]
    embeddings = embed_texts(summaries)
    engine = PaperSearchEngine(np.array(embeddings), raw_papers)

    query_embedding = embed_texts([query])
    semantic_results = engine.search(query_embedding, top_k=top_k)

    # ── Display Comparison Table ──────────────────────────────────────────
    print(f"{'Rank':<6} | {'Original arXiv Baseline Title':<35} | {'Our Semantic Re-ranked Title':<35}")
    print("-" * 84)

    for rank in range(1, top_k + 1):
        orig_title = (raw_papers[rank - 1]['title'][:32] + "...") if rank <= len(raw_papers) else "N/A"
        sem_title  = (semantic_results[rank - 1]['title'][:32] + "...") if rank <= len(semantic_results) else "N/A"
        
        orig_rank_of_sem = semantic_results[rank - 1]['original_rank'] if rank <= len(semantic_results) else "-"
        sim_score = semantic_results[rank - 1].get('similarity_score', 0) if rank <= len(semantic_results) else 0

        print(f"#{rank:<5} | {orig_title:<35} | {sem_title:<35}")

    print("\n" + "=" * 80)
    print("DETAILED RANKING SHIFTS:")
    print("=" * 80)
    for res in semantic_results:
        shift = res['original_rank'] - res['semantic_rank']
        if shift > 0:
            trend = f"▲ Promoted by +{shift} ranks (Semantic search identified deeper relevance)"
        elif shift < 0:
            trend = f"▼ Lowered by {shift} ranks (Keyword matched but low semantic relevance)"
        else:
            trend = "= Same rank"
        
        print(f"• Semantic Rank #{res['semantic_rank']} (was arXiv #{res['original_rank']}):")
        print(f"  Title     : {res['title']}")
        print(f"  Sim Score : {res['similarity_score']} (FAISS Distance: {res['faiss_distance']})")
        print(f"  Analysis  : {trend}")
        print(f"  PDF URL   : {res['url']}\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compare Original arXiv Search vs Our Semantic Search")
    parser.add_argument("query", nargs="?", default="machine learning for medical diagnosis", help="Search query")
    parser.add_argument("--top_k", type=int, default=5, help="Number of papers to compare")
    args = parser.parse_args()

    compare_search(args.query, top_k=args.top_k)
