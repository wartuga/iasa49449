from ecr.estimulo import Estimulo

"""
Representa o estimulo de encontrar um obstaculo numa
determinada direção
"""
class EstimuloObst(Estimulo):
    """
    Construtor da classe
    """
    def __init__(self, direccao, intensidade = 1):
        self.__direccao = direccao
        self.__intensidade = intensidade

    """
    Caso esteja em contacto com um obstáculo, retorna
    a sua intensidade, caso contrário retorna 0
    """
    def detectar(self, percepcao):
        if percepcao.contacto_obst(self.__direccao):
            intensidade = self.__intensidade
        else:
            intensidade = 0

        return intensidade