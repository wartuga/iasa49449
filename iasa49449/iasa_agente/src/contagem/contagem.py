from mod_prob.problema_contagem import ProblemaContagem
from mod_prob.heuristica_contagem import HeuristicaContagem
from pee.prof.procura_profundidade import ProcuraProfundidade
from pee.larg.procura_largura import ProcuraLargura
from pee.prof.procura_profundidade_limitada import ProcuraProfLim
from pee.melhor_prim.procura_custo_unif import ProcuraCustoUnif
from pee.melhor_prim.procura_aa import ProcuraAA
from pee.melhor_prim.procura_sofrega import ProcuraSofrega

VALOR_INICIAL = 0
VALOR_FINAL = 9
INCREMENTOS = [1,2]

# instância do problema
problema = ProblemaContagem(VALOR_INICIAL, VALOR_FINAL, INCREMENTOS)

heuristica = HeuristicaContagem(VALOR_FINAL)

# definição do mecanismo de procura para o problema
mec_proc = ProcuraSofrega()

# solução calculada pelo mecanismo no problema
solucao = mec_proc.procurar(problema, heuristica)

# caso exista solução, mostra os passos efetuados
if solucao:
    print(solucao)
    for passo in solucao:
        print(passo.estado.valor, passo.operador.incremento)
    print("Custo da solução: ", solucao.custo)
    print("Dimensão da solução: ", solucao.dimensao)