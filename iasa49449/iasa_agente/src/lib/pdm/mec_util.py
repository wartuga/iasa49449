"""
Representa o mecanismo de um processo de decisão de Markov (PDM).
Recebe um modelo, um gama e um delta máximo.
O modelo é o modeloPDM com os vários métodos (S, A, T, R, suc).
O gama é o fator de desconto.
O delta máximo é o valor máximo que o delta pode ter.
"""
class MecUtil:

    def __init__(self, modelo, gama, delta_max):
        self.__gama = gama
        self.__delta_max = delta_max
        self.__modelo = modelo
    
    """
    Método para calcular a utilidade de um estado,
    este retorna uma utilidade, chave é o estado e 
    o valor é a ação.

    Utilidade(valor)

	    Representa o valor de se estar num estado para efeitos de concretização
        de objetivos do sistema (valor de longo prazo).	

        O sistema reconhece ganhos e recompensas locais.(esta pode enganar)
        Não têm tanto impacto a longo prazo.

        É o efeito acumulado da evolução.
        h - história de evolução -> sequência de estados (com ganhos e perdas)
        R(s) - recompensa -> ganho ou perda no estado atual, valor finito

        Uh([s0,s1,...,sn]) -> simulação massiva das evoluções possíveis

    Calcular a utilidade para cada estado com as várias
    ações possíveis
    Delta = max(Delta, abs(U(s) - Uanterior(s)))
    enquanto Delta > delta_max
    retorna a utilidade
    """
    def utilidade(self):
        estados = self.__modelo.S()
        # Iniciar a utilidade a 0 em todos os elementos do conjunto de estados.
        utilidade = {estado: 0 for estado in estados}
        # aproximação do do-while com while True e break
        while True:
            # Guardar a utilidade anterior
            utilidade_anterior = utilidade.copy()
            # Inicializar o delta a 0
            delta = 0
            # Calcular a utilidade para cada estado
            for estado in estados:
                # Obter a ação para o estado
                accao = self.__modelo.A(estado)
                # Calcular a utilidade para o estado, sendo o máximo entre a ação e a utilidade da ação	
                utilidade[estado] = max(accao, self.util_accao(estado, accao, utilidade))
                # Calcular o delta sendo o máximo entre o delta e a diferença entre a utilidade do estado e a utilidade anterior do estado
                delta = max(delta, abs(utilidade[estado] - utilidade_anterior[estado]))
            # Se o delta for menor que o delta máximo, termina o ciclo
            if delta < self.__delta_max:
                break
        # Retorna a utilidade do estado
        return utilidade

    """
    Método para calcular a utilidade de uma ação,
    este retorna uma utilidade, chave é o estado e
    o valor é a ação.

    Valor esperado
	E(x) = somatório(i=0 a infinito) xi*p(xi)

	Cadeia de Markov (política: pi)
	r1^1 -> r2^1 -> r3^1
	
	U^pi(s)	= E(r1+yr2+y^2r3+...) // E(r1 + g*(r2 + g*r3 + ...)); r2 + g*r3 + ... utilidade do estado reguinte U(s') 
		= E(r1+yU(s'))

	1 - Selecionar uma ação
	2 - Ver o estado sucessor que foi gerado

	Transição de estado com base num modelo (politica pi(s,a))
	Probabilidade da transição
	T(s,a,s')
	s' € suc(s,a) contido ou igual a S

	Equações de Bellman (Utilidade com base num modelo)
	U^pi(s) = E(r1+yr2+y^2r3+...)
			= E(r1+yU^pi(s'))
			= somatório(a)pi(s,a)somatório(s')T(s,a,s')[R(s,a,s') + yU^pi(s')]
			somatório(a)pi(s,a) - prob. da ação ser escolhida 
            somatório(s')T(s,a,s') - prob. de transição para um estado s'
    """
    def util_accao(self, s, a, U):
        return sum([self.__modelo.T(s, a, sn) * (self.__modelo.R(s, a, sn) + self.__gama * U[sn]) for sn in self.__modelo.suc(s, a)])