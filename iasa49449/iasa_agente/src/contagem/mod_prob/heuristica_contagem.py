from pee.melhor_prim.aval.heuristica import Heuristica

"""
Representa a heurística concreta para o problema
da contagem, possuindo o construtor a receber o 
valor final e o método h retorna a distância, 
sendo esta o valor absoluto da diferença do valor
final e do valor do estado recebido
"""
class HeuristicaContagem(Heuristica):

    """
    Construtor da classe
    """
    def __init__(self, valor):
        self.__valor = valor

    """
    Método para cálculo da distância entre o 
    valor final e o valor do estado recebido
    """
    def h(self, estado):
        return abs(self.__valor - estado.valor)