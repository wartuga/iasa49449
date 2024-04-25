from pee.mec_proc.mecanismo_procura import MecanismoProcura

"""
Representação de uma procura em grafos.
Especializando a class Mecanismo de Procura
"""
class ProcuraGrafo(MecanismoProcura):

    """
    é preciso fazer o override do método uma vez
    que este não é abstrato
    """
    def _iniciar_memoria(self):
        super().__init__(self._fronteira)
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
