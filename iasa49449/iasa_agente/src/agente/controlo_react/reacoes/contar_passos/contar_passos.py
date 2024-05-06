from ecr.comportamento import Comportamento
from sae import Direccao
from ..resposta.resposta_mover import RespostaMover

"""
Exercicio da aula onde após 10 passos
o agente apenas de move para NORTE
"""
class ContarPassos(Comportamento):
    """
    Construtor da classe
    """
    def __init__(self):
        self.__direcao = RespostaMover(Direccao.NORTE)
        self.__passos = 0

    """
    recebe a percepcao, incrementando o número de
    passos e caso seja maior ou igual a 10
    o agente toma a acao de apenas se mover para NORTE
    """
    def activar(self, percepcao):
        self.__passos += 1
        if self.__passos >= 10:
            resposta = self.__direcao
            return resposta.activar(percepcao)