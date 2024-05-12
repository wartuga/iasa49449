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
        self.__direccao = RespostaMover(Direccao.NORTE)
        self.__counter = 0

    """
    recebe a percepcao, incrementando o número de
    passos e caso seja maior ou igual a 10
    o agente toma a acao de apenas se mover para NORTE
    """
    def activar(self, percepcao):
        self.__counter += 1
        if self.__counter >= 10:
            resposta = self.__direccao
            return resposta.activar(percepcao)