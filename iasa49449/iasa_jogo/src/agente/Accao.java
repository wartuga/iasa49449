package agente;

import ambiente.Comando;

/**
 * Accao representa a ação a ser efetuada pelo agente.
 */
public class Accao {
    /**
     * comando é o comando a ser executado pelo agente sobre o ambiente.
     */
    private Comando comando;

    /**
     * Contrutor público de Accao
     * @param comando - comando a ser armazenado na Accao criada.
     */
    public Accao(Comando comando){
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
