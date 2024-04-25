from pee.mec_proc.fronteira import Fronteira

"""
Representa a fronteira de prioridade necessária
para a lógica da procura melhor primeiro
uma vez que será envolvido o valor do custo
de cada operador
"""
class FronteiraPrioridade(Fronteira):
    """
    Construtor da classe
    """
    def __init__(self):
        raise NotImplementedError

    """
    Método para inserir um nó na coleção
    da fronteira
    """
    def inserir(self, no):
        raise NotImplementedError

    """
    Método para remover o nó com menor custo,
    sendo este o primeiro elemento da coleção
    """
    def remover(self):
        raise NotImplementedError