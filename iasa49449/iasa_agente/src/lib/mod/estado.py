from abc import ABC, abstractmethod

"""
Representação de um estado.
"""
class Estado(ABC):
    """
    Redefinição do método hash para ser compatível dependendo
    da implementação do método id_value
    """
    def __hash__(self):
        return self.id_value()

    """
    Redefinição do método equals para possível comparação
    entre 2 instâncias de Estado
    """
    def __eq__(self, value):
        if(isinstance(value, Estado)):
            return self.__hash__() == value.__hash__()
    
    @abstractmethod
    def id_value(self):
        """
        Método a ser implementado para um domínio concreto.
        Retorna o id do estado.
        """