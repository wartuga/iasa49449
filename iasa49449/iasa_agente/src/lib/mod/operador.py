from abc import ABC, abstractmethod

"""
Representação de um operador/transição.
// TODO: adcionar documentação teórica
"""
class Operador(ABC):
    
    @abstractmethod
    def aplicar(self, estado):
        """
        Método abstrato para ser implementado
        para uma ação em concreto para aplicar
        uma ação sobre um estado
        """

    @abstractmethod
    def custo(self, estado, estado_suc):
        """
        Método abstrato a ser implementado
        para o cálculo do custo de um estado
        para estado sucessor 
        """