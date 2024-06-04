from sae import Agente
from .controlo_delib.controlo_delib import ControloDelib
from plan.plan_pdm.planeador_pdm import PlaneadorPDM

class AgenteDelibPDM(Agente):
    def __init__(self):
        planeador = PlaneadorPDM()
        controlo = ControloDelib(planeador)
        super().__init__(controlo)