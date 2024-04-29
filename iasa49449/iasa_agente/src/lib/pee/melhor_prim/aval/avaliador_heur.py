from .avaliador import Avaliador

"""
Representa o avaliador heurístico, este é especializado
pelo AvaliadorSof e AvaliadorAA.
"""
class AvaliadorHeur(Avaliador):

    """
    Guarda a heuristica recebida como parâmetro
    """
    def definir_heuristica(self, heuristica):
        self._heuristica = heuristica