from ecr.resposta import Resposta
from sae import Accao
"""
Especialização de resposta. Representa uma resposta de movimento na
qual produz uma ação com a direção recebida.
"""
class RespostaMover(Resposta):
    """
    Construtor da classe RespostaMover
    @param direcao - Direcao usada para gerar a acao
    @returns - RespostaMover
    """
    def __init__(self, direccao):
        """
        variavel explicativa, a direcao é uma acao
        """
        accao = Accao(direccao)
        """
        a resposta recebe uma acao, neste caso 
        em concreto, é uma direcao
        """
        super().__init__(accao)
