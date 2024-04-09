from agente.controlo_react.reacoes.resposta.resposta_mover import RespostaMover
from sae.ambiente.direccao import Direccao
from random import choice

"""
Representa a resposta evitar um obstáculo
"""
class RespostaEvitar(RespostaMover):
    """
    Construtor da classe
    """
    def __init__(self, dir_inicial = Direccao.ESTE):
        self.__direcoes = list(Direccao)
        super().__init__(dir_inicial)

    """
    Método para o agente evitar a colisão com um obstáculo
    caso esteja numa direção que tenha um obstáculo,
    caso contrário, segue nessa direção
    """
    def ativar(self, percepcao, intensidade):
        direcao = percepcao.contacto_obst(self._acao.direccao)
        if direcao:
            direcao_livre = self.__direcao_livre(percepcao)
            if direcao_livre:
                self._acao.direccao = direcao_livre
            else:
                return None
            
        return super().ativar(percepcao, intensidade)

    """
    Método auxiliar para escolher uma direção livre
    """
    def __direcao_livre(self, percepcao):
        """
        simplificação da construção da lista de direções livres
        dir_livres2 = [direcao for direcao in self.__direcoes 
                       if not percepcao.contacto_obst(direcao)]
        """
        dir_livres = []
        for direcao in self.__direcoes:
            if percepcao.contacto_obst(direcao):
                continue
            else:
                dir_livres.append(direcao)
        return choice(dir_livres)