from .procura_informada import ProcuraInformada
from .aval.avaliador_aa import AvaliadorAA

"""
Representa a Procura A* que é uma variante da procura
melhor-primeiro, esta sendo uma heurística admissível
(otimista), com minimização de custo global.
A estimativa de custo é sempre inferior ou igual ao 
custo efetivo mínimo 
Garante uma solução ótima com a melhor eficiência 
computacional.
Não é tão seletiva como a procura sôfrega mas é mais 
eficiente que a pesquisa uniforme.
0 <= h(n) <= h*(n)
"""
class ProcuraAA(ProcuraInformada):
    """
    Construtor da classe
    """
    def __init__(self):
        super().__init__(AvaliadorAA())