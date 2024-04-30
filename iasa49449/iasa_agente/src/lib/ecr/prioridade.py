from .comport_comp import ComportComp

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
    # esquecimento do self da classe
    def selecionar_accao(self, accoes):
        """
        Para escolher a accao com a maior prioridade,
        pega-se na primeira ação e ao percorrer a 
        coleção, caso essa ação tenha uma prioridade
        maior, atualiza-se a accao escolhida para assim
        retornar a accao com a maior prioridade
        """
        if accoes:
            """ 
            Função de seleção da ação, onde escolhe a que tem 
            maior prioridade
            """
            criterio_selecao = lambda accao: accao.prioridade
            """ variável explicativa """
            accao = max(accoes, key = criterio_selecao)
            return accao