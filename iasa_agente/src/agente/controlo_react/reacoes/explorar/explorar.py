from ecr.comportamento import Comportamento
from random import choice
from sae.ambiente.direccao import Direccao
from ..resposta.resposta_mover import RespostaMover

"""
Representa o comportamento explorar de um agente, onde
este gera uma Acao através de uma Percepcao recebida
É um sub-objetivo de Recolher
"""
class Explorar(Comportamento):

    """
    Método para ativar a exploração, onde uma direcao
    é escolhida aleatoriamente e com isso é devolvida
    uma acao com essa direcao, esta ativada pela 
    percepcao recebida como parametro
    """
    def ativar(self, percepcao):
        direcao = self.__direcao_aleatoria()
        resposta = RespostaMover(direcao)
        return resposta.ativar(percepcao)
        
    """
    Método auxiliar para escolher uma direcao aleatória
    Private pois apenas é usada por um método da classe
    e não permite ser chamado pelo exterior
    """
    def __direcao_aleatoria(self):
        direcoes = list(Direccao)
        return choice(direcoes)