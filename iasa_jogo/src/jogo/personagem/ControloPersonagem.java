package jogo.personagem;

import agente.Acao;
import agente.Controlo;
import agente.Percepcao;
import ambiente.Evento;
import jogo.ambiente.ComandoJogo;
import jogo.ambiente.EventoJogo;
import maqest.Estado;
import maqest.MaquinaEstados;

/**
 * Representa o controlo da personagem onde é inicializada a máquina de estados
 * que possibilita esta ser um agente inteligente
 */
public class ControloPersonagem implements Controlo {
    /**
     * Guarda a máquina de estado inicializada no construtor
     * Neste caso é guardada uma máquina de Mealy pois a saída depende das entradas.
     * Possuí apenas 4 estados possíveis: 
     * Procura, Inspeçao, Observação, Registo
     */
    private MaquinaEstados maqEst;

    /**
     * getter do estado da MaquinaEstados para não ser possível a sua 
     * afetação a partir do exterior
     * @return
     */
    Estado getEstado(){
        return maqEst.getEstado();
    }

    ControloPersonagem() {
        /**
         * É possível representar o comportamento através de um fluxo de controlo
         * Partições de execução - Associar um comportamento a determinada parte do sistema
         * Neste caso o comportamente é representado através de uma Transicao e as partes 
         * são representadas por Estado
         */
        /**
         * As entradas deste sistema são os Eventos(Evento):
         * silêncio, ruido, animal, fuga, fotografia, terminar
         * As saídas são as Ações(Acao):
         * procurar, aproximar, observar, fotografar
         * Os estados são os Estados(Estado):
         * procura, inspeçao, observação, registo
         */
        /**
         * Instâncias de todos os estados possíveis
         */
        Estado procura = new Estado("Procura");
        Estado inspecao = new Estado("Inspeção");
        Estado observacao = new Estado("Observação");
        Estado registo = new Estado("Registo");

        /**
         * Instâncias de todas as ações possíveis
         */
        Acao procurar = new Acao(ComandoJogo.PROCURAR);
        Acao aproximar = new Acao(ComandoJogo.APROXIMAR);
        Acao observar = new Acao(ComandoJogo.OBSERVAR);
        Acao fotografar = new Acao(ComandoJogo.FOTOGRAFAR);

        /**
         * Carregamento de todas as possíveis transições para cada estado
         */
        procura
            .transicao(EventoJogo.ANIMAL, observacao, aproximar)
            .transicao(EventoJogo.RUIDO, inspecao, aproximar)
            .transicao(EventoJogo.SILENCIO, procura, procurar);

        inspecao
            .transicao(EventoJogo.ANIMAL, observacao, aproximar)
            .transicao(EventoJogo.RUIDO, inspecao, procurar)
            .transicao(EventoJogo.SILENCIO, procura);

        observacao
            .transicao(EventoJogo.FUGA, inspecao)
            .transicao(EventoJogo.ANIMAL, registo, observar);

        registo
            .transicao(EventoJogo.ANIMAL, registo, fotografar)
            .transicao(EventoJogo.FUGA, procura)
            .transicao(EventoJogo.FOTOGRAFIA, procura);

        // Inicialização maquina de estados
        this.maqEst = new MaquinaEstados(procura);
    }

    /**
     * Permite a personagem escolher a Acao segundo a Percepcao recebida
     * @return Acao
     */
    public Acao processar(Percepcao percepcao) {
        /**
         * Adquire-se o evento através da Percepcao recebida
         */
        Evento evento = percepcao.getEvento();
        /**
         * A Acao é resultado da máquina de estados processar o evento atual
         */
        Acao acao = maqEst.processar(evento);
        mostrar();
        return acao;
    }

    /**
     * Método para mostrar o estado da personagem
     */
    private void mostrar() {
        System.out.printf("Estado: %s\n", getEstado().getNome());
    }
}
