from mod.estado import Estado

"""
Representa o estado do agente.
Especialização de estado.

implementa id_valor e tem uma posição
para a distância deste
"""
class EstadoAgente(Estado):
    """
    Construtor da classe
    """
    def __init__(self, posicao):
        self.__posicao = posicao

    """
    Definição do valor identificador do estado do agente
    """
    def id_value(self):
        return hash(self.__posicao)

    """
    Propriedade posição do agente
    """
    @property
    def posicao(self):
        return self.__posicao