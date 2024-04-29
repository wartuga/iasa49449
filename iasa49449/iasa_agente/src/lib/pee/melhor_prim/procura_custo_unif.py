from .procura_melhor_prim import ProcuraMelhorPrim
from .aval.avaliador_custo_unif import AvaliadorCustoUnif

"""
Após execução de contagem.py usando ProcuraCustoUnif
o resultado apresentado é:
0 1
1 1
2 1
3 1
4 1
5 1
6 1
7 1
8 1
Custo da solução:  9
Dimensão da solução:  9
"""
"""
Representa uma procura de custo uniforme, é uma
variante de procura melhor-primeiro
não informada.
procura de custo uniforme -> f(n) = g(n)
minimização de custo acumulado até ao nó final
"""
class ProcuraCustoUnif(ProcuraMelhorPrim):

    """
    Construtor da classe
    """
    def __init__(self):
        super().__init__(AvaliadorCustoUnif())