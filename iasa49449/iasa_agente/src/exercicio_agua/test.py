from exercicio_agua.problema import Deposito
from pee.melhor_prim.procura_custo_unif import ProcuraCustoUnif

volume_inicial = 0
volume_final = 9
solucao = []

problema = Deposito(volume_inicial, volume_final)
custo_uniforme = ProcuraCustoUnif()
solucao = custo_uniforme.procurar(problema)

print(solucao)

"""
teoria da última aula

Decisão sequencial que o agente tem de 

num problema de decisao sequencial o agente está em estados e tem de efetuar decisões para ir para novos estados, as recompensas podem nao ser imediatas, a ação não é certa, 

o problema foi abordado de forma a incorporar o problema numa representação do mundo com processos de markov

precisamos de conhecer os estados do mundo
as ações em cada estado
que evoluções podem ocurrer
quais os ganhos e perdas ao longo do tempo

permitindo um espaço de estados não deterministico e dessa forma tomar decisões através da função de utilidade

quantos espaços de estados possui um automóvel, a direção tem quantos espaços angulares? 1000 ou 10000?

fatores de ramificação do problema

o mundo real é infinitamente complexo

conceito de racionalidade limitada, em vez de resolver o problema na sua totalidade, ou seja, atingir a sua solução ótima pretende atingir uma solução razoável simplificando os problemas.

os modelos de transição e os modelos de recompensa? incógnitas

daí a solução ser colocar o sistema a aprender por ele proprio



como evoluir o que temos estado a fazer

aprendizagem incremental com a experiência

se o sistema não tem informação, gera uma ação aleatória e analisa o estado, ganho e/ou perda

o sistema aprende se ganhar a capacidade de 
a memória é o grau mais baixo de inteligência

Aprendizagem != memorização

generalização
formação de abstrações
	protótipos
	conceitos
	padrôes comportamentais

O sistema aprende se o seu desempenho for melhorando a cada tarefa com a experiência adquirida

sistema artificial restrita ou clássica, 

na geral os sistemas conseguem um conhecimento alargado do mundo, ou seja, começa a desenvolver em diversos aspetos, introduzindo um nível de abrangência.

quando este aprende, na base da medida de desempenho, métrica de custo.

qualquer métrica de inteligência tem associada um métrica de desempenho
e.g. no xadrez é a quantidade de jogos ganhos

Aprendizagem por reforço

Aprendizagem a partir da interação com o ambiente
estado
ação
reforço (ganho/perda)

aprendizagem de comportamentos

o que fazer
relações entre situações e ações

o agente irá aprender políticas da seguinte forma:

aprendizagem de valor de ação
e.g.	escolha repetida de diferentes ações
	por cada ação é obtida uma recompensa (de acordo com uma distribuição de probabilidades)
	resultado depende só da ação escolhida

	A3 = 10 unidades
	A4 = -5 unidades
	A2 = 5 unidades
	A1 = 10 unidades
	A1 = 15 unidades
	A1 = 5 unidades
	A3 = 2 unidades
	A4 = -5 unidades
	A1 = 5 unidades
	A3 = -5000 unidades
	A1 = -1000 unidades
	A4 = 10000 unidades
	
Lei dos grandes números

	Se tentarmos o número de vezes suficientes irá convergir para o valor real
	

Motivação

	maximizar a recompensas

Aprendizagem de valor de ação
	
	Valor médio para uma ação a após n tentativas
	Cada tentativa produz uma recompensa 
	
	Estimação por acumulação não linear
	Qn(a) = Q(n-1)(a) + 1/n * [r(n)^alpha - Q(n-1)(a)]

	alpha € [0,1] - fator de aprendizagem (regula o valor aplicado valores mais recentes e mais antigos, quanto mais perto de 0, maior o valor do passado, quando a 1 apenas o presente tem peso, tornando-se num agente reativo)

	Em situações reais mudam com o tempo, ou seja, menos informação
	logo não é possível utilizar apenas o valor médio

	
Dilema Explorar / Aproveitar

	Aprendizagem por reforço
		explorar - para obter conhecimento
		aproveitar - para maximizar o valor

	Exploração
		Escolher 


	Apesar de existirem diversas técnicas, a que irá ser abordar é a greedy ou a Sôfrega, possui maus resultados a médios e longos prazos

	Estratégia sôfrega

		Escolher a melhor ação a* de acordo com a estimativa de atual valor de cada ação Qt(a)

		at = a*t = argmax a Qt(a)

	Estratégia €-greedy
			a*t com probabilidade 1 - €
		a1
			ação aleatória com probabilidade €

		€ entre [0,1] - fator de exploração

		Balanceamento de Exploração / Aproveitamento

		quando já tem bastante conhecimento, o € vai baixando até atingir o 0 e quando ainda não possui conhecimento nenhum, este deve ser 1

	Após atingir a solução ótima, deve-se baixar o epsilone €, caso contrário este gerará soluções não ótimas.


Aprendizagem associativa

	Estados observados
		s € S
	Ações realizadas
		a € A
	Reforços obtidos
		r € R

	Valor de num estado realizar uma ação
		Q(s,a) € R

	Valor de ação estimados

		Q'(s,a) = r + yQ(s',a')

	Estimativa de valor é formada através 

Aprendizagem por Diferença Temporal

Algoritmo SARSA (s -> a -> r -> s' -> a')

	Vai tentar resolver o problema várias vezes, cada uma dessas é designado episódio e uma transição é um passo na aprendizagem. (e.g. no jogo do galo, um episódio é um jogo completo e uma jogada é um passo de aprendizagem)


Q(s,a) = q

1 2 3
4 5 6
7 8 9

o x o
o o x
o o o

[o,x,o,o,o,x,o,o,o]

s	a	q
s0	a2	0
s3	a5	0
...	
s1	a2	-1
...

durante muito tempo as ações não geram recompensas

"""