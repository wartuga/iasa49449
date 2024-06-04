from mod.estado import Estado

class EstadoDeposito(Estado):

    def __init__(self, volume):
        self.__volume = volume

    def id_value(self):
        return self.__volume