import json

# Carregar os dados do arquivo JSON
with open("alimentador.json", "r", encoding="utf-8") as file:
    dados = json.load(file)

def search_info(question):
    # Lista para armazenar informações relevantes
    resultados = []

    # Buscar textos que contenham palavras-chave da pergunta
    palavras_chave = question.lower().split()
    for item in dados:
        texto = item["texto"].lower()
        if any(palavra in texto for palavra in palavras_chave):
            resultados.append(item["texto"])

    return resultados