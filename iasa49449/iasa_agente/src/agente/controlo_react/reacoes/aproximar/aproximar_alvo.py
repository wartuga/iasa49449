from ecr.prioridade import Prioridade
from sae import Direccao
from agente.controlo_react.reacoes.aproximar.aproximar_dir import AproximarDir

"""
Representa a reação de aproximação de um alvo
É um sub-objetivo de Recolher
"""
class AproximarAlvo(Prioridade):
    """
    Construtor da classe Aproximar
    """
    def __init__(self):
        # simplificação de código
        comportamentos = [AproximarDir(direccao) for direccao in Direccao]
        """
        comportamentos = [
            AproximarDir(Direccao.NORTE), 
            AproximarDir(Direccao.SUL), 
            AproximarDir(Direccao.ESTE), 
            AproximarDir(Direccao.OESTE)
        ]
        """
        # alteração devido a redundância
        # motivo: estava a selecionar o comportamento
        # porém o activar da Prioridade já o faz
        super().__init__(comportamentos)