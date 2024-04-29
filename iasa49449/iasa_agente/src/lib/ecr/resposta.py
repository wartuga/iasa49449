"""
Representa a classe Resposta de uma arquitetura de agentes reativos
A resposta é o encapsulamento da accao e pode ser mais que uma ação 
(e.g.) nivel de prioridade
Resultado de um estímulo.
"""

class Resposta:
    """
    Construtor da classe Resposta
    """
    def __init__(self, accao):
        self._accao = accao

    """
    É o método chamado para gerar a ação é gerada 
    consoante a percepção recebida e a intensidade
    """
    def activar(self, _, intensidade = 0.0):
        self._accao.prioridade = intensidade
        return self._accao