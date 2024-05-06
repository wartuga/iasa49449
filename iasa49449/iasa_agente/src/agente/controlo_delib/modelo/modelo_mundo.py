from sae import Direccao
from .estado_agente import EstadoAgente
from math import dist
from .operador_mover import OperadorMover
"""
Controlo Deliberativo
	Modelo do mundo ---> Mecanismo de deliberação
			 |
			 >-> Planeador

"""
"""
Informação necessária para a representação do ambiente
estado atual
conjunto de estados do mundo
conjunto de operadores
obter um elemento do mundo
calcular uma distancia a que o objetivo
atualizar o modelo com uma percepçao
mostrar as informações do modelo num painel
"""
"""
Representa a representação do ambiente para um agente
deliberativo.
"""
class ModeloMundo:
    """
    Construtor da classe
    """
    def __init__(self):
        self.__alterado = False
        self.__estado = None
        self.__estados = []
        self.__elementos = {}
        self.__operadores = []

    """
    Obtém o estado do agente
    """
    def obter_estado(self):
        return self.__estado

    """
    Obtém os estados visíveis para o agente
    """
    def obter_estados(self):
        return self.__estados

    """
    Obtém os operadores possíveis de aplicar ao agente
    em todas as direções
    """
    def obter_operadores(self):  
        return self.__operadores

    """
    Obtem o elemento na posição do estado recebido
    """
    def obter_elemento(self, estado):
        return self.__elementos[estado.posicao]

    """
    Obtém a distância entre dois estados recebidos
    """
    def distancia(self, estado):
        return dist(self.__estado, estado)

    """
    Atualiza as informações do modelo consoante a percepção recebida
    """
    def actualizar(self, percepcao):
        posicao = percepcao.posicao
        posicoes = percepcao.posicoes
        novo_estado = EstadoAgente(posicao)
        novos_estados = [EstadoAgente(pos) for pos in posicoes]
        novos_elementos = percepcao.elementos
        novos_operadores = [OperadorMover(self, direccao) for direccao in list(Direccao)]
        if self.__estado != novo_estado or self.__estados != novos_estados or self.__elementos != novos_elementos or self.__operadores != novos_operadores:
            self.__alterado = True
            self.__estado = novo_estado
            self.__estados = novos_estados
            self.__elementos = novos_elementos
            self.__operadores = novos_operadores
        else:
            self.__alterado = False

    def mostrar(self, vista):
        return NotImplementedError

    """
    Propriedade alterado do agente, representa se
    a última atualização alterou algo ou se manteve
    """
    @property
    def alterado(self):
        return self.__alterado
    
    """
    Propriedade dos elementos do agente, adquiridos
    através da percepção recebida no método actualizar
    """
    @property
    def elementos(self):
        return self.__elementos