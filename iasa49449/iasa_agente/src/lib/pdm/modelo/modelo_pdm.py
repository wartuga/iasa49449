from abc import ABC, abstractmethod

"""
Representa um modelo de um processo de decisáo de Markov (PDM).
Este tem S que é o conjunto de estados, A que é o conjunto de acções,
T que é a função de transição, R que é a função de recompensa e
suc que é a função para estados sucessores.
"""
class ModeloPDM(ABC):

    @abstractmethod
    def S(self):
        """
        Retorna a lista de estados possíveis
        """

    @abstractmethod
    def A(self, s):
        """
        Retorna a lista de acções possíveis para um estado
        """

    @abstractmethod
    def T(self, s, a, sn):
        """
        Retorna a probabilidade de transição para um estado sucessor
        """

    @abstractmethod
    def R(self, s, a, sn):
        """
        Retorna a probabilidade de obter o valor da recompensa
        """

    """
    Retorna a lista de estados sucessores
    """
    def suc(self, s, a):
        return [sn for sn in self.S() if self.T(s, a, sn) > 0]