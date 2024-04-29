from pee.mec_proc.mecanismo_procura import MecanismoProcura
from .fronteira_lifo import FronteiraLIFO

"""
Procura em profundidade
complexidade temporal: O(b^d)
complexidade espacial: O(bd)
solução linear
ótimo? não
completo? não
"""
"""
Após execução de contagem.py usando ProcuraProfundidade
o resultado apresentado é:
0 2
2 2
4 2
6 2
8 2
Custo da solução:  20
Dimensão da solução:  5
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