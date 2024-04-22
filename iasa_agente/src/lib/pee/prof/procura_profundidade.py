from pee.mec_proc.mecanismo_procura import MecanismoProcura
from pee.prof.fronteira_lifo import FronteiraLIFO

"""
Procura em profundidade
complexidade temporal: O(b^d)
complexidade espacial: O(bd)
solução linear
ótimo? não
completo? não
"""
"""
Representação de uma procura em profundidade.
Especializando a class Mecanismo de Procura
com uma estrutura de dados LIFO
"""
class ProcuraProfundidade(MecanismoProcura):
    """
    Construtor da classe
    """
    def __init__(self):
        fronteira = FronteiraLIFO()
        super().__init__(fronteira)

    """
    M+etodo para inserir o no na estrutura de dados
    """
    def _memorizar(self, no):
        self._fronteira.inserir(no)