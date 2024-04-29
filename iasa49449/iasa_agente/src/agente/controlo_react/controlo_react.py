from sae import Controlo

"""
Representa o controlo reativo do agente. Neste projeto
o controlo consiste em receber uma percepção tem a reação
e após o seu processamento, gera uma ação.
"""
class ControloReact(Controlo):
    """
    Construtor da classe
    """
    def __init__(self, comportamento):
        self.__comportamento = comportamento
        """
        Flag para mostrar o que o agente está a visualizar 
        na posição atual (informação sensorial)
        """
        self.mostrar_per_dir = True

    """
    Método para retornar a Accao consoante a Percepcao recebida
    """
    def processar(self, percepcao):
        """ variável explicativa => maior simplicidade """
        accao = self.__comportamento.activar(percepcao)
        return accao