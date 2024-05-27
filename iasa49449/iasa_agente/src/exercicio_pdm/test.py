from exercicio_pdm.modelo_pdm_impl import ModeloPDMImpl
from pdm.pdm import PDM

# erro na utilidade do sn, não entendi o motivo
# erro na atualização da politica e da utilidade, má utilização do max

"""
dificuldade no debug do código

componente conceptual final
modelos de software ou modelos matemáticos que nos permitem implementar o código e, em caso de falha, 
identificar e corrigir o problema.
a chance de colocar a correr código complexo é muito baixa

como é que eles são gerados e o significado de cada um desses modelos possíveis de observar

Contexto geral

Estudo na implementação de sistemas que operam no contexto de um ambiente e tomam decisões complexas 
num ambiente incerto.
onde existe um futuro com múltiplas ramificações, não se sabe que estado se pretende atingir, porém 
pretende-se otimizar os ganhos estando presenta a incerteza

Processo de modelação para lidar com estes problemas

espaço de estados probabilisticos
onde as transições não são determinísticas
e.g. s0 pode transitar para o s2 com 80% ou para o s1 com 20%

Para a formalização do raciocínio é necessário conhecer o conjunto de estados, os possíveis estados, 
um modelo de transição(probabilidade de transitar para um estado s' a partir do estado s) e o modelo de recompensas

O cálculo é feito através do cálculo da utilidade
podem ser aditivas(não são influenciadas pelo tempo) ou descontadas(com o tempo é descontado devido à oportunidade)

obtenção dos valores de utilidade para os estados

politica, dado um estado indica qual o estado a seguir
probabilistica a politica da a probabilidade de ocorrer uma ação num determinado estado

política ótima

o principio da soluçao otima, deduzimos a utilidade de estado, com o valor esperado

o cálculo da politica ótima pi*
escolha do argumento ação que maximiza o valor de utilidade de estado

programação dinamica, resolução em sub problemas mais simples

podemos terminar as iterações no delta máx visto que a utilidade a partir de um certo número de iterações 
converge para um valor fixo

e.g.
ambiente 7x1
estados terminaris 1 e 7
+ - 7
- - 1
neutro - 2 a 6

S - {1,2,3,4,5,6,7}
A(s) - {E, D}
// assumindo que p = 1 => 1 - p = 0
// forma deterministica
T(s,a,s') - {T(1,E,1) = 0, T(1,D,2) = 0, T(2,E,1) = 1, T(2,D,3) = 1, T(3,E,2) = 1, T(3,D,4) = 1, T(4,E,3) = 1, T(4,D,5) = 1, T(5,E,4) = 1, T(5,D,6) = 1, T(6,E,5) = 1, T(6,D,7) = 1, T(7,E,6) = 0, T(7,D,7) = 0}
R(s,a,s') - {T(1,E,1) = 0, T(1,D,2) = 0, T(2,E,1) = -1, T(2,D,3) = 0, T(3,E,2) = 0, T(3,D,4) = 0, T(4,E,3) = 0, T(4,D,5) = 0, T(5,E,4) = 0, T(5,D,6) = 0, T(6,E,5) = 0, T(6,D,7) = 1, T(7,E,6) = 0, T(7,D,7) = 0}

Y = 0,5
U(s,a) = T(s,a,s')R(s,a,s') + yU(s')
U(s) = max(a, U(s,a))
Uação = 

utilidade = {-1;0,061;0,125;0,25;0,5;1;1}
U(1) = 0
U(2) = 0,063 = [T(2,E,1)R(2,E,1) + yU(1)] + [T(2,D,3)R(2,D,3) + y(U(3))] = (1*0+0) + (1*0+U(3)) = 0 + (0 + 0,5*0,125)
U(3) = 0,125 = [T(3,E,2)R(3,E,2) + yU(2)] + [T(3,D,4)R(3,D,4) + yU(4)] = (1*0+0) + (1*0 + 0,5*0,25)
U(4) = 0,25 = [T(4,E,3)R(4,E,3) + yU(3)] + [T(4,D,5)R(4,D,5) + yU(5)] = (1*0+0) + (1*0 + 0,5*0,5)
U(5) = 0,5 = [T(5,E,4)R(5,E,4) + yU(4)] + [T(5,D,6)R(5,D,6) + yU(6)] = (1*0+0) + (1*0 + 0,5*1)
U(6) = 1 = [T(6,E,5)R(6,E,5) + yU(5)] + [T(6,D,7)R(6,D,7) + yU(7)] = (1*0+0) + (1*1) + 0
U(7) = 1

pi*(2) = D
U(2,E) = -1
U(2,D) = 0,063

pi*(3) = D
U(3,E) = 0,031
U(3,D) = 0,125

pi*(4) = D
U(4,E) = 0,063
U(4,D) = 0,25

pi*(5) = D
U(5,E) = 0,125
U(5,D) = 0,5

pi*(6) = D
U(6,E) = 0,25
U(6,D) = 1

A utilidade para a E do estado s é a metade da utilidade do estado s' para a direita, uma vez que o desconto (y)
é igual a 0,5 e gastamos uma unidade de tempo, logo o resultado é calculado segundo yU(s', D), por exemplo para 
s = 6 => 0,5 * U(5, D) => 0,5 * 0,5 = 0,25
"""

modelo = ModeloPDMImpl()
pdm = PDM(modelo, 0.5, 0)

utilidade, politica = pdm.resolver()

print(utilidade)
print(politica)