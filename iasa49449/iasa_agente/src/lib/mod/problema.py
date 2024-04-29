from abc import ABC, abstractmethod

"""
Representação de um problema.
Contém os operadores e o estado inicial.
"""
class Problema(ABC):
    """
    Construtor da classe
    """
    def __init__(self, estado_inicial, operadores):
        self.__estado_inicial = estado_inicial
        self.__operadores = operadores
    
    """
    Propriedade estado_inicial de problema
    Representa o estado inicial doproblema
    """
    @property
    def estado_inicial(self):
        return self.__estado_inicial
    
    """
    Propriedade operadores de problema
    Representa as ações do problema
    """
    @property
    def operadores(self):
        return self.__operadores

    @abstractmethod
    def objetivo(self, estado):
        """
        Método abstrato objetivo para ser implementado
        consoante o problema em questão
        """