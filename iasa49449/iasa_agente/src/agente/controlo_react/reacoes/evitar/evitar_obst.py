from ecr.hierarquia import Hierarquia
from agente.controlo_react.reacoes.evitar.resposta_evitar import RespostaEvitar
from agente.controlo_react.reacoes.evitar.evitar_dir import EvitarDir
from sae import Direccao

"""
Por possuir memória podemos ter comportamentos como o de "evitar o passado"
Neste tipo de comportamento, a reação não depende apenas da percepçáo, mas
também da memória.

Para isto é necessário ter manutenção de estado.
As vantagens são: 
    - ter a capacidade de produzir todo o tipo de comportamento
    - ter evoluçáo de estado ao longo do tempo
    - poder agir devido à ausência de memória
    - suporta situações de falha por meio da exploração de ações não 
    realizadas anteriormente

As desvantagens são:
    - necessidade de memória => necessidade de mais recursos
    - necessidade de manter as representações de estado => aumento de complexidade

Arquitetura de Subsunção

Resultado do comportamento pode ser a entrada de outro comportamento

Camadas superiores controlam as camadas inferiores => Hierarquia de camadas

Inibição
	Inibir as entradas
Supressão
	Suprimir as saídas
Reinício 
	Reset do estado interno
	

Definida por conjuntos de comporamentos
Comportamentos organizados em camadas (niveis de competência)
Desenvolvimento incremental
Robustas
Relativamente simples com um problema
	Facilmente se transforma numa teia (se for muito complexa)

Niveis de competência não mantém memória, os comportamentos sim
"""
"""
Representa a reação de evitar um obstaculo
É um sub-objetivo de Recolher
"""
class EvitarObst(Hierarquia):
    def __init__(self):
        self.__resposta = RespostaEvitar()

        """
        redução de complexidade ao construir a lista com as direções possíveis
        pois teria de se construir algum tipo de coleção para iterar sobre as direções
        """
        comportamentos = [EvitarDir(direcao, self.__resposta) for direcao in list(Direccao)]

        super().__init__(comportamentos)