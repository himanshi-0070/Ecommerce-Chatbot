from config import LLM_BACKEND
# Groq support disabled for now — using OpenAI exclusively
from llm.llm_wrapper import generate_response

def rag_ask(query, retrieved_chunks):
    prompt = [
        {"role": "system", "content": "You are an intelligent assistant that answers based on the provided context."},
        {"role": "user", "content": f"Context:\n{chr(10).join(retrieved_chunks)}\n\nQuestion: {query}"}
    ]
    return generate_response(prompt)