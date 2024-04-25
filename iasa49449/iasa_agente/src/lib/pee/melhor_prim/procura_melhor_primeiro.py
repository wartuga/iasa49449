from pee.mec_proc.procura_grafo import ProcuraGrafo

"""
Procura melhor primeiro (best-first)
Utiliza uma função f de avaliação de cada nó gerado
f(n) >= 0
tipicamente f(n) representa uma estimativa do custo
da solução através do nó n

A fronteira de exploração é ordenada por odem cescente 
de f(n) (maior => pior)
Explora primeiro os melhores percursos
envolve o custo

vai se alterar o método manter
"""
"""
Representa a procura melhor primeiro
Sendo uma especialização de uma procura
em grafo
"""
class ProcuraMelhorPrim(ProcuraGrafo):

    """
    Construção da classe
    """
    def __init__(self):
        raise NotImplementedError

    """
    Alteração do método manter, adicionando o
    resto da condição necessária para a procura
    melhor primeiro, pois a procura em prioridade
    tem apenas parte dessa condição, logo basta 
    uma extensao da condição, aproveitando o que 
    a super classe já tem
    """
    def _manter(self, no):
        return super()._manter(no) or no.custo < self._explorados[no.estado].custo