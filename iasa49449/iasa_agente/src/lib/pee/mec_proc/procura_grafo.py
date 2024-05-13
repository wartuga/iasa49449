from .mecanismo_procura import MecanismoProcura

"""
Representação de uma procura em grafos.
Especializando a class Mecanismo de Procura

Procura em grafos com ciclos
	Estados repetidos na árvore de procura
		Grafo do espaço de estados apresenta ciclos
		Múltiplas transições para o mesmo estado
		Ações correspondentes às transições de estado são reversíveis

	Nós Abertos (Não explorados)
		Fronteira de exploração
	Nós Fechados (Explorados)
		noSuc ~€ Abertos && noSuc ~€ Fechados => inserir noSuc em Abertos
		noSuc € Abertos

	Memória de nós processados
		Nós gerados mas não expandidos
			Abertos		|
		Nós expandidos	| Explorados
			Fechados	|
"""
class ProcuraGrafo(MecanismoProcura):

    """
    é preciso fazer o override do método uma vez
    que este não é abstrato
    """
    def _iniciar_memoria(self):
        super()._iniciar_memoria()
        self._explorados = {}
    
    """
    Método para guardar o nó caso este seja para ser mantido
    """
    def _memorizar(self, no):
        estado = no.estado
        if self._manter(no):
            self._explorados[estado] = no
            self._fronteira.inserir(no)
    
    """
    Método para saber se um nó deve ser mantido
    """
    def _manter(self, no):
        return no.estado not in self._explorados
