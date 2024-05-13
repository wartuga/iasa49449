from abc import ABC, abstractmethod

"""
Representa o contrato para existência de 
compatibilidade entre o planeador e o 
modelo mundo
"""
class ModeloPlan(ABC):

    @abstractmethod
    def obter_estado(self):
        """
        Método para obter o estado
        do plano 
        """

    @abstractmethod
    def obter_estados(self):
        """
        Método para obter os estados
        possiveis do plano 
        """

    @abstractmethod
    def obter_operadores(self):
        """
        Método para obter os operadores
        do plano 
        """