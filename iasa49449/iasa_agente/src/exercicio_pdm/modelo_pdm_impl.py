from pdm.modelo.modelo_pdm import ModeloPDM

# o erro era o 1 e o 7 estarem a 0 e nao a -1 e 1 respetivamente.

"""
Implementação do modelo de um processo de decisão de Markov (PDM)
de forma a formular o problema apresentado em aula.
O problema consiste num espaço de estados de 1 a 7
onde as ações possíveis são -1 e 1,
a função de transição é 1
"""

"""
minha solução
s = [1,2,3,4,5,6,7]
A = [-1, 1]
T = lambda s, a, sn: 1 if s != 1 and s != 7 else 0
R = lambda s, a, sn: -1 if s == 2 and a == -1 and sn == 1 else 1 if s == 6 and a == 1 and sn == 7 else 0
suc = [s + a[0], s + a[1]]
"""
class ModeloPDMImpl(ModeloPDM):
    def S(self):
        # alteração do ficheiro de teste diretamente aqui na fun
        return [1, 2, 3, 4, 5, 6, 7]
    
    def A(self, s):
        # alteração de -1 e 1 para < e >
        return ['<', '>'] if s not in [1, 7] else []
    
    def T(self, s, a, sn):
        # fiz o mesmo
        return 1 if s not in [1, 7] else 0
    
    def R(self, s, a, sn):
        return 1 if sn == 7 else -1 if sn == 1 else 0
    
    def suc(self, s, a):
        return [max(1, s - 1) if a == '<' else min(7, s + 1)]