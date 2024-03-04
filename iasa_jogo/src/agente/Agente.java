package agente;

import ambiente.Ambiente;
import ambiente.Comando;
import ambiente.Evento;

/**
 * Agente representa um agente inteligente que toma decisões/ações(output)
 * com base na sua percepção/visualização(input).
 */
/**
 * Class é a representação de "algo" físico ou virtual para o âmbito da programação.
 * Que possui atributos que representam as características desse "algo" e métodos que representam as suas ações.
 */
public class Agente {
    /**
     * ambiente serve para guardar o ambiente do momento da criação do agente
     * adquirida através de uma relação unidirecional
     */
    private Ambiente ambiente;
    /**
     * controlo serve para guardar o controlo do momento da criação do agente
     * adquirida através de uma relação de composição
     */
    private Controlo controlo;

    /**
     * Construtor da classe Agente.
     * @param ambiente - ambiente a ser percepcionado pelo agente.
     * @param controlo - parte do agente na qual é processada a percepção para o agente atuar.
     */
    public Agente(Ambiente ambiente, Controlo controlo){
        this.ambiente = ambiente;
        this.controlo = controlo;
    }

    /**
     * para a próxima aula
     */
    public void executar(){

    }

    /**
     * percepcionar é o método para o agente observar o ambiente e ter uma percepção do mesmo.
     * @return Percepcao
     */
    protected Percepcao percepcionar(){
        // variável explicativa
        Evento evento = ambiente.observar();
        return new Percepcao(evento);
    }

    /**
     * atuar é o método para o agente executar um comando com base na ação recebida.
     * @param acao - contém o comando a ser executado pelo agente no ambiente.
     */
    protected void atuar(Acao acao){
        if(acao != null){
            // variável explicativa
            Comando comando = acao.getComando();
            ambiente.executar(comando);
        }
    }
}