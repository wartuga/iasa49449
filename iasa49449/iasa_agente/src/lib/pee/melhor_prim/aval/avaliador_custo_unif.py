from .avaliador import Avaliador

"""
Representa uma procura de custo uniforme, é uma
variante de procura melhor-primeiro
não informada.
"""
class AvaliadorCustoUnif(Avaliador):

    """
    Método para produzir a prioridade do nó
    """
    def prioridade(self, no):
        return no.custo