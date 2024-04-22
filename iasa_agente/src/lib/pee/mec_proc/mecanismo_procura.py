from abc import ABC, abstractmethod
from pee.mec_proc.no import No
from pee.mec_proc.solucao import Solucao

"""
Representa o mecanismo de procura de um agente inteligente com memória
"""
class MecanismoProcura(ABC):
    """
    Construtor da classe
    """
    def __init__(self, fronteira) -> None:
        self._fronteira = fronteira

    """
    Método auxiliar à construção da estrutura de dados
    """
    def _iniciar_memoria(self):
        return self._fronteira.iniciar()
    
    """
    Método para adicionar o no à coleção de nós explorados
    """
    @abstractmethod
    def _memorizar(self, no):
        raise NotImplementedError
    
    """
    É o núcleo deste mecanismo, retorna a soluçáo caso esta exista
    """
    def procurar(self, problema):

        # inicializa a estrutura de dados utilizada
        self._iniciar_memoria()

        # guarda o nó inicial
        no = No(problema.estado_inicial)

        # adiciona o nó inicial à coleção
        self._memorizar(no)

        # enquando a fronteira não estiver vazia 
        # significa que ainda há nós para percorrer
        while not self._fronteira.vazia:

            # retorna e remove o primeiro nó da fronteira
            no = self._fronteira.remover()

            # caso o nó atual seja o objetivo retorna-se
            # a solução com esse nó
            if problema.objetivo(no.estado):
                return Solucao(no)
            
            # caso contrário expande-se o nó atual
            for no_sucessor in self._expandir(problema, no):

                # adicionando-se o seu sucessor à 
                # coleção para se iterar
                self._memorizar(no_sucessor)

        # em caso do problema não possuir solução
        return None
    
    """
    Método para fazer a expansão de cada nó
    """
    def _expandir(self, problema, no):
        # Inicialize-se a coleção vazia
        sucessores = list()

        # guarda-se o estado do nó
        estado = no.estado

        # percorre-se os operadores do problema
        for operador in problema.operadores:

            # guarda-se o estado do nó sucessor
            estado_suc = operador.aplicar(estado)

            # caso haja estado no nó sucessor faz-se o tratamento
            if estado_suc is not None:

                # é calculado o custo desse nó
                custo = no.custo + operador.custo(estado, estado_suc)

                # é então construida uma instância de nó com os dados atualizados
                no_sucessor = No(estado_suc, operador, no, custo)

                # adicionar o nó à coleção para se retornar
                sucessores.append(no_sucessor)
                
        return sucessores
    