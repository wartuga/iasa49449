from .avaliador_heur import AvaliadorHeur

"""
Representa o avaliador heurístico da procura A* 
"""
class AvaliadorAA(AvaliadorHeur):
    """
    Método para produzir a prioridade de um nó seguindo 
    o modelo de A* sendo que este é f(n) = g(n) + h(n)
    """
    def prioridade(self, no):
        estado = no.estado
        custo = no.custo
        return self._heuristica.h(estado) + custo