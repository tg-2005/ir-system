import faiss
import numpy as np

class PaperSearchEngine:
    def __init__(self, embeddings, papers):
        # IndexFlatL2 measures squared Euclidean distance between 384-dim vectors
        self.index = faiss.IndexFlatL2(embeddings.shape[1])
        self.index.add(embeddings)
        self.papers = papers

    def search(self, query_embedding, top_k=5):
        actual_k = min(top_k, len(self.papers))
        if actual_k <= 0:
            return []
        
        distances, indices = self.index.search(query_embedding, actual_k)
        
        ranked_papers = []
        for rank, (dist, idx) in enumerate(zip(distances[0], indices[0]), start=1):
            if 0 <= idx < len(self.papers):
                paper = dict(self.papers[idx])
                paper['semantic_rank'] = rank
                paper['faiss_distance'] = round(float(dist), 4)
                # Convert distance to approximate similarity score (0 to 1 range)
                paper['similarity_score'] = round(float(1 / (1 + dist)), 4)
                ranked_papers.append(paper)
        return ranked_papers
