from pee.mec_proc.fronteira import Fronteira

"""
Representação de uma fronteira com modelo FIFO
pois é uma implementação em largura
"""
class FronteiraFIFO(Fronteira):

    """
    Implementação do método inserir em modo FIFO
    """
    def inserir(self, no):
        self._nos.append(no)