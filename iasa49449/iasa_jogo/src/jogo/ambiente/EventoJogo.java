package jogo.ambiente;

import ambiente.Evento;

/**
 * Contém todos os eventos possíveis do jogo
 */
public enum EventoJogo implements Evento {
    SILENCIO,
    RUIDO,
    ANIMAL,
    FUGA,
    FOTOGRAFIA,
    TERMINAR;

    /**
     * método utilizado para mostrar o evento do jogo
     */
    @Override
    public void mostrar() {
        System.out.printf("Evento: %s\n", this);
    }
}
// transformar a letra num evento
// é uma associação