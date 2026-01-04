from langchain_community.vectorstores import Chroma
from sentence_transformers import SentenceTransformer
from langchain.embeddings.base import Embeddings

# ---- Local Embedding (same as build_vectorstore) ----
class LocalEmbedding(Embeddings):
    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def embed_documents(self, texts):
        return self.model.encode(texts, batch_size=16).tolist()

    def embed_query(self, text):
        return self.model.encode(text).tolist()

# ---- Load vector store (LOCAL) ----
db = Chroma(
    persist_directory="rag/chroma_db",
    embedding_function=LocalEmbedding()
)

def retrieve_interaction_text(drug_a, drug_b):
    """
    Retrieve ONLY evidence that mentions BOTH drugs.
    Prevents cross-drug hallucination.
    """
    query = f"drug interaction between {drug_a} and {drug_b}"
    results = db.similarity_search(query, k=5)

    drug_a = drug_a.lower()
    drug_b = drug_b.lower()

    filtered = []
    for r in results:
        text = r.page_content.lower()
        if drug_a in text and drug_b in text:
            filtered.append(r.page_content)

    if not filtered:
        return ["No direct evidence found in retrieved sources."]

    return filtered
