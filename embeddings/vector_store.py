from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.config import Settings

def search_similar_chunks(query, top_k=5):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    q_emb = model.encode([query])[0]

    client = chromadb.Client(Settings(chroma_db_impl="duckdb+parquet", persist_directory="chroma_store"))
    collection = client.get_collection("product_chunks")

    results = collection.query(query_embeddings=[q_emb.tolist()], n_results=top_k)
    return results["documents"][0]