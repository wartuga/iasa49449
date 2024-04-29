from ecr.estimulo import Estimulo

"""
Representa o estimulo de encontrar um obstaculo numa
determinada direção
"""
class EstimuloObst(Estimulo):
    def __init__(self, direcao, intensidade = 1):
        self.__direcao = direcao
        self.__intensidade = intensidade

    """
    Caso esteja em contacto com um obstáculo, retorna
    a sua intensidade, caso contrário retorna 0
    """
    def detetar(self, percepcao):
        if percepcao.contacto_obst(self.__direcao):
            intensidade = self.__intensidade
        else:
            intensidade = 0

        return intensidade