from sae import Agente
from .controlo_react.controlo_react import ControloReact
from .controlo_react.reacoes.recolher import Recolher

"""
Representa um agente reativo, uma possível extensão de Agente
"""
class AgenteReativo(Agente):
    def __init__(self):
        """
        geração do comportamento
        """
        comportamento = Recolher()
        """
        Variável explicativa
        """
        controlo = ControloReact(comportamento)
        """
        Mostra o que o agente está a visualizar na posição atual
        """
        controlo.mostrar_per_dir = True
        """
        injeção de dependência de Controlo
        """
        super().__init__(controlo)