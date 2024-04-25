from mod.problema import Problema
from mod_prob.estado_contagem import EstadoContagem
from mod_prob.operador_incremento import OperadorIncremento

"""
Representação do problema de contagem
"""
class ProblemaContagem(Problema):

    """
    Construtor da classe
    """
    def __init__(self, valor_inicial, valor_final, incrementos):
        super().__init__(
            EstadoContagem(valor_inicial), 
            [OperadorIncremento(incremento) for incremento in incrementos]
        )
        self.__valor_final = valor_final

    """
    Implementação e definição do objetivo do problema
    """
    def objetivo(self, estado):
        return estado.valor >= self.__valor_final