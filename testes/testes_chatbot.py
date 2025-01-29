def test_enviar_mensagem(chatbot):
    """
    Testar se o botão de click para enviar mensagem 
    funciona corretamente
    """
    input_mensagem = "Olá, assistente!"
    chatbot.enviar_mensagem(input_mensagem)
    assert chatbot.mensagem_enviada() == input_mensagem


def test_resposta_chatbot(chatbot):
    """
    Por hora fantasia,
    verifica uma ou mais respostas (no futuro)
    do chat para uma determinada pergunta
    """
    pergunta = "Qual é o horário de funcionamento da biblioteca?"
    chatbot.enviar_mensagem(pergunta)
    resposta = chatbot.obter_resposta()
    assert resposta == "A biblioteca funciona de segunda a sexta, das 8h às 18h."


def test_historico_mensagens(chatbot):
    """
    Se aplicavél, irá testar se o historico de mensagens vai existir
    """
    mensagens = ["Oi", "Como você está?", "Qual é a sua função?"]
    for msg in mensagens:
        chatbot.enviar_mensagem(msg)
    assert chatbot.obter_historico() == mensagens

def test_pergunta_geral_agente_macro(chatbot):
    """
    Determinar se o agente geral responde adequadamente
    verificar qual resposta deve ser padrão para essa pergunta por exemplo
    """
    pergunta = "O que é a UFBA?"
    chatbot.enviar_mensagem(pergunta)
    resposta = chatbot.obter_resposta()
    assert resposta == "A UFBA é a Universidade Federal da Bahia."

def test_pergunta_especialista(chatbot):
    pergunta = "Quais são os cursos de pós-graduação?"
    chatbot.enviar_mensagem(pergunta)
    resposta = chatbot.obter_resposta()
    assert resposta == "Para saber mais sobre cursos de pós-graduação, consulte o agente especialista."
