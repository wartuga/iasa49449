package ambiente;

/**
 * Ambiente representa um meio físico ou virtual, o qual se pode observar.
 * Permitindo-nos fazer associações a algo que seja do nosso conhecimento.
 * Neste caso terá evoluções de estado.
 * */
/**
 * Interface é um género de contrato realisado no âmbito de satisfazer uma ou mais necessidades.
 * Podendo ser implementada de formas diferentes mas sem mudar o objetivo ou sem quebrar o contrato.
 * */
public interface Ambiente {
    /**
     * evoluir é o método usado para fazer o ambiente mudar de estado.
     * */
    void evoluir();

    /**
     * observar é o método utilizado para observar o ambiente no estado atual.
     * @return Evento
     */
    Evento observar();

    /**
     * executar é o método usado para visualizar o comando executado sobre o ambiente.
     * @param comando - comando executado sobre o ambiente.
     */
    void executar(Comando comando);
}
