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
    Método para ativar todos os comportamentos que se ativam
    devido à Percepcao recebida e retorna uma acao
    """
    def ativar(self, percepcao):
        acoes = []
        for comportamento in self.__comportamentos:
            acao = comportamento.ativar(percepcao)
            if acao:
                acoes.append(acao)
        if acoes:
            """ variável explicativa => aumenta a simplicidade """
            acao = self.selecionar_acao(acoes)
            return acao
    
    """
    Método para selecionar uma Acao numa coleção de ações
    """
    @abstractmethod
    def selecionar_acao(acoes):
        raise NotImplementedError