from ecr.comport_comp import ComportComp

"""
Representa o mecanismo de combinação e seleção de ações
baseado em prioridade, onde as respostas são selecionadas 
de acordo com uma prioridade associada que varia ao longo
da execução, sendo possivel associar uma prioridade a uma
resposta
"""
class Prioridade(ComportComp):
    """
    Método para selecionar uma ação de um conjunto de ações
    baseado em prioridade, ou seja, a ação com a maior
    prioridade associada
    """
    def selecionar_acao(acoes):
        """
        Para escolher a acao com a maior prioridade,
        pega-se na primeira ação e ao percorrer a 
        coleção, caso essa ação tenha uma prioridade
        maior, atualia-se a acao escolhida para assim
        retornar a acao com a maior prioridade
        """
        if acoes:
            """ 
            Função de seleção da ação, onde escolhe a que tem 
            maior prioridade
            """
            criterio_selecao = lambda acao: acao.prioriade
            """ variável explicativa """
            acao = max(acoes, key = criterio_selecao)
            return acao