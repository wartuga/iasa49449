from .avaliador_heur import AvaliadorHeur

"""
Representa o avaliador heurístico da procura Sôfrega(Greedy Search)
"""
class AvaliadorSof(AvaliadorHeur):

    """
    Método para produzir a prioridade de um nó seguindo 
    o modelo de A* sendo que este é f(n) = h(n)
    """
    def prioridade(self, no):
        estado = no.estado
        return self._heuristica.h(estado)