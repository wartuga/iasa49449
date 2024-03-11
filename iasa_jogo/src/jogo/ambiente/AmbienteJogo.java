package jogo.ambiente;

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

import ambiente.Ambiente;
import ambiente.Comando;
import ambiente.Evento;

/**
 * Representa o ambiente do jogo
 */
public class AmbienteJogo implements Ambiente {

    /**
     * Guarda o evento atual do ambiente do jogo
     * Adquirida através de uma relação unidirecional
     */
    private EventoJogo evento;
    /**
     * Mapa para o mapeamento das teclas num determinado evento
     * fazendo assim a associação entre estes
     * Adquirida através de uma relação de composição unidirecional em que
     * para cada instância de AmbienteJogo existe uma ou mais entradas no mapa
     */
    private final Map<String, EventoJogo> eventos;
    /**
     * variável auxiliar para a leitura de inpput por parte
     * do utilizador
     */
    private Scanner scanner = new Scanner(System.in);

    public AmbienteJogo() {
        this.eventos = new HashMap<String,EventoJogo>();
        eventos.put("s", EventoJogo.SILENCIO);
        eventos.put("r", EventoJogo.RUIDO);
        eventos.put("a", EventoJogo.ANIMAL);
        eventos.put("f", EventoJogo.FUGA);
        eventos.put("o", EventoJogo.FOTOGRAFIA);
        eventos.put("t", EventoJogo.TERMINAR);
    }

    /**
     * getter de evento para o deixar público e read only
     * @return Evento
     */
    public Evento getEvento() {
        return this.evento;
    }

    /**
     * força a que esta função implementada em AmbienteJogo
     * respeite as regras da função evoluir da interface Ambiente
     * reduzindo assim a complexidade
     */
    @Override
    /**
     * Evoluir o estado do ambiente do jogo
     */
    public void evoluir() {
        evento = gerarEvento();
    }

    /**
     * Método que permite observar o ambiente do jogo
     */
    @Override
    public Evento observar() {
        /**
         * Com intuito de não explodir caso o evento seja null,
         * ou seja, caso o utilizador introduza uma tecla 
         * diferente das que estão registadas: (s,r,a,f,o,t)
         */
        if(evento != null){
            evento.mostrar();
        }else{
            System.out.printf("Sem evento\n");
        }
        return evento;
    }

    /**
     * Método para visualizar o comando sobre o ambiente do
     * jogo atual
     */
    @Override
    public void executar(Comando comando) {
        comando.mostrar();
    }
    
    /**
     * Método para gerar o próximo evento do ambiente do jogo
     * @return EventoJogo - Evento atual do ambiente do jogo
     */
    private EventoJogo gerarEvento() {
        System.out.printf("\nEvento? %s \n", eventos.keySet());
        String textoComando = scanner.next();
        return eventos.get(textoComando);
    }
}
