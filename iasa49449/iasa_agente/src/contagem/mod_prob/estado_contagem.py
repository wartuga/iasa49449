from mod.estado import Estado

"""
mantem o estado da contagem
convem ter acesso apenas de leitura
o valor do estado
"""
"""
Representa o estado de uma contagem
"""
class EstadoContagem(Estado):
    """
    Construtor da classe
    """
    def __init__(self, valor):
        self.__valor = valor

    """
    Propriedade valor da contagem
    """
    @property
    def valor(self):
        return self.__valor

    """
    Retorna o id do estado da contagem.
    Por serem inteiros, pode-se retornar
    o próprio valor.
    """
    def id_value(self):
        return self.__valor