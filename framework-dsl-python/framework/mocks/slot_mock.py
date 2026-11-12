from framework.core.slot import Slot

class SlotMock(Slot):
    def __init__(self):
        super().__init__()
        self.mensajesEscritos = []
        self.numLecturas = 0

    def escribirMensaje(self, mensaje):
        self.mensajesEscritos.append(mensaje)
        super().escribirMensaje(mensaje)

    def leerMensaje(self):
        self.numLecturas += 1
        return super().leerMensaje()

    def getEscritos(self):
        return self.mensajesEscritos

    def getNumLecturas(self):
        return self.numLecturas
