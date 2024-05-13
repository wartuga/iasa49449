"""
Representa um plano de solução baseado num mecanismo
de procura melhor primeiro
"""
class PlanoPEE:
    """
    Construtor da classe
    """
    def __init__(self, solucao):
        # simplificação de arquitetura feita pelo professor
        self.__passos = [passo for passo in solucao]
    
    """
    Nota: passos tem estado e operadores
    Método para obter o operador que contém a ação
    """
    def obter_accao(self, estado):
        if self.__passos:
            passo = self.__passos.pop(0)
            if passo.estado == estado:
                return passo.operador
    
    """
    Método para verificar se o estado recebido
    é válido ou não
    """
    def valido(self, estado):
        raise NotImplementedError

    """
    Método para mostrar o plano com base na vista
    recebida como parametro
    """
    def mostrar(self, vista):
        if self.__passos:
            for passo in self.__passos:
                vista.mostrar_vector(passo.estado.posicao, passo.operador.ang)