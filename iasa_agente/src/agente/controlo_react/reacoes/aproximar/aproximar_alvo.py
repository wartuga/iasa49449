from ecr.prioridade import Prioridade
from sae.ambiente.direccao import Direccao
"""
Representa a reação de aproximação de um alvo
É um sub-objetivo de Recolher
"""
class AproximarAlvo(Prioridade):
    """
    Construtor da classe Aproximar
    """
    def __init__(self, ):
        comportamentos = [
            AproximarDir(Direccao.NORTE), 
            AproximarDir(Direccao.SUL), 
            AproximarDir(Direccao.ESTE), 
            AproximarDir(Direccao.OESTE)
        ]
        super().__init__().selecionar_acao(comportamentos)