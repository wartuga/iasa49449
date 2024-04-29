from abc import ABC, abstractmethod

"""
2 tipos de procuras:
	nao informadas
		as que estudamos ate agr, profundidade, 
        largura, etc
	
	informadas
		procura de exploração seletiva do espaço 
        de estados
"""
"""
funções heuristicas possibilitam cálculos efetivos e 
por isso imprecisas (são estimativas rápidas mas 
possivelmente sem solução) não são robustas(não 
garantem soluções)

Representa a função heurística que é a representação
de uma estimativa do custo do percurso desde o nó até
ao objetivo final
Para definir uma heuristica admissivel precisamos de 
eliminar restrições do problema
e.g. não movimentação através de obstáculos
"""
class Heuristica(ABC):

    @abstractmethod
    def h(self, estado):
        """
        Método abstrato para produzir a distância
        heurística entre o objetivo final e o estado
        recebido
        """