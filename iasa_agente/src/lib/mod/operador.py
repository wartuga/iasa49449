from abc import ABC, abstractmethod

"""
Representação de um operador/transição.
"""
class Operador(ABC):
    """
    Método abstrato para ser implementado
    para uma ação em concreto para aplicar
    uma ação sobre um estado
    """
    @abstractmethod
    def aplicar(self, estado):
        raise NotImplementedError

    """
    Método abstrato a ser implementado
    para o cálculo do custo de um estado
    para estado sucessor 
    """
    @abstractmethod
    def custo(self, estado, estado_suc):
        raise NotImplementedError