from plan.plano import Plano

"""
Classe para representar o plano PDM (Planeamento de Decisão de Markov)
e que implementa a interface de plano
Este tem como objetivo obter o operador para um estado consoante a politica
"""
class PlanoPDM(Plano):
    """
    Contrutor da classe
    """
    def __init__(self, utilidade, politica):
        self.__utilidade = utilidade
        self.__politica = politica

    """
    Método para obter o operador para um estado consoante a politica
    """
    def obter_accao(self, estado):
        if self.__politica:
            return self.__politica.get(estado)
    
    """
    Método para mostrar o plano
    """
    def mostrar(self, vista):
        # Verificar se existe politica
        if self.__politica:
            # Mostrar a utilidade
            for estado, valor in self.__utilidade.items():
                vista.mostrar_valor_posicao(estado.posicao, valor)

            # Mostrar a politica
            for estado, acao in self.__politica.items():
                vista.mostrar_vector(estado.posicao, acao.ang)