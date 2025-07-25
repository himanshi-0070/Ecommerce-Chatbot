import pandas as pd
from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.config import Settings

def load_and_split_csv(path):
    df = pd.read_csv(path)
    texts = df.apply(lambda row: f"{row['title']} - {row['description']}", axis=1)
    return list(texts)

def build_vector_store(text_chunks):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = model.encode(text_chunks)

    client = chromadb.Client(Settings(chroma_db_impl="duckdb+parquet", persist_directory="chroma_store"))
    collection = client.get_or_create_collection("product_chunks")

    for i, (text, emb) in enumerate(zip(text_chunks, embeddings)):
        collection.add(documents=[text], embeddings=[emb.tolist()], ids=[str(i)])

    client.persist()