from embeddings.embed_store import load_and_split_csv, build_vector_store
from embeddings.vector_store import search_similar_chunks
from rag.rag_pipeline import rag_ask

# Step 1: Index the data (run only once, or when data updates)
chunks = load_and_split_csv("data/Product_Information_Dataset (1).csv")
build_vector_store(chunks)

# Step 2: Query & get response
query = "What are the top 5 highly-rated guitar products?"
retrieved = search_similar_chunks(query)
response = rag_ask(query, retrieved)

print("\n🔍 Retrieved Chunks:\n", retrieved)
print("\n🤖 LLM Response:\n", response)