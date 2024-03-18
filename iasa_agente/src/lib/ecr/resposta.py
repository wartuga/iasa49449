"""
Representa a classe Resposta de uma arquitetura de agentes reativos
A resposta pode ser mais que uma ação (e.g.) nivel de prioridade
Resultado de um estímulo.
"""

class Resposta:
    """
    Construtor da classe Resposta
    """
    def __init__(self, acao):
        self._acao = acao

    """
    É o método chamado para gerar a ação é gerada 
    consoante a percepção recebida e a intensidade
    """
    def ativar(self, percepcao, intensidade = 0.0):
        self._acao.prioridade = intensidade
        return self._acao