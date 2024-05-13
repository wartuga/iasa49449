from sae import Direccao, Elemento
from .estado_agente import EstadoAgente
from math import dist
from .operador_mover import OperadorMover
from plan.modelo.modelo_plan import ModeloPlan

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
O modeloMundo implementa modeloPlan para ser compativel com o pleaneador
"""
class ModeloMundo(ModeloPlan):
    """
    Construtor da classe
    """
    def __init__(self):
        self.__recolha = False
        self.__estado = None
        self.__estados = []
        self.__elementos = {}
        # os operadores serão sempre os mesmos para a mesma intância de ModeloMundo e as direções serão sempre quatro também 
        self.__operadores = [OperadorMover(self, direccao) for direccao in list(Direccao)]

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
        return self.__elementos.get(estado.posicao)

    """
    Obtém a distância entre dois estados recebidos
    """
    def distancia(self, estado):
        return dist(self.__estado.posicao, estado.posicao)

    """
    Atualiza as informações do modelo consoante a percepção recebida
    """
    def actualizar(self, percepcao):
        posicao = percepcao.posicao
        posicoes = percepcao.posicoes
        self.__estado = EstadoAgente(posicao)
        self.__estados = [EstadoAgente(pos) for pos in posicoes]
        self.__elementos = percepcao.elementos
        self.__recolha = percepcao.recolha

    """
    
    """
    def mostrar(self, vista):
        for posicao, elemento in self.__elementos.items():
            if elemento in [Elemento.ALVO, Elemento.OBSTACULO]:
                vista.mostrar_elemento(posicao, elemento)
        vista.marcar_posicao(self.__estado.posicao)

    """
    Propriedade alterado do agente, representa se
    a última atualização alterou algo ou se manteve
    """
    @property
    def alterado(self):
        return self.__recolha
    
    """
    Propriedade dos elementos do agente, adquiridos
    através da percepção recebida no método actualizar
    """
    @property
    def elementos(self):
        return self.__elementos