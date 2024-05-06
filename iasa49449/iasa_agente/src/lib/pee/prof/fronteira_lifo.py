from pee.mec_proc.fronteira import Fronteira

"""
Representação de uma fronteira com modelo LIFO
pois é uma implementação em profundidade
"""
class FronteiraLIFO(Fronteira):

    """
    Implementação do método inserir em modo LIFO
    """
    def inserir(self, no):
        self._nos.insert(0, no)