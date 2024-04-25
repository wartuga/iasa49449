from pee.mec_proc.passo_solucao import PassoSolucao

"""
Representa a solução de um problema.
Tem como propriedades o custo total e a dimensão da solução.
Possui ainda os passos, que é um PassoSolucao para cada nó da soluçáo,
é iterável.
""" 
class Solucao:

    """
    Construtor da classe
    """
    def __init__(self, no_final):
        self.__custo = no_final.custo
        self.__dimensao = no_final.profundidade

        # complexidade desnecessária
        # self.__passos = deque([])

        self.__passos = []
        no = no_final
        while no.antecessor:
            """
            adicionar em passos, o PassoSolução com o estado do nó anterior e o operador do nó atual simbolizando
            o operador necessário para se passar do estado do nó anterior para o estado do nó atual
            """
            self.__passos.insert(0, PassoSolucao(no.antecessor.estado, no.operador))
            #self.__passos.appendleft(PassoSolucao(no.antecessor.estado, no.operador))

            no = no.antecessor
    
    """
    Propriedade readable do custo da solução
    """
    @property
    def custo(self):    
        return self.__custo
    
    """
    Propriedade readable da dimensão da solução
    """
    @property
    def dimensao(self):
        return self.__dimensao
    
    """
    Para ser iterável é necessário dar override ao método __iter__ da classe
    """
    def __iter__(self):
        return iter(self.__passos)

    """
    Método para ir buscar um elemento da posição index
    Estamos a usar a sobrecarga do operador
    """
    def __getitem__(self, index):
        return self.__passos[index]