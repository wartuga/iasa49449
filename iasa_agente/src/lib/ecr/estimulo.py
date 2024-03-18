from abc import ABC, abstractmethod

"""
Representação de um Estimulo de uma arquitetura de 
agentes reativos
O estimulo é um elemento da Percepcao e pode gerar
uma resposta através de associação
"""
class Estimulo(ABC):

    @abstractmethod
    def detetar(self, percepcao) -> float:
        """
        Método da interface Estimulo
        Recebe uma `Percepcao` e retorna um `float`
        representanto a prioridade da ação
        """