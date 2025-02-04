import openai
import os
from db_service import search_info

def ask_chatgpt(question):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    info = search_info(question)
    context = "\n".join(info)

    prompt = f"""
    Use as informações abaixo para responder à pergunta.
    Se não encontrar uma resposta, diga 'Não encontrei essa informação na base de dados'.

    Informações disponíveis:
    {context}

    Pergunta: {question}
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]
