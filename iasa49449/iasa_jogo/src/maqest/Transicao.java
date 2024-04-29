package maqest;

import agente.Accao;

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
    private Accao accao;

    /**
     * Construtor da Transição
     * @param estadoSucessor - define a função delta
     * @param accao - define a função lambda
     */
    Transicao(Estado estadoSucessor, Accao accao) {
        this.estadoSucessor = estadoSucessor;
        this.accao = accao;
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
    Accao getAccao() {
        return accao;
    }
}
