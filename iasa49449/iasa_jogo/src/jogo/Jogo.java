package jogo;

import jogo.ambiente.AmbienteJogo;
import jogo.ambiente.EventoJogo;
import jogo.personagem.Personagem;

/**
 * A divisão dos packages deste projeto é decidida conforme
 * a coerência e a relação dos ficheiros.
 * Por exemplo o package src.ambiente contém a interface de Ambiente
 * e as outras interfaces que têm dependência, ou seja, Evento e Comando
 * Neste projeto a coesão tem um carácter organizado
 */
/**
 * Para atingir o objetivo de concretizar as boas práticas estudadas
 * em aula segue-se um processo iterativo de:
 * arquitetura -> modelo -> implementação -> arquitetura -> ...
 * onde a arquitetura é a aquisição de conhecimento
 * o modelo é abordar o problema no nivel abstrato
 * e em termos de implementação, realiza-se a estrutural primeiro
 * e apenas após essa realização se concretizar, a implementação comportamental
 */
/**
 * A abstração, modularização e fatorização contribuem para um menor acopolamento
 * mas uma maior coesão e assim fazer uma gestão de complexidade
 * Relativamente à complexidade pode existir a redução e o controlo
 * onde a redução entende-se por eliminar a complexidade desorganizada e o
 * controlo por gerir a complexidade organizada, ou seja, dentro do que é 
 * realmente necessário fazer essa gestão ainda agora referida
 */
/**
 * Quando menor o acopolamento melhor pois é mais fácil de evoluir e desenvolver
 * pode ser medido de várias formas, como o grau de interdependências entre partes,
 * visibilidade das classes, as suas relações e niveis de acopolamento,
 * dependência(mais baixo), associação, agregação, composição, herança(mais alto)
 * e por fim a direção, pois as relações bi-direcionais contam a dobrar
 */
/**
 * Este jogo está dividido em 3 partições, ambiente, agente e controlo.
 * O ambiente pode observar e evoluir.
 * O agente pode percepcionar e actuar.
 * O controlo pode processar.
 */
/**
 * Representa o jogo onde uma personagem atua sobre um
 * ambiente gerando um evento
 */
public class Jogo {
    /**
     * adquirida através de uma relação de composição unidirecional
     */
    private static Personagem personagem;
    /**
     * adquirida através de uma relação de composição unidirecional
     */
    private static AmbienteJogo ambiente;

    /**
     * método main do Jogo
     * @param args
     */
    public static void main(String[] args){
        /**
         * Inicialização do ambiente para o jogo
         */
        ambiente = new AmbienteJogo();
        /**
         * Inicialização da personagem para o jogo
         */
        personagem = new Personagem(ambiente);
        executar();
    }

    /**
     * executar é privado pois reduz o acopolamento
     * e apenas é usado no main do Jogo no âmbito de
     * iniciar o jogo
     */
    private static void executar() {
        do {
            ambiente.evoluir();
            personagem.executar();
        } while(ambiente.getEvento() != EventoJogo.TERMINAR);
    }
}
