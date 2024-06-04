from .transferir import Transferir

class Encher(Transferir):
    """
    
    """
    def aplicar(self, estado):
        return estado.id_value() + self.volume