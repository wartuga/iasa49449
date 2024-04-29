from pee.melhor_prim.procura_melhor_prim import ProcuraMelhorPrim

"""
Representa uma procura informada, tendo esta a noção
da distância/custo do nó atual até ao objetivo fazendo
uso da heurística
"""
class ProcuraInformada(ProcuraMelhorPrim):
    """
    Método procurar para produzir uma solução, com uma
    nova heurística recebida como parâmetro no problema
    também recebido como parâmetro
    """
    def procurar(self, problema, heuristica):
        # alteramos a heuristica de forma dinâmica
        self._avaliador.definir_heuristica(heuristica)
        # podemos usar o método procurar usando a nova heurística
        # este método procurar é do método MecanismoProcura
        return super().procurar(problema)