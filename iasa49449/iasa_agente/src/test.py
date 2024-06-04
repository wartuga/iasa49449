from sae import Simulador
from agente.agente_reativo import AgenteReativo
from agente.agente_delib_pee import AgenteDelibPEE
from agente.agente_delib_pdm import AgenteDelibPDM

# Executar simulador da SAE
# recebe um numero e um agente
Simulador(2, AgenteDelibPDM()).executar()