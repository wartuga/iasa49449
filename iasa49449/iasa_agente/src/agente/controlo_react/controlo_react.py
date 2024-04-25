from sae import Controlo

"""
Representa o controlo reativo do agente
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
    Método para retornar a Acao consoante a Percepcao passada
    """
    def processar(self, percepcao):
        """ variável explicativa => maior simplicidade """
        acao = self.__comportamento.ativar(percepcao)
        return acao