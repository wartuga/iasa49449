from ecr.comportamento import Comportamento
from random import choice
from sae import Direccao
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
        direccao = self.__direccao_aleatoria()
        resposta = RespostaMover(direccao)
        return resposta.activar(percepcao)
        
    """
    Método auxiliar para escolher uma direcao aleatória
    Private pois apenas é usada por um método da classe
    e não permite ser chamado pelo exterior
    """
    def __direccao_aleatoria(self):
        direccoes = list(Direccao)
        return choice(direccoes)