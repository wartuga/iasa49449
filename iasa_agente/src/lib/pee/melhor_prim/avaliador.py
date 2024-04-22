from abc import ABC, abstractmethod

"""
Representa o avaliador usado para cada nó
"""
class Avaliador(ABC):
    
    @abstractmethod
    def prioridade(self, no):
        raise NotImplementedError