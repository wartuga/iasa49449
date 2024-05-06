from mod.operador import Operador
from sae import Accao
from math import sin, cos, dist
from estado_agente import EstadoAgente

"""
Representa o operador mover, especialização de operador.
Operadores são representações de ações para simular 
Nota: No ambiente que temos o y cresce de cima para baixo
"""
class OperadorMover(Operador):
    """
    Construtor da classe
    """
    def __init__(self, modelo_mundo, direccao):
        self.__modelo_mundo = modelo_mundo
        self.__accao = Accao(direccao)
        
    """
    Aplica uma transalação geométrica à posição
    do estado atual, resultando num novo estado
    com a nova posição 
    """
    def aplicar(self, estado):
        posicao = estado.posicao
        nova_posicao_x = posicao.x + round(self.accao.passo * cos(self.ang))
        nova_posicao_y = posicao.y + round(-self.accao.passo * sin(self.ang))
        estado = EstadoAgente(nova_posicao_x, nova_posicao_y)
        if estado in self.__modelo_mundo.obter_estados():
            return estado
    
    """
    Representa o custo entre os dois estados recebidos
    neste caso esse custo é representado através da distância
    """
    def custo(self, estado, estado_suc):
        return dist(estado.posicao, estado_suc.posicao)

    """
    Propriedade ang do operador, representa o ângulo
    da ação(movimento) do agente
    """
    @property
    def ang(self):
        return self.__accao.ang
    
    """
    Propriedade ação do operador, representa a
    ação(movimento) do agente
    """
    @property
    def accao(self):
        return self.__accao