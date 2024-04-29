"""
Representa um no de uma árvore de um mecanismo de procura.
"""
class No:
    """
    Construtor da classe
    """
    def __init__(self, estado, operador = None, antecessor = None, custo = 0):
        if antecessor:
            self.__profundidade = antecessor.profundidade + 1
        else:
            self.__profundidade = 0
        self.__antecessor = antecessor
        self.__custo = custo
        self.__estado = estado
        self.__operador = operador

    """
    Propriedade estado do nó
    """
    @property
    def estado(self):
        return self.__estado
    
    """
    Propriedade operador do nó
    """
    @property
    def operador(self):
        return self.__operador
    
    """
    Propriedade antecessor do nó
    Representa o no antecessor do nó
    """
    @property
    def antecessor(self):
        return self.__antecessor

    """
    Propriedade profundidade do nó
    Representa o nivel do nó na árvore
    """
    @property
    def profundidade(self):
        return self.__profundidade
    
    """
    Propriedade custo do nó
    Representa o custo do nó atual
    """
    @property
    def custo(self):
        return self.__custo
    
    """
    Necessário para ser possível existir uma
    possível comparação entre duas instâncias
    de No sendo este necessário na ProcuraCustoUnif
    """
    def __lt__(self, no):
        return self.custo < no.custo