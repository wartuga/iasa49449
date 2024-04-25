package agente;

import ambiente.Comando;

/**
 * Acao representa a ação a ser efetuada pelo agente.
 */
public class Acao {
    /**
     * comando é o comando a ser executado pelo agente sobre o ambiente.
     */
    private Comando comando;

    /**
     * Contrutor público de Acao
     * @param comando - comando a ser armazenado na Acao criada.
     */
    public Acao(Comando comando){
        this.comando = comando;
    }

    /**
     * permite que o comando seja lido pelo agente mas não modificado por ninguém de fora.
     * @return Comando
     */
    public Comando getComando() {
        return this.comando;
    }
}
