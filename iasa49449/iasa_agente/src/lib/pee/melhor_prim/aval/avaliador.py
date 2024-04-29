from abc import ABC, abstractmethod

"""
Representa o avaliador usado para cada nó.
Neste caso concreto o avaliador será o custo associado a cada nó,
este custo é o custo acumulado até ao nó
"""
class Avaliador(ABC):
    
    @abstractmethod
    def prioridade(self, no):
        """
        Método abstrato para avaliar a prioridade do nó
        """