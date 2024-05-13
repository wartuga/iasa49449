from mod.problema import Problema

"""
Representa o problema do planeador com base no mecanismo
de procura melhor primeiro.
Precisamos do problema de planeamento é uma concretização 
da definição de problema base, o planeamento será de um 
estado inicial para um estado final.
"""
class ProblemaPlan(Problema):
    """
    Construtor da classe
    """
    def __init__(self, modelo_plan, estado_final):
        operadores = modelo_plan.obter_operadores()
        estado_inicial = modelo_plan.obter_estado()
        super().__init__(estado_inicial, operadores)
        self.__estado_final = estado_final

    """
    Método para verificar se o estado recebido
    é o estado final
    """
    def objetivo(self, estado):
        return self.__estado_final == estado