import openai
from config import OPENAI_API_KEY, OPENAI_MODEL

openai.api_key = OPENAI_API_KEY

def generate_response(messages):
    response = openai.ChatCompletion.create(
        model=OPENAI_MODEL,
        messages=messages,
        temperature=0.7
    )
    return response["choices"][0]["message"]["content"]