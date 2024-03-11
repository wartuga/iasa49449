package maqest;

import agente.Acao;

/**
 * Representa uma transição de uma máquina de estados
 */
public class Transicao {
    /**
     * Guarda o estado sucessor
     */
    private Estado estadoSucessor;
    /**
     * Guarda a açao consoante o estado sucessor
     */
    private Acao acao;

    /**
     * Construtor da Transição
     * @param estadoSucessor - define a função delta
     * @param acao - define a função lambda
     */
    Transicao(Estado estadoSucessor, Acao acao) {
        this.estadoSucessor = estadoSucessor;
        this.acao = acao;
    }

    /**
     * método para aceder ao estado seguinte da transição
     * @return
     */
    Estado getEstadoSucessor() {
        return estadoSucessor;
    }

    /**
     * método para aceder à ação da transição
     * @return
     */
    Acao getAcao() {
        return acao;
    }
}
