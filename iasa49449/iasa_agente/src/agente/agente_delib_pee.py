from sae import Agente
from .controlo_delib.controlo_delib import ControloDelib
from plan.plan_pee.planeador_pee import PlaneadorPEE

"""
Representa um agente reativo, uma possível extensão de Agente.
Este agente terá o comportamento complexo recolher e o seu 
controlo será uma instância de ControloReact recebendo esse 
mesmo comportamento.
"""
class AgenteDelibPEE(Agente):
    def __init__(self):
        """
        geração do comportamento
        """
        planeador = PlaneadorPEE()
        """
        Variável explicativa
        """
        controlo = ControloDelib(planeador)
        """
        injeção de dependência de Controlo
        """
        super().__init__(controlo)