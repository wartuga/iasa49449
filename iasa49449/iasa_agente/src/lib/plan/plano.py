from abc import ABC, abstractmethod

"""
objetivos -------------> planeador -> plano
modelo de planeamento ->

Representa o plano de um agente deliberativo,
resultado através do estado do planeador
"""
class Plano(ABC):

    @abstractmethod
    def obter_accao(self, estado):
        """
        Obtem o operador segundo o estado recebido
        """

    @abstractmethod
    def mostrar(self, vista):
        """
        Método para mostrar o plano com base na 
        vista recebida
        """