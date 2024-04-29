from .comportamento import Comportamento

"""
x => público
_x => protegido
__x => privado
from abc import ABC, abstractmethod

classe abstrata em python
class Estimulo(ABC):
"""

"""
Uma percepção é um agregado de estimulos e pode gerar múltiplas respostas
"""

"""
Existem três modelos para arquitetura de agentes reativos
Relativo, Deliberativo e Hibrido
Relativo - se, então; objetos implicitos
Deliberativo - capaz de prever o que acontece no futuro; objetos explicitos
    Consequência -> Exige maior capacidade computacional
Hibrido - contem o melhor dos dois mundos; objetos explicitos
    Consequência -> Maior complexidade
"""

"""
Representa a Reaccao de uma arquitetura de agentes reativos
A reação define uma associação de um estímulo a uma resposta
Implementa a interface Comportamento
"""
class Reaccao(Comportamento):
    """
    Construtor de Reaccao
    """
    def __init__(self, estimulo, resposta):
        self.__estimulo = estimulo
        self.__resposta = resposta
    
    """
    Método que verifica a intensidade da Percepcao recebida
    caso esta seja maior que '0' afeta o valor de prioridade
    da Accao e retorna-a, caso contrário retorna None
    """
    def activar(self, percepcao):
        intensidade = self.__estimulo.detectar(percepcao)
        if(intensidade > 0):
            """ variável explicativa => maior simplicidade """
            accao = self.__resposta.activar(percepcao, intensidade)
            return accao