from pee.mec_proc.fronteira import Fronteira

"""
Representação de uma fronteira com modelo FIFO
pois é uma implementação em largura
"""
class FronteiraFIFO(Fronteira):
    
    """
    Para inicializar o modelo de dados visto que é
    feito no init da classe Fronteira
    """
    def __init__(self):
        super().__init__()

    """
    Implementação do método inserir em modo FIFO
    """
    def inserir(self, no):
        self._nos.append(no)