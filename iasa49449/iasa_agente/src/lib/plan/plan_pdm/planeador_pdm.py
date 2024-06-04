from pdm.pdm import PDM
from .modelo.modelo_pdm_plan import ModeloPDMPlan
from plan.plan_pdm.plano_pdm import PlanoPDM
from plan.planeador import Planeador

"""
Classe que representa um planeador PDM
e que implementa a interface de planeador
"""
class PlaneadorPDM(Planeador):
    """
    Construtor da classe
    """
    def __init__(self, gama = 0.85, delta_max = 1):
        self.__gama = gama
        self.__delta_max = delta_max

    """
    Método para gerar um plano PDM através da resolução de um PDM
    em que lhe é passado um modelo de plano e os objetivos
    """
    def planear(self, modelo_plan, objetivos):
        if objetivos:
            modelo_pdm = ModeloPDMPlan(modelo_plan, objetivos)
            pdm = PDM(modelo_pdm, self.__gama, self.__delta_max)
            utilidade, politica = pdm.resolver()
            plano_pdm = PlanoPDM(utilidade, politica)
            return plano_pdm