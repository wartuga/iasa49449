from .comportamento import Comportamento
from abc import abstractmethod

"""
Representa o commportamento complexo de uma arquitetura de agentes reativos.
Implementa Comportamento.
Um comportamente composto pode ser composto por comportamentos simples ou 
por outros comportamentos complexos.
"""
class ComportComp(Comportamento):
    """
    Construtor de ComportComp
    Recebe uma coleção de comportamentos.
    """
    def __init__(self, comportamentos):
        self.__comportamentos = comportamentos

    """
    Método para activar todos os comportamentos que se ativam
    devido à Percepcao recebida e retorna uma accao
    """
    def activar(self, percepcao):
        accoes = []
        for comportamento in self.__comportamentos:
            accao = comportamento.activar(percepcao)
            if accao:
                accoes.append(accao)
        if accoes:
            """ variável explicativa => aumenta a simplicidade """
            accao = self.selecionar_accao(accoes)
            return accao
    
    @abstractmethod
    def selecionar_accao(self, accoes):
        """
        Método para selecionar uma Accao numa coleção de ações
        """