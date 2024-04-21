from pee.mec_proc.passo_solucao import PassoSolucao
from collections import deque 
"""
Representa a solução de um problema.
Tem como propriedades o custo total e a dimensão da solução.
Possui ainda os passos, que é um PassoSolucao para cada nó da soluçáo,
é iterável.
""" 
class Solucao:

    def __init__(self, no_final):
        self.__custo = no_final.custo
        self.__dimensao = no_final.profundidade
        # uma doubly ended queue(dequeue) is preferred over a list in this case
        # since we are walking through the nodes and starting in the last one
        # with a deque we have a O(1) complexity in append and pop operations
        # we dont need to do: list.reverse() since we can appendLeft()
        self.__passos = deque([])
        no = no_final
        while no.antecessor:
            self.__passos.appendleft(PassoSolucao(no.estado, no.operador))
            no = no.antecessor
        self.__passos.appendleft(PassoSolucao(no.estado, no.operador))
    
    @property
    def custo(self):
        return self.__custo
    
    @property
    def dimensao(self):
        return self.__dimensao
    
    def __iter__(self):
        iter(self.__passos)

    def __getitem__(self, index):
        return self.__passos[index]
