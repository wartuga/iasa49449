from sae.ambiente.elemento import Elemento
from ecr.estimulo import Estimulo

"""
Representa o estimulo de encontrar um alvo
na posição atual do agente
"""
class EstimuloAlvo(Estimulo):
    """
    Construtor da classe EstimuloAlvo
    """
    def __init__(self, direcao, gama = 0.9):
        self.__direcao = direcao
        self.__gama = gama

    """
    método para retornar a intensidade consoante
    a percepcao recebida
    se existir um alvo numa determinada direçao
    tem de retornar um intensidade
    que é a inversa da distancia (gama^dist)
    caso contrário, a prioridade retornada é 0
    """
    def detetar(self, percepcao):
        (elemento, distancia, _) = percepcao[self.__direcao]
        if elemento == Elemento.ALVO:
            intensidade = self.__gama**distancia
        else:
            intensidade = 0
        """
        numa programação estruturada é boa prática
        ter um único ponto de entrada e um único 
        ponto de saída, tornando o código mais simples
        e claro para debug
        
            return intensidade
        return 0
        """
        return intensidade