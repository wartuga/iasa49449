from ..resposta.resposta_mover import RespostaMover
from agente.controlo_react.reacoes.aproximar.estimulo_alvo import EstimuloAlvo
from ecr.reacao import Reacao

"""
Representa a Reacao para a direcao que o agente 
está a visualizar gerando uma Reacao através do 
EstimuloAlvo e a resposta dada pela RespostaMover
"""
class AproximarDir(Reacao):
    """
    se detetar um estimuloAlvo => vai dar 
    uma respostaMover na direção respetiva
    """
    def __init__(self, direcao):
        estimulo = EstimuloAlvo(direcao)
        resposta = RespostaMover(direcao)
        super().__init__(estimulo, resposta)