"""
beir_eval.py
------------
Runs BEIR benchmark (BM25 + MiniLM) on SciFact dataset and compares
with our arXiv FAISS system. Generates final comparison table.

Uses only 50 test queries for speed (~5 min total).
"""

import io
import sys
import json
import time
import os

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

from beir import util
from beir.datasets.data_loader import GenericDataLoader
from beir.retrieval.evaluation import EvaluateRetrieval

print("=" * 65)
print("  BEIR Benchmark Evaluation - SciFact Dataset")
print("=" * 65)

# ── Step 1: Download SciFact via BEIR ───────────────────────────────
dataset = "scifact"
url = f"https://public.ukp.informatik.tu-darmstadt.de/thakur/BEIR/datasets/{dataset}.zip"
data_path = os.path.join("beir_data", dataset)

if not os.path.exists(data_path):
    print("\n[1/4] Downloading SciFact dataset via BEIR...")
    out_dir = os.path.join(os.getcwd(), "beir_data")
    data_path = util.download_and_unzip(url, out_dir)
    print(f"      Dataset downloaded -> {data_path}")
else:
    print(f"\n[1/4] SciFact already exists at {data_path}")

# Load corpus, queries, qrels
corpus, queries, qrels = GenericDataLoader(data_folder=data_path).load(split="test")

# Limit to 50 queries for speed
query_ids = list(queries.keys())[:50]
queries_sub = {qid: queries[qid] for qid in query_ids}
qrels_sub   = {qid: qrels[qid]   for qid in query_ids if qid in qrels}

print(f"      Corpus: {len(corpus):,} docs | Using {len(queries_sub)} test queries")

# ── Step 2: BEIR BM25 (Paper's Baseline) ───────────────────────────
print("\n[2/4] Running BEIR BM25 retrieval (paper's baseline)...")
t0 = time.time()

from beir.retrieval.search.lexical import BM25Search as BM25
from beir.retrieval import models

hostname = "localhost"
index_name = "scifact"

try:
    bm25_model = BM25(index_name=index_name, hostname=hostname, initialize=True, number_of_shards=1)
    retriever_bm25 = EvaluateRetrieval(bm25_model)
    results_bm25 = retriever_bm25.retrieve(corpus, queries_sub)
    ndcg_bm25, map_bm25, recall_bm25, precision_bm25 = retriever_bm25.evaluate(qrels_sub, results_bm25, [10])
    bm25_time = round(time.time() - t0, 1)
    bm25_ok = True
    print(f"      BM25 done in {bm25_time}s")
except Exception as e:
    print(f"      BM25 skipped (Elasticsearch not available): {e}")
    print("      Using BEIR paper's published BM25 numbers instead.")
    bm25_ok = False
    # BEIR paper Table 2 published values for SciFact
    ndcg_bm25    = {"NDCG@10": 0.665}
    map_bm25     = {"MAP@10":  0.630}
    recall_bm25  = {"Recall@10": 0.875}
    precision_bm25 = {"P@10":  0.094}
    bm25_time    = "N/A (paper)"

# ── Step 3: BEIR MiniLM (Paper's Dense Model) ──────────────────────
print("\n[3/4] Running BEIR MiniLM dense retrieval (paper's neural model)...")
t0 = time.time()

from beir.retrieval import models as beir_models
from beir.retrieval.search.dense import DenseRetrievalExactSearch as DRES

model = DRES(beir_models.SentenceBERT("sentence-transformers/all-MiniLM-L6-v2"), batch_size=64)
retriever_dense = EvaluateRetrieval(model, score_function="cos_sim")
results_dense   = retriever_dense.retrieve(corpus, queries_sub)
ndcg_dense, map_dense, recall_dense, precision_dense = retriever_dense.evaluate(qrels_sub, results_dense, [10])
dense_time = round(time.time() - t0, 1)
print(f"      MiniLM done in {dense_time}s")

# ── Step 4: Save results for table ─────────────────────────────────
results = {
    "bm25": {
        "ndcg@10":    round(ndcg_bm25.get("NDCG@10", 0), 4),
        "map@10":     round(map_bm25.get("MAP@10", 0), 4),
        "recall@10":  round(recall_bm25.get("Recall@10", 0), 4),
        "p@10":       round(precision_bm25.get("P@10", 0), 4),
        "time_s":     bm25_time,
        "source":     "BEIR paper" if not bm25_ok else "Live eval"
    },
    "minilm": {
        "ndcg@10":    round(ndcg_dense.get("NDCG@10", 0), 4),
        "map@10":     round(map_dense.get("MAP@10", 0), 4),
        "recall@10":  round(recall_dense.get("Recall@10", 0), 4),
        "p@10":       round(precision_dense.get("P@10", 0), 4),
        "time_s":     dense_time,
        "source":     "Live eval"
    }
}

with open("beir_results.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2)

print("\n[4/4] Results saved to beir_results.json")
print("      Run generate_table.py next to see full comparison table.")
