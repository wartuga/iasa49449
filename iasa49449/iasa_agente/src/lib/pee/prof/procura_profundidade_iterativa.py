from .procura_profundidade_limitada import ProcuraProfLim

"""
Representa a procura em profundidade Iterativa, ou seja,
Chama a procura em profundidade limitada até limite_prof + 1
vezes ou até encontrar a solução
"""
class ProcuraProfIter(ProcuraProfLim):

    """
    Método procurar onde é fazer várias vezes a procura
    da procura profundidade limitada aumentando a sua 
    profundidade a cada iteração
    """
    def procurar(self, problema, inc_prof = 1, limite_prof = 1000):
        for profundidade in range(0, limite_prof + 1, inc_prof):
            self.prof_max = profundidade
            solucao = super().procurar(problema)
            if solucao:
                return solucao