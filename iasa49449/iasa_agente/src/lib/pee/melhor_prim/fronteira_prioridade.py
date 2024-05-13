from pee.mec_proc.fronteira import Fronteira
from heapq import heappop, heappush

"""
estratégia de controlo
	explorar primeiro os nós com menor custo
		fronteira ordenada por custo associado a cada nó
		o primeiro é o melhor, logo é o que expandimos
		e.g. de representação de um nó "1:5" representa 
        o nó 1 com custo 5

consegue-se diminuir tempo com o aumento de complexidade 
(qualidade espaço-tempo)
se tivermos uma estrutura de dados que já tem o que 
necessitamos em vez de uma lista

priorityQueue - utilização como lista, implementação 
interna como árvores

lib heapq
metodos
heappush(heap, item)
heappop(heap)        
"""
"""
Representa a fronteira de prioridade necessária
para a lógica da procura melhor primeiro
uma vez que será envolvido o valor do custo
de cada operador
"""
class FronteiraPrioridade(Fronteira):
    """
    Construtor da classe
    Nota: avaliador vai ser protected (alterado em aula)
    """
    def __init__(self, avaliador):
        self._avaliador = avaliador
        # código desnecessário
        # super().__init__()

    """
    Método para inserir um nó na coleção
    da fronteira
    """
    def inserir(self, no):
        prioridade = self._avaliador.prioridade(no)
        heappush(self._nos, (prioridade, no))

    """
    Método para remover o nó com menor custo,
    sendo este o primeiro elemento da coleção
    """
    def remover(self):
        # não se faz o teste pois a fronteira nunca pode estar vazia
        _, no = heappop(self._nos)
        return no