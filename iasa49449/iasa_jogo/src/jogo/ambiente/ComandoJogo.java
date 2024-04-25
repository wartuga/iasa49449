package jogo.ambiente;

import ambiente.Comando;

/**
 * Contém todos os comandos possíveis do jogo
 */
public enum ComandoJogo implements Comando {
    PROCURAR,
    APROXIMAR,
    OBSERVAR,
    FOTOGRAFAR;

    /**
     * método utilizado para mostrar o comando a ser
     * executado no ambiente do jogo
     */
    @Override
    public void mostrar() {
        System.out.printf("Comando: %s", this);
    }
}
