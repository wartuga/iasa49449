package maqest;

import java.util.HashMap;
import java.util.Map;

import agente.Accao;
import ambiente.Evento;

/**
 * Representa o estado de uma máquina de estados
 * 
 */
public class Estado {
    /**
     * para guardar o nome do estado atual
     */
    private final String nome;
    /**
     * para guardar a associação de uma Transicao a um Evento
     * simplificando a máquina de estados
     */
    private Map<Evento,Transicao> transicoes;

    /**
     * construtor de um estado
     * @param nome
     */
    public Estado(String nome) {
        this.nome = nome;
        this.transicoes = new HashMap<Evento,Transicao>();
    }

    /**
     * getter do nome
     * @return
     */
    public String getNome() {
        return this.nome;
    }

    /**
     * Método para produzir uma Transicao
     * @param evento
     * @return Transicao
     */
    Transicao processar(Evento evento) {
        return transicoes.get(evento);
    }

    /**
     * Polimorfismo presente no método transição
     * Este realiza as funções delta(função de transição de estado) e lambda(função de saída)
     */
    /**
     * Adiciona às transições uma associação de um Evento a uma Transicao
     * @param evento
     * @param estadoSucessor
     * @return Estado - estado atual
     */
    public Estado transicao(Evento evento, Estado estadoSucessor) {
        return transicao(evento, estadoSucessor, null);
    }

    /**
     * Adiciona às transições uma associação de um Evento a uma Transicao
     * @param evento
     * @param estadoSucessor
     * @return Estado - estado atual
     */
    public Estado transicao(Evento evento, Estado estadoSucessor, Accao accao) {
        transicoes.put(evento, new Transicao(estadoSucessor, accao));
        return this;
    }
}
