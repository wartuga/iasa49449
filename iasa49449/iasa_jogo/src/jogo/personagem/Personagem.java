package jogo.personagem;

import agente.Agente;
import jogo.ambiente.AmbienteJogo;

/**
 * Encontra-se uma generalização de Agente em Personagem
 * Uma vez que não acrescenta nada em termos de propriedades
 * ou métodos, podemos dizer que é uma fatorização por herança
 * onde Personagem é Agente num contexto de um Jogo
 * Isto provoca um alto acopolamento e fatorização estrutural
 */
/**
 * Existe ainda a fatorização por delegação onde B utiliza A
 * Por outro lado tem baixo acopolamento e fatorização funcional
 * Este acopolamento pode variar dinamicamente
 */
/**
 * Ambas contribuem para a decomposição ainda que de formas diferentes
 * Existe ainda outro ponto da modularização que é o encapsulamento
 * que consiste em fechar o interior do módulo, ou seja, isolar os
 * detalhes internos das partes de um sistema em relação ao exterior
 * As interfaces têm uma grande papel neste aspeto uma vez que são
 * contratos funcionais para interação com o exterior
 */
/**
 * Representa a Personagem de um jogo extendendo a classe
 * agente e herdando os seus métodos
 */
public class Personagem extends Agente {

    /**
     * Construtor de Personagem
     * @param ambiente - ambiente recebido pela personagem
     */
    public Personagem(AmbienteJogo ambiente) {
        super(ambiente, new ControloPersonagem());
    }
}
