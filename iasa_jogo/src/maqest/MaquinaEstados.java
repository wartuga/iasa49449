package maqest;

import agente.Acao;
import ambiente.Evento;

/**
 * Representa uma máquina de estado genérica
 */
public class MaquinaEstados {
    /**
     * guarda o estado atual da máquina de estados
     */
    private Estado estado;

    /**
     * getter do estado para não permitir a alteração
     * feita a partir do exterior
     * @return Estado
     */
    public Estado getEstado() {
        return estado;
    }

    /**
     * construtor da máquina de estados
     * @param estadoInicial
     */
    public MaquinaEstados(Estado estadoInicial) {
        this.estado = estadoInicial;
    }

    /**
     * Método para processar um Evento e gerar uma Acao
     * @param evento
     * @return Acao
     */
    public Acao processar(Evento evento) {
        /**
         * Produz uma transação através do estado atual processar o evento recebido
         */
        Transicao transicao = estado.processar(evento);
        if(transicao != null){
            /**
             * atualiza o estado atual com o estado sucessor presente na Transicao
             */
            estado = transicao.getEstadoSucessor();
            /**
             * Acao presente na Transicao
             * Variável explicativa
             */
            Acao acao = transicao.getAcao();
            return acao;
        }else{
            return null;
        }
    }
}
