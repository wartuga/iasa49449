from ecr.hierarquia import Hierarquia
from agente.controlo_react.reacoes.evitar.resposta_evitar import RespostaEvitar
from agente.controlo_react.reacoes.evitar.evitar_dir import EvitarDir
from sae.ambiente.direccao import Direccao

"""
// meter comentários sobre os apontamentos da aula
"""
"""
Representa a reação de evitar um obstaculo
É um sub-objetivo de Recolher
"""
class EvitarObst(Hierarquia):
    def __init__(self):
        self.__resposta = RespostaEvitar()

        """
        redução de complexidade ao construir a lista com as direções possíveis
        pois teria de se construir algum tipo de coleção para iterar sobre as direções
        """
        comportamentos = [EvitarDir(direcao, self.__resposta) for direcao in list(Direccao)]

        super().__init__(comportamentos)