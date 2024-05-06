from abc import ABC, abstractmethod

"""
Representa o Comportamento da arquitetura de agentes reativos
Um comportamento relaciona padrões de percepção com padrões de ação
Existem dois tipos de comportamento:
    comportamento simples e comportamento composto
"""
class Comportamento(ABC):
    @abstractmethod
    def activar(self, percepcao):
        """
        Método da interface Comportamento
        Recebe uma Percepcao
        Retorna uma Accao
        """