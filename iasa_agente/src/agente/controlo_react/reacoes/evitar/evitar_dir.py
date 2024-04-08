from ecr.reacao import Reacao
from agente.controlo_react.reacoes.evitar.estimulo_obst import EstimuloObst

"""
Representa a Reacao de evitar um obstaculo 
numa direcao específica
"""
class EvitarDir(Reacao):
    def __init__(self, direcao, resposta):
        estimulo = EstimuloObst(direcao)
        super().__init__(estimulo, resposta)