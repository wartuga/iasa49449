from ecr.reaccao import Reacao
from agente.controlo_react.reacoes.evitar.estimulo_obst import EstimuloObst

"""
Representa a Reacao de evitar um obstaculo 
numa direcao específica gerando uma Reacao através do 
EstimuloObst uma vez que recebe a resposta e invoca

"""
class EvitarDir(Reacao):
    def __init__(self, direcao, resposta):
        estimulo = EstimuloObst(direcao)
        super().__init__(estimulo, resposta)