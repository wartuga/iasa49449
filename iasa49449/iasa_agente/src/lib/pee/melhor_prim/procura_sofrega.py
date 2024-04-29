from .procura_informada import ProcuraInformada
from .aval.avaliador_sof import AvaliadorSof

"""
Representa a Procura Sôfrega que é uma variante 
da procura melhor-primeiro, é diferente da procura
de custo uniforme, é informada, possui uma solução 
sub-ótima e uma menor complexidade computacional.
É exponencialmente mais eficiente que a procura de 
custo uniforme
"""
class ProcuraSofrega(ProcuraInformada):

    """
    Construtor da classe
    """
    def __init__(self):
        super().__init__(AvaliadorSof())