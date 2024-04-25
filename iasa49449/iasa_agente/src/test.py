from sae import Simulador
from agente.agente_reativo import AgenteReativo as Agente


# Executar simulador da SAE
# recebe um numero e um agente
Simulador(1, Agente()).executar()