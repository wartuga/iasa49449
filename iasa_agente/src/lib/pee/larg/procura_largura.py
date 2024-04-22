from pee.mec_proc.procura_grafo import ProcuraGrafo
from pee.larg.fronteira_fifo import FronteiraFIFO

"""
Procura em largura
1 + b + b^2 + b^3 + ... + b^d
Complexidade temporal: O(b^d)
complexidade espacial: O(b^d)
solução exponencial
ótimo? sim
completo? sim
"""
"""
Representação de uma procura em profundidade.
Especializando a class Procura Grado
com uma estrutura de dados FIFO
"""
class ProcuraLargura(ProcuraGrafo):
    def __init__(self):
        fronteira = FronteiraFIFO()
        super().__init__(fronteira)