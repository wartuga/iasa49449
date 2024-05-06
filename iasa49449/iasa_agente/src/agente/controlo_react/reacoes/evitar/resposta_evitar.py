from agente.controlo_react.reacoes.resposta.resposta_mover import RespostaMover
from sae import Direccao
from random import choice

"""
Representa a resposta evitar um obstáculo
"""
class RespostaEvitar(RespostaMover):
    """
    Construtor da classe
    """
    def __init__(self, dir_inicial = Direccao.ESTE):
        self.__direccoes = list(Direccao)
        super().__init__(dir_inicial)

    """
    Método para o agente evitar a colisão com um obstáculo
    caso esteja numa direção que tenha um obstáculo,
    caso contrário, segue nessa direção
    """
    def activar(self, percepcao, intensidade):
        direccao = percepcao.contacto_obst(self._accao.direccao)
        if direccao:
            direccao_livre = self.__direccao_livre(percepcao)
            if direccao_livre:
                self._accao.direccao = direccao_livre
            else:
                return None
            
        return super().activar(percepcao, intensidade)

    """
    Método auxiliar para escolher uma direção livre
    """
    def __direccao_livre(self, percepcao):
        """
        simplificação da construção da lista de direções livres
        dir_livres2 = [direcao for direcao in self.__direcoes 
                       if not percepcao.contacto_obst(direcao)]
        """
        dir_livres = []
        for direccao in self.__direccoes:
            if percepcao.contacto_obst(direccao):
                continue
            else:
                dir_livres.append(direccao)
        return choice(dir_livres)