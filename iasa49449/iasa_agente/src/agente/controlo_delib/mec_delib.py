from sae import Elemento

"""
estados são objetivos que o agente pretende atingir
Gera os objetivos, decidindo o que fazer.
Pretende-se atingir todas as posições dos alvos existentes.
"""
"""
Representa o mecanismo deliberativo.
Recebe uma representação do ambiente (modelo_mundo)
"""
class MecDelib:
    """
    Construtor da classe
    """
    def __init__(self, modelo_mundo):
        self.__modelo_mundo = modelo_mundo

    """
    método que retorna uma lista de estados cujo
    elemento é um alvo.
    """
    def deliberar(self):
        estados = self.__modelo_mundo.obter_estados()
        for estado in estados:
            if self.__modelo_mundo.obter_elemento(estado) != Elemento.ALVO:
                estados.remove(estado)
        return estados