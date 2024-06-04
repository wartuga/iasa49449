from plan.modelo.modelo_plan import ModeloPlan
from pdm.modelo.modelo_pdm import ModeloPDM

"""
Método para representar o modelo de um plano PDM
onde procede à implementação dos métodos abstratos
da classe ModeloPlan e ModeloPDM
"""
class ModeloPDMPlan(ModeloPlan, ModeloPDM):
    """
    Construtor da classe
    """
    def __init__(self, modelo_plan, objetivos, rmax = 1000):
        self.__modelo_plan = modelo_plan
        self.__objetivos = objetivos
        self.__rmax = rmax
        
        """
        dicionário de estado, ação como chave e estado seguinte como valor
        de forma a que todas as transições sejam pré-calculadas
        e o funcionamento de T e R seja mais eficiente
        """
        self.__transicoes = {
            (s, a): a.aplicar(s)
            for s in self.obter_estados()
            for a in self.obter_operadores()
        }

    """
    Método para obter o estado
    """
    def obter_estado(self):
        return self.__modelo_plan.obter_estado()
    
    """
    Método para obter as estados possíveis
    """
    def obter_estados(self):
        return self.__modelo_plan.obter_estados()
    
    """
    Método para obter os operadores
    """
    def obter_operadores(self):
        return self.__modelo_plan.obter_operadores()
    
    """
    Método para obter os estados possíveis
    """
    def S(self):
        return self.obter_estados()
    
    """
    Método para obter as ações possíveis
    """
    def A(self, s):
        return self.obter_operadores() if s not in self.__objetivos else []
    
    """
    Método para obter a transição
    """
    # modelo deterministico
    def T(self, s, a, sn):
        return 1 if self.__transicoes.get((s, a)) == sn else 0
    
    """
    Método para obter a recompensa
    """
    def R(self, s, a, sn):
        return self.__rmax if sn in self.__objetivos else -a.custo(s, sn)
    
    """
    Método para obter o estado seguinte
    """
    # determinístico
    def suc(self, s, a):
        sn = self.__transicoes.get((s, a))
        return [sn] if sn else []