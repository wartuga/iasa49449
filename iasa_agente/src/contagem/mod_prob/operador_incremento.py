from mod.operador import Operador
from mod_prob.estado_contagem import EstadoContagem

"""
Representação do operador incremento
"""
class OperadorIncremento(Operador):
    """
    Construtor da classe
    """
    def __init__(self, incremento):
        self.__incremento = incremento

    """
    Propriedade incremento do operador incremento
    """
    @property
    def incremento(self):
        return self.__incremento
    
    """
    Definição do método aplicar, onde é
    efetuado a alteração de estado da 
    contagem
    """
    def aplicar(self, estado):
        return EstadoContagem(estado.valor + self.__incremento)

    """
    Implementação do custo, neste caso,
    o problema apresentado não dependia
    do estado nem do estado sucessor para
    ser calculado o custo do operador,
    sendo este sempre o quadrado do incremento
    efetuado ao estado
    """
    def custo(self, estado, estado_suc):
        return self.__incremento ** 2