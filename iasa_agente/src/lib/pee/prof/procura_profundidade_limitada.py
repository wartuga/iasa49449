from pee.prof.procura_profundidade import ProcuraProfundidade

"""
é ótimo se encontrando a solução, é a melhor
é completo se havendo solução, encontra a solução

Alternativa é a procura em profundidade limitada
Problema: A profundidade a que se encontra a solução 
pode não ser conhecida

Descobrimos a profundidade, fazendo a procura aumentando
o limite da profundidade sucessão de procura em profundidade
limitada, aumentando o limite

Completo? sim
Ótimo? apenas se o nivel de profundidade for igual ao
nivel de profundidade da solução ou o ramo da solução seja
o primeiro a ser percorrido
"""
"""
Representação da procura em profundidade limitada
2º nivel de especializaçao ProcuraProfLim limita 
a ProcuraProfundidade, restringe a ProcuraProfundidade 
para explorar até ao limite
"""
class ProcuraProfLim(ProcuraProfundidade):
    """
    Construtor da classe
    """
    def __init__(self, prof_max = 500):
        super().__init__()
        self.__prof_max = prof_max
    
    # a propriedade escrita vem a seguir à de leitura
    @property
    def prof_max(self):
        return self.__prof_max

    @prof_max.setter
    def prof_max(self, value):
        self.__prof_max = value

    """
    apenas iremos expandir se a profundidade do nó
    for menor que a profundidade máxima
    senão retornar uma lista vazia
    """
    def _expandir(self, problema, no):
        if no.profundidade < self.__prof_max:
            return super()._expandir(problema, no)
        else:
            return []