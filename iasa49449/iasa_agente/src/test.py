from sae import Simulador
from agente.agente_reativo import AgenteReativo
from agente.agente_delib_pee import AgenteDelibPEE

# Executar simulador da SAE
# recebe um numero e um agente
Simulador(4, AgenteDelibPEE()).executar()