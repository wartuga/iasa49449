from mod_prob.problema_contagem import ProblemaContagem
from pee.prof.procura_profundidade import ProcuraProfundidade
from pee.larg.procura_largura import ProcuraLargura
from pee.prof.procura_profundidade_limitada import ProcuraProfLim

VALOR_INICIAL = 0
VALOR_FINAL = 9
INCREMENTOS = [1,2]

# instância do problema
problema = ProblemaContagem(VALOR_INICIAL, VALOR_FINAL, INCREMENTOS)

# definição do mecanismo de procura para o problema
mec_proc = ProcuraProfLim()

# solução calculada pelo mecanismo no problema
solucao = mec_proc.procurar(problema)

# caso exista solução, mostra os passos efetuados
if solucao:
    print(solucao)
    for passo in solucao:
        print(passo.estado.valor, passo.operador.incremento)