from pee.melhor_prim.aval.heuristica import Heuristica
from math import dist

"""
Representa uma heurística baseada em distância,
que representa o custo neste problema.
Esta precisa do estado final.
"""
class HeurDist(Heuristica):
    """
    Construtor da classe
    """
    def __init__(self, estado_final):
        self.__estado_final = estado_final

    """
    Método que representa a função heurística
    para calcular a distância entre o estado 
    atual e o estado objetivo
    """
    def h(self, estado):
        return dist(estado.posicao, self.__estado_final.posicao)