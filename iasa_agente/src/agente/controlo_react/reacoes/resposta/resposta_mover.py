from ecr.resposta import Resposta
from sae import Accao
"""
representa uma resposta de movimento na direção indicada
"""
class RespostaMover(Resposta):
    """
    Construtor da classe RespostaMover
    @param direcao - Direcao usada para gerar a acao
    @returns - RespostaMover
    """
    def __init__(self, direcao):
        """
        variavel explicativa, a direcao é uma acao
        """
        acao = Accao(direcao)
        """
        a resposta recebe uma acao, neste caso 
        em concreto, é uma direcao
        """
        super().__init__(acao)
