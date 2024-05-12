from ..resposta.resposta_mover import RespostaMover
from agente.controlo_react.reacoes.aproximar.estimulo_alvo import EstimuloAlvo
from ecr.reaccao import Reaccao

"""
Representa a Reacao para a direcao que o agente 
está a visualizar gerando uma Reacao através do 
EstimuloAlvo e a resposta dada pela RespostaMover
"""
class AproximarDir(Reaccao):
    """
    se detectar um estimuloAlvo => vai dar 
    uma respostaMover na direção respetiva
    """
    def __init__(self, direccao):
        estimulo = EstimuloAlvo(direccao)
        resposta = RespostaMover(direccao)
        super().__init__(estimulo, resposta)