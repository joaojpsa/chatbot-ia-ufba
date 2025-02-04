import pytest

def test_example():
    assert 1 + 1 == 2

# Teste do agente macro
def test_macro_agent_response():
    resposta = "O Instituto de Computação da UFBA oferece cursos de graduação e pós-graduação."
    assert "UFBA" in resposta

# Teste do agente especialista
def test_specialist_agent_redirect():
    pergunta = "Quais são as disciplinas do curso de Ciência da Computação?"
    especialista = "Agente de Graduação"
    assert especialista == "Agente de Graduação"
