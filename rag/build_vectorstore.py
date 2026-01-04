import pandas as pd
import os
from langchain_core.documents import Document
from langchain_community.vectorstores import Chroma
from sentence_transformers import SentenceTransformer
from langchain.embeddings.base import Embeddings

DB_DIR = "rag/chroma_db"

# ---- Local Embedding Wrapper ----
class LocalEmbedding(Embeddings):
    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def embed_documents(self, texts):
        return self.model.encode(texts, batch_size=16, show_progress_bar=True).tolist()

    def embed_query(self, text):
        return self.model.encode(text).tolist()

# ---- Load data (LIMIT SIZE FIRST) ----
df = pd.read_csv("data/processed/processed_ddinter.csv")

# LIMIT for stability (IMPORTANT)
df = df.head(2000)   # 🔥 THIS IS KEY

docs = []
for _, row in df.iterrows():
    docs.append(
        Document(
            page_content=f"Drug interaction between {row['Drug_A']} and {row['Drug_B']}.",
            metadata={
                "drug_a": row["Drug_A"],
                "drug_b": row["Drug_B"],
                "source": "DDInter"
            }
        )
    )

# ---- Build Vector Store ----
db = Chroma.from_documents(
    documents=docs,
    embedding=LocalEmbedding(),
    persist_directory=DB_DIR
)

db.persist()
print("✅ Vector store built successfully (LOCAL embeddings)")
