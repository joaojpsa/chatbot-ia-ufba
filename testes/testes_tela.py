def test_botao_enviar(funcionario_botao_enviar):
    assert funcionario_botao_enviar.clicado() == True


def test_limpar_chat(chatbot):
    chatbot.enviar_mensagem("Mensagem 1")
    chatbot.enviar_mensagem("Mensagem 2")
    chatbot.limpar_chat()
    assert chatbot.obter_historico() == []


def test_icone_carregamento(chatbot):
    """
    Supondo que a UX vai incluir um carregamento prévio para
    mostrar na tela
    """
    chatbot.enviar_mensagem("Qual é a previsão do tempo?")
    assert chatbot.icone_carregamento_visivel() == True
