from sae import Controlo
from .mec_delib import MecDelib
from .modelo.modelo_mundo import ModeloMundo

"""
Constraste com a arquitetura reativa 
	problema: esta produz soluções expeditas mas sub-ótimas
	não tem memória
	
temos como base os mecanismos automáticos, integrar estes no agente

O comportamento está relacionado com tempo, tem 3 horizontes, presente, passado e futuro
Podemos alargar os horizontes

apenas com presente - reage
passado-presente - repetir ou evitar com a informação do passado (evitar/repetido passado)
passado-presente-futuro - antecipar o futuro para ootimizar

este horizonte temporal reflete-se na memória, essas percepções podem ser designadas como memória sensorial

Sempre que faz este registo 

A memória(espaço lógico/espaço de trabalho) é o suporte à simulação do futuro

Memoria do passado - processo reativo(reagir conforme o passado)
Antecipação para atingir objetivos, deliberação, uso dos recursos cognitivos do sistema para atingir uma determinada situação específica.

Arquitetura Deliberativa

    ^----------------> percepcao ---------v-----------v
Ambiente                              memória    deliberação


não funciona sem memória, sendo esta o suporte da representação interna.
Processos deliberativos => raciocínio sobre as sequências de ações para alcançar um objetivo
saber como fazer

Resultado desses processos internos são planos (não reação direta do agente)

Quando se fala de deliberação, sistemas intencionais, operam por concretização de objetivos uso de recursos internos para atingir um objetivo.

Ao contrário do reativos, estes objetivos estão implicitos nas ações (e.g. recolher alvo)

Se o agente tem várias situações futuras que pretende atingir, terá de escolher uma.

Geração de objetivos(deliberar sobre o que fazer)

Deliberação => Raciocínio sobre os fins.

Existem os fins e os meios, os fins são os objetivos e os meios são as ações que permitem atingir os fins.

Deliberação e planeamento

Não se pode antecipar o futuro sem conhecimento, este pode vir da experiência do agente(agente que aprende sozinho) ou de algo que tem o conhecido e lhe transmite(modelo mundo/conhecimento do domínio do problema).

Estados que o agente pode observar.

Modelo 1 base para lhe dar essa informação(representação interna) que permite fazer simulações.

Se este sabe as coordenadas que pode passar, este faz a simulação de um caminho

Qualquer sistema que pretende ter objetivos necessita de lógica que o permita compreender isso (e.g. é bom tudo o que o aproxima do objetivo, é mau tudo o que o afaste).

Exploração de opções
	Racioncinio prospetivo
		Antecipação do que pode acontecer
	Simulação interna do domínio do problema
		Requer formas de representação interna do domínio do problema

Avaliação de opções
	Custo
		Recursos necessários
	Valor
		Ganho ou perda, medido em termos de utilidade

Raciocinio automático é um processo cognitivo que permite resolver um problema através da simulação interna do problema

que situações são possiveis atraves de determinadas opções

Minimizar a perda/custo

Maximizar o ganho é outra forma de raciocínio.

Raciocínio automático é divido em raciocínio prático e lógico

O teórico é orientado para a compreensão e explicação

O prático é orientado à ação, usa representações dos objetivos, ações e do mundo para obter como resultado planos de ação
	
Sobre os fins(deliberação)
	Pegar na representação interna e decidir o que fazer a partir das opções possíveis, tornam-se em objetivos

Sobre os meios(planeamento)
	Decidir como fazer (ações)
	Resulta em planos

No mundo real não se procura atingir soluções ótimas, apenas boas o suficiente.

A memória vai ser organizada internamente de forma a que seja adequeada a esse contexto

Processo da tomada de decisão e ação
	
	Observar (gerar percepções)para dar conhecimento ao sistema(em cada passo do agente)
	Atualizar com essas percepções
	Deliberar sobre as percepções atualizadas
	Planear para os objetivos gerados pela deliberação
	Executar o plano

Se já há planos, não é necessário planear, se já há deliberação, não é necessário deliberar

Problemas
	O mundo pode mudar dinamicamente(e.g. semáforo fechado -> abrir mas pedestre ainda a passar, logo o objetivo inicial de avançar ao abrir muda) => reconsiderar
	Recursos computacionais limitados

Processo atualizado
	Observar
	Atualizar
	se Reconsiderar
		Deliberar
		Planear
	Executar

Controlo Deliberativo
	Modelo do mundo ---> Mecanismo de deliberação
			 |
			 >-> Planeador
"""
"""
Representa o controlo deliberativo de um agente

processar devido ao controlo da sae
assimilar - atualizaçao da representação interna
considerar - para reconsiderar
deliberar - método que implementa os objetivos
planear - geração dos planos
executar - executar os planos
mostrar - mostra as informações internas

controlo_delib é composto por um modelo_mundo
"""

class ControloDelib(Controlo):
    """
    Construtor da classe
    """
    def __init__(self, planeador):
        self.__planeador = planeador
        self.__modelo_mundo  = ModeloMundo()
        self.__mec_delib = MecDelib(self.__modelo_mundo)
        self.__objetivos = None
        """
        adicionado devido à teoria
        """
        self.__plano = None

    """
    Processo de tomada de decisão
        Observar
        Atualizar
        se Reconsiderar
            Deliberar
            Planear
        Executar
    """
    def processar(self, percepcao):
        self.__assimiliar(percepcao)
        if self.__reconsiderar():
            self.__deliberar()
            self.__planear()
        self.__mostrar()
        return self.__executar()

    """
    método para atualizar a percepção do agente
    """
    def __assimiliar(self, percepcao):
        self.__modelo_mundo.actualizar(percepcao)

    """
    método para reconsiderar se não houver plano 
    ou caso o modelo do mundo tiver sofrido alterações
    """
    def __reconsiderar(self):
        return not self.__plano or self.__modelo_mundo.alterado

    """
    Método para efetuar a deliberação do agente
    atualizando assim os seus objetivos através
    do método deliberar do mecanismo deliberativo
    """
    def __deliberar(self):
        self.__objetivos = self.__mec_delib.deliberar()

    """
    Método para atualizar o plano do controlo 
    deliberativo do agente
    """
    def __planear(self):
        self.__plano = self.__planeador.planear(self.__modelo_mundo, self.__objetivos)

    """
    Método para executar um plano caso este exista
    """
    def __executar(self):
        """
        se existir plano vai executar a ação corrente
        do plano
        """
        if self.__plano:
            estado_agente = self.__modelo_mundo.obter_estado()
            operador = self.__plano.obter_accao(estado_agente)
            if operador:
                return operador.accao
            else:
                self.__plano = None

    """
    Método para visualizar as informações internas
    tanto do ambiente no qual o agente de encontra
    como o do plano guardado por este
    """
    def __mostrar(self):
        vista = self.vista
        # limpa a vista para não ficarem sobrepostas
        vista.limpar()
        # mostra o modelo do mundo atual na vista
        self.__modelo_mundo.mostrar(vista)
        # se houver plano mostra-o
        if self.__plano:
            self.__plano.mostrar(vista)
        # se houverem objetivos, estes serão marcados
        if self.__objetivos:
            for objetivo in self.__objetivos:
                self.vista.marcar_posicao(objetivo.posicao)