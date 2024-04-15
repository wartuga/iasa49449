from dataclasses import dataclass
from mod.operador import Operador
from mod.estado import Estado

"""
Representa um passo da solução onde tem um estado
e o operador para mudar de estado
"""
@dataclass
class PassoSolucao:
    estado: Estado
    operador: Operador