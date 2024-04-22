from abc import abstractmethod

"""
Representação da fronteira da árvore
"""
class Fronteira:
    """
    Construtor da classe
    """
    def __init__(self):
        self.iniciar()
    
    """
    Propriedade vazia de fronteira
    Retorna True se a dimensão da 
    coleção de nós for de tamanho 0
    caso contrário, retorna False
    """
    @property
    def vazia(self):
        return self.dimensao == 0
    
    """
    Propriedade dimensão de fronteira
    Representa a quantidade de nós 
    presentes na coleção
    """
    @property
    def dimensao(self):
        return len(self._nos)

    """
    Método para iniciar a fronteira
    """
    def iniciar(self):
        self._nos = list()
    
    """
    Método abstrato para realizar a 
    inserção na estrutura de dados
    """
    @abstractmethod
    def inserir(self, no):
        raise NotImplementedError
    
    """
    Método para realizar a remoção do
    primeiro elemento da estrutura de dados
    """
    def remover(self):
        if self.dimensao > 0:
            return self._nos.pop(0)