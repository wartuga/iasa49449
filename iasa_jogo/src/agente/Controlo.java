package agente;

/**
 * Controlo representa a parte do agente na qual é processada a percepção para o agente atuar.
 */
public interface Controlo {
    /**
     * processar é o método para retornar uma Acao consoante a Percepcao recebida.
     * @param percepcao - observação do ambiente.
     * @return Acao
     */
    Acao processar(Percepcao percepcao);
}
