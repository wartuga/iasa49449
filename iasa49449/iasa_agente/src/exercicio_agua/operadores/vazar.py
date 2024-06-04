from .transferir import Transferir

class Vazar(Transferir):
    """
    
    """
    def aplicar(self, estado):
        resultado = estado.id_value() - self.volume
        if resultado < 0:
            return 0