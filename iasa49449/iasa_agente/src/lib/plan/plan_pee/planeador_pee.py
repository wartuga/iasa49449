from plan.planeador import Planeador
from pee.melhor_prim.procura_aa import ProcuraAA
from .mod_prob.heur_dist import HeurDist
from .mod_prob.problema_plan import ProblemaPlan
from .plano_pee import PlanoPEE

"""
objetivos -------------> planeador -> plano
modelo de planeamento ->

Raciocinio através de procura
Estado -> posiçao do agente
Operador -> Operador mover que define as transiçoes de estado
Problema -> indica o estado inicial, estado objetivo e operadores
Solução -> plano de ação que o planeador vai definir

Representa um planeador de solução baseado num mecanismo
de procura melhor primeiro, neste caso procura A*
"""
class PlaneadorPEE(Planeador):

    """
    Construtor da classe
    """
    def __init__(self):
        """
        Este mec_pee ao ser abstrato, oferece
        flexibilidade ao mecanismo de procura
        usado, desde que cumpra o contrato de
        procura melhor primeiro, ou seja,
        procura A* e procura sôfrega
        """
        self.__mec_pee = ProcuraAA()

    """
    Assume-se que os objetivos vêm ordenados
    pela distância ao objetivo
    """
    def planear(self, modelo_plan, objetivos):
        if objetivos:
            estado_final = objetivos[0]
            problema = ProblemaPlan(modelo_plan, estado_final)
            heuristica = HeurDist(estado_final)
            solucao = self.__mec_pee.procurar(problema, heuristica)
            if solucao:
                return PlanoPEE(solucao)