from ecr.hierarquia import Hierarquia
from agente.controlo_react.reacoes.aproximar.aproximar_alvo import AproximarAlvo
from agente.controlo_react.reacoes.evitar.evitar_obst import EvitarObst
from agente.controlo_react.reacoes.explorar.explorar import Explorar

#parte do exercício em aula
#from agente.controlo_react.reacoes.contar_passos.contar_passos import ContarPassos

"""
Existem diferentes mecanismos de combinação e seleção de ações.
    Mecanismos de combinação
        Execução paralela de ações
            - Ações que não interferem entre si e.g. atuadores
        Prioridade de ações
            - Ações que interferem entre si, associar informação de
            prioridade a cada ação e.g. um obstaculo em frente, 
            virar à esquerda ou à direita?
        Combinação de ações
            - Diferentes ações são combinadas numa única ação 
            e.g. virar à direita + virar à esquerda => seguir em frente
    
    Seleção de ação
        Hierarquia
            Os comportamentos estão organizados numa hierarquia fixa
            de subsunção (supressão e substituição)
            e.g. recarregar bateria e aproximar alvo, varia a prioridade
            pois quando temos um estimulo recarregar bateria tem uma maior 
            prioridade pois aproximar do alvo pode ficar sem bateria
            e.g. evitar obstaculo e explorar, não se pode explorar sem evitar obstaculo
            Regras de prioridades fixas, uma reação de alta prioridade 
            substitui/suprime a reação de prioridade mais baixa
        
        Prioridade
            As respostas são selecionadas de acordo com uma prioridade associada que varia ao longo da execução
            Outro tipo de prioridade, associada a cada resposta temos uma prioridade
            Um mux recebe as várias respostas e escolhe a que tem maior prioridade
        
        Combinação
            ...

Agente Prospetor
    Objetivo
        Recolher alvos
	Sub-Objetivos
		Aproximar alvo
		Evitar obstáculos
		Explorar
"""
"""
Representa o recolher, sendo o objetivo principal
recolher os alvos no ambiente e possui sub-objetivos,
neste caso, AproximarAlvo, EvitarObst e Explorar, do
mais prioritário para o menos, respetivamente.
"""
class Recolher(Hierarquia):
    """
    Construtor da classe Recolher
    """
    def __init__(self):
        """
        parte do exercício em aula
        ContarPassos()
        """
        comportamentos = [AproximarAlvo(), EvitarObst(), Explorar()]
        super().__init__(comportamentos)