from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

class DenseRetrievalSystem:
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        """Initialize the RAG system with a sentence transformer model and FAISS index"""
        self.model = SentenceTransformer(model_name)
        self.embedding_dimension = self.model.get_sentence_embedding_dimension()
        self.index = faiss.IndexFlatL2(self.embedding_dimension)
        self.entries = []

    def push(self, entry: str):
        """Add a new entry to the system"""
        self.entries.append(entry)
        vector = self.model.encode(entry)
        vector_np = np.array([vector]).astype('float32')
        self.index.add(vector_np)

    def search(self, user_text: str, k: int = 3) -> list[tuple[str, float]]:
        """Search for k similar entries to the user text"""
        new_vector = self.model.encode(user_text)
        new_vector_np = np.array([new_vector]).astype('float32')

        # Search for k similar entries
        D, I = self.index.search(new_vector_np, k)
        
        # Return only up to k results (in case we have fewer entries than k)
        k = min(k, len(self.entries))
        return [(self.entries[I[0][i]], D[0][i]) for i in range(k)]

# Example usage:
# rag = RAGSystem()
# rag.push("for john to pass his test")
# results = rag.search("test", k=3)