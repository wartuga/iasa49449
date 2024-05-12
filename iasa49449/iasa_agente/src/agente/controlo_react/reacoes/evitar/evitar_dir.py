from ecr.reaccao import Reaccao
from agente.controlo_react.reacoes.evitar.estimulo_obst import EstimuloObst

"""
Representa a Reacao de evitar um obstaculo 
numa direcao específica gerando uma Reacao através do 
EstimuloObst uma vez que recebe a resposta e invoca
"""
class EvitarDir(Reaccao):
    def __init__(self, direccao, resposta):
        estimulo = EstimuloObst(direccao)
        super().__init__(estimulo, resposta)