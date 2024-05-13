from abc import ABC, abstractmethod
"""
objetivos -------------> planeador -> plano
modelo de planeamento ->

Representa o planeador de um agente deliberativo,
feito com o modelo do mundo e os objetivos.

// TODO Implementa um raciocínico ...
"""
class Planeador(ABC):
    # escolher procura A*
    @abstractmethod
    def planear(self, modelo_plan, objetivos):
        """
        Método para fazer o planeamento de um estado
        inicial até um estado objetivo
        """