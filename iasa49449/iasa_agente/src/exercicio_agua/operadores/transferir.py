from abc import abstractmethod
from mod.operador import Operador

class Transferir(Operador):
    """
    construtor recebe o volume transferido
    """
    def __init__(self, volume):
        self.volume = volume

    @abstractmethod
    def aplicar(self, estado):
        """
        método abstrato aplicar para ser implementado
        """

    """
    método para calcular o custo associado a cada operador
    """
    def custo(self, estado, estado_seguinte):
        return (estado_seguinte.id_value() - estado.id_value()) * (estado_seguinte.id_value() - estado.id_value())