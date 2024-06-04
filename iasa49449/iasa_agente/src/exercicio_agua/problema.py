from mod.problema import Problema
from .estado import EstadoDeposito
from .operadores.encher import Encher
from .operadores.vazar import Vazar
"""
2 vasos
1 vaso de 3 litros que é possível encher e vazar o depósito
1 vaso de 2 litros que é possível encher e vazar o depósito

o depósito tem 10 litros de água


"""
class Deposito(Problema):

    def __init__(self, volume_inical, volume_final):
        super().__init__(EstadoDeposito(volume_inical), [Encher(2), Encher(3), Vazar(2), Vazar(3)])
        self.__volume_final = volume_final

    def objetivo(self, estado):
        return 1 if estado.id_value() == self.__volume_final else 0