from pee.mec_proc.fronteira import Fronteira

"""
Representação de uma fronteira com modelo LIFO
pois é uma implementação em profundidade
"""
class FronteiraLIFO(Fronteira):
    
    """
    Para inicializar o modelo de dados visto que é
    feito no init da classe Fronteira
    """
    def __init__(self):
        super().__init__()

    """
    Implementação do método inserir em modo LIFO
    """
    def inserir(self, no):
        self._nos.insert(0, no)