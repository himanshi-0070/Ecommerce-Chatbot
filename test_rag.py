# main.py
from fastapi import FastAPI
from pydantic import BaseModel
from rag.rag_pipeline import build_prompt
from llm.llm_wrapper import generate_response

app = FastAPI()

class Query(BaseModel):
    user_input: str

@app.post("/chat")
def chat(query: Query):
    prompt = build_prompt(query.user_input)
    response = generate_response(prompt)
    return {"response": response}
