from .comport_comp import ComportComp

"""
Representa o mecanismo de combinação e seleção de ações
baseado em hierarquia, onde os comportamentos estão 
organizados numa hierarquia fixa de subsunção, ou seja,
possui regras de prioridades fixas onde uma reação de 
alta prioridade substitui/suprime a reação de prioridade 
mais baixa
"""
class Hierarquia(ComportComp):
    """
    Método para selecionar uma ação de um conjunto de ações
    baseado em hierarquia
    Recebe uma coleção de ações onde já se encontram ordenadas
    """
    def selecionar_accao(self, accoes):
        if accoes:
            """ variável explicativa """
            accao = accoes[0]
            """ retorna a accao selecionada """
            return accao