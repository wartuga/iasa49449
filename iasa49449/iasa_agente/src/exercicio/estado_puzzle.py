from mod.estado import Estado

"""
Classe representante do estado de um puzzle
"""
class EstadoPuzzle(Estado):
    """
    Construtor da classe
    """
    def __init__(self, estado_inicial):
        self.estado_inicial = estado_inicial

    """
    Implementação do método id_value para se conseguir
    para cada combinação umm valor diferente
    Retorna um valor inteiro em base 10 representando
    cada posição do puzzle
    """
    def id_value(self):
        res = 0
        i = 0
        for peca in self.estado_inicial:
            res += peca * 10**i
        return res
