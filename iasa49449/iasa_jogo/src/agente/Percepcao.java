package agente;

import ambiente.Evento;

/**
 * Percepao representa o resultado de um evento do ambiente após percepcionar.
 */
public class Percepcao {
    /**
     * armazena o evento recebido no momento da criação de Percepcao
     */
    private Evento evento;

    /**
     * Contrutor público de Percepcao.
     * @param evento - resultado da observação do ambiente.
     */
    public Percepcao(Evento evento){
        this.evento = evento;
    }

    /**
     * permite que o evento seja lido pelo agente mas não modificado por ninguém de fora.
     * @return Evento
     */
    public Evento getEvento(){
        return this.evento;
    }
}
